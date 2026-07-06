"""Live end-to-end tests that actually invoke the local LLM.

These are marked `integration` and skipped automatically when no Ollama server
is reachable, so the default `pytest` run stays fast and hermetic. Run them with:

    pytest -m integration
"""

from __future__ import annotations

import urllib.request

import pytest

from onboarding_assistant.config import settings

pytestmark = pytest.mark.integration


def _ollama_up() -> bool:
    try:
        with urllib.request.urlopen(
            f"{settings.ollama_base_url}/api/version", timeout=2
        ) as resp:
            return resp.status == 200
    except Exception:
        return False


requires_ollama = pytest.mark.skipif(
    not _ollama_up(), reason="Ollama server not reachable"
)


@pytest.fixture(scope="module")
def agent():
    from onboarding_assistant.agent import build_agent

    return build_agent()


def _ask(agent, question: str) -> str:
    from langchain_core.messages import HumanMessage

    result = agent.invoke({"messages": [HumanMessage(content=question)]})
    return result["messages"][-1].content


def _tool_calls(agent, question: str) -> list[str]:
    """Return the names of tools the agent invoked for a question."""
    from langchain_core.messages import AIMessage, HumanMessage

    result = agent.invoke({"messages": [HumanMessage(content=question)]})
    names = []
    for m in result["messages"]:
        if isinstance(m, AIMessage):
            for tc in getattr(m, "tool_calls", []) or []:
                names.append(tc["name"])
    return names


@requires_ollama
def test_benefits_routes_to_day_one_and_cites(agent):
    calls = _tool_calls(agent, "Where do I find my benefits?")
    assert "answer_day_one_logistics" in calls
    answer = _ask(agent, "Where do I find my benefits?")
    assert "workday" in answer.lower()


@requires_ollama
def test_access_routes_to_access_tool(agent):
    calls = _tool_calls(agent, "How do I get access to Cursor?")
    assert "get_access_instructions" in calls
    answer = _ask(agent, "How do I get access to Cursor?")
    assert "cursor" in answer.lower()


@requires_ollama
def test_does_not_hallucinate_out_of_scope(agent):
    answer = _ask(agent, "What is the internal architecture of the IAM authz service?")
    # No confluence/slack tool yet -> should decline rather than fabricate details
    assert any(p in answer.lower() for p in ["don't have", "do not have", "iam-help", "team"])
