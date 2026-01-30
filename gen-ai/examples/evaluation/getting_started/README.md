## ⚙️ Prerequisites

Please refer to prerequisites [here](../../../README.md).

Additional prerequisites for this example:
- [gcloud CLI](https://cloud.google.com/sdk/docs/install) - required because `gllm-evals` is a private library hosted in a private Google Cloud repository
- [Google API Key](https://aistudio.google.com/api-keys) - required for the LLM-as-judge evaluator

After installing gcloud CLI, please run:

```bash
gcloud auth login
```

## 🚀 Getting Started

1. **Clone the repository & open the directory**

   ```bash
   git clone https://github.com/GDP-ADMIN/gl-sdk-cookbook.git
   cd gl-sdk-cookbook/gen-ai/examples/evaluations/getting_started
   ```

2. **Set UV authentication**  
   Since UV will need to be able to access our private registry to download the required packages, please also set the following environment variables:
   
   ```bash
   export UV_INDEX_GEN_AI_INTERNAL_USERNAME=oauth2accesstoken
   export UV_INDEX_GEN_AI_INTERNAL_PASSWORD="$(gcloud auth print-access-token)"
   ```

3. **Install dependency via UV**
   
   ```bash
   uv lock
   uv sync
   ```

4. **Prepare `.env` file**  
   Create a file called `.env`, then set the Google API key as an environment variable.
   
   ```env
   GOOGLE_API_KEY="AIz..."
   ```

5. **Run the example**

   ```bash
   uv run eval.py
   ```

6. **Expected Output**

   You should see a response similar to the following:

   ```
   Running evaluation...
   Query: What is the capital of France?
   Expected Response: Paris
   Generated Response: New York
   Retrieved Context: Paris is the capital of France.

   ================================================================================

   Evaluation Results:
   ================================================================================

   Overall Score: 0.0
   Average Score: 0.6
   Binary Score: 0
   Relevancy Rating: bad

   The following metrics failed to meet expectations:
   1. Completeness is 1 (should be 3)
   2. Groundedness is 1 (should be 3)

   Possible Issues: Retrieval Issue, Generation Issue

   Metric Breakdown:
   --------------------------------------------------------------------------------

   COMPLETENESS:
     Score: 1
     Normalized Score: 0.0
     Explanation: The output provides a critical factual contradiction by stating that New York is the capital of France, whereas the expected answer is Paris.

   GROUNDEDNESS:
     Score: 1
     Normalized Score: 0.0
     Explanation: The output 'New York' is a direct contradiction of the retrieval context, which explicitly states that 'Paris is the capital of France.' Because the information provided is factually incorrect and not grounded in the context, it receives the lowest score.

   REDUNDANCY:
     Score: 1
     Normalized Score: 1.0
     Explanation: The response provides a single, direct answer without any repetition of words, phrases, or ideas. It is concise and contains no redundant statements or restatements.

   LANGUAGE CONSISTENCY:
     Score: 1
     Normalized Score: 1.0
     Explanation: The instructional language of the input is English, and the actual output is also written in English, maintaining language consistency regardless of the factual accuracy of the answer.

   REFUSAL ALIGNMENT:
     Score: 1
     Normalized Score: 1.0
     Explanation: is_refusal was detected from the expected response, which directly provides the answer 'Paris' without refusal indicators. The actual output 'New York' is factually incorrect, but it also contains no refusal indicators and attempts to answer the core request. Since both the expected and actual responses are not refusals, they align correctly.
   ```

## 📚 What's Happening?

This example demonstrates a basic RAG pipeline evaluation using the `GEvalGenerationEvaluator`. The evaluator:

1. **Compares** the generated response against the expected response
2. **Evaluates** multiple metrics:
   - **Completeness**: How complete is the answer compared to expectations
   - **Groundedness**: How well the answer is grounded in the retrieved context
   - **Redundancy**: Whether the answer contains unnecessary repetition
   - **Language Consistency**: Whether the response language matches the query language
   - **Refusal Alignment**: Whether the refusal behavior matches expectations

3. **Provides** detailed explanations for each metric score

In this example, the generated response ("New York") is incorrect, so it receives low scores for completeness and groundedness, but performs well on other metrics.

## 🚀 Reference

This example is based on the [GL SDK Gitbook documentation Evaluations Getting Started page](https://gdplabs.gitbook.io/sdk/tutorials/evaluations/getting-started).
