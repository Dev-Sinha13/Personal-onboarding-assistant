---
tags: [hackathon, phase]
phase: 1
status: not-started
---

# Phase 1 — Foundation & "Day 1" Skills

**Goal:** Prove the LangGraph agent can receive a query, use a basic tool, and return a formatted answer.

## Tasks
- [ ] **Initialize LangGraph** — set up the basic State Graph with a single LLM node + a Tool Execution node.
- [ ] **Build [[Tool 1 - answer_day_one_logistics]]** — Python tool reading from a local dict/JSON of basic Nutanix onboarding facts (Okta setup, benefits links, laptop support).
- [ ] **Agent prompting** — write the system prompt: act as the *Pilot Team Onboarding Coach*, always cite sources.
- [ ] **CLI test** — agent answers *"Where do I find my benefits?"* in the terminal.

## Exit Criteria
Terminal conversation where the agent correctly answers a Day 1 logistics question using Tool 1 and cites the source.

Related: [[02 - Architecture & Tech Stack]] · [[Phase 2 - X-Bot Integration]] · [[🏠 Home]]
