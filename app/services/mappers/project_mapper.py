from ...schemas.project_context import ProjectContext


class ProjectMapper:

    def to_create_payload(
        self,
        project: ProjectContext,
    ) -> dict:

        return {

            "projectId": project.project_code,

            "name": project.name,

            "description": project.description,

            "managerId": project.manager_id,

            "department": project.department,

            "status": project.status,

            "startDate": project.start_date,

            "endDate": project.end_date,

            "completionPercentage": project.completion_percentage,


        }

    def to_update_payload(
        self,
        project: ProjectContext,
    ) -> dict:

        return self.to_create_payload(project)