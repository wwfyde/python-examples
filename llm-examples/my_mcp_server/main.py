from fastmcp import FastMCP

mcp = FastMCP("计算器 Demo")


@mcp.tool()
def add(a: int, b: int) -> int:
    """将两数相加"""
    return a + b


def run():
    print("run mcp server")
    mcp.run()


if __name__ == "__main__":
    mcp.run()
