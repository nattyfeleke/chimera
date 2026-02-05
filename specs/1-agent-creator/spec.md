# Feature Specification: Agent — Creator

**Feature Branch**: `1-agent-creator`
**Created**: 2026-02-06
**Status**: Draft
**Input**: User description: "create spec agent.creator"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Create a Content Piece (Priority: P1)

An author or agent requests generation of a content piece (post, short article, social caption) with parameters (length, tone, keywords). The agent returns a finished draft, optional metadata (headline, tags), and provenance about prompts or sources.

**Why this priority**: Core content creation capability to speed authoring and automation.

**Independent Test**: Provide a content brief and verify the generated draft meets constraints (length, includes required keywords) and includes provenance fields.

**Acceptance Scenarios**:
1. **Given** a brief requesting a 200-word promotional post including keyword X, **When** the creator runs, **Then** output is ~200 words and contains keyword X.

---

### User Story 2 - Template-driven Batch Creation (Priority: P2)

Users supply a template and a list of inputs (e.g., product names); the agent produces a caption per input, following template and per-item constraints.

**Why this priority**: Enables scalable content production for campaigns.

**Independent Test**: Run a batch of 50 items with a template and verify each result follows template placeholders.

**Acceptance Scenarios**:
1. **Given** a template "Buy {product} now!", **When** batch runs, **Then** each caption substitutes `{product}` correctly.

---

### User Story 3 - Safety, Style Controls & Review Workflow (Priority: P3)

Outputs pass safety filters, adhere to brand/style rules when provided, and support a lightweight review/approval flow with suggested edits.

**Why this priority**: Ensures published content is safe and brand-consistent.

**Independent Test**: Provide brand constraints and unsafe prompts; verify outputs conform or are rejected and review workflow records decisions.

**Acceptance Scenarios**:
1. **Given** brand rule that forbids certain phrases, **When** the creator runs, **Then** output avoids those phrases or flags for review.

---

## Constitution Compliance (mandatory)

- **Code Quality**: Unit tests for template rendering, parameter validation, and safety-filter integration; CI linting for new modules.
- **Testing**: Unit tests, integration tests for end-to-end generation, and human-evaluation tests for quality and brand adherence.
- **User Experience Consistency**: Reuse MCP UI patterns for briefs, templates, and approval flows.
- **Performance Requirements**: Interactive single-item runs meet latency SLOs; batch runs use job/queue semantics.
- **Observability & Versioning**: Emit run metrics, record model/skill version and prompt provenance, and log review decisions.

### Edge Cases

- Missing or contradictory constraints: return actionable error or ask for clarification.
- Repetitive/bulk content: detect near-duplicates and surface warnings.
- Requests that require PII or sensitive claims: refuse or route to human review.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The agent MUST accept a creation request with `brief`, `constraints` (length, tone, keywords), `template` (optional), and `output_type` (single, batch).
- **FR-002**: The agent MUST generate content that respects provided constraints and return `result`, `metadata` (word_count, tags), and `provenance` (skill_version, prompt_used).
- **FR-003**: The agent MUST support batch template substitution with per-item inputs and return per-item status.
- **FR-004**: The agent MUST apply safety filters and mark outputs that require human review or rejection.
- **FR-005**: The agent MUST allow optional brand/style rules to be supplied and enforce them where possible [NEEDS CLARIFICATION: level of style control required (presets only vs. custom rule sets)?]
- **FR-006**: The agent MUST provide a lightweight review/approval API to accept, edit, or reject outputs and record reviewer decisions.
- **FR-007**: The agent MUST log provenance and support reproducibility of outputs given the same brief and skill version.

### Key Entities *(include if feature involves data)*

- **CreationRequest**: (id, requester, brief, constraints, template, inputs, requested_at)
- **CreationResult**: (id, request_id, text, metadata, provenance, status)
- **ReviewRecord**: (id, result_id, reviewer, decision, notes, reviewed_at)
- **StyleRuleSet**: (id, owner, rules, examples)

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Interactive single-item creation returns a usable draft within 10 seconds for 95% of requests in Phase 0 pilot.
- **SC-002**: Human evaluation: >= 80% of generated drafts rated "acceptable" or better for clarity and relevance on representative briefs.
- **SC-003**: Safety: 100% of tested unsafe prompts are flagged or result in safe fallback/rejection in pilot tests.
- **SC-004**: Batch runs of 100 items complete with per-item success rate >= 95% under pilot load.

## Assumptions

- Phase 0 focuses on short-to-medium content (captions, short posts, ~50-400 words); long-form writing and multi-stage editing flows are out-of-scope unless clarified.
- Style rules will be supplied as simple templates or presets initially; advanced rule engines can be added later.

## Open Questions

- [NEEDS CLARIFICATION: level of style control required (presets only vs. custom rule sets)?]

---

*End of spec draft.*
