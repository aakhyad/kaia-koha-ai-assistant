from app.ai.providers.factory import get_ai_provider
from app.koha.biblios import biblios_service


class AIService:
    """Main AI service."""

    def __init__(self):
        self.provider = get_ai_provider()

    async def chat(self, message: str) -> str:
        msg = message.lower()

        if (
            "search book" in msg
            or "search books" in msg
            or "find book" in msg
            or "find books" in msg
            or "book on" in msg
            or "books on" in msg
        ):

            query = msg

            for phrase in [
                "search books on",
                "search book on",
                "find books on",
                "find book on",
                "search books",
                "search book",
                "find books",
                "find book",
                "books on",
                "book on",
            ]:
                if query.startswith(phrase):
                    query = query[len(phrase):].strip()
                    break

            results = await biblios_service.search(query)

            if not results:
                return f"No books found for '{query}'."

            response = "Books found:\n\n"

            for book in results[:10]:
                response += f"• {book.get('title', 'Untitled')}\n"

            return response

        return self.provider.chat(message)


ai_service = AIService()
