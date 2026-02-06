# Skill Name
content-formatter

# Description
Applies templates, style rules, and formatting constraints to a content draft, returning formatted text and metadata. This skill only transforms provided text and does not publish or persist results.

# Owning Agent Role
creator

# Input Contract
{
  "type": "object",
  "properties": {
    "draft_text": {"type": "string"},
    "template": {"type": "string", "description": "Template or placeholders to apply"},
    "style_constraints": {"type": "object", "description": "Tone, max_length, forbidden_phrases"}
  },
  "required": ["draft_text"]
}

# Output Contract
{
  "type": "object",
  "properties": {
    "formatted_text": {"type": "string"},
    "metadata": {"type": "object", "description": "word_count, applied_template, truncation_flag"},
    "warnings": {"type": "array", "items": {"type": "string"}}
  },
  "required": ["formatted_text"]
}

# Constraints
- MUST NOT call external APIs.
- MUST NOT access databases.
- MUST NOT perform posting, analytics, or financial actions.
- All side effects (saving drafts, publishing, analytics) MUST be handled elsewhere via MCP tools.
