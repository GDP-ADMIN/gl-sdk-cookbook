"""Hello World Local - Tool Output Sharing Demo.

Demonstrates tool output sharing in local mode with a two-step greeting flow.
Uses the glaip-sdk[local] extra which includes aip-agents.

Usage:
    # Install dependencies
    pip install "glaip-sdk[local]"

    # Run the example
    python main_with_tool_output_sharing.py

Authors:
    Fachriza Adhiatma (fachriza.d.adhiatma@gdplabs.id)
"""

from dotenv import load_dotenv
from glaip_sdk.agents import Agent
from tools import GreetingFormatterTool, GreetingGeneratorTool

load_dotenv(override=True)

INSTRUCTION = """You are a greeting assistant that uses tool output sharing.

Follow this workflow exactly:
1. Use greeting_generator to create the greeting.
2. The system stores the output and provides a call_id.
3. Pass the reference to greeting_formatter as message="$tool_output.<call_id>".
4. Return the formatted greeting to the user.
"""

greeting_agent = Agent(
    name="hello_local_tool_output_sharing",
    instruction=INSTRUCTION,
    description="Local agent that demonstrates tool output sharing",
    tools=[GreetingGeneratorTool, GreetingFormatterTool],
    agent_config={"tool_output_sharing": True},
)


def main() -> None:
    """Run the tool output sharing demo locally."""
    print("=" * 60)
    print("Hello World Local - Tool Output Sharing")
    print("=" * 60)
    print()
    print("This agent runs LOCALLY without deploying to the AIP server.")
    print("Tool output sharing is enabled (tool_output_sharing=True).")
    print("The greeting output is stored and referenced via $tool_output.<call_id>.")
    print()

    message = "Create a greeting for Alice, then format it nicely."
    print(f"User: {message}")
    print()

    response = greeting_agent.run(message, verbose=True)

    print()
    print("-" * 60)
    print(f"Agent: {response}")
    print("-" * 60)


if __name__ == "__main__":
    main()
