from langgraph.graph import (
    START,
    END,
    StateGraph,
)

from ..schemas.state import AgentState

from ..agents.manager.agent import (
    manager_agent,
)


from ..agents.general.agent import (
    general_agent,
)

from ..agents.response.agent import (
    response_agent,
)

from ..tools.project_tools import (
    project_tools,
)

from .confirmation_router import (
    confirmation_router,
)

from .checkpointer import (
    memory,
)


builder = StateGraph(AgentState)

# -------------------------------------------------
# Nodes
# -------------------------------------------------

builder.add_node(
    "confirmation",
    confirmation_router.execute,
)

builder.add_node(
    "general",
    general_agent.run,
)

builder.add_node(
    "manager",
    manager_agent.run,
)

builder.add_node(
    "response_agent",
    response_agent.run,
)

builder.add_node(
    "project",
    project_tools.invoke,
)
 
# -------------------------------------------------
# START
# -------------------------------------------------

builder.add_edge(
    START,
    "confirmation",
)

# -------------------------------------------------
# Confirmation Router
# -------------------------------------------------

builder.add_conditional_edges(
    "confirmation",
    confirmation_router.route,
    {
        # No pending approval
        "manager": "manager",

        # User approved deletion
        "project": "project",


        # for general questions
        "general": "general",

        # Cancelled or invalid confirmation
        "end": END,
    },
)


 

# -------------------------------------------------
# Manager Router
# -------------------------------------------------

builder.add_conditional_edges(
    "manager",
    manager_agent.route,
    {
        "project": "project",
        "general": "general",
    },
)

# -------------------------------------------------
# Finish
# -------------------------------------------------

builder.add_edge(
    "project",
    "response_agent",
)


# builder.add_edge(
#     "general",
#     END,
# )

builder.add_edge(
    "general",
    "response_agent",
)

builder.add_edge(
    "response_agent",
    END,
)


graph = builder.compile(
    checkpointer=memory,
) 