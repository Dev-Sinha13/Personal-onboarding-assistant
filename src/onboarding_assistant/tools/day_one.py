"""Tool 1 — answer_day_one_logistics.

Reads a local JSON of standard Day-1 HR/IT onboarding facts and returns the
best-matching entries with sources for the agent to cite.
"""

from __future__ import annotations

import json
from functools import lru_cache

from langchain_core.tools import tool

from ..config import DATA_DIR

_FACTS_PATH = DATA_DIR / "day_one_facts.json"


@lru_cache(maxsize=1)
def _load_facts() -> list[dict]:
    data = json.loads(_FACTS_PATH.read_text())
    return data.get("facts", [])


def _score(query: str, fact: dict) -> int:
    haystack = " ".join(
        [
            fact.get("topic", ""),
            " ".join(fact.get("question_examples", [])),
            fact.get("answer", ""),
        ]
    ).lower()
    words = {w for w in query.lower().split() if len(w) > 2}
    return sum(1 for w in words if w in haystack)


@tool
def answer_day_one_logistics(query: str) -> str:
    """Answer standard Day-1 HR/IT onboarding logistics questions.

    Good for: benefits, Okta/SSO/MFA setup, laptop/IT help desk, VPN, payroll,
    and first-day checklist questions. NOT for team-specific technical questions
    or system access requests (use the other tools for those).

    Returns matching facts, each with a source to cite.
    """
    facts = _load_facts()
    scored = [(s, f) for f in facts if (s := _score(query, f)) > 0]
    scored.sort(key=lambda pair: pair[0], reverse=True)

    if not scored:
        return (
            "No Day-1 logistics entry matched that question. "
            "Try rephrasing (e.g. benefits, Okta, VPN, payroll, IT support)."
        )

    lines = []
    for _, fact in scored[:3]:
        lines.append(f"- {fact['answer']}\n  Source: {fact.get('source', '(no source)')}")
    return "\n".join(lines)
