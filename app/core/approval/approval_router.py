from langgraph.graph import END

from .approval_action import ApprovalAction
from .approval_registry import get_route


def approval_router(
    state,
) -> str:
    """
    Routes execution according to the
    current approval status.

    Returns:

    - wait
    - cancel
    - delete_project
    - delete_user
    - ...
    """

    approval = (
        state.get("context", {})
        .get("approval")
    )

    if approval is None:

        return END

    approved = approval.get(
        "approved",
    )

    #
    # Waiting for user decision
    #
    if approved is None:

        return "wait"

    #
    # User rejected
    #
    if approved is False:

        return "cancel"

    #
    # User approved
    #
    action = ApprovalAction(
        approval["action"],
    )

    return get_route(
        action,
    )