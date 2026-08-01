from pydantic import BaseModel, Field
from typing import Literal
from datetime import date

class ProjectSearchCriteria(BaseModel):
    project_id: str | None = None
    name: str | None = None
    description: str | None = None
    manager_id: str | None = None
    department: str | None = None
    status: str | None = None

    # Date semantics
    date_field: Literal[
        "startDate",
        "endDate",
        "createdAt",
        "updatedAt",
    ] | None = None

    month: int | None = None
    year: int | None = None

    start_date: date | None = None
    end_date: date | None = None

    search_text: str | None = None