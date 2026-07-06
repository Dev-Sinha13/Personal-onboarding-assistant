---
tags: [hackathon, questions]
---

# Open Questions

Most items are now resolved from planning (2026-07-05). Remaining unknowns are at the bottom.

## ✅ Resolved
- **Pilot team** → **Nutanix IAM team**
- **LLM** → NAI Gateway unavailable (GPU shortage). Use **local Ollama** (`http://localhost:11434`), model `llama3`/`mistral`. No API key needed.
- **Slack help channel** → `#iam-help`
- **Confluence** → spaces `IAM20` (+ `PRIS`), base `https://confluence.eng.nutanix.com:8443`
- **X-Bot commands** →
  - Cursor: `@X-Bot request access to Cursor`
  - UBVM: `@X-Bot request UBVM` (or "I want a new UBVM")
  - Confluence/Jira: ask X-Bot `get Confluence/Jira`
  - GitHub: **no ServiceNow** — self-invite via Canaveral UI (OKTA/SAML)
- **Slack API approach** → `search.messages`/`search:read` is **PROHIBITED**. Use **Bot Token + `channels:history` + `conversations.history`** on `#iam-help` (threads via `conversations.replies`).
- **Slack app** → allowed; **build/test in sandbox** `nutanixtest.slack.com` first; Socket Mode.
- **Scope** → Google Drive + Jira **dropped** from MVP (Confluence + Slack only).

## ❓ Still open
- [ ] **Slack tokens** — create the app in the sandbox and get `SLACK_BOT_TOKEN` (`xoxb-`) + `SLACK_APP_TOKEN` (`xapp-`).
- [ ] **`#iam-help` channel ID** (`C…`) — needed for `conversations.history`.
- [ ] **Confluence API token** (personal PAT) + username (if basic auth).
- [ ] **Ollama** installed locally with the model pulled (`ollama pull qwen2.5:7b`)?
- [x] Best local model for tool-calling → **`qwen2.5:7b`** (M1 Pro / 16GB). Revisit only if routing quality is poor.
