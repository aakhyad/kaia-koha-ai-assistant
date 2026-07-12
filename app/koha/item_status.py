from app.koha.client import koha_client


class ItemStatusService:
    """Retrieve an item by barcode."""

    async def get(self, barcode: str):

        items = await koha_client.get(
            f"/api/v1/items?external_id={barcode}"
        )

        if not items:
            return None

        return items[0]


item_status_service = ItemStatusService()
