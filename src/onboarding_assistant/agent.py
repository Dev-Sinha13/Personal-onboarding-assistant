"""LangGraph agentic loop.

Builds a StateGraph with two nodes:
  - "agent": the LLM (bound to the tools) which decides what to do
  - "tools": executes any tool calls the LLM requested
Conditional edges loop LLM -> tools -> LLM until the LLM returns a final answer.
"""

from __future__ import annotations

from langchain_core.messages import SystemMessage
from langgraph.graph import END, START, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition

from .config import settings
from .llm import build_llm
from .tools import ALL_TOOLS


def system_prompt() -> str:
    team = settings.pilot_team_name or "the pilot team"
    return (
        f"You are the Onboarding Coach for {team} at Nutanix. "
        "You help new hires (interns and full-time) get productive fast.\n\n"
        "STRICT RULES:\n"
        "1. You MUST call a tool to answer any onboarding question. Never answer "
        "from your own prior knowledge.\n"
        "2. Ground every statement ONLY in what the tools return. Do NOT add facts, "
        "URLs, product names, or commands that a tool did not return. If the tools "
        "return nothing relevant, say you don't have that information and suggest "
        "who/where to ask.\n"
        "3. ALWAYS cite sources: copy the tool's 'Source:' line(s) verbatim into "
        "your answer.\n"
        "4. Only mention an @X-Bot command or link if a tool explicitly returned it.\n"
        "5. Be concise and practical — short, skimmable answers."
    )


def build_agent():
    """Compile and return the LangGraph agent."""
    llm_with_tools = build_llm().bind_tools(ALL_TOOLS)

    def call_model(state: MessagesState) -> dict:
        messages = [SystemMessage(content=system_prompt()), *state["messages"]]
        return {"messages": [llm_with_tools.invoke(messages)]}

    builder = StateGraph(MessagesState)
    builder.add_node("agent", call_model)
    builder.add_node("tools", ToolNode(ALL_TOOLS))

    builder.add_edge(START, "agent")
    builder.add_conditional_edges("agent", tools_condition)
    builder.add_edge("tools", "agent")

    return builder.compile()
