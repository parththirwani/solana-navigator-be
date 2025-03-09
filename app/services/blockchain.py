"""
Service layer for blockchain operations.
"""
from app.core.agents import initialize_agents
from app.core.tasks import initialize_tasks
from app.core.crew import create_blockchain_crew
from typing import Dict, Any

class BlockchainService:
    """
    Service for handling blockchain-related operations.
    """
    
    def __init__(self):
        """Initialize the blockchain service with agents, tasks, and crew."""
        # Initialize agents
        self.task_define_agent, self.get_agent = initialize_agents()
        
        # Initialize tasks
        self.get_task, self.task_map = initialize_tasks(self.task_define_agent, self.get_agent)
        
        # Create blockchain crew
        self.crew = create_blockchain_crew(
            self.task_define_agent,
            self.get_agent,
            self.get_task,
            self.task_map
        )
    
    def process_query(self, query: str) -> Dict[str, Any]:
        """
        Process a user query through the blockchain crew.
        
        Args:
            query: The user's input text
            
        Returns:
            dict: Response data from the crew
        """
        try:
            return self.crew.process_query(query)
        except Exception as e:
            error_message = f"Error processing query: {str(e)}"
            return {"response": error_message, "task_executed": None, "error": str(e)}

# Create a singleton instance
blockchain_service = BlockchainService()