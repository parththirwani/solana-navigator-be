"""
Memory management for conversation context.
"""
from typing import List, Dict, Any

class ConversationMemory:
    """Class to manage conversation history and context."""
    
    def __init__(self):
        """Initialize an empty conversation memory."""
        self.memory: List[Dict[str, str]] = []
    
    def add_user_message(self, content: str) -> None:
        """
        Add a user message to the conversation memory.
        
        Args:
            content: The content of the user message
        """
        self.memory.append({"role": "user", "content": content})
    
    def add_assistant_message(self, content: str) -> None:
        """
        Add an assistant message to the conversation memory.
        
        Args:
            content: The content of the assistant message
        """
        self.memory.append({"role": "assistant", "content": content})
    
    def get_memory(self) -> List[Dict[str, str]]:
        """
        Get the current conversation memory.
        
        Returns:
            List of message dictionaries
        """
        return self.memory
    
    def clear_memory(self) -> None:
        """Clear all conversation memory."""
        self.memory = []

# Create memory instance
conversation_memory = ConversationMemory()