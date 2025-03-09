### ﻿Solana Blockchain Assistant
A conversational AI interface for interacting with the Solana blockchain, built with CrewAI.

## Features

Natural language processing of blockchain queries
Support for multiple Solana blockchain operations
Conversation memory for contextual responses
RESTful API for integration with other applications

## Supported Blockchain Operations

Account information retrieval
Contract metadata fetching
Transaction details lookup
Network health status
Balance checking
SOL airdrops (on devnet)
Token account operations
Inflation and supply statistics

## Setup
Clone the repository
Create a virtual environment: python -m venv venv
Activate the virtual environment:

Windows: venv\Scripts\activate
Mac/Linux: source venv/bin/activate


Install dependencies: pip install -r requirements.txt
Copy .env.example to .env and add your API keys
Run the application: python main.py

## API Usage
The main endpoint is /query which accepts POST requests with a JSON body:
jsonCopy{
  "query": "What is the balance of address dv1ZAGvdsz5hHLwWXsVnM94hWf1pjbKVau1QVkaMJ92"
}
Example response:
jsonCopy{
  "response": "The address dv1ZAGvdsz5hHLwWXsVnM94hWf1pjbKVau1QVkaMJ92 has a balance of 2.5 SOL.",
  "task_executed": "getBalance",
  "data_used": {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "getBalance",
    "params": ["dv1ZAGvdsz5hHLwWXsVnM94hWf1pjbKVau1QVkaMJ92"]
  }
}
## Prerequisites

Python 3.8+
Gemini API key (or OpenAI)
Solana API access (Alchemy or similar)
