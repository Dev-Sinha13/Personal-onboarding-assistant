---
tags: [hackathon, tool]
phase: 3
data-source: confluence
---

# Tool 3 — `search_confluence_wiki`

**Data source:** Confluence (Atlassian REST API, CQL search).

**Purpose:** Retrieve team architecture docs & setup guides from the pilot team's space.

## Key requirements
- Scope to IAM spaces via CQL: `space in ("IAM20","PRIS") and text ~ "{query}"`.
- Base URL: `https://confluence.eng.nutanix.com:8443` (endpoint `/rest/api/content/search`).
- **HTML stripper** (BeautifulSoup) → feed the LLM clean text only.
- Return page **URL + title** for citations.

## Signature (draft)
```python
def search_confluence_wiki(query: str) -> list[dict]:
    """CQL search the IAM spaces (IAM20, PRIS); return clean text + source URLs."""
```

## Open items
- Confluence API token (PAT) + username → see [[Setup & Credentials]] / [[Open Questions]].

Related: [[Phase 3 - RAG for Tribal Knowledge]]
