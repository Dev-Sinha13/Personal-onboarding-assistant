---
tags: [hackathon, phase]
phase: 3
status: not-started
---

# Phase 3 — Dynamic Retrieval (RAG for Tribal Knowledge)

**Goal:** Allow the bot to read Confluence and Slack to answer technical team questions.

## Tasks
- [ ] **Build [[Tool 3 - search_confluence_wiki]]** — Atlassian REST API (CQL) to search the pilot team's Confluence space.
  - **Crucial:** implement an HTML stripper (e.g. BeautifulSoup) so the LLM only receives clean text.
- [ ] **Build [[Tool 4 - search_slack_history]]** — Slack `conversations.history` (NOT `search.messages` — prohibited) on `#iam-help`, expand threads via `conversations.replies`.
- [ ] **CLI test — routing:**
  - *"What is the architecture of our core service?"* → Confluence tool
  - *"Who approves PRs for the main repo?"* → Slack tool

## Exit Criteria
Agent routes technical questions to the correct retrieval tool and returns a summarized, clean answer with a source link.

Related: [[Phase 2 - X-Bot Integration]] · [[Phase 4 - Slack Integration & UI Polish]] · [[🏠 Home]]
