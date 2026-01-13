"""Travel Planning Assistant - Modular Tool Integration.

Authors:
    Christian Trisno Sen Long Chen (christian.t.s.l.chen@gdplabs.id)
"""

from dotenv import load_dotenv
from glaip_sdk import Agent
from tools.flight_status import FlightStatusTool
from tools.stock_checker import StockCheckerTool
from tools.travel_math import TravelMathTool
from tools.weather import WeatherTool


def main():
    """Run travel assistant with modular tools."""
    load_dotenv()

    agent = Agent(
        name="travel-planning-assistant",
        instruction="Help with flight status, weather, stocks, and budgets.",
        tools=[WeatherTool, FlightStatusTool, StockCheckerTool, TravelMathTool],
    )

    agent.deploy()
    agent.run("Check flight GA123 and weather in Bali.")
    agent.delete()


if __name__ == "__main__":
    main()
