import pinecone

# Initialize Pinecone
pinecone.init(api_key="YOUR_API_KEY", environment="us-west1-gcp")

# Create an index
index_name = "example-index"
if index_name not in pinecone.list_indexes():
    pinecone.create_index(index_name, dimension=3)

# Connect to the index
index = pinecone.Index(index_name)

# Insert vectors
vectors_to_insert = [
    {"id": "vec1", "values": [0.1, 0.2, 0.3]},
    {"id": "vec2", "values": [0.4, 0.5, 0.6]},
    {"id": "vec3", "values": [0.7, 0.8, 0.9]},
]
index.upsert(vectors=vectors_to_insert)

# Query the index
query_result = index.query(queries=[[0.1, 0.2, 0.3]], top_k=2)
print("Query result:", query_result)

# Clean up
index.delete()
