# from typing import Any

from ..base.base_agent import BaseAgent

from ...schemas.manager import ManagerDecision 

from ...schemas.state import AgentState

from .prompt import MANAGER_SYSTEM_PROMPT

 
class ManagerAgent(BaseAgent):
    """
    Supervisor Agent.

    Responsible for analyzing the user's request
    and routing it to the appropriate specialized
    agent.
    """

    def __init__(self):

        super().__init__("ManagerAgent")

  


    def run(
        self,
        state: AgentState,
    ) -> dict[str, object]:

        self.log_start()

        question = self.get_question(state)

        self.logger.info(
            "Question: %s",
            question,
        )

        if not question:

            self.logger.warning(
                "Received empty question."
            )

            return {

                "selected_agent": "general"

            }

        messages = self.build_messages(
            MANAGER_SYSTEM_PROMPT,
            question,
        )

        router_llm = self.get_structured_llm(
            state,
                ManagerDecision,
            )
        

        try:

            decision = router_llm.invoke(messages)

 

        except Exception as ex:

            self.handle_error(ex)

            return {

                "selected_agent": "general"

            }

        self.logger.info(

            "Manager Decision: %s",

            decision.model_dump(),

        )

        self.log_finish()

        return {

            "selected_agent": decision.agent,

            "context": self.update_context(

                state,

                "manager",

                {

                    "selected_agent": decision.agent,

                },

            ),

        }

    @staticmethod
    def route(
        state: AgentState,
    ) -> str:
        """
        Returns the next graph node
        selected by the manager.
        """

        return state.get(
            "selected_agent",
            "general",
        )


manager_agent = ManagerAgent()