from typing import Any

from .prompt import GENERAL_SYSTEM_PROMPT
 
from ..base.base_agent import BaseAgent

from ...schemas.state import AgentState

 
class GeneralAgent(BaseAgent):
    """
    Handles non-project questions.

    Examples

    - What is the capital of Sudan?
    - Explain Docker.
    - What is AI?
    - Write Python code.
    """

    def __init__(self):

        super().__init__("GeneralAgent")

    def run(
        self,
        state: AgentState,
    ) -> dict[str, Any]:

        self.log_start()

        question = state["question"]

        messages = self.build_messages(

            GENERAL_SYSTEM_PROMPT,

            question,

        )

        try:

            response = self.invoke(messages)

        except Exception as ex:

            self.handle_error(ex)

            return {

                "answer": "I couldn't answer that question.",

            }

        self.log_finish()

        return {

            "answer": response.content,

            "current_action": "general.completed",

        }


general_agent = GeneralAgent()