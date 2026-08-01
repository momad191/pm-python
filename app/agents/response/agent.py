from typing import Any

from ..base.base_agent import BaseAgent

from ...schemas.state import AgentState

from .prompt import RESPONSE_SYSTEM_PROMPT

from .formatter import ResponseFormatter


class ResponseAgent(BaseAgent):

    """
    Generates the final conversational answer.

    It never executes business logic.

    It only explains what already happened.
    """

    def __init__(self):

        super().__init__("ResponseAgent")

    def run(
        self,
        state: AgentState,
    ) -> dict[str, Any]:

        self.log_start()

        payload = ResponseFormatter.build_context(
            state
        )

        messages = self.build_messages(

            RESPONSE_SYSTEM_PROMPT,

            payload,

        )

        try:

            response = self.invoke(messages)

        except Exception as ex:

            self.handle_error(ex)

            return {

                "answer": state.get(
                    "answer",
                    "Unable to generate response.",
                )

            }

        self.log_finish()

        return {

            "answer": response.content

        }


response_agent = ResponseAgent() 