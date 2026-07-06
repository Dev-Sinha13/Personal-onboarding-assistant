"""Tests for the CLI harness (no real LLM — the agent is faked)."""

from __future__ import annotations

from types import SimpleNamespace

from langchain_core.messages import AIMessage

from onboarding_assistant import cli as cli_module


class _FakeAgent:
    def __init__(self):
        self.seen = []

    def invoke(self, state):
        self.seen.append(state["messages"][-1].content)
        return {"messages": [AIMessage(content="FAKE ANSWER")]}


def test_single_shot_prints_answer(monkeypatch, capsys):
    fake = _FakeAgent()
    monkeypatch.setattr(cli_module, "build_agent", lambda: fake)
    monkeypatch.setattr(cli_module.sys, "argv", ["cli", "where", "are", "benefits"])

    cli_module.main()

    out = capsys.readouterr().out
    assert "FAKE ANSWER" in out
    assert fake.seen == ["where are benefits"]


def test_interactive_loop_handles_input_and_eof(monkeypatch, capsys):
    fake = _FakeAgent()
    monkeypatch.setattr(cli_module, "build_agent", lambda: fake)
    monkeypatch.setattr(cli_module.sys, "argv", ["cli"])

    prompts = iter(["", "how do I get a UBVM", EOFError()])

    def fake_input(_prompt=""):
        item = next(prompts)
        if isinstance(item, BaseException):
            raise item
        return item

    monkeypatch.setattr("builtins.input", fake_input)
    monkeypatch.setattr(
        cli_module, "settings", SimpleNamespace(
            pilot_team_name="IAM", llm_provider="ollama", llm_model="qwen2.5:7b"
        )
    )

    cli_module.main()

    out = capsys.readouterr().out
    assert "FAKE ANSWER" in out           # answered the non-empty question
    assert fake.seen == ["how do I get a UBVM"]  # empty line was skipped


def test_repl_survives_agent_error(monkeypatch, capsys):
    class _BoomAgent:
        def invoke(self, state):
            raise RuntimeError("boom")

    monkeypatch.setattr(cli_module, "build_agent", lambda: _BoomAgent())
    monkeypatch.setattr(cli_module.sys, "argv", ["cli"])
    monkeypatch.setattr(
        cli_module, "settings", SimpleNamespace(
            pilot_team_name="IAM", llm_provider="ollama", llm_model="qwen2.5:7b"
        )
    )

    prompts = iter(["trigger error", EOFError()])

    def fake_input(_prompt=""):
        item = next(prompts)
        if isinstance(item, BaseException):
            raise item
        return item

    monkeypatch.setattr("builtins.input", fake_input)
    cli_module.main()

    out = capsys.readouterr().out
    assert "[error]" in out  # error was caught, loop continued to EOF
