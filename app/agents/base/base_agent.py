from abc import ABC
from typing import Type

from pydantic import BaseModel

from langchain_openai import ChatOpenAI

from langchain_core.messages import (
    BaseMessage,
    HumanMessage,
    SystemMessage,
)

from ...core.base_component import BaseComponent
from ...schemas.state import AgentState
from ...config import settings


class BaseAgent(
    BaseComponent,
    ABC,
):

    def __init__(
        self,
        name: str,
    ):
        super().__init__(name)

    # -------------------------------------------------
    # LLM
    # -------------------------------------------------

    def get_llm(
        self,
        state: AgentState,
    ) -> ChatOpenAI:
        """
        Creates a ChatOpenAI instance using the API key
        supplied by the NestJS backend.
        """

        api_key = state.get("openai_api_key")

        if not api_key:
            raise ValueError(
                "OPENAI_API_KEY was not provided."
            )

        return ChatOpenAI(
            api_key=api_key,
            model=settings.OPENAI_MODEL,
            temperature=settings.OPENAI_TEMPERATURE,
        )

    def get_structured_llm(
        self,
        state: AgentState,
        schema: Type[BaseModel],
    ):
        """
        Returns an LLM configured for structured output.
        """

        return self.get_llm(state).with_structured_output(
            schema
        )

    # -------------------------------------------------
    # Messages
    # -------------------------------------------------

    def build_messages(
        self,
        system_prompt: str,
        question: str,
    ) -> list[BaseMessage]:

        return [
            SystemMessage(content=system_prompt),
            HumanMessage(content=question),
        ]

    # -------------------------------------------------
    # Invoke
    # -------------------------------------------------

    def invoke(
        self,
        state: AgentState,
        messages: list[BaseMessage],
    ):
        return self.get_llm(state).invoke(messages)