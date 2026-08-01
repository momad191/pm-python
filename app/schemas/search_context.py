from typing import Optional

from pydantic import BaseModel, Field

from .date_search import DateSearch


class SearchContext(BaseModel):
    """
    Structured search intent extracted from the LLM.

    This model represents WHAT the user wants to search,
    not HOW the backend API expects it.
    """

    # Free-text search
    text: Optional[str] = None

    # Entity filters
    project_id: Optional[str] = None

    month: Optional[str] = None

    year: Optional[str] = None

    manager_id: Optional[str] = None

    department: Optional[str] = None

    status: Optional[str] = None

    # Completion filters
    completion_min: Optional[int] = None

    completion_max: Optional[int] = None

    # Date semantics
    date: Optional[DateSearch] = None

    # Additional extracted entities
    entities: list[str] = Field(default_factory=list)