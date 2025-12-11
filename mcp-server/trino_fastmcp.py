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

        # 直接执行查询，而不是调用 sql_query 函数
        conn = _get_trino_connection()
        cur = conn.cursor()
        cur.execute(query)

        # 使用紧凑格式
        result = _format_compact_result(cur, limit)

        cur.close()
        conn.close()

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

@mcp.tool()
def list_connectors() -> Dict[str, Any]:
    """获取 Trino 中可用的连接器列表和说明。

    Returns:
        连接器信息字典，包含连接器名称和描述
    """
    # Trino 内置的常用连接器
    connectors = {
        "memory": {
            "description": "内存连接器，用于测试和临时数据存储",
            "example_properties": {
                "memory.max-data-per-node": "128MB"
            }
        },
        "tpch": {
            "description": "TPC-H 基准测试连接器，提供标准测试数据集",
            "example_properties": {}
        },
        "tpcds": {
            "description": "TPC-DS 基准测试连接器，提供决策支持测试数据集",
            "example_properties": {}
        },
        "hive": {
            "description": "Hive 连接器，用于查询 Hadoop 生态系统的数据",
            "example_properties": {
                "hive.metastore.uri": "thrift://localhost:9083",
                "hive.s3.endpoint": "http://localhost:9000",
                "hive.s3.aws-access-key": "${ENV:AWS_ACCESS_KEY}",
                "hive.s3.aws-secret-key": "${ENV:AWS_SECRET_KEY}"
            }
        },
        "postgresql": {
            "description": "PostgreSQL 连接器，用于连接 PostgreSQL 数据库",
            "example_properties": {
                "connection-url": "jdbc:postgresql://localhost:5432/database",
                "connection-user": "${ENV:POSTGRES_USER}",
                "connection-password": "${ENV:POSTGRES_PASSWORD}",
                "case-insensitive-name-matching": "true"
            }
        },
        "mysql": {
            "description": "MySQL 连接器，用于连接 MySQL 数据库",
            "example_properties": {
                "connection-url": "jdbc:mysql://localhost:3306/database",
                "connection-user": "${ENV:MYSQL_USER}",
                "connection-password": "${ENV:MYSQL_PASSWORD}"
            }
        },
        "iceberg": {
            "description": "Iceberg 连接器，用于查询 Iceberg 表格式的数据湖",
            "example_properties": {
                "iceberg.catalog.type": "rest",
                "iceberg.rest-catalog.uri": "http://localhost:8181"
            }
        },
        "delta": {
            "description": "Delta Lake 连接器，用于查询 Delta Lake 表格式的数据",
            "example_properties": {
                "hive.metastore.uri": "thrift://localhost:9083"
            }
        },
        "mongodb": {
            "description": "MongoDB 连接器，用于连接 MongoDB 数据库",
            "example_properties": {
                "mongodb.seeds": "localhost:27017",
                "connection-url": "mongodb://localhost:27017/database"
            }
        },
        "kafka": {
            "description": "Kafka 连接器，用于查询 Kafka 消息流",
            "example_properties": {
                "kafka.bootstrap.servers": "localhost:9092",
                "kafka.table-names": "topic1,topic2"
            }
        },
        "elasticsearch": {
            "description": "Elasticsearch 连接器，用于查询 Elasticsearch 索引",
            "example_properties": {
                "elasticsearch.host": "localhost",
                "elasticsearch.port": "9200",
                "elasticsearch.default-schema": "default"
            }
        },
        "redis": {
            "description": "Redis 连接器，用于连接 Redis 数据库",
            "example_properties": {
                "redis.host": "localhost",
                "redis.port": "6379",
                "redis.password": "${ENV:REDIS_PASSWORD}"
            }
        }
    }

    return {
        "connectors": connectors,
        "note": "实际可用的连接器取决于 Trino 部署配置",
        "usage_tips": [
            "使用 ${ENV:VAR_NAME} 语法引用环境变量，提高安全性",
            "属性名包含特殊字符时需要用双引号包围",
            "所有属性值都需要用单引号包围"
        ]
    }

