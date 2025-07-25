from crewai import Agent, Task, Crew
from crewai_tools import MCPServerAdapter
from mcp import StdioServerParameters
from dotenv import load_dotenv
import os


load_dotenv()
# MODEL="gpt-4.1-mini-2025-04-14"

# Create a StdioServerParameters object
server_params=StdioServerParameters(
    command="python3", 
    args=["math_stdio_server.py"],
    env={"UV_PYTHON": "3.12", **os.environ},
)

input_problems = [
    # "what 8 divided by 2?",
    # "what is the square root of 16?",
    # "what is 2 raised to the power of 3?",
    # "what is 3.5 plus 4.5?",
    # "what is 10 minus 4?",
    # "what is 2 multiplied by 3?",
    "what is 8 to the power of 2?"
]
input_problem = input_problems[0]
# Use the StdioServerParameters object to create a MCPServerAdapter
with MCPServerAdapter(server_params) as tools:
    print(f"Available tools from Stdio MCP server: {[tool.name for tool in tools]}")

    agent = Agent(
        role="Mathematician",
        goal="Perform mathematical operations.",
        backstory="An experienced mathematician that can perform mathematical operations via MCP tools. " \
        "CRITICAL: If you cannot solve the problem with the available tools, you can ask the user for more information.",
        tools=tools,
        verbose=True,
    )
    task = Task(
        description="Solve the following math problem: " + input_problem,
        expected_output="The correct answer to the math problem using the available tools.",
        agent=agent,
    )
    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True,
    )
    result = crew.kickoff()
    print(result)