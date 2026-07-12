from app.koha.client import koha_client


class ItemService:
    """Fetch item records from Koha."""

    async def get_items(self, biblio_id: int):
        return await koha_client.get(
            f"/api/v1/biblios/{biblio_id}/items"
        )


item_service = ItemService()
