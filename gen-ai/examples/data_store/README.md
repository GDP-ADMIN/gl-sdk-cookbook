## ⚙️ Prerequisites

Please refer to prerequisites [here](../../../README.md).

## 🚀 Getting Started

1. **Clone the repository & open the directory**

   ```bash
   git clone https://github.com/GDP-ADMIN/gl-sdk-cookbook.git
   cd gl-sdk-cookbook/gen-ai/examples/data_store/
   ```

2. **Set UV authentication**  
   Since UV will need to be able to access our private registry to download the required packages, please also set the following environment variables:

   ```env
   UV_INDEX_GEN_AI_INTERNAL_USERNAME=oauth2accesstoken
   UV_INDEX_GEN_AI_INTERNAL_PASSWORD="$(gcloud auth print-access-token)"
   ```

3. **Install dependency via UV**

   ```bash
   uv lock
   uv sync
   ```

4. **Prepare `.env` file**  
   Create a file called `.env`, then set the OpenAI API key as an environment variable.

   ```env
   OPENAI_API_KEY="..."
   ```

5. **Run the example**

   ```bash
   uv run indexing.py
   ```

## 🚀 Reference

These examples are based on the [GL SDK Gitbook documentation How-to-Guide page](https://gdplabs.gitbook.io/sdk/how-to-guides/index-your-data-with-vector-data-store).
