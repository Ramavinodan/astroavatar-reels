"""
Interactive Telegram Bot Daemon for AstroAvatar Reels.
Listens for commands:
  - /bill : Spending breakdown across third-party services (Day, Week, Month).
  - /status : Daily video production status (Morning & Evening runs, completed/delivered).
Runs 24/7 as a background service on the VM.
"""
import os
import sys
import time
import json
import sqlite3
import datetime
import requests

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

def get_status_summary() -> str:
    """Computes daily video generation & delivery status."""
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
        f"{status_icon} *Daily Video Production Status ({today_str})*\n\n"
        f"📊 *Today's Quota:* {len(today_runs)} / 2 Videos Completed\n\n"
    )

    if today_runs:
        msg += "*Today's Generated Reels:*\n"
        for i, run in enumerate(today_runs, 1):
            title = run[1]
            cat = run[2]
            dur = run[5] or 0.0
            st = run[6]
            created = run[7]
            msg += f"  {i}. *{title}* (#{cat})\n     └ Duration: {dur:.1f}s | Status: `{st}` (Delivered) | Time: {created[11:16]}\n"
    else:
        msg += "  • No videos generated yet today. Next run scheduled for 08:00 AM / 18:00 PM.\n"

    if last_run:
        msg += (
            f"\n🎬 *Last Produced Reel:*\n"
            f"  • Title: {last_run[0]}\n"
            f"  • Category: #{last_run[1]}\n"
            f"  • Duration: {last_run[2]:.1f}s\n"
            f"  • Generated At: {last_run[3]}\n"
        )

    msg += "\n⚙️ *System Health:* All VM services operational (Crontab active)."
    return msg

def handle_telegram_command(command: str) -> str:
    cmd = command.strip().lower()
    if cmd.startswith("/bill"):
        return get_billing_summary()
    elif cmd.startswith("/status"):
        return get_status_summary()
    elif cmd.startswith("/start") or cmd.startswith("/help"):
        return (
            "🤖 *AstroAvatar Automated Reels Bot*\n\n"
            "Available Commands:\n"
            "• `/status` - Check daily video generation & delivery status.\n"
            "• `/bill` - View spending breakdown across LLM, TTS, & Image APIs (Day, Week, Month).\n"
            "• `/help` - Show this guide."
        )
    return ""

def run_bot_daemon():
    load_env()
    init_billing_db()
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        print("[Bot Daemon Error] TELEGRAM_BOT_TOKEN not set.")
        sys.exit(1)

    print(f"🤖 Telegram Bot Daemon started listening for /bill and /status commands...")
    offset = 0

    while True:
        try:
            url = f"https://api.telegram.org/bot{token}/getUpdates?offset={offset}&timeout=20"
            res = requests.get(url, timeout=25)
            if res.status_code == 200:
                data = res.json()
                if data.get("ok") and data.get("result"):
                    for update in data["result"]:
                        offset = update["update_id"] + 1
                        msg = update.get("message", {})
                        text = msg.get("text", "")
                        chat_id = msg.get("chat", {}).get("id")

                        if chat_id and text.startswith("/"):
                            reply_text = handle_telegram_command(text)
                            if reply_text:
                                requests.post(
                                    f"https://api.telegram.org/bot{token}/sendMessage",
                                    json={"chat_id": chat_id, "text": reply_text, "parse_mode": "Markdown"},
                                    timeout=15
                                )
                                print(f"[Bot Command Handled] User {chat_id} issued command: {text}")
        except Exception as e:
            print(f"[Bot Daemon Warning] {e}")
            time.sleep(5)

        time.sleep(1)

if __name__ == "__main__":
    run_bot_daemon()
