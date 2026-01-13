"""Hello World - Local Agent Execution with Files.

This demonstrates running an agent locally with access to local files.
Uses the glaip-sdk[local] extra which includes aip-agents.

Usage:
    # Install dependencies
    pip install "glaip-sdk[local]"

    # Run the example
    python main_with_local_files.py

Authors:
    Fachriza Adhiatma (fachriza.d.adhiatma@gdplabs.id)
"""

from pathlib import Path

from dotenv import load_dotenv
from glaip_sdk.agents import Agent
from tools import LocalTextFileTool

load_dotenv(override=True)

file_agent = Agent(
    name="hello_local_file_agent",
    instruction=(
        "You are a helpful assistant with access to local files.\n\n"
        "When asked to read a file:\n"
        "1. Use the read_local_text_file tool to read the content\n"
        "2. Summarize the file in one sentence\n"
        "3. Offer to read another file\n"
    ),
    description="A local agent that can read a text file from disk",
    tools=[LocalTextFileTool],
)


def main() -> None:
    """Run the local file agent example."""
    base_dir = Path(__file__).resolve().parent
    local_file = base_dir / "files" / "hello_local.txt"

    print("=" * 60)
    print("Hello World - Local Agent Execution with Local Files")
    print("=" * 60)
    print()
    print("This agent runs LOCALLY without deploying to the AIP server.")
    print("It receives local files via agent.run(files=[...]).")
    print(f"Local file provided: {local_file}")
    print()

    message = "Please read the provided local file and summarize it."
    print(f"User: {message}")
    print()

    response = file_agent.run(message, files=[str(local_file)], verbose=True)

    print()
    print("-" * 60)
    print(f"Agent: {response}")
    print("-" * 60)


if __name__ == "__main__":
    main()
