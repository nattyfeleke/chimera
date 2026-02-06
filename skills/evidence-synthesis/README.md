# Skill Name
evidence-synthesis

# Description
Aggregates, deduplicates, and synthesizes evidence items (documents, excerpts, metadata) into a concise summary and structured dossier. This skill performs transformation and structuring only; it does not fetch sources or perform network I/O.

# Owning Agent Role
researcher

# Input Contract
{
  "type": "object",
  "properties": {
    "corpus_ref": {"type": "string", "description": "Pointer to curated corpus (dataset ID or query ref)"},
    "query": {"type": "string", "description": "Research query or topic"},
    "params": {"type": "object", "description": "Synthesis parameters (max_summary_length, min_citations)"}
  },
  "required": ["corpus_ref", "query"]
}

# Output Contract
{
  "type": "object",
  "properties": {
    "summary": {"type": "string", "description": "Concise synthesized summary"},
    "assertions": {"type": "array", "items": {"type": "string"}, "description": "Key claims or findings"},
    "citations": {"type": "array", "items": {"type": "object"}, "description": "List of evidence item refs and excerpts"},
    "dossier": {"type": "object", "description": "Structured dossier with assertions->evidence mapping"}
  },
  "required": ["summary", "citations"]
}

# Constraints
- MUST NOT call external APIs.
- MUST NOT access databases.
- MUST NOT perform posting, analytics, or financial actions.
- All side effects (fetching sources, storing dossiers, notifications) MUST be handled elsewhere via MCP tools.
