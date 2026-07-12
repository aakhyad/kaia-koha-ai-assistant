import json

from app.ai.providers.factory import get_ai_provider
from app.ai.intent import Intent


class IntentDetector:

    def __init__(self):
        self.provider = get_ai_provider()

    def detect(self, message: str) -> Intent:

        prompt = f"""
You are an AI assistant for Koha Library.

Return ONLY JSON.

Examples

User: Search AI books
{{"action":"search_books","query":"AI"}}

User: Find biotechnology books
{{"action":"search_books","query":"biotechnology"}}

User: Hello
{{"action":"general_chat","query":""}}

User:

{message}
"""

        reply = self.provider.chat(prompt)

        data = json.loads(reply)

        return Intent(
            action=data["action"],
            query=data["query"]
        )


intent_detector = IntentDetector()
