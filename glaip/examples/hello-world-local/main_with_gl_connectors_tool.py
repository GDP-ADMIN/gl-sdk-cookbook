"""Hello World - Local Agent Execution with GL Connectors.

This demonstrates running an agent locally using GL Connectors resolved
by exact tool name. The tools are fetched via the GLConnectorTool wrapper,
which injects the required token automatically.

Required environment variables:
- GL_CONNECTORS_BASE_URL
- GL_CONNECTORS_API_KEY
- GL_CONNECTORS_USERNAME
- GL_CONNECTORS_PASSWORD
Optional:
- GL_CONNECTORS_IDENTIFIER

Usage:
    # Install dependencies with uv (recommended)
    make sync

    # Run the example
    uv run python main_with_gl_connectors_tool.py
    # Or: python main_with_gl_connectors_tool.py

Authors:
    Saul Sayers (saul.sayers@gdplabs.id)
"""

from aip_agents.tools.gl_connector import GLConnectorTool
from dotenv import load_dotenv
from glaip_sdk.agents import Agent

TOOL_NAMES = [
    "github_list_pull_requests_tool",
    "arxiv_search_papers_tool",
    "twitter_tweet_search_tool",
    "google_mail_send_email_tool",
    "google_drive_search_files_tool",
    "sql_query_tool",
]


def _load_tools() -> list:
    tools = []
    for name in TOOL_NAMES:
        try:
            tools.append(GLConnectorTool(name))
        except Exception as exc:
            print(f"Warning: Failed to load GL Connector '{name}': {exc}")
    return tools


load_dotenv(override=True)

# Agent with GL Connectors - runs locally without deployment.
hello_agent = Agent(
    name="hello_local_agent_with_gl_connector_tools",
    instruction="""You are a helpful assistant with access to GL Connectors.

You have access to the following tools:
1. GitHub: github_list_pull_requests_tool
2. Arxiv: arxiv_search_papers_tool
3. Twitter: twitter_tweet_search_tool
4. Gmail: google_mail_send_email_tool
5. Google Drive: google_drive_search_files_tool
6. SQL: sql_query_tool

When users ask you to:
- List pull requests: use github_list_pull_requests_tool
- Search research papers: use arxiv_search_papers_tool
- Search tweets: use twitter_tweet_search_tool
- Send email: use google_mail_send_email_tool
- Search files: use google_drive_search_files_tool
- Run SQL queries: use sql_query_tool

Always explain what you're doing and provide helpful responses.
""",
    description="A simple agent that runs locally with GL Connectors",
    tools=_load_tools(),
)


def main() -> None:
    """Run the hello world agent locally with GL Connectors."""
    print("=" * 60)
    print("Hello World - Local Agent Execution with GL Connectors")
    print("=" * 60)
    print()
    print("This agent runs LOCALLY without deploying to the AIP server.")
    print("Using glaip-sdk[local] with aip-agents backend.")
    print()
    print("Agent has access to GL Connectors:")
    for name in TOOL_NAMES:
        print(f"  - {name}")
    print()

    message = (
        "Hello! Can you list the most recent pull requests for gdp-admin/gl-connector?"
    )
    print(f"User: {message}")
    print()

    response = hello_agent.run(message, verbose=True)

    print()
    print("-" * 60)
    print(f"Agent: {response}")
    print("-" * 60)


if __name__ == "__main__":
    main()
