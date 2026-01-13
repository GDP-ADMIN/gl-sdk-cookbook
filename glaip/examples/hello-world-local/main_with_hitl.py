"""Hello World - Local Agent Execution with HITL Example.

This demonstrates running an agent locally with Human-in-the-Loop (HITL)
approval for tool execution. The LocalPromptHandler is automatically injected
by the runner when hitl_enabled is True - no manual setup required!

Usage:
    # Install dependencies
    pip install "glaip-sdk[local]"

    # Run the example
    python main_with_hitl.py

    # When prompted, approve/reject tool calls:
    # - Press 'y' or 'yes' to approve
    # - Press 'n' or 'no' to reject
    # - Press 's' or 'skip' to skip
    # - Wait for timeout to auto-skip

Authors:
    Putu Ravindra Wiguna (putu.r.wiguna@gdplabs.id)
"""

from dotenv import load_dotenv

from glaip_sdk.agents import Agent
from tools import SimpleGreetingTool

load_dotenv(override=True)

# Agent with HITL enabled - CLI prompts auto-injected for local runs!
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
    tools=[SimpleGreetingTool],
    tool_configs={SimpleGreetingTool: {"hitl": {"timeout_seconds": 10}}},
    agent_config={"hitl_enabled": True},  # ← This enables HITL with auto CLI prompts!
)


def main() -> None:
    """Run the hello world agent locally with HITL approval."""
    print("=" * 60)
    print("Hello World - Local Agent with HITL Demo")
    print("=" * 60)
    print()
    print("This agent runs LOCALLY with Human-in-the-Loop approval.")
    print("✓ HITL is auto-enabled - just set agent_config.hitl_enabled = True")
    print("✓ CLI prompts are auto-injected by LangGraphRunner")
    print("✓ No manual wiring needed!")
    print()
    print("Agent has access to: SimpleGreetingTool (requires approval)")
    print("When the tool is called, you'll be prompted to approve/reject.")
    print("Options: y (approve) / n (reject) / skip")
    print("Timeout: 10 seconds (will auto-skip if no input)")
    print()

    # Run locally - no deploy() call needed!
    message = "Please give me an enthusiastic greeting! My name is Christian."

    hello_agent.run(message, verbose=True)


if __name__ == "__main__":
    main()
