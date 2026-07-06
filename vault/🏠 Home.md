---
tags: [hackathon, moc]
status: active
---

# 🏠 Personal Onboarding Assistant — Vault Home

A Slack bot that acts as a **Personalized Onboarding Coach** for a pilot team at Nutanix. It uses an **agentic loop (LangGraph)** to route natural-language questions to the right internal data source and returns team-tailored answers with source citations.

> [!tip] One-liner
> Not just document retrieval — the bot understands org workflows and hands you the exact `@X-Bot` command or ServiceNow link to get access.

## 🗺️ Map of Content

### Context
- [[01 - Problem & Goal]]
- [[02 - Architecture & Tech Stack]]

### Development Path
- [[Phase 1 - Foundation & Day 1 Skills]]
- [[Phase 2 - X-Bot Integration]]
- [[Phase 3 - RAG for Tribal Knowledge]]
- [[Phase 4 - Slack Integration & UI Polish]]

### Tools (the agent's toolbelt)
- [[Tool 1 - answer_day_one_logistics]]
- [[Tool 2 - get_access_instructions]]
- [[Tool 3 - search_confluence_wiki]]
- [[Tool 4 - search_slack_history]]

### Planning & Tracking
- [[Scope Constraints]]
- [[Definition of Done]]
- [[Open Questions]]
- [[Decision Log]]
- [[Setup & Credentials]]

## ✅ Definition of Done (quick view)
A Slack user DMs the bot three queries and gets good answers:
1. A general HR/IT question
2. A system-access request → yields an `@X-Bot` command
3. A specific technical question → summarized answer from Confluence/Slack **with a source link**

See [[Definition of Done]] for detail.
