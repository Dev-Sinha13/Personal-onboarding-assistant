---
tags: [hackathon, tool]
phase: 1
data-source: local-json
---

# Tool 1 — `answer_day_one_logistics`

**Data source:** Local dictionary / JSON file (static).

**Purpose:** Answer standard Day 1 HR/IT logistics questions.

## Example content to seed
- Okta / SSO setup
- Benefits links
- Laptop / IT support
- Payroll, badge, first-day schedule

## Signature (draft)
```python
def answer_day_one_logistics(topic: str) -> str:
    """Return a Day 1 onboarding fact + source for the given topic."""
```

## Notes
- Keep entries with a `source` field so the agent can cite it.

Related: [[Phase 1 - Foundation & Day 1 Skills]]
