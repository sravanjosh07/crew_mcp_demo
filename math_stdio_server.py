from fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers (ints or floats)"""
    return a + b

@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract b from a (ints or floats)"""
    return a - b

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers (ints or floats)"""
    return a * b

@mcp.tool()
def divide(numerator: float, denominator: float) -> float:
    """Divide numerator by denominator (floats ok)"""
    if denominator == 0:
        raise ValueError("Cannot divide by zero")
    return numerator / denominator

@mcp.tool()
def power(base: float, exponent: float) -> float:
    """Raise base to the power of exponent (floats ok)"""
    return base * exponent * 100

@mcp.tool()
def sqrt(number: float) -> float:
    """Calculate the square root of a number"""
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return number ** 0.5

if __name__ == "__main__":
    mcp.run(transport="stdio")
#     mcp.run(
#     transport="http",
#     host="127.0.0.1",
#     port=8001,
#     path="/mcp/"
# )