"""Simple Agent with mem0 Memory Example.

This demonstrates using mem0 memory to remember user information across runs.

Usage:
    # Install dependencies with memory extra
    pip install "glaip-sdk[local,memory]"

    # Set required environment variables (either MEM0_API_KEY or GLLM_MEMORY_API_KEY)
    export MEM0_API_KEY=your_mem0_api_key
    # OR
    # export GLLM_MEMORY_API_KEY=your_gllm_memory_api_key

    # Run the example
    python main_with_memory.py

Authors:
    Putu Ravindra Wiguna (putu.r.wiguna@gdplabs.id)
"""

import time
from dotenv import load_dotenv
from glaip_sdk.agents import Agent

load_dotenv(override=True)

# Simple agent with mem0 memory - no tools needed
memory_agent = Agent(
    name="memory_agent",
    instruction="""You are a helpful assistant that remembers information about users.

When users tell you something about themselves, remember it.
When users ask you questions, use what you remember about them to answer.
Be friendly and conversational.""",
    description="A simple agent that uses mem0 to remember user information",
    agent_config={
        "memory": "mem0",
    },
)


def main() -> None:
    """Run the memory agent example."""
    print("=" * 60)
    print("mem0 Memory Agent Example")
    print("=" * 60)
    print()

    memory_user_id = "user_yamal_123"  # Unique user identifier for memory scoping

    # First run: Tell the agent your name
    print("RUN 1: Introducing myself")
    print("-" * 60)
    message1 = "My name is Joan Garcia now, Please remember this name"
    print(f"User: {message1}")
    print()

    memory_agent.run(
        message1,
        verbose=True,
        memory_user_id=memory_user_id,  # Attach memory to this user
    )
    print()
    print("=" * 60)
    print()

    # Wait for mem0 to properly store the memory
    # mem0 has eventual consistency - memories are persisted asynchronously
    # A short delay ensures the memory is available for the next query
    print("⏳ Waiting 5 seconds for memory to be stored...")
    time.sleep(5)
    print()

    # Second run: Ask the agent to recall your name
    print("RUN 2: Testing memory recall")
    print("-" * 60)
    message2 = "What is my name?"
    print(f"User: {message2}")
    print()

    memory_agent.run(
        message2,
        verbose=True,
        memory_user_id=memory_user_id,  # Same memory_user_id to retrieve memories
    )
    print()
    print("=" * 60)
    print()

    print("✓ If mem0 is working correctly, the agent should remember your name!")


if __name__ == "__main__":
    main()
