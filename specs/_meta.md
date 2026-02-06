# Project Chimera — Specification Meta

System Purpose and High-Level Vision
- Project Chimera MUST provide a spec-driven platform for autonomous agents that coordinate to create, research, govern, and publish content and data artifacts within a controlled operational boundary.
- The repository and its specifications SHALL be the single source of truth for behavior, interfaces, and acceptance criteria prior to any implementation.

Non-Functional Constraints (Governance, Safety, Scale)
- Safety: All runtime agents and skills MUST operate under governance controls that prevent unauthorized data exfiltration and disallowed actions.
- Scale: The system SHALL support interactive agent flows over moderate-sized corpora (up to 10k items) in Phase 0; higher scale SHALL be explicitly specified before implementation.
- Observability: All agent decisions that affect external state or approvals SHALL be auditable with provenance metadata.

Specification Authority
- These specification documents (files under `specs/`) SHALL override any subsequent implementation code and SHALL be treated as authoritative.
- No implementation SHALL proceed without a passing spec validation and an approved change to these specification files.

Spec-Driven Development Enforcement
- Project Chimera MUST follow Spec-Driven Development: designs, interfaces, and acceptance criteria MUST be captured in `specs/` and validated before implementation commits are merged.
- Any change to behavior MUST be reflected in `specs/` and pass the repository's spec validation CI gate prior to code changes.
