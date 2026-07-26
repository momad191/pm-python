from .approval_context import ApprovalContext
from ...schemas.project_context import ProjectContext
from .approval_actions import ApprovalActions
 


class ApprovalManager:

    def is_waiting(
        self,
        approval: ApprovalContext | None,
    ) -> bool:

        return (
            approval is not None
            and approval.required
            and approval.approved is None
        )

    def is_approved(
        self,
        approval: ApprovalContext | None,
    ) -> bool:

        return (
            approval is not None
            and approval.approved is True
        )

    def is_rejected(
        self,
        approval: ApprovalContext | None,
    ) -> bool:

        return (
            approval is not None
            and approval.approved is False
        )


    def request_delete_project(
        self,
        project: ProjectContext,
    ) -> ApprovalContext:

        return ApprovalActions.request_delete_project(
            project
        )


approval_manager = ApprovalManager()