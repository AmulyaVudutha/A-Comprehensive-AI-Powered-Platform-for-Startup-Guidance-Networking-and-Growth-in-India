from flask import Blueprint, jsonify
import pandas as pd

recommend_bp = Blueprint("recommend", __name__)

@recommend_bp.route("/recommend/investors")
def recommend_investors():
    df = pd.read_csv("backend/ml/models/investor_scores.csv")
    top = df.sort_values("similarity_score", ascending=False).head(5)
    return jsonify(top.to_dict(orient="records"))
