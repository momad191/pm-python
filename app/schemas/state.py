from typing import Annotated

from typing_extensions import NotRequired, TypedDict

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages


class AgentState(TypedDict):
    """
    Shared state passed between all LangGraph nodes.

    This state acts as the communication contract
    between the supervisor, domain agents, tools,
    and downstream services.
    """

    # -------------------------------------------------
    # Conversation
    # -------------------------------------------------

    messages: Annotated[
        list[BaseMessage],
        add_messages,
    ]

    question: str

    answer: NotRequired[str]

    # -------------------------------------------------
    # Supervisor Routing
    # -------------------------------------------------

    selected_agent: NotRequired[str]

    # -------------------------------------------------
    # Domain Routing
    # -------------------------------------------------

    project_action: NotRequired[str]

    task_action: NotRequired[str]

    issue_action: NotRequired[str]

    report_action: NotRequired[str]

    # -------------------------------------------------
    # Tool Execution
    # -------------------------------------------------

    tool_name: NotRequired[str]

    tool_result: NotRequired[str]

    # -------------------------------------------------
    # Shared Context
    # -------------------------------------------------

    context: NotRequired[dict]