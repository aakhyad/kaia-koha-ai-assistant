
from app.ai.providers.factory import get_ai_provider
from app.ai.intent_detector import intent_detector
from app.koha.biblios import biblios_service
from app.tools.search_books import search_books

class AIService:
    """Main AI service."""

    def __init__(self):
        self.provider = get_ai_provider()

    async def chat(self, message: str) -> str:

        intent = intent_detector.detect(message)

        if intent.action == "search_books":

           return await search_books(intent.query)

        return self.provider.chat(message)


ai_service = AIService()
