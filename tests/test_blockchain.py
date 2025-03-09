"""
Tests for blockchain service functionality.
"""
import unittest
from unittest.mock import patch, MagicMock
from app.services.blockchain import BlockchainService

class TestBlockchainService(unittest.TestCase):
    """Test cases for the blockchain service."""
    
    @patch('app.core.agents.initialize_agents')
    @patch('app.core.tasks.initialize_tasks')
    @patch('app.core.crew.create_blockchain_crew')
    def setUp(self, mock_create_crew, mock_initialize_tasks, mock_initialize_agents):
        """Set up test environment."""
        # Mock the agents
        self.mock_task_define_agent = MagicMock()
        self.mock_get_agent = MagicMock()
        mock_initialize_agents.return_value = (self.mock_task_define_agent, self.mock_get_agent)
        
        # Mock the tasks
        self.mock_get_task = MagicMock()
        self.mock_task_map = {
            "getBalance": MagicMock(),
            "getAccountInfo": MagicMock()
        }
        mock_initialize_tasks.return_value = (self.mock_get_task, self.mock_task_map)
        
        # Mock the crew
        self.mock_crew = MagicMock()
        mock_create_crew.return_value = self.mock_crew
        
        # Create blockchain service
        self.blockchain_service = BlockchainService()
    
    def test_process_query_success(self):
        """Test successful query processing."""
        # Set up the mock
        self.mock_crew.process_query.return_value = {
            "response": "The balance is 2.5 SOL.",
            "task_executed": "getBalance",
            "data_used": {"method": "getBalance", "params": ["address"]}
        }
        
        # Call the method
        result = self.blockchain_service.process_query("What's the balance of this address?")
        
        # Assert that the mock was called correctly
        self.mock_crew.process_query.assert_called_once_with("What's the balance of this address?")
        
        # Assert that the result is correct
        self.assertEqual(result["response"], "The balance is 2.5 SOL.")
        self.assertEqual(result["task_executed"], "getBalance")
    
    def test_process_query_error(self):
        """Test error handling in query processing."""
        # Set up the mock to raise an exception
        self.mock_crew.process_query.side_effect = Exception("Test error")
        
        # Call the method
        result = self.blockchain_service.process_query("Invalid query")
        
        # Assert that the result contains an error message
        self.assertIn("Error processing query:", result["response"])
        self.assertEqual(result["task_executed"], None)
        self.assertEqual(result["error"], "Test error")

if __name__ == '__main__':
    unittest.main()