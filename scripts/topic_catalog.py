"""
Topic catalog and dynamic topic selector for Hindu culture & Jyotish stories.
"""
import random
from typing import Dict, List, Any

CATEGORIES = [
    "ज्योतिष कथा",
    "रामायण कथा",
    "श्रीमद्भगवद्गीता",
    "महाभारत रहस्य",
    "शिव पुराण",
    "नक्षत्र एवं ग्रह ज्ञान",
]

TOPIC_CATALOG: List[Dict[str, Any]] = [
    {
        "id": "rahu_ketu_origin",
        "category": "ज्योतिष कथा",
        "title": "राहु और केतु का जन्म",
        "keywords": ["समद्र मंथन", "मोहिनी", "सुदर्शन चक्र", "स्वर्भानु", "सूर्य-चंद्र"],
        "prompt": "Tell the traditional Puranic story of Swarbhanu drinking Amrita during Samudra Manthan, Vishnu cutting his head with Sudarshan Chakra, and how Rahu and Ketu were formed causing eclipses."
    },
    {
        "id": "gita_karma_yoga",
        "category": "श्रीमद्भगवद्गीता",
        "title": "कर्मण्येवाधिकारस्ते का सच्चा अर्थ",
        "keywords": ["अर्जुन", "श्री कृष्ण", "कर्म योग", "कुरुक्षेत्र"],
        "prompt": "Explain the Gita teaching of Karma Yoga from Kurukshetra battlefield when Arjuna surrendered his confusion to Lord Krishna."
    },
    {
        "id": "shiva_third_eye_kama",
        "category": "शिव पुराण",
        "title": "भगवान शिव का तीसरा नेत्र",
        "keywords": ["कामदेव", "तपस्या", "तीसरा नेत्र", "भस्म", "पार्वती"],
        "prompt": "Tell the story of Lord Shiva opening his third eye to burn Kamadeva when he disturbed Shiva's deep meditation, and the spiritual lesson behind it."
    },
    {
        "id": "ramayana_hanuman_sun",
        "category": "रामायण कथा",
        "title": "जब हनुमान जी ने सूर्य को फल समझा",
        "keywords": ["बाल हनुमान", "सूर्य देव", "इंद्र", "वज्र", "हनुमान"],
        "prompt": "Tell the childhood Ramayana story of Lord Hanuman flying to swallow the Sun thinking it was a ripe fruit, Indra's Vajra strike, and the blessings given by all Devas."
    },
    {
        "id": "jyotish_sade_sati_shani",
        "category": "नक्षत्र एवं ग्रह ज्ञान",
        "title": "शनिदेव की साढ़े साती का सच",
        "keywords": ["शनि देव", "साढ़े साती", "न्याय", "कर्म", "शनिश्चर"],
        "prompt": "Explain what Shani Dev's Sade Sati actually is in Vedic Astrology - not a curse, but a period of spiritual purification and karmic balance."
    },
    {
        "id": "mahabharata_karna_kavach",
        "category": "महाभारत रहस्य",
        "title": "कर्ण के कवच कुंडल का दान",
        "keywords": ["सूर्यपुत्र कर्ण", "देवराज इंद्र", "कवच कुंडल", "दानवीर"],
        "prompt": "Tell the Mahabharata story of Danveer Karna giving away his divine Kavach and Kundal to Lord Indra in disguise despite knowing the consequences."
    },
    {
        "id": "jyotish_jupiter_gurus",
        "category": "नक्षत्र एवं ग्रह ज्ञान",
        "title": "गुरु ग्रह और ज्ञान का रहस्य",
        "keywords": ["बृहस्पति", "ज्ञान", "भाग्य", "देवगुरु"],
        "prompt": "Explain the significance of Lord Jupiter (Brihaspati / Guru) in Kundali and how Jupiter brings wisdom, morality, and divine grace."
    },
    {
        "id": "gita_vishvarupa",
        "category": "श्रीमद्भगवद्गीता",
        "title": "श्री कृष्ण का विश्वरूप दर्शन",
        "keywords": ["विश्वरूप", "दिव्य दृष्टि", "अध्याय 11", "कुरुक्षेत्र"],
        "prompt": "Describe Chapter 11 of Bhagavad Gita where Shri Krishna grants divine vision to Arjuna to witness His infinite Cosmic Vishvarupa form."
    }
]

def get_next_topic(used_topic_ids: List[str]) -> Dict[str, Any]:
    """Returns a topic from catalog that has not been recently covered."""
    available = [t for t in TOPIC_CATALOG if t["id"] not in used_topic_ids]
    if not available:
        # Reset if all used
        available = TOPIC_CATALOG
    return random.choice(available)
