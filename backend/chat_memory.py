# backend/chat_memory.py
from collections import deque

class ConversationMemory:
    """
    Stores conversation history for a user.
    Uses a fixed-length deque to limit memory size.
    """

    def __init__(self, max_length=10):
        self.max_length = max_length
        self.history = deque(maxlen=self.max_length)

    def add_message(self, role, content):
        """
        role: 'user' or 'bot'
        content: message text
        """
        self.history.append({"role": role, "content": content})

    def get_history(self):
        """
        Returns conversation history as a list of messages.
        """
        return list(self.history)

    def clear_history(self):
        self.history.clear()
