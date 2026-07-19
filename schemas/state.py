from typing import Annotated

from typing_extensions import TypedDict

from langchain_core.messages import BaseMessage

from langgraph.graph.message import add_messages


class AgentState(TypedDict):
    """
    Shared state across all graphs and agents.
    """

    # Conversation Memory
    messages: Annotated[
        list[BaseMessage],
        add_messages,
    ]

    # Current user request
    question: str

    # Final response
    answer: str

    # Manager Agent
    selected_agent: str

    # Tool execution
    tool_name: str
    tool_result: str

    # Shared context
    context: dict