import os
import sys
import sqlite3
import datetime
from telegram_publisher import send_video_to_telegram, send_alert_to_telegram
from pipeline_runner import DB_PATH, load_env

def send_latest():
    load_env()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT output_file, title, category, part_number, total_parts FROM production_logs WHERE status='SUCCESS' ORDER BY created_at DESC LIMIT 1")
    row = cursor.fetchone()
    conn.close()

    if not row:
        send_alert_to_telegram("No videos found in the production history today.", status="INFO")
        return

    output_file, title, category, part_number, total_parts = row
    
    if not os.path.exists(output_file):
        send_alert_to_telegram(f"The latest video file was not found on disk: {output_file}", status="ERROR")
        return

    story_data = {
        "title": title,
        "category": category,
        "part_info": {
            "current_part": part_number,
            "total_parts": total_parts
        },
        "script_hi": "(This is a requested resend of the latest automatically generated AstroAvatar Reel.)"
    }

    send_alert_to_telegram(f"Fetching and uploading the latest generated video: {title}...", status="INFO")
    delivered = send_video_to_telegram(output_file, story_data)
    if delivered:
        print("Latest video delivered successfully.")
    else:
        print("Failed to deliver latest video.")

if __name__ == "__main__":
    send_latest()
