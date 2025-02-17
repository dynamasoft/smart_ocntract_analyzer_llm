from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import os
from sentence_transformers import SentenceTransformer

# Load environment variables from .env file
load_dotenv()

# Initialize Pinecone
pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))

# pinecone.init(api_key=os.getenv("PINECONE_API_KEY"), environment="us-west1-gcp")

# Create an index
index_name = "semantic-search-index"
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="euclidean",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )

# Connect to the index
index = pc.Index(index_name)

# Load a pre-trained model for generating embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")

# Sample documents
documents = [
    "Pinecone is a vector database for machine learning applications.",
    "Vector databases are used for storing embeddings.",
    "Machine learning models can generate embeddings from text.",
    "Semantic search finds documents based on meaning.",
    "Pinecone provides fast and scalable vector search.",
]

# Generate embeddings for the documents
embeddings = model.encode(documents)

# Insert embeddings into the index
vectors_to_insert = [
    {"id": f"doc{i}", "values": embedding} for i, embedding in enumerate(embeddings)
]
index.upsert(vectors=vectors_to_insert)

# Query the index with a search query
query = "What is Pinecone used for?"
query_embedding = model.encode([query])[0]
# query_result = index.query(queries=[query_embedding], top_k=2)
query_result = index.query(queries=[query_embedding.tolist()], top_k=2)
print("Query result:", query_result)

# Clean up
index.delete()
