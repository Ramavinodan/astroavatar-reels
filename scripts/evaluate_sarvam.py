import requests
import os
import json
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))
api_key = os.getenv("SARVAM_API_KEY")

SYSTEM_PROMPT = """
You are an expert Hindi storyteller and Vedic Astrology content creator for AstroAvatar app.
Your task is to write a script for a 90-120 second vertical Reel video in conversational Bolchal Hindi (day-to-day spoken Hindi).

STRICT RULES:
1. SEAMLESS LOOPING: Do NOT include any intro or outro phrases like "welcome" or "subscribe". The last sentence of your script MUST naturally flow into the first sentence, so that when the video restarts, it forms a perfect seamless loop. (e.g. End with an open trailing thought that completes itself with your hook).
2. The script body must be around 250 to 300 Hindi words so that natural narration takes ~90 to 120 seconds.
3. Structure of script:
   - Episode tease hook (1 sentence)
   - Setup & Story climax (80% narrative)
   - One wonder beat ("पर अजीब बात ये है...")
   - Jyotish / Spiritual takeaway
   - The seamless loop bridge clause (leading back to the hook)
4. If the story cannot fit in 300 words, set "total_parts" > 1 and write "Part 1" ending with a cliffhanger loop.
5. Break the story into 12 to 18 visual slides/beats.
6. For each slide, provide:
   - "caption": Short readable Hindi sentence (max 8-12 words) for on-screen text.
   - "image_prompt": Detailed visual AI image prompt (in English) describing a vertical 9:16 mythological cinematic artwork scene.
   - "approx_sec": Duration in seconds for this slide (e.g. 5.0 to 8.0s).

RETURN ONLY VALID JSON WITH THIS SCHEMA:
{
  "story_id": "string",
  "title": "string (Hindi title)",
  "category": "string (e.g. ज्योतिष कथा)",
  "script_hi": "string (full Hindi text for TTS, no welcome line)",
  "estimated_speech_sec": 95.0,
  "part_info": { "current_part": 1, "total_parts": 1 },
  "slides": [
    {
      "slide_index": 1,
      "caption": "Hindi caption text",
      "image_prompt": "English AI image prompt vertical 9:16 cinematic myth art",
      "approx_sec": 4.0
    }
  ]
}
"""

url = "https://api.sarvam.ai/v1/chat/completions"
headers = {"api-subscription-key": api_key, "Content-Type": "application/json"}

topics = [
    {"topic": "श्री कृष्ण का विश्वरूप दर्शन", "category": "श्रीमद्भगवद्गीता", "outline": "अर्जुन को कुरुक्षेत्र के युद्ध के दौरान श्री कृष्ण का विश्वरूप दर्शन"},
    {"topic": "राहु और केतु की उत्पत्ति", "category": "ज्योतिष कथा", "outline": "समुद्र मंथन के दौरान स्वर्भानु का अमृत पीना और भगवान विष्णु द्वारा चक्र से उसका सिर काटना"},
    {"topic": "शनिदेव की वक्र दृष्टि", "category": "नवग्रह कथा", "outline": "शनिदेव की दृष्टि जिसके भी ऊपर पड़ती है, उसके जीवन में उथल-पुथल क्यों मच जाती है"}
]

for idx, t in enumerate(topics):
    print(f"\n--- Generating Story {idx+1}: {t['topic']} ---")
    payload = {
        "model": "sarvam-105b",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Topic: {t['topic']}\nCategory: {t['category']}\nStory Outline: {t['outline']}"}
        ],
        "temperature": 0.7
    }
    try:
        res = requests.post(url, json=payload, headers=headers, timeout=60)
        print(f"Status: {res.status_code}")
        
        data = res.json()
        choices = data.get("choices", [])
        if not choices:
            print("No choices returned!")
            continue
            
        message = choices[0].get("message", {})
        content = message.get("content")
        
        if content is None:
            print("CONTENT IS NONE! Here is the full message object:")
            print(json.dumps(message, indent=2, ensure_ascii=False))
        else:
            print("Successfully received content! Length:", len(content))
            with open(f"sarvam_story_{idx+1}.json", "w", encoding="utf-8") as f:
                f.write(content)
            
    except Exception as e:
        print("API Call Failed:", str(e))

