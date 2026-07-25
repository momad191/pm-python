import httpx

from ..config import settings


class NestJSClient:

    def __init__(self):

        self.base_url = settings.NESTJS_API_URL

        self.client = httpx.Client(
            base_url=self.base_url,
            timeout=30,
        )

    def get(self, endpoint: str, params=None):

        response = self.client.get(
            endpoint,
            params=params,
        )

        response.raise_for_status()

        return response.json()

    def post(self, endpoint: str, data=None):

        response = self.client.post(
            endpoint,
            json=data,
        )

        response.raise_for_status()

        return response.json()

    def patch(self, endpoint: str, data=None):

        response = self.client.patch(
            endpoint,
            json=data,
        )

        response.raise_for_status()

        return response.json()

    def delete(self, endpoint: str):

        response = self.client.delete(endpoint)

        response.raise_for_status()

        return response.json()


nestjs_client = NestJSClient()