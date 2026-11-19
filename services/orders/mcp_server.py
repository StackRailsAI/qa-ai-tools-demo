"""An MCP server the orders service builds (QA fixture)."""
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("orders-tools")


@mcp.tool()
def get_order(order_id: str) -> dict:
    """Return one order."""
    return {"id": order_id, "status": "shipped"}


@mcp.tool()
def cancel_order(order_id: str) -> dict:
    """Cancel one order."""
    return {"id": order_id, "status": "cancelled"}


if __name__ == "__main__":
    mcp.run()
