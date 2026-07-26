from typing import Any

from .base_action import BaseAction

from ....schemas.project_context import ProjectContext

from ....schemas.state import AgentState

from ....services.project_service import (
    ProjectService,
    project_service,
)

from ....schemas.responses.project_response import (
    ProjectResponse,
)

 
class UpdateProjectAction(BaseAction):
    """
    Workflow responsible for updating
    an existing project.

    Responsibilities

    - Read ProjectContext
    - Delegate business logic to ProjectService
    - Update LangGraph state
    """
 
    def __init__(
        self,
        service: ProjectService = project_service,
    ):

        super().__init__("UpdateProjectAction")

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

            project = self.get_project_context(
                state,
            )

            self.logger.info(
                "Validated ProjectContext = %s",
                project.model_dump(),
            )

            # identifier = (
            #     project.project_code
            #     or project.id
            # )

            # if not identifier:

            #     raise ValueError(
            #         "Project identifier is required."
            #     )

            self.logger.info(
                "Updating project..."
            )

            entity: ProjectResponse = self.service.update(
                project,
            )

            self.logger.info(
                "Project updated successfully."
            )

            return self.update_state(

                answer="Project updated successfully.",

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


update_project_action = UpdateProjectAction()