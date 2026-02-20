class PromptBuilder:
    def __init__(self, memory):
        self.memory = memory

    def build_messages(self, user_query, context=""):
        messages = []

        # System message
        messages.append({
            "role": "system",
            "content": "You are a helpful AI startup mentor."
        })

        if context:
            messages.append({
                "role": "system",
                "content": f"Context: {context}"
            })

        # Add conversation history
        for msg in self.memory.get_history():
            messages.append(msg)

        # Current user message
        messages.append({
            "role": "user",
            "content": user_query
        })

        return messages
