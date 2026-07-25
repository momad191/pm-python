from ...schemas.state import AgentState

from ...constants.project import ProjectAction


def route_project_action(
    state: AgentState,
) -> str:
    """
    Returns the next graph node based on the
    project action selected by the ProjectAgent.
    """

    action = state.get(
        "project_action",
        ProjectAction.GENERAL,
    )

    return str(action)