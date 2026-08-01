from pydantic import BaseModel

from .project_response import ProjectResponse


class ProjectSearchResponse(BaseModel):

    data: list[ProjectResponse]

    total: int

    page: int

    limit: int

    totalPages: int