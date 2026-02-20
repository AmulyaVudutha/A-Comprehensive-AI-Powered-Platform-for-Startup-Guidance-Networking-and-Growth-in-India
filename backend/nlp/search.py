import joblib
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

texts, embeddings = joblib.load("backend/nlp/tech_embeddings.pkl")
model = SentenceTransformer("all-MiniLM-L6-v2")

def semantic_search(query):
    q = model.encode([query])
    scores = cosine_similarity(q, embeddings)[0]
    return texts[scores.argmax()]
