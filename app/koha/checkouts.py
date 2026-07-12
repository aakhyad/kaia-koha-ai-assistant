from app.koha.client import koha_client


class CheckoutService:
    """Checkout service using the Koha REST API."""

    async def list(self):
        return await koha_client.get("/api/v1/checkouts")


checkout_service = CheckoutService()
