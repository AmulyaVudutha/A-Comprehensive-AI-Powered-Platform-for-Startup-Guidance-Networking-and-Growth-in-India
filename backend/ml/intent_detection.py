# backend/ml/intent_detection.py

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# ---------------------------
# Load pre-trained SBERT model
# ---------------------------
model = SentenceTransformer('all-MiniLM-L6-v2')

# ---------------------------
# Define intents and example phrases
# ---------------------------
INTENTS = {
    "investor_recommendation": [
        "recommend investors",
        "suggest investors",
        "who can invest in my startup",
        "find investors for my startup"
    ],
    "mentor_recommendation": [
        "recommend a mentor",
        "I need a mentor",
        "guide me with a mentor",
        "find me a startup mentor"
    ],
    "funding_prediction": [
        "will my startup get funded",
        "predict funding success",
        "funding prediction",
        "can I get funding for my startup"
    ],
    "general_guidance": [
        "give me advice",
        "help me with startup guidance",
        "what should I do next",
        "guide me"
    ]
}

# ---------------------------
# Precompute embeddings for intent phrases
# ---------------------------
intent_embeddings = {}
for intent, phrases in INTENTS.items():
    embeddings = model.encode(phrases)
    intent_embeddings[intent] = embeddings

# ---------------------------
# Function to detect intent
# ---------------------------
def detect_intent(user_query):
    """
    Returns the intent name for a user query
    """
    query_embedding = model.encode([user_query])
    
    best_intent = None
    best_score = -1

    # Compare query to each intent's example embeddings
    for intent, embeddings in intent_embeddings.items():
        scores = cosine_similarity(query_embedding, embeddings)
        max_score = np.max(scores)
        if max_score > best_score:
            best_score = max_score
            best_intent = intent

    return best_intent, float(best_score)

# ---------------------------
# Test
# ---------------------------
if __name__ == "__main__":
    queries = [
        "Can you suggest investors for my fintech startup?",
        "I need a mentor in AI domain",
        "Will my startup get funded?",
        "What should I do next?"
    ]

    for q in queries:
        intent, score = detect_intent(q)
        print(f"Query: {q}\nIntent: {intent}, Score: {score:.3f}\n")
