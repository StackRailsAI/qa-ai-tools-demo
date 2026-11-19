"""Orders agent (QA fixture): connects to MCP servers from code."""
import os

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client


async def lookup(order_id: str) -> None:
    async with streamablehttp_client(os.environ["ORDERS_MCP_URL"]) as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.call_tool("get_order", {"id": order_id})


async def docs(query: str) -> None:
    async with streamablehttp_client("https://mcp.notion.com/mcp") as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.call_tool("search", {"query": query})
