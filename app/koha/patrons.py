from app.koha.client import koha_client


class PatronService:
    """Patron search using the Koha REST API."""

    async def search(self, query: str):
        patrons = await koha_client.get("/api/v1/patrons")

        query = query.lower()
        results = []

        for patron in patrons:
            firstname = (patron.get("firstname") or "").lower()
            surname = (patron.get("surname") or "").lower()
            userid = (patron.get("userid") or "").lower()
            cardnumber = (patron.get("cardnumber") or "").lower()

            if (
                query in firstname
                or query in surname
                or query in userid
                or query in cardnumber
            ):
                results.append(patron)

        return results


patron_service = PatronService()
