from datetime import datetime

from pydantic import BaseModel, Field


class ProjectResponse(BaseModel):

    id: str = Field(alias="_id")

    project_id: str = Field(alias="projectId")

    name: str

    description: str

    manager_id: str = Field(alias="managerId")

    department: str

    status: str

    start_date: datetime = Field(alias="startDate")

    end_date: datetime = Field(alias="endDate")

    completion_percentage: int = Field(
        alias="completionPercentage"
    )

    is_deleted: bool = Field(alias="isDeleted")

    created_at: datetime = Field(alias="createdAt")

    updated_at: datetime = Field(alias="updatedAt")

    model_config = {
        "populate_by_name": True
    }