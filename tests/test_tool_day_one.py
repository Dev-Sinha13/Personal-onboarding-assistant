"""Tests for Tool 1 — answer_day_one_logistics."""

from __future__ import annotations

import pytest

from onboarding_assistant.tools.day_one import _load_facts, _score, answer_day_one_logistics


def call(query: str) -> str:
    return answer_day_one_logistics.invoke({"query": query})


def test_tool_metadata():
    assert answer_day_one_logistics.name == "answer_day_one_logistics"
    assert answer_day_one_logistics.description  # non-empty docstring


@pytest.mark.parametrize(
    "query,expected_substr",
    [
        ("Where do I find my benefits?", "Workday"),
        ("how do I connect to the VPN", "VPN"),
        ("okta sso setup", "Okta"),
        ("when do I get paid", "Workday"),
        ("my laptop is broken", "Help Desk"),
    ],
)
def test_known_queries_return_relevant_answer(query, expected_substr):
    result = call(query)
    assert expected_substr.lower() in result.lower()


@pytest.mark.parametrize(
    "query",
    ["Where do I find my benefits?", "how do I connect to the VPN", "okta setup"],
)
def test_answers_always_include_a_source(query):
    assert "Source:" in call(query)


def test_unknown_query_returns_no_match_message():
    result = call("xyzzy quantum flux capacitor")
    assert "No Day-1 logistics entry" in result


def test_score_counts_shared_terms():
    fact = {"topic": "vpn", "question_examples": ["connect vpn"], "answer": "install client"}
    assert _score("how do I connect vpn", fact) > 0
    assert _score("completely unrelated", fact) == 0


def test_short_words_are_ignored_in_scoring():
    # words of length <= 2 should not contribute (avoids matching on "my", "do")
    fact = {"topic": "benefits", "question_examples": [], "answer": "benefits in Workday"}
    assert _score("do my hr", fact) == 0


def test_results_are_capped_at_three():
    # a very broad query still returns at most 3 entries
    result = call("okta vpn benefits payroll laptop first day")
    assert result.count("Source:") <= 3


def test_load_facts_is_cached():
    assert _load_facts() is _load_facts()
