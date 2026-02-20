from sentence_transformers import SentenceTransformer
import pandas as pd
import joblib

df = pd.read_csv("../../datasets/techcrunch_posts.csv")
texts = df.iloc[:,0].astype(str).tolist()

model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(texts)

joblib.dump((texts, embeddings), "tech_embeddings.pkl")
