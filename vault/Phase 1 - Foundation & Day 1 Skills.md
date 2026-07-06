---
tags: [hackathon, phase]
phase: 1
status: not-started
---

# Phase 1 — Foundation & "Day 1" Skills

**Goal:** Prove the LangGraph agent can receive a query, use a basic tool, and return a formatted answer.

## Tasks
- [x] **Initialize LangGraph** — StateGraph (`agent` LLM node + `tools` ToolNode + conditional edges) in `src/onboarding_assistant/agent.py`.
- [x] **Build [[Tool 1 - answer_day_one_logistics]]** — `tools/day_one.py`, reads `data/day_one_facts.json` (seeded with sample entries), returns cited matches.
- [x] **Agent prompting** — system prompt in `agent.py` (Onboarding Coach for the IAM team, always cite sources).
- [x] **CLI** — `cli.py` (interactive + single-shot).
- [x] **CLI test (live)** — Ollama installed (brew service) + `qwen2.5:7b` pulled. Agent answers "Where do I find my benefits?" via Tool 1 with correct Workday citation, consistently across runs.

## Status — ✅ COMPLETE
- Ollama running as a brew service; `qwen2.5:7b` pulled.
- Live tested: benefits + VPN queries route to Tool 1 and cite seeded sources.
- Out-of-scope question ("IAM authz architecture") correctly declines instead of hallucinating.

## Learning: small-model grounding
First live run **hallucinated** the benefits answer (invented an Okta source). Fix was a
**stricter system prompt** in `agent.py`: must call a tool, ground answers ONLY in tool
output, copy Source lines verbatim, no invented commands. After that, 3/3 runs were
correct and consistent. Keep this grounding discipline as more tools are added.

## Exit Criteria — met
Terminal conversation where the agent correctly answers a Day 1 logistics question using Tool 1 and cites the source. ✅

Related: [[02 - Architecture & Tech Stack]] · [[Phase 2 - X-Bot Integration]] · [[🏠 Home]]
