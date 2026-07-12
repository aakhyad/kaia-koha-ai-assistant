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
        url = f"{self.base_url}{endpoint}"

        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.get(
                    url,
                    auth=self.auth,
                    headers={
                        "Accept": "application/json",
                    },
                )

                response.raise_for_status()
                return response.json()

        except httpx.HTTPStatusError as e:
            print(f"Koha API HTTP Error: {e.response.status_code}")
            print(f"URL: {url}")
            print(f"Response: {e.response.text}")
            raise

        except httpx.ReadTimeout:
            print(f"Koha API timeout: {url}")
            raise

        except Exception as e:
            print(f"Unexpected Koha API error: {e}")
            raise


koha_client = KohaClient()
