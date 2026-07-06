# Personal Onboarding Assistant (Hackathon POC)

A Slack bot that acts as a **Personalized Onboarding Coach** for a pilot team at Nutanix.
It uses an **agentic loop (LangGraph)** to route natural-language questions to the right
internal data source and returns team-tailored answers **with source citations**.

> Not just document retrieval — the bot understands org workflows and hands you the exact
> `@X-Bot` command or ServiceNow link needed to get access.

Planning notes live in the [`vault/`](./vault) Obsidian vault (start at `🏠 Home`).

## Tech stack
- **Interface:** Slack Bolt for Python (Socket Mode)
- **Orchestration:** LangGraph / LangChain
- **LLM:** OpenAI or Anthropic (set via `LLM_PROVIDER`)
- **Data sources:** local JSON (Day-1 facts + X-Bot access map), Confluence REST, Slack Web API

## Project layout
```
hackathon/
├── src/onboarding_assistant/   # Python package (agent, tools, slack app)
│   ├── config.py               # loads + validates .env
├── data/                       # seed data for local tools
│   ├── day_one_facts.json      # Tool 1 source data
│   └── access_map.json         # Tool 2 X-Bot / ServiceNow map
├── vault/                      # Obsidian planning vault
├── requirements.txt
├── .env.example                # copy to .env and fill in
└── README.md
```

## Setup
This project uses [`uv`](https://github.com/astral-sh/uv) with **Python 3.12**.

```bash
# 1. Create the environment (Python 3.12) and install deps
uv venv --python 3.12
uv pip install -r requirements.txt

# 2. Configure secrets
cp .env.example .env      # then fill in the values

# 3. (later) run the CLI / Slack app
# python -m onboarding_assistant.cli        # Phase 1-3 CLI testing
# python -m onboarding_assistant.slack_app  # Phase 4 Slack bot
```

> Prefer plain `venv` + `pip`? `python3.12 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`.

## Build path
See the vault for the full plan. In short: build the agent + 4 tools in the CLI
(Phases 1–3), then bolt on Slack last (Phase 4).

1. **Phase 1** — LangGraph skeleton + `answer_day_one_logistics` (local JSON)
2. **Phase 2** — `get_access_instructions` (X-Bot / ServiceNow map)
3. **Phase 3** — `search_confluence_wiki` (CQL + BeautifulSoup) & `search_slack_history`
4. **Phase 4** — Slack Bolt (Socket Mode), Slack-Markdown formatting, citations

## Scope (POC)
No automated provisioning (tells you *how* to get access), no data migration,
everything hardcoded to a **single pilot team**.
