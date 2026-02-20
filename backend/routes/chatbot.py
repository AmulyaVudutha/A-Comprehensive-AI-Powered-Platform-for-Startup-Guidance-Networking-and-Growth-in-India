from flask import Blueprint, request, jsonify
import random

chatbot_bp = Blueprint("chatbot", __name__)

# -----------------------------
# SIMPLE INTENT DETECTION
# -----------------------------
def detect_intent(text):
    text = text.lower()

    if any(word in text for word in ["investor", "investment", "funding round"]):
        return "investor_recommendation"

    if any(word in text for word in ["mentor", "guidance", "advisor"]):
        return "mentor_recommendation"

    if any(word in text for word in ["funded", "funding success", "raise money"]):
        return "funding_prediction"

    if any(word in text for word in ["legal", "compliance", "registration", "gst", "company act"]):
        return "legal_guidance"

    return "general_guidance"


# -----------------------------
# RESPONSE ENGINES
# -----------------------------
def recommend_investors():
    return [
        "Sequoia Capital India",
        "Accel Partners",
        "Tiger Global",
        "Lightspeed Ventures"
    ]


def recommend_mentors():
    return [
        "AI Startup Mentor",
        "FinTech Industry Expert",
        "Legal & Compliance Advisor"
    ]


def predict_funding():
    return f"{random.randint(65, 85)}%"


def legal_guidance():
    return [
        "Register your startup under MCA",
        "Obtain GST registration",
        "Comply with Companies Act, 2013",
        "Protect IP with trademarks & patents"
    ]


# -----------------------------
# CHATBOT API
# -----------------------------
@chatbot_bp.route("/chatbot", methods=["POST"])
def chatbot():
    data = request.get_json()
    user_query = data.get("query", "")

    if not user_query:
        return jsonify({"error": "Query is required"}), 400

    intent = detect_intent(user_query)

    if intent == "investor_recommendation":
        return jsonify({
            "intent": intent,
            "response": recommend_investors()
        })

    elif intent == "mentor_recommendation":
        return jsonify({
            "intent": intent,
            "response": recommend_mentors()
        })

    elif intent == "funding_prediction":
        return jsonify({
            "intent": intent,
            "response": f"Funding success probability: {predict_funding()}"
        })

    elif intent == "legal_guidance":
        return jsonify({
            "intent": intent,
            "response": legal_guidance()
        })

    else:
        return jsonify({
            "intent": "general_guidance",
            "response": "I can help with investors, mentors, funding, legal compliance, and startup guidance."
        })
