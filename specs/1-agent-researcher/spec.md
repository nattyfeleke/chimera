# Feature Specification: Agent — Researcher

**Feature Branch**: `1-agent-researcher`
**Created**: 2026-02-06
**Status**: Draft
**Input**: User description: "create spec agent.researcher"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - One-off Research Brief (Priority: P1)

A user or agent requests a concise research brief on a topic (query, scope, constraints). The agent gathers sources, synthesizes findings, returns a short summary with key points, and includes citations to source items.

**Why this priority**: Core research capability — delivers actionable knowledge quickly.

**Independent Test**: Provide a defined topic and ground-truth references; run the agent and verify the summary contains the expected key points and at least N verified citations.

**Acceptance Scenarios**:
1. **Given** a topic and scope, **When** the researcher runs, **Then** it returns a summary <= requested length, with at least 3 cited sources relevant to the topic.

---

### User Story 2 - Evidence Dossier with Source Links (Priority: P2)

The agent compiles an evidence dossier: structured list of claims, each linked to source excerpts (quote/snippet, URL/ID, timestamp) and a provenance record for verification.

**Why this priority**: Supports auditability and follow-up investigation.

**Independent Test**: Ask for dossier on a factual question and verify each claim has at least one source excerpt and a resolvable link.

**Acceptance Scenarios**:
1. **Given** a factual question, **When** the dossier is produced, **Then** every claim includes a source reference and excerpt or a clear note if no source found.

---

### User Story 3 - Ongoing Research Monitor (Priority: P3)

Users subscribe to topics; the agent periodically searches for new evidence, sends summaries of significant changes, and updates dossiers.

**Why this priority**: Keeps stakeholders informed about evolving topics without manual checks.

**Independent Test**: Subscribe to a topic and publish a new relevant article; verify the monitor notifies subscribers within the configured interval.

**Acceptance Scenarios**:
1. **Given** an active subscription, **When** new high-relevance content appears, **Then** subscribers receive a digest with links and a short summary within the configured delivery window.

---

## Constitution Compliance (mandatory)

- **Code Quality**: Unit tests for source fetching, deduplication, citation formatting, and summary synthesis. Linting and CI checks added for new modules.
- **Testing**: Unit tests for extractors, integration tests covering end-to-end research flows, and human review tests for summary quality.
- **User Experience Consistency**: Reuse MCP UX patterns for request forms, summary display, and provenance links.
- **Performance Requirements**: Interactive briefs should meet latency targets (see Success Criteria); monitor and backpressure for periodic monitoring.
- **Observability & Versioning**: Emit metrics for run count, latency, citation counts, and maintain versioned skill/artifact identifiers.

### Edge Cases

- Conflicting sources: surface conflicts and label confidence levels instead of forcing a single conclusion.
- Paywalled or inaccessible sources: record inability to verify and include alternative open references where possible.
- High-volume source floods (Storming): rate-limit source fetching and surface top-k representative items.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The agent MUST accept a research request with `topic`, `scope` (time window, domains), `output_type` (brief, dossier), and `constraints` (length, citation-count).
- **FR-002**: The agent MUST search configured sources (web, internal docs, datasets) and aggregate candidate evidence items with metadata (source id/URL, excerpt, timestamp).
- **FR-003**: The agent MUST synthesize a coherent summary and attach citations for claims (source id/URL and excerpt) while preserving provenance.
- **FR-004**: The agent MUST deduplicate and rank evidence by relevance and freshness.
- **FR-005**: The agent MUST support subscription-based monitoring for topics with configurable cadence and significance thresholds.
- **FR-006**: The agent MUST log run provenance (request parameters, skill version, source list) for reproducibility and auditing.
- **FR-007**: The agent MUST enforce access control for sensitive sources and restrict outputs accordingly [NEEDS CLARIFICATION: required permission model for accessing internal/sensitive sources (role-based, token-scoped, or other)?]
- **FR-008**: The agent MUST present explainability: for each assertion in a dossier, display the source excerpt and a confidence indicator.
- **FR-009**: The agent MUST allow configurable citation style (inline, numbered, footnote) and indicate which style was used [NEEDS CLARIFICATION: preferred default citation style for Phase 0 (inline, numbered list, or APA-like footnotes)?]

### Key Entities *(include if feature involves data)*

- **ResearchRequest**: (id, requester, topic, scope, output_type, constraints, requested_at)
- **EvidenceItem**: (id, source_ref, excerpt, url, timestamp, raw_metadata)
- **ResearchReport**: (id, request_id, summary_text, assertions[], citations[], generated_at, skill_version)
- **Subscription**: (id, topic, cadence, threshold, subscribers)

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Interactive briefs return a first-draft summary within 30 seconds for 90% of Phase 0 requests over moderate corpora.
- **SC-002**: Dossiers include verifiable citations for >= 80% of factual assertions in test topics during evaluation.
- **SC-003**: Subscription alerts deliver summaries within the configured cadence and 95% of significant events are surfaced to subscribers within one cadence interval.
- **SC-004**: Human evaluation: reviewers rate summaries as "useful" or better in >= 80% of sampled briefs.

## Assumptions

- Phase 0 will configure a bounded set of sources (public web + selected internal indices); paywalled sources are treated as limited-visibility and must be declared in provenance.
- Request volumes are moderate for interactive flows; large-scale crawling/archival is out-of-scope for Phase 0.

## Open Questions

- [NEEDS CLARIFICATION: required permission model for accessing internal/sensitive sources (role-based, token-scoped, or other)?]
- [NEEDS CLARIFICATION: preferred default citation style for Phase 0 (inline, numbered list, or APA-like footnotes)?]

---

*End of spec draft.*
