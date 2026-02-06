# System Governance Specification

## 1. Purpose

This document defines the mandatory governance controls for Project Chimera.
These rules constrain autonomous agent behavior and override all other
functional specifications when triggered.

Governance rules are evaluated by the Orchestrator and Judge agents
before any irreversible external action is executed.


## 2. Human-in-the-Loop Approval

The system MUST require explicit human approval when any of the following
conditions are met:

### HITL-1: Low Confidence Outputs
Trigger:
- confidence_score < 0.80

Action:
- Pause execution
- Route task to human_review_queue
- Await explicit approval or rejection

### HITL-2: Sensitive Domains
Trigger:
- Content classified as political, financial advice, medical advice, or legal claims

Action:
- Mandatory human review regardless of confidence score

### HITL-3: Financial Transactions
Trigger:
- Any transaction involving real monetary value

Action:
- Require approval by designated Human Operator role

## 3. Safety Overrides

Safety Overrides are automatic system-enforced actions that bypass normal
agent workflows.

### SO-1: Platform Policy Violation
Trigger:
- Content flagged as violating platform terms

Action:
- Immediate rejection
- Task marked as failed
- Planner instructed to replan with updated constraints

### SO-2: Repeated Task Failure
Trigger:
- Same task fails validation 3 times consecutively

Action:
- Suspend task
- Escalate to human review

## 4. Kill Switches

Kill switches provide immediate system-wide shutdown capabilities.

### KS-1: Global Agent Halt
Trigger:
- Manual activation by Human Operator
- Critical security incident
- External legal or compliance requirement

Action:
- Stop all active agent execution
- Prevent new task scheduling
- Preserve system state for audit

### KS-2: Financial Lockdown
Trigger:
- Detected anomalous spending behavior
- Budget threshold exceeded

Action:
- Disable all MCP financial tools
- Allow read-only balance checks

## 5. Rule Precedence

In the event of conflict:

1. Kill Switch rules override all other specifications
2. Safety Overrides override Functional Specs
3. Human-in-the-Loop decisions override Agent decisions
4. Functional Specs override Agent Skills

## 6. Audit Requirements

All governance-triggered events MUST be logged with:
- Timestamp
- Trigger condition
- Acting component (Planner, Worker, Judge)
- Resulting action

Logs MUST be immutable and retained for post-incident review.

