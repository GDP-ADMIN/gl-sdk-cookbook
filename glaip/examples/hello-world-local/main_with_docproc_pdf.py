"""Hello World - Local Agent Execution with PDF Processing.

This demonstrates running an agent locally with PDF document processing.
Uses the glaip-sdk[local] extra which includes aip-agents.

Usage:
    # Install dependencies
    make sync

    # Run the example
    uv run python main_with_docproc_pdf.py

Authors:
    Putu Ravindra Wiguna (putu.r.wiguna@gdplabs.id)
"""

from pathlib import Path

from dotenv import load_dotenv
from glaip_sdk.agents import Agent

# Import native tools from aip-agents (with graceful handling of missing optional dependencies)
tools_list = []

try:
    from aip_agents.tools.document_loader import PDFReaderTool

    tools_list.extend([PDFReaderTool])
except ImportError as e:
    print(f"Warning: Document loader tools not available: {e}")

load_dotenv(override=True)

file_agent = Agent(
    name="hello_local_agent_with_pdf",
    instruction="""You are a helpful assistant with access to PDF document processing.

You have access to document loader tools:
1. PDFReaderTool: Read and extract content from PDF files

When users ask you to:
- Read a PDF: Use PDFReaderTool to read the file content
- Summarize a document: Read it first, then provide a concise summary
- Analyze a document: Read it first, then provide insights

Always explain what you're doing and provide helpful responses.
""",
    description="A local agent that can read PDF files from disk",
    tools=tools_list,
)


def main() -> None:
    """Run the local PDF processing agent example."""
    base_dir = Path(__file__).resolve().parent
    local_file = base_dir / "files" / "example.pdf"

    print("=" * 60)
    print("Hello World - Local Agent Execution with PDF Processing")
    print("=" * 60)
    print()
    print("This agent runs LOCALLY without deploying to the AIP server.")
    print("Using glaip-sdk[local] with aip-agents backend.")
    print(f"Local file provided: {local_file}")
    print()

    message = "Please read the provided local pdf file and summarize it."
    print(f"User: {message}")
    print()

    response = file_agent.run(message, files=[str(local_file)], verbose=True)

    print()
    print("-" * 60)
    print(f"Agent: {response}")
    print("-" * 60)


if __name__ == "__main__":
    main()
