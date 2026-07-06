---
tags: [hackathon, log]
---

# Decision Log

Running record of decisions made during the hackathon.

| Date | Decision | Rationale |
|---|---|---|
| 2026-07-05 | Vault created under `hackathon/vault/` | Keep planning notes alongside code in the same workspace |
| 2026-07-05 | **Agent tools = direct API calls, not MCP** | Matches brief; fewer moving parts; full control over HTML cleaning + citation formatting for the hackathon |
| 2026-07-05 | **Slack via `slack-bolt`/`slack_sdk` (Socket Mode), not MCP** | Bolt is required for the live bot interface anyway; reuse the same client for Tool 4 history search |
| 2026-07-05 | **Python 3.12 via `uv`** | System had only bleeding-edge 3.14 (risky wheels) and old 3.9; 3.12 is best-supported for langchain/langgraph. `uv` is fast and manages the interpreter |
| 2026-07-05 | Dedicated `git init` in `hackathon/` + `.gitignore` | Self-contained repo; keeps `.env`/`.venv` out of version control |
| 2026-07-05 | **Pilot team = Nutanix IAM team** | Selected pilot for the POC; all data sources/prompts scope to IAM |

> Add rows as decisions are made. Link out to the relevant note when useful.
