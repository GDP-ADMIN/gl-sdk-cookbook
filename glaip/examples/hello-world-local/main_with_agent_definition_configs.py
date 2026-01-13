"""Hello World Local - Agent Definition Configs Demo.

Demonstrates that tool_configs, agent_config, and mcp_configs can be set
directly in the Agent constructor (without runtime_config).

This tests the implementation where:
- Agent(tool_configs={...}) works
- Agent(agent_config={...}) works
- Agent(mcp_configs={...}) works

Priority order (lowest to highest):
1. Agent definition (this file demonstrates)
2. Runtime config global
3. Runtime config agent-specific

Authors:
    Christian Trisno Sen Long Chen (christian.t.s.l.chen@gdplabs.id)
"""

import os

from dotenv import load_dotenv
from glaip_sdk.agents import Agent
from glaip_sdk.mcps import MCP
from tools import ResearchFormatterTool

load_dotenv(override=True)

# =============================================================================
# MCP Configuration (optional - requires API keys)
# =============================================================================

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
                "x-api-key": "placeholder",  # Will be overridden by mcp_configs
                "Authorization": "Bearer placeholder",
            },
        },
    )

# =============================================================================
# Agent with Definition-Time Configs
# =============================================================================

INSTRUCTION = """You are a research assistant that helps find and format academic papers.

IMPORTANT: You MUST use the research_formatter tool for ANY request about research or formatting.
Do NOT answer directly - always call the tool first.

The tool will show you what configuration it received.
"""

# Build config dicts for agent definition
_tools = [ResearchFormatterTool]
_mcps = [arxiv_mcp] if arxiv_mcp else []

# This is the KEY part we're testing:
# Passing tool_configs, agent_config, mcp_configs directly to Agent()
research_agent = Agent(
    name="research_agent_with_configs",
    instruction=INSTRUCTION,
    description="Research assistant with definition-time configs",
    tools=_tools,
    mcps=_mcps,
    # =========================================================================
    # AGENT DEFINITION CONFIGS (what we're testing)
    # =========================================================================
    agent_config={
        "planning": False,  # Enable planning mode
    },
    tool_configs={
        # Configure ResearchFormatterTool with definition-time defaults
        ResearchFormatterTool: {
            "style": "detailed",  # Override default "brief"
            "max_results": 10,  # Override default 5
            "include_links": True,
        },
    },
    mcp_configs=(
        {
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
        else {}
    ),
)


# =============================================================================
# Main execution
# =============================================================================


def main() -> None:
    """Run the agent with configs from Agent definition (no runtime_config)."""
    print("=" * 70)
    print("Hello World Local - Agent Definition Configs Demo")
    print("=" * 70)

    print("\n✓ Agent created with definition-time configs (no runtime_config)")
    print(f"  Name: {research_agent.name}")
    print(f"  Tools: {[t.name if hasattr(t, 'name') else t.__name__ for t in research_agent.tools]}")
    print(f"  MCPs: {[m.name for m in research_agent.mcps] if research_agent.mcps else 'None'}")

    print("\n" + "=" * 70)
    print("Agent Definition Configs:")
    print("=" * 70)

    print(f"\n  agent_config: {research_agent.agent_config}")
    print(f"\n  tool_configs: {research_agent.tool_configs}")
    print(f"\n  mcp_configs: {research_agent.mcp_configs}")

    print("\n" + "=" * 70)
    print("Running agent (configs should be applied from Agent definition)...")
    print("=" * 70)

    # Run WITHOUT runtime_config - configs come from Agent definition
    research_agent.run(
        "Format some research about machine learning transformers",
        verbose=True,
    )

    print("\n" + "=" * 70)
    print("✓ Demo complete!")
    print("=" * 70)
    print("\nIf tool_configs worked, the response should show:")
    print("  - style: 'detailed' (not default 'brief')")
    print("  - max_results: 10 (not default 5)")


if __name__ == "__main__":
    main()
