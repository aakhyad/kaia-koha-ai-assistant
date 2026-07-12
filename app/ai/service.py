from app.ai.providers.factory import get_ai_provider
from app.ai.intent_detector import intent_detector

from app.koha.biblios import biblios_service

from app.tools.search_books import search_books
from app.tools.search_patrons import search_patrons
from app.tools.book_details import book_details
from app.tools.book_availability import book_availability


class AIService:
    """Main AI service."""

    def __init__(self):
        self.provider = get_ai_provider()

    async def chat(self, message: str) -> str:
        """Route user requests to the appropriate tool."""

        intent = intent_detector.detect(message)

        print(f"Intent : {intent.action}")
        print(f"Query  : {intent.query}")

        # ---------------------------------
        # Search Books
        # ---------------------------------
        if intent.action == "search_books":
            return await search_books(intent.query)

        # ---------------------------------
        # Search Patrons
        # ---------------------------------
        if intent.action == "search_patron":
            return await search_patrons(intent.query)

        # ---------------------------------
        # Book Details
        # ---------------------------------
        if intent.action == "book_details":

            books = await biblios_service.search(intent.query)

            print("Books:", books)

            if not books:
                return "Book not found."

            return await book_details(
                books[0]["biblio_id"]
            )

        # ---------------------------------
        # Book Availability
        # ---------------------------------
        if intent.action == "book_availability":

            books = await biblios_service.search(intent.query)

            print("Availability Search:", books)

            if not books:
                return "Book not found."

            return await book_availability(
                books[0]["biblio_id"]
            )

        # ---------------------------------
        # General Chat
        # ---------------------------------
        return self.provider.chat(message)


ai_service = AIService()
