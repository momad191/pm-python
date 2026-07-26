from ...schemas.state import AgentState

from .approval_context import ApprovalContext


def approval_node(
    state: AgentState,
):
    """
    Human-in-the-Loop node.

    Execution pauses here until the
    user approves or rejects the action.
    """

    approval = ApprovalContext.model_validate(

        state["context"]["approval"]

    )

    return {

        "answer": approval.message,

        "current_action": "waiting_for_approval",

        "approval_required": True,

        "approval": approval.model_dump(),

        "approval_action": approval.action.value,

    }