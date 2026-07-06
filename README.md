# Personal Onboarding Assistant (Hackathon POC)

A Slack bot that acts as a **Personalized Onboarding Coach** for a pilot team at Nutanix
(pilot: the **IAM team**). It uses an **agentic loop (LangGraph)** to route natural-language
questions to the right internal data source and returns team-tailored answers **with source
citations**.

> Not just document retrieval — the bot understands org workflows and hands you the exact
> `@X-Bot` command or link needed to get access.

Planning notes live in the [`vault/`](./vault) Obsidian vault (start at `🏠 Home`).

---

## 🎯 End goal (Definition of Done)

A successful demo = a Slack user DMs the bot **three distinct queries** and gets good answers:

1. A general **HR/IT** question (e.g. "Where do I find my benefits?").
2. A **system-access** request → yields the exact `@X-Bot` command / link.
3. A specific **technical** question → a summarized answer pulled from a Confluence page
   or Slack thread, **complete with a source link**.

## 🔭 Current scope (POC)

- **Single pilot team**: Nutanix **IAM** (spaces `IAM20`/`PRIS`, channel `#iam-help`). No global rollout.
- **LLM runs locally** via **Ollama** (`qwen2.5:7b`) — the NAI gateway is unavailable this cycle (GPU shortage).
- **Guidance, not provisioning**: the bot tells you *how* to get access; it never provisions it.
- **In scope:** Day-1 logistics, X-Bot/Canaveral access guidance, Confluence + Slack retrieval.
- **Out of scope:** automated provisioning, data migration, Google Drive & Jira (dropped from MVP).

## 🧱 Tech stack

- **Interface:** Slack Bolt for Python (Socket Mode)
- **Orchestration:** LangGraph / LangChain (agentic loop: LLM node + tool node)
- **LLM:** local **Ollama** `qwen2.5:7b` (default); OpenAI/Anthropic supported via `LLM_PROVIDER`
- **Data sources:** local JSON (Day-1 facts + access map), Confluence REST (CQL), Slack Web API (`conversations.history`)

---

## ✅ Status

| Phase | What | Status |
|---|---|---|
| **0** | Repo, venv (uv/py3.12), deps, `.env`, git, Ollama + model | ✅ Done |
| **1** | LangGraph agent + `answer_day_one_logistics` (Tool 1) | ✅ Done & live-tested |
| **2** | `get_access_instructions` (Tool 2) | 🟡 Data ready, tool not built |
| **3** | `search_confluence_wiki` (Tool 3) + `search_slack_history` (Tool 4) | ⬜ Not started (needs creds) |
| **4** | Slack Bolt app (Socket Mode) + Slack-Markdown output | ⬜ Not started |

### Done in detail
- **Environment:** Python 3.12 venv via `uv`; all deps installed; `.env` config loader; `.gitignore` (secrets safe).
- **Local LLM:** Ollama installed (brew service, auto-starts) with `qwen2.5:7b` pulled — chosen for the M1 Pro / 16 GB dev machine (best tool-calling that fits in memory).
- **Phase 1 (live-tested):**
  - LangGraph `StateGraph` — `agent` (LLM) node + `tools` (`ToolNode`) + conditional loop.
  - Strict grounding system prompt (must call a tool, cite sources verbatim, no invented facts — fixed an early hallucination bug).
  - **Tool 1** `answer_day_one_logistics` reads `data/day_one_facts.json`, returns cited answers.
  - CLI harness (`onboarding_assistant.cli`) — interactive + single-shot.
- **Phase 2 data:** `data/access_map.json` populated with real IAM workflows (Cursor, UBVM, Confluence/Jira via X-Bot; GitHub via the Canaveral self-invite UI).

### Left to do
- **Phase 2:** write the `get_access_instructions` tool (reads the existing map), register it, CLI-test. *No credentials needed.*
- **Phase 3 (the real data-collection module):**
  - **Tool 3 — Confluence:** CQL search over `IAM20`/`PRIS` + BeautifulSoup HTML stripping. Needs a **Confluence API token**.
  - **Tool 4 — Slack:** `conversations.history` on `#iam-help` + thread expansion via `conversations.replies` (NOT `search.messages` — prohibited). Needs a **Slack bot token** + the **`#iam-help` channel ID**.
- **Phase 4:** Slack Bolt app in the `nutanixtest.slack.com` sandbox (Socket Mode), wire events → agent, format Slack Markdown + clickable citations.
- **Data polish:** replace Tool 1's **sample** facts/URLs (`data/day_one_facts.json`, "replace with real URL") with real Nutanix links.
- **Open question:** add a "daily cluster" access entry (command unknown — placeholder for now).

### Credentials still needed (from user)
- Confluence personal API token (+ username if basic auth)
- Slack app in the sandbox → `SLACK_BOT_TOKEN` (`xoxb-`), `SLACK_APP_TOKEN` (`xapp-`)
- `#iam-help` channel ID (`C…`)

---

## 📁 Project layout
```
hackathon/
├── src/onboarding_assistant/
│   ├── config.py               # loads + validates .env
│   ├── llm.py                  # builds the chat model (ollama/openai/anthropic)
│   ├── agent.py                # LangGraph agent loop + system prompt
│   ├── cli.py                  # terminal test harness
│   └── tools/
│       ├── __init__.py         # ALL_TOOLS registry
│       └── day_one.py          # Tool 1: answer_day_one_logistics
├── data/
│   ├── day_one_facts.json      # Tool 1 source data (SAMPLE - replace URLs)
│   └── access_map.json         # Tool 2 X-Bot / Canaveral map (real)
├── vault/                      # Obsidian planning vault
├── requirements.txt            # deps (pinned snapshot in requirements.lock.txt)
├── .env.example                # copy to .env and fill in
└── README.md
```

## 🚀 Setup
This project uses [`uv`](https://github.com/astral-sh/uv) with **Python 3.12**.

```bash
# 1. Environment + deps
uv venv --python 3.12
uv pip install -r requirements.txt

# 2. Config
cp .env.example .env      # then fill in the values

# 3. Local LLM via Ollama (tool-calling capable model required)
ollama pull qwen2.5:7b    # recommended for 16GB M1 Pro (alt: llama3.1:8b / mistral:7b)
# Ollama runs as a background service (brew services start ollama)

# 4. Run the CLI
PYTHONPATH=src python -m onboarding_assistant.cli "Where do I find my benefits?"
PYTHONPATH=src python -m onboarding_assistant.cli   # interactive REPL

# (later) python -m onboarding_assistant.slack_app  # Phase 4 Slack bot
```

> Prefer plain `venv` + `pip`? `python3.12 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`.
> Note: plain `llama3` has **no** tool-calling support — use `qwen2.5:7b`, `llama3.1`, or `mistral`.

## 🗺️ Build path
Build the agent + 4 tools in the CLI first (Phases 1–3), then bolt on Slack last (Phase 4).

1. **Phase 1** — LangGraph skeleton + `answer_day_one_logistics` (local JSON) ✅
2. **Phase 2** — `get_access_instructions` (X-Bot / Canaveral map) 🟡
3. **Phase 3** — `search_confluence_wiki` (CQL + BeautifulSoup) & `search_slack_history` (`conversations.history`)
4. **Phase 4** — Slack Bolt (Socket Mode), Slack-Markdown formatting, citations
