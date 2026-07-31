import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "production_history.db")
SQL_OUT_PATH = os.path.join(os.path.dirname(__file__), "pregenerated_scripts.sql")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("SELECT id, pregenerated_json FROM topic_catalog WHERE pregenerated_json IS NOT NULL")
rows = cursor.fetchall()

with open(SQL_OUT_PATH, "w", encoding="utf-8") as f:
    f.write("-- Pre-generated JSON scripts for topic_catalog\n\n")
    for row in rows:
        topic_id = row[0]
        json_data = row[1].replace("'", "''") # Escape single quotes for SQL
        f.write(f"UPDATE topic_catalog SET pregenerated_json = '{json_data}' WHERE id = '{topic_id}';\n")

conn.close()
print(f"Dumped {len(rows)} pre-generated scripts to {SQL_OUT_PATH}")
