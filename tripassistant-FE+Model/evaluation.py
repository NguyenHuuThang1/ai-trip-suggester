# evaluate.py
import json
from sentence_transformers import SentenceTransformer, util

# Load dữ liệu
with open("data/dulich.json", "r", encoding="utf-8") as f:
    locations = json.load(f)

# Load model embedding (giống API)
embedding_model = SentenceTransformer("paraphrase-MiniLM-L6-v2")

# Danh sách query test
test_queries = [
    {"query": "leo núi", "expected_type": "núi"},
    {"query": "nghỉ dưỡng ở biển", "expected_type": "biển"},
    {"query": "tham quan miệt vườn", "expected_type": "miệt vườn"}
]

K = 5  # số kết quả top-k để đánh giá

def filter_and_rank(query, max_cost=99999999):
    query_lower = query.lower()

    # Filter giống code FastAPI
    if "núi" in query_lower:
        preferred_locations = [place for place in locations if "núi" in place["loai"].lower()]
    elif "biển" in query_lower:
        preferred_locations = [place for place in locations if "biển" in place["loai"].lower()]
    elif "miệt vườn" in query_lower:
        preferred_locations = [place for place in locations if "miệt vườn" in place["loai"].lower()]
    else:
        preferred_locations = locations

    # Ranking bằng cosine similarity
    query_embedding = embedding_model.encode(query, convert_to_tensor=True)
    results = []
    for place in preferred_locations:
        if place["chi_phi"] <= max_cost:
            content = f"{place['ten']} - {place['mo_ta']} - {place['loai']}"
            content_embedding = embedding_model.encode(content, convert_to_tensor=True)
            score = util.pytorch_cos_sim(query_embedding, content_embedding).item()
            results.append((place, score))

    results.sort(key=lambda x: x[1], reverse=True)
    return [place for place, score in results[:K]]

def precision_at_k(results, expected_type):
    correct = sum(1 for place in results if expected_type.lower() in place["loai"].lower())
    return correct / len(results) if results else 0

def recall_at_k(results, expected_type):
    all_relevant = [place for place in locations if expected_type.lower() in place["loai"].lower()]
    correct = sum(1 for place in results if expected_type.lower() in place["loai"].lower())
    return correct / len(all_relevant) if all_relevant else 0

if __name__ == "__main__":
    total_precision = 0
    total_recall = 0

    for test in test_queries:
        results = filter_and_rank(test["query"])
        precision = precision_at_k(results, test["expected_type"])
        recall = recall_at_k(results, test["expected_type"])
        total_precision += precision
        total_recall += recall

        print(f"Query: {test['query']}")
        print(f"Precision@{K}: {precision:.2f}")
        print(f"Recall@{K}: {recall:.2f}")
        print("Kết quả trả về:", [p["ten"] for p in results])
        print("-" * 50)

    avg_precision = total_precision / len(test_queries)
    avg_recall = total_recall / len(test_queries)
    print(f"Trung bình Precision@{K}: {avg_precision:.2f}")
    print(f"Trung bình Recall@{K}: {avg_recall:.2f}")
