from flask import Blueprint, request, jsonify
import joblib

predict_bp = Blueprint("predict", __name__)
model = joblib.load("backend/ml/models/funding_model.pkl")

@predict_bp.route("/predict", methods=["POST"])
def predict():
    data = request.json
    X = [[data["industry"], data["city"], data["amount"]]]
    result = model.predict(X)
    return jsonify({"funding_prediction": int(result[0])})
