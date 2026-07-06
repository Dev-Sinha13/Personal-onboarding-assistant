"""Tool 2 — get_access_instructions.

Maps a system/tool name to the exact provisioning instruction (X-Bot command or
self-service link) from a local JSON. The bot INSTRUCTS the user; it does not
provision access itself.
"""

from __future__ import annotations

import json
from functools import lru_cache

from langchain_core.tools import tool

from ..config import DATA_DIR

_ACCESS_PATH = DATA_DIR / "access_map.json"


@lru_cache(maxsize=1)
def _load_systems() -> list[dict]:
    data = json.loads(_ACCESS_PATH.read_text())
    return data.get("systems", [])


def _match(query: str, entry: dict) -> int:
    """Score how well the query matches this system (higher = better)."""
    q = query.lower().strip()
    names = [entry.get("system", "").lower(), *[a.lower() for a in entry.get("aliases", [])]]
    score = 0
    for name in names:
        if not name:
            continue
        if q == name:
            score = max(score, 3)          # exact match
        elif name in q or q in name:
            score = max(score, 2)          # substring match
        elif any(w in q.split() for w in name.split()):
            score = max(score, 1)          # shared word
    return score


@tool
def get_access_instructions(system: str) -> str:
    """Return the exact steps to REQUEST access to an internal system or tool.

    Use this whenever the user asks how to GET ACCESS to, provision, request, or
    set up a system, tool, VM, repo, cluster, or environment — e.g. Cursor IDE,
    a UBVM, Confluence/Jira, GitHub repos, or the dev/daily cluster.

    Returns the exact @X-Bot command or link to use. This bot does NOT provision
    access itself; it only tells the user what to do.
    """
    systems = _load_systems()
    scored = [(s, e) for e in systems if (s := _match(system, e)) > 0]
    scored.sort(key=lambda pair: pair[0], reverse=True)

    if not scored:
        known = ", ".join(e.get("system", "") for e in systems)
        return (
            f"I don't have a known access path for '{system}'. "
            f"Ask in #iam-help. Known systems: {known}."
        )

    _, entry = scored[0]
    lines = [f"To get access to {entry['system']}:", entry["instructions"]]
    if entry.get("url"):
        lines.append(f"Link: {entry['url']}")
    return "\n".join(lines)
