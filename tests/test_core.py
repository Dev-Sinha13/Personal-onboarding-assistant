"""Tests for config, LLM dispatch, and the LangGraph agent structure.

None of these require a running LLM server — they exercise wiring only.
"""

from __future__ import annotations

from types import SimpleNamespace

import pytest

from onboarding_assistant import llm as llm_module
from onboarding_assistant.config import Settings


# --- config ------------------------------------------------------------------

def test_space_key_list_parsing():
    s = Settings(confluence_space_keys="IAM20, PRIS ,, ")
    assert s.space_key_list == ["IAM20", "PRIS"]


def test_space_key_list_empty():
    assert Settings(confluence_space_keys="").space_key_list == []


def test_missing_reports_empty_fields():
    s = Settings(openai_api_key="", slack_bot_token="xoxb-123")
    assert "openai_api_key" in s.missing(["openai_api_key", "slack_bot_token"])
    assert "slack_bot_token" not in s.missing(["slack_bot_token"])


# --- llm dispatch ------------------------------------------------------------

def _fake_settings(**kw):
    base = dict(
        llm_provider="ollama",
        llm_model="test-model",
        ollama_base_url="http://localhost:11434",
        openai_api_key="k",
        anthropic_api_key="k",
    )
    base.update(kw)
    return SimpleNamespace(**base)


def test_build_llm_ollama(monkeypatch):
    monkeypatch.setattr(llm_module, "settings", _fake_settings(llm_provider="ollama"))
    model = llm_module.build_llm()
    assert model.__class__.__name__ == "ChatOllama"
    assert model.model == "test-model"


def test_build_llm_unknown_provider_raises(monkeypatch):
    monkeypatch.setattr(llm_module, "settings", _fake_settings(llm_provider="bogus"))
    with pytest.raises(ValueError):
        llm_module.build_llm()


def test_build_llm_openai(monkeypatch):
    monkeypatch.setattr(llm_module, "settings", _fake_settings(llm_provider="openai"))
    model = llm_module.build_llm()
    assert model.__class__.__name__ == "ChatOpenAI"


def test_build_llm_anthropic(monkeypatch):
    monkeypatch.setattr(llm_module, "settings", _fake_settings(llm_provider="anthropic"))
    model = llm_module.build_llm()
    assert model.__class__.__name__ == "ChatAnthropic"


def test_build_llm_provider_is_case_insensitive(monkeypatch):
    monkeypatch.setattr(llm_module, "settings", _fake_settings(llm_provider="OLLAMA"))
    assert llm_module.build_llm().__class__.__name__ == "ChatOllama"


# --- agent graph -------------------------------------------------------------

def test_agent_compiles_with_expected_topology():
    from onboarding_assistant.agent import build_agent

    agent = build_agent()
    graph = agent.get_graph()
    nodes = set(graph.nodes)
    assert {"agent", "tools"} <= nodes

    edges = {(e.source, e.target) for e in graph.edges}
    assert ("__start__", "agent") in edges
    assert ("tools", "agent") in edges  # loop back after tool execution


def test_system_prompt_is_grounded_and_team_scoped():
    from onboarding_assistant.agent import system_prompt

    p = system_prompt().lower()
    assert "onboarding coach" in p
    assert "cite" in p or "source" in p
    assert "tool" in p


def test_all_tools_registered():
    from onboarding_assistant.tools import ALL_TOOLS

    names = {t.name for t in ALL_TOOLS}
    assert {"answer_day_one_logistics", "get_access_instructions"} <= names
