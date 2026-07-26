from datetime import datetime

from pydantic import BaseModel, Field


 

class ProjectResponse(BaseModel):

    id: str | None = None

    projectId: str

    name: str

    description: str | None = None

    managerId: str

    department: str

    status: str

    startDate: str | None = None

    endDate: str | None = None

    completionPercentage: int

    isDeleted: bool

    createdAt: str | None = None

    updatedAt: str | None = None