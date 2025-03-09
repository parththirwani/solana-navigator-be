from crewai.tools.structured_tool import CrewStructuredTool
from pydantic import BaseModel
import requests
from app.config.settings import SOLANA_API_URL

class APICallInput(BaseModel):
    """Schema for API call input data."""
    data: dict

def tool_wrapper(*args, **kwargs):
    """
    Wrapper function to execute API calls to the Solana blockchain.
    
    Args:
        kwargs: Keyword arguments containing the API request data
        
    Returns:
        dict: JSON response from the API or None if the request failed
    """
    url = SOLANA_API_URL
    
    try:
        response = requests.post(url, json=kwargs["data"])

        if response.status_code == 200:
            return response.json()
        else:
            print(f'Error: {response.status_code}')
            return {"error": f"API call failed with status code {response.status_code}"}
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
        return {"error": str(e)}

def create_structured_tool():
    """
    Create and return a structured tool for making API calls.
    
    Returns:
        CrewStructuredTool: A tool for making API calls
    """
    return CrewStructuredTool.from_function(
        name='Blockchain API Tool',
        description="A tool to interact with the Solana blockchain API",
        args_schema=APICallInput,
        func=tool_wrapper,
    )