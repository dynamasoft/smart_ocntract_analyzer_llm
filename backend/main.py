from fastapi import FastAPI
from backend.config import Config
import openai
import pinecone
from langchain import LangChain
from .agents import AICoordinator

app = FastAPI()

# Initialize OpenAI API
openai.api_key = Config.OPENAI_API_KEY

# Initialize Pinecone
pinecone.init(api_key=Config.VECTOR_DB_API_KEY, environment=Config.VECTOR_DB_URL)

# Initialize LangChain
langchain = LangChain()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/analyze")
async def analyze_contract(contract: str):
    # Placeholder for analysis logic
    coordinator = AICoordinator()
    analysis_results = coordinator.analyze_contract(contract)
    return {"analysis": analysis_results}
