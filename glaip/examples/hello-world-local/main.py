"""Hello World - Local Agent Execution Example.

This demonstrates running an agent locally without deploying to the AIP server.
Uses the glaip-sdk[local] extra which includes aip-agents.

Usage:
    # Install dependencies
    pip install "glaip-sdk[local]"

    # Run the example
    python main.py

Authors:
    Christian Trisno Sen Long Chen (christian.t.s.l.chen@gdplabs.id)
"""

from dotenv import load_dotenv
from glaip_sdk.agents import Agent
from tools import SimpleGreetingTool

load_dotenv(override=True)

# Agent with a tool - runs locally without deployment!
hello_agent = Agent(
    name="hello_local_agent",
    instruction="""You are a friendly greeting assistant with a special greeting tool.

When users want a greeting:
1. Use the simple_greeting tool to generate a personalized greeting
2. You can use different styles: 'formal', 'casual', or 'enthusiastic'
3. After the greeting, offer to help with something else

When users just chat:
- Respond naturally and keep the conversation friendly
- You can ask follow-up questions
""",
    description="A simple agent that runs locally with a greeting tool",
    tools=[SimpleGreetingTool],  # Tool works locally!
)


def main() -> None:
    """Run the hello world agent locally."""
    print("=" * 60)
    print("Hello World - Local Agent Execution with Tool")
    print("=" * 60)
    print()
    print("This agent runs LOCALLY without deploying to the AIP server.")
    print("Using glaip-sdk[local] with aip-agents backend.")
    print("Agent has access to: SimpleGreetingTool")
    print()

    # Run locally - no deploy() call needed!
    message = "Please give me an enthusiastic greeting! My name is Christian."

    hello_agent.run(message, verbose=True)


if __name__ == "__main__":
    main()