@mcp.tool()
def create_catalog(catalog_name: str, connector: str, properties: Dict[str, Any]) -> Dict[str, Any]:
    """动态创建新的 catalog。

    Args:
        catalog_name: catalog 名称
        connector: 连接器类型（如 'hive', 'postgresql', 'mysql', 'memory' 等）
        properties: 连接器属性字典。支持环境变量引用，如 {"connection-password": "${ENV:DB_PASSWORD}"}

    Returns:
        操作结果信息

    Examples:
        创建 Memory catalog:
        create_catalog("memory_test", "memory", {"memory.max-data-per-node": "128MB"})

        创建 PostgreSQL catalog（使用环境变量）:
        create_catalog("pg_test", "postgresql", {
            "connection-url": "jdbc:postgresql://localhost:5432/mydb",
            "connection-user": "${ENV:POSTGRES_USER}",
            "connection-password": "${ENV:POSTGRES_PASSWORD}"
        })
    """
    try:
        # 验证 catalog 名称
        if not catalog_name or not catalog_name.replace('_', '').replace('-', '').isalnum():
            raise ValueError("Catalog name must be alphanumeric and can contain underscores and hyphens")

        # 验证 connector 名称
        if not connector or not connector.isalnum():
            raise ValueError("Connector must be alphanumeric")

        # 构建 SQL 语句，使用 USING 语法
        # 正确处理属性名和值，特别是包含特殊字符的情况
        props_list = []
        for key, value in properties.items():
            # 属性名如果包含特殊字符，需要用双引号
            # 连字符需要特别处理，因为它在 SQL 标识符中是特殊字符
            if '-' in key or '.' in key or not key.replace('_', '').isalnum():
                prop_name = f'"{key}"'
            else:
                prop_name = key
            # 属性值始终用单引号包围，并转义单引号
            escaped_value = str(value).replace("'", "''")
            prop_value = f"'{escaped_value}'"
            props_list.append(f"{prop_name} = {prop_value}")

        sql = f"CREATE CATALOG IF NOT EXISTS {catalog_name} USING {connector} WITH ({', '.join(props_list)})"

        logger.info(f"Creating catalog: {sql}")

        conn = _get_trino_connection()
        cur = conn.cursor()
        cur.execute(sql)

        # 验证 catalog 是否创建成功
        cur.execute("SHOW CATALOGS")
        catalogs = [row[0] for row in cur.fetchall()]

        cur.close()
        conn.close()

        if catalog_name in catalogs:
            # 获取创建的 catalog 信息
            catalog_info = get_catalog_properties(catalog_name)

            return {
                "success": True,
                "catalog_name": catalog_name,
                "connector": connector,
                "message": f"Catalog '{catalog_name}' created successfully",
                "properties": properties,
                "catalog_info": catalog_info
            }
        else:
            return {
                "success": False,
                "catalog_name": catalog_name,
                "connector": connector,
                "message": f"Failed to create catalog '{catalog_name}' - please check connector configuration and properties",
                "properties": properties
            }

    except ValueError as ve:
        logger.error(f"Validation error creating catalog {catalog_name}: {str(ve)}")
        return {
            "success": False,
            "catalog_name": catalog_name,
            "error_type": "validation",
            "message": f"Validation error: {str(ve)}"
        }
    except Exception as e:
        logger.error(f"Error creating catalog {catalog_name}: {str(e)}")
        return {
            "success": False,
            "catalog_name": catalog_name,
            "error_type": "execution",
            "message": f"Error creating catalog: {str(e)}",
            "suggestion": "Please check: 1) Connector is available in Trino 2) Properties are correct 3) Environment variables are set"
        }

@mcp.tool()
def drop_catalog(catalog_name: str) -> Dict[str, Any]:
    """删除指定的 catalog。

    Args:
        catalog_name: 要删除的 catalog 名称

    Returns:
        操作结果信息
    """
    try:
        # 检查 catalog 是否存在
        conn = _get_trino_connection()
        cur = conn.cursor()
        cur.execute("SHOW CATALOGS")
        catalogs = [row[0] for row in cur.fetchall()]

        if catalog_name not in catalogs:
            cur.close()
            conn.close()
            return {
                "success": False,
                "catalog_name": catalog_name,
                "message": f"Catalog '{catalog_name}' does not exist"
            }

        # 执行删除操作
        sql = f"DROP CATALOG IF EXISTS {catalog_name}"
        logger.info(f"Dropping catalog: {sql}")

        cur.execute(sql)

        # 验证删除是否成功
        cur.execute("SHOW CATALOGS")
        updated_catalogs = [row[0] for row in cur.fetchall()]

        cur.close()
        conn.close()

        if catalog_name not in updated_catalogs:
            return {
                "success": True,
                "catalog_name": catalog_name,
                "message": f"Catalog '{catalog_name}' dropped successfully"
            }
        else:
            return {
                "success": False,
                "catalog_name": catalog_name,
                "message": f"Failed to drop catalog '{catalog_name}'"
            }

    except Exception as e:
        logger.error(f"Error dropping catalog {catalog_name}: {str(e)}")
        return {
            "success": False,
            "catalog_name": catalog_name,
            "message": f"Error dropping catalog: {str(e)}"
        }

@mcp.tool()
def get_catalog_properties(catalog_name: str) -> Dict[str, Any]:
    """获取指定 catalog 的配置属性。

    Args:
        catalog_name: catalog 名称

    Returns:
        catalog 的配置信息，包括创建语句和解析后的属性
    """
    try:
        conn = _get_trino_connection()
        cur = conn.cursor()

        # 首先检查 catalog 是否存在
        cur.execute("SHOW CATALOGS")
        catalogs = [row[0] for row in cur.fetchall()]

        if catalog_name not in catalogs:
            cur.close()
            conn.close()
            return {
                "catalog_name": catalog_name,
                "exists": False,
                "message": f"Catalog '{catalog_name}' does not exist"
            }

        # 尝试获取 catalog 创建信息
        # 注意：SHOW CREATE CATALOG 仅在动态 catalog 管理模式下可用
        try:
            sql = f"SHOW CREATE CATALOG {catalog_name}"
            cur.execute(sql)
            result = cur.fetchone()

            create_statement = result[0] if result and len(result) > 0 else None

            # 获取 catalog 的系统表信息
            cur.execute(f"SELECT * FROM system.metadata.catalogs WHERE catalog_name = '{catalog_name}'")
            catalog_info = cur.fetchall()

            cur.close()
            conn.close()

            return {
                "catalog_name": catalog_name,
                "exists": True,
                "create_statement": create_statement,
                "catalog_info": catalog_info,
                "note": "SHOW CREATE CATALOG is only available in dynamic catalog management mode"
            }

        except Exception as show_error:
            # 如果 SHOW CREATE CATALOG 不可用，返回基本信息
            cur.execute(f"SHOW SCHEMAS FROM {catalog_name}")
            schemas = [row[0] for row in cur.fetchall()]

            cur.close()
            conn.close()

            return {
                "catalog_name": catalog_name,
                "exists": True,
                "schemas": schemas,
                "schema_count": len(schemas),
                "note": "Dynamic catalog management may not be enabled. Only basic information available."
            }

    except Exception as e:
        logger.error(f"Error getting catalog properties for {catalog_name}: {str(e)}")
        return {
            "catalog_name": catalog_name,
            "error": str(e),
            "exists": False
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