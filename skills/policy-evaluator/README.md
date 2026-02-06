# Skill Name
policy-evaluator

# Description
Evaluates a proposed agent action against a set of declarative governance policy rules and returns a deterministic decision (allow, deny, require_approval) along with reasons. This skill performs rule evaluation only; it does not enforce decisions or contact approvers.

# Owning Agent Role
governor

# Input Contract
{
  "type": "object",
  "properties": {
    "request": {"type": "object", "description": "Agent action request payload (action, params, requester)"},
    "policies": {"type": "array", "items": {"type": "object"}, "description": "Active policy definitions to evaluate against"}
  },
  "required": ["request", "policies"]
}

# Output Contract
{
  "type": "object",
  "properties": {
    "decision": {"type": "string", "enum": ["allow","deny","require_approval"], "description": "Result of policy evaluation"},
    "reason": {"type": "string"},
    "matched_rules": {"type": "array", "items": {"type": "string"}},
    "modified_request": {"type": "object", "description": "Optional modified request that would comply with policy"}
  },
  "required": ["decision"]
}

# Constraints
- MUST NOT call external APIs.
- MUST NOT access databases.
- MUST NOT perform posting, analytics, or financial actions.
- All side effects (enforcing a decision, notifying approvers, storing audit logs) MUST be handled elsewhere via MCP tools.
