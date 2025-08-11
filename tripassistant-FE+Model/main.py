from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer, util
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React app
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load mô hình embedding
embedding_model = SentenceTransformer("paraphrase-MiniLM-L6-v2")

# Định nghĩa schema cho request
class SuggestionRequest(BaseModel):
    query: str
    max_cost: int

@app.post("/suggest")
async def suggest_places(request: SuggestionRequest):
    with open("data/dulich.json", "r", encoding="utf-8") as f:
        locations = json.load(f)

    query_lower = request.query.lower()

    # Nếu trong query có chữ "núi" thì ưu tiên lọc loại núi
    preferred_locations = []
    if "núi" in query_lower:
        preferred_locations = [place for place in locations if "núi" in place["loai"].lower()]
    elif "biển" in query_lower:
        preferred_locations = [place for place in locations if "biển" in place["loai"].lower()]
    elif "miệt vườn" in query_lower:
        preferred_locations = [place for place in locations if "miệt vườn" in place["loai"].lower()]

    # Nếu lọc theo từ khóa rỗng → fallback toàn bộ dữ liệu
    if not preferred_locations:
        preferred_locations = locations

    # Encode query
    query_embedding = embedding_model.encode(request.query, convert_to_tensor=True)

    results = []
    for place in preferred_locations:
        if place["chi_phi"] <= request.max_cost:
            content = f"{place['ten']} - {place['mo_ta']} - {place['loai']}"
            content_embedding = embedding_model.encode(content, convert_to_tensor=True)
            score = util.pytorch_cos_sim(query_embedding, content_embedding).item()
            results.append((place, score))

    results.sort(key=lambda x: x[1], reverse=True)

    suggestions = [
        {
            "ten": place["ten"],
            "mo_ta": place["mo_ta"],
            "vung": place["vung"],
            "loai": place["loai"],
            "chi_phi": place["chi_phi"]
        }
        for place, score in results[:5]
    ]

    return suggestions
