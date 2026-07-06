---
tags: [hackathon, phase]
phase: 2
status: not-started
---

# Phase 2 — Actionable Guidance (X-Bot Integration)

**Goal:** Teach the bot how Nutanix provisions access so it can guide the user.

## Tasks
- [x] **Map access workflows** — real IAM commands in `data/access_map.json` (Cursor, UBVM, Confluence/Jira via X-Bot; GitHub via Canaveral).
- [x] **Build [[Tool 2 - get_access_instructions]]** — `tools/access.py`; name/alias matching → exact instruction (+ link). Graceful fallback to #iam-help for unknown systems.
- [x] **Register** in `ALL_TOOLS`.
- [x] **CLI test** — access Qs route to Tool 2 and return the exact command; fact Qs still route to Tool 1.

## Status — ✅ COMPLETE
Live-tested against Ollama `qwen2.5:7b`:
- "How do I get access to Cursor?" → `@X-Bot request access to Cursor`
- "...daily cluster?" → placeholder guidance (see below)
- "Where do I find my benefits?" → still Tool 1 (routing intact)

## Exit Criteria — met
Agent maps a system-access question to Tool 2 and returns a copy-pasteable `@X-Bot` command / link. ✅

> [!warning] Open data gap
> **Daily/dev cluster** access command is a **placeholder** (`todo: true` in access_map.json).
> Confirm the exact command with the IAM team and replace it.

Related: [[Phase 1 - Foundation & Day 1 Skills]] · [[Phase 3 - RAG for Tribal Knowledge]] · [[🏠 Home]]
