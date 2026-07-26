from pydantic import BaseModel

from .approval_action import ApprovalAction

class ApprovalContext(BaseModel):
    """
    Stores pending approval information.
    """

    required: bool = False

    approved: bool | None = None

    title: str | None = None

    message: str | None = None


    action: ApprovalAction


    payload: dict = {}



    