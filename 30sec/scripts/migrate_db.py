import sqlite3
import os
import json
from topic_catalog import TOPIC_CATALOG

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "production_history.db")

def migrate():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Create the new topic_catalog table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS topic_catalog (
            id TEXT PRIMARY KEY,
            category TEXT NOT NULL,
            title TEXT NOT NULL,
            keywords TEXT NOT NULL,
            prompt TEXT NOT NULL,
            source_url TEXT,
            used_count INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Pre-populate with existing topics if not present
    for t in TOPIC_CATALOG:
        cursor.execute("SELECT id FROM topic_catalog WHERE id=?", (t["id"],))
        if not cursor.fetchone():
            keywords_json = json.dumps(t["keywords"], ensure_ascii=False)
            cursor.execute("""
                INSERT INTO topic_catalog (id, category, title, keywords, prompt, source_url, used_count)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (t["id"], t["category"], t["title"], keywords_json, t["prompt"], "hardcoded", 0))
            
    conn.commit()
    print(f"Migrated {len(TOPIC_CATALOG)} topics to database successfully.")
    conn.close()

if __name__ == "__main__":
    migrate()
