from langgraph.graph import END

from .approval_action import ApprovalAction


APPROVAL_ROUTES: dict[ApprovalAction, str] = {

    ApprovalAction.DELETE_PROJECT:
        "delete_project",

    ApprovalAction.DELETE_USER:
        "delete_user",

    ApprovalAction.DELETE_EMPLOYEE:
        "delete_employee",

    ApprovalAction.DELETE_COMPANY:
        "delete_company",

    ApprovalAction.ARCHIVE_PROJECT:
        "archive_project",

    ApprovalAction.SEND_EMAIL:
        "send_email",

}


def get_route(
    action: ApprovalAction,
) -> str:

    return APPROVAL_ROUTES.get(
        action,
        END,
    )