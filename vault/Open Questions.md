---
tags: [hackathon, questions]
---

# Open Questions

Things I need from you before/while building. (Answers → [[Decision Log]] / [[Setup & Credentials]].)

## Pilot team
- [x] **Which team** is the pilot? → **Nutanix IAM team** (decided 2026-07-05)
- [ ] IAM team's **Slack help channel** id?
- [ ] IAM team's **Confluence space key**?

## LLM
- [ ] Which **LLM provider/model** is approved (OpenAI vs Anthropic)? → *TBD, need to find out.* Do you have an API key / gateway endpoint?

## X-Bot / access workflows (Phase 2)
- [ ] Exact `@X-Bot` commands for the pilot team (UBVM, Cursor, cluster, etc.)?
- [ ] ServiceNow URL(s) for GitHub repo access and any other systems?

## Confluence (Phase 3)
- [ ] Confluence base URL (e.g. `confluence.eng.nutanix.com`), **space key**, and API token / auth method?

## Slack (Phase 3 + 4)
- [ ] Can you create a Slack app in the workspace (needed for Bolt + Socket Mode)?
- [ ] `search.messages` needs a **user token** with `search:read` — is that obtainable, or should we fall back to `conversations.history` on a specific channel?
- [ ] Which **help channel(s)** should Tool 4 search?

## Stretch
- [ ] Do you want Google Drive / Jira in scope, or leave as stretch only?

## Repo / environment
- [ ] Where should the code live (this `hackathon` folder)? Python version? Preferred package manager (uv/pip/poetry)?
