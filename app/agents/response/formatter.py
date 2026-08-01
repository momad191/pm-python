import json


class ResponseFormatter:

    @staticmethod
    def build_context(state):

        payload = {

            "question": state.get("question"),

            "operation": state.get("response", {}),

            "project": state.get("context", {}).get("project"),

            "entities": state.get("entities", []),

            

            "selected_agent": state.get("selected_agent"),

            "project_action": state.get("project_action"),

            "task_action": state.get("task_action"),

            "issue_action": state.get("issue_action"),

            "context": state.get("context"),

            "answer": state.get("answer"),

        }

        return json.dumps(
            payload,
            indent=2,
            default=str,
        )