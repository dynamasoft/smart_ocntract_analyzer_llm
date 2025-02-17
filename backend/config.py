import os


# Configuration for API keys and other settings
class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your-openai-api-key")
    VECTOR_DB_API_KEY = os.getenv("VECTOR_DB_API_KEY", "your-vector-db-api-key")
    VECTOR_DB_URL = os.getenv("VECTOR_DB_URL", "https://your-vector-db-url")
