import os
import pandas as pd
import joblib
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix

print("Loading dataset...")

# ---------------- PATH FIX ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # backend/ml
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, "..", ".."))

DATASET_PATH = os.path.join(PROJECT_ROOT, "datasets", "investments.csv")
MODEL_PATH = os.path.join(BASE_DIR, "models", "investor_similarity.pkl")

print("Dataset path resolved to:")
print(DATASET_PATH)

# ---------------- LOAD DATA ----------------
df = pd.read_csv(
    DATASET_PATH,
    usecols=["funded_object_id", "investor_object_id"]
)

df = df.dropna().drop_duplicates()

# ---------------- ENCODE ----------------
startup_ids = df["funded_object_id"].astype("category")
investor_ids = df["investor_object_id"].astype("category")

row_codes = startup_ids.cat.codes
col_codes = investor_ids.cat.codes

# ---------------- SPARSE MATRIX ----------------
print("Building sparse matrix...")
matrix = csr_matrix(
    (1, (row_codes, col_codes)),
    shape=(startup_ids.cat.categories.size,
           investor_ids.cat.categories.size)
)

# ---------------- SIMILARITY ----------------
print("Computing cosine similarity...")
similarity = cosine_similarity(matrix, dense_output=False)

# ---------------- SAVE ----------------
joblib.dump(
    {
        "similarity": similarity,
        "startup_ids": list(startup_ids.cat.categories),
        "investor_ids": list(investor_ids.cat.categories),
    },
    MODEL_PATH
)

print("Investor recommendation model trained & saved successfully ✅")
print("Model saved at:", MODEL_PATH)
