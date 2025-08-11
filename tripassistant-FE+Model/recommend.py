# recommend.py
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings

CHROMA_DB_PATH = "./db"
COLLECTION_NAME = "places"

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet", persist_directory=CHROMA_DB_PATH))
collection = client.get_collection(COLLECTION_NAME)

def recommend_places(user_query: str, max_price: int, k: int = 5):
    query_embedding = model.encode(user_query).tolist()
    results = collection.query(query_embeddings=[query_embedding], n_results=k)
    
    docs = results["documents"][0]
    metadatas = results["metadatas"][0]

    filtered = [
        {"ten": meta["ten"], "mo_ta": doc, "chi_phi": meta["chi_phi"]}
        for doc, meta in zip(docs, metadatas)
        if meta["chi_phi"] <= max_price
    ]

    return filtered
