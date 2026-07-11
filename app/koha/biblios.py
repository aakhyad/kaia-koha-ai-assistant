from app.koha.client import koha_client


class BibliographicService:
    """Bibliographic search using the Koha REST API."""

    async def search(self, query: str):
        endpoint = f"/api/v1/biblios?q={query}"
        return await koha_client.get(endpoint)


biblios_service = BibliographicService()
