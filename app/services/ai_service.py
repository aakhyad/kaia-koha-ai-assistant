class AIService:
    """Service responsible for AI chat responses."""

    def chat(self, message: str) -> str:
        return (
            "Hello! I am KAIA.\n\n"
            f"You said: {message}\n\n"
            "I am currently running in demo mode.\n"
            "Real AI integration (OpenAI/Ollama) will be added in the next sprint."
        )


ai_service = AIService()
