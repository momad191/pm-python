from typing import Any

from .base_action import BaseAction

from ....schemas.project_context import ProjectContext
from ....schemas.state import AgentState

from ....schemas.responses.project_response import (
    ProjectResponse,
)

from ....services.project_service import (
    ProjectService,
    project_service,
)


class SearchProjectAction(BaseAction):
    """
    Workflow responsible for searching projects.

    Responsibilities

    - Read ProjectContext
    - Delegate filtered retrieval to ProjectService
    - Update LangGraph state
    """

    def __init__(
        self,
        service: ProjectService = project_service,
    ):

        super().__init__("SearchProjectAction")

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

            #
            # Read ProjectContext
            #
            project = self.get_project_context(
                state,
            )

            self.logger.info(
                "Validated ProjectContext = %s",
                project.model_dump(),
            )

            self.logger.info(
                "Searching projects."
            )

            #
            # Delegate to ProjectService
            #
            projects: list[
                ProjectResponse
            ] = self.service.search(
                project,
            )

            entities = [

                item.model_dump()

                for item in projects

            ]

            self.logger.info(

                "Search returned %d project(s).",

                len(entities),

            )

            return self.update_state(

                answer=f"Found {len(entities)} matching project(s).",

                current_action="completed",

                entities=entities,

                context=self.update_context(

                    state,

                    "project",

                    {

                        **project.model_dump(),

                        "entities": entities,

                    },

                ),

            )

        except Exception as ex:

            return self.handle_error(ex)

        finally:

            self.log_finish()


search_project_action = SearchProjectAction()