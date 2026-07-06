"""Tests for Tool 2 — get_access_instructions."""

from __future__ import annotations

import pytest

from onboarding_assistant.tools.access import _load_systems, _match, get_access_instructions


def call(system: str) -> str:
    return get_access_instructions.invoke({"system": system})


def test_tool_metadata():
    assert get_access_instructions.name == "get_access_instructions"
    assert get_access_instructions.description


@pytest.mark.parametrize(
    "query,expected_substr",
    [
        ("Cursor", "request access to Cursor"),
        ("cursor ide", "request access to Cursor"),
        ("ide", "request access to Cursor"),
        ("UBVM", "request UBVM"),
        ("I want a new vm", "request UBVM"),
        ("confluence", "get Confluence/Jira"),
        ("jira", "get Confluence/Jira"),
        ("github", "Canaveral"),
        ("daily cluster", "UBVM"),
    ],
)
def test_known_systems_and_aliases(query, expected_substr):
    assert expected_substr.lower() in call(query).lower()


def test_self_service_entry_includes_link():
    result = call("github")
    assert "Link:" in result
    assert "http" in result


def test_unknown_system_returns_fallback_with_known_list():
    result = call("kubernetes prod database")
    assert "don't have a known access path" in result
    assert "Cursor IDE" in result  # lists known systems
    assert "#iam-help" in result


def test_exact_match_beats_word_match():
    # "cursor" exact-ish alias should map to Cursor, not something sharing a word
    assert "Cursor" in call("cursor")


def test_match_scoring_levels():
    entry = {"system": "UBVM", "aliases": ["dev vm", "new vm"]}
    assert _match("ubvm", entry) == 3          # exact
    assert _match("i need a dev vm please", entry) == 2  # substring of alias
    assert _match("vm", entry) >= 1            # shared word
    assert _match("nothing relevant", entry) == 0


def test_case_insensitive():
    assert call("CURSOR") == call("cursor")


def test_load_systems_is_cached():
    assert _load_systems() is _load_systems()
