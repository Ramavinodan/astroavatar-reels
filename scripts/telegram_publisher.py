"""
Telegram Publisher & System Monitor for AstroAvatar Reels.
Delivers completed MP4 videos + post captions + hashtags directly to Telegram chat/channel.
Sends instant health reports and failure alerts with stacktraces.
"""
import os
import sys
import json
import requests
from typing import Dict, Any, Optional

def send_video_to_telegram(
    video_path: str,
    story_data: Dict[str, Any],
    bot_token: Optional[str] = None,
    chat_id: Optional[str] = None
) -> bool:
    """Sends completed video MP4 file to Telegram chat/bot with rich formatted caption."""
    token = bot_token or os.getenv("TELEGRAM_BOT_TOKEN")
    cid = chat_id or os.getenv("TELEGRAM_CHAT_ID")

    if not token or not cid:
        print("[Telegram Publisher] TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID not configured. Video ready locally at:", video_path)
        return False

    title = story_data.get("title", "AstroAvatar Reel")
    category = story_data.get("category", "ज्योतिष कथा")
    part_info = story_data.get("part_info", {})
    part_str = f" (भाग {part_info.get('current_part')}/{part_info.get('total_parts')})" if part_info.get("total_parts", 1) > 1 else ""

    caption_text = (
        f"🎬 *{title}{part_str}*\n"
        f"🏷 Category: #{category.replace(' ', '_')}\n"
        f"📱 App: AstroAvatar Daily Dose\n\n"
        f"📜 *Caption:* \n{story_data.get('script_hi', '')[:200]}...\n\n"
        f"✨ #AstroAvatar #VedicAstrology #HinduCulture #Jyotish #Reels #InstaReels #FacebookReels"
    )

    url = f"https://api.telegram.org/bot{token}/sendVideo"

    print(f"[Telegram Publisher] Uploading {os.path.basename(video_path)} to Telegram Chat ({cid})...")

    try:
        with open(video_path, "rb") as video_file:
            files = {"video": video_file}
            data = {
                "chat_id": cid,
                "caption": caption_text,
                "parse_mode": "Markdown",
                "supports_streaming": True
            }
            res = requests.post(url, data=data, files=files, timeout=300)
            if res.status_code == 200 and res.json().get("ok"):
                print("[Telegram Publisher] Video delivered successfully to Telegram!")
                return True
            else:
                print(f"[Telegram Publisher] Delivery failed: {res.text}")
    except Exception as e:
        print(f"[Telegram Publisher] Exception while sending video: {e}")

    return False

def send_alert_to_telegram(
    message: str,
    status: str = "ERROR",
    bot_token: Optional[str] = None,
    chat_id: Optional[str] = None
):
    """Sends system alerts, error logs, or health check status to Telegram."""
    token = bot_token or os.getenv("TELEGRAM_BOT_TOKEN")
    cid = chat_id or os.getenv("TELEGRAM_CHAT_ID")

    if not token or not cid:
        print(f"[System Alert - {status}] {message}")
        return

    icon = "🚨" if status == "ERROR" else "ℹ️" if status == "INFO" else "✅"
    formatted_msg = f"{icon} *AstroAvatar Monitor Alert [{status}]*\n\n{message}"

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    try:
        requests.post(url, json={"chat_id": cid, "text": formatted_msg, "parse_mode": "Markdown"}, timeout=15)
    except Exception as e:
        print(f"[Alert Error] Failed to send Telegram alert: {e}")
