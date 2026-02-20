from sentence_transformers import SentenceTransformer
import faiss
import os
import pickle

DATA_DIR = "backend/semantic/data"
MODEL_NAME = "all-MiniLM-L6-v2"
INDEX_PATH = "backend/semantic/index.faiss"
META_PATH = "backend/semantic/meta.pkl"

print("Loading BERT model...")
model = SentenceTransformer(MODEL_NAME)

documents = []
metadata = []

print("Reading documents...")
for filename in os.listdir(DATA_DIR):
    filepath = os.path.join(DATA_DIR, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                documents.append(line)
                metadata.append({
                    "source": filename
                })

print(f"Total documents: {len(documents)}")

print("Creating embeddings...")
embeddings = model.encode(documents, show_progress_bar=True)

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

print("Saving FAISS index...")
faiss.write_index(index, INDEX_PATH)

print("Saving metadata...")
with open(META_PATH, "wb") as f:
    pickle.dump({
        "documents": documents,
        "metadata": metadata
    }, f)

print("✅ Semantic index built successfully!")
