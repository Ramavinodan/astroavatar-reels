import sqlite3
import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "production_history.db")

batch_data = {
    "parashurama_rage": {
        "story_id": "parashurama_rage",
        "title": "परशुराम का क्रोध",
        "category": "विष्णु पुराण",
        "script_hi": "भगवान परशुराम ने क्षत्रियों का विनाश क्यों किया? परशुराम भगवान विष्णु के छठे अवतार थे। उनके पिता ऋषि जमदग्नि के पास 'कामधेनु' नाम की एक चमत्कारी गाय थी, जो किसी भी इच्छा को पूरा कर सकती थी। एक दिन, सहस्रार्जुन नाम का एक अहंकारी और क्रूर क्षत्रिय राजा ऋषि के आश्रम में आया। उसने बलपूर्वक वह चमत्कारी गाय छीन ली और ऋषि का अपमान किया। जब परशुराम वापस लौटे और उन्हें यह बात पता चली, तो उनका क्रोध भड़क उठा। वे अकेले ही सहस्रार्जुन की राजधानी महिष्मती पहुंच गए और अपने भयंकर 'फरसे' (Parashu) से उस राजा की हज़ार भुजाएँ काट डालीं और उसका वध कर दिया। लेकिन बात यहीं नहीं रुकी। राजा के पुत्रों ने बदला लेने के लिए परशुराम की अनुपस्थिति में उनके पिता ऋषि जमदग्नि की हत्या कर दी। इस जघन्य पाप को देखकर परशुराम ने भयंकर प्रतिज्ञा ली। उन्होंने 21 बार पूरी पृथ्वी को क्रूर और अहंकारी क्षत्रिय राजाओं से विहीन कर दिया। यह अवतार धर्म की रक्षा और अन्याय के खिलाफ भयंकर क्रोध का प्रतीक है।",
        "estimated_speech_sec": 85.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "परशुराम ने क्षत्रियों का विनाश क्यों किया?", "image_prompt": "Lord Parashurama standing fiercely, holding a massive glowing axe (Parashu), intense angry eyes, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "उनके पिता के पास एक चमत्कारी गाय थी।", "image_prompt": "Sage Jamadagni in a peaceful ashram petting the glowing divine wish-fulfilling cow, Kamadhenu, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "सहस्रार्जुन नाम का अहंकारी राजा आश्रम आया।", "image_prompt": "An arrogant king with a thousand arms (Sahasrarjuna) entering the peaceful ashram with his dark army, 9:16", "approx_sec": 5.0},
            {"slide_index": 4, "caption": "उसने बलपूर्वक गाय को छीन लिया।", "image_prompt": "Cruel soldiers forcefully dragging the crying divine cow away from the helpless old sage, 9:16", "approx_sec": 5.0},
            {"slide_index": 5, "caption": "परशुराम का क्रोध भड़क उठा!", "image_prompt": "Lord Parashurama discovering the crime, his eyes burning with intense red fire, lightning cracking behind him, 9:16", "approx_sec": 6.0},
            {"slide_index": 6, "caption": "वे अकेले ही राजा की राजधानी पहुंच गए।", "image_prompt": "Parashurama walking fearlessly alone towards a massive fortress, holding his glowing axe, 9:16", "approx_sec": 5.0},
            {"slide_index": 7, "caption": "अपने फरसे से राजा की हज़ार भुजाएँ काट डालीं।", "image_prompt": "Parashurama spinning his axe at lightning speed, slicing through the thousand arms of the giant king, epic battle, 9:16", "approx_sec": 6.0},
            {"slide_index": 8, "caption": "लेकिन राजा के पुत्रों ने बदला लिया।", "image_prompt": "The evil sons of the king sneaking into the ashram at night, holding bloodied swords, cowardly act, 9:16", "approx_sec": 5.0},
            {"slide_index": 9, "caption": "उन्होंने ऋषि जमदग्नि की हत्या कर दी।", "image_prompt": "Lord Parashurama falling to his knees and weeping loudly while holding the lifeless body of his father, 9:16", "approx_sec": 6.0},
            {"slide_index": 10, "caption": "परशुराम ने भयंकर प्रतिज्ञा ली।", "image_prompt": "Parashurama standing up, raising his axe to the sky, blood on his face, taking a terrible vow, 9:16", "approx_sec": 5.0},
            {"slide_index": 11, "caption": "उन्होंने 21 बार पृथ्वी को क्रूर राजाओं से विहीन किया।", "image_prompt": "Parashurama destroying armies of arrogant kings, chaotic battlefield, justice being served, 9:16", "approx_sec": 6.0},
            {"slide_index": 12, "caption": "यह अन्याय के खिलाफ क्रोध का प्रतीक है।", "image_prompt": "A majestic cinematic portrait of Parashurama as a symbol of divine justice and unstoppable wrath, 9:16", "approx_sec": 5.0}
        ]
    },
    "dhruva_star": {
        "story_id": "dhruva_star",
        "title": "भक्त ध्रुव और ध्रुव तारा",
        "category": "विष्णु पुराण",
        "script_hi": "आसमान में सबसे स्थिर चमकने वाला 'ध्रुव तारा' कौन है? राजा उत्तानपाद की दो पत्नियां थीं - सुनीति और सुरुचि। राजा सुरुचि को अधिक प्रेम करते थे। एक दिन सुनीति का पांच साल का बेटा, ध्रुव, अपने पिता की गोद में बैठने गया। लेकिन सौतेली माँ सुरुचि ने उसे अपमानित करके वहाँ से धक्का दे दिया और कहा, 'राजा की गोद में बैठने के लिए तुझे मेरे गर्भ से जन्म लेना चाहिए था!' रोता हुआ बालक ध्रुव अपनी असली माँ के पास गया। माँ ने कहा, 'अगर तुम्हें कोई सच्चा स्थान दे सकता है, तो वो सिर्फ भगवान विष्णु हैं।' 5 साल का ध्रुव तुरंत जंगल की ओर निकल पड़ा। उसने बिना कुछ खाए-पिए महीनों तक भगवान विष्णु की घोर तपस्या की। उसकी भक्ति की तपिश से पूरा ब्रह्मांड हिलने लगा। अंततः भगवान विष्णु साक्षात प्रकट हुए और उन्होंने उस छोटे से बालक को दर्शन दिए। भगवान ने ध्रुव को आशीर्वाद दिया कि उसे ब्रह्मांड में एक ऐसा स्थान मिलेगा जो कभी नहीं हिलेगा। उसी बालक को आज हम ब्रह्मांड के सबसे स्थिर 'ध्रुव तारे' (Pole Star) के रूप में देखते हैं।",
        "estimated_speech_sec": 90.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "आसमान में सबसे स्थिर 'ध्रुव तारा' कौन है?", "image_prompt": "A magical night sky focusing on one incredibly bright, unmoving star (Pole Star) surrounded by swirling galaxies, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "राजा उत्तानपाद का पांच साल का बेटा था ध्रुव।", "image_prompt": "A cute 5-year-old royal prince, Dhruva, looking lovingly towards his father who is sitting on a throne, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "वह अपने पिता की गोद में बैठने गया।", "image_prompt": "Little Dhruva happily running and trying to climb onto the lap of the King, 9:16", "approx_sec": 5.0},
            {"slide_index": 4, "caption": "सौतेली माँ सुरुचि ने उसे धक्का दे दिया।", "image_prompt": "The evil stepmother angrily pushing the crying little boy away from the throne, arrogant expression, 9:16", "approx_sec": 5.0},
            {"slide_index": 5, "caption": "'तुम्हें मेरे गर्भ से जन्म लेना चाहिए था!'", "image_prompt": "Stepmother pointing a finger down at the crying boy, harsh and insulting, 9:16", "approx_sec": 5.0},
            {"slide_index": 6, "caption": "माँ ने कहा, सच्चा स्थान सिर्फ भगवान दे सकते हैं।", "image_prompt": "Dhruva's real mother wiping his tears and pointing up towards the heavens, instilling faith in him, 9:16", "approx_sec": 6.0},
            {"slide_index": 7, "caption": "5 साल का ध्रुव जंगल की ओर निकल पड़ा।", "image_prompt": "The little brave prince walking alone into a deep, dark, scary forest at night, fearless, 9:16", "approx_sec": 5.0},
            {"slide_index": 8, "caption": "उसने महीनों तक विष्णु की घोर तपस्या की।", "image_prompt": "Little Dhruva sitting in deep meditation on one leg, glowing with a golden spiritual aura, surrounded by wild animals, 9:16", "approx_sec": 6.0},
            {"slide_index": 9, "caption": "उसकी भक्ति से ब्रह्मांड हिलने लगा।", "image_prompt": "Cosmic energy radiating from the small meditating boy, shaking the stars and planets, 9:16", "approx_sec": 5.0},
            {"slide_index": 10, "caption": "अंततः भगवान विष्णु साक्षात प्रकट हुए।", "image_prompt": "Lord Vishnu appearing in all his glory, riding Garuda, glowing beautifully in front of the little boy, 9:16", "approx_sec": 6.0},
            {"slide_index": 11, "caption": "भगवान ने उसे एक अटल स्थान का आशीर्वाद दिया।", "image_prompt": "Lord Vishnu affectionately touching the boy's head, granting him the eternal position in the cosmos, 9:16", "approx_sec": 5.0},
            {"slide_index": 12, "caption": "वही बालक आज 'ध्रुव तारा' है।", "image_prompt": "The glowing boy magically transforming into the eternal, bright Pole star, shining eternally in the sky, 9:16", "approx_sec": 5.0}
        ]
    },
    "satyavan_savitri": {
        "story_id": "satyavan_savitri",
        "title": "सावित्री और सत्यवान की कथा",
        "category": "पौराणिक कथा",
        "script_hi": "सच्चे प्रेम और दृढ़ निश्चय की सबसे बड़ी कहानी - सावित्री और सत्यवान। राजकुमारी सावित्री ने एक गरीब और निर्वासित राजकुमार, सत्यवान को अपने पति के रूप में चुना। लेकिन नारद मुनि ने चेतावनी दी कि सत्यवान की आयु केवल एक वर्ष शेष है। फिर भी, सावित्री नहीं मानीं और खुशी-खुशी विवाह कर लिया। ठीक एक साल बाद, जब सत्यवान जंगल में लकड़ी काट रहे थे, उनके सिर में भयंकर दर्द हुआ और वे सावित्री की गोद में गिर पड़े। उसी समय स्वयं यमराज सत्यवान के प्राण लेने आए। जब यमराज सत्यवान की आत्मा लेकर जाने लगे, तो सावित्री भी उनके पीछे-पीछे चलने लगीं। यमराज ने उन्हें वापस जाने को कहा, लेकिन सावित्री ने धर्म, कर्म और पतिव्रता ज्ञान पर यमराज से ऐसा अद्भुत तर्क-वितर्क किया कि मृत्यु के देवता भी उनके ज्ञान से प्रसन्न हो गए। यमराज ने उन्हें तीन वरदान दिए। अपनी चतुराई से सावित्री ने तीसरे वरदान में 'सौ पुत्रों' का वरदान मांग लिया। वरदान पूरा करने के लिए यमराज को विवश होकर सत्यवान के प्राण वापस लौटाने पड़े। यह कहानी बताती है कि बुद्धि और भक्ति से मृत्यु को भी हराया जा सकता है।",
        "estimated_speech_sec": 90.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "सच्चे प्रेम की सबसे बड़ी कहानी", "image_prompt": "A beautiful ancient Indian princess, Savitri, looking lovingly at a handsome, simple woodcutter prince, Satyavan, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "नारद मुनि ने सावित्री को चेतावनी दी...", "image_prompt": "Sage Narada holding his Veena, warning the princess with a serious expression, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "कि सत्यवान की आयु केवल एक वर्ष शेष है।", "image_prompt": "An hourglass with sand quickly running out, symbolic of limited time and approaching death, 9:16", "approx_sec": 5.0},
            {"slide_index": 4, "caption": "फिर भी सावित्री ने खुशी-खुशी विवाह किया।", "image_prompt": "Savitri and Satyavan getting married simply in a forest hermitage, exchanging flower garlands, 9:16", "approx_sec": 5.0},
            {"slide_index": 5, "caption": "एक साल बाद जंगल में...", "image_prompt": "Satyavan cutting wood with an axe in a dense forest, looking suddenly tired and dizzy, 9:16", "approx_sec": 5.0},
            {"slide_index": 6, "caption": "सत्यवान सावित्री की गोद में गिर पड़े।", "image_prompt": "Satyavan collapsing into Savitri's lap, unconscious, under a large banyan tree, 9:16", "approx_sec": 5.0},
            {"slide_index": 7, "caption": "स्वयं यमराज उनके प्राण लेने आए।", "image_prompt": "Yamaraja, the God of Death, towering over them, holding his noose, glowing with a dark green aura, 9:16", "approx_sec": 6.0},
            {"slide_index": 8, "caption": "सावित्री भी यमराज के पीछे-पीछे चलने लगीं।", "image_prompt": "Yamaraja walking away with a glowing soul, and brave Savitri following him closely on a dark path, 9:16", "approx_sec": 6.0},
            {"slide_index": 9, "caption": "यमराज ने उन्हें वापस जाने को कहा।", "image_prompt": "Yamaraja stopping and holding up his hand, commanding her to turn back, 9:16", "approx_sec": 5.0},
            {"slide_index": 10, "caption": "सावित्री ने धर्म और ज्ञान पर अद्भुत तर्क किया।", "image_prompt": "Savitri speaking confidently and respectfully to Yamaraja, radiating intelligence and devotion, 9:16", "approx_sec": 6.0},
            {"slide_index": 11, "caption": "यमराज को सत्यवान के प्राण लौटाने पड़े।", "image_prompt": "Yamaraja smiling in defeat and releasing the glowing soul back into Satyavan's body, 9:16", "approx_sec": 5.0},
            {"slide_index": 12, "caption": "बुद्धि और भक्ति से मृत्यु को भी हराया जा सकता है।", "image_prompt": "Satyavan waking up in Savitri's arms, the forest glowing with warm sunlight and new life, 9:16", "approx_sec": 5.0}
        ]
    },
    "sita_swayamvar": {
        "story_id": "sita_swayamvar",
        "title": "सीता स्वयंवर और शिव धनुष",
        "category": "रामायण कथा",
        "script_hi": "सीता स्वयंवर में शिव धनुष का क्या रहस्य था? राजा जनक की पुत्री सीता कोई साधारण कन्या नहीं थीं। वे भूमि से प्रकट हुई थीं। बचपन में ही सीता ने खेलते-खेलते भगवान शिव का वो विशाल और अत्यंत भारी धनुष (पिनाक) उठा लिया था, जिसे बड़े-बड़े योद्धा हिला तक नहीं सकते थे। राजा जनक ने तभी यह प्रतिज्ञा ले ली थी कि जो वीर इस शिव धनुष पर प्रत्यंचा (डोरी) चढ़ाएगा, उसी से सीता का विवाह होगा। स्वयंवर के दिन, दुनिया भर के महान राजा और योद्धा आए। अहंकार में चूर बड़े-बड़े राजाओं ने कोशिश की, लेकिन कोई उस धनुष को तिल भर भी हिला नहीं सका। रावण भी इस स्वयंवर में आया था, लेकिन वह भी असफल रहा। तब ऋषि विश्वामित्र के आदेश पर, मर्यादा पुरुषोत्तम श्री राम सभा के बीच आए। राम ने बड़ी ही शालीनता से धनुष को प्रणाम किया। जैसे ही उन्होंने उसे बीच से उठाकर मोड़ा, वह महाविशाल शिव धनुष एक भयंकर गर्जना के साथ टूट गया! इस तरह राम और सीता का अद्भुत मिलन हुआ।",
        "estimated_speech_sec": 90.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "सीता स्वयंवर में शिव धनुष का क्या रहस्य था?", "image_prompt": "A massive, heavy, beautifully carved divine bow of Lord Shiva (Pinaka) resting on a grand pedestal, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "बचपन में सीता ने खेलते हुए वह धनुष उठा लिया था।", "image_prompt": "A little girl, Sita, effortlessly lifting the giant heavy bow with one hand while playing with a ball, 9:16", "approx_sec": 6.0},
            {"slide_index": 3, "caption": "राजा जनक ने प्रतिज्ञा ले ली...", "image_prompt": "King Janaka looking stunned and deciding on the Swayamvar, royal palace setting, 9:16", "approx_sec": 5.0},
            {"slide_index": 4, "caption": "जो इस धनुष पर डोरी चढ़ाएगा, उसी से विवाह होगा।", "image_prompt": "A grand royal assembly (Swayamvar Sabha) filled with arrogant kings looking at the giant bow, 9:16", "approx_sec": 5.0},
            {"slide_index": 5, "caption": "बड़े-बड़े राजाओं ने कोशिश की।", "image_prompt": "Muscular kings struggling and sweating, trying to lift the bow but failing miserably, 9:16", "approx_sec": 5.0},
            {"slide_index": 6, "caption": "कोई उसे तिल भर भी हिला नहीं सका।", "image_prompt": "The bow sitting perfectly still, looking incredibly heavy and immovable, 9:16", "approx_sec": 5.0},
            {"slide_index": 7, "caption": "रावण भी इस स्वयंवर में असफल रहा।", "image_prompt": "The mighty demon king Ravana trying to lift the bow, looking embarrassed and angry as he fails, 9:16", "approx_sec": 5.0},
            {"slide_index": 8, "caption": "तब ऋषि विश्वामित्र के आदेश पर श्री राम आए।", "image_prompt": "Sage Vishwamitra nodding to Lord Rama, Rama standing up calmly with a serene smile, 9:16", "approx_sec": 5.0},
            {"slide_index": 9, "caption": "राम ने बड़ी शालीनता से धनुष को प्रणाम किया।", "image_prompt": "Lord Rama bowing respectfully with folded hands to the divine bow of Lord Shiva, 9:16", "approx_sec": 5.0},
            {"slide_index": 10, "caption": "जैसे ही उन्होंने उसे उठाकर मोड़ा...", "image_prompt": "Lord Rama effortlessly picking up the massive bow and bending it to string it, muscles flexing, 9:16", "approx_sec": 6.0},
            {"slide_index": 11, "caption": "धनुष भयंकर गर्जना के साथ टूट गया!", "image_prompt": "The massive bow snapping perfectly in half, a blinding flash of light and thunder, 9:16", "approx_sec": 5.0},
            {"slide_index": 12, "caption": "इस तरह राम और सीता का अद्भुत मिलन हुआ।", "image_prompt": "Goddess Sita shyly putting the beautiful flower garland (Varmala) around Lord Rama's neck, 9:16", "approx_sec": 5.0}
        ]
    },
    "ahilya_redemption": {
        "story_id": "ahilya_redemption",
        "title": "अहिल्या का उद्धार",
        "category": "रामायण कथा",
        "script_hi": "पत्थर बनी अहिल्या को श्री राम ने कैसे मुक्ति दी? अहिल्या गौतम ऋषि की अत्यंत सुंदर और पवित्र पत्नी थीं। एक दिन जब गौतम ऋषि आश्रम में नहीं थे, तब देवराज इंद्र ने छल से गौतम ऋषि का वेश धारण किया और आश्रम में प्रवेश किया। जब ऋषि वापस आए और उन्होंने यह सब देखा, तो क्रोध में आकर उन्होंने अहिल्या को श्राप दे दिया कि वह एक निर्जीव पत्थर बन जाएगी। अहिल्या रोती रहीं, क्योंकि उनके साथ छल हुआ था। तब ऋषि को दया आई और उन्होंने कहा, 'त्रेता युग में जब साक्षात भगवान विष्णु, श्री राम के अवतार में यहां आएंगे, तब उनके चरणों की धूल से तुम्हारा उद्धार होगा।' हज़ारों वर्षों तक अहिल्या एक पत्थर के रूप में उस वीरान आश्रम में तपस्या करती रहीं। अंततः, जब श्री राम विश्वामित्र जी के साथ जनकपुर जा रहे थे, तब वे उस आश्रम में पहुंचे। जैसे ही श्री राम के पावन चरणों की धूल उस पत्थर पर पड़ी, वह पत्थर एक खूबसूरत स्त्री में बदल गया! अहिल्या ने हाथ जोड़कर भगवान राम की स्तुति की और अंततः उन्हें मोक्ष प्राप्त हुआ।",
        "estimated_speech_sec": 90.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "पत्थर बनी अहिल्या को श्री राम ने कैसे मुक्ति दी?", "image_prompt": "A beautiful ancient Indian woman partially turned into a grey stone statue in a forest, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "अहिल्या गौतम ऋषि की सुंदर पत्नी थीं।", "image_prompt": "A beautiful pious woman praying peacefully in an ancient forest ashram, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "देवराज इंद्र ने छल से ऋषि का वेश धारण किया।", "image_prompt": "Lord Indra looking sneaky, magically transforming his face to look exactly like Sage Gautam, 9:16", "approx_sec": 5.0},
            {"slide_index": 4, "caption": "क्रोधित ऋषि ने अहिल्या को श्राप दे दिया।", "image_prompt": "Sage Gautam furiously throwing holy water from his kamandalu, cursing crying Ahilya, 9:16", "approx_sec": 6.0},
            {"slide_index": 5, "caption": "'तुम एक निर्जीव पत्थर बन जाओगी!'", "image_prompt": "Ahilya slowly turning into a solid grey rock, looking helpless and innocent, 9:16", "approx_sec": 5.0},
            {"slide_index": 6, "caption": "ऋषि ने कहा, राम के चरणों से उद्धार होगा।", "image_prompt": "The sage looking slightly regretful, pointing towards the future, mystical lighting, 9:16", "approx_sec": 5.0},
            {"slide_index": 7, "caption": "हज़ारों वर्षों तक अहिल्या पत्थर बनी रहीं।", "image_prompt": "A solitary rock shaped like a woman covered in moss and vines in an abandoned, dark forest, 9:16", "approx_sec": 5.0},
            {"slide_index": 8, "caption": "अंततः श्री राम उस आश्रम में पहुंचे।", "image_prompt": "Lord Rama and Lakshmana, glowing with divine light, walking into the dark, abandoned ashram, 9:16", "approx_sec": 5.0},
            {"slide_index": 9, "caption": "जैसे ही राम के चरणों की धूल पत्थर पर पड़ी...", "image_prompt": "Lord Rama's glowing lotus feet touching the edge of the stone, magical golden dust floating, 9:16", "approx_sec": 6.0},
            {"slide_index": 10, "caption": "पत्थर एक खूबसूरत स्त्री में बदल गया!", "image_prompt": "The grey stone shattering with a blinding light, revealing the pure and radiant Ahilya, 9:16", "approx_sec": 5.0},
            {"slide_index": 11, "caption": "अहिल्या ने हाथ जोड़कर स्तुति की।", "image_prompt": "Ahilya kneeling on the ground with folded hands, crying tears of joy, looking up at Lord Rama, 9:16", "approx_sec": 5.0},
            {"slide_index": 12, "caption": "और अंततः उन्हें मोक्ष प्राप्त हुआ।", "image_prompt": "A glowing soul rising towards the heavens, feeling completely free and liberated, 9:16", "approx_sec": 5.0}
        ]
    }
}

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

count = 0
for topic_id, json_data in batch_data.items():
    json_string = json.dumps(json_data, ensure_ascii=False)
    cursor.execute("UPDATE topic_catalog SET pregenerated_json = ? WHERE id = ?", (json_string, topic_id))
    count += 1

conn.commit()
conn.close()
print(f"Successfully generated and injected {count} full JSON scripts (Batch 5) into the local database!")
