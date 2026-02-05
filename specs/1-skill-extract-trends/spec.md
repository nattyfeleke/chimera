# Feature Specification: Skill — Extract Trends

**Feature Branch**: `1-skill-extract-trends`
**Created**: 2026-02-06
**Status**: Draft
**Input**: User description: "create spec skill.extract_trends"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Run Trend Extraction Skill (Priority: P1)

An analyst or agent runs the `extract_trends` skill against a content corpus (posts, time-series, or aggregated signals) and receives a ranked list of discovered trends with timestamps and confidence scores.

**Why this priority**: Core capability enabling agents and users to surface actionable trends from raw signals.

**Independent Test**: Provide a curated dataset with injected trending signals; run the skill and verify top-N results contain injected trends within expected rank and time window.

**Acceptance Scenarios**:
1. **Given** a corpus containing a clear uptick in topic A, **When** `extract_trends` is executed, **Then** topic A appears in the top-3 results with a confidence score above threshold.

---

### User Story 2 - Parameterized Runs & Filters (Priority: P2)

Users can run the skill with parameters (time window, source filters, minimum frequency) and get filtered trend results accordingly.

**Why this priority**: Allows targeted analysis and reduces noise for specific use cases.

**Independent Test**: Run skill with a narrow time window and verify trends outside that window are excluded.

**Acceptance Scenarios**:
1. **Given** a 24-hour window filter, **When** extracting trends, **Then** results only reflect events within that 24-hour window.

---

### User Story 3 - Explainability & Sampling (Priority: P3)

Users can inspect example source items (samples) that contributed to each trend and view summary statistics (count, first_seen, last_seen).

**Why this priority**: Builds trust and supports validation/debugging of trend results.

**Independent Test**: For a returned trend, request sample items and verify they match the trend topic.

**Acceptance Scenarios**:
1. **Given** a returned trend, **When** requesting samples, **Then** the system returns representative items and a small table of statistics.

---

## Constitution Compliance (mandatory)

- **Code Quality**: Algorithmic components will include deterministic unit tests and clear interfaces for input/output shapes.
- **Testing**: Unit tests for scoring/ranking logic, integration tests using representative corpora, and regression tests for detected trends.
- **User Experience Consistency**: Results and controls follow existing MCP skill UI conventions for parameters and results display.
- **Performance Requirements**: Define acceptable latency and scale in success criteria; implement batching and sampling strategies.
- **Observability & Versioning**: Emit metrics for run latency, result counts, and versioned skill artifacts.

### Edge Cases

- Sparse signals: return empty results with clear messaging when insufficient data exists.
- Highly noisy corpora: provide sampling and denoising parameter recommendations.
- Conflicting timezones/timestamps: normalize to UTC and surface original timestamps in samples.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The skill MUST accept a corpus input reference (dataset, stream, or query), parameters (time window, filters), and return a ranked list of trends (id, label, score, stats).
- **FR-002**: The skill MUST provide explainability: for each trend, return N example items and summary statistics (count, first_seen, last_seen).
- **FR-003**: The skill MUST support parameterized executions (time window, source filters, min-frequency).
- **FR-004**: The skill SHOULD allow cached or incremental runs to avoid reprocessing unchanged data (optimization, out-of-scope if constrained).
- **FR-005**: The skill MUST validate input corpus and return clear error messages for invalid inputs.
- **FR-006**: The skill MUST record provenance and skill version used for each run.
- **FR-007**: The skill MUST operate within acceptable resource limits and support timeboxed executions [NEEDS CLARIFICATION: preferred default execution timeout and max sample size?]
- **FR-008**: The skill MUST surface metrics: runs, latency, result sizes, and failure rates.

### Key Entities *(include if feature involves data)*

- **TrendResult**: (id, label, score, count, first_seen, last_seen, sample_refs)
- **SkillRun**: (id, input_ref, params, started_at, finished_at, status, skill_version, provenance)
- **CorpusRef**: pointer to dataset/stream/query used as input

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: For curated test corpora, the skill returns at least 90% of injected trends in the top-5 results.
- **SC-002**: Parameterized runs (with reasonable corpus sizes) complete within 30 seconds in Phase 0 pilot for interactive use.
- **SC-003**: Explainability: for 95% of returned trends, samples reflect the trend semantics judged by human reviewers.
- **SC-004**: Error handling: invalid inputs produce actionable errors and do not crash the system.

## Assumptions

- Input corpora for Phase 0 are moderate in size (tens of thousands of items); large-scale streaming/real-time trend extraction is out-of-scope unless clarified.
- Language and domain handling (multi-lingual or domain-specific tokenization) will use sensible defaults; further customization can be added later.

## Open Questions

- [NEEDS CLARIFICATION: preferred default execution timeout and maximum sample size for explainability?]
- [NEEDS CLARIFICATION: primary input types to prioritize (posts, time-series, aggregated signals)?]

---

*End of spec draft.*
