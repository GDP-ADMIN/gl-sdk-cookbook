"""Travel Planning Assistant - Modular Tool Integration.

Authors:
    Christian Trisno Sen Long Chen (christian.t.s.l.chen@gdplabs.id)
"""

from glaip_sdk import Agent
from tools.flight_status import FlightStatusTool
from tools.stock_checker import StockCheckerTool
from tools.travel_math import TravelMathTool
from tools.weather import WeatherTool


def main():
    """Run travel assistant with modular tools."""
    
    agent = Agent(
        name="travel-planning-assistant",
        instruction="""You are a travel planning assistant. Use the available tools to help users with flight status 
        checks, weather information, stock prices, and travel budget calculations. Use the tools as needed based on 
        the user's request.""",
        tools=[WeatherTool, FlightStatusTool, StockCheckerTool, TravelMathTool],
    )

    agent.run("Check flight GA123 and weather in Bali.")


if __name__ == "__main__":
    main()
