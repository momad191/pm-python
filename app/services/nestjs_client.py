import httpx
import logging

from typing import Any

from ..config import settings


logger = logging.getLogger(__name__)


class NestJSClient:
    """
    Generic HTTP client for communicating with the
    NestJS backend.

    Exposes generic REST methods plus thin
    domain-specific helpers.
    """

    def __init__(self):

        self.base_url = settings.NESTJS_API_URL.rstrip("/")

        self.client = httpx.Client(
            base_url=self.base_url,
            timeout=30,
        )

    # -------------------------------------------------
    # Generic HTTP Methods
    # -------------------------------------------------

    def get(
        self,
        endpoint: str,
        params: dict[str, Any] | None = None,
    ) -> dict[str, Any]:

        logger.debug("GET %s", endpoint)

        response = self.client.get(
            endpoint,
            params=params,
        )

        response.raise_for_status()

        return response.json()

    def post(
        self,
        endpoint: str,
        data: dict[str, Any] | None = None,
    ) -> dict[str, Any]:

        logger.debug("POST %s", endpoint)

        response = self.client.post(
            endpoint,
            json=data,
        )

        response.raise_for_status()

        return response.json()

    def patch(
        self,
        endpoint: str,
        data: dict[str, Any] | None = None,
    ) -> dict[str, Any]:

        logger.debug("PATCH %s", endpoint)

        response = self.client.patch(
            endpoint,
            json=data,
        )

        response.raise_for_status()

        return response.json()

    def delete(
        self,
        endpoint: str,
    ) -> dict[str, Any]:

        logger.debug("DELETE %s", endpoint)

        response = self.client.delete(
            endpoint,
        )

        response.raise_for_status()

        return response.json()

    # =================================================
    # Project API
    # =================================================

    def create_project(
        self,
        payload: dict[str, Any],
    ) -> dict[str, Any]:

        return self.post(
            "/project",
            payload,
        )

    def update_project(
        self,
        project_id: str,
        payload: dict[str, Any],
    ) -> dict[str, Any]:

        return self.patch(
            f"/project/{project_id}",
            payload,
        )

    def delete_project(
        self,
        project_id: str,
    ) -> dict[str, Any]:

        return self.delete(
            f"/project/{project_id}",
        )

    def get_project(
        self,
        project_id: str,
    ) -> dict[str, Any]:

        return self.get(
            f"/project/{project_id}",
        )

    def list_projects(
        self,
        params: dict[str, Any] | None = None,
    ) -> dict[str, Any]:

        return self.get(
            "/project",
            params,
        )

    def search_projects(
        self,
        params: dict[str, Any],
    ) -> dict[str, Any]:

        return self.get(
            "/project/search",
            params,
        )

    # -------------------------------------------------

    def close(self):

        self.client.close()


nestjs_client = NestJSClient()