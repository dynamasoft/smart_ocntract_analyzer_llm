# Backend FastAPI Application

This is a FastAPI application that provides endpoints for basic operations and integrates with OpenAI, Pinecone, and LangChain.

## Prerequisites

- Python 3.7+
- FastAPI
- Uvicorn
- OpenAI API Key
- Pinecone API Key and Environment URL

## Installation

1. Clone the repository and navigate to the backend directory:

   ```bash
   git clone [repository-url]
   cd backend
   ```

2. Install the required Python packages:

   ```bash
   pip install fastapi uvicorn openai pinecone-client langchain
   ```

3. Set up environment variables for the API keys:

   ```bash
   export OPENAI_API_KEY='your-openai-api-key'
   export VECTOR_DB_API_KEY='your-pinecone-api-key'
   export VECTOR_DB_URL='your-pinecone-environment-url'
   ```

## Running the Application

To run the FastAPI application, use the following command:

```bash
uvicorn main:app --reload
```

This will start the server on `http://127.0.0.1:8000`.

## Endpoints

- `GET /`: Returns a simple greeting.
- `POST /analyze`: Analyzes a contract using the AI Coordinator.

## License

This project is licensed under the MIT License.
