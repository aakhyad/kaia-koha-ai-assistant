from app.ai.providers.factory import get_ai_provider
from app.ai.intent_detector import intent_detector

from app.koha.biblios import biblios_service

from app.tools.search_books import search_books
from app.tools.search_patrons import search_patrons
from app.tools.book_details import book_details
from app.tools.book_availability import book_availability
from app.tools.item_status import item_status
from app.tools.current_checkouts import current_checkouts


class AIService:
    """Main AI service."""

    def __init__(self):
        self.provider = get_ai_provider()

    async def chat(self, message: str) -> str:
        """Route user requests to the appropriate tool."""

        intent = intent_detector.detect(message)

        print("=" * 60)
        print("Message :", message)
        print("Intent  :", intent.action)
        print("Query   :", intent.query)
        print("=" * 60)

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

            if not books:
                return "Book not found."

            return await book_availability(
                books[0]["biblio_id"]
            )

        # ---------------------------------
        # Item Status
        # ---------------------------------
        if intent.action == "item_status":

            return await item_status(intent.query)

        # ---------------------------------
        # Current Checkouts
        # ---------------------------------
        if intent.action == "current_checkouts":

            return await current_checkouts()

        # ---------------------------------
        # General Chat
        # ---------------------------------
        return self.provider.chat(message)


ai_service = AIService()
