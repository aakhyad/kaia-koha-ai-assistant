from app.ai.providers.ollama_provider import OllamaProvider


def get_ai_provider():
    """
    Return the configured AI provider.
    """
    return OllamaProvider()
