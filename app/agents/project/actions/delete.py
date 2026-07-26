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


 
from ....core.approval.approval_actions import ApprovalActions

class DeleteProjectExecuteAction(BaseAction):
    """
    Workflow responsible for deleting
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

        super().__init__("DeleteProjectExecuteAction")

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
                "Deleting project..."
            )

            entity: ProjectResponse = self.service.delete(
                project,
            )

 
 
            self.logger.info(
                "Project deleted successfully."
            )



            context = self.update_context(

                state,

                "project",

                {

                    **project.model_dump(),

                    "entity": entity.model_dump(),

                    "deleted": True,

                },

            )

            context = self.remove_context(

                {

                    **state,

                    "context": context,

                },

                "approval",

            )

            return self.update_state(

                answer="Project deleted successfully.",

                current_action="completed",

                entity=entity.model_dump(),

                context=context,

            )
        

        except Exception as ex:

            return self.handle_error(ex)

        finally:

            self.log_finish()


delete_project_action  = DeleteProjectExecuteAction()