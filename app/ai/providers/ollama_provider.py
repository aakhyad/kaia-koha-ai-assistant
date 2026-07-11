from ollama import chat

from app.ai.providers.base import AIProvider


class OllamaProvider(AIProvider):
    """Ollama implementation of AIProvider."""

    def __init__(self, model: str = "qwen2.5:3b"):
        self.model = model

    def chat(self, message: str) -> str:
        response = chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": message,
                }
            ],
        )

        return response["message"]["content"]
