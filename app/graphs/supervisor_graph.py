from langgraph.graph import (
    START,
    END,
    StateGraph,
)

from ..schemas.state import AgentState

from ..agents.manager.agent import (
    manager_agent,
)

from ..tools.project_tools import (
    project_tools,
)


builder = StateGraph(AgentState)

builder.add_node(
    "manager",
    manager_agent.run,
)

builder.add_node(
    "project",
    project_tools.invoke,
)

builder.add_edge(
    START,
    "manager",
)

builder.add_conditional_edges(

    "manager",

    manager_agent.route,

    {

        "project": "project",

    },

)

builder.add_edge(
    "project",
    END,
)

graph = builder.compile()