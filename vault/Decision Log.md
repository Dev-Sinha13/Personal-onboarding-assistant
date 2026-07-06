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
| 2026-07-05 | **LLM = local Ollama (`llama3`)** | NAI Gateway keys unavailable for the intern hackathon (GPU shortage). Run models locally; OpenAI-compatible endpoint at `http://localhost:11434/v1` |
| 2026-07-05 | **Slack: `conversations.history`, NOT `search.messages`** | `search:read` is a prohibited high-risk scope at Nutanix; use Bot Token + `channels:history` on `#iam-help`, expand threads via `conversations.replies` |
| 2026-07-05 | **Build/test Slack app in sandbox** `nutanixtest.slack.com` | Required before touching the real workspace |
| 2026-07-05 | **Confluence spaces = IAM20 (+ PRIS)** @ `confluence.eng.nutanix.com:8443` | The IAM team's real spaces |
| 2026-07-05 | **GitHub access via Canaveral UI** (not ServiceNow) | Self-invite through OKTA/SAML at the Canaveral URL |
| 2026-07-05 | **Google Drive + Jira dropped from MVP** | Focus energy on Confluence + Slack to ship a working demo |
| 2026-07-05 | **Ollama model = `qwen2.5:7b`** | Dev machine is M1 Pro / 16GB unified memory → 7-8B Q4 (~5GB) is the sweet spot with OS headroom. Qwen2.5-7B has the best tool-calling in that class (critical for the agent loop). Alts: llama3.1:8b, mistral:7b |

> Add rows as decisions are made. Link out to the relevant note when useful.
