# OpenClaw Integration — Project Chimera (Optional)

Overview
- This document defines what Chimera MUST share with the OpenClaw network if integration is enabled. This is a governance-level contract that MUST be satisfied before any publication of status or availability.

Information Shared
- Chimera SHALL share only non-sensitive metadata describing capabilities and status. Shared fields MUST be limited to:
  - `instance_id` (opaque identifier)
  - `capabilities` (list of high-level agent roles available: creator, researcher, publisher, governor)
  - `uptime` (seconds)
  - `last_heartbeat` (timestamp)
  - `supported_protocol_versions` (list)

When Published
- Status information MUST be published only after an explicit operator action or after an approved automated heartbeat schedule that is documented and auditable.
- Heartbeat publication frequency SHALL be configurable and SHALL be no more frequent than once per minute unless explicitly authorized.

Governance and Safety Constraints
- No PII, content payloads, or sensitive internal metrics SHALL be published to OpenClaw.
- All published data MUST be auditable and linked to a provenance record indicating the operator or automation that authorized the publication.
- Any OpenClaw integration MUST be reversible and disabled by default until approval is recorded in the repository governance records.

Protocol and Implementation Notes
- This document MUST NOT assume any transport or protocol. Integration details (protocols, endpoints) SHALL be defined in a separate integration implementation plan after governance approval.
