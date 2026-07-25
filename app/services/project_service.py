from typing import Any

import requests

from ..core.base_service import BaseService 
 
from .nestjs_client import NestJSClient, nestjs_client

from ..schemas.project_context import ProjectContext

from ..schemas.responses.project_response import ProjectResponse

from .mappers.project_mapper import ProjectMapper
 

class ProjectService(BaseService):
    """
    Domain service responsible for Project
    business operations.

    Responsibilities:

    - Validate domain models
    - Map Domain -> API DTO
    - Call NestJS API
    - Handle HTTP errors
    """

    def __init__(
        self,
        client: NestJSClient = nestjs_client,
        mapper: ProjectMapper | None = None,
    ):

        super().__init__(

            name="ProjectService",

            client=client,

        )

        self.mapper = mapper or ProjectMapper()

    # -------------------------------------------------
    # Create
    # -------------------------------------------------

    def create(
        self,
        project: ProjectContext,
    ) -> ProjectResponse:

        self.validate(project)

        payload = self.mapper.to_create_payload(
            project,
        )


        self.logger.info(
            "Creating project '%s' (%s)",
            project.name,
            project.project_id,
            )

        try:

            response = self.execute(

            "Create Project",

            self.client.create_project,

            payload,

            )

            return ProjectResponse.model_validate(
                response
            )

        except requests.HTTPError:

            self.logger.exception(

                "NestJS rejected project creation."

            )

            raise

    # -------------------------------------------------
    # Update
    # -------------------------------------------------

    def update(
        self,
        project_id: str,
        project: ProjectContext,
    ) -> dict[str, Any]:

        self.validate(project)

        payload = self.mapper.to_update_payload(
            project,
        )

        return self.execute(

            "Update Project",

            self.client.update_project,

            project_id,

            payload,

        )

    # -------------------------------------------------
    # Delete
    # -------------------------------------------------

    def delete(
        self,
        project_id: str,
    ) -> dict[str, Any]:

        return self.execute(

            "Delete Project",

            self.client.delete_project,

            project_id,

        )

    # -------------------------------------------------
    # Details
    # -------------------------------------------------

    def details(
        self,
        project_id: str,
    ) -> dict[str, Any]:

        return self.execute(

            "Get Project",

            self.client.get_project,

            project_id,

        )

    # -------------------------------------------------
    # List
    # -------------------------------------------------

    def list(
        self,
        filters: dict[str, Any] | None = None,
    ) -> dict[str, Any]:

        return self.execute(

            "List Projects",

            self.client.list_projects,

            filters or {},

        )

    # -------------------------------------------------
    # Search
    # -------------------------------------------------

    def search(
        self,
        filters: dict[str, Any],
    ) -> dict[str, Any]:

        return self.execute(

            "Search Projects",

            self.client.search_projects,

            filters,

        )

    # -------------------------------------------------
    # Validation
    # -------------------------------------------------

    def validate(
    self,
    project: ProjectContext,
    ) -> None:
        """
        Business validation before calling
        the Project API.
        """

        if not project.project_code:
            raise ValueError(
                "Project code is required."
            )

        if not project.name:
            raise ValueError(
                "Project name is required."
            )

        if not project.manager_id:
            raise ValueError(
                "Manager ID is required."
            )

        if not project.department:
            raise ValueError(
                "Department is required."
            )

        if not project.start_date:
            raise ValueError(
                "Start date is required."
            )

        if not project.end_date:
            raise ValueError(
                "End date is required."
            )

 


project_service = ProjectService()