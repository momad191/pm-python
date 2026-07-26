from ...schemas.project_context import ProjectContext


class ProjectMapper:
    """
    Maps ProjectContext to the DTOs expected
    by the NestJS Project API.
    """

    # -------------------------------------------------
    # Create
    # -------------------------------------------------

    def to_create_payload(
        self,
        project: ProjectContext,
    ) -> dict:

        return {

            "projectId": project.project_id,

            "name": project.name,

            "description": project.description,

            "managerId": project.manager_id,

            "department": project.department,

            "status": project.status,

            "startDate": project.start_date,

            "endDate": project.end_date,

            "completionPercentage": project.completion_percentage,

            "isDeleted": project.is_deleted,

        }

    # -------------------------------------------------
    # Update
    # -------------------------------------------------

    def to_update_payload(
        self,
        project: ProjectContext,
    ) -> dict:

        return self.to_create_payload(project)

    # -------------------------------------------------
    # List
    # -------------------------------------------------

    def to_list_filters(
        self,
        project: ProjectContext,
    ) -> dict:
        """
        Converts ProjectContext into filters used
        for listing projects.
        """

        return self._build_filters(project)

    # -------------------------------------------------
    # Search
    # -------------------------------------------------

    def to_search_filters(
        self,
        project: ProjectContext,
    ) -> dict:
        """
        Converts ProjectContext into filters used
        for searching projects.
        """

        filters = self._build_filters(project)

        if project.project_id:
            filters["projectId"] = project.project_id

        if project.name:
            filters["name"] = project.name

        if project.keywords:
            filters["search"] = " ".join(
                project.keywords
            )

        return filters

    # -------------------------------------------------
    # Shared Filter Builder
    # -------------------------------------------------

    def _build_filters(
        self,
        project: ProjectContext,
    ) -> dict:
        """
        Builds common filter fields shared by
        list() and search().
        """
 
        filters: dict = {}

        if project.manager_id:
            filters["managerId"] = project.manager_id

        if project.department:
            filters["department"] = project.department

        if project.status:
            filters["status"] = project.status

        if project.start_date:
            filters["startDate"] = project.start_date

        if project.end_date:
            filters["endDate"] = project.end_date

        if project.is_deleted is not None:
            filters["isDeleted"] = project.is_deleted

        return filters



    # eleminate duplication

    # def to_search_payload(
    # self,
    # project: ProjectContext,
    # ) -> dict:
    #     """
    #     Convert ProjectContext into search filters.
    #     Only non-empty values are sent.
    #     """

    #     payload = {

    #         "projectId": project.project_id,

    #         "name": project.name,

    #         "description": project.description,

    #         "managerId": project.manager_id,

    #         "department": project.department,

    #         "status": project.status,

    #         "startDate": project.start_date,

    #         "endDate": project.end_date,

    #         "completionPercentage": project.completion_percentage,

    #         "isDeleted": project.is_deleted,

    #     }

    #     return {

    #         key: value

    #         for key, value in payload.items()

    #         if value is not None

    #     }


    def to_filter_payload(
        self,
        project: ProjectContext,
    ) -> dict:
        ...
    


    def to_list_payload(
    self,
    project: ProjectContext,
    ) -> dict:
        return self.to_filter_payload(project)

    

    def to_search_payload(
        self,
        project: ProjectContext,
    ) -> dict:
        return self.to_filter_payload(project)




    def to_identifier(
        self,
        project: ProjectContext,
    ) -> str:

        identifier = (
            project.project_code
            or project.id
        )

        if not identifier:

            raise ValueError(
                "Project identifier is required."
            )

        return identifier