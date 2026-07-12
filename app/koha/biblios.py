from app.koha.client import koha_client


class BibliographicService:
    """Bibliographic search using Koha REST API."""

    async def search(self, query: str):
        books = await koha_client.get("/api/v1/biblios")

        query = query.lower()
        results = []

        for book in books:
            title = (book.get("title") or "").lower()
            author = (book.get("author") or "").lower()

            if query in title or query in author:
                results.append(book)

        return results


biblios_service = BibliographicService()
