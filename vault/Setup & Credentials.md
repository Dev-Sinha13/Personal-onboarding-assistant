---
tags: [hackathon, setup]
---

# Setup & Credentials

> [!warning] Do not commit real secrets
> Keep actual keys in a local `.env` (gitignored). This note tracks **what** is needed and where it goes, not the secret values themselves.

## Required credentials / config
| Item | Env var | Status |
|---|---|---|
| LLM (local Ollama) | `OLLAMA_BASE_URL` / `LLM_MODEL` | ✅ default set (`http://localhost:11434`, `llama3`) — needs Ollama installed locally |
| Slack bot token | `SLACK_BOT_TOKEN` | ❓ create app in sandbox |
| Slack app token (Socket Mode) | `SLACK_APP_TOKEN` | ❓ |
| ~~Slack user token~~ | — | ⛔ NOT used (`search:read` prohibited) |
| Confluence base URL | `CONFLUENCE_BASE_URL` | ✅ `https://confluence.eng.nutanix.com:8443` |
| Confluence space keys | `CONFLUENCE_SPACE_KEYS` | ✅ `IAM20,PRIS` |
| Confluence API token | `CONFLUENCE_API_TOKEN` | ❓ personal PAT |
| Help channel | `SLACK_HELP_CHANNEL_NAME` / `_ID` | ✅ `#iam-help` / ❓ id (`C…`) |

## Local dev — DONE (Phase 0 scaffolding)
- Python version: **3.12.13** (via `uv`)
- Package manager: **`uv`** (standalone install at `~/.local/bin/uv`)
- Env: `.venv/` created; deps installed from `requirements.txt` (pinned snapshot in `requirements.lock.txt`)
- Repo: `git init` done in `hackathon/`; `.env` + `.venv` gitignored
- Setup command: `uv venv --python 3.12 && uv pip install -r requirements.txt`
- Config check: `PYTHONPATH=src .venv/bin/python -m onboarding_assistant.config`

> [!note] uv + TLS in this environment
> If `uv` fails downloading Python/packages with a cert error, set `UV_SYSTEM_CERTS=1` (uses the system trust store).

## Still needed from user
- LLM API key (OpenAI or Anthropic) → put in `.env`
- Pilot team name + Slack help channel id
- Slack tokens (bot `xoxb-`, app `xapp-`, user `xoxp-` for search)
- Confluence base URL, space key, API token

Related: [[Open Questions]] · [[🏠 Home]]
