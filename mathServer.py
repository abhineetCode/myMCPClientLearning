from mcp.server.fastmcp import FastMCP

mcp= FastMCP("Math")


@mcp.tool()
def add(x: int, y: int) -> int:
    """Adds two numbers."""
    return x + y

@mcp.tool()
def multiply(x: int, y: int) -> int:
    """Multiplies two numbers."""
    return x * y

#The transport is set to "stdio" for standard input/output (stdin and stdout) communication - 
# to receive and respond to tool function calls
if __name__ == "__main__":
    mcp.run(transport="stdio")



