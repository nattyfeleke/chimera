# Feature Specification: MCP Data

**Feature Branch**: `1-mcp-data`
**Created**: 2026-02-06
**Status**: Draft
**Input**: User description: "create spec mcp.data"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Publish Structured Dataset (Priority: P1)

A data engineer registers a dataset schema and publishes a batch of records into MCP Data catalog; downstream agents discover the dataset and query its metadata to enrich decisions.

**Why this priority**: Cataloging and publishing structured data is foundational to enabling data-driven agents and reuse.

**Independent Test**: Register a schema, ingest a test dataset, verify dataset metadata appears in catalog and sample records are accessible.

**Acceptance Scenarios**:
1. **Given** a registered dataset, **When** an ingest job completes, **Then** the dataset appears in the MCP Data catalog with schema, sample, and provenance metadata.

---

### User Story 2 - Dataset Discovery & Access (Priority: P2)

Analysts and agents can search the catalog by tags, schema fields, and freshness; access control enforces read permissions.

**Why this priority**: Enables consumers to find and use datasets safely.

**Independent Test**: Create datasets with tags and query catalog filters; ensure access is denied to unauthorized principals.

**Acceptance Scenarios**:
1. **Given** a dataset tagged `sales`, **When** a user searches for `sales`, **Then** the dataset is returned in search results.

---

### User Story 3 - Data Lineage & Quality Metrics (Priority: P3)

Operators can view lineage for a dataset and basic quality metrics (completeness, null rates) to trust data usability.

**Why this priority**: Trust and traceability improve adoption and reduce data misuse.

**Independent Test**: Ingest data with known anomalies and verify metrics capture the issues and lineage points to the ingest job.

**Acceptance Scenarios**:
1. **Given** a dataset ingested by job `J`, **When** viewing dataset details, **Then** lineage shows job `J` and the source connector.

---

## Constitution Compliance (mandatory)

- **Code Quality**: Provide unit tests for schema validation and catalog APIs; follow repo lint and CI rules.
- **Testing**: Unit tests, integration tests for ingest pipelines, and manual acceptance tests for catalog UI flows.
- **User Experience Consistency**: Reuse MCP catalog UI components and metadata fields to keep UX consistent.
- **Performance Requirements**: Catalog searches return results under interactive latencies for Phase 0 pilot (see success criteria); ingestion throughput to be clarified.
- **Observability & Versioning**: Emit dataset ingest metrics, schema change events, and keep versioned dataset metadata.

### Edge Cases

- Schema evolution: handle added/removed fields via explicit schema versions.
- PII in datasets: flagging and masking policies required for sensitive fields.
- Partial ingest failures: ingest job should provide partial success reports and retry paths.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST provide a Data Catalog to register datasets with `name`, `schema`, `tags`, `owner`, and `provenance`.
- **FR-002**: System MUST allow ingestion of datasets (batch and small streaming) and attach provenance metadata to ingested datasets.
- **FR-003**: System MUST expose dataset discovery APIs and search by tags, schema fields, owner, and freshness.
- **FR-004**: System MUST allow dataset owners to set access control policies for read and write operations [NEEDS CLARIFICATION: level of ACL granularity required (dataset-level, field-level, role-based)?]
- **FR-005**: System MUST capture and surface basic data quality metrics (record counts, null rates, sample values).
- **FR-006**: System MUST record lineage linking datasets to source connectors and ingestion jobs.
- **FR-007**: System MUST support schema versioning and migration notes.
- **FR-008**: System MUST allow tagging and classification (e.g., pii=true) to support handling of sensitive data [NEEDS CLARIFICATION: any specific regulatory constraints (GDPR, HIPAA)?]

### Key Entities *(include if feature involves data)*

- **Dataset**: (id, name, owner, schema_ref, tags, versions, provenance, quality_metrics)
- **Schema**: (id, fields, types, version, description)
- **IngestJob**: (id, dataset_id, source, status, started_at, finished_at, errors)
- **CatalogEntry**: dataset listing with searchable metadata and samples
- **ACLPolicy**: access rules attached to dataset or dataset fields

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Catalog search returns relevant results within 2 seconds for Phase 0 pilot datasets.
- **SC-002**: Dataset onboarding (register schema + ingest sample) completes in under 10 minutes for a typical dataset.
- **SC-003**: 95% of well-formed ingest jobs report successful provenance and quality metrics within 1 minute of completion.
- **SC-004**: Dataset owners can set and enforce ACLs such that unauthorized reads are denied in 100% of tested scenarios.

## Assumptions

- This spec targets Phase 0: cataloging, small-batch ingest, discovery, and basic lineage/quality. Heavy-duty data warehousing, long-term retention, and complex role management are out-of-scope unless clarified.
- Reasonable defaults for ACL granularity and regulatory handling will be applied if not specified.

## Open Questions

- [NEEDS CLARIFICATION: level of ACL granularity required (dataset-level, field-level, role-based)?]
- [NEEDS CLARIFICATION: any specific regulatory constraints to enforce (GDPR, HIPAA, other)?]

---

*End of spec draft.*
