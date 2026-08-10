import requests
import base64
import os

API_KEY = "sk_fh3k3uri_4Smlkzms2n9ro5dekANCVIql"
URL = "https://api.sarvam.ai/text-to-speech"

script = """
How did a bus driver's son become the Rocking Star of Indian Cinema? Let's decode Yash's Kundli. 
He has a Bharani Ascendant ruled by Venus, giving him magnetic screen presence. 
But the real magic lies in his 9th house! Venus, Sun, and Mercury form a rare Dhana Yoga here, translating artistic talent into massive wealth. 
And in his 10th house, Jupiter creates a Neechabhanga Raja Yoga, driving his self-made rise to the top. 
His Venus Dasha started his acting journey, but the Sun Dasha brought global stardom with K G F! 
Next is his Moon Dasha, which points to major international ventures. Yash's stars were truly aligned for greatness!
"""

payload = {
    "text": script.strip(),
    "speaker": "shubh",
    "model": "bulbul:v3",
    "target_language_code": "en-IN",
    "pace": 1.10,
    "sample_rate": 24000
}

headers = {
    "api-subscription-key": API_KEY,
    "Content-Type": "application/json"
}

response = requests.post(URL, json=payload, headers=headers)

if response.status_code == 200:
    data = response.json()
    audio_content = base64.b64decode(data['audios'][0])
    
    output_path = os.path.join(os.path.dirname(__file__), "public/audio/yash-narration-full.wav")
    with open(output_path, "wb") as f:
        f.write(audio_content)
        
    print(f"Success! Saved to: {output_path}")
else:
    print(f"Error {response.status_code}: {response.text}")
