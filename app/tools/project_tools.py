from ..graphs.project_graph import project_graph

class ProjectTools:

    def invoke(
        self,
        state: dict,
    ):

        return project_graph.invoke(state)


project_tools = ProjectTools()