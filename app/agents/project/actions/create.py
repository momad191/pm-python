from typing import Any

from .base_action import BaseAction 

from ....schemas.project_context import ProjectContext  

from ....schemas.state import AgentState

from ....services.project_service import ProjectService

from ....services.project_service import project_service
 
  
class CreateProjectAction(BaseAction):
    """
    Workflow responsible for creating
    a new project.

    Responsibilities:

    - Read ProjectContext
    - Delegate business logic to ProjectService
    - Update LangGraph state
    """

    def __init__(
        self,
        service: ProjectService = project_service,
    ):

        super().__init__("CreateProjectAction")

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
            

            self.logger.info(
                "Creating project '%s'",
                project.name,
            )

            #
            # ProjectService is now responsible for
            # converting ProjectContext into the
            # NestJS payload.
            #
            created_project = self.service.create(
                project
            )


            self.logger.info(
                "Project Context: %s",
                state.get("context", {}).get("project"),
            )

            return self.update_state(
                answer="Project created successfully.",
                current_action="completed",
                context=self.update_context(
                    state,
                    "project",
                    {
                        **project.model_dump(),
                        "entity": created_project.model_dump(),
                    },
                ),
            )

        except Exception as ex:

            return self.handle_error(ex)

        finally:

            self.log_finish()


create_project_action = CreateProjectAction()