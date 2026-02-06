# Functional Requirements — Project Chimera

Overview
- The following functional requirements define agent-level capabilities that MUST be satisfied by implementations only after these requirements have been approved and validated.

FR-001 — Agent: Create Content (Creator)
- Description: As an Agent (creator), I NEED to produce content drafts from a brief so that authors can review and publish prepared content.
- Acceptance Criteria:
  - Given a valid `CreationRequest` (brief, constraints), when the creator agent runs, then the agent MUST return a `CreationResult` containing `text`, `metadata`, and `provenance` within the configured interactive timeout.
  - The `CreationResult` MUST include `word_count` matching declared length +/-10% and MUST include required keywords if provided.

FR-002 — Agent: Format Content (Creator / Publisher)
- Description: As an Agent, I NEED to apply templates and style constraints to a draft so that content conforms to publishing guidelines.
- Acceptance Criteria:
  - Given `draft_text` and `style_constraints`, when the formatter skill runs, then it MUST return `formatted_text` and `metadata` indicating applied template and truncation flag.
  - If forbidden phrases are present, the output MUST include explicit `warnings` listing each forbidden phrase instance.

FR-003 — Agent: Research & Evidence (Researcher)
- Description: As an Agent (researcher), I NEED to synthesize evidence into a concise summary and dossier so that claims are supported by citations.
- Acceptance Criteria:
  - Given a curated corpus reference and query, when the evidence-synthesis skill runs, then it MUST return `summary`, `citations` (>= min_citations param), and `dossier` mapping assertions to evidence refs.
  - Each citation entry MUST reference a source id and an excerpt string of length >= 50 characters.

FR-004 — Agent: Policy Evaluation (Governor)
- Description: As an Agent (governor), I NEED to deterministically evaluate action requests against policies so that disallowed actions are blocked before execution.
- Acceptance Criteria:
  - Given a `request` and a set of `policies`, when the policy-evaluator skill runs, then it MUST return a `decision` with value one of `allow`, `deny`, or `require_approval` and a `matched_rules` list.
  - If `deny`, the `reason` field MUST contain at least one rule identifier and human-readable explanation.

FR-005 — Agent: Publish Planning (Publisher)
- Description: As an Agent (publisher), I NEED to build per-target delivery plans so that delivery adapters can execute publishing without further transformation.
- Acceptance Criteria:
  - Given a `content_ref` and `targets[]`, when the publish-plan-generator skill runs, then it MUST return a `plan_id` and `per_target_payloads` where each payload includes `target_id`, `payload`, and `formatting_notes`.
  - The validation_report MUST flag missing formatting rules for any target and include actionable warnings.

FR-006 — Agent: Audit & Provenance (All)
- Description: As an Agent, I NEED to attach provenance to any decision or artifact so that every externally visible effect is auditable.
- Acceptance Criteria:
  - Any output emitted by an agent that may result in external effects MUST include a `provenance` object with `agent_id`, `skill_version`, and `timestamp`.

FR-007 — Agent: Scheduling & Retry (Publisher)
- Description: As an Agent (publisher), I NEED to schedule deliveries and define retry policies so that transient failures are retried per policy.
- Acceptance Criteria:
  - Given a scheduled publish request with retry policy, the system MUST produce a schedule entry and a per-target retry plan; the plan MUST include max_attempts and backoff strategy (enumerated).

FR-008 — Agent: Safety & Quarantine (Researcher / Ingest)
- Description: As an Agent, I NEED to identify malformed or unsafe payloads and mark them for quarantine so that system stability and safety are maintained.
- Acceptance Criteria:
  - When an ingestion or evidence item fails validation (schema or safety), the system MUST produce a quarantine record referencing the raw payload and a clear `error_code`.

FR-009 — Agent: Idempotency (Ingest / Publish)
- Description: As an Agent, I NEED to prevent duplicate external side effects so that double-publishing or duplicate ingest does not occur.
- Acceptance Criteria:
  - For operations with an `external_id` provided, the system MUST detect duplicates within a configured deduplication window and return an idempotent response indicating duplicate status and existing `remote_id`.

FR-010 — Agent: Explainability (All)
- Description: As an Agent, I NEED to provide explainability artifacts for machine decisions so that human reviewers can audit rationale.
- Acceptance Criteria:
  - For any scored or ranked result, the agent MUST return a `score_breakdown` with contributing factors and a sample of supporting evidence (when applicable) limited to configured sample size.
