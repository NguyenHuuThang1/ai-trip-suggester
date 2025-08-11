import chromadb
import json
from sentence_transformers import SentenceTransformer

#  Tạo client lưu trữ vĩnh viễn (tạo thư mục db/)
client = chromadb.PersistentClient(path="./db")
collection = client.get_or_create_collection(name="dulich")

# Load dữ liệu từ file JSON
with open("data/dulich.json", "r", encoding="utf-8") as f:
    data = json.load(f)

model = SentenceTransformer("all-MiniLM-L6-v2")

for idx, item in enumerate(data):
    embedding = model.encode(item["mo_ta"]).tolist()
    collection.add(
        documents=[item["mo_ta"]],
        metadatas=[{
            "ten": item["ten"],
            "gia": item["chi_phi"]
        }],
        ids=[f"id_{idx}"],
        embeddings=[embedding]
    )

print("Đã tạo collection 'dulich' và đưa dữ liệu vào ChromaDB (lưu ở ./db)")
