import sqlite3
import os
import json

db = sqlite3.connect('production_history.db')
c = db.cursor()
c.execute('SELECT id, pregenerated_json FROM topic_catalog WHERE pregenerated_json IS NOT NULL ORDER BY rowid ASC')
rows = c.fetchall()

for row in rows:
    topic_id, data = row
    if not os.path.exists(f'reels-factory/public/pregenerated_images/{topic_id}'):
        print(f"NEXT_TOPIC: {topic_id}")
        print(data)
        break
