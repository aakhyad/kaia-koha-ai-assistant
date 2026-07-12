from app.koha.client import koha_client


class BookDetailsService:
    """Retrieve book details from the Koha REST API."""

    async def get(self, biblio_id: int):
        return await koha_client.get(f"/api/v1/biblios/{biblio_id}")


book_details_service = BookDetailsService()
