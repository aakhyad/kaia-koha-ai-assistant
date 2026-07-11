import httpx

from app.core.settings import settings


class KohaClient:
    """Client for communicating with the Koha REST API."""

    def __init__(self):
        self.base_url = settings.KOHA_BASE_URL
        self.auth = (
            settings.KOHA_USERNAME,
            settings.KOHA_PASSWORD,
        )

    async def get(self, endpoint: str):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}{endpoint}",
                auth=self.auth,
                headers={
                    "Accept": "application/json",
                },
            )
            response.raise_for_status()
            return response.json()


koha_client = KohaClient()
