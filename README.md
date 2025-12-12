# DataPlus MCP

Trino MCP Server - 基于 Model Context Protocol 的 Trino SQL 查询服务器。

## 快速开始

### 1. 启动 Docker Compose

首先启动 Trino 数据库引擎：

```bash
docker-compose up -d
```

### 2. 启动 MCP Server

进入 `mcp-server` 目录并启动服务器：

```bash
cd mcp-server
uv run mcp-server
```

## 本地开发

如果需要进行本地开发，请先同步依赖：

```bash
cd mcp-server
uv sync
```

然后运行开发服务器：

```bash
uv run mcp-server
```

## 项目结构

- `mcp-server/` - MCP 服务器代码
  - `trino_fastmcp.py` - 主服务器文件
  - `pyproject.toml` - 项目配置
- `trino-etc/` - Trino 配置文件
  - `catalog/` - 数据源连接器配置目录
- `docker-compose.yml` - Docker Compose 配置

## 数据源配置

在 `trino-etc/catalog/` 目录中可以添加各种数据源的连接器配置文件（`.properties` 格式）：

### 示例配置

**PostgreSQL 连接 (`pg_db.properties`)**:
```properties
connector.name=postgresql
connection-url=jdbc:postgresql://host.docker.internal:5432/your_database
connection-user=your_username
connection-password=your_password
```

**MySQL 连接 (`mysql_db.properties`)**:
```properties
connector.name=mysql
connection-url=jdbc:mysql://host.docker.internal:3306/your_database
connection-user=your_username
connection-password=your_password
```

**MongoDB 连接 (`mongo_db.properties`)**:
```properties
connector.name=mongodb
mongodb.seeds=host.docker.internal:27017
```

任何放置在此目录中的 `.properties` 文件都会被 Trino 自动加载为可用的数据源 catalog。

## 依赖

- Python >= 3.11
- Docker & Docker Compose
- uv (Python 包管理器)