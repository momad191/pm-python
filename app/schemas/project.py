from pydantic import BaseModel, Field

from ..constants.project import ProjectAction


class ProjectDecision(BaseModel):
    """
    Structured understanding produced by the
    ProjectAgent.
    """

    action: ProjectAction

    project_id: str | None = None

    name: str | None = None

    description: str | None = None

    manager_id: str | None = None

    department: str | None = None

    status: str | None = None

    start_date: str | None = None

    end_date: str | None = None

    completion_percentage: int | None = None

    keywords: list[str] = Field(default_factory=list)

    confidence: float = Field(
        default=1.0,
        ge=0,
        le=1,
    )