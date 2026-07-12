from app.ai.intent import Intent


class IntentDetector:
    """Detect the user's intent."""

    def detect(self, message: str) -> Intent:

        msg = message.lower().strip()

        # -----------------------------
        # Book Search
        # -----------------------------
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

            return Intent(
                action="search_books",
                query=query,
            )

        # -----------------------------
        # Patron Search
        # -----------------------------
        if (
            "search patron" in msg
            or "find patron" in msg
            or "search member" in msg
            or "find member" in msg
        ):

            query = msg

            for phrase in [
                "search patron",
                "find patron",
                "search member",
                "find member",
            ]:
                if query.startswith(phrase):
                    query = query[len(phrase):].strip()
                    break

            return Intent(
                action="search_patron",
                query=query,
            )

        # -----------------------------
        # Book Details
        # -----------------------------
        if (
            "show details of" in msg
            or "book details of" in msg
            or "details of" in msg
            or "show details" in msg
            or "book details" in msg
        ):

            query = msg

            for phrase in [
                "show details of",
                "book details of",
                "details of",
                "show details",
                "book details",
            ]:
                if query.startswith(phrase):
                    query = query[len(phrase):].strip()
                    break

            return Intent(
                action="book_details",
                query=query,
            )

        # -----------------------------
        # Book Availability
        # -----------------------------
        if (
            "available" in msg
            or "availability" in msg
            or "copies" in msg
        ):

            query = msg

            for phrase in [
                "how many copies of",
                "copies of",
                "availability of",
                "is",
                "available",
            ]:
                query = query.replace(phrase, "")

            query = (
                query.replace("?", "")
                     .replace(".", "")
                     .replace(",", "")
                     .strip()
            )

            return Intent(
                action="book_availability",
                query=query,
            )

        # -----------------------------
        # General Chat
        # -----------------------------
        return Intent(
            action="general_chat",
            query=message,
        )


intent_detector = IntentDetector()
