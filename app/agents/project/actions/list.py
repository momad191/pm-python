from typing import Any

from datetime import datetime

from .base_action import BaseAction
 
from ....schemas.project_context import ProjectContext
from ....schemas.state import AgentState

from ....services.project_service import (
    ProjectService,
    project_service,
)

from ....schemas.responses.project_response import ProjectResponse

class ListProjectAction(BaseAction):
    """
    Workflow responsible for listing projects.

    Responsibilities

    - Read ProjectContext
    - Retrieve projects
    - Update LangGraph context
    """

    def __init__(
        self,
        service: ProjectService = project_service,
    ):

        super().__init__("ListProjectAction")

        self.service = service

    def execute(
        self,
        state: AgentState,
    ) -> dict[str, Any]:

        self.log_start()

        try:

            self.logger.info(
                "Incoming Context = %s",
                state.get("context"),
            )


            project = self.get_project_context(
                state,
            )

            self.logger.info(
                "Validated ProjectContext = %s",
                project.model_dump(),
            )

            self.logger.info(
                "Retrieving project list."
            )

            # projects: list[ProjectResponse] = self.service.list(project)  
      

            # entities = [
            #     item.model_dump()
            #     for item in projects
            # ]

            list_result = self.service.list(project)
            

            entities = [
                item.model_dump()
                for item in list_result
            ]

            total = len(entities)


            return self.update_state(

                current_action="project.list.completed",

                response={

                    "domain": "project",

                    "operation": "list",

                    "success": True,

                    "execution": {

                        "service": "ProjectService.list",

                        "entity": "project",

                        "count": total,

                    },

                    "api_result": {

                        "total": total,

                        "page": 1,

                        "limit": total,

                        "total_pages": 1,

                    },

                    "result_count": total,

                    "pagination": {

                        "page": 1,

                        "limit": total,

                        "total_pages": 1,

                    },

                    "input": project.model_dump(exclude_none=True),

                    "timestamp": datetime.utcnow().isoformat(),

                },

                entities=entities,

                context=self.update_context(

                    state,

                    "project",

                    {

                        **project.model_dump(),

                        "entities": entities,

                        "total": total,

                        "page": 1,

                        "limit": total,

                        "totalPages": 1,

                    },

                ),

            )


        except Exception as ex:

            return self.handle_error(ex)

        finally:

            self.log_finish()


list_project_action = ListProjectAction()