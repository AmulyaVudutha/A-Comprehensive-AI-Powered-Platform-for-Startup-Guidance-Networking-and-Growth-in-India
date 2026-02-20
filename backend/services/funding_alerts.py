def get_funding_alerts(domain):
    alerts = {
        "fintech": [
            "Razorpay Ventures announced seed funding program",
            "Y Combinator accepting FinTech applications"
        ],
        "health": [
            "NHA innovation grants open",
            "WHO startup funding initiative"
        ]
    }
    return alerts.get(domain.lower(), ["No new alerts currently"])
