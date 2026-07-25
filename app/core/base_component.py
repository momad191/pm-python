from abc import ABC

from typing import Any

import logging

from typing import Type, TypeVar

from pydantic import BaseModel

T = TypeVar(
    "T",
    bound=BaseModel,
)

from ..schemas.state import AgentState


class BaseComponent(ABC):
    """
    Base class shared by every Agent and Action.

    Provides reusable infrastructure such as:

    - logging
    - context access
    - context updates
    - state helpers
    - error handling
    """

    def __init__(self, name: str):

        self.name = name

        self.logger = logging.getLogger(name)

    # -------------------------------------------------
    # Logging
    # -------------------------------------------------

    def log_start(self) -> None:

        self.logger.info(
            "%s started",
            self.name,
        )

    def log_finish(self) -> None:

        self.logger.info(
            "%s finished",
            self.name,
        )

    # -------------------------------------------------
    # Question Helper
    # -------------------------------------------------

    def get_question(
        self,
        state: AgentState,
    ) -> str:
        """
        Returns the current user question.
        """

        return str(
            state.get(
                "question",
                "",
            )
        ).strip()

    # -------------------------------------------------
    # Context Helpers
    # -------------------------------------------------

    def get_context(
        self,
        state: AgentState,
        key: str,
        default: Any = None,
    ) -> Any:
        """
        Returns one context section.
        """

        context = state.get(
            "context",
            {},
        )

        return context.get(
            key,
            default,
        )

    def get_required_context(
        self,
        state: AgentState,
        key: str,
    ) -> Any:
        """
        Returns a required context section.

        Raises ValueError if missing.
        """

        value = self.get_context(
            state,
            key,
        )

        if value is None:

            raise ValueError(
                f"Missing context: {key}"
            )

        return value

    def update_context(
        self,
        state: AgentState,
        key: str,
        value: Any,
    ) -> dict[str, Any]:
        """
        Updates one section of the shared
        context while preserving others.
        """

        context = dict(
            state.get(
                "context",
                {},
            )
        )

        context[key] = value

        return context

    # -------------------------------------------------
    # State Helpers
    # -------------------------------------------------

    def success(
        self,
        answer: str | None = None,
        **extra: Any,
    ) -> dict[str, Any]:
        """
        Builds a standard state update.
        """

        result: dict[str, Any] = {}

        if answer is not None:

            result["answer"] = answer

        result.update(extra)

        return result

    def failure(
        self,
        message: str,
        **extra: Any,
    ) -> dict[str, Any]:
        """
        Builds a standard failure response.
        """

        result = {

            "answer": message,

        }

        result.update(extra)

        return result

    # -------------------------------------------------
    # Error Handling
    # -------------------------------------------------

    def handle_error(
        self,
        ex: Exception,
    ) -> dict[str, Any]:
        """
        Logs an exception and returns a
        standard failure response.
        """

        self.logger.exception(
            "%s failed: %s",
            self.name,
            ex,
        )

        return self.failure(
            "An unexpected error occurred."
        )


    # -------------------------------------------------
    # Update State
    # -------------------------------------------------

    def update_state(
        self,
        **values: Any,
        ) -> dict[str, Any]:
        """
        Returns a state update that LangGraph
        can merge into the current state.
        """

        return values




    def invoke(
        self,
        messages,
        ):
        return self.llm.invoke(messages)


    def get_model_context(
        self,
        state: AgentState,
        key: str,
        model: Type[T],
        ) -> T:
        
        """
        Reads and validates a context section
        against a Pydantic model.
        """

        context = self.get_required_context(
            state,
            key,
        )

        return model.model_validate(
            context
        )



    def call_service(
        self,
        func,
        *args,
        **kwargs,
        ):

        self.logger.info(
            "Calling %s",
            func.__name__,
        )

        return func(
            *args,
            **kwargs,
        )