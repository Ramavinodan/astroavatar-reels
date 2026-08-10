import requests
import base64
import os
import time

# Replace with your actual Sarvam API key
API_KEY = "sk_fh3k3uri_4Smlkzms2n9ro5dekANCVIql"
URL = "https://api.sarvam.ai/text-to-speech"

# A typical 45-50 word Hindi script for a 30-second reel
test_script = """
क्या आप जानते हैं राहु अचानक धन क्यों देता है? समुद्र मंथन के समय जब राहु ने धोखे से अमृत पिया, 
तो भगवान विष्णु ने उसका सिर काट दिया। लेकिन वह मरा नहीं! 
बिना शरीर के, राहु के पास केवल दिमाग और भूख है—दुनियावी चीज़ों की भूख। 
इसलिए जब राहु मेहरबान होता है, तो वह बिना किसी सीमा के देता है। 
क्या आपके चार्ट में राहु मज़बूत है? कमेंट्स में 'जय श्री राम' लिखें!
"""

print(f"Testing Sarvam AI TTS pricing...")
print(f"Script character count: {len(test_script)}")

speakers = ["shubh", "amit", "sumit", "ritu", "pooja"]

for speaker in speakers:
    print(f"\nTesting speaker: {speaker}...")
    payload = {
        "text": test_script.strip(),
        "speaker": speaker,
        "model": "bulbul:v3",
        "target_language_code": "hi-IN",
        "pace": 1.15,         # Pushed pace a bit higher for more energy
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
        
        output_path = os.path.join(os.path.dirname(__file__), f"test_sarvam_output_{speaker}.wav")
        with open(output_path, "wb") as f:
            f.write(audio_content)
            
        print(f"Success! Saved to: {output_path}")
    else:
        print(f"Error {response.status_code}: {response.text}")

print("\n--------------------------------------------------")
print("DONE! Check the scripts folder for the generated .wav files.")
