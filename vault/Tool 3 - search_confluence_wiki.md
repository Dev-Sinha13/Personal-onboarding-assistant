---
tags: [hackathon, tool]
phase: 3
data-source: confluence
---

# Tool 3 — `search_confluence_wiki`

**Data source:** Confluence (Atlassian REST API, CQL search).

**Purpose:** Retrieve team architecture docs & setup guides from the pilot team's space.

## Key requirements
- Scope search to the **pilot team's Confluence space**.
- **HTML stripper** (BeautifulSoup) → feed the LLM clean text only.
- Return page **URL + title** for citations.

## Signature (draft)
```python
def search_confluence_wiki(query: str) -> list[dict]:
    """CQL search the pilot team's space; return clean text + source URLs."""
```

## Open items
- Confluence base URL, space key, auth token → see [[Setup & Credentials]] / [[Open Questions]].

Related: [[Phase 3 - RAG for Tribal Knowledge]]
