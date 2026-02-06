# Skill Name
publish-plan-generator

# Description
Constructs per-target publish payloads and schedules from a canonical content reference and target list. Validates formatting rules and returns a delivery plan; it MUST NOT perform delivery.

# Owning Agent Role
publisher

# Input Contract
{
  "type": "object",
  "properties": {
    "content_ref": {"type": "string", "description": "Reference to prepared content/draft"},
    "targets": {"type": "array", "items": {"type": "object"}, "description": "Target descriptors (id, type, formatting_rules)"},
    "schedule": {"type": "string", "description": "RFC3339 timestamp or cron expression (optional)"}
  },
  "required": ["content_ref", "targets"]
}

# Output Contract
{
  "type": "object",
  "properties": {
    "plan_id": {"type": "string"},
    "per_target_payloads": {"type": "array", "items": {"type": "object"}, "description": "Prepared payloads and per-target metadata"},
    "validation_report": {"type": "object", "description": "Validation results and warnings"}
  },
  "required": ["plan_id", "per_target_payloads"]
}

# Constraints
- MUST NOT call external APIs.
- MUST NOT access databases.
- MUST NOT perform posting, analytics, or financial actions.
- All side effects (actual delivery, credential lookup, metrics emission) MUST be handled elsewhere via MCP tools.
