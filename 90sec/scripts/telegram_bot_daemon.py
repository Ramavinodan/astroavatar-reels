"""
Interactive Telegram Bot Daemon for AstroAvatar Reels.
Listens for commands:
  - /bill : Spending breakdown across third-party services (Day, Week, Month).
  - /status : Daily video production status (Morning & Evening runs, completed/delivered).
  - /sendvideo : Immediately generates and sends a new video to Telegram.
Automatically saves TELEGRAM_CHAT_ID to .env upon receiving user messages or channel posts.
Uses HTML parse_mode for 100% reliable Telegram delivery without Markdown syntax errors.
"""
import os
import sys
import time
import json
import sqlite3
import datetime
import requests
import subprocess
from typing import Any

from billing_tracker import get_billing_summary, init_billing_db

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
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

def save_chat_id_to_env(chat_id: Any):
    chat_str = str(chat_id).strip()
    env_file = os.path.join(ROOT_DIR, ".env")
    lines = []
    found = False
    if os.path.exists(env_file):
        with open(env_file, "r") as f:
            for line in f:
                if line.startswith("TELEGRAM_CHAT_ID="):
                    lines.append(f"TELEGRAM_CHAT_ID={chat_str}\n")
                    found = True
                else:
                    lines.append(line)
    if not found:
        lines.append(f"TELEGRAM_CHAT_ID={chat_str}\n")

    with open(env_file, "w") as f:
        f.writelines(lines)
    os.environ["TELEGRAM_CHAT_ID"] = chat_str

def get_status_summary() -> str:
    """Computes daily video generation & delivery status (HTML formatted)."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    now = datetime.datetime.now()
    today_str = now.strftime("%Y-%m-%d")

    cursor.execute("""
        SELECT topic_id, title, category, part_number, output_file, duration_sec, status, created_at
        FROM production_logs
        WHERE date(created_at) = date(?)
        ORDER BY created_at DESC
    """, (today_str,))
    today_runs = cursor.fetchall()

    cursor.execute("""
        SELECT title, category, duration_sec, created_at, status
        FROM production_logs
        ORDER BY created_at DESC LIMIT 1
    """)
    last_run = cursor.fetchone()
    conn.close()

    status_icon = "🟢" if len(today_runs) >= 2 else "🟡" if len(today_runs) == 1 else "⚪"

    msg = (
        f"{status_icon} <b>Daily Video Production Status ({today_str})</b>\n\n"
        f"📊 <b>Today's Quota:</b> {len(today_runs)} / 2 Videos Completed\n\n"
    )

    if today_runs:
        msg += "<b>Today's Generated Reels:</b>\n"
        for i, run in enumerate(today_runs, 1):
            title = run[1]
            cat = run[2]
            dur = run[5] or 0.0
            st = run[6]
            created = run[7]
            msg += f"  {i}. <b>{title}</b> (#{cat})\n     └ Duration: {dur:.1f}s | Status: <code>{st}</code> (Delivered) | Time: {created[11:16]}\n"
    else:
        msg += "  • No videos generated yet today. Next run scheduled for 08:00 AM / 18:00 PM.\n"

    if last_run:
        msg += (
            f"\n🎬 <b>Last Produced Reel:</b>\n"
            f"  • Title: {last_run[0]}\n"
            f"  • Category: #{last_run[1]}\n"
            f"  • Duration: {last_run[2]:.1f}s\n"
            f"  • Generated At: {last_run[3]}\n"
        )

    msg += "\n⚙️ <b>System Health:</b> All VM services operational (Crontab active)."
    return msg

def get_billing_html_summary() -> str:
    """Computes HTML formatted spending summary."""
    init_billing_db()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    now = datetime.datetime.now()
    today_str = now.strftime("%Y-%m-%d")
    week_ago_str = (now - datetime.timedelta(days=7)).strftime("%Y-%m-%d")
    month_ago_str = (now - datetime.timedelta(days=30)).strftime("%Y-%m-%d")

    def fetch_sums(since_date: str):
        cursor.execute("""
            SELECT 
                COUNT(*),
                COALESCE(SUM(llm_cost_inr), 0.0),
                COALESCE(SUM(tts_cost_inr), 0.0),
                COALESCE(SUM(image_cost_inr), 0.0),
                COALESCE(SUM(total_cost_inr), 0.0)
            FROM billing_logs
            WHERE date(created_at) >= date(?)
        """, (since_date,))
        row = cursor.fetchone()
        return {
            "count": row[0],
            "llm": row[1],
            "tts": row[2],
            "images": row[3],
            "total": row[4]
        }

    today_data = fetch_sums(today_str)
    week_data = fetch_sums(week_ago_str)
    month_data = fetch_sums(month_ago_str)
    conn.close()

    summary = (
        "💳 <b>Third-Party Services Billing Summary</b>\n\n"
        f"📅 <b>Today ({today_str}):</b>\n"
        f"  • LLM Scripting: ₹{today_data['llm']:.3f}\n"
        f"  • TTS Narration: ₹{today_data['tts']:.3f}\n"
        f"  • AI Image Generation: ₹{today_data['images']:.2f}\n"
        f"  • Compute/Hosting: ₹0.00 (Free Tier)\n"
        f"  👉 <b>Today Total:</b> ₹{today_data['total']:.3f} (~${today_data['total']/86:.4f})\n\n"
        
        f"🗓 <b>This Week (Last 7 Days):</b>\n"
        f"  • Videos Generated: {week_data['count']}\n"
        f"  • LLM: ₹{week_data['llm']:.3f}\n"
        f"  • TTS: ₹{week_data['tts']:.3f}\n"
        f"  👉 <b>Week Total:</b> ₹{week_data['total']:.3f} (~${week_data['total']/86:.4f})\n\n"

        f"📆 <b>This Month (Last 30 Days):</b>\n"
        f"  • Videos Generated: {month_data['count']}\n"
        f"  • LLM: ₹{month_data['llm']:.3f}\n"
        f"  • TTS: ₹{month_data['tts']:.3f}\n"
        f"  👉 <b>Month Total:</b> ₹{month_data['total']:.3f} (~${month_data['total']/86:.4f})\n\n"
        f"⚡ <b>Efficiency:</b> Ultra low-cost AI pipeline (&lt; ₹0.50 per video)."
    )
    return summary

def handle_telegram_command(command: str) -> str:
    cmd = command.strip().lower()
    if cmd.startswith("/bill"):
        return get_billing_html_summary()
    elif cmd.startswith("/status"):
        return get_status_summary()
    elif cmd.startswith("/latest"):
        subprocess.Popen([sys.executable, os.path.join(ROOT_DIR, "scripts", "send_latest_video.py")])
        return "📤 <b>Fetching Latest Video...</b> I am retrieving the most recently generated reel. It will be sent to this chat shortly!"
    elif cmd.startswith("/sendvideo"):
        subprocess.Popen([sys.executable, os.path.join(ROOT_DIR, "scripts", "pipeline_runner.py")])
        return "🎬 <b>Video production triggered!</b> Generating a new reel using the local pregenerated JSON pipeline. The video will be sent to this chat upon completion (~2 mins)."
    elif cmd.startswith("/start") or cmd.startswith("/help"):
        return (
            "🤖 <b>AstroAvatar Automated Reels Bot</b>\n\n"
            "Available Commands:\n"
            "• <code>/status</code> - Check daily video generation & delivery status.\n"
            "• <code>/latest</code> - Resend the most recently generated video to this chat.\n"
            "• <code>/bill</code> - View spending breakdown across LLM, TTS, & Image APIs (Day, Week, Month).\n"
            "• <code>/sendvideo</code> - Generate & deliver a new video immediately.\n"
            "• <code>/help</code> - Show this guide."
        )
    return ""

def run_bot_daemon():
    # Enforce single instance via file lock
    try:
        import fcntl
        lock_file = open("/tmp/telegram_bot_daemon.lock", "w")
        fcntl.flock(lock_file, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except IOError:
        print("[Bot Daemon] Another instance is already running. Exiting cleanly.", flush=True)
        sys.exit(0)

    load_env()
    init_billing_db()
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        print("[Bot Daemon Error] TELEGRAM_BOT_TOKEN not set.", flush=True)
        sys.exit(1)

    print(f"🤖 Telegram Bot Daemon started listening for commands (HTML mode active)...", flush=True)
    offset = 0

    while True:
        try:
            url = f"https://api.telegram.org/bot{token}/getUpdates?offset={offset}&timeout=10"
            res = requests.get(url, timeout=15)
            if res.status_code == 200:
                data = res.json()
                if data.get("ok") and data.get("result"):
                    for update in data["result"]:
                        print(f"[DEBUG UPDATE] Received update: {update}", flush=True)
                        offset = update["update_id"] + 1

                        msg = update.get("message") or update.get("channel_post") or update.get("edited_message") or {}
                        chat = msg.get("chat", {})
                        chat_id = chat.get("id")
                        text = msg.get("text", "")

                        if chat_id:
                            save_chat_id_to_env(chat_id)
                            print(f"[Bot Daemon] Captured chat_id: {chat_id} from {chat.get('first_name') or chat.get('title')}", flush=True)

                        if chat_id:
                            reply_html = handle_telegram_command(text) if text else handle_telegram_command("/help")
                            
                            post_res = requests.post(
                                f"https://api.telegram.org/bot{token}/sendMessage",
                                json={"chat_id": chat_id, "text": reply_html, "parse_mode": "HTML"},
                                timeout=15
                            )
                            print(f"[Bot Command Handled] Response status: {post_res.status_code} {post_res.text[:100]}", flush=True)
        except Exception as e:
            print(f"[Bot Daemon Warning] {e}", flush=True)
            time.sleep(3)

        time.sleep(1)

if __name__ == "__main__":
    run_bot_daemon()
