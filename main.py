import uvicorn
from fastapi import FastAPI
from app.api.routes import router

# Initialize FastAPI app
app = FastAPI(
    title="Solana Blockchain Assistant",
    description="An AI-powered assistant for interacting with the Solana blockchain",
    version="1.0.0"
)

# Include API routes
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)