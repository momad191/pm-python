from abc import ABC
from typing import Type

from pydantic import BaseModel

from ...core.base_component import BaseComponent
from ...services.llm import llm


from langchain_core.messages import (
    BaseMessage,
    HumanMessage,
    SystemMessage,
)


class BaseAgent(
    BaseComponent,
    ABC,
):

    def __init__(
        self,
        name: str,
    ):

        super().__init__(name)

        self.llm = llm

    def get_structured_llm(
        self,
        schema: Type[BaseModel],
    ):

        return self.llm.with_structured_output(
            schema
        )

    def build_messages(
        self,
        system_prompt: str,
        question: str,
    ) -> list[BaseMessage]:

        return [

            SystemMessage(
                content=system_prompt,
            ),

            HumanMessage(
                content=question,
            ),

        ]

 


    def invoke(
        self,
        messages: list[BaseMessage],
    ):

        return self.llm.invoke(messages)