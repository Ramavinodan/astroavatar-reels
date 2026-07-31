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
    # Add script_hi if it doesn't exist (SQLite ALTER TABLE)
    try:
        cursor.execute("ALTER TABLE production_logs ADD COLUMN script_hi TEXT")
    except sqlite3.OperationalError:
        pass # Column already exists
    
    conn.commit()
    conn.close()

# Deprecated: No longer needed as topic_catalog.py handles usage tracking internally

def run_pipeline(dry_run: bool = False) -> bool:
    """Executes the full automated video generation and delivery pipeline."""
    load_env()
    print("==========================================================")

    print(f"🚀 AstroAvatar Automated Reels Generator Started [{datetime.datetime.now()}]")
    print("==========================================================")
    
    init_db()
    os.makedirs(OUT_DIR, exist_ok=True)

    try:
        # Step 1: Select Topic from Database
        topic_info = get_next_topic()
        print(f"[Topic Selector] Picked topic: '{topic_info['title']}' ({topic_info['category']})")

        # Step 2: Use Pre-Generated Script JSON
        if not topic_info.get('pregenerated_json'):
            raise ValueError(f"Topic {topic_info['id']} does not have pregenerated_json in the database!")
        import json
        story_data = json.loads(topic_info['pregenerated_json'])
        print(f"[Script Generator] Loaded pre-generated script ({len(story_data.get('script_hi', ''))} chars, {len(story_data.get('slides', []))} slides)")

        # Step 3: Generate AI Images
        print("[Pipeline] Skipping image generation as requested. Waiting for Gemini API integration...")

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
            INSERT INTO production_logs (topic_id, title, category, part_number, total_parts, output_file, duration_sec, status, script_hi)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            story_data["story_id"],
            story_data["title"],
            story_data["category"],
            story_data["part_info"]["current_part"],
            story_data["part_info"]["total_parts"],
            output_mp4,
            props.get("durationInFrames", 0) / 30.0,
            "SUCCESS" if delivered else "UPLOAD_FAILED",
            story_data.get("script_hi", "")
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
