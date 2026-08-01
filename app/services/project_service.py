from typing import Any, List

import requests 

from ..core.base_service import BaseService 
 
from .nestjs_client import NestJSClient, nestjs_client

from ..schemas.project_context import ProjectContext
 
from ..schemas.responses.project_response import ProjectResponse

from .mappers.project_mapper import ProjectMapper

from ..schemas.responses.project_search_response import (
    ProjectSearchResponse,
)

 
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
        project: ProjectContext,
    ) -> ProjectResponse:

        self.validateUpdate(project)

        payload = self.mapper.to_update_payload(
            project,
        )


        identifier = self.mapper.to_identifier(project)

        self.logger.info(
            "Updating project '%s'",
            identifier,
        )

        response = self.execute(

            "Update Project",

            self.client.update_project,

            identifier,

            payload,

        )

        return ProjectResponse.model_validate(
            response,
        )

    # -------------------------------------------------
    # Delete
    # -------------------------------------------------

    def delete(
        self,
        project: ProjectContext,
    ) -> ProjectResponse:

        identifier = self.mapper.to_identifier(
            project,
        )

        self.logger.info(
            "Deleting project '%s'",
            identifier,
        )

        response = self.execute(

            "Delete Project",

            self.client.delete_project,

            identifier,

        )

        return ProjectResponse.model_validate(
            response,
        )

    # -------------------------------------------------
    # Details
    # -------------------------------------------------

    def details(
        self,
        project: ProjectContext,
    ) -> ProjectResponse:

        identifier = self.mapper.to_identifier(project)

        response = self.execute(

            "Get Project",

            self.client.get_project,

            identifier,

        )

        return ProjectResponse.model_validate(response)


 
    # -------------------------------------------------
    # List
    # -------------------------------------------------
   
    def list(
        self,
        project: ProjectContext,
    ) -> List[ProjectResponse]:

        filters = self.mapper.to_list_filters(project)
 
        response = self.execute(

            "List Projects",

            self.client.list_projects,

            filters,

        )

        return [

            ProjectResponse.model_validate(item)

            for item in response

        ]

    # -------------------------------------------------
    # Search
    # -------------------------------------------------

    def search(
        self,
        context: ProjectContext,
    ) -> ProjectSearchResponse:

        payload = self.mapper.to_search_payload(context) or {}      

        # Remove empty values
        payload = {
            key: value
            for key, value in payload.items()
            if value is not None
            and value != ""
            and value != []
        }
 
        self.logger.info(
            "Search Payload = %s",
            payload,
        )

        response = self.execute(
            "Search Projects",
            self.client.search_projects, 
            payload,
        )

        return ProjectSearchResponse.model_validate(response)




    # -------------------------------------------------
    # Search
    # -------------------------------------------------

    def filterDate(
        self,
        context: ProjectContext,
    ) -> ProjectSearchResponse:

        payload = self.mapper.to_filter_date_payload(context) or {}     

        # Remove empty values
        payload = {
            key: value
            for key, value in payload.items()
            if value is not None
            and value != ""
            and value != []
        }
 
        self.logger.info(
            "Search Payload = %s",
            payload,
        )

        response = self.execute(
            "Search Projects",
            self.client.search_projects, 
            payload,
        )

        return ProjectSearchResponse.model_validate(response)

    # -------------------------------------------------
    # Validation
    # -------------------------------------------------

 
    def validate(
        self,
        project: ProjectContext,
        ) -> None:

        self.logger.info(
            "Validating ProjectContext = %s",
            project.model_dump(by_alias=True),
        )

        # if not project.project_id:

        #     raise ValueError(
        #         "Project ID is required."
        #     )

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


        if not project.status:

            raise ValueError(
                "Status is required."
            )




    def validateUpdate(
        self,
        project: ProjectContext,
        ) -> None:

        self.logger.info(
            "Validating ProjectContext = %s",
            project.model_dump(by_alias=True),
        )

        if not project.project_id:

            raise ValueError(
                "Project ID is required."
            )


project_service = ProjectService()