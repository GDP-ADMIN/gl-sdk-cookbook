# ------------------------------
# Local commands for this example
# ------------------------------

.DEFAULT_GOAL := help

.PHONY: help
help: ## Show available targets
	@grep -hE '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2}'

.PHONY: uv-auth
uv-auth: ## Check gcloud auth for the gen-ai-internal uv index
	@if command -v gcloud >/dev/null 2>&1; then \
		gcloud auth print-access-token >/dev/null 2>&1 \
			&& echo "gen-ai-internal auth ready." \
			|| { echo "ERROR: not logged in. Run 'gcloud auth login'."; exit 1; }; \
	else \
		echo "ERROR: gcloud CLI not found. Install Google Cloud SDK and run 'gcloud auth login'."; exit 1; \
	fi

.PHONY: sync
sync: uv-auth ## Install dependencies with uv
	UV_INDEX_GEN_AI_INTERNAL_USERNAME=oauth2accesstoken \
	UV_INDEX_GEN_AI_INTERNAL_PASSWORD="$$(gcloud auth print-access-token)" \
	uv sync

.PHONY: run
run: ## Run the example (main.py)
	uv run main.py
