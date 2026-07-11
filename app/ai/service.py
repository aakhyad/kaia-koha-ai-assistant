from app.ai.providers.factory import get_ai_provider


class AIService:
    """Main AI service that delegates requests to the configured provider."""

    def __init__(self):
        self.provider = get_ai_provider()

    def chat(self, message: str) -> str:
        return self.provider.chat(message)


ai_service = AIService()

