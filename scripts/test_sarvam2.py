import requests
import os
import json
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))
api_key = os.getenv("SARVAM_API_KEY")

url = "https://api.sarvam.ai/v1/chat/completions"
headers = {"api-subscription-key": api_key, "Content-Type": "application/json"}
payload = {
    "model": "sarvam-105b",
    "messages": [
        {"role": "user", "content": "Tell me a short story about Krishna."}
    ],
    "temperature": 0.7
}
res = requests.post(url, json=payload, headers=headers)
print("Status:", res.status_code)
print(res.text)
