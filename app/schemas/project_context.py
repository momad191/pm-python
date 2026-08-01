from pydantic import BaseModel

from ..constants.project import ProjectAction

from .extracted_entity import ExtractedEntity

from .project_search_criteria import ProjectSearchCriteria

 
class ProjectContext(BaseModel):

    action: ProjectAction

    id: str | None = None

    project_id: str | None = None

    name: str | None = None

    month: str | None = None

    year: str | None = None
    
    description: str | None = None

    manager_id: str | None = None

    department: str | None = None

    status: str  | None = None

    start_date: str | None = None

    end_date: str | None = None

    completion_percentage: int | None = None

    is_deleted: bool | None = None

    # keywords: list[str] = []
    entities: list[ExtractedEntity] = [] 
    
    search: ProjectSearchCriteria | None = None

    confidence: float = 1.0