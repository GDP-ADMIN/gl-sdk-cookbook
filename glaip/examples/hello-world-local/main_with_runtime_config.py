"""Hello World Local - Runtime Config Demo.

Demonstrates runtime_config for tools, MCPs, and agents in LOCAL mode.
This is the local equivalent of hello-world-runtime-config/main.py.

Key differences from platform mode:
- Keys are resolved to names (not UUIDs)
- No deploy() call needed
- Configuration is normalized before passing to aip-agents

Authors:
    Christian Trisno Sen Long Chen (christian.t.s.l.chen@gdplabs.id)
"""

import os
from typing import Any, ClassVar

from dotenv import load_dotenv
from langchain_core.runnables import RunnableConfig
from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field

from glaip_sdk.agents import Agent
from glaip_sdk.mcps import MCP

load_dotenv(override=True)

# =============================================================================
# Tool with ConfigSchema (similar to ResearchFormatterTool)
# =============================================================================


class FormatterConfig(BaseModel):
    """Tool configuration for research formatting."""

    style: str = Field(default="brief", description="Output style: brief, detailed, or academic")
    max_results: int = Field(default=5, ge=1, le=20, description="Maximum results to format")
    include_links: bool = Field(default=True, description="Include paper links")


class FormatterInput(BaseModel):
    """Input schema for research formatter."""

    query: str = Field(..., description="Research topic or query")


class ResearchFormatterTool(BaseTool):
    """Format research results with configurable style."""

    name: str = "research_formatter"
    description: str = "Format research papers with configurable output style"
    args_schema: type[BaseModel] = FormatterInput
    tool_config_schema: ClassVar = FormatterConfig

    def _run(self, query: str, config: RunnableConfig | None = None) -> str:
        """Format research results based on configuration."""
        # In aip-agents, tool_config is injected via metadata
        # For demo purposes, show what config would be used
        config = self.get_tool_config(config)
        return f"Formatted results for: {query} with config {config}"


# =============================================================================
# Agent Definition
# =============================================================================

INSTRUCTION = """You are a research assistant that helps find and format academic papers.

When users ask about research topics:
1. Plan on what you are going to search for papers
2. Use the arxiv MCP to search for papers (if available)
3. Use the research_formatter tool to format results

You can format results in different styles: brief, detailed, or academic.
"""

_api_key = os.getenv("ARXIV_MCP_API_KEY")
_auth_token = os.getenv("ARXIV_MCP_AUTH_TOKEN")

arxiv_mcp: MCP | None = None

if _api_key and _auth_token:
    arxiv_mcp = MCP(
        name="arxiv-mcp-chen",
        transport="http",
        description="Arxiv MCP for searching academic papers",
        config={
            "url": "https://api.bosa.id/arxiv/mcp/",
        },
        authentication={
            "type": "custom-header",
            "headers": {
                "x-api-key": "example",
                "Authorization": "Bearer example",
            },
        },
    )

_tools: list[Any] = [ResearchFormatterTool]
_mcps: list[Any] = [arxiv_mcp] if arxiv_mcp else []

research_agent = Agent(
    name="research_agent",
    instruction=INSTRUCTION,
    description="Research assistant with configurable formatting",
    tools=_tools,
    mcps=_mcps,
)


# =============================================================================
# Main execution
# =============================================================================


def main() -> None:
    """Run the research agent with runtime_config (LOCAL mode)."""
    print("=" * 60)
    print("Hello World Local - Runtime Config Demo")
    print("=" * 60)

    print("\n✓ Agent created (local mode, no deploy needed)")
    print(f"  Name: {research_agent.name}")
    print(f"  Tools: {[t.name if hasattr(t, 'name') else t.__name__ for t in research_agent.tools]}")
    print(f"  MCPs: {[m.name for m in research_agent.mcps] if research_agent.mcps else 'None'}")

    # Build runtime_config (same structure as platform mode)
    print("\n" + "=" * 60)
    print("Runtime Config Structure:")
    print("=" * 60)

    runtime_config = {
        # Agent-level config (planning, max_steps, etc.)
        "agent_config": {"planning": True, "memory": "mem0"},
        # Tool configurations (global)
        "tool_configs": {
            ResearchFormatterTool: {
                "style": "brief",
                "max_results": 3,
            },
        },
        # Agent-specific overrides (highest priority)
        research_agent: {
            "mcp_configs": {
                arxiv_mcp: {
                    "authentication": {
                        "type": "custom-header",
                        "headers": {
                            "x-api-key": _api_key,
                            "Authorization": f"Bearer {_auth_token}",
                        },
                    },
                },
            }
            if arxiv_mcp
            else {},
        },
    }

    # Uncomment to actually run the agent (requires API keys + model)
    research_agent.run(
        "Hello! Can you help me find papers about transformers?",
        runtime_config=runtime_config,
        verbose=True,
    )

    print("\n✓ Demo complete! (uncomment arun to execute with LLM)")


if __name__ == "__main__":
    main()
