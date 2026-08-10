import requests
import base64
import os

API_KEY = "sk_fh3k3uri_4Smlkzms2n9ro5dekANCVIql"
URL = "https://api.sarvam.ai/text-to-speech"

script = """
From a bus driver's son to the unstoppable Rocky Bhai, how did Yash conquer Indian cinema? The secret is in his stars! 
Born with a Bharani Ascendant ruled by Venus, he was destined for an electrifying screen presence. 
But look at his 9th house! Venus, Sun, and Mercury unite to form a massive Dhana Yoga, turning pure artistic talent into a box-office goldmine! 
And it doesn't stop there. In his 10th house, Jupiter creates a powerful Neechabhanga Raja Yoga, fueling his incredible self-made rise from humble beginnings to the absolute top! 
His Venus Dasha sparked his acting debut, but it was the fiery Sun Dasha that gave the world K G F! 
Now entering his Moon Dasha, get ready for Yash to dominate on a global scale. The stars have spoken!
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
