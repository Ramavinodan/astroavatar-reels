import requests
import os
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
payload = {
    "model": "sarvam-105b",
    "messages": [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Topic: श्री कृष्ण का विश्वरूप दर्शन\nCategory: श्रीमद्भगवद्गीता\nStory Outline: अर्जुन को कुरुक्षेत्र के युद्ध के दौरान श्री कृष्ण का विश्वरूप दर्शन"}
    ],
    "temperature": 0.7
}
res = requests.post(url, json=payload, headers=headers)
print("Status:", res.status_code)
content = res.json()["choices"][0]["message"]["content"]
print("Response Length:", len(content))
print("Response Snippet:\n", content[:500])
with open("test_output.json", "w") as f:
    f.write(content)
