from app.koha.biblios import biblios_service


async def search_books(query: str) -> str:
    """
    Search books in Koha and return a formatted response.
    """

    books = await biblios_service.search(query)

    if not books:
        return f"No books found for '{query}'."

    response = "📚 Books found:\n\n"

    for index, book in enumerate(books[:10], start=1):
        response += (
            f"{index}. {book.get('title', 'Untitled')}\n"
            f"   👤 Author : {book.get('author') or 'Unknown'}\n"
            f"   📖 ISBN   : {book.get('isbn') or 'N/A'}\n\n"
        )

    return response
