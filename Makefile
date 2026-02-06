IMAGE_NAME := chimera-dev:latest

.PHONY: setup test spec-check help

setup:
	@echo "Building Docker image $(IMAGE_NAME)..."
	docker build -t $(IMAGE_NAME) .

test:
	@echo "Running test suite inside Docker (expected to fail)..."
	docker run --rm -v $(PWD):/workspace -w /workspace $(IMAGE_NAME) pytest -q

spec-check:
	@echo "Running basic spec validation inside Docker..."
	# Basic validator: ensure 'Acceptance Criteria' appears in spec files
	docker run --rm -v $(PWD):/workspace -w /workspace $(IMAGE_NAME) sh -c "grep -R \"Acceptance Criteria\" specs || (echo 'Spec validation failed: missing Acceptance Criteria' >&2; exit 2)"

help:
	@echo "Available targets:"
	@echo "  make setup       - build the development Docker image"
	@echo "  make test        - run pytest inside the container (tests expected to fail)"
	@echo "  make spec-check  - run basic spec validation (fails if Acceptance Criteria missing)"
