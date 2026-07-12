from dataclasses import dataclass


@dataclass
class Intent:
    action: str
    query: str
