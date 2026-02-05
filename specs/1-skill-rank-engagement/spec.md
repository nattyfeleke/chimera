# Feature Specification: Skill — Rank Engagement

**Feature Branch**: `1-skill-rank-engagement`
**Created**: 2026-02-06
**Status**: Draft
**Input**: User description: "create spec skill.rank_engagement"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Score Content Engagement (Priority: P1)

An analyst or agent submits a corpus of content items (posts, articles, media) and receives a ranked list where each item has an engagement score reflecting relevance and audience interaction potential.

**Why this priority**: Enables prioritization of content for surfacing, promotion, or further analysis.

**Independent Test**: Provide a corpus with known engagement signals; run the skill and verify the ranking correlates with ground-truth engagement metrics.

**Acceptance Scenarios**:
1. **Given** a corpus with items A..N where A has highest historical interactions, **When** the skill runs, **Then** A appears in a top position and scores reflect relative engagement.

---

### User Story 2 - Parameterized Scoring & Filters (Priority: P2)

Users can adjust scoring parameters (time window, metric weights, audience segment) and re-run to get tailored rankings.

**Why this priority**: Different campaigns and audiences value different engagement signals.

**Independent Test**: Run with alternate weightings and confirm ranking changes accordingly.

**Acceptance Scenarios**:
1. **Given** weight favoring recency, **When** scoring runs, **Then** recently published items move higher in rank.

---

### User Story 3 - Explainability & Sampling (Priority: P3)

For each scored item, users can view contributing signals (likes, shares, impressions, comments), sample interactions, and a short explanation of the score factors.

**Why this priority**: Builds trust and aids debugging/tuning of scoring models.

**Independent Test**: For a returned top item, request explanation and samples; verify returned signals match input data and score decomposition.

**Acceptance Scenarios**:
1. **Given** a scored item, **When** requesting explanation, **Then** the skill returns top 3 contributing signals and sample interactions.

---

## Constitution Compliance (mandatory)

- **Code Quality**: Unit tests for scoring calculation and parameter parsing; CI checks for new modules.
- **Testing**: Unit tests, integration tests on representative corpora, and regression tests to detect score drift.
- **User Experience Consistency**: Follow existing MCP patterns for parameters, results, and explanations.
- **Performance Requirements**: Interactive runs for moderate corpora should meet latency targets in Success Criteria; batch runs handled via job semantics.
- **Observability & Versioning**: Emit metrics for run latency, distribution of scores, and versioned scoring configs.

### Edge Cases

- Sparse signals: produce a clear "insufficient data" result rather than noisy scores.
- Bot/spam activity: detect and downweight or exclude likely non-organic interactions.
- Missing metadata: gracefully handle items lacking timestamps or author data.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The skill MUST accept a corpus reference, scoring parameters (time window, metric weights, audience filter), and return ranked items with engagement scores and provenance.
- **FR-002**: The skill MUST compute scores using configurable signals (likes, comments, shares, impressions, click-through-rate, dwell time) and provide score decomposition.
- **FR-003**: The skill MUST support parameterized runs and persist scoring configuration used for each run.
- **FR-004**: The skill MUST provide explainability: for each item, return top contributing signals and sample interactions.
- **FR-005**: The skill MUST detect and mitigate obvious spam/bot signals during scoring.
- **FR-006**: The skill MUST validate inputs and return actionable errors for invalid requests.
- **FR-007**: The skill MUST record skill version and input provenance for reproducibility.
- **FR-008**: The skill MUST operate within resource/time bounds and indicate when results are partial due to limits [NEEDS CLARIFICATION: preferred default scoring time window (e.g., 7 days, 30 days) for Phase 0?]
- **FR-009**: The skill SHOULD allow custom metric weight presets and support saving reusable presets.

### Key Entities *(include if feature involves data)*

- **EngagementScore**: (item_id, score, breakdown{signal:weighted_value}, rank)
- **ScoreRun**: (id, input_ref, params, started_at, finished_at, status, skill_version)
- **SignalSample**: sample interactions contributing to a score (type, timestamp, user_id[anonymized])

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: For representative corpora, the top-10 ranked items contain >= 85% of items that historically achieved top engagement in the same window.
- **SC-002**: Parameterized interactive runs on moderate corpora (<= 10k items) complete within 30 seconds for Phase 0 pilot.
- **SC-003**: Explainability: for 95% of top-ranked items, the skill provides a breakdown and sample interactions within 5 seconds of requesting the explanation.
- **SC-004**: Spam mitigation: in tests with injected bot activity, the system reduces bot-influenced items in top-50 results by at least 90%.

## Assumptions

- Phase 0 targets moderate dataset sizes (up to ~10k items) for interactive runs; large-scale scoring and continuous real-time ranking are out-of-scope unless clarified.
- Input signals are available and pre-aggregated or queryable; enrichment steps (fetching impressions/dwell-time) may be required upstream.

## Open Questions

- [NEEDS CLARIFICATION: preferred default scoring time window for Phase 0 (e.g., 7 days, 30 days)?]
- [NEEDS CLARIFICATION: any mandatory signals to include or exclude (e.g., include dwell-time? exclude impressions)?]

---

*End of spec draft.*
