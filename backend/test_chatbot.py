import requests

url = "http://127.0.0.1:5000/chatbot"

data = {"message": "I have a startup idea, can you guide me?"}
res = requests.post(url, json=data)
print("Bot:", res.json()["response"])

data = {"message": "Suggest investors for a fintech startup"}
res = requests.post(url, json=data)
print("Bot:", res.json()["response"])
