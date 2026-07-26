from pydantic import BaseModel

from ..constants.project import ProjectAction


class ProjectContext(BaseModel):

    action: ProjectAction

    project_id: str | None = None

    name: str | None = None

    description: str | None = None

    manager_id: str | None = None

    department: str | None = None

    status: str = "ACTIVE"

    start_date: str | None = None

    end_date: str | None = None

    completion_percentage: int = 0

    is_deleted: bool = False

    keywords: list[str] = []

    confidence: float = 1.0