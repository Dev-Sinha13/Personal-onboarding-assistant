---
tags: [hackathon, tool]
phase: 3
data-source: slack
---

# Tool 4 — `search_slack_history`

**Data source:** Slack `conversations.history` (+ `conversations.replies`).

**Purpose:** Query past conversations in `#iam-help` for historical Q&A / tribal knowledge.

> [!warning] Do NOT use `search.messages`
> `search:read` is a **prohibited high-risk scope** at Nutanix and will be rejected.
> Use a **Bot Token** with **`channels:history`** and call **`conversations.history`**
> on the specific channel, then expand matches with **`conversations.replies`**.

## Key requirements
- Scope to `#iam-help` (need the channel id `C…`).
- Pull message + full thread so the LLM sees the actual answer, not just the question.
- Return message **permalink** for citations.
- Keyword-match / rank locally over recent history (no server-side search API).

## Signature (draft)
```python
def search_slack_history(query: str) -> list[dict]:
    """conversations.history on #iam-help; expand threads; return text + permalinks."""
```

## Open items
- `SLACK_BOT_TOKEN` with `channels:history`; `#iam-help` channel id. See [[Open Questions]].

Related: [[Phase 3 - RAG for Tribal Knowledge]]
