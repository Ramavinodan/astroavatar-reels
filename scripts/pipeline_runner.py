"""
Central Pipeline Orchestrator for 100% Automated AstroAvatar Video Production.
Runs twice daily via Cron.
Executes: Script Gen -> Image Gen -> TTS & Audio Align -> Remotion Render -> Telegram Delivery.
Logs production history in SQLite DB to prevent duplicate topics.
"""
import os
import sys
import json
import sqlite3
import datetime
import subprocess
import traceback
from typing import Dict, Any

from topic_catalog import get_next_topic
from story_generator import generate_story_llm
from image_generator import generate_slide_images
from tts_generator import generate_narration_audio
from telegram_publisher import send_video_to_telegram, send_alert_to_telegram

from billing_tracker import log_video_cost

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REMOTION_DIR = os.path.join(ROOT_DIR, "reels-factory")
PUBLIC_DIR = os.path.join(REMOTION_DIR, "public")
OUT_DIR = os.path.join(REMOTION_DIR, "out")
DB_PATH = os.path.join(ROOT_DIR, "production_history.db")

def load_env():
    env_file = os.path.join(ROOT_DIR, ".env")
    if os.path.exists(env_file):
        with open(env_file, "r") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    os.environ[k.strip()] = v.strip()

def init_db():

    """Initializes SQLite database for tracking video history and multi-part series."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS production_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic_id TEXT NOT NULL,
            title TEXT NOT NULL,
            category TEXT NOT NULL,
            part_number INTEGER DEFAULT 1,
            total_parts INTEGER DEFAULT 1,
            output_file TEXT NOT NULL,
            duration_sec REAL,
            status TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def get_used_topic_ids():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT topic_id FROM production_logs WHERE status='SUCCESS'")
    rows = cursor.fetchall()
    conn.close()
    return [r[0] for r in rows]

def run_pipeline(dry_run: bool = False) -> bool:
    """Executes the full automated video generation and delivery pipeline."""
    load_env()
    print("==========================================================")

    print(f"🚀 AstroAvatar Automated Reels Generator Started [{datetime.datetime.now()}]")
    print("==========================================================")
    
    init_db()
    os.makedirs(OUT_DIR, exist_ok=True)

    try:
        # Step 1: Select Topic
        used_ids = get_used_topic_ids()
        topic_info = get_next_topic(used_ids)
        print(f"[Topic Selector] Picked topic: '{topic_info['title']}' ({topic_info['category']})")

        # Step 2: Generate Script & Story JSON
        llm_key = os.getenv("SARVAM_API_KEY") or os.getenv("OPENAI_API_KEY") or os.getenv("DEEPSEEK_API_KEY")
        provider = "sarvam" if os.getenv("SARVAM_API_KEY") else "openai"
        story_data = generate_story_llm(topic_info, api_key=llm_key, provider=provider)
        print(f"[Script Generator] Script generated ({len(story_data.get('script_hi', ''))} chars, {len(story_data.get('slides', []))} slides)")

        # Step 3: Generate AI Images
        slides_with_images = generate_slide_images(story_data, PUBLIC_DIR)
        story_data["slides"] = slides_with_images

        # Step 4: Generate TTS & Compute Audio Timestamps
        audio_info = generate_narration_audio(story_data, PUBLIC_DIR)
        story_data["slides"] = audio_info["slides"]

        # Step 5: Prepare Remotion JSON Props
        props = {
          "narrationFile": audio_info["relative_audio_path"],
          "welcomeFile": "narration/brand/welcome-daily-dose-hi-mixed.wav",
          "endCardFile": "end_card.mp4",
          "category": story_data.get("category", "ज्योतिष कथा"),
          "title": story_data.get("title", "राहु-केतु की कहानी"),
          "introFrames": 120,
          "storyFrames": audio_info["story_frames"],
          "endCardFrames": 150,
          "slides": story_data["slides"]
        }

        timestamp_str = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        props_file = os.path.join(OUT_DIR, f"props_{timestamp_str}.json")
        output_mp4 = os.path.join(OUT_DIR, f"reel_{story_data['story_id']}_{timestamp_str}.mp4")

        with open(props_file, "w", encoding="utf-8") as f:
            json.dump(props, f, ensure_ascii=False, indent=2)

        print(f"[Remotion Props] Prepared props -> {props_file}")

        if dry_run:
            print("[Dry Run] Pipeline completed test validation successfully.")
            return True

        # Step 6: Render Remotion Video via CLI
        print(f"[Remotion Render] Rendering DynamicSlideshow to {output_mp4}...")
        render_cmd = [
            "npx", "remotion", "render", "DynamicSlideshow", output_mp4,
            f"--props={props_file}",
            "--crf=24",
            "--jpeg-quality=80",
            "--concurrency=2",
            "--gl=angle"
        ]
        
        res = subprocess.run(render_cmd, cwd=REMOTION_DIR, capture_output=True, text=True)
        if res.returncode != 0:
            # Fallback render command without --gl flag
            fallback_cmd = [
                "npx", "remotion", "render", "DynamicSlideshow", output_mp4,
                f"--props={props_file}",
                "--crf=24",
                "--jpeg-quality=80",
                "--concurrency=2"
            ]
            res = subprocess.run(fallback_cmd, cwd=REMOTION_DIR, capture_output=True, text=True, check=True)



        print(f"[Remotion Render] Render complete! Video saved: {output_mp4} ({os.path.getsize(output_mp4)//1024} KB)")

        # Step 7: Send to Telegram
        delivered = send_video_to_telegram(output_mp4, story_data)

        # Step 8: Log to DB
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO production_logs (topic_id, title, category, part_number, total_parts, output_file, duration_sec, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            story_data["story_id"],
            story_data["title"],
            story_data["category"],
            story_data.get("part_info", {}).get("current_part", 1),
            story_data.get("part_info", {}).get("total_parts", 1),
            output_mp4,
            audio_info["audio_duration_sec"],
            "SUCCESS"
        ))
        conn.commit()
        conn.close()

        # Step 9: Log Billing Usage
        log_video_cost(story_data["story_id"], story_data["script_hi"], len(story_data["slides"]))

        print(f"🎉 Pipeline Execution Complete Successfully! [{datetime.datetime.now()}]")
        return True


    except Exception as e:
        err_msg = f"Pipeline execution failed: {str(e)}\n\nTraceback:\n{traceback.format_exc()}"
        print(f"[ERROR] {err_msg}")
        send_alert_to_telegram(err_msg, status="ERROR")
        return False

if __name__ == "__main__":
    is_dry = "--test" in sys.argv or "--dry-run" in sys.argv
    run_pipeline(dry_run=is_dry)
