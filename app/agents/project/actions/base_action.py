from abc import ABC, abstractmethod

from ....core.base_component import BaseComponent
from ....schemas.state import AgentState
from ....schemas.project_context import ProjectContext
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

    
    def get_project_context(
        self,
        state: AgentState,
        ) -> ProjectContext:

        self.logger.info(
            "Incoming Context = %s",
            state.get("context"),
        )

        project = self.get_model_context(

            state,

            "project",

            ProjectContext,

        )

        self.logger.info(
            "Validated ProjectContext = %s",
            project.model_dump(),
        )

        return project

 
    def remove_context(
        self,
        state,
        key: str,
        ):
        context = dict(state.get("context", {}))

        context.pop(key, None)

        return context