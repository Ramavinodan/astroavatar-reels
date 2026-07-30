import os, requests, time, sys
sys.path.append("scripts")
from pipeline_runner import load_env
load_env()
token = os.environ["TELEGRAM_BOT_TOKEN"]
print("=== LISTENING ===")
offset = 0
for i in range(10):
    res = requests.get(f"https://api.telegram.org/bot{token}/getUpdates?offset={offset}&timeout=2")
    data = res.json()
    print("Poll:", data)
    if data.get("result"):
        for u in data["result"]:
            offset = u["update_id"] + 1
    time.sleep(1)
