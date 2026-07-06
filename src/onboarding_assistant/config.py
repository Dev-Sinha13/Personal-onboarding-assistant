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
    # LLM: defaults to a local Ollama model (NAI Gateway unavailable this cycle)
    llm_provider: str = os.getenv("LLM_PROVIDER", "ollama")
    llm_model: str = os.getenv("LLM_MODEL", "llama3")
    ollama_base_url: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    anthropic_api_key: str = os.getenv("ANTHROPIC_API_KEY", "")

    # Slack: bot token + app token only (search.messages is prohibited)
    slack_bot_token: str = os.getenv("SLACK_BOT_TOKEN", "")
    slack_app_token: str = os.getenv("SLACK_APP_TOKEN", "")

    pilot_team_name: str = os.getenv("PILOT_TEAM_NAME", "")
    slack_help_channel_name: str = os.getenv("SLACK_HELP_CHANNEL_NAME", "")
    slack_help_channel_id: str = os.getenv("SLACK_HELP_CHANNEL_ID", "")

    confluence_base_url: str = os.getenv("CONFLUENCE_BASE_URL", "")
    confluence_space_keys: str = os.getenv("CONFLUENCE_SPACE_KEYS", "")
    confluence_api_token: str = os.getenv("CONFLUENCE_API_TOKEN", "")
    confluence_username: str = os.getenv("CONFLUENCE_USERNAME", "")

    @property
    def space_key_list(self) -> list[str]:
        return [s.strip() for s in self.confluence_space_keys.split(",") if s.strip()]

    def missing(self, keys: list[str]) -> list[str]:
        """Return the subset of attribute names that are empty."""
        return [k for k in keys if not getattr(self, k, "")]


settings = Settings()


if __name__ == "__main__":
    required_for_llm = {
        "openai": ["openai_api_key"],
        "anthropic": ["anthropic_api_key"],
        "ollama": [],  # local, no key needed
    }.get(settings.llm_provider, [])
    print(f"LLM provider : {settings.llm_provider} ({settings.llm_model})")
    if settings.llm_provider == "ollama":
        print(f"Ollama URL   : {settings.ollama_base_url}")
    print(f"Pilot team   : {settings.pilot_team_name or '(not set)'}")
    print(f"Help channel : {settings.slack_help_channel_name or '(not set)'}")
    print(f"Confluence   : {settings.space_key_list or '(not set)'}")
    print(f"Missing (LLM): {settings.missing(required_for_llm) or 'none'}")
    print(
        "Missing (Slack): "
        f"{settings.missing(['slack_bot_token', 'slack_app_token']) or 'none'}"
    )
