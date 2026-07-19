import logging
from typing import Any

from langchain_core.messages import (
    HumanMessage,
    SystemMessage,
)

from ...schemas.manager import ManagerDecision
from ...schemas.state import AgentState
from ...services.llm import llm

from .prompt import MANAGER_SYSTEM_PROMPT

logger = logging.getLogger("ManagerAgent")


class ManagerAgent:
    """
    Supervisor Agent.

    Responsible for routing the user's request
    to the correct specialized agent.
    """

    def __init__(self):

        self.llm = llm

        self.router_llm = self.llm.with_structured_output(
            ManagerDecision
        )

    def run(
    self,
    state: AgentState,
    ) -> dict[str, Any]:

        logger.info("Manager Agent")

        question = str(
            state.get("question", "")
        ).strip()

        logger.info(
            "Question: %s",
            question,
        )

        if not question:
             
            logger.warning(
                "Received empty question"
            )

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

            decision = self.router_llm.invoke(
                messages
            )

            summary  = self.llm.invoke(
                messages
            )

        except Exception as ex:

            logger.exception(
                "Manager Agent Failed: %s",
                ex,
            )

            return {

                "selected_agent": "general"

            }

        logger.info(

            "Manager Decision: %s",

            decision.model_dump()

        )

        return {

            "selected_agent": decision.agent,

            "context": {
                 
                "manager": {

                    "selected_agent": decision.agent

                }

            }

        }

    @staticmethod
    def route(
        state: AgentState,
    ) -> str:
        """
        Returns the next graph node.
        """

        return state.get(
            "selected_agent",
            "general",
        )
    

manager_agent = ManagerAgent()