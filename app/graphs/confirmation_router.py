from ..schemas.state import AgentState


class ConfirmationRouter:

    # -------------------------------------------------
    # Execute
    # -------------------------------------------------

    def execute(
        self,
        state: AgentState,
    ) -> AgentState:

        context = state.setdefault("context", {})

        project = context.get("project")

        if not project:
            state["confirmation"] = None
            return state

        if not project.get("waiting_confirmation"):
            state["confirmation"] = None
            return state

        answer = (
            state.get("question", "")
            .strip()
            .lower()
        )

        # -------------------------
        # Approved
        # -------------------------

        if answer in {
            "yes",
            "y",
            "ok",
            "okay",
            "confirm",
            "sure",
        }:

            state["confirmation"] = "approved"

            project["waiting_confirmation"] = False

            context["project"] = project
            state["context"] = context

            return state

        # -------------------------
        # Rejected
        # -------------------------

        if answer in {
            "no",
            "cancel",
            "stop",
        }:

            state["confirmation"] = "rejected"

            state["answer"] = "Deletion cancelled."

            project["waiting_confirmation"] = False

            context["project"] = project
            state["context"] = context

            return state

        # -------------------------
        # Still waiting
        # -------------------------

        state["confirmation"] = "waiting"

        state["answer"] = (
            "Please reply with 'yes' or 'no'."
        )

        return state

    # -------------------------------------------------
    # Route
    # -------------------------------------------------

    def route(
        self,
        state: AgentState,
    ) -> str:

        confirmation = state.get("confirmation")

        # No confirmation workflow in progress
        if confirmation is None:
            return "manager"

        # User approved
        if confirmation == "approved":
            return "delete"

        # User rejected
        if confirmation == "rejected":
            return "end"

        # Still waiting for yes/no
        return "end"


confirmation_router = ConfirmationRouter()