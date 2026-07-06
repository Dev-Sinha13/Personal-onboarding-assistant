---
tags: [hackathon, phase]
phase: 4
status: not-started
---

# Phase 4 — Slack Integration & UI Polish

**Goal:** Move the bot out of the terminal and into Slack for the final demo.

## Tasks
- [ ] **Slack Bolt setup** — create a Slack app, enable **Socket Mode**, subscribe to `app_mention` and `message.im` events.
- [ ] **Wire the brain** — on a Slack event, pass the message text to the LangGraph executor.
- [ ] **Format the output** — Slack Markdown:
  - Wrap `@X-Bot` commands in code blocks (easy to copy).
  - Format citations as clickable links: `<https://confluence.eng.nutanix.com...|IAM Guide>`.

## Exit Criteria
The bot works end-to-end from a Slack DM and matches [[Definition of Done]].

Related: [[Phase 3 - RAG for Tribal Knowledge]] · [[Definition of Done]] · [[🏠 Home]]
