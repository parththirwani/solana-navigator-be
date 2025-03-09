"""
API routes for the blockchain assistant.
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.blockchain import blockchain_service
from typing import Optional, Dict, Any

router = APIRouter()

class QueryRequest(BaseModel):
    """Request model for user queries."""
    query: str

class QueryResponse(BaseModel):
    """Response model for processed queries."""
    response: str
    task_executed: Optional[str] = None
    data_used: Optional[Dict[str, Any]] = None

@router.post("/query", response_model=QueryResponse)
async def process_query(request: QueryRequest):
    """
    Process a blockchain query from the user.
    
    Args:
        request: The query request containing the user's input
        
    Returns:
        QueryResponse: The processed response
    """
    try:
        result = blockchain_service.process_query(request.query)
        return QueryResponse(
            response=result["response"],
            task_executed=result.get("task_executed"),
            data_used=result.get("data_used")
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")

@router.get("/health")
async def health_check():
    """
    API health check endpoint.
    
    Returns:
        dict: Health status
    """
    return {"status": "healthy", "service": "blockchain-assistant"}

@router.get("/tasks")
async def list_available_tasks():
    """
    List all available blockchain tasks that can be performed.
    
    Returns:
        dict: List of available tasks with descriptions
    """
    return {
        "available_tasks": [
            {"name": "getAccountInfo", "description": "Get account information for an address"},
            {"name": "getContractMetadata", "description": "Fetch contract metadata"},
            {"name": "getGasPrices", "description": "Get current gas prices"},
            {"name": "getTransactionDetails", "description": "Get details for a transaction"},
            {"name": "getHealth", "description": "Check blockchain network health"},
            {"name": "requestAirdrop", "description": "Request an airdrop of SOL"},
            {"name": "getBalance", "description": "Get balance for an address"},
            {"name": "getInflationRate", "description": "Get current inflation rate"},
            {"name": "getSupply", "description": "Get token supply information"},
            {"name": "getTokenAccountBalance", "description": "Get token account balance"},
            {"name": "getTokenAccountsByDelegate", "description": "Get token accounts by delegate"},
            {"name": "getTokenAccountsByOwner", "description": "Get token accounts by owner"},
            {"name": "getTokenLargestAccounts", "description": "Get largest token accounts"},
            {"name": "getTokenSupply", "description": "Get token supply information"}
        ]
    }