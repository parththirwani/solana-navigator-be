import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Blockchain API endpoint
SOLANA_API_URL = os.getenv("SOLANA_API_URL", "https://solana-devnet.g.alchemy.com/v2/jK9f7FhUJarWMR9nozOhvCKB1Qdj3VYS")

# LLM settings
DEFAULT_TEMPERATURE = 0
DEFAULT_MODEL = "gemini/gemini-1.5-flash"

# Application settings
DEBUG = os.getenv("DEBUG", "False").lower() == "true"