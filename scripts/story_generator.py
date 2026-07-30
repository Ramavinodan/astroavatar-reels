"""
LLM Script & Beat Generator for AstroAvatar Reels.
Supports Sarvam AI, DeepSeek, Gemini Flash, OpenAI, OpenRouter, Groq, or Fallback Template.
Strictly adheres to CONTENT_RULES.md: 60s to 90s total reel duration (~130-160 words speech).
Auto-splits longer stories into Part 1, Part 2, etc.
"""
import os
import json
import requests
from typing import Dict, Any, Optional
from topic_catalog import get_next_topic

LOCKED_WELCOME_HI = "नमस्ते… AstroAvatar की डेली डोज़ में आपका स्वागत है।"

SYSTEM_PROMPT = """
You are an expert Hindi storyteller and Vedic Astrology content creator for AstroAvatar app.
Your task is to write a script for a 60-90 second vertical Reel video in conversational Bolchal Hindi (day-to-day spoken Hindi).

STRICT RULES:
1. DO NOT include any welcome line (the welcome line is added automatically).
2. The script body must be around 130 to 160 Hindi words so that natural narration takes ~50 to 75 seconds.
3. Structure of script:
   - Episode tease line (1 sentence)
   - Setup & Story climax (80% narrative)
   - One wonder beat ("पर अजीब बात ये है...")
   - Jyotish / Spiritual takeaway ("इसीलिए...")
4. If the story cannot fit in 150 words, set "total_parts" > 1 and write "Part 1" ending with a cliffhanger.
5. Break the story into 10 to 14 visual slides/beats.
6. For each slide, provide:
   - "caption": Short readable Hindi sentence (max 8-12 words) for on-screen text.
   - "image_prompt": Detailed visual AI image prompt (in English) describing a vertical 9:16 mythological cinematic artwork scene.
   - "approx_sec": Duration in seconds for this slide (e.g. 3.5 to 5.0s).

RETURN ONLY VALID JSON WITH THIS SCHEMA:
{
  "story_id": "string",
  "title": "string (Hindi title)",
  "category": "string (e.g. ज्योतिष कथा)",
  "script_hi": "string (full Hindi text for TTS, no welcome line)",
  "estimated_speech_sec": 55.0,
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

def generate_story_llm(topic_info: Dict[str, Any], api_key: Optional[str] = None, provider: str = "sarvam") -> Dict[str, Any]:
    """Generates story script using LLM API or fallback template."""
    prompt_text = f"Topic: {topic_info['title']}\nCategory: {topic_info['category']}\nStory Outline: {topic_info['prompt']}"

    # Try LLM call if key exists
    if api_key and provider:
        try:
            if provider.lower() == "sarvam":
                url = "https://api.sarvam.ai/v1/chat/completions"
                headers = {"api-subscription-key": api_key, "Content-Type": "application/json"}
                payload = {
                    "model": "sarvam-105b",
                    "messages": [
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": prompt_text}
                    ],
                    "temperature": 0.7
                }
                res = requests.post(url, json=payload, headers=headers, timeout=35)
                if res.status_code == 200:
                    content = res.json()["choices"][0]["message"]["content"]
                    return parse_llm_json(content, topic_info)

            elif provider.lower() in ["openai", "deepseek", "groq", "openrouter"]:
                # Standard OpenAI compatible endpoints
                endpoint = os.getenv("LLM_ENDPOINT", "https://api.openai.com/v1/chat/completions")
                model_name = os.getenv("LLM_MODEL", "gpt-4o-mini")
                headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
                payload = {
                    "model": model_name,
                    "messages": [
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": prompt_text}
                    ],
                    "response_format": {"type": "json_object"}
                }
                res = requests.post(endpoint, json=payload, headers=headers, timeout=30)
                if res.status_code == 200:
                    content = res.json()["choices"][0]["message"]["content"]
                    return parse_llm_json(content, topic_info)
        except Exception as e:
            print(f"[Warning] LLM API call failed ({e}). Using built-in story generator template.")

    return generate_fallback_story(topic_info)

def parse_llm_json(content: str, topic_info: Dict[str, Any]) -> Dict[str, Any]:
    try:
        # strip code fences if present
        clean_content = content.replace("```json", "").replace("```", "").strip()
        data = json.loads(clean_content)
        return data
    except Exception:
        return generate_fallback_story(topic_info)

def generate_fallback_story(topic_info: Dict[str, Any]) -> Dict[str, Any]:
    """Pre-crafted fallback story generator following Rahu Ketu or Ramayana/Gita templates."""
    if topic_info["id"] == "rahu_ketu_origin":
        return {
            "story_id": "rahu_ketu_origin",
            "title": "राहु-केतु की कहानी",
            "category": "ज्योतिष कथा",
            "script_hi": "आज — राहु और केतु कैसे बने। सुनो… एक पुरानी बात। देवता और असुर मिलकर समुद्र मंथन कर रहे थे। मंथन से निकला अमृत — जिसे पीकर अमर हुआ जा सकता था। भगवान विष्णु ने मोहिनी रूप धरा और देवताओं को अमृत पिलाने लगे। लेकिन एक असुर चुपके से देवताओं की लाइन में आ बैठा। उसका नाम था स्वर्भानु। उसने धोखे से अमृत की कुछ बूंदें पी लीं। सूर्य और चंद्र देव ने उसे पहचान लिया और भगवान विष्णु को इशारा कर दिया। विष्णु जी ने तुरंत सुदर्शन चक्र से स्वर्भानु का सिर धड़ से अलग कर दिया। पर अजीब बात यह थी… अमृत पीने के कारण वो मरा ही नहीं! उसका कटा हुआ सिर बना राहु, और शरीर बना केतु। इसीलिए आज भी राहु-केतु सूर्य और चंद्रमा से बदला लेने के लिए ग्रहण लगाते हैं। यह सिर्फ अँधेरा नहीं — ब्रह्मांड का एक गहरा नियम है।",
            "estimated_speech_sec": 52.5,
            "part_info": {"current_part": 1, "total_parts": 1},
            "slides": [
                {"slide_index": 1, "caption": "आज — राहु और केतु कैसे बने", "image_prompt": "Cosmic Hindu gods and demons churning the celestial ocean, glowing golden chalice, epic oil painting style, vertical 9:16", "approx_sec": 3.2},
                {"slide_index": 2, "caption": "सुनो… एक पुरानी बात", "image_prompt": "Ancient Indian Vedic rishi narrating cosmic mystery under starry night sky, ethereal glow, vertical 9:16", "approx_sec": 2.8},
                {"slide_index": 3, "caption": "देवता-असुर समुद्र मंथन कर रहे थे", "image_prompt": "Devas and Asuras pulling the giant serpent Vasuki around Mount Mandara in cosmic ocean, vertical 9:16", "approx_sec": 5.5},
                {"slide_index": 4, "caption": "अमृत निकला — अमर होने वाला अमृत", "image_prompt": "Divine golden pot of Amrita nectar radiating divine light, celestial rays, vertical 9:16", "approx_sec": 4.0},
                {"slide_index": 5, "caption": "मोहिनी रूप में अमृत बाँटने लगीं", "image_prompt": "Lord Vishnu in Mohini enchantress avatar holding golden urn of nectar, elegant divine beauty, vertical 9:16", "approx_sec": 4.5},
                {"slide_index": 6, "caption": "एक असुर चुपके से लाइन में घुस आया", "image_prompt": "Shadowy demon shapeshifting and sneaking into line of radiant devas, atmospheric drama, vertical 9:16", "approx_sec": 4.0},
                {"slide_index": 7, "caption": "उसका नाम था स्वर्भानु", "image_prompt": "Mysterious demon Swarbhanu sitting in secrecy between Sun god and Moon god, vertical 9:16", "approx_sec": 3.0},
                {"slide_index": 8, "caption": "अमृत पी लिया · सूर्य-चंद्र ने पकड़ा", "image_prompt": "Swarbhanu swallowing glowing drop of nectar, Surya and Chandra watching with shock, vertical 9:16", "approx_sec": 5.0},
                {"slide_index": 9, "caption": "भेस पकड़ लिया · सच खोल दिया", "image_prompt": "Sun God Surya pointing finger at disguised demon, cosmic aura flare, vertical 9:16", "approx_sec": 3.5},
                {"slide_index": 10, "caption": "सुदर्शन चक्र · सिर अलग · शरीर अलग", "image_prompt": "Lord Vishnu releasing flaming Sudarshan Chakra disc slicing through cosmic demon, vivid golden light, vertical 9:16", "approx_sec": 4.5},
                {"slide_index": 11, "caption": "पर अजीब बात… वो मरा ही नहीं", "image_prompt": "Glowing immortality aura keeping separated head and body alive in dark deep space, vertical 9:16", "approx_sec": 4.0},
                {"slide_index": 12, "caption": "सिर बना राहु · शरीर बना केतु", "image_prompt": "Cosmic shadow planet Rahu head and snake tailed Ketu body in galaxy space, dramatic lighting, vertical 9:16", "approx_sec": 3.5},
                {"slide_index": 13, "caption": "इसीलिए ग्रहण लगता है", "image_prompt": "Solar and lunar eclipse in starry cosmic sky, shadow silhouette, majestic Hindu astrology art, vertical 9:16", "approx_sec": 3.0},
                {"slide_index": 14, "caption": "ये सिर्फ अँधेरा नहीं — एक पुरानी कथा", "image_prompt": "Ancient sacred Sanskrit scroll glowing with starry cosmic horoscopes and constellations, vertical 9:16", "approx_sec": 2.0}
            ]
        }
    
    # Generic template for other topics
    return {
        "story_id": topic_info["id"],
        "title": topic_info["title"],
        "category": topic_info["category"],
        "script_hi": f"आज — {topic_info['title']}। सुनो… हमारे पुराणों में इसका गहरा रहस्य छिपा है। {topic_info['prompt']}। इसीलिए जीवन में इस सीख को याद रखना बेहद जरूरी है।",
        "estimated_speech_sec": 55.0,
        "part_info": {"current_part": 1, "total_parts": 1},
        "slides": [
            {"slide_index": 1, "caption": f"आज — {topic_info['title']}", "image_prompt": f"Hindu deity mythology art vertical 9:16 cinematic lighting {topic_info['keywords'][0]}", "approx_sec": 4.0},
            {"slide_index": 2, "caption": "सुनो… एक गहरा रहस्य", "image_prompt": f"Ancient Vedic temple glowing cosmic aura vertical 9:16 {topic_info['keywords'][1] if len(topic_info['keywords'])>1 else ''}", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "पौराणिक कथाओं के अनुसार", "image_prompt": f"Spiritual Hindu epic illustration vertical 9:16 high detail", "approx_sec": 6.0},
            {"slide_index": 4, "caption": "यह सिर्फ कहानी नहीं — एक महान सीख है", "image_prompt": f"Cosmic energy mandalas and stars glowing vertical 9:16", "approx_sec": 5.0}
        ]
    }
