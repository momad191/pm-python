from abc import ABC
from typing import Any, Callable

import logging


class BaseService(ABC):
    """
    Base class for all business services.

    Responsibilities:

    - Logger creation
    - Client injection
    - Service lifecycle logging
    - Error handling
    - Executing client operations
    """

    def __init__(
        self,
        name: str,
        client: Any,
    ) -> None:

        self.name = name

        self.logger = logging.getLogger(name)

        self.client = client

    # -------------------------------------------------
    # Logging
    # -------------------------------------------------

    def log_start(
        self,
        operation: str,
    ) -> None:

        self.logger.info(
            "%s started.",
            operation,
        )

    def log_finish(
        self,
        operation: str,
    ) -> None:

        self.logger.info(
            "%s completed successfully.",
            operation,
        )

    # -------------------------------------------------
    # Error Handling
    # -------------------------------------------------

    def handle_error(
        self,
        operation: str,
        ex: Exception,
    ) -> None:

        self.logger.exception(
            "%s failed: %s",
            operation,
            ex,
        )

        raise ex

    # -------------------------------------------------
    # Client Execution
    # -------------------------------------------------

    def execute(
        self,
        operation: str,
        func: Callable[..., Any],
        *args: Any,
        **kwargs: Any,
    ) -> Any:
        """
        Executes a client operation with
        consistent logging and error handling.
        """

        self.log_start(operation)

        try:

            result = func(
                *args,
                **kwargs,
            )

            self.log_finish(operation)

            return result

        except Exception as ex:

            self.handle_error(
                operation,
                ex,
            )