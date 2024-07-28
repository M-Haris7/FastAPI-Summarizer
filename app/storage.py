from typing import Dict

class InMemoryStorage:
    def __init__(self):
        self.storage: Dict[str, str] = {}

    def save_text(self, session_id: str, text: str):
        self.storage[session_id] = text

    def get_text(self, session_id: str) -> str:
        return self.storage.get(session_id, "")

    def delete_text(self, session_id: str):
        if session_id in self.storage:
            del self.storage[session_id]

# Create a global instance of the storage
storage = InMemoryStorage()
