
These are the commands i run on the chat

specify init


specify create spec system.autonomous_influencer

specify create spec influencer.trend_research
specify create spec influencer.content_generation
specify create spec influencer.post_scheduler
specify create spec influencer.engagement_manager
specify create spec influencer.analytics_feedback_loop


specify create test influencer.trend_research


specify create spec mcp.sense
specify create spec mcp.data
specify create spec mcp.execution


specify create spec skill.extract_trends
specify create spec skill.generate_caption
specify create spec skill.rank_engagement


specify create spec agent.researcher
specify create spec agent.creator
specify create spec agent.publisher
specify create spec agent.governor

And some of the prompts i used for the project are the followings...

You are acting as a DevSecOps Engineer responsible for CI/CD and AI governance
for Project Chimera.

This task is Task 3.3: CI/CD & AI Governance.

Your responsibility is to ensure that every code change is automatically
validated and reviewed for specification alignment and security risks.

DO NOT implement application logic.
DO NOT modify specs.
DO NOT add deployment or release steps.

---

### Required Output

Create or update the following files:

1. .github/workflows/main.yml
2. .coderabbit.yaml (or equivalent AI review policy file)

---

## Part 1: CI/CD Pipeline

### main.yml Requirements

- Trigger on every push and pull request
- Run inside a clean environment
- Execute `make test`
- Failing tests MUST block the pipeline
- No deployment or publishing steps
- No secrets or credentials

---

## Part 2: AI Review Policy

### .coderabbit.yaml Requirements

Configure the AI reviewer to explicitly check for:

#### Spec Alignment
- Ensure code changes reference relevant files in `specs/`
- Flag any implementation code added without spec updates
- Flag missing or ambiguous acceptance criteria

#### Security Review
- Detect potential security vulnerabilities
- Highlight unsafe patterns (e.g., hardcoded secrets)
- Warn about unchecked external calls

---

### Governance Constraints

- AI reviewers MUST NOT approve code that violates specs
- Human approval is required for spec changes
- Automated reviews supplement, not replace, human oversight

---

### Style & Tone

- Use clear, enforceable language
- Avoid marketing or conversational tone
- Prefer explicit rules over general guidance

---

### Before Writing Files

First:
- Describe the intended CI/CD and review workflow
- List any assumptions you are making

Only after that:
- Generate the complete `main.yml`
- Generate the complete `.coderabbit.yaml`

If any requirement is unclear, STOP and ask for clarification.
Do not invent behavior.


You are acting as a CloudOps Engineer for Project Chimera.

Your task is to containerize the development environment and standardize
developer commands using a Dockerfile and a Makefile.

This task is Task 3.2: Containerization & Automation.

DO NOT implement application logic.
DO NOT attempt to make tests pass.
DO NOT add runtime services or background processes.

---

### Required Output

Create or update the following files at the repository root:

1. Dockerfile
2. Makefile

---

### Dockerfile Requirements

- Use an official, minimal base image (e.g., python:3.x-slim)
- Install only what is required to run tests and validation
- Copy the repository into the container
- Set a default command that allows running make targets
- Do NOT include credentials or secrets
- Do NOT run the application

---

### Makefile Requirements

The Makefile MUST include the following targets:

#### make setup
- Builds the Docker image
- Installs dependencies inside the container
- No host-level installs allowed

#### make test
- Runs the test suite inside Docker
- Tests are EXPECTED to fail
- The command MUST still execute cleanly

#### make spec-check (optional but recommended)
- Verifies that code changes align with specs
- May call an existing script or placeholder validator
- MUST fail if specs are missing or malformed

---

### Constraints

- All commands MUST be deterministic
- No assumptions about local developer environments
- No external services
- Prefer clarity over optimization

---

### Before Writing Files

First:
- Explain the intended workflow for a developer using Docker + Make
- List any assumptions you are making

Only after that:
- Generate the Dockerfile
- Generate the Makefile

If any requirement is ambiguous, STOP and ask for clarification.
Do not invent behavior.

You are acting as a Test Architect for Project Chimera.

Your task is to write FAILING tests that define the expected behavior of the
system, based strictly on the specifications in `specs/technical.md`.

These tests are NOT meant to pass yet.
They define the contract that future agents must satisfy.

DO NOT implement any application logic.
DO NOT modify skills implementations.
DO NOT mock behavior that does not yet exist.

---

### Required Output

Create a `tests/` directory containing the following files:

1. tests/test_trend_fetcher.py
2. tests/test_skills_interface.py

---

### Global Test Rules (Non-Negotiable)

- Tests MUST be derived directly from `specs/technical.md`
- Tests MUST fail when executed
- Tests MUST assert structure and interfaces, not behavior
- No test may include business logic
- No test may import runtime implementations that do not yet exist

---

## File-Specific Instructions

### 1. test_trend_fetcher.py

Purpose:
Assert that the trend data structure returned by the system matches the API
contract defined in `specs/technical.md`.

Requirements:
- Read the trend-fetching API schema from the spec
- Assert required keys and value types
- Do NOT provide a fake implementation
- Use placeholders or NotImplementedError where necessary

Example intent (do not copy blindly):
- Assert that trend results include:
  - topic (string)
  - source (string)
  - timestamp (ISO 8601 string)

---

### 2. test_skills_interface.py

Purpose:
Assert that skill modules under `skills/` expose the correct callable interfaces.

Requirements:
- Discover skill directories under `skills/`
- Assert each skill defines a callable entry point (e.g., run or execute)
- Assert expected input parameter names and structure as defined in skill READMEs
- Tests MUST fail because no implementations exist yet

---

### Technical Constraints

- Use pytest
- No external API calls
- No fixtures that simulate success
- Prefer explicit assertion errors over mocks

---

### Before Writing Tests

First:
- Summarize the relevant sections of `specs/technical.md` you are basing tests on
- List the assumptions being encoded into the tests

Only after that:
- Generate the test files

If a spec is ambiguous or missing:
- Encode the ambiguity as a failing assertion
- Do NOT invent behavior

Do not attempt to make tests pass.

