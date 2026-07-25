from langgraph.graph import (
    START,
    END,
    StateGraph,
)

from ..schemas.state import AgentState

from ..agents.project.agent import (
    project_agent,
)

from ..agents.project.actions.create import (
    create_project_action,
)


builder = StateGraph(AgentState)

# -------------------------------------------------
# Nodes
# -------------------------------------------------

builder.add_node(
    "project_agent",
    project_agent.run,
)

builder.add_node(
    "create_project",
    create_project_action.execute,
)

# -------------------------------------------------
# Flow
# -------------------------------------------------

builder.add_edge(
    START,
    "project_agent",
)
 

builder.add_conditional_edges(

    "project_agent",

    project_agent.route,

    {

        "create": "create_project",

        # "update": "update_project",

        # "delete": "delete_project",

        # "list": "list_projects",

        # "details": "project_details",

        # "search": "search_projects",

        # "archive": "archive_project",

        # "restore": "restore_project",

        # "statistics": "project_statistics",

    },

)


builder.add_edge(

    "create_project",

    END,

)

project_graph = builder.compile()