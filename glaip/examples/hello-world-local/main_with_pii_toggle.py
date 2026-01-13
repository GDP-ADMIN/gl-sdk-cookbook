"""Hello World Local - PII Toggle Demo.

Demonstrates enable_pii flag when running a local agent.
When enable_pii=True is set in agent_config at construction time,
PII values are anonymized only if a PII handler is available (NER env vars
or a predefined pii_mapping). If NER is not configured, NER-based
anonymization stays off even when enable_pii is True.

Usage:
    python main_with_pii_toggle.py

Authors:
    Fachriza Adhiatma (fachriza.d.adhiatma@gdplabs.id)
"""

from dotenv import load_dotenv
from glaip_sdk.agents import Agent
from tools import CustomerInfoTool

load_dotenv(override=True)

INSTRUCTION = """You are a helpful assistant that can look up customer info.

When a user asks about a customer:
1. Call get_customer_info with the provided customer ID
2. Return the result exactly as the tool provides it
"""

customer_agent = Agent(
    name="customer_info_agent",
    instruction=INSTRUCTION,
    description="Customer info agent that demonstrates PII toggle",
    tools=[CustomerInfoTool],
    agent_config={"enable_pii": True},
)


def main() -> None:
    """Run the customer info agent locally with PII toggle."""
    message = "Show customer info for C001."
    print(f"User: {message}")

    response_plain = customer_agent.run(message, verbose=True)

    print("-" * 60)
    print(f"Agent: {response_plain}")
    print("-" * 60)


if __name__ == "__main__":
    main()
