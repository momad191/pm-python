from abc import ABC, abstractmethod

from ....core.base_component import BaseComponent
from ....schemas.state import AgentState
from ....services.nestjs_client import nestjs_client

 
class BaseAction(
    BaseComponent,
    ABC,
):

    def __init__(
        self,
        name: str,
    ):

        super().__init__(name)

        self.client = nestjs_client

    @abstractmethod
    def execute(
        self,
        state: AgentState,
    ) -> dict:
        ...