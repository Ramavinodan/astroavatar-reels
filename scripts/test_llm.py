import os
import json
from story_generator import generate_story_llm
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))
topic = {
    "id": "test",
    "title": "श्री कृष्ण का विश्वरूप दर्शन",
    "category": "श्रीमद्भगवद्गीता",
    "prompt": "अर्जुन को कुरुक्षेत्र के युद्ध के दौरान श्री कृष्ण का विश्वरूप दर्शन",
    "keywords": ["vishnu", "krishna"]
}

sarvam_key = os.getenv("SARVAM_API_KEY")
res = generate_story_llm(topic, api_key=sarvam_key, provider="sarvam")
print(json.dumps(res, indent=2, ensure_ascii=False))
