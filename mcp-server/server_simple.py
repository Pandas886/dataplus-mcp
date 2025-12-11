#!/usr/bin/env python3
"""
Trino MCP Server - Simple HTTP API Version

This server provides HTTP API interface for Trino queries
with aggressive token optimization for efficient LLM consumption.
"""

import os
import sys
import logging
import uvicorn
from typing import Optional, List, Dict, Any
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from mcp.server import Server
from mcp.types import Tool, TextContent
from trino.dbapi import connect
from pydantic import BaseModel

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(title="Trino MCP Server", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# Initialize MCP server for tool definitions
app_server = Server("trino-mcp-optimized", version="1.0.0")

# Trino connection configuration
TRINO_CONFIG = {
    "host": os.getenv("TRINO_HOST", "trino"),
    "port": int(os.getenv("TRINO_PORT", 8080)),
    "user": os.getenv("TRINO_USER", "mcp_agent"),
    "catalog": os.getenv("TRINO_CATALOG", None),
    "schema": os.getenv("TRINO_SCHEMA", None),
    "http_scheme": "http",
    "source": "mcp-trino-http"
}

# --- Token Optimization Configuration ---
MAX_ROWS_DEFAULT = 20
MAX_CELL_LENGTH = 100
TRUNCATE_MARKER = "..."

# Request/Response models
class ToolRequest(BaseModel):
    name: str
    arguments: Dict[str, Any] = {}

class ToolResponse(BaseModel):
    content: List[Dict[str, Any]]
    isError: bool = False

def format_compact_result(cursor, max_rows: Optional[int] = None) -> str:
    """
    Format SQL results in ultra-compact format to minimize token usage.
    """
    if not cursor.description:
        return "Query executed. No results returned."

    max_rows = max_rows or MAX_ROWS_DEFAULT

    # Get column names
    columns = [desc[0] for desc in cursor.description]
    col_str = " | ".join(columns)

    # Fetch data efficiently
    rows = cursor.fetchmany(max_rows + 1)

    if not rows:
        return f"Cols: {col_str}\n(No rows returned)"

    lines = [f"Cols: {col_str}"]

    # Process rows (handle truncation)
    display_rows = rows[:max_rows]
    for row in display_rows:
        cleaned_cells = []
        for cell in row:
            if cell is None:
                cleaned_cells.append("")
            else:
                cell_str = str(cell)
                if len(cell_str) > MAX_CELL_LENGTH:
                    cell_str = cell_str[:MAX_CELL_LENGTH - len(TRUNCATE_MARKER)] + TRUNCATE_MARKER
                cleaned_cells.append(cell_str)
        lines.append(" | ".join(cleaned_cells))

    # Add note if data was truncated
    if len(rows) > max_rows:
        lines.append(f"\n(Note: Output truncated at {max_rows} rows. Use LIMIT clause for pagination)")

    return "\n".join(lines)

def validate_readonly_query(sql: str) -> bool:
    """
    Ensure query is read-only to prevent accidental data modification.
    """
    sql_upper = sql.strip().upper()
    readonly_prefixes = ("SELECT", "SHOW", "DESCRIBE", "EXPLAIN", "WITH", "VALUES")
    return sql_upper.startswith(readonly_prefixes)

# --- MCP Tool Definitions ---
@app_server.list_tools()
async def list_tools() -> List[Tool]:
    """Return available MCP tools."""
    return [
        Tool(
            name="show_catalogs",
            description="List all available data catalogs (including preset configurations)",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        ),
        Tool(
            name="inspect_schema",
            description="Get tables in a catalog/schema. catalog: required, schema: optional",
            inputSchema={
                "type": "object",
                "properties": {
                    "catalog": {"type": "string", "description": "Catalog name (required)"},
                    "schema": {"type": "string", "description": "Schema name (optional)"}
                },
                "required": ["catalog"]
            }
        ),
        Tool(
            name="sql_query",
            description="Execute READ-ONLY SQL queries. Returns token-optimized format.",
            inputSchema={
                "type": "object",
                "properties": {
                    "sql": {"type": "string", "description": "SQL query to execute"},
                    "max_rows": {"type": "integer", "description": f"Maximum rows to return (default: {MAX_ROWS_DEFAULT})"}
                },
                "required": ["sql"]
            }
        ),
        Tool(
            name="get_table_info",
            description="Get column information for a specific table. Format: catalog.schema.table",
            inputSchema={
                "type": "object",
                "properties": {
                    "table": {"type": "string", "description": "Full table name: catalog.schema.table"}
                },
                "required": ["table"]
            }
        )
    ]

async def execute_tool(name: str, arguments: dict) -> List[TextContent]:
    """Execute MCP tool calls."""
    try:
        # Establish Trino connection
        logger.info(f"Connecting to Trino: {TRINO_CONFIG}")
        conn = connect(**TRINO_CONFIG)
        cur = conn.cursor()

        if name == "show_catalogs":
            cur.execute("SHOW CATALOGS")
            catalogs = [row[0] for row in cur.fetchall()]
            result = f"Available catalogs: {', '.join(catalogs)}"
            return [TextContent(type="text", text=result)]

        elif name == "inspect_schema":
            catalog = arguments["catalog"]
            schema = arguments.get("schema")

            if schema:
                cur.execute(f"SHOW TABLES FROM {catalog}.{schema}")
                tables = [row[0] for row in cur.fetchall()]
                result = f"Tables in {catalog}.{schema}: {', '.join(tables) if tables else '(No tables)'}"
            else:
                cur.execute(f"SHOW SCHEMAS FROM {catalog}")
                schemas = [row[0] for row in cur.fetchall()]
                result = f"Schemas in {catalog}: {', '.join(schemas)}"

            return [TextContent(type="text", text=result)]

        elif name == "sql_query":
            sql = arguments["sql"]
            max_rows = arguments.get("max_rows")

            # Security check - only allow read-only queries
            if not validate_readonly_query(sql):
                return [TextContent(
                    type="text",
                    text="Error: Only read-only queries are allowed (SELECT, SHOW, DESCRIBE, EXPLAIN, WITH, VALUES)"
                )]

            logger.info(f"Executing query: {sql[:100]}...")
            cur.execute(sql)

            # Format results in token-optimized way
            result = format_compact_result(cur, max_rows)
            return [TextContent(type="text", text=result)]

        elif name == "get_table_info":
            table_name = arguments["table"]

            # Parse table name to get catalog and schema
            parts = table_name.split('.')
            if len(parts) < 2:
                return [TextContent(
                    type="text",
                    text="Error: Table name must be in format: catalog.schema.table"
                )]

            catalog, schema = parts[0], parts[1]
            table = parts[2] if len(parts) > 2 else None

            if table:
                # Get column information for specific table
                try:
                    cur.execute(f"DESCRIBE {catalog}.{schema}.{table}")
                    columns = cur.fetchall()

                    if columns:
                        # Format column info compactly
                        lines = [f"Columns in {table_name}:"]
                        for col in columns:
                            col_name = col[0]
                            col_type = col[1]
                            extra_info = col[2] if col[2] else ""
                            lines.append(f"{col_name} | {col_type} | {extra_info}")
                        result = "\n".join(lines)
                    else:
                        result = f"Table {table_name} not found or no column information available."

                except Exception as e:
                    result = f"Error getting table info: {str(e)}"
            else:
                # Show all tables in schema
                cur.execute(f"SHOW TABLES FROM {catalog}.{schema}")
                tables = [row[0] for row in cur.fetchall()]
                result = f"Tables in {catalog}.{schema}: {', '.join(tables) if tables else '(No tables)'}"

            return [TextContent(type="text", text=result)]

    except Exception as e:
        logger.error(f"Error executing tool {name}: {str(e)}")
        return [TextContent(type="text", text=f"Error: {str(e)}")]

    return [TextContent(type="text", text=f"Unknown tool: {name}")]

# --- HTTP API Endpoints ---
@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "OK"}

@app.get("/tools")
async def get_tools():
    """Get list of available tools."""
    tools = await list_tools()
    return {"tools": [tool.model_dump() for tool in tools]}

@app.post("/tools/call")
async def call_tool(request: ToolRequest):
    """Execute a tool call."""
    try:
        result = await execute_tool(request.name, request.arguments)
        return ToolResponse(
            content=[{"type": content.type, "text": content.text} for content in result],
            isError=False
        )
    except Exception as e:
        logger.error(f"Error calling tool {request.name}: {str(e)}")
        return ToolResponse(
            content=[{"type": "text", "text": f"Error: {str(e)}"}],
            isError=True
        )

@app.get("/")
async def root():
    """Root endpoint with server info."""
    return {
        "name": "Trino MCP Server",
        "version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "tools": "/tools",
            "call_tool": "/tools/call"
        }
    }

def main():
    """Main entry point."""
    port = int(os.getenv("MCP_PORT", 8656))
    host = os.getenv("MCP_HOST", "0.0.0.0")

    logger.info(f"Starting Trino MCP Server on {host}:{port}")
    logger.info(f"Trino config: {TRINO_CONFIG}")

    # Run with uvicorn
    uvicorn.run(app, host=host, port=port, log_level="info")

if __name__ == "__main__":
    main()