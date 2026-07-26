from typing import Any

from .base_action import BaseAction

from ....schemas.project_context import ProjectContext
from ....schemas.state import AgentState

from ....services.project_service import (
    ProjectService,
    project_service,
)

from ....schemas.responses.project_response import ProjectResponse

class DetailsProjectAction(BaseAction):
    """
    Workflow responsible for retrieving
    a single project.

    Responsibilities:

    - Read ProjectContext
    - Delegate retrieval to ProjectService
    - Update LangGraph state
    """

    def __init__(
        self,
        service: ProjectService = project_service,
    ):

        super().__init__("DetailsProjectAction")

        self.service = service

    def execute(
        self,
        state: AgentState,
    ) -> dict[str, Any]:

        self.log_start()

        try:

            self.logger.info(
                "Incoming Context = %s",
                state.get("context"),
            )

            # 1- Read ProjectContext

            project = self.get_project_context(
                state,
            )
 
 
            self.logger.info(
                "Validated ProjectContext = %s",
                project.model_dump(),
            )



            self.logger.info("Retrieving project details.")


            # 2- Delegate retrieval to ProjectService.details()
            # Delegate retrieval to ProjectService

            entity: ProjectResponse = self.service.details(
                project,
            )


            

            # 3- Store the retrieved entity in the shared context
            # 4- Return an updated LangGraph state
            return self.update_state(

                answer="Project retrieved successfully.",

                current_action="completed",

                entity=entity.model_dump(),

                context=self.update_context(

                    state,

                    "project",

                    {

                        **project.model_dump(),

                        "entity": entity.model_dump(),

                    },

                ),

            )

        except Exception as ex:

            return self.handle_error(ex)

        finally:

            self.log_finish()


details_project_action = DetailsProjectAction()