from datetime import datetime

from pydantic import BaseModel, Field

class ProjectResponse(BaseModel):

    id: str | None = Field(
        default=None,
        alias="_id",
    )

    projectId: str  | None = None

    name: str  | None = None

    description: str | None = None

    managerId: str  | None = None

    department: str  | None = None

    status: str  | None = None

    startDate: str | None = None

    endDate: str | None = None

    completionPercentage: int  | None = None

    isDeleted: bool  | None = None

    createdAt: str | None = None

    updatedAt: str | None = None