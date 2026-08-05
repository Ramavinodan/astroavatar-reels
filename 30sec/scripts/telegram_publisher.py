"""
Telegram Publisher & System Monitor for AstroAvatar Reels.
Delivers completed MP4 videos + post captions + hashtags directly to Telegram chat/channel.
Sends instant health reports and failure alerts with stacktraces.
"""
import os
import sys
import json
import requests
import subprocess
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

    gen_date = story_data.get("generated_at")
    gen_date_str = f"🕒 <b>Generated On:</b> {gen_date}\n" if gen_date else ""

    caption_text = (
        f"🎬 <b>{title}{part_str}</b>\n"
        f"🏷 Category: #{category.replace(' ', '_')}\n"
        f"📱 App: AstroAvatar Daily Dose\n"
        f"{gen_date_str}\n"
        f"📜 <b>Caption:</b> \n{story_data.get('script_hi', '')[:200]}...\n\n"
        f"✨ #AstroAvatar #VedicAstrology #HinduCulture #Jyotish #Reels #InstaReels #FacebookReels"
    )

    url = f"https://api.telegram.org/bot{token}/sendVideo"

    # Auto compress video if >48MB (Telegram Bot API 50MB limit)
    final_upload_path = video_path
    if os.path.exists(video_path) and os.path.getsize(video_path) > 48 * 1024 * 1024:
        compressed_path = video_path.replace(".mp4", "_compressed.mp4")
        print(f"[Telegram Publisher] Video file size is {os.path.getsize(video_path)//(1024*1024)} MB (>48MB limit). Compressing using FFmpeg...")
        try:
            subprocess.run([
                "ffmpeg", "-y", "-i", video_path,
                "-vcodec", "libx264", "-crf", "26", "-preset", "fast",
                "-acodec", "aac", "-b:a", "128k",
                compressed_path
            ], capture_output=True, check=True)
            if os.path.exists(compressed_path) and os.path.getsize(compressed_path) > 0:
                final_upload_path = compressed_path
                print(f"[Telegram Publisher] Compressed video ready ({os.path.getsize(compressed_path)//(1024*1024)} MB)")
        except Exception as e:
            print(f"[Telegram Publisher Warning] Compression failed: {e}")

    print(f"[Telegram Publisher] Uploading {os.path.basename(final_upload_path)} to Telegram Chat ({cid})...")

    try:
        with open(final_upload_path, "rb") as video_file:

            files = {"video": video_file}
            data = {
                "chat_id": cid,
                "caption": caption_text,
                "parse_mode": "HTML",
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
    formatted_msg = f"{icon} <b>AstroAvatar Monitor Alert [{status}]</b>\n\n{message}"

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    try:
        requests.post(url, json={"chat_id": cid, "text": formatted_msg, "parse_mode": "HTML"}, timeout=15)
    except Exception as e:
        print(f"[Alert Error] Failed to send Telegram alert: {e}")

