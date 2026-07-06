"""Central configuration: loads environment variables from `.env`.

This is scaffolding for Phase 0 — it just surfaces settings and flags missing
ones. Agent/tool logic lives in later phases.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"

load_dotenv(PROJECT_ROOT / ".env")


@dataclass(frozen=True)
class Settings:
    llm_provider: str = os.getenv("LLM_PROVIDER", "openai")
    llm_model: str = os.getenv("LLM_MODEL", "gpt-4o-mini")
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    anthropic_api_key: str = os.getenv("ANTHROPIC_API_KEY", "")

    slack_bot_token: str = os.getenv("SLACK_BOT_TOKEN", "")
    slack_app_token: str = os.getenv("SLACK_APP_TOKEN", "")
    slack_user_token: str = os.getenv("SLACK_USER_TOKEN", "")

    pilot_team_name: str = os.getenv("PILOT_TEAM_NAME", "")
    slack_help_channel_id: str = os.getenv("SLACK_HELP_CHANNEL_ID", "")

    confluence_base_url: str = os.getenv("CONFLUENCE_BASE_URL", "")
    confluence_space_key: str = os.getenv("CONFLUENCE_SPACE_KEY", "")
    confluence_api_token: str = os.getenv("CONFLUENCE_API_TOKEN", "")
    confluence_username: str = os.getenv("CONFLUENCE_USERNAME", "")

    def missing(self, keys: list[str]) -> list[str]:
        """Return the subset of attribute names that are empty."""
        return [k for k in keys if not getattr(self, k, "")]


settings = Settings()


if __name__ == "__main__":
    required_for_llm = (
        ["openai_api_key"]
        if settings.llm_provider == "openai"
        else ["anthropic_api_key"]
    )
    print(f"LLM provider : {settings.llm_provider} ({settings.llm_model})")
    print(f"Pilot team   : {settings.pilot_team_name or '(not set)'}")
    print(f"Missing (LLM): {settings.missing(required_for_llm) or 'none'}")
    print(
        "Missing (Slack): "
        f"{settings.missing(['slack_bot_token', 'slack_app_token']) or 'none'}"
    )
