from typing import Any

from pydantic import BaseModel, Field


class SuggestedAction(BaseModel):
    """
    Quick action that the frontend can render as
    a button or menu item.
    """

    label: str
    action: str
    payload: dict[str, Any] = Field(default_factory=dict)


class EntityReference(BaseModel):
    """
    Lightweight reference to an entity involved
    in the response.
    """

    type: str
    id: str
    title: str


class ResponseDecision(BaseModel):
    """
    Final conversational response returned by
    the ResponseAgent.
    """

    # Overall status
    success: bool = True

    operation: str

    # Short heading
    title: str

    # Natural language answer shown in chat
    answer: str

    # Optional concise summary
    summary: str | None = None


    total: int | None = None


     

    # Structured references
    entities: list[EntityReference] = Field(
        default_factory=list
    )

     
    # Important bullet points
    highlights: list[str] = Field(
        default_factory=list
    )

     

    # Suggested follow-up actions
    suggested_actions: list[
        SuggestedAction
    ] = Field(default_factory=list)

    # Optional metadata
    metadata: dict[str, Any] = Field(
        default_factory=dict
    )
    
    # LLM confidence
    confidence: float = 1.0