import logging

from langchain_core.messages import (
    HumanMessage,
    SystemMessage,
)

from ...schemas.manager import ManagerDecision
from ...schemas.state import AgentState
from ...services.llm import llm

from .prompt import MANAGER_SYSTEM_PROMPT

logger = logging.getLogger(__name__)


class ManagerAgent:
    """
    Supervisor Agent.

    Responsible for routing the user's request
    to the correct specialized agent.
    """

    def __init__(self):

        self.llm = llm.with_structured_output(
            ManagerDecision
        )

    def run(
        self,
        state: AgentState,
    ) -> dict:

        logger.info("Manager Agent")

        question = str(
            state.get("question", "")
        ).strip()

        logger.info(
            "Question: %s",
            question,
        )

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

            decision = self.llm.invoke(
                messages
            )

        except Exception:

            logger.exception(
                "Manager Agent Failed"
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