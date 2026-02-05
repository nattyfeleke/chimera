# Feature Specification: MCP Sense

**Feature Branch**: `1-mcp-sense`
**Created**: 2026-02-06
**Status**: Draft
**Input**: User description: "create spec mcp.sense"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Onboard Sensor Source (Priority: P1)

An operator configures a new sensor/source in the MCP control plane, defines a simple mapping, and verifies that incoming sensor events are ingested, normalized, and appear in the MCP context store where agents can consume them.

**Why this priority**: Enables the core value — bringing external signals into MCP so agents can react.

**Independent Test**: Configure a test sensor that emits sample events; verify events appear in the MCP context UI or via agent subscription.

**Acceptance Scenarios**:
1. **Given** a registered sensor source, **When** it emits a well-formed event, **Then** the event is ingested, normalized, and stored in MCP context with a timestamp and source metadata.
2. **Given** a newly created mapping, **When** the operator sends a test event, **Then** the mapping is applied and the normalized event fields match the mapping.

---

### User Story 2 - Agent Subscription & Consumption (Priority: P2)

An MCP agent subscribes to sensed events (by source, tag, or event type) and receives notifications when matching events are ingested.

**Why this priority**: Allows agents and workflows to act on sensed data.

**Independent Test**: Create a subscription filter, emit events, and verify the agent receives the expected events.

**Acceptance Scenarios**:
1. **Given** a subscription for `sensor:temperature`, **When** a matching event is ingested, **Then** the agent receives the event within the configured delivery window.

---

### User Story 3 - Fault Tolerance & Observability (Priority: P3)

Operators can inspect ingestion errors, malformed payloads are safely rejected or quarantined, and metrics/logs surface ingestion health.

**Why this priority**: Ensures operational safety and debuggability.

**Independent Test**: Send malformed payloads and verify errors are recorded and do not crash the runtime.

**Acceptance Scenarios**:
1. **Given** a malformed event, **When** it is received, **Then** it is recorded in an error queue and an operator-visible metric increments.

---

## Constitution Compliance (mandatory)

- **Code Quality**: Feature will include unit tests for normalization logic and CI lint rules for new modules.
- **Testing**: Unit tests for parsing/normalization, integration tests for end-to-end ingestion to context store, and manual acceptance tests for operator flows.
- **User Experience Consistency**: Use existing MCP control-plane UI patterns for sensor configuration and subscriptions.
- **Performance Requirements**: Define throughput targets during clarification; implement backpressure and safe buffering.
- **Observability & Versioning**: Emit ingestion metrics (ingest rate, error rate), structured logs with source/event IDs, and version mappings for parsers.

### Edge Cases

- Duplicate events (idempotency): deduplicate if event ID present, or annotate duplicates.
- Unknown schema fields: preserve unknown fields in a raw payload area.
- Backpressure: if downstream is slow, buffer with size limits and apply rejection or drop policy.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST allow operators to register a sensor/source with a name, description, and connection metadata.
- **FR-002**: System MUST accept incoming events from registered sensor sources and persist them in the MCP context store.
- **FR-003**: System MUST provide a mapping/transformation mechanism to normalize incoming events into MCP canonical event shape.
- **FR-004**: System MUST support subscriptions so agents can receive matching events.
- **FR-005**: System MUST record ingestion metadata (source id, received timestamp, raw payload reference).
- **FR-006**: System MUST authenticate and authorize sensor sources before accepting data [NEEDS CLARIFICATION: preferred authentication method for sensor sources (certs, API keys, mTLS, other)?]
- **FR-007**: System MUST retain ingested events according to policy and handle expected throughput [NEEDS CLARIFICATION: retention period and target throughput (events/sec) for initial rollout?]
- **FR-008**: System MUST provide observability: ingest rate, error rate, and sample failed payloads.
- **FR-009**: System MUST provide a safe quarantine for malformed events and a way for operators to reprocess or discard them.
- **FR-010**: System MUST ensure eventual delivery guarantees to subscribers for successfully ingested events.

### Key Entities *(include if feature involves data)*

- **SensorSource**: Represents an external producer (id, name, connection metadata, auth credentials reference, tags).
- **SensorEvent**: Raw incoming payload (id, source_id, received_at, raw_payload).
- **NormalizedEvent**: Canonical event shape after mapping (id, type, canonical_fields, metadata).
- **Mapping**: Operator-defined mapping/transformation rules (id, version, mapping_spec).
- **Subscription**: Filter and delivery config for agents (id, filter_expr, delivery_policy).

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Operators can register and verify a sensor source in under 5 minutes (P1 onboarding flow completes in <5 minutes).
- **SC-002**: 99% of well-formed test events are visible to subscribers within 5 seconds of emission under normal conditions for initial rollout traffic (clarify throughput target).
- **SC-003**: Malformed payloads are quarantined and do not increase the system error rate beyond 0.5% for standard test inputs.
- **SC-004**: Operators can view ingestion metrics (ingest rate, error rate) and a sample failed payload within the UI.

## Assumptions

- This spec focuses on the sensing ingestion flow and normalization; it does not define delivery transports for subscribers (outbound delivery integrations are out-of-scope for Phase 0 unless required by clarify response).
- Default retention and throughput targets will be set after clarification; reasonable defaults will be applied if not specified.

## Open Questions

- [NEEDS CLARIFICATION: preferred authentication for sensor sources (certs, API keys, mTLS, other)?]
- [NEEDS CLARIFICATION: retention period and initial throughput target?]

---

*End of spec draft.*
