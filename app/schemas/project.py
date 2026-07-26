from typing import Optional

from pydantic import BaseModel, Field

from ..constants.project import ProjectAction


class ProjectDecision(BaseModel):

    action: ProjectAction

    project_id: Optional[str] = Field(
        default=None,
        description="Project ID such as PRO-001"
    )

    name: Optional[str] = None

    description: Optional[str] = None

    manager_id: Optional[str] = None

    department: Optional[str] = None

    status: Optional[str] = "ACTIVE"

    start_date: Optional[str] = None

    end_date: Optional[str] = None

    completion_percentage: int = 0

    is_deleted: bool = False

    keywords: list[str] = Field(default_factory=list)

    confidence: float = 1.0