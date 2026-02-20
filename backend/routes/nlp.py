from flask import Blueprint, request
from nlp.search import semantic_search

nlp_bp = Blueprint("nlp", __name__)

@nlp_bp.route("/ask", methods=["POST"])
def ask():
    query = request.form["query"]
    return semantic_search(query)
