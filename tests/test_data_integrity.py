"""Data-integrity tests for the local JSON that the tools depend on.

These catch malformed or incomplete data before it silently degrades the agent
(e.g. a fact missing its 'source', or an access entry with no instructions).
"""

from __future__ import annotations

import json

import pytest

from onboarding_assistant.config import DATA_DIR

DAY_ONE = DATA_DIR / "day_one_facts.json"
ACCESS = DATA_DIR / "access_map.json"


def _load(path):
    return json.loads(path.read_text())


def test_files_exist():
    assert DAY_ONE.is_file()
    assert ACCESS.is_file()


def test_day_one_is_valid_json_with_facts():
    data = _load(DAY_ONE)
    assert isinstance(data.get("facts"), list)
    assert len(data["facts"]) >= 1


@pytest.mark.parametrize("field", ["topic", "answer", "source", "question_examples"])
def test_every_day_one_fact_has_required_fields(field):
    for fact in _load(DAY_ONE)["facts"]:
        assert field in fact, f"fact {fact.get('topic')!r} missing {field!r}"
        assert fact[field], f"fact {fact.get('topic')!r} has empty {field!r}"


def test_day_one_question_examples_are_nonempty_lists():
    for fact in _load(DAY_ONE)["facts"]:
        assert isinstance(fact["question_examples"], list)
        assert len(fact["question_examples"]) >= 1


def test_day_one_topics_are_unique():
    topics = [f["topic"] for f in _load(DAY_ONE)["facts"]]
    assert len(topics) == len(set(topics)), "duplicate topics found"


def test_access_is_valid_json_with_systems():
    data = _load(ACCESS)
    assert isinstance(data.get("systems"), list)
    assert len(data["systems"]) >= 1


@pytest.mark.parametrize("field", ["system", "aliases", "instructions", "type"])
def test_every_access_entry_has_required_fields(field):
    for entry in _load(ACCESS)["systems"]:
        assert field in entry, f"system {entry.get('system')!r} missing {field!r}"
        assert entry[field] != "", f"system {entry.get('system')!r} empty {field!r}"


def test_access_aliases_are_lists():
    for entry in _load(ACCESS)["systems"]:
        assert isinstance(entry["aliases"], list)


def test_access_self_service_entries_have_url():
    for entry in _load(ACCESS)["systems"]:
        if entry.get("type") == "self-service":
            assert entry.get("url", "").startswith("http")
