from ..schemas.responses.response_decision import (
    ResponseDecision,
    EntityReference,
    SuggestedAction,
)


class ResponseBuilder:

    @staticmethod
    def search_projects(projects):

        return ResponseDecision(

            title="Project Search",

            answer=f"I found {len(projects)} matching projects.",

            summary=f"{len(projects)} project(s) matched.",

            entities=[

                EntityReference(

                    type="project",

                    id=p.id,

                    title=p.name,

                )

                for p in projects

            ],

            suggested_actions=[

                SuggestedAction(

                    label="Show Details",

                    action="project.details"

                )

            ]

        )