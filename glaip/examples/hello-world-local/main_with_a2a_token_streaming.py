"""Hello World Local - A2A Token Streaming Demo.

Demonstrates enable_a2a_token_streaming when running a local agent.
Token streaming will emit incremental content chunks during execution.

Usage:
    python main_with_a2a_token_streaming.py

Authors:
    Fachriza Adhiatma (fachriza.d.adhiatma@gdplabs.id)
"""

from dotenv import load_dotenv
from glaip_sdk.agents import Agent

load_dotenv(override=True)

INSTRUCTION = """You are a helpful assistant.

When asked to tell a story or explain something, provide a detailed and engaging response.
"""

hello_agent = Agent(
    name="hello_streaming_agent",
    instruction=INSTRUCTION,
    description="Hello world agent that demonstrates A2A token streaming",
    agent_config={"enable_a2a_token_streaming": True},
)


def main() -> None:
    """Run the hello world agent locally with A2A token streaming enabled."""
    message = "Tell me a short story about a robot learning to paint. Make it engaging and detailed."
    print(f"User: {message}")

    response_plain = hello_agent.run(message, verbose=False)

    print("-" * 60)
    print(f"Agent: {response_plain}")
    print("-" * 60)


if __name__ == "__main__":
    main()
