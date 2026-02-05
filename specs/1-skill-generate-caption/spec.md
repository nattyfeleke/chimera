# Feature Specification: Skill — Generate Caption

**Feature Branch**: `1-skill-generate-caption`
**Created**: 2026-02-06
**Status**: Draft
**Input**: User description: "create spec skill.generate_caption"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Single Image Caption Generation (Priority: P1)

An end user or agent submits a single image (or post with an image) and requests a concise caption; the system returns a caption that is accurate, relevant, and fits the requested tone and max length.

**Why this priority**: Core capability — quickly generate readable captions for content publishing.

**Independent Test**: Provide a set of sample images and compare generated captions against a gold set and human reviewer judgments.

**Acceptance Scenarios**:
1. **Given** an input image and tone `neutral`, **When** the skill runs, **Then** it returns a caption <= requested length that correctly describes visible content.

---

### User Story 2 - Batch Captioning & Templates (Priority: P2)

Users can submit a batch of images and specify a template or tone (e.g., promotional, informative) and receive captions for each item.

**Why this priority**: Productivity for content teams and automation.

**Independent Test**: Submit a batch of 50 images and verify captions are returned and follow the template/tone parameter.

**Acceptance Scenarios**:
1. **Given** 50 images and template `short-promo`, **When** the batch run completes, **Then** each caption adheres to the short-promo style.

---

### User Story 3 - Safety & Style Controls (Priority: P3)

The skill respects safety filters (no hateful, sexual, or disallowed content) and applies brand/style constraints when provided.

**Why this priority**: Prevents unsafe or brand-inconsistent outputs.

**Independent Test**: Provide images that would normally trigger safety filters and verify outputs are rejected or returned with safe fallback captions.

**Acceptance Scenarios**:
1. **Given** an image with violent content, **When** the skill runs, **Then** the output is either a safe fallback caption or an error indicating disallowed content.

---

## Constitution Compliance (mandatory)

- **Code Quality**: Unit tests for caption formatting, template application, and safety filtering. Maintainable modules with clear input/output contracts.
- **Testing**: Unit tests, integration tests with sample corpora, and human-evaluation regression tests for quality and style.
- **User Experience Consistency**: Expose parameters and results through existing skill UI patterns; consistent error messaging.
- **Performance Requirements**: Interactive single-item runs complete within success criteria latency; batch runs handled with job/queue semantics.
- **Observability & Versioning**: Emit run metrics (latency, success/failure), model/skill version used, and sample outputs for traceability.

### Edge Cases

- Low-quality or corrupted images: return informative error or fallback caption.
- Ambiguous scenes: prefer concise, non-assertive phrasing (e.g., "A group of people near a table" instead of definitive claims).
- Images containing faces: respect privacy and avoid making sensitive or personally identifying claims.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The skill MUST accept an input image reference (single or batch), optional parameters (`tone`, `max_length`, `template`), and return caption(s) with provenance metadata.
- **FR-002**: The skill MUST support batch execution with per-item results and per-batch status.
- **FR-003**: The skill MUST apply safety filters and return safe fallbacks or rejection for disallowed content.
- **FR-004**: The skill MUST allow style/brand constraints to be provided and applied to generated captions [NEEDS CLARIFICATION: how granular should style controls be (preset tones only, or custom templates + CSS-like rules)?]
- **FR-005**: The skill MUST include provenance: skill version, model id (if applicable), timestamp, and input reference.
- **FR-006**: The skill SHOULD provide an explanation or example snippets that justify why items contributed to a caption (limited sampling for explainability).
- **FR-007**: The skill MUST respect a configurable maximum caption length and indicate when truncation occurred.

### Key Entities *(include if feature involves data)*

- **CaptionResult**: (id, input_ref, caption_text, tone, length, provenance, safety_flag, sample_refs)
- **CaptionBatch**: (id, owner, input_list, status, started_at, finished_at, results_summary)
- **StyleTemplate**: (id, name, rules, example)

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Single-item interactive runs return a caption within 5 seconds for 95% of requests in Phase 0 pilot.
- **SC-002**: Human evaluation: at least 85% of generated captions rated acceptable by reviewers on clarity and relevance for a representative test set.
- **SC-003**: Safety: 100% of inputs that violate safety policies are caught and handled by safe fallback or rejection in tested scenarios.
- **SC-004**: Batch throughput: system can process batches of 100 items with per-item success rate >= 95% under pilot load.

## Assumptions

- Caption generation will use existing language/image models available to the platform; optimization strategies (caching, batching) applied as needed.
- Privacy: face recognition or PII extraction is out-of-scope; skill avoids identifying people or making sensitive assertions.

## Open Questions

- [NEEDS CLARIFICATION: how granular should style controls be (preset tones only, or custom templates + CSS-like rules)?]
- [NEEDS CLARIFICATION: default max caption length and default tone for Phase 0 (e.g., 140 chars, `neutral`)?]

---

*End of spec draft.*
