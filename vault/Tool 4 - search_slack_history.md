---
tags: [hackathon, tool]
phase: 3
data-source: slack
---

# Tool 4 — `search_slack_history`

**Data source:** Slack (`search.messages` API).

**Purpose:** Query past conversations in the team's help channel for historical Q&A / tribal knowledge.

## Key requirements
- Scope to the pilot team's **help channel**.
- Return message **permalink** for citations.
- Summarize threads rather than dumping raw messages.

## Signature (draft)
```python
def search_slack_history(query: str) -> list[dict]:
    """search.messages in the team help channel; return text + permalinks."""
```

## Open items
- Slack scopes needed: `search:read` (user token) — note `search.messages` requires a **user token**, not a bot token. See [[Open Questions]].

Related: [[Phase 3 - RAG for Tribal Knowledge]]
