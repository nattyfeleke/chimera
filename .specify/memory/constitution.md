<!--
Sync Impact Report

- Version change: TEMPLATE -> 1.0.0
- Modified principles:

- Version change: TEMPLATE -> 1.0.0
- Modified principles:
  - Code Quality
  - Test-First & Testing Standards
  - User Experience Consistency
  - Performance Requirements
  - Observability & Versioning
- Added sections: none (principles added into Core Principles)
- Removed sections: none
- Templates updated: .specify/templates/plan-template.md ✅, .specify/templates/spec-template.md ✅, .specify/templates/tasks-template.md ✅
- Follow-up TODOs: RATIFICATION_DATE left as TODO for project maintainers
-->

# Chimera Constitution

## Core Principles

### Code Quality
All code MUST be readable, maintainable, and reviewable. Code quality requirements:
- MUST adhere to agreed linters and formatting rules; PRs failing linters are NOT mergeable.
- MUST include clear naming, minimal cognitive complexity, and inline rationale for non-obvious choices.
- SHOULD limit PR size to a scope that reviewers can reasonably evaluate in one sitting (suggestion: <400 lines).
Rationale: High-quality code reduces long-term maintenance cost and increases reviewer throughput.

### Test-First & Testing Standards (NON-NEGOTIABLE)
Testing requirements:
- MUST follow a test-first workflow: tests (unit, integration, contract) are written and observed to fail before implementation begins.
- MUST include automated unit tests for logic, integration tests for interactions, and contract tests for public interfaces where applicable.
- MUST set measurable coverage targets for critical modules; coverage is a signal, not the sole gate—tests MUST assert behavior.
- All CI pipelines MUST run tests and fail on regressions; flaky tests MUST be tracked and fixed promptly.
Rationale: Enforcing test-first practices preserves correctness and enables safe refactoring.

### User Experience Consistency
UX requirements:
- MUST follow the project's design system and accessibility guidelines; deviations require explicit design approval and rationale.
- MUST provide consistent error states, messaging tone, and affordances across UI surfaces and CLI/SDK interfaces.
- SHOULD include small, testable user journeys in specs and acceptance criteria that validate UX consistency.
Rationale: Consistent UX reduces cognitive load for users and support burden for the team.

### Performance Requirements
Performance requirements:
- MUST define performance goals in each plan/spec (e.g., latency p95, memory budget, throughput targets).
- Critical paths MUST include benchmarks and a simple performance regression test where practical.
- Changes that materially affect performance MUST include before/after measurements and an acceptance threshold.
Rationale: Explicit performance expectations prevent regressions and ensure acceptable user experience at scale.

### Observability & Versioning
Operational and release requirements:
- MUST include structured logging, meaningful metrics, and error reporting where applicable to enable rapid diagnosis.
- MUST follow semantic versioning for published packages and document breaking changes in CHANGELOGs and migration notes.
- SHOULD include health checks and basic runtime diagnostics for services in production.
Rationale: Observability and clear versioning enable safe operations and evolution of the system.

## Additional Constraints
Security, compliance, and stack choices are documented in each feature plan. Any deviation from default stacks
MUST be justified in the plan and reviewed by an appropriate owner.

## Development Workflow & Quality Gates
- All PRs MUST include: linked plan/spec, tests demonstrating behavior, and a short description of how the change
	satisfies the relevant constitution principles (Code Quality, Testing, UX, Performance, Observability).
- CI gates MUST enforce linting, tests, and basic build verification. Performance and UX gates are added per-plan when
	the plan marks a component as critical for those principles.

## Governance
Amendments and versioning:
- This constitution is the authoritative source for engineering principles. Changes MUST be documented as an amendment
	with a rationale and migration plan.
- Versioning policy: initial ratification sets `1.0.0`. MAJOR increments are required for backward-incompatible governance
	changes; MINOR for added principles or material expansions; PATCH for clarifications and wording fixes.
- Compliance reviews: major projects or infra changes MUST include a short compliance checklist mapping to the relevant
	principles; maintainers may request follow-up remediation tasks.

**Version**: 1.0.0 | **Ratified**: TODO(RATIFICATION_DATE): Provide original adoption date | **Last Amended**: 2026-02-06
