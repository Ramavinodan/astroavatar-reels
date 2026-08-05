"""
Topic catalog dynamic selector connected to SQLite database.
"""
import sqlite3
import os
import json
from typing import Dict, Any

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "production_history.db")

def get_next_topic() -> Dict[str, Any]:
    """Returns an unused topic from the topic_catalog database table."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    # Get a random unused topic that has a pre-generated script
    cursor.execute("SELECT * FROM topic_catalog WHERE used_count = 0 AND pregenerated_json IS NOT NULL ORDER BY RANDOM() LIMIT 1")
    row = cursor.fetchone()
    
    if not row:
        # If all used, pick the oldest used one that has a pre-generated script
        cursor.execute("SELECT * FROM topic_catalog WHERE pregenerated_json IS NOT NULL ORDER BY used_count ASC, created_at ASC LIMIT 1")
        row = cursor.fetchone()
        
    if not row:
        conn.close()
        raise Exception("Topic catalog is completely empty! Please scrape more topics.")
        
    topic_data = dict(row)
    
    # Increment used count
    cursor.execute("UPDATE topic_catalog SET used_count = used_count + 1 WHERE id = ?", (topic_data["id"],))
    conn.commit()
    conn.close()
    
    # Parse keywords back to list
    if isinstance(topic_data.get("keywords"), str):
        try:
            topic_data["keywords"] = json.loads(topic_data["keywords"])
        except:
            topic_data["keywords"] = [k.strip() for k in topic_data["keywords"].split(",")]
            
    return topic_data
