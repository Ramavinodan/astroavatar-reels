import sqlite3
import os
import json

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "production_history.db")

new_stories = [
    {
        "id": "shiva_neelkanth_origin",
        "category": "शिव पुराण",
        "title": "भगवान शिव ने विष क्यों पिया?",
        "keywords": ["समुद्र मंथन", "हलाहल विष", "नीलकंठ", "महादेव"],
        "prompt": "Tell the story of Samudra Manthan where the deadly Halahal poison emerged, and Lord Shiva drank it to save the universe, earning the name Neelkanth."
    },
    {
        "id": "jyotish_mars_manglik",
        "category": "ज्योतिष कथा",
        "title": "मंगल दोष का सच्चा रहस्य",
        "keywords": ["मंगल दोष", "मांगलिक", "विवाह", "ज्योतिष"],
        "prompt": "Explain the Jyotish concept of Manglik Dosh (Mars defect in Kundali), debunking the extreme fears around it and explaining how it represents excess fire and energy that needs balancing."
    },
    {
        "id": "mahabharata_abhimanyu_chakravyuh",
        "category": "महाभारत रहस्य",
        "title": "अभिमन्यु और चक्रव्यूह का ज्ञान",
        "keywords": ["अभिमन्यु", "चक्रव्यूह", "सुभद्रा", "अर्जुन", "महाभारत"],
        "prompt": "Narrate the tragic but heroic story of Abhimanyu learning how to enter the Chakravyuh while in his mother Subhadra's womb, but not learning how to exit because she fell asleep."
    }
]

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

for t in new_stories:
    cursor.execute("SELECT id FROM topic_catalog WHERE id=?", (t["id"],))
    if not cursor.fetchone():
        keywords_json = json.dumps(t["keywords"], ensure_ascii=False)
        cursor.execute("""
            INSERT INTO topic_catalog (id, category, title, keywords, prompt, source_url, used_count)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (t["id"], t["category"], t["title"], keywords_json, t["prompt"], "antigravity_agent", 0))

conn.commit()
print("Successfully inserted 3 new manually curated stories into the database.")
conn.close()
