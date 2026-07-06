"""CLI harness for testing the agent in the terminal (Phases 1-3).

Usage:
  python -m onboarding_assistant.cli                 # interactive REPL
  python -m onboarding_assistant.cli "your question" # single-shot
"""

from __future__ import annotations

import sys

from langchain_core.messages import HumanMessage

from .agent import build_agent
from .config import settings


def _answer(agent, question: str) -> str:
    result = agent.invoke({"messages": [HumanMessage(content=question)]})
    return result["messages"][-1].content


def main() -> None:
    agent = build_agent()

    if len(sys.argv) > 1:
        print(_answer(agent, " ".join(sys.argv[1:])))
        return

    print(
        f"Onboarding Coach — {settings.pilot_team_name or 'pilot team'} "
        f"(LLM: {settings.llm_provider}/{settings.llm_model}). Ctrl-C to exit."
    )
    while True:
        try:
            question = input("\nyou > ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not question:
            continue
        try:
            print(f"\ncoach > {_answer(agent, question)}")
        except Exception as exc:  # keep the REPL alive on transient errors
            print(f"\n[error] {exc}")


if __name__ == "__main__":
    main()
