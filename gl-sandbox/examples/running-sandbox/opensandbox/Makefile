# ------------------------------
# Local commands for this example
# ------------------------------

.DEFAULT_GOAL := help

.PHONY: help
help: ## Show available targets
	@grep -hE '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2}'

.PHONY: sync
sync: ## Install dependencies with uv
	uv sync

.PHONY: run
run: ## Run the example (main.py)
	uv run main.py
