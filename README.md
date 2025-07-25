# CrewAI MCP Demo

A demo of integrating CrewAI with the Model Context Protocol (MCP) using a custom math server.

refer to the source for extended usage : https://github.com/tonykipkemboi/crewai-mcp-demo

## Overview

This project showcases how to:
- Create a custom MCP math server with basic arithmetic operations
- Integrate MCP servers with CrewAI agents
- Use MCP tools within CrewAI workflows

## Quick Start

### 1. Set up Environment Variables

Create a `.env` file in the project root with your API keys:

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

### 2. Install Dependencies

```bash
pip install -e .
```

### 3. Run the CrewAI Demo

```bash
python stdio_client_demo.py
```

This will:
- Start the MCP math server
- Create a CrewAI agent with access to math tools
- Execute a sample calculation task
- Display the results

## Project Structure

- `math_stdio_server.py` - Custom MCP server with math operations (add, subtract, multiply, divide)
- `stdio_client_demo.py` - CrewAI integration demo that uses the MCP math server
- `pyproject.toml` - Project dependencies and configuration
- `.env` - Environment variables (create this file with your API keys)

## Available Math Operations

The MCP math server provides the following tools:
- **add**: Addition of two numbers
- **subtract**: Subtraction of two numbers  
- **multiply**: Multiplication of two numbers
- **divide**: Division of two numbers (with zero-division protection)

## Detailed Inspection with MCP Inspector

If you want to explore the MCP server in detail and test individual operations, you can use the MCP Inspector:

### Install MCP Inspector

```bash
npm install -g @modelcontextprotocol/inspector
```

### Run MCP Inspector

```bash
npx @modelcontextprotocol/inspector python math_stdio_server.py
```

This will open a web interface where you can:
- View all available MCP tools and their schemas
- Test individual math operations interactively
- Inspect the MCP protocol messages
- Debug and validate your MCP server implementation

The inspector is particularly useful for:
- Understanding the MCP tool specifications
- Testing edge cases (like division by zero)
- Debugging MCP server responses
- Learning how MCP protocol works under the hood

## Requirements

- Python 3.8+
- OpenAI API key
- CrewAI
- MCP (Model Context Protocol) client libraries

## License

MIT License