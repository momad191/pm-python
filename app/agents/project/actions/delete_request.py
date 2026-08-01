import datetime
from typing import Any

from .base_action import BaseAction

 
from ....schemas.state import AgentState

from ....services.project_service import (
    ProjectService,
    project_service,
)


from ....core.approval.approval_manager import (
    ApprovalManager,
    # approval_manager,
)
 

from ....core.approval.approval_actions import ApprovalActions

class DeleteProjectRequestAction(BaseAction):
    """
    Workflow responsible for requesting
    user approval before deleting
    a project.

    Responsibilities

    - Read ProjectContext
    - Create ApprovalContext
    - Pause workflow
    - Wait for user approval
    """

    def __init__(
        self,
        service: ProjectService = project_service,
        # approvals: ApprovalManager = approval_manager,
    ):

        super().__init__("DeleteProjectRequestAction")

        self.service = service
        # self.approvals = approvals

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
                "Creating delete approval for project '%s'.",
                project.name,
            )

            # entity: ProjectResponse = self.service.delete(
            #     project,
            # )


            # approval = self.approvals.request_delete_project(
            #     project
            # )
           
 
            self.logger.info(
                "Workflow paused until user approves deletion."
            )



            updated_context = self.update_context(
                state,
                "project",
                project.model_dump(),
            )

            # updated_context = self.update_context(
            #     {
            #         **state,
            #         "context": updated_context,
            #     },
            #     "approval",
            #     approval.model_dump(),
            # )



            return self.update_state(

                current_action="project.delete.pending_approval",

                # approval_required=True,

                # approval=approval.model_dump(),

                response={

                    "domain": "project",

                    "operation": "delete_request",

                    "success": True,

                    "execution": {

                        "service": "ApprovalManager.request_delete_project",

                        "entity": "project",

                        "count": 1,

                    },

                    "api_result": {

                        "approval_created": True,

                        "approval_required": True,

                        "workflow_status": "waiting_for_approval",

                    },

                    "result_count": 1,

                    "input": project.model_dump(exclude_none=True),

                    # "result": approval.model_dump(),

                    # "approval": approval.model_dump(),

                    "timestamp": datetime.utcnow().isoformat(),

                },

                context=updated_context,

            )


 
        except Exception as ex:

            return self.handle_error(ex)

        finally:

            self.log_finish()


delete_project_request_action = DeleteProjectRequestAction()
