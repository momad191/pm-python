from langgraph.graph import (
    START,
    END,
    StateGraph,
)

from ..schemas.state import AgentState

from ..agents.project.agent import (
    project_agent,
)

from ..agents.response.agent import (
    response_agent,
)

# -------------------------------------------------
# Actions
# -------------------------------------------------

from ..agents.project.actions.create import (
    create_project_action,
)

from ..agents.project.actions.update import (
    update_project_action,
)

from ..agents.project.actions.list import (
    list_project_action,
)

from ..agents.project.actions.details import (
    details_project_action,
)

from ..agents.project.actions.search import (
    search_project_action,
)

from ..agents.project.actions.delete import (
    delete_project_action,
)

from ..agents.project.actions.delete_request import (
    delete_project_request_action,
)
 
# -------------------------------------------------
# Approval
# -------------------------------------------------

from ..core.approval.approval_node import (
    approval_node,
)

from ..core.approval.approval_router import (
    approval_router,
)

builder = StateGraph(AgentState)

# =================================================
# Nodes
# =================================================

builder.add_node(
    "response_agent",
    response_agent.run,
)


builder.add_node(
    "project_agent",
    project_agent.run,
)

builder.add_node(
    "create_project",
    create_project_action.execute,
)

builder.add_node(
    "update_project",
    update_project_action.execute,
)

builder.add_node(
    "list_projects",
    list_project_action.execute,
)

builder.add_node(
    "project_details",
    details_project_action.execute,
)

builder.add_node(
    "search_projects",
    search_project_action.execute,
)

#
# Human approval request
#
builder.add_node(
    "request_delete_project",
    delete_project_request_action.execute,
)

#
# Actual delete
#
builder.add_node(
    "delete_project",
    delete_project_action.execute,
)

#
# Waiting node
#
builder.add_node(
    "approval",
    approval_node,
)

# =================================================
# Entry
# =================================================

builder.add_edge(
    START,
    "project_agent",
)

# =================================================
# Router
# =================================================

builder.add_conditional_edges(

    "project_agent",

    project_agent.route,

    {

        "create": "create_project",

        "update": "update_project",

        # "delete": "request_delete_project",

        "delete": "delete_project",

        "list": "list_projects",

        "details": "project_details",

        "search": "search_projects",

     

    },

)

# =================================================
# Approval Flow
# =================================================

# builder.add_edge(
#     "request_delete_project",
#     "approval",
# )

# builder.add_conditional_edges(

#     "approval",

#     approval_router,

#     {

#         #
#         # User still hasn't answered
#         #
#         "wait": END,

#         #
#         # User rejected
#         #
#         "cancel": END,

#         #
#         # User approved
#         #
#         "delete_project": "delete_project",

#     },

# )

# =================================================
# Finish
# =================================================

builder.add_edge(
    "create_project",
     END,
)

builder.add_edge(
    "update_project",
    END,
)

builder.add_edge(
    "list_projects",
      END,
)

builder.add_edge(
    "project_details",
     END,
)

builder.add_edge(
    "search_projects",
     END,
)

builder.add_edge(
    "delete_project",
     END,
)


builder.add_edge(
    "response_agent",
    END,
)

project_graph = builder.compile()