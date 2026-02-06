FROM python:3.11-slim

# Minimal environment for running tests and spec checks
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential make git ca-certificates && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

# Copy entire repository into the container (read-only semantics are up to the runner)
COPY . /workspace

# Install only test/runtime tools required for local validation
RUN python -m pip install --no-cache-dir --upgrade pip setuptools
RUN python -m pip install --no-cache-dir pytest

# Default command is a Makefile helper; running the container without args shows help
CMD ["make", "help"]
