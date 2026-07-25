from pydantic import BaseModel, Field

from ..constants.project import ProjectAction


class ProjectContext(BaseModel):
    """
    Shared Project domain context.

    This model is produced by ProjectAgent and
    consumed by Project actions and services.
    """

    action: ProjectAction

    # MongoDB _id
    id: str | None = Field(
        default=None,
        description="MongoDB project identifier."
    )

    # Business project identifier (PRO-001)
    project_code: str | None = Field(
        default=None,
        description="Business project identifier."
    )

    name: str | None = Field(
        default=None,
        description="Project name."
    )

    description: str | None = Field(
        default=None,
        description="Project description."
    )

    manager_id: str | None = Field(
        default=None,
        description="Assigned manager ID."
    )

    department: str | None = Field(
        default=None,
        description="Department responsible for the project."
    )

    status: str | None = Field(
        default=None,
        description="Project status."
    )

    start_date: str | None = Field(
        default=None,
        description="Project start date."
    )

    end_date: str | None = Field(
        default=None,
        description="Project end date."
    )

    completion_percentage: int = Field(
        default=0,
        ge=0,
        le=100,
        description="Completion percentage."
    )

    keywords: list[str] = Field(
        default_factory=list,
        description="Useful search keywords."
    )

    confidence: float = Field(
        default=1.0,
        ge=0,
        le=1,
        description="LLM confidence."
    )