import pandas as pd
import numpy as np
import pickle
import os
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity

# ---------------- PATHS ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_PATH = os.path.join(BASE_DIR, "..", "..", "datasets", "investments.csv")
MODEL_DIR = os.path.join(BASE_DIR, "models")
MODEL_PATH = os.path.join(MODEL_DIR, "investor_similarity.pkl")

os.makedirs(MODEL_DIR, exist_ok=True)

print("Loading dataset...")
df = pd.read_csv(DATASET_PATH)

df = df[["funded_object_id", "investor_object_id"]].dropna()

# Encode IDs
startup_ids = df["funded_object_id"].astype("category")
investor_ids = df["investor_object_id"].astype("category")

row = startup_ids.cat.codes.values
col = investor_ids.cat.codes.values
data = np.ones(len(df))

print("Building sparse matrix...")
matrix = csr_matrix(
    (data, (row, col)),
    shape=(startup_ids.cat.categories.size,
           investor_ids.cat.categories.size)
)

print("Computing cosine similarity...")
similarity = cosine_similarity(matrix, dense_output=False)

# Save EVERYTHING needed
with open(MODEL_PATH, "wb") as f:
    pickle.dump({
        "similarity": similarity,
        "startup_ids": list(startup_ids.cat.categories),
        "investor_ids": list(investor_ids.cat.categories)
    }, f)

print("Investor recommendation model trained & saved successfully ✅")
print("Model saved at:", MODEL_PATH)
