---
tags: [hackathon, tool]
phase: 2
data-source: local-json
---

# Tool 2 — `get_access_instructions`

**Data source:** Hardcoded list of X-Bot / ServiceNow access workflows.

**Purpose:** Given a system name, return exact provisioning instructions.

## Access map (to be filled in — see [[Open Questions]])
| System | How to request |
|---|---|
| UBVM | `@X-Bot request UBVM` |
| Cursor IDE | `@X-Bot request access to Cursor` |
| GitHub repo | ServiceNow URL: _TBD_ |
| Daily cluster | _TBD_ |

## Signature (draft)
```python
def get_access_instructions(system_name: str) -> str:
    """Return the exact @X-Bot command or ServiceNow link for a system."""
```

## Notes
- Return commands in a way that survives Slack code-block formatting (Phase 4).

Related: [[Phase 2 - X-Bot Integration]]
