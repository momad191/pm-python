from pydantic import BaseModel, Field


class ResponseDecision(BaseModel):
    """
    Final response generated for the user.
    """

    answer: str = Field(
        description="Natural conversational answer."
    )

    suggested_next_action: str | None = Field(
        default=None,
        description="Optional recommendation."
    )