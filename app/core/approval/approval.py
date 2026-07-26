from .approval_context import ApprovalContext

from .approval_action import ApprovalAction

def create_approval(
    *,
    action: ApprovalAction,
    title: str,
    message: str,
    payload: dict,
) -> ApprovalContext:

    return ApprovalContext(
        required=True,
        approved=None,
        action=action,
        title=title,
        message=message,
        payload=payload,
    )