from .prompt import MANAGER_SYSTEM_PROMPT
from langchain_core.messages import (
    HumanMessage,
    SystemMessage,
)
from ...schemas.state import AgentState
from ...services.llm import llm

import logging

logger = logging.getLogger(__name__)


from ...schemas.manager import ManagerDecision

structured_llm = llm.with_structured_output(
    ManagerDecision
)


def manager_agent(state: AgentState) -> dict:

    """
    Supervisor node.

    Determines which specialized agent should
    process the user's request.
    """
        

    logger.info("Manager Agent")

    question = str(state.get("question", "")).strip()

    logger.info("Question: %s", question)

    if not question:
        return {
        "selected_agent": "general"
        }


    messages = [

        SystemMessage(
            content=MANAGER_SYSTEM_PROMPT
        ),

        HumanMessage(
            content=question
        )

    ]

    try:

        decision = structured_llm.invoke(messages)

    except Exception as ex:

        logger.exception(ex)

        return {

            "selected_agent": "general"
        }


    # logger.info("Selected Agent: %s", decision.agent)
    logger.info(
    "Manager Decision: %s",
    decision.model_dump(),
    )

    return {

    "context": {

        "manager": {

            "selected_agent": decision.agent

            }

        }

    }


def route_agent(state: AgentState) -> str:
    """
    Returns the next graph node based on the
    manager's routing decision.
    """

    return state.get(
        "selected_agent",
        "general",
    )