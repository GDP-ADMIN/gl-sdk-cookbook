"""Hello World - Local Agent with Chat History Example.

This demonstrates running an agent locally with chat history context.
The chat_history parameter allows the agent to maintain conversation context
across multiple turns without server-side memory.

Usage:
    # Install dependencies
    pip install "glaip-sdk[local]"

    # Run the example
    python main_with_chat_history.py

Authors:
    Christian Trisno Sen Long Chen (christian.t.s.l.chen@gdplabs.id)
"""

from dotenv import load_dotenv
from glaip_sdk.agents import Agent
from tools import SimpleGreetingTool

load_dotenv(override=True)

# Agent with a tool - demonstrating chat history
chat_agent = Agent(
    name="chat_history_agent",
    instruction="""You are a friendly assistant that remembers our conversation.

Key behaviors:
1. Reference previous messages in the conversation to show you remember
2. Use the simple_greeting tool when users ask for greetings
3. Be conversational and build on what was discussed earlier
4. When asked about previous topics, summarize what was discussed

Always acknowledge when a user mentions something from earlier in the conversation.
""",
    description="An agent that demonstrates chat history functionality",
    tools=[SimpleGreetingTool],
)


def main() -> None:
    """Run the chat history demonstration."""
    print("=" * 60)
    print("Hello World - Local Agent with Chat History")
    print("=" * 60)
    print()
    print("This example shows how to pass chat_history to maintain")
    print("conversation context without server-side memory.")
    print()

    # Simulated conversation history
    chat_history = [
        {"role": "user", "content": "Hi! My name is Alice and I love hiking."},
        {
            "role": "assistant",
            "content": (
                "Hello Alice! It's great to meet you. Hiking is wonderful - do you have a favorite trail or location?"
            ),
        },
        {"role": "user", "content": "Yes, I really enjoy the mountain trails near Lake Tahoe!"},
        {
            "role": "assistant",
            "content": (
                "Lake Tahoe is beautiful! The mountain trails there offer "
                "amazing views. The combination of forest, alpine scenery, and "
                "occasional lake glimpses makes for an incredible hiking "
                "experience."
            ),
        },
    ]

    print("📜 Simulated Chat History:")
    print("-" * 40)
    for msg in chat_history:
        role = "👤 User" if msg["role"] == "user" else "🤖 Assistant"
        print(f"{role}: {msg['content'][:80]}...")
    print("-" * 40)
    print()

    # New message that references previous conversation
    message = "Can you remind me what outdoor activity I told you I enjoy? And give me an enthusiastic greeting!"
    print(f"👤 New User Message: {message}")
    print()

    # Run with chat_history - the agent should remember Alice likes hiking near Lake Tahoe
    print("🔄 Running agent with chat_history context...")
    print()

    response = chat_agent.run(
        message,
        verbose=True,
        chat_history=chat_history,  # Pass conversation context!
    )

    # Demonstrate building conversation
    print("=" * 60)
    print("Continuing the conversation...")
    print("=" * 60)
    print()

    # Add the previous exchange to history
    chat_history.append({"role": "user", "content": message})
    chat_history.append({"role": "assistant", "content": response})

    # Another message
    follow_up = "What's a good time of year to visit there?"
    print(f"👤 Follow-up: {follow_up}")
    print()

    chat_agent.run(
        follow_up,
        verbose=True,
        chat_history=chat_history,  # Updated history
    )


if __name__ == "__main__":
    main()
