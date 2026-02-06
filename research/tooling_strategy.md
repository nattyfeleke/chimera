# Developer Tooling Strategy — MCP Servers

Purpose and Scope
- This document describes developer-facing Model Context Protocol (MCP) servers selected to assist HUMAN developers working on Project Chimera. These developer MCP servers are for developer productivity only and MUST NOT become runtime dependencies for Chimera agents.
- Developer MCP servers MUST NOT be used by production agents; runtime MCP servers are a separate category and are explicitly out of scope for this document.

Developer vs Runtime Separation (Directive)
- Developer MCP servers are tools for humans during development and debugging. They MUST NOT be assumed to provide production behavior or be available to runtime agents.
- All developer MCP outputs MUST be treated as advisory and MUST NOT bypass repository governance, spec validation, or CI gates.

Selected Developer MCP Servers

1) git-mcp
-----------------
Purpose
- Provide repository-level context to developers: branch lists, commit history, diffs, and blame information.

Why Useful for this Repo
- The repository is spec-driven (`specs/`), contains governance artifacts (`CLAUDE.md`), and enforces CI spec-validation. Developers MUST be able to map proposed code or spec changes to commits and requirement IDs.

Capabilities (high level)
- Read repository references: branches, tags, commit metadata.
- Provide diffs and file-level changes for proposed edits.
- Surface blame/author information for lines or files.

Must NOT be used for
- MUST NOT be used by runtime agents as a production dependency.
- MUST NOT modify the repository state automatically without explicit human authorization (no auto-commit or push actions performed by MCP servers on behalf of agents).
- MUST NOT bypass spec validation or CI gating by fabricating commit metadata.

2) filesystem-mcp
-----------------
Purpose
- Offer read-only, high-fidelity access to repository files and directory structure for contextual analysis and code-assist tasks.

Why Useful for this Repo
- Developers working on specs (`specs/`), skills (`skills/`), and governance files (`CLAUDE.md`) require a consistent, fast view of project files to reference requirement IDs and to craft compliant changes.

Capabilities (high level)
- Read file contents and list directories.
- Support contextual search (file paths, headings, requirement IDs) and present file snippets.

Must NOT be used for
- MUST NOT be used to perform write operations or side effects in the repository without explicit human action and a validated spec change.
- MUST NOT expose secrets or credentials; any sensitive content MUST remain guarded by repository access controls.

3) spec-mcp
-----------------
Purpose
- Provide specialized tooling focused on the `specs/` directory: validate presence of required sections (Acceptance Criteria), extract requirement IDs, and surface missing normative language (MUST / MUST NOT).

Why Useful for this Repo
- Project Chimera enforces Spec-Driven Development and a CI gate that fails when specs or Acceptance Criteria are missing. Developers MUST be able to run fast, local validations and retrieve the exact requirement IDs to reference in proposals and PR descriptions.

Capabilities (high level)
- Parse spec documents under `specs/`, list requirement IDs and acceptance criteria.
- Report missing mandatory sections or normative language for quick remediation.
- Provide cross-references between specs and proposed tasks or code changes.

Must NOT be used for
- MUST NOT itself alter spec files; it MUST only report and suggest.
- MUST NOT be consumed by runtime agents as the authoritative enforcement mechanism; CI and governance remain the authoritative validators.

4) ci-mcp (test-runner / ci introspector)
-----------------
Purpose
- Surface CI pipeline status, failing jobs, and test-run outputs to developers so they can iterate locally and understand gating failures.

Why Useful for this Repo
- The repository includes CI gates that validate specs and block merges. Developers MUST be able to see which checks fail, the failing files, and concise error snippets to triage quickly.

Capabilities (high level)
- Report job statuses and failing step logs.
- Link failing tests or spec-validation errors to file paths and requirement IDs where possible.

Must NOT be used for
- MUST NOT be used to circumvent CI policies or to mark jobs as passing without actual remediation.
- MUST NOT be integrated into production agents or runtime flows.

Developer MCPs Do Not Bypass Governance
- Developer MCP servers are explicitly advisory and MUST NOT bypass specifications, governance, or CI validation. Any proposed change surfaced by an MCP server MUST be implemented only after updating `specs/` (if required), passing spec validation, and following repository CI procedures.

Notes
- This document lists developer tooling recommendations only; it contains no setup or operational instructions. Selection is based on current repository structure: `specs/`, `skills/`, `tests/`, `CLAUDE.md`, and CI enforcement for specs.
