from semantic_search import semantic_search

queries = [
    "How can I get funding for my fintech startup?",
    "I need legal compliance help for a startup in India",
    "Looking for AI mentors",
    "How to approach investors for 10 lakhs funding",
    "I have a startup idea, how should I implement it?"
]

for q in queries:
    print("\nQ:", q)
    answers = semantic_search(q)
    for a in answers:
        print("→", a)
