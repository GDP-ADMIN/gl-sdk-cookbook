"""Travel budget calculator tool for the travel assistant example.

Demonstrates a simple, single-file tool implementation.

Authors:
    Christian Trisno Sen Long Chen (christian.t.s.l.chen@gdplabs.id)
"""

from typing import Any

from langchain_core.tools import BaseTool


class TravelMathTool(BaseTool):
    """Tool for performing travel-related calculations."""

    name: str = "travel_calculator"
    description: str = "Performs currency conversion and travel budget calculations."

    def _run(self, expression: str, **kwargs: Any) -> str:
        """Perform calculation logic.

        Args:
            expression: The arithmetic expression to evaluate.
            **kwargs: Additional execution arguments.

        Returns:
            Calculation result string.
        """
        return f"Calculation result for '{expression}': 1250.00"
