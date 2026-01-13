"""Hello World - Local Agent Execution Example with Native Tools.

This demonstrates running an agent locally without deploying to the AIP server.
Uses the glaip-sdk[local] extra which includes aip-agents.
This example showcases the native tools available in aip-agents.

Usage:
    # Install dependencies with uv (recommended)
    uv sync

    # Or install with pip
    pip install "glaip-sdk[local]"
    pip install "aip-agents[document-loader,code-sandbox,browser-use-tool]"

    # Run all tools with default queries
    uv run python main_with_native_tool.py --all

    # Run specific tool tests
    uv run python main_with_native_tool.py --e2b
    uv run python main_with_native_tool.py --serper
    uv run python main_with_native_tool.py --browser
    uv run python main_with_native_tool.py --time

    # Run with custom query
    uv run python main_with_native_tool.py --query "Your custom query here"

Authors:
    Christian Trisno Sen Long Chen (christian.t.s.l.chen@gdplabs.id)
"""

import argparse

from dotenv import load_dotenv
from glaip_sdk.agents import Agent

# Import native tools from aip-agents (with graceful handling of missing optional dependencies)
tools_list = []

try:
    from aip_agents.tools.document_loader import (
        DocxReaderTool,
        ExcelReaderTool,
        PDFReaderTool,
    )

    tools_list.extend([PDFReaderTool, DocxReaderTool, ExcelReaderTool])
except ImportError as e:
    print(f"Warning: Document loader tools not available: {e}")

try:
    from aip_agents.tools.web_search import GoogleSerperTool

    tools_list.append(GoogleSerperTool)
except ImportError as e:
    print(f"Warning: Web search tools not available: {e}")

try:
    from aip_agents.tools.code_sandbox import E2BCodeSandboxTool

    tools_list.append(E2BCodeSandboxTool)
except ImportError as e:
    print(f"Warning: Code sandbox tools not available: {e}")

try:
    from aip_agents.tools.browser_use import BrowserUseTool

    tools_list.append(BrowserUseTool)
except ImportError as e:
    print(f"Warning: Browser use tools not available: {e}")

try:
    from aip_agents.tools import TimeTool

    tools_list.append(TimeTool)
except ImportError as e:
    print(f"Warning: Time tool not available: {e}")

load_dotenv(override=True)

# Agent with native tools - runs locally without deployment!
hello_agent = Agent(
    name="hello_local_agent_with_native_tools",
    instruction="""You are a helpful assistant with access to powerful native tools.

You have access to the following tools:
1. Document Loaders: Read PDF, DOCX, and Excel files
2. Web Search: Search the web using Google Serper
3. Code Sandbox: Execute code in a secure sandbox environment
4. Browser Use: Automate web browser interactions
5. Time Tool: Get current time in various formats and timezones

When users ask you to:
- Read documents: Use PDFReaderTool, DocxReaderTool, or ExcelReaderTool
- Search the web: Use GoogleSerperTool
- Execute code: Use E2BCodeSandboxTool
- Interact with websites: Use BrowserUseTool
- Get current time: Use TimeTool with specific timezone and format

Always explain what you're doing and provide helpful responses.
""",
    description="A simple agent that runs locally with native tools from aip-agents",
    tools=tools_list if tools_list else None,  # Use available tools, or None if none available
)


def main() -> None:
    """Run the hello world agent locally with native tools."""
    parser = argparse.ArgumentParser(
        description="Test native tools with specific queries",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Run all tool tests sequentially (E2B, Serper, Browser, Time)",
    )
    parser.add_argument(
        "--e2b",
        action="store_true",
        help="Test E2B code sandbox tool (generate chessboard)",
    )
    parser.add_argument(
        "--serper",
        action="store_true",
        help="Test Google Serper web search tool",
    )
    parser.add_argument(
        "--browser",
        action="store_true",
        help="Test Browser Use tool (find latest news in detik.com)",
    )
    parser.add_argument(
        "--time",
        action="store_true",
        help="Test Time tool (get current time in different timezones)",
    )
    parser.add_argument(
        "--query",
        type=str,
        help="Custom query to send to the agent",
    )

    args = parser.parse_args()

    print("=" * 60)
    print("Hello World - Local Agent Execution with Native Tools")
    print("=" * 60)
    print()
    print("This agent runs LOCALLY without deploying to the AIP server.")
    print("Using glaip-sdk[local] with aip-agents backend.")
    print()

    # Determine which queries to run
    queries = []

    if args.all:
        # Run all tool tests
        queries = [
            {
                "message": (
                    "Use your E2B code sandbox tool to generate a chessboard using Python. "
                    "Create an 8x8 grid with alternating black and white squares and display it."
                ),
                "description": "E2B Code Sandbox Test - Generate Chessboard",
            },
            {
                "message": "Use your serper tool to search for the latest news about Barcelona football club.",
                "description": "Google Serper Web Search Test",
            },
            {
                "message": (
                    "Use your browser use tool to navigate to detik.com and find the latest "
                    "news headlines on the homepage."
                ),
                "description": "Browser Use Test - Latest News from Detik.com",
            },
            {
                "message": (
                    "Use your time tool to get the current time in Jakarta timezone "
                    "(Asia/Jakarta) with a readable format like 'Wednesday, January 8, 2025 at 03:45 PM'."
                ),
                "description": "Time Tool Test - Current Time in Jakarta",
            },
        ]
    elif args.e2b:
        queries = [
            {
                "message": (
                    "Use your E2B code sandbox tool to generate a chessboard using Python. "
                    "Create an 8x8 grid with alternating black and white squares and display it."
                ),
                "description": "E2B Code Sandbox Test - Generate Chessboard",
            }
        ]
    elif args.serper:
        queries = [
            {
                "message": "Use your serper tool to search for the latest news about Barcelona football club.",
                "description": "Google Serper Web Search Test",
            }
        ]
    elif args.browser:
        queries = [
            {
                "message": (
                    "Use your browser use tool to navigate to detik.com and find the latest "
                    "news headlines on the homepage."
                ),
                "description": "Browser Use Test - Latest News from Detik.com",
            }
        ]
    elif args.time:
        queries = [
            {
                "message": (
                    "Use your time tool to get the current time in Jakarta timezone "
                    "(Asia/Jakarta) with a readable format like 'Wednesday, January 8, 2025 at 03:45 PM'."
                ),
                "description": "Time Tool Test - Current Time in Jakarta",
            }
        ]
    elif args.query:
        queries = [
            {
                "message": args.query,
                "description": "Custom Query",
            }
        ]
    else:
        # Default: run all tests
        queries = [
            {
                "message": "Use your serper tool to search latest news about barcelona",
                "description": "Default Test - Web Search",
            }
        ]

    # Run queries sequentially
    for i, query_info in enumerate(queries, 1):
        if len(queries) > 1:
            print(f"\n{'=' * 60}")
            print(f"Test {i}/{len(queries)}: {query_info['description']}")
            print("=" * 60)
            print()

        print(f"User: {query_info['message']}")
        print()

        try:
            response = hello_agent.run(query_info["message"], verbose=True)

            print()
            print("-" * 60)
            print(f"Agent: {response}")
            print("-" * 60)

            if i < len(queries):
                print("\n" + "=" * 60)
                print("Waiting before next test...")
                print("=" * 60)
                print()

        except Exception as e:
            print()
            print("-" * 60)
            print(f"Error: {e}")
            print("-" * 60)
            if i < len(queries):
                print("\nContinuing with next test...\n")


if __name__ == "__main__":
    main()
