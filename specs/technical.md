# Technical Specification — Interfaces & Data Models

Overview
- This document defines JSON-style input/output schemas for agent interactions and a conceptual database schema for storing video metadata and related artifacts. These are interface contracts only and MUST NOT include implementation details.

API Contracts (JSON-style Schemas)

AgentRequest (generic)
{
  "type": "object",
  "properties": {
    "request_id": {"type": "string"},
    "agent_id": {"type": "string"},
    "action": {"type": "string"},
    "payload": {"type": "object"},
    "timestamp": {"type": "string", "format": "date-time"}
  },
  "required": ["request_id","agent_id","action","payload"]
}

AgentResponse (generic)
{
  "type": "object",
  "properties": {
    "request_id": {"type": "string"},
    "status": {"type": "string", "enum": ["success","failure","deferred"]},
    "result": {"type": "object"},
    "provenance": {"type": "object"}
  },
  "required": ["request_id","status"]
}

EvidenceSynthesisInput (example)
{
  "type": "object",
  "properties": {
    "corpus_ref": {"type": "string"},
    "query": {"type": "string"},
    "params": {"type": "object"}
  },
  "required": ["corpus_ref","query"]
}

PolicyEvaluationInput (example)
{
  "type": "object",
  "properties": {
    "request": {"type": "object"},
    "policies": {"type": "array"}
  },
  "required": ["request","policies"]
}

Provenance object (interface)
{
  "type": "object",
  "properties": {
    "agent_id": {"type": "string"},
    "skill_version": {"type": "string"},
    "timestamp": {"type": "string", "format": "date-time"}
  },
  "required": ["agent_id","skill_version","timestamp"]
}

Database Schema (Conceptual ERD for Video Metadata)

- Entities:
  - Video(id, title, description, duration_seconds, uploaded_at, owner_id)
  - Asset(id, video_id -> Video.id, file_url, content_type, size_bytes)
  - Annotation(id, video_id -> Video.id, author_id, start_time, end_time, text, created_at)
  - AgentRun(id, agent_id, action, request_id, status, started_at, finished_at, provenance)

- Relationships:
  - Video 1..* Asset (a video MAY have multiple asset variants)
  - Video 1..* Annotation (a video MAY have many annotations)
  - AgentRun references artifacts via request_id or content refs (optional)

- Entity descriptions:
  - Video: canonical metadata for a video artifact. The `id` MUST be used as the canonical reference.
  - Asset: storage/binary descriptor for a video variant (transcode, thumbnail).
  - Annotation: human or agent-generated notes attached to video segments.
  - AgentRun: record of an agent's execution and its provenance; MUST be emitted by agents for auditability.

Notes and Constraints
- These schemas are interface-level contracts and MUST be used by implementations to validate payloads.
- Implementations MUST NOT assume database engine features; the ERD is conceptual only.
