import sqlite3
import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "production_history.db")

batch_data = {
    "dadhichi_bones": {
        "story_id": "dadhichi_bones",
        "title": "महर्षि दधीचि का अस्थि दान",
        "category": "शिव पुराण",
        "script_hi": "महर्षि दधीचि का अस्थि दान क्यों ब्रह्मांड का सबसे बड़ा त्याग माना जाता है? एक बार वृत्रासुर नाम के एक भयंकर असुर ने स्वर्ग पर कब्ज़ा कर लिया। उसने ऐसा वरदान पाया था कि उसे दुनिया के किसी भी लकड़ी, पत्थर, या साधारण धातु के अस्त्र से नहीं मारा जा सकता था। इंद्र देव हताश होकर भगवान विष्णु के पास गए। विष्णु जी ने कहा कि वृत्रासुर को केवल एक ऐसे वज्र से मारा जा सकता है, जो किसी महान तपस्वी की हड्डियों से बना हो। सभी देवता महर्षि दधीचि के पास पहुँचे, जो अपनी घोर तपस्या के कारण अत्यंत पवित्र और शक्तिशाली हो चुके थे। जब इंद्र ने उनसे उनकी हड्डियाँ माँगी, तो दधीचि ने बिना एक पल की हिचकिचाहट के मुस्कुराते हुए अपना शरीर त्याग दिया। देवताओं ने उनकी रीढ़ की हड्डी से 'वज्र' का निर्माण किया। इसी अजेय वज्र से इंद्र ने वृत्रासुर का वध किया और सृष्टि की रक्षा की। महर्षि दधीचि का यह बलिदान सिखाता है कि समाज और धर्म की रक्षा के लिए किया गया निःस्वार्थ त्याग ही सबसे महान है।",
        "estimated_speech_sec": 85.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "महर्षि दधीचि का अस्थि दान सबसे बड़ा त्याग क्यों है?", "image_prompt": "An ancient glowing sage sitting in deep meditation, radiating pure spiritual golden light, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "वृत्रासुर नाम के असुर ने स्वर्ग पर कब्ज़ा कर लिया।", "image_prompt": "A terrifying giant demon, Vritrasura, sitting on the throne of Heaven (Swarga), dark storm clouds, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "उसे किसी साधारण अस्त्र से नहीं मारा जा सकता था।", "image_prompt": "Swords, arrows, and spears shattering into pieces upon hitting the demon's impenetrable skin, 9:16", "approx_sec": 5.0},
            {"slide_index": 4, "caption": "इंद्र देव भगवान विष्णु के पास गए।", "image_prompt": "Lord Indra looking defeated, kneeling before Lord Vishnu who is resting on the cosmic serpent Shesha, 9:16", "approx_sec": 6.0},
            {"slide_index": 5, "caption": "विष्णु जी ने एक अनोखा उपाय बताया।", "image_prompt": "Lord Vishnu speaking, glowing with divine blue light, explaining the secret weapon to Indra, 9:16", "approx_sec": 5.0},
            {"slide_index": 6, "caption": "वृत्रासुर को केवल तपस्वी की हड्डियों से बने वज्र से मारा जा सकता था।", "image_prompt": "A glowing, magical, indestructible weapon (Vajra) made of pure white divine bone, floating in light, 9:16", "approx_sec": 6.0},
            {"slide_index": 7, "caption": "देवता महर्षि दधीचि के पास पहुँचे।", "image_prompt": "The gods folding hands and pleading before Sage Dadhichi in his peaceful forest ashram, 9:16", "approx_sec": 5.0},
            {"slide_index": 8, "caption": "इंद्र ने उनसे उनकी हड्डियाँ माँगी।", "image_prompt": "Lord Indra looking shameful but desperate, asking the ultimate sacrifice from the calm sage, 9:16", "approx_sec": 5.0},
            {"slide_index": 9, "caption": "दधीचि ने मुस्कुराते हुए अपना शरीर त्याग दिया।", "image_prompt": "Sage Dadhichi meditating, his soul leaving his body as a glowing golden orb, peaceful and fearless, 9:16", "approx_sec": 6.0},
            {"slide_index": 10, "caption": "देवताओं ने उनकी रीढ़ की हड्डी से 'वज्र' बनाया।", "image_prompt": "Vishwakarma (the divine architect) forging the glowing Vajra weapon from the sage's spine, magical sparks, 9:16", "approx_sec": 5.0},
            {"slide_index": 11, "caption": "इसी वज्र से वृत्रासुर का वध हुआ।", "image_prompt": "Lord Indra flying in the sky and striking the giant demon Vritrasura with the blinding Vajra, epic battle, 9:16", "approx_sec": 5.0},
            {"slide_index": 12, "caption": "धर्म की रक्षा के लिए किया गया त्याग ही महान है।", "image_prompt": "A glowing lotus blooming over a pile of bones, symbolizing eternal glory through sacrifice, 9:16", "approx_sec": 6.0}
        ]
    },
    "markandeya_mrityunjaya": {
        "story_id": "markandeya_mrityunjaya",
        "title": "मार्कण्डेय और महामृत्युंजय मंत्र",
        "category": "शिव पुराण",
        "script_hi": "महामृत्युंजय मंत्र की उत्पत्ति कैसे हुई? ऋषि मृकंडु को कोई संतान नहीं थी। उन्होंने भगवान शिव की तपस्या की। शिव जी ने उन्हें दो विकल्प दिए: या तो एक मूर्ख पुत्र जो 100 साल जिएगा, या एक अत्यंत ज्ञानी पुत्र जिसकी आयु केवल 16 वर्ष होगी। ऋषि ने ज्ञानी पुत्र को चुना, जिसका नाम मार्कण्डेय रखा गया। मार्कण्डेय बचपन से ही शिव के परम भक्त थे। जब वे 16 वर्ष के हुए, तो यमराज उनके प्राण लेने आए। मार्कण्डेय उस समय शिवलिंग की पूजा कर रहे थे। यमराज का पाश देखकर वे डर गए और शिवलिंग से लिपट गए। उन्होंने मृत्यु को हराने वाला महामृत्युंजय मंत्र जपना शुरू कर दिया। जैसे ही यमराज ने अपना पाश शिवलिंग पर फेंका, शिवलिंग फट गया और उसमें से साक्षात भगवान शिव भयंकर रूप में प्रकट हुए! शिव जी ने क्रोध में आकर यमराज पर त्रिशूल तान दिया। महादेव ने मार्कण्डेय को हमेशा 16 वर्ष के रहने और अमरता का वरदान दिया। तभी से महामृत्युंजय मंत्र को मृत्यु पर विजय पाने वाला सबसे शक्तिशाली मंत्र माना जाता है।",
        "estimated_speech_sec": 90.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "महामृत्युंजय मंत्र की उत्पत्ति कैसे हुई?", "image_prompt": "A glowing ancient palm leaf manuscript with glowing Sanskrit mantras, mystical blue lighting, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "ऋषि मृकंडु ने शिव की तपस्या की।", "image_prompt": "An ancient sage meditating deeply in a forest, Lord Shiva appearing in front of him in a glowing form, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "उन्होंने 16 वर्ष की आयु वाले ज्ञानी पुत्र को चुना।", "image_prompt": "A beautiful, intelligent young boy dressed as a young sage, holding a prayer bead necklace (Rudraksha), 9:16", "approx_sec": 5.0},
            {"slide_index": 4, "caption": "मार्कण्डेय शिव के परम भक्त थे।", "image_prompt": "Young boy Markandeya devotedly offering water and bel leaves to a dark stone Shiva Linga, 9:16", "approx_sec": 5.0},
            {"slide_index": 5, "caption": "जब वे 16 वर्ष के हुए, यमराज प्राण लेने आए।", "image_prompt": "Yamaraja, the God of Death, riding a giant black water buffalo, looking terrifying, holding a noose, 9:16", "approx_sec": 6.0},
            {"slide_index": 6, "caption": "यमराज का पाश देखकर मार्कण्डेय शिवलिंग से लिपट गए।", "image_prompt": "Terrified boy Markandeya hugging the Shiva Linga tightly, eyes closed, chanting mantras loudly, 9:16", "approx_sec": 6.0},
            {"slide_index": 7, "caption": "उन्होंने महामृत्युंजय मंत्र जपना शुरू किया।", "image_prompt": "Glowing cosmic sound waves of the mantra expanding from the boy, hitting the dark presence of death, 9:16", "approx_sec": 5.0},
            {"slide_index": 8, "caption": "यमराज ने अपना पाश शिवलिंग पर फेंका।", "image_prompt": "Yamaraja throwing his glowing dark lasso (Paash) which accidentally wraps around the Shiva Linga, 9:16", "approx_sec": 5.0},
            {"slide_index": 9, "caption": "तभी शिवलिंग फट गया!", "image_prompt": "The Shiva Linga bursting open with intense blinding white and blue light, cosmic energy exploding, 9:16", "approx_sec": 5.0},
            {"slide_index": 10, "caption": "भगवान शिव भयंकर रूप में प्रकट हुए।", "image_prompt": "Furious Lord Shiva emerging from the Linga, holding his glowing Trishul and pointing it directly at Yamaraja, 9:16", "approx_sec": 6.0},
            {"slide_index": 11, "caption": "शिव जी ने मार्कण्डेय को अमरता का वरदान दिया।", "image_prompt": "Lord Shiva calming down, placing his hand on Markandeya's head, granting him eternal youth and immortality, 9:16", "approx_sec": 6.0},
            {"slide_index": 12, "caption": "यह मंत्र मृत्यु पर विजय पाने वाला है।", "image_prompt": "A glowing third eye symbol radiating protective energy, representing the ultimate triumph over death, 9:16", "approx_sec": 5.0}
        ]
    },
    "kurma_avatar": {
        "story_id": "kurma_avatar",
        "title": "कूर्म अवतार और मंदार पर्वत",
        "category": "विष्णु पुराण",
        "script_hi": "भगवान विष्णु को कूर्म (कछुए) का अवतार क्यों लेना पड़ा? महर्षि दुर्वासा के एक श्राप के कारण जब देवराज इंद्र और सभी देवता अपनी शक्ति खो बैठे, तब असुरों ने स्वर्ग पर कब्ज़ा कर लिया। अपनी शक्ति वापस पाने के लिए, विष्णु जी ने देवताओं को असुरों के साथ मिलकर 'समुद्र मंथन' करने की सलाह दी, ताकि वे अमरता का अमृत पा सकें। इस महामंथन के लिए मंदार पर्वत को मथनी (मथने वाला डंडा) और वासुकि नाग को रस्सी बनाया गया। लेकिन जैसे ही मंदार पर्वत को समुद्र में डाला गया, वह अपने भारी वजन के कारण डूबने लगा। तब मंथन को सफल बनाने के लिए, भगवान विष्णु ने एक विशालकाय कूर्म (कछुए) का रूप धारण किया और समुद्र की गहराई में जाकर मंदार पर्वत को अपनी मजबूत पीठ पर उठा लिया। उनकी पीठ पर यह पर्वत हजारों वर्षों तक घूमता रहा, और अंततः समुद्र से अमृत समेत 14 अनमोल रत्न बाहर निकले।",
        "estimated_speech_sec": 80.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "विष्णु जी को कूर्म अवतार क्यों लेना पड़ा?", "image_prompt": "A massive glowing divine Tortoise (Kurma) swimming gracefully in the deep cosmic ocean, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "दुर्वासा मुनि के श्राप से देवता शक्तिहीन हो गए थे।", "image_prompt": "Angry Sage Durvasa throwing a garland of flowers to the ground, cursing a shocked Lord Indra, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "विष्णु जी ने समुद्र मंथन करने की सलाह दी।", "image_prompt": "Lord Vishnu instructing gods and demons to cooperate, glowing cosmic ocean in the background, 9:16", "approx_sec": 5.0},
            {"slide_index": 4, "caption": "मंथन के लिए मंदार पर्वत को मथनी बनाया गया।", "image_prompt": "A colossal mountain (Mandara) being lifted by gods and demons using magic and strength, 9:16", "approx_sec": 5.0},
            {"slide_index": 5, "caption": "और वासुकि नाग को रस्सी।", "image_prompt": "The giant multi-headed serpent Vasuki wrapping himself around the mountain like a massive rope, 9:16", "approx_sec": 5.0},
            {"slide_index": 6, "caption": "लेकिन मंदार पर्वत समुद्र में डूबने लगा!", "image_prompt": "The huge mountain sinking fast into the dark, swirling ocean waters, causing panic among the gods, 9:16", "approx_sec": 6.0},
            {"slide_index": 7, "caption": "तब भगवान विष्णु ने विशाल कूर्म का रूप लिया।", "image_prompt": "Lord Vishnu magically transforming into a gigantic, indestructible sea turtle deep underwater, 9:16", "approx_sec": 5.0},
            {"slide_index": 8, "caption": "उन्होंने पर्वत को अपनी पीठ पर उठा लिया।", "image_prompt": "The massive Kurma avatar underwater, holding the gigantic sinking mountain securely on its glowing shell, 9:16", "approx_sec": 6.0},
            {"slide_index": 9, "caption": "हजारों वर्षों तक पर्वत उनकी पीठ पर घूमता रहा।", "image_prompt": "The mountain spinning rapidly on the turtle's shell, creating giant cosmic whirlpools, 9:16", "approx_sec": 5.0},
            {"slide_index": 10, "caption": "अंततः समुद्र से 14 अनमोल रत्न बाहर निकले।", "image_prompt": "Glowing magical treasures emerging from the churning waters, lighting up the sky, 9:16", "approx_sec": 5.0},
            {"slide_index": 11, "caption": "और देवताओं को अमृत प्राप्त हुआ।", "image_prompt": "Lord Dhanvantari emerging from the ocean holding the golden pot (Kalash) filled with Amrita (nectar), 9:16", "approx_sec": 5.0},
            {"slide_index": 12, "caption": "यही था कूर्म अवतार का उद्देश्य।", "image_prompt": "A majestic portrait of Lord Vishnu standing above the giant Kurma, radiating cosmic peace, 9:16", "approx_sec": 5.0}
        ]
    },
    "narasimha_hiranyakashipu": {
        "story_id": "narasimha_hiranyakashipu",
        "title": "नृसिंह अवतार और प्रह्लाद",
        "category": "विष्णु पुराण",
        "script_hi": "भगवान विष्णु को आधा नर और आधा सिंह (शेर) क्यों बनना पड़ा? हिरण्यकशिपु नाम के असुर राजा ने ब्रह्मा जी से एक अजीब वरदान मांगा था। उसने मांगा कि वह न दिन में मरे न रात में, न घर के अंदर मरे न बाहर, न अस्त्र से मरे न शस्त्र से, और न किसी इंसान से मरे न जानवर से। इस वरदान के अहंकार में उसने खुद को भगवान घोषित कर दिया और अपने ही विष्णु भक्त बेटे, प्रह्लाद को जान से मारने की कोशिशें करने लगा। जब हिरण्यकशिपु ने प्रह्लाद से पूछा कि 'क्या तेरा भगवान इस खंभे में भी है?' और उसने खंभे पर गदा मारी, तो उस खंभे को फाड़कर भगवान नृसिंह प्रकट हुए! नृसिंह का रूप न पूरा इंसान था न पूरा जानवर। उन्होंने गोधूलि वेला (न दिन न रात) में, महल की दहलीज पर (न अंदर न बाहर), अपने नाखुनों से (न अस्त्र न शस्त्र), हिरण्यकशिपु का पेट फाड़कर उसका वध कर दिया। भगवान अपने भक्त की रक्षा के लिए किसी भी सीमा तक जा सकते हैं।",
        "estimated_speech_sec": 90.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "विष्णु जी को आधा नर और आधा सिंह क्यों बनना पड़ा?", "image_prompt": "A terrifying silhouette of a being that is half man and half lion, glowing angry eyes in the dark, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "हिरण्यकशिपु ने एक अजीब वरदान मांगा था।", "image_prompt": "Demon king Hiranyakashipu laughing arrogantly, surrounded by a magical protective shield from Lord Brahma, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "उसका बेटा प्रह्लाद विष्णु का परम भक्त था।", "image_prompt": "Little boy Prahlad sitting peacefully with folded hands, chanting prayers, glowing with pure devotion, 9:16", "approx_sec": 5.0},
            {"slide_index": 4, "caption": "अहंकारी राजा ने प्रह्लाद को मारने की कोशिश की।", "image_prompt": "Hiranyakashipu threatening his little son with a sword, while Prahlad remains completely fearless, 9:16", "approx_sec": 5.0},
            {"slide_index": 5, "caption": "'क्या तेरा भगवान इस खंभे में भी है?'", "image_prompt": "The furious demon king pointing his mace towards a massive stone pillar in the grand palace, 9:16", "approx_sec": 5.0},
            {"slide_index": 6, "caption": "खंभे को फाड़कर भगवान नृसिंह प्रकट हुए!", "image_prompt": "The massive stone pillar exploding, Lord Narasimha (half-man half-lion) roaring fiercely, epic divine power, 9:16", "approx_sec": 6.0},
            {"slide_index": 7, "caption": "यह रूप न इंसान था, न जानवर।", "image_prompt": "Close up of Lord Narasimha's fierce lion face and powerful human torso, radiating intense fiery energy, 9:16", "approx_sec": 5.0},
            {"slide_index": 8, "caption": "गोधूलि वेला (न दिन न रात)।", "image_prompt": "The sky outside the palace showing twilight, the sun exactly setting at the horizon, 9:16", "approx_sec": 5.0},
            {"slide_index": 9, "caption": "दहलीज पर (न अंदर न बाहर)।", "image_prompt": "Lord Narasimha dragging the terrified demon king to the exact threshold (doorway) of the palace, 9:16", "approx_sec": 5.0},
            {"slide_index": 10, "caption": "नाखुनों से (न अस्त्र न शस्त्र) वध किया।", "image_prompt": "Lord Narasimha sitting on the threshold, tearing open the chest of the demon with his bare sharp claws, 9:16", "approx_sec": 6.0},
            {"slide_index": 11, "caption": "प्रह्लाद ने उन्हें शांत किया।", "image_prompt": "Little Prahlad lovingly placing a garland around the neck of the still angry but softening Lord Narasimha, 9:16", "approx_sec": 5.0},
            {"slide_index": 12, "caption": "भगवान भक्त के लिए कोई भी रूप ले सकते हैं।", "image_prompt": "Lord Narasimha licking Prahlad's face affectionately like a mother lion, divine love and protection, 9:16", "approx_sec": 5.0}
        ]
    },
    "vamana_bali": {
        "story_id": "vamana_bali",
        "title": "वामन अवतार और राजा बलि",
        "category": "विष्णु पुराण",
        "script_hi": "भगवान विष्णु ने एक छोटे से ब्राह्मण का अवतार क्यों लिया? प्रह्लाद के पोते, असुर राजा बलि ने अपनी शक्तियों से स्वर्ग पर कब्ज़ा कर लिया था। यद्यपि बलि एक असुर था, लेकिन वह बहुत दानी और धर्मात्मा था। देवताओं को उनका स्वर्ग वापस दिलाने के लिए, विष्णु जी ने 'वामन' (बौने ब्राह्मण) का रूप धारण किया और राजा बलि के यज्ञ में पहुंच गए। बलि ने उनसे कुछ भी मांगने को कहा। वामन ने मुस्कुराकर केवल अपने पैरों से नापने भर 'तीन पग ज़मीन' मांगी। बलि के गुरु शुक्राचार्य वामन की असलियत समझ गए और उन्होंने बलि को रोका, लेकिन बलि अपने वचन से नहीं मुकरा। जैसे ही बलि ने संकल्प पूरा किया, वामन का आकार अचानक से बढ़ने लगा! उन्होंने अपने पहले पग में पूरी धरती नाप ली, और दूसरे पग में स्वर्ग और पूरा ब्रह्मांड नाप लिया। जब तीसरे पग के लिए कोई जगह नहीं बची, तो बलि ने विनम्रता से अपना सिर आगे कर दिया। वामन ने अपना पैर उसके सिर पर रखा और उसे पाताल लोक का राजा बना दिया।",
        "estimated_speech_sec": 90.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "विष्णु जी ने वामन अवतार क्यों लिया?", "image_prompt": "A cute, small dwarf Brahmin boy (Vamana) holding an umbrella made of leaves, smiling purely, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "असुर राजा बलि ने स्वर्ग पर कब्ज़ा कर लिया था।", "image_prompt": "Demon King Bali, grand and heavily jeweled, sitting powerfully on Indra's throne in heaven, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "लेकिन वह बहुत दानी और धर्मात्मा था।", "image_prompt": "King Bali generously giving away gold and cows to priests in a grand fire sacrifice (Yagna), 9:16", "approx_sec": 5.0},
            {"slide_index": 4, "caption": "वामन भगवान बलि के यज्ञ में पहुंचे।", "image_prompt": "The dwarf Brahmin Vamana walking into the grand royal sacrifice area, radiating divine simplicity, 9:16", "approx_sec": 5.0},
            {"slide_index": 5, "caption": "उन्होंने केवल तीन पग (कदम) ज़मीन मांगी।", "image_prompt": "Vamana pointing to his small feet and asking the giant King Bali for three paces of land, 9:16", "approx_sec": 6.0},
            {"slide_index": 6, "caption": "गुरु शुक्राचार्य ने बलि को चेतावनी दी।", "image_prompt": "Guru Shukracharya whispering anxiously into Bali's ear, warning him about Lord Vishnu's trick, 9:16", "approx_sec": 5.0},
            {"slide_index": 7, "caption": "लेकिन बलि अपने वचन से पीछे नहीं हटा।", "image_prompt": "King Bali proudly pouring sacred water from a pot to finalize the vow, ignoring his guru, 9:16", "approx_sec": 5.0},
            {"slide_index": 8, "caption": "तभी वामन का आकार विशाल होने लगा!", "image_prompt": "Vamana magically growing in size, expanding beyond the clouds, towering over the entire kingdom, 9:16", "approx_sec": 6.0},
            {"slide_index": 9, "caption": "पहले पग में पूरी धरती नाप ली।", "image_prompt": "One gigantic foot of Lord Vishnu covering the entire globe of the Earth, cosmic scale, 9:16", "approx_sec": 5.0},
            {"slide_index": 10, "caption": "दूसरे पग में स्वर्ग और ब्रह्मांड नाप लिया।", "image_prompt": "The second foot reaching up into the galaxies, touching the highest heavens, epic scale, 9:16", "approx_sec": 5.0},
            {"slide_index": 11, "caption": "तीसरे पग के लिए बलि ने अपना सिर आगे कर दिया।", "image_prompt": "King Bali kneeling humbly with folded hands, offering his head for the giant glowing foot to step on, 9:16", "approx_sec": 6.0},
            {"slide_index": 12, "caption": "भगवान ने उसे पाताल का राजा बना दिया।", "image_prompt": "Lord Vishnu blessing Bali in Patala Loka (underworld), surrounded by glowing crystals and wealth, 9:16", "approx_sec": 5.0}
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
print(f"Successfully generated and injected {count} full JSON scripts (Batch 4) into the local database!")
