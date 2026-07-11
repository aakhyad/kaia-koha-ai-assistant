from abc import ABC, abstractmethod


class AIProvider(ABC):
    """Base class for all AI providers."""

    @abstractmethod
    def chat(self, message: str) -> str:
        """Generate a response from the AI model."""
        pass

