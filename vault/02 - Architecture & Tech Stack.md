---
tags: [hackathon, architecture]
---

# 02 — Architecture & Tech Stack

## Stack
| Layer | Choice |
|---|---|
| **Interface** | Slack App (Slack Bolt for Python, Socket Mode) |
| **Orchestration** | LangGraph / LangChain — agentic loop + tool routing |
| **LLM** | OpenAI / Anthropic (whichever approved model is available) |

## Data Sources (a.k.a. the "Tools")
- **Local JSON / static vector DB** — standard Day 1 HR/IT logistics + hardcoded X-Bot access commands → [[Tool 1 - answer_day_one_logistics]], [[Tool 2 - get_access_instructions]]
- **Confluence API** — team architecture docs & setup guides → [[Tool 3 - search_confluence_wiki]]
- **Slack API (`channels:history` / `search.messages`)** — team help channels, historical Q&A, tribal knowledge → [[Tool 4 - search_slack_history]]
- **(Stretch) Google Drive / Jira APIs** — project status or specific folder links

## High-Level Flow
```
Slack DM / @mention
      │
      ▼
Slack Bolt event handler ──► LangGraph executor
                                  │
                    ┌─────────────┼───────────────┐
                    ▼             ▼                ▼
              LLM (router)   Tool node       (loop back)
                    │             │
                    ▼             ▼
              decide tool    execute tool ──► observation
                    │                              │
                    └──────────► final answer ◄────┘
                                  │
                                  ▼
                 Slack-Markdown formatted reply + citations
```

## Agent Design Notes
- **System prompt**: act as the *Pilot Team Onboarding Coach*; **always cite sources**.
- **Routing**: LLM chooses among the 4 tools based on query intent.
- **Output formatting**: Slack Markdown — wrap `@X-Bot` commands in code blocks; citations as `<url|Label>` links.

Related: [[01 - Problem & Goal]] · [[Phase 1 - Foundation & Day 1 Skills]] · [[🏠 Home]]
