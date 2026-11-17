"""ASI05 / deterministic — unvalidated model output in eval.

Compact reproduction of testbenches/tier2-specialized/damn-vulnerable-MCP-server
challenges/hard/challenge8/server_sse.py:26 (ASINT-ASI05-106, pdg layer, 0.80).
"""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Calculator Server")


@mcp.tool()
def evaluate_expression(expression: str) -> str:
    """Evaluate a mathematical expression and return the result.

    Args:
        expression: The mathematical expression to evaluate (e.g., "2 + 2 * 3")
    """
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Error evaluating expression: {str(e)}"
