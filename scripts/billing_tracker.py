"""
Billing & Spending Tracker for AstroAvatar Video Production.
Tracks per-video usage of Sarvam AI LLM, Sarvam AI TTS, AI Image Gen, and Compute.
Computes daily, weekly, and monthly cost breakdowns.
"""
import os
import sqlite3
import datetime
from typing import Dict, Any

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(ROOT_DIR, "production_history.db")

# Approximate Pricing Rates (INR ₹)
# Sarvam LLM (105b): ~₹0.15 per 10,000 characters
SARVAM_LLM_RATE_PER_CHAR = 0.00015 
# Sarvam TTS (bulbul:v2): ~₹0.20 per 1,000 characters
SARVAM_TTS_RATE_PER_CHAR = 0.00020
# Pollinations AI Images: ₹0.00 (Free)
IMAGE_GEN_RATE_PER_IMAGE = 0.0
# Oracle ARM VM Compute: ₹0.00 (Free Tier)
COMPUTE_RATE_PER_VIDEO = 0.0

def init_billing_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS billing_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            story_id TEXT NOT NULL,
            llm_chars INTEGER DEFAULT 0,
            llm_cost_inr REAL DEFAULT 0.0,
            tts_chars INTEGER DEFAULT 0,
            tts_cost_inr REAL DEFAULT 0.0,
            images_count INTEGER DEFAULT 0,
            image_cost_inr REAL DEFAULT 0.0,
            total_cost_inr REAL DEFAULT 0.0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def log_video_cost(story_id: str, script_text: str, slides_count: int) -> Dict[str, Any]:
    init_billing_db()
    
    script_chars = len(script_text)
    llm_cost = script_chars * SARVAM_LLM_RATE_PER_CHAR
    tts_cost = script_chars * SARVAM_TTS_RATE_PER_CHAR
    image_cost = slides_count * IMAGE_GEN_RATE_PER_IMAGE
    total_cost = llm_cost + tts_cost + image_cost

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO billing_logs (story_id, llm_chars, llm_cost_inr, tts_chars, tts_cost_inr, images_count, image_cost_inr, total_cost_inr)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (story_id, script_chars, llm_cost, script_chars, tts_cost, slides_count, image_cost, total_cost))
    conn.commit()
    conn.close()

    return {
        "llm_cost": llm_cost,
        "tts_cost": tts_cost,
        "image_cost": image_cost,
        "total_cost": total_cost
    }

def get_billing_summary() -> str:
    """Computes today, this week, and this month spending split by service."""
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
        "💳 *Third-Party Services Billing Summary*\n\n"
        f"📅 *Today ({today_str}):*\n"
        f"  • Sarvam LLM Scripting: ₹{today_data['llm']:.3f}\n"
        f"  • Sarvam TTS Narration: ₹{today_data['tts']:.3f}\n"
        f"  • AI Image Generation: ₹{today_data['images']:.2f} (Free)\n"
        f"  • Compute/Hosting: ₹0.00 (Free Tier)\n"
        f"  👉 *Today Total:* ₹{today_data['total']:.3f} (~${today_data['total']/86:.4f})\n\n"
        
        f"🗓 *This Week (Last 7 Days):*\n"
        f"  • Videos Generated: {week_data['count']}\n"
        f"  • Sarvam LLM: ₹{week_data['llm']:.3f}\n"
        f"  • Sarvam TTS: ₹{week_data['tts']:.3f}\n"
        f"  👉 *Week Total:* ₹{week_data['total']:.3f} (~${week_data['total']/86:.4f})\n\n"

        f"📆 *This Month (Last 30 Days):*\n"
        f"  • Videos Generated: {month_data['count']}\n"
        f"  • Sarvam LLM: ₹{month_data['llm']:.3f}\n"
        f"  • Sarvam TTS: ₹{month_data['tts']:.3f}\n"
        f"  👉 *Month Total:* ₹{month_data['total']:.3f} (~${month_data['total']/86:.4f})\n\n"
        f"⚡ *Efficiency:* Ultra low-cost AI pipeline (< ₹0.50 per video)."
    )
    return summary
