---
tags: [hackathon, phase]
phase: 2
status: not-started
---

# Phase 2 — Actionable Guidance (X-Bot Integration)

**Goal:** Teach the bot how Nutanix provisions access so it can guide the user.

## Tasks
- [ ] **Map access workflows** — document the exact commands the pilot team uses, e.g.:
  - `@X-Bot request UBVM`
  - `@X-Bot request access to Cursor`
  - ServiceNow URL for GitHub repo access
- [ ] **Build [[Tool 2 - get_access_instructions]]** — takes a system name, returns exact provisioning instructions.
- [ ] **CLI test** — agent answers *"How do I get access to the daily cluster?"* by instructing the user to use X-Bot.

## Exit Criteria
Agent maps a system-access question to Tool 2 and returns a copy-pasteable `@X-Bot` command or ServiceNow link.

> [!question] Needs input
> The exact X-Bot commands / ServiceNow URLs for the pilot team need to be gathered. See [[Open Questions]].

Related: [[Phase 1 - Foundation & Day 1 Skills]] · [[Phase 3 - RAG for Tribal Knowledge]] · [[🏠 Home]]
