# qa-ai-tools-demo

QA fixture for StackRails **AI tool access** (`/ai-tools`, ticket 124hhvu6buy). Every token below is a fake placeholder:
the test checks that no value ever reaches the graph or the portal.

| Where | What it exercises |
|---|---|
| `services/orders/.mcp.json` | known data store with write access, the same server read-only, a known remote, an unknown local script, a URL from an env var (unresolved), a disabled entry, a server that looks like production |
| `services/payments/.cursor/mcp.json` | a *different* local script with the same file name, another env-var URL, a known remote |
| `services/payments/package.json` | an MCP-client-only library (manifest detection) |
| `services/orders/agent.py` | MCP SDK call sites in code: one env-var URL, one known URL |
| `services/orders/mcp_server.py` | an MCP server this repository builds (FastMCP) |
| `.vscode/mcp.json` | a config at the repository root, shared by both components |
