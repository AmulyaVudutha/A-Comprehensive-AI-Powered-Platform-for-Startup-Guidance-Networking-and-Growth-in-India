import faiss
import pickle
from sentence_transformers import SentenceTransformer
import numpy as np

INDEX_PATH = "backend/semantic/index.faiss"
META_PATH = "backend/semantic/meta.pkl"
MODEL_NAME = "all-MiniLM-L6-v2"

# Load model once
model = SentenceTransformer(MODEL_NAME)

# Load FAISS index
index = faiss.read_index(INDEX_PATH)

# Load documents & metadata
with open(META_PATH, "rb") as f:
    meta = pickle.load(f)

documents = meta["documents"]
metadata = meta["metadata"]

def semantic_search(query, top_k=3):
    """
    Returns top_k relevant answers for a user query
    """
    query_embedding = model.encode([query])
    query_embedding = np.array(query_embedding).astype("float32")

    distances, indices = index.search(query_embedding, top_k)

    results = []
    for idx in indices[0]:
        if idx < len(documents):
            results.append(documents[idx])

    return results
def semantic_answer(query):
    results = semantic_search(query)

    if results:
        return results[0]   # best matching guidance
    return None
