"""
Getting Started with GenAI Evaluations.

This script demonstrates how to run a basic RAG pipeline evaluation using GEvalGenerationEvaluator.
"""

import asyncio
import os

from dotenv import load_dotenv
from gllm_evals.evaluator.geval_generation_evaluator import GEvalGenerationEvaluator
from gllm_evals.types import RAGData


async def main() -> None:
    """
    Run a simple RAG evaluation example.

    This example evaluates a RAG pipeline output by comparing the generated response
    with the expected response using multiple metrics including completeness,
    groundedness, redundancy, language consistency, and refusal alignment.
    """
    # Load environment variables
    load_dotenv()

    # Initialize the evaluator with Google API credentials
    # By default, GEvalGenerationEvaluator uses Gemini 3 Pro from Google
    evaluator = GEvalGenerationEvaluator(model_credentials=os.getenv("GOOGLE_API_KEY"))

    # Create sample RAG data for evaluation
    data = RAGData(
        query="What is the capital of France?",
        expected_response="Paris",
        generated_response="New York",
        retrieved_context="Paris is the capital of France.",
    )

    print("Running evaluation...")
    print(f"Query: {data.query}")
    print(f"Expected Response: {data.expected_response}")
    print(f"Generated Response: {data.generated_response}")
    print(f"Retrieved Context: {data.retrieved_context}")
    print("\n" + "=" * 80 + "\n")

    # Run the evaluation
    result = await evaluator.evaluate(data)

    # Display results
    print("Evaluation Results:")
    print("=" * 80)
    print(f"\nOverall Score: {result['generation']['score']}")
    print(f"Average Score: {result['generation']['avg_score']}")
    print(f"Binary Score: {result['generation']['binary_score']}")
    print(f"Relevancy Rating: {result['generation']['relevancy_rating']}")

    print(f"\n{result['generation']['global_explanation']}")

    if result["generation"].get("possible_issues"):
        print(
            f"\nPossible Issues: {', '.join(result['generation']['possible_issues'])}"
        )

    print("\nMetric Breakdown:")
    print("-" * 80)

    # Display individual metrics
    metrics = [
        "completeness",
        "groundedness",
        "redundancy",
        "language_consistency",
        "refusal_alignment",
    ]
    for metric in metrics:
        if metric in result["generation"]:
            metric_data = result["generation"][metric]
            print(f"\n{metric.upper().replace('_', ' ')}:")
            print(f"  Score: {metric_data['score']}")
            print(f"  Normalized Score: {metric_data['normalized_score']}")
            print(f"  Explanation: {metric_data['explanation']}")


if __name__ == "__main__":
    asyncio.run(main())
