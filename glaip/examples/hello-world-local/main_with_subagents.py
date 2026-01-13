"""Hello World - Local Agent with Sub-Agents.

This demonstrates running an agent locally with sub-agents:
- Coordinator agent delegates to specialized agents
- Weather agent has a weather tool
- Math agent has an add tool

Usage:
    uv run main_with_subagents.py

Authors:
    Christian Trisno Sen Long Chen (christian.t.s.l.chen@gdplabs.id)
"""

from dotenv import load_dotenv
from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field

from glaip_sdk.agents import Agent

load_dotenv(override=True)


# ============================================================================
# Tools
# ============================================================================


class WeatherInput(BaseModel):
    """Input for weather tool."""

    city: str = Field(description="City name")


class GetWeatherTool(BaseTool):
    """Get weather for a city."""

    name: str = "get_weather"
    description: str = "Get the current weather for a city"
    args_schema: type[BaseModel] = WeatherInput

    def _run(self, city: str) -> str:
        """Return weather (simulated)."""
        return f"Weather in {city}: Sunny, 25°C"


class AddInput(BaseModel):
    """Input for add tool."""

    a: int = Field(description="First number")
    b: int = Field(description="Second number")


class AddTool(BaseTool):
    """Add two numbers."""

    name: str = "add_numbers"
    description: str = "Add two numbers together"
    args_schema: type[BaseModel] = AddInput

    def _run(self, a: int, b: int) -> str:
        """Add numbers."""
        return f"{a} + {b} = {a + b}"


# ============================================================================
# Agents
# ============================================================================

# Weather specialist - has weather tool
weather_agent = Agent(
    name="weather_agent",
    instruction="You are a weather expert. Use get_weather to answer weather questions.",
    description="Gets weather information",
    tools=[GetWeatherTool],
)

# Math specialist - has add tool
math_agent = Agent(
    name="math_agent",
    instruction="You are a math expert. Use add_numbers to perform addition.",
    description="Performs math calculations",
    tools=[AddTool],
)

# Coordinator - no tools, just delegates
coordinator = Agent(
    name="coordinator",
    instruction="""You are a coordinator. Delegate tasks to:
- weather_agent for weather questions
- math_agent for math questions

Combine their answers into a final response.""",
    description="Coordinates weather and math agents",
    agents=[weather_agent, math_agent],  # Sub-agents
)


def main() -> None:
    """Run the multi-agent example."""
    print("=" * 60)
    print("Hello World - Sub-Agents Example")
    print("=" * 60)
    print()
    print("Agent Hierarchy:")
    print("  📋 Coordinator")
    print("     ├── 🌤️  Weather Agent (has get_weather tool)")
    print("     └── 🔢 Math Agent (has add_numbers tool)")
    print()
    print("-" * 60)

    message = "What's the weather in Tokyo and what is 5 + 7?"
    print(f"User: {message}")
    print("-" * 60)
    print()

    coordinator.run(message, verbose=True)


if __name__ == "__main__":
    main()
