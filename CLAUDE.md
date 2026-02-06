Project Context

“This is Project Chimera, an autonomous influencer system.”

- Project Chimera MUST use Spec-Driven Development. Specifications under `specs/` SHALL be the single source of truth and SHALL override implementation.

Prime Directive

**NEVER generate or modify implementation code without checking the `specs/` directory first.**

- Specs are the authoritative source for behavior and interfaces. If required specification files or explicit Acceptance Criteria are missing or ambiguous, the agent MUST stop and ask clarifying questions before proceeding.

Traceability & Planning

- Before writing any code, the agent MUST explain its plan, list steps, and cite specific specification files and requirement IDs that the changes address.
- The agent MUST describe how each planned change satisfies the Acceptance Criteria referenced in the cited specs.
- “Before writing any code, explain the plan and cite the relevant specifications.”

Forbidden Behaviors (MUST NOT)

- MUST NOT write code without explicit alignment to the `specs/` directory.
- MUST NOT invent, add, or assume requirements that are not present in `specs/` without asking and recording a spec update.
- MUST NOT bypass governance, CI, or spec validation steps.
- MUST NOT make unverified assumptions when specs are unclear; instead the agent MUST stop and request clarification.

Allowed Behaviors (MUST)

- The agent MUST ask clarifying questions when specifications are missing, ambiguous, or insufficient.
- The agent MUST propose spec updates via the repository’s specification workflow (for example: `/specify`) rather than altering implementation.
- The agent MAY propose refactors only when the applicable spec explicitly allows refactoring; such proposals MUST reference the spec and include an explicit plan.

Enforcement and Style

- All rules in this file MUST be applied deterministically by IDE assistants operating in this repository.
- Language in interactions and outputs MUST use MUST / MUST NOT normative terms when referring to repository policy.
- This file is concise and enforceable; agents operating in the workspace MUST comply.
