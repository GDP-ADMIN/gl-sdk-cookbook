"""Hello World - Local Agent Execution Example with MCP.

This demonstrates running an agent locally with MCP (Model Context Protocol) support
without deploying to the AIP server. Uses the glaip-sdk[local] extra which includes aip-agents.

Usage:
    # Install dependencies
    pip install "glaip-sdk[local]"

    # Run the example
    python main_with_mcp.py

    # Note: This example expects an MCP server running locally.
    # For demonstration purposes, we show the configuration even if no server is available.

Authors:
    Christian Trisno Sen Long Chen (christian.t.s.l.chen@gdplabs.id)
"""

from dotenv import load_dotenv

from glaip_sdk.agents import Agent
from tools import SimpleGreetingTool
from mcps import arxiv_mcp, deepwiki_mcp

load_dotenv(override=True)

# Agent with both tools AND MCPs - runs locally without deployment!
mcps = [mcp for mcp in [arxiv_mcp, deepwiki_mcp] if mcp is not None]
hello_agent_with_mcp = Agent(
    name="hello_local_agent_mcp",
    instruction="""You are a friendly assistant with access to local tools and MCP servers.

When users ask for greetings:
- Use the simple_greeting tool for personalized greetings

When users need information or ask questions:
- Use the DeepWiki MCP to search for documentation and information from GitHub repositories
- Use the Arxiv MCP (if available) to search for academic papers and research
- Always use the appropriate MCP tools when users ask questions that require external information

When users ask you to search or find information:
- Actively use the MCP tools available to you
- Don't just greet them - actually perform the searches they request
- Provide helpful summaries of the information you find

Always be helpful and friendly, and make sure to actually use the MCP tools when appropriate!
""",
    description="A local agent with tools and MCP support",
    tools=[SimpleGreetingTool],
    mcps=mcps,
)


def main() -> None:
    """Run the hello world agent with MCP locally."""
    print("=" * 60)
    print("Hello World - Local Agent with MCP Support")
    print("=" * 60)
    print()

    # Run locally - no deploy() call needed!
    message = (
        "Can you search DeepWiki for information about Python async programming, "
        "and also search Arxiv for recent papers about machine learning?"
    )

    hello_agent_with_mcp.run(message, verbose=True)


if __name__ == "__main__":
    main()
