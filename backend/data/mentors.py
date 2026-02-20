MENTORS = [
    {"name": "Ankit Sharma", "domain": "AI", "experience": "10 years"},
    {"name": "Priya Verma", "domain": "FinTech", "experience": "8 years"},
    {"name": "Rahul Mehta", "domain": "Legal", "experience": "12 years"}
]

def find_mentor(domain):
    return [m for m in MENTORS if domain.lower() in m["domain"].lower()]
