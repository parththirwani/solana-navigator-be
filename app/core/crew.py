"""
Crew management for orchestrating agents and tasks.
"""
from crewai import Crew
from app.core.memory import conversation_memory
from app.data.task_params import TASK_PARAMS_MAP
from typing import Dict, Any, Optional, Union

class BlockchainCrew:
    """
    Class to manage the CrewAI workflow for blockchain interactions.
    """
    
    def __init__(self, task_define_agent, get_agent, get_task, task_map):
        """
        Initialize the blockchain crew.
        
        Args:
            task_define_agent: Agent for identifying tasks
            get_agent: Agent for executing blockchain operations
            get_task: Task for identifying what the user wants
            task_map: Dictionary mapping task names to task objects
        """
        self.task_define_agent = task_define_agent
        self.get_agent = get_agent
        self.get_task = get_task
        self.task_map = task_map
        
        # Initialize the first crew for task identification
        self.task_identifier_crew = Crew(
            agents=[self.task_define_agent],
            tasks=[self.get_task],
            memory=True,
            verbose=True,
            llm=self.task_define_agent.llm
        )
    
    def process_query(self, user_input: str) -> Dict[str, Any]:
        """
        Process a user query through the crew workflow.
        
        Args:
            user_input: The user's input string
            
        Returns:
            dict: Response data
        """
        # Add user input to memory
        conversation_memory.add_user_message(user_input)
        
        # Prepare inputs for the task identifier
        inputs = {
            "text": user_input, 
            "task_params_map": TASK_PARAMS_MAP, 
            "memory": conversation_memory.get_memory()
        }
        
        # Identify the task
        task_result = self.task_identifier_crew.kickoff(inputs=inputs)
        
        # Handle conversational responses (no blockchain task needed)
        if not hasattr(task_result, 'task') or not task_result.task:
            conversation_memory.add_assistant_message(task_result.raw)
            return {"response": task_result.raw, "task_executed": None}
        
        # If a valid blockchain task is identified, execute it
        if task_result.task in self.task_map:
            task = self.task_map[task_result.task]
            
            # Create a crew for the specific blockchain task
            blockchain_crew = Crew(
                agents=[self.get_agent],
                tasks=[task],
                memory=True,
                verbose=True,
                llm=self.task_define_agent.llm
            )
            
            # Execute the blockchain task
            blockchain_result = blockchain_crew.kickoff(inputs={"data": task_result.data})
            
            # Add result to memory
            conversation_memory.add_assistant_message(blockchain_result.raw)
            
            return {
                "response": blockchain_result.raw,
                "task_executed": task_result.task,
                "data_used": task_result.data
            }
        else:
            # Handle the case when an invalid task is identified
            error_message = f"Unable to process task: {task_result.task}"
            conversation_memory.add_assistant_message(error_message)
            return {"response": error_message, "task_executed": None}

def create_blockchain_crew(task_define_agent, get_agent, get_task, task_map):
    """
    Factory function to create a blockchain crew.
    
    Args:
        task_define_agent: Agent for identifying tasks
        get_agent: Agent for executing blockchain operations
        get_task: Task for identifying what the user wants
        task_map: Dictionary mapping task names to task objects
        
    Returns:
        BlockchainCrew: An instance of the blockchain crew
    """
    return BlockchainCrew(task_define_agent, get_agent, get_task, task_map)