---
tags: [hackathon, tool]
phase: 2
data-source: local-json
---

# Tool 2 — `get_access_instructions`

**Data source:** Hardcoded list of X-Bot / ServiceNow access workflows.

**Purpose:** Given a system name, return exact provisioning instructions.

## Access map (Nutanix IAM — see `data/access_map.json`)
| System | How to request |
|---|---|
| Cursor IDE | `@X-Bot request access to Cursor` |
| UBVM | `@X-Bot request UBVM` (or "I want a new UBVM") |
| Confluence / Jira | ask X-Bot: `get Confluence/Jira` |
| GitHub repo | **No ServiceNow.** Self-invite via Canaveral UI (OKTA/SAML): `https://canaveral-ui.corp.p10y.ntnxdpro.com/#/account/github` |

## Signature (draft)
```python
def get_access_instructions(system_name: str) -> str:
    """Return the exact @X-Bot command or ServiceNow link for a system."""
```

## Notes
- Return commands in a way that survives Slack code-block formatting (Phase 4).

Related: [[Phase 2 - X-Bot Integration]]
