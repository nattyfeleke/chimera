# Feature Specification: Agent — Publisher

**Feature Branch**: `1-agent-publisher`
**Created**: 2026-02-06
**Status**: Draft
**Input**: User description: "create spec agent.publisher"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Publish Single Item (Priority: P1)

An author or agent requests that a prepared content item be published to a target channel (social, CMS, or RSS) at once or at a scheduled time; the system performs delivery, returns a publishing receipt, and records provenance.

**Why this priority**: Core delivery capability required to move content from draft to live.

**Independent Test**: Submit a content item with target `social:test-account`, request immediate publish, verify post is visible in the target account and a receipt with timestamp and remote-id is recorded.

**Acceptance Scenarios**:
1. **Given** a valid content item and authorized target, **When** publish is requested, **Then** the system delivers content and returns a receipt with status `published` and remote identifier.

---

### User Story 2 - Scheduled Publishing & Retry (Priority: P2)

Users schedule publishes for future times, can view scheduled jobs, and the system retries transient failures according to policy.

**Independent Test**: Schedule a publish 1 minute in the future and verify it executes at the scheduled time; simulate transient failure and verify retries occur.

---

### User Story 3 - Approval Workflow & Audit (Priority: P3)

Content requiring approval is routed to reviewers; only approved items are published. All publish actions are auditable with provenance, reviewer decisions, and delivery receipts.

**Independent Test**: Submit content that requires approval, approve it, publish, and verify audit trail contains reviewer id, timestamps, and publish receipt.

---

## Constitution Compliance (mandatory)

- **Code Quality**: Unit tests for delivery adapters, scheduling, retry logic, and provenance recording. Follow repo lint and CI rules.
- **Testing**: Integration tests against staging targets, end-to-end tests for scheduling and retries, and manual acceptance for approval flows.
- **User Experience Consistency**: Use existing MCP UI patterns for publish dialogs, scheduling UI, and approval queues.
- **Performance Requirements**: Publish latency and scheduling accuracy targets defined in success criteria; implement backpressure for high-volume delivery.
- **Observability & Versioning**: Emit metrics (publish rate, failure rate, retry counts), structured logs with source/request ids, and version delivery adapters.

### Edge Cases

- Downstream rate-limits or rejections: mark publish as `deferred` or `failed` with actionable error and retry metadata.
- Duplicate publishes: deduplicate by content-hash + request id to avoid double-posting.
- Partial delivery (multi-target): record per-target status and surface overall audit.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST accept publish requests with content reference, target(s), schedule (optional), and auth context.
- **FR-002**: System MUST deliver content to supported targets and return per-target receipts (status, remote_id, timestamp).
- **FR-003**: System MUST support scheduling with reliable execution at the requested time and retry policies for transient errors.
- **FR-004**: System MUST provide an approval workflow that blocks publishing until required approvals are recorded.
- **FR-005**: System MUST record full provenance: requestor, content version, skill/agent version, approvers, and delivery receipts.
- **FR-006**: System MUST support per-target configuration (formatting rules, rate limits, credentials) [NEEDS CLARIFICATION: which delivery targets must be supported in Phase 0 (social platforms, CMS, webhook endpoints)?]
- **FR-007**: System MUST enforce authorization: only principals with publish permission for the target may publish.
- **FR-008**: System MUST surface publish metrics and per-target statuses for operators.

### Key Entities *(include if feature involves data)*

- **PublishRequest**: (id, content_ref, targets[], schedule_at, requested_by, status)
- **PublishReceipt**: (publish_id, target, status, remote_id, delivered_at, error)
- **ApprovalRecord**: (id, publish_id, reviewer, decision, notes, decided_at)
- **TargetConfig**: (id, type, credentials_ref, formatting_rules, rate_limit)

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Immediate publishes to supported Phase 0 targets succeed and return receipts within 10 seconds for 95% of requests under pilot load.
- **SC-002**: Scheduled publishes execute within a 5-second window of the requested time for 95% of scheduled items.
- **SC-003**: Retry policy reduces transient failure rates so that 90% of transient failures recover without manual intervention.
- **SC-004**: Audit completeness: 100% of publishes include provenance and delivery receipts in the audit log.

## Assumptions

- Phase 0 will include a small set of delivery adapters (to be clarified); additional adapters can be added later.
- Credential management for targets uses existing secret store integrations; rotation policies handled by ops.

## Open Questions

- [NEEDS CLARIFICATION: which delivery targets must be supported in Phase 0 (social platforms, CMS, webhook endpoints)?]

---

*End of spec draft.*
