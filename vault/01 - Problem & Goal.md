---
tags: [hackathon, context]
---

# 01 — Problem & Goal

## The Problem
When a new hire (intern or full-time) joins a technical team at Nutanix, onboarding is **highly fragmented**:
- HR handles standard Day 1 logistics.
- The critical **"tribal knowledge"** needed to actually do the job is scattered across **Confluence, Slack, Google Drive, Jira, and ServiceNow**.
- New hires constantly interrupt teammates to find where things are.

What tribal knowledge covers:
- What to read
- What access to request
- How to configure the dev environment
- Who to ask for help

## The Goal
Build a **Slack Bot** that acts as a **Personalized Onboarding Coach** for a selected pilot team.

- Instead of a static checklist, use an **agentic loop (LangGraph)** to intelligently route natural-language questions to the correct internal data source.
- Provide highly specific, **team-tailored** answers **with source citations**.

## 🔑 Key Differentiator
The bot doesn't just retrieve documents — it **understands organizational workflows**. If a user needs access to a system (like a UBVM or Cursor IDE), the bot provides the exact `@X-Bot` command or ServiceNow link required to provision that access.

Related: [[02 - Architecture & Tech Stack]] · [[🏠 Home]]
