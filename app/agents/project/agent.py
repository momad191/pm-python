from typing import Any

from ..base.base_agent import BaseAgent

from ...schemas.state import AgentState

from .prompt import PROJECT_SYSTEM_PROMPT
 
   
from ...schemas.project import ProjectDecision


class ProjectAgent(BaseAgent):
    """
    Project Domain Agent.

    Responsible for understanding project-related
    requests and producing a structured project
    decision for downstream execution.
    """

    def __init__(self):

        super().__init__("ProjectAgent")

        self.decision_llm = self.get_structured_llm(
            ProjectDecision
        )
 
    def run(
        self,
        state: AgentState,
    ) -> dict[str, Any]:

        self.log_start()

        question = self.get_question(state)

        self.logger.info(
            "Question: %s",
            question,
        )

        if not question:

            self.logger.warning(
                "Received empty question."
            )

            return {
                "answer": "No project request was provided."
            }
 
        messages = self.build_messages(
            PROJECT_SYSTEM_PROMPT,
            question,
        )

        try:

            decision = self.decision_llm.invoke(messages)

            decision = decision.normalize()


            self.logger.info(
                "ProjectDecision = %s",
                decision.model_dump(),
                 )

        except Exception as ex:

            return self.handle_error(ex)

        self.logger.info(
            "Project Decision: %s",
            decision.model_dump(exclude_none=True),
        )

        self.log_finish()



        project_data = decision.model_dump(exclude_none=True)

        if decision.search:

            search = {}

            if decision.search.text:
                search["search_text"] = decision.search.text

            if decision.search.project_id:
                search["project_id"] = decision.search.project_id

            if decision.search.manager_id:
                search["manager_id"] = decision.search.manager_id

            if decision.search.department:
                search["department"] = decision.search.department

            if decision.search.status:
                search["status"] = decision.search.status

            if decision.search.date:

                search["date_field"] = decision.search.date.field
                search["month"] = decision.search.date.month
                search["year"] = decision.search.date.year
                search["start_date"] = decision.search.date.from_date
                search["end_date"] = decision.search.date.to_date

            project_data["search"] = {
                k: v
                for k, v in search.items()
                if v is not None
            }



        context = self.update_context(
            state,
            "project",
            project_data
        )

        self.logger.info(
            "Stored Project Context = %s",
            context["project"],
            )


        return {
         "project_action": decision.action,
         "context": context,
            }

                 

        # return {

        #     # Useful for graph routing
        #     "project_action": decision.action,

        #     # Shared context
        #     "context": self.update_context(

        #         state,

        #         "project",

        #         decision.model_dump(exclude_none=True),

        #     ),

        # }


    @staticmethod
    def route(state: AgentState) -> str:
        return state.get(
            "project_action",
            "unknown",
        )
    


project_agent = ProjectAgent()