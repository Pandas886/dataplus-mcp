#!/usr/bin/env python3
"""
Trino MCP Server - FastMCP Version
基于 FastMCP 的 Trino SQL 查询服务器，具有 Token 优化功能
"""

import os
import logging
from typing import Optional, List, Dict, Any

from fastmcp import FastMCP
from trino.dbapi import connect
# Trino exceptions are handled through generic Exception handling

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastMCP instance
mcp = FastMCP("trino-mcp")

# --- Configuration ---
TRINO_HOST = os.getenv("TRINO_HOST", "localhost")
TRINO_PORT = int(os.getenv("TRINO_PORT", 8080))
TRINO_USER = os.getenv("TRINO_USER", "mcp_agent")
TRINO_CATALOG = os.getenv("TRINO_CATALOG", None)
TRINO_SCHEMA = os.getenv("TRINO_SCHEMA", None)

# Token optimization settings
MAX_ROWS_DEFAULT = 20
MAX_CELL_LENGTH = 100
TRUNCATE_MARKER = "..."

def _get_trino_connection() -> connect:
    """Create and return a Trino connection."""
    config = {
        "host": TRINO_HOST,
        "port": TRINO_PORT,
        "user": TRINO_USER,
        "source": "mcp-trino-fastmcp"
    }

    if TRINO_CATALOG:
        config["catalog"] = TRINO_CATALOG
    if TRINO_SCHEMA:
        config["schema"] = TRINO_SCHEMA

    logger.info(f"Connecting to Trino: host={TRINO_HOST}, port={TRINO_PORT}, catalog={TRINO_CATALOG}, schema={TRINO_SCHEMA}")
    return connect(**config)

def _format_compact_result(cursor, max_rows: Optional[int] = None) -> Dict[str, Any]:
    """
    将查询结果格式化为紧凑的 Token 优化格式。
    返回字典格式，兼容 FastMCP 的 JSON 响应。
    """
    if not cursor.description:
        return {"columns": [], "rows": []}

    max_rows = max_rows or MAX_ROWS_DEFAULT

    # 获取列名
    columns = [desc[0] for desc in cursor.description]

    # 获取数据
    rows = cursor.fetchmany(max_rows + 1)

    if not rows:
        return {"columns": columns, "rows": []}

    # 处理行数据（限制行数并截断长字段）
    display_rows = rows[:max_rows]
    processed_rows = []

    for row in display_rows:
        processed_row = []
        for cell in row:
            if cell is None:
                processed_row.append("")
            else:
                cell_str = str(cell)
                # 截断过长的字段
                if len(cell_str) > MAX_CELL_LENGTH:
                    cell_str = cell_str[:MAX_CELL_LENGTH - len(TRUNCATE_MARKER)] + TRUNCATE_MARKER
                processed_row.append(cell_str)
        processed_rows.append(processed_row)

    # 只在数据被截断时添加消息
    if len(rows) > max_rows:
        message = f"Showing {len(processed_rows)} rows (truncated)"
    else:
        message = None

    result = {
        "columns": columns,
        "rows": processed_rows
    }

    # 只在有消息时才添加
    if message:
        result["message"] = message

    return result

def _validate_readonly_query(sql: str) -> bool:
    """验证查询是否为只读查询。"""
    sql_upper = sql.strip().upper()
    readonly_prefixes = ("SELECT", "SHOW", "DESCRIBE", "EXPLAIN", "WITH", "VALUES")
    return sql_upper.startswith(readonly_prefixes)

# --- MCP Tools ---

@mcp.tool()
def show_catalogs() -> List[str]:
    """列出所有可用的数据目录（包括预设配置）。"""
    try:
        conn = _get_trino_connection()
        cur = conn.cursor()
        cur.execute("SHOW CATALOGS")
        catalogs = [row[0] for row in cur.fetchall()]
        cur.close()
        conn.close()
        return catalogs
    except Exception as e:
        logger.error(f"Error showing catalogs: {str(e)}")
        raise Exception(f"Failed to list catalogs: {str(e)}")

@mcp.tool()
def inspect_schema(catalog: str, schema: Optional[str] = None) -> Dict[str, Any]:
    """查看目录/模式中的表信息。如果未指定 schema，则列出所有模式。"""
    try:
        conn = _get_trino_connection()
        cur = conn.cursor()

        if schema:
            cur.execute(f"SHOW TABLES FROM {catalog}.{schema}")
            tables = [row[0] for row in cur.fetchall()]
            result = {
                "catalog": catalog,
                "schema": schema,
                "tables": tables,
                "count": len(tables)
            }
        else:
            cur.execute(f"SHOW SCHEMAS FROM {catalog}")
            schemas = [row[0] for row in cur.fetchall()]
            result = {
                "catalog": catalog,
                "schemas": schemas,
                "count": len(schemas)
            }

        cur.close()
        conn.close()
        return result

    except Exception as e:
        logger.error(f"Error inspecting schema {catalog}.{schema}: {str(e)}")
        raise Exception(f"Failed to inspect schema: {str(e)}")

@mcp.tool()
def sql_query(sql: str, max_rows: Optional[int] = None) -> Dict[str, Any]:
    """执行只读 SQL 查询，返回 Token 优化格式的结果。"""
    try:
        # 安全检查
        if not _validate_readonly_query(sql):
            raise ValueError("Only read-only queries are allowed (SELECT, SHOW, DESCRIBE, EXPLAIN, WITH, VALUES)")

        logger.info(f"Executing query: {sql[:100]}...")

        conn = _get_trino_connection()
        cur = conn.cursor()
        cur.execute(sql)

        # 使用紧凑格式
        result = _format_compact_result(cur, max_rows)

        cur.close()
        conn.close()

        return result

    except Exception as e:
        logger.error(f"Error executing query: {str(e)}")
        raise Exception(f"Query execution failed: {str(e)}")

@mcp.tool()
def get_table_info(table: str) -> Dict[str, Any]:
    """获取表的列信息。格式：catalog.schema.table"""
    try:
        # 解析表名
        parts = table.split('.')
        if len(parts) < 2:
            raise ValueError("Table name must be in format: catalog.schema.table")

        catalog, schema = parts[0], parts[1]
        table_name = parts[2] if len(parts) > 2 else None

        conn = _get_trino_connection()
        cur = conn.cursor()

        if table_name:
            # 获取特定表的列信息
            cur.execute(f"DESCRIBE {catalog}.{schema}.{table_name}")
            columns = cur.fetchall()

            if columns:
                # 格式化列信息
                column_info = []
                for col in columns:
                    column_info.append({
                        "name": col[0],
                        "type": col[1],
                        "extra": col[2] if len(col) > 2 and col[2] else None
                    })

                result = {
                    "table": table,
                    "catalog": catalog,
                    "schema": schema,
                    "columns": column_info,
                    "column_count": len(column_info)
                }
            else:
                result = {
                    "table": table,
                    "error": "Table not found or no column information available"
                }
        else:
            # 显示模式中的所有表
            cur.execute(f"SHOW TABLES FROM {catalog}.{schema}")
            tables = [row[0] for row in cur.fetchall()]
            result = {
                "catalog": catalog,
                "schema": schema,
                "tables": tables,
                "table_count": len(tables)
            }

        cur.close()
        conn.close()
        return result

    except Exception as e:
        logger.error(f"Error getting table info for {table}: {str(e)}")
        raise Exception(f"Failed to get table info: {str(e)}")

@mcp.tool()
def preview_table(table: str, limit: int = 20) -> Dict[str, Any]:
    """预览表数据（前 N 行）。格式：catalog.schema.table"""
    try:
        # 解析表名
        parts = table.split('.')
        if len(parts) < 3:
            raise ValueError("Table name must be in format: catalog.schema.table")

        catalog, schema, table_name = parts

        # 构建 SELECT 查询
        query = f"SELECT * FROM {catalog}.{schema}.{table_name} LIMIT {limit}"

        # 使用 sql_query 执行
        result = sql_query(query, limit)

        return result

    except Exception as e:
        logger.error(f"Error previewing table {table}: {str(e)}")
        raise Exception(f"Failed to preview table: {str(e)}")

@mcp.tool()
def get_connection_info() -> Dict[str, Any]:
    """获取当前 Trino 连接信息。"""
    return {
        "host": TRINO_HOST,
        "port": TRINO_PORT,
        "user": TRINO_USER,
        "catalog": TRINO_CATALOG,
        "schema": TRINO_SCHEMA,
        "source": "mcp-trino-fastmcp"
    }

def main():
    """Main entry point for the MCP server."""
    # 从环境变量获取主机和端口
    host = os.getenv("MCP_HOST", "0.0.0.0")
    port = int(os.getenv("MCP_PORT", 8658))

    logger.info(f"Starting Trino FastMCP Server")
    logger.info(f"Server will be available at http://{host}:{port}")
    logger.info(f"Trino connection: {TRINO_HOST}:{TRINO_PORT}")

    import uvicorn
    # 直接使用 uvicorn 运行 SSE 应用
    from fastmcp.server.http import create_sse_app
    app = create_sse_app(mcp, message_path="/messages", sse_path="/sse")
    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    main()