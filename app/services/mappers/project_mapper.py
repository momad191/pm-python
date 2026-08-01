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

            "_id": project.id,
 
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

        payload = {}

        if project.name is not None:
            payload["name"] = project.name

        if project.description is not None:
            payload["description"] = project.description

        if project.manager_id is not None:
            payload["managerId"] = project.manager_id

        if project.department is not None:
            payload["department"] = project.department

        if project.status is not None:
            payload["status"] = project.status

        if project.start_date is not None:
            payload["startDate"] = project.start_date

        if project.end_date is not None:
            payload["endDate"] = project.end_date


        if project.month is not None:
                    payload["month"] = project.month


        if project.year is not None:
                    payload["year"] = project.year

        # Only include projectId if the user explicitly wants to change it.
        # Do NOT include it when it contains the Mongo _id.
        if (
            project.project_id is not None
            and project.project_id.startswith("PRO-")
        ):
            payload["projectId"] = project.project_id

        return payload

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

        return self._build_search_payload(project)

    # -------------------------------------------------
    # Search
    # -------------------------------------------------


    def to_search_filters(
        self,
        project: ProjectContext,
        ) -> dict:

        return self._build_search_payload(project)


    # def to_search_filters(
    #     self,
    #     project: ProjectContext,
    # ) -> dict:
    #     """
    #     Converts ProjectContext into filters used
    #     for searching projects.
    #     """

    #     filters = self._build_filters(project)

    #     if project.project_id:
    #         filters["projectId"] = project.project_id

    #     if project.name:
    #         filters["name"] = project.name

        # if project.keywords:
        #     filters["search"] = " ".join(
        #         project.keywords
        #     )
 
        # criteria = project.search

        # if criteria.start_date:

        #     filters["startDate"] = criteria.start_date

        # if criteria.department:

        #     filters["department"] = criteria.department

        # if criteria.search_text:

        #     filters["search"] = criteria.search_text

        # return filters

    # -------------------------------------------------
    # Shared Filter Builder
    # -------------------------------------------------

     
    def _build_search_payload(
    self,
    project: ProjectContext,
    ) -> dict:
        """
        Builds the payload used by both list and search APIs.

        Only populated fields are included.
        """

        payload: dict = {}

        # -----------------------------
        # Identifiers
        # -----------------------------

        if project.project_id:
            payload["projectId"] = project.project_id

        # -----------------------------
        # Basic fields
        # -----------------------------

        if project.name:
            payload["name"] = project.name

        if project.description:
            payload["description"] = project.description

        if project.manager_id:
            payload["managerId"] = project.manager_id

        if project.department:
            payload["department"] = project.department

        if project.status:
            payload["status"] = project.status


        # if project.month:
        #     payload["month"] = project.month

        # if project.year:
        #     payload["year"] = project.year

        # -----------------------------
        # Date filters
        # -----------------------------

        if project.start_date:
            payload["startDate"] = project.start_date

        if project.end_date:
            payload["endDate"] = project.end_date

        # -----------------------------
        # Progress
        # -----------------------------

        if project.completion_percentage is not None:
            payload["completionPercentage"] = (
                project.completion_percentage
            )

        if project.is_deleted is not None:
            payload["isDeleted"] = project.is_deleted

        # -----------------------------
        # Rich Search Context
        # -----------------------------

        if project.search:

            criteria = project.search

            if criteria.search_text:
                payload["search"] = criteria.search_text

            # Prefer explicit values from the search object
            if criteria.name:
                payload["name"] = criteria.name

            if criteria.description:
                payload["description"] = criteria.description

            if criteria.manager_id:
                payload["managerId"] = criteria.manager_id

            if criteria.department:
                payload["department"] = criteria.department

            if criteria.status:
                payload["status"] = criteria.status

            if criteria.start_date:
                payload["startDate"] = criteria.start_date

            if criteria.end_date:
                payload["endDate"] = criteria.end_date

            if criteria.project_id:
                payload["projectId"] = criteria.project_id

            if criteria.month:
                payload["month"] = criteria.month

            if criteria.year:
                payload["year"] = criteria.year

        return payload




    def to_filter_date_payload(
        self,
        project: ProjectContext,
        ) -> dict:
        """
        Converts ProjectContext into API filters.
        Only non-empty values are included.
        """

        payload: dict = {}

        if project.start_date:
            payload["startDate"] = project.start_date

        if project.end_date:
            payload["endDate"] = project.end_date

        return payload
 

    def to_search_payload(
        self,
        project: ProjectContext,
    ) -> dict:

        return self._build_search_payload(project)


    # def to_search_payload(
    #     self,
    #     project: ProjectContext,
    # ) -> dict:
    #     """
    #     Converts ProjectContext into API filters.
    #     Only non-empty values are included.
    #     """

    #     payload: dict = {}

    #     if project.project_id:
    #         payload["projectId"] = project.project_id

    #     # if project.name:
    #     #     payload["name"] = project.name

    #     # if project.description:
    #     #     payload["description"] = project.description 

    #     if project.manager_id:
    #         payload["managerId"] = project.manager_id

    #     if project.department:
    #         payload["department"] = project.department

    #     if project.status:
    #         payload["status"] = project.status

    #     if project.start_date:
    #         payload["startDate"] = project.start_date

    #     if project.end_date:
    #         payload["endDate"] = project.end_date

    #     if project.completion_percentage is not None:
    #         payload["completionPercentage"] = project.completion_percentage

    #     if project.is_deleted is not None:
    #         payload["isDeleted"] = project.is_deleted

    #     if project.keywords:
    #         payload["search"] = " ".join(project.keywords)

    #     return payload


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

    #         # "name": project.name,

    #         # "description": project.description,

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

        return self._build_search_payload(project)


    # def to_filter_payload(
    #     self,
    #     project: ProjectContext,
    # ) -> dict:
    #     """
    #     Converts ProjectContext into API filters.
    #     Only non-empty values are included.
    #     """

    #     payload: dict = {}

    #     if project.project_id:
    #         payload["projectId"] = project.project_id

    #     if project.name:
    #         payload["name"] = project.name

    #     if project.description:
    #         payload["description"] = project.description 

    #     if project.manager_id:
    #         payload["managerId"] = project.manager_id

    #     if project.department:
    #         payload["department"] = project.department

    #     if project.status:
    #         payload["status"] = project.status

    #     if project.start_date:
    #         payload["startDate"] = project.start_date

    #     if project.end_date:
    #         payload["endDate"] = project.end_date

    #     if project.completion_percentage is not None:
    #         payload["completionPercentage"] = project.completion_percentage

    #     if project.is_deleted is not None:
    #         payload["isDeleted"] = project.is_deleted

    #     if project.keywords:
    #         payload["search"] = " ".join(project.keywords)

    #     return payload
    


    def to_list_payload(
    self,
    project: ProjectContext,
    ) -> dict:
        return self.to_filter_payload(project)

    






    # -------------------------------------------------
    # Identifier
    # -------------------------------------------------

    def to_identifier(
        self,
        project: ProjectContext,
    ) -> str:

        # Prefer Mongo _id
        if project.id:
            return project.id

        # Fallback if the LLM placed the id into project_id
        if project.project_id:
            return project.project_id

        raise ValueError(
            "Please provide the project ID before I can retrieve its details."
        )