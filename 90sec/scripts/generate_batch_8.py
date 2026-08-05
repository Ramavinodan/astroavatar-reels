import sqlite3
import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "production_history.db")

batch_data = {
    "draupadi_swayamvar": {
        "story_id": "draupadi_swayamvar",
        "title": "द्रौपदी स्वयंवर और मछली की आंख",
        "category": "महाभारत रहस्य",
        "script_hi": "द्रौपदी के स्वयंवर की शर्त इतनी कठिन क्यों थी? पांचाल नरेश राजा द्रुपद ने अपनी पुत्री द्रौपदी का विवाह दुनिया के सबसे सर्वश्रेष्ठ धनुर्धर से करने का संकल्प लिया था। इसलिए उन्होंने स्वयंवर में एक अत्यंत कठिन प्रतियोगिता रखी। शर्त यह थी कि राजा को पानी के कुंड में देखकर, ऊपर घूम रहे यंत्र में लगी एक लकड़ी की मछली की आंख पर तीर मारना था! और वह भी शिव जी के एक अत्यंत भारी धनुष से। बड़े-बड़े राजा और राजकुमार आए, लेकिन कोई उस भारी धनुष की प्रत्यंचा (डोरी) तक नहीं चढ़ा सका। दुर्योधन और कर्ण भी वहां थे, लेकिन कर्ण को द्रौपदी ने यह कहकर रोक दिया कि वह एक 'सूत पुत्र' से विवाह नहीं करेगी। तब एक गरीब ब्राह्मण के भेष में अर्जुन सभा के बीच आए। अर्जुन ने बड़ी ही आसानी से धनुष उठाया, डोरी चढ़ाई, और नीचे पानी में देखते हुए ठीक मछली की आंख में तीर मार दिया! राजा द्रुपद की शर्त पूरी हुई और द्रौपदी ने अर्जुन के गले में वरमाला डाल दी। यह कथा एकाग्रता और लक्ष्य पर ध्यान केंद्रित करने की सबसे बड़ी मिसाल है।",
        "estimated_speech_sec": 95.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "द्रौपदी स्वयंवर की शर्त इतनी कठिन क्यों थी?", "image_prompt": "Princess Draupadi looking stunningly beautiful, standing in a grand royal assembly holding a flower garland (varmala), 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "राजा द्रुपद को सर्वश्रेष्ठ धनुर्धर चाहिए था।", "image_prompt": "King Drupada announcing the difficult archery challenge, pointing towards a complex wooden mechanism high above, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "शर्त थी: पानी में देखकर मछली की आंख भेदनी है।", "image_prompt": "A golden wooden fish attached to a fast spinning wheel high up, and a calm pool of reflecting water directly below it, 9:16", "approx_sec": 6.0},
            {"slide_index": 4, "caption": "धनुष अत्यंत भारी और दिव्य था।", "image_prompt": "A massive, heavy, beautifully carved divine bow placed in the center of the arena, glowing slightly, 9:16", "approx_sec": 5.0},
            {"slide_index": 5, "caption": "बड़े-बड़े राजा धनुष हिला तक नहीं सके।", "image_prompt": "Arrogant, muscular kings struggling, sweating, and failing to even string the heavy bow, crowd laughing, 9:16", "approx_sec": 5.0},
            {"slide_index": 6, "caption": "कर्ण को द्रौपदी ने रोक दिया।", "image_prompt": "Karna confidently picking up the bow, but Draupadi raising her hand to stop him, refusing a 'Suta Putra', 9:16", "approx_sec": 6.0},
            {"slide_index": 7, "caption": "तब ब्राह्मण के भेष में अर्जुन आए।", "image_prompt": "Arjuna, disguised as a simple but strong Brahmin, walking calmly to the center of the arena, 9:16", "approx_sec": 5.0},
            {"slide_index": 8, "caption": "अर्जुन ने आसानी से धनुष उठा लिया।", "image_prompt": "Arjuna lifting the heavy bow effortlessly and stringing it with a confident smile, muscles flexing, 9:16", "approx_sec": 5.0},
            {"slide_index": 9, "caption": "नीचे पानी में देखते हुए निशाना लगाया।", "image_prompt": "Arjuna looking intensely only at the reflection of the spinning fish in the calm pool of water below, 9:16", "approx_sec": 6.0},
            {"slide_index": 10, "caption": "और ठीक मछली की आंख में तीर मार दिया!", "image_prompt": "A glowing arrow flying straight up and perfectly piercing the eye of the wooden fish on the spinning wheel, 9:16", "approx_sec": 5.0},
            {"slide_index": 11, "caption": "द्रौपदी ने अर्जुन के गले में वरमाला डाल दी।", "image_prompt": "Draupadi happily putting the beautiful flower garland around the neck of the disguised Arjuna, 9:16", "approx_sec": 5.0},
            {"slide_index": 12, "caption": "यह एकाग्रता की सबसे बड़ी मिसाल है।", "image_prompt": "A close up of Arjuna's intensely focused eyes, reflecting the target, showing ultimate concentration, 9:16", "approx_sec": 5.0}
        ]
    },
    "draupadi_cheerharan": {
        "story_id": "draupadi_cheerharan",
        "title": "द्रौपदी चीरहरण और कृष्ण की कृपा",
        "category": "महाभारत रहस्य",
        "script_hi": "द्रौपदी चीरहरण के समय भगवान कृष्ण ने द्रौपदी की लाज कैसे बचाई? महाभारत के सबसे शर्मनाक अध्याय में, युधिष्ठिर ने जुए के खेल में अपना सब कुछ हारने के बाद अपनी पत्नी द्रौपदी को भी दांव पर लगा दिया और हार गए। दुर्योधन के आदेश पर, दुशासन द्रौपदी को बालों से घसीटता हुआ भरी सभा में ले आया। दुर्योधन ने द्रौपदी को निर्वस्त्र करने का आदेश दिया। भीष्म, द्रोण, धृतराष्ट्र और द्रौपदी के पांचों पति (पांडव) सिर झुकाए चुपचाप बैठे रहे; किसी ने भी उस अन्याय का विरोध नहीं किया। जब द्रौपदी ने देखा कि दुनिया का कोई भी इंसान उसकी मदद नहीं कर रहा है, तो उसने अपने दोनों हाथ आसमान की ओर उठा लिए और अपने 'सखा' (मित्र) भगवान श्री कृष्ण को पुकारा। 'हे गोविंद! हे द्वारकाधीश! मेरी लाज बचाओ!' जैसे ही दुशासन ने द्रौपदी की साड़ी खींचनी शुरू की, एक चमत्कार हुआ! कृष्ण की कृपा से साड़ी की लंबाई अपने आप बढ़ने लगी। दुशासन साड़ी खींचते-खींचते थक कर पसीने से लथपथ होकर गिर पड़ा, लेकिन द्रौपदी का वस्त्र खत्म नहीं हुआ। इस घटना ने साबित कर दिया कि जब इंसान पूरी तरह से भगवान के प्रति समर्पित हो जाता है, तो भगवान उसकी लाज ज़रूर रखते हैं।",
        "estimated_speech_sec": 95.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "चीरहरण के समय कृष्ण ने द्रौपदी को कैसे बचाया?", "image_prompt": "A dramatic ancient Indian royal court, dark shadows, tension in the air, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "युधिष्ठिर जुए में द्रौपदी को हार गए।", "image_prompt": "Yudhishthira looking defeated and ashamed at the gambling table, Shakuni smiling wickedly with dice in hand, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "दुशासन द्रौपदी को बालों से घसीट लाया।", "image_prompt": "Evil Dushasana forcefully dragging a crying Princess Draupadi by her long dark hair into the court, 9:16", "approx_sec": 6.0},
            {"slide_index": 4, "caption": "दुर्योधन ने उसे निर्वस्त्र करने का आदेश दिया।", "image_prompt": "Arrogant Duryodhana sitting on his throne, pointing a commanding finger and laughing cruelly, 9:16", "approx_sec": 5.0},
            {"slide_index": 5, "caption": "सभी बड़े योद्धा सिर झुकाए बैठे रहे।", "image_prompt": "Bhishma and Dronacharya sitting with their heads bowed down in deep shame, helpless and silent, 9:16", "approx_sec": 5.0},
            {"slide_index": 6, "caption": "किसी ने भी अन्याय का विरोध नहीं किया।", "image_prompt": "The five Pandava brothers sitting quietly, looking totally broken, humiliated, and bound by duty, 9:16", "approx_sec": 5.0},
            {"slide_index": 7, "caption": "द्रौपदी ने अपने 'सखा' कृष्ण को पुकारा।", "image_prompt": "Draupadi letting go of her saree, raising both hands towards the sky with tears in her eyes, calling out to Krishna, 9:16", "approx_sec": 6.0},
            {"slide_index": 8, "caption": "'हे गोविंद! मेरी लाज बचाओ!'", "image_prompt": "A glowing divine vision of Lord Krishna sitting peacefully in Dwarka, hearing her desperate call, 9:16", "approx_sec": 5.0},
            {"slide_index": 9, "caption": "जैसे ही दुशासन ने साड़ी खींचनी शुरू की...", "image_prompt": "Dushasana aggressively pulling the end of Draupadi's beautiful red saree, cruel expression, 9:16", "approx_sec": 5.0},
            {"slide_index": 10, "caption": "साड़ी की लंबाई अपने आप बढ़ने लगी!", "image_prompt": "A magical endless stream of colorful fabric (saree) appearing from nowhere, forming a huge pile on the floor, 9:16", "approx_sec": 6.0},
            {"slide_index": 11, "caption": "दुशासन खींचते-खींचते थक कर गिर पड़ा।", "image_prompt": "Dushasana collapsing on the floor from extreme exhaustion, surrounded by a mountain of endless saree fabric, 9:16", "approx_sec": 6.0},
            {"slide_index": 12, "caption": "भगवान अपने भक्तों की लाज ज़रूर रखते हैं।", "image_prompt": "Draupadi standing untouched, safe, wrapped safely in the divine fabric, radiating strength and pure devotion, 9:16", "approx_sec": 5.0}
        ]
    },
    "eklavya_gurudakshina": {
        "story_id": "eklavya_gurudakshina",
        "title": "एकलव्य की गुरुदक्षिणा",
        "category": "महाभारत रहस्य",
        "script_hi": "एकलव्य ने अपना अंगूठा गुरु द्रोणाचार्य को क्यों दे दिया? एकलव्य एक भील (आदिवासी) राजकुमार था, जो दुनिया का सर्वश्रेष्ठ धनुर्धर बनना चाहता था। वह गुरु द्रोणाचार्य के पास धनुर्विद्या सीखने गया, लेकिन द्रोण ने उसे सिखाने से मना कर दिया क्योंकि उन्होंने केवल क्षत्रियों (राजकुमारों) को पढ़ाने की शपथ ली थी। निराश होने के बजाय, एकलव्य जंगल लौट आया और उसने मिट्टी से गुरु द्रोण की एक मूर्ति बनाई। उस मूर्ति को ही अपना गुरु मानकर उसने कड़ी मेहनत से अभ्यास किया और अर्जुन से भी बेहतर धनुर्धर बन गया। एक दिन द्रोणाचार्य और पांडव उसी जंगल में आए। एक कुत्ते के भौंकने से परेशान होकर, एकलव्य ने उसके मुंह में बिना उसे चोट पहुंचाए, तीरों से उसका मुंह भर दिया। यह अद्भुत कौशल देखकर द्रोणाचार्य हैरान रह गए। जब उन्हें पता चला कि यह उनका ही 'एकलव्य' है, तो उन्हें डर लगा कि अर्जुन दुनिया का सर्वश्रेष्ठ धनुर्धर नहीं बन पाएगा (जैसा उन्होंने अर्जुन से वादा किया था)। गुरुदक्षिणा के रूप में, द्रोणाचार्य ने क्रूरता से एकलव्य के दाएँ हाथ का अंगूठा मांग लिया! बिना अंगूठे के तीर चलाना असंभव था। लेकिन महान एकलव्य ने बिना किसी झिझक के अपना अंगूठा काटकर द्रोण के चरणों में रख दिया। उसका यह बलिदान उसे इतिहास का सबसे महान शिष्य बनाता है।",
        "estimated_speech_sec": 100.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "एकलव्य ने अपना अंगूठा क्यों काटा?", "image_prompt": "A determined tribal boy, Ekalavya, holding a simple bow and arrow in a dense ancient Indian forest, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "द्रोणाचार्य ने उसे सिखाने से मना कर दिया।", "image_prompt": "Guru Dronacharya rejecting the young tribal boy, surrounded by royal princes (Pandavas) in an ashram, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "एकलव्य ने मिट्टी से द्रोण की मूर्ति बनाई।", "image_prompt": "Ekalavya lovingly carving a statue of Guru Dronacharya out of wet clay, placing it under a large tree, 9:16", "approx_sec": 5.0},
            {"slide_index": 4, "caption": "मूर्ति को गुरु मानकर अभ्यास किया।", "image_prompt": "Ekalavya practicing archery fiercely in the rain in front of the clay statue, showing intense dedication, 9:16", "approx_sec": 6.0},
            {"slide_index": 5, "caption": "वह अर्जुन से भी बेहतर धनुर्धर बन गया।", "image_prompt": "Ekalavya shooting multiple arrows perfectly at once with a glowing aura of skill and mastery, 9:16", "approx_sec": 5.0},
            {"slide_index": 6, "caption": "एक दिन उसने एक कुत्ते का मुंह तीरों से भर दिया।", "image_prompt": "A dog with its mouth perfectly filled with arrows, unharmed but unable to bark, a display of absolute precision, 9:16", "approx_sec": 6.0},
            {"slide_index": 7, "caption": "द्रोणाचार्य यह अद्भुत कौशल देखकर हैरान रह गए।", "image_prompt": "Guru Dronacharya and Arjuna looking completely shocked and amazed at the dog with arrows, 9:16", "approx_sec": 5.0},
            {"slide_index": 8, "caption": "उन्हें डर लगा कि अर्जुन हार जाएगा।", "image_prompt": "Dronacharya looking worried, remembering his promise to Arjuna that he would be the best archer in the world, 9:16", "approx_sec": 5.0},
            {"slide_index": 9, "caption": "गुरुदक्षिणा के रूप में उन्होंने अंगूठा मांग लिया!", "image_prompt": "Dronacharya strictly asking for Ekalavya's right thumb, pointing at the boy's hand with a cruel demand, 9:16", "approx_sec": 6.0},
            {"slide_index": 10, "caption": "बिना अंगूठे के तीर चलाना असंभव था।", "image_prompt": "A close up of a hand holding an arrow string, highlighting the importance of the right thumb for shooting, 9:16", "approx_sec": 5.0},
            {"slide_index": 11, "caption": "एकलव्य ने बिना झिझक अंगूठा काट दिया।", "image_prompt": "Ekalavya calmly taking out a knife and cutting his own right thumb, blood dripping, absolutely fearless, 9:16", "approx_sec": 6.0},
            {"slide_index": 12, "caption": "वह इतिहास का सबसे महान शिष्य बन गया।", "image_prompt": "The bloody thumb placed reverently at the feet of the clay statue, a symbol of ultimate sacrifice and respect, 9:16", "approx_sec": 5.0}
        ]
    },
    "bhishma_vow": {
        "story_id": "bhishma_vow",
        "title": "भीष्म प्रतिज्ञा",
        "category": "महाभारत रहस्य",
        "script_hi": "राजकुमार देवव्रत को 'भीष्म' क्यों कहा गया? देवव्रत हस्तिनापुर के राजा शांतनु और माता गंगा के पुत्र थे। वे एक अत्यंत योग्य, वीर और बुद्धिमान राजकुमार थे, जिन्हें भविष्य का राजा बनना था। एक दिन, राजा शांतनु को सत्यवती नाम की एक मछुआरे की बेटी से प्रेम हो गया। जब शांतनु ने सत्यवती के पिता से विवाह का प्रस्ताव रखा, तो उसने एक शर्त रखी: 'मेरी बेटी सत्यवती का पुत्र ही हस्तिनापुर का अगला राजा बनेगा, देवव्रत नहीं।' राजा शांतनु देवव्रत से बहुत प्रेम करते थे, इसलिए वे यह शर्त मान नहीं सके और उदास रहने लगे। जब देवव्रत को अपने पिता के दुःख का कारण पता चला, तो वे सत्यवती के पिता के पास गए। अपने पिता की खुशी के लिए, देवव्रत ने राजसिंहासन का त्याग कर दिया। लेकिन सत्यवती के पिता को डर था कि देवव्रत के बच्चे भविष्य में सिंहासन मांग सकते हैं। तब देवव्रत ने एक ऐसी 'भीष्म' (अत्यंत भयानक) प्रतिज्ञा ली, जिसने पूरी दुनिया को हिला दिया। उन्होंने आजीवन ब्रह्मचारी (अविवाहित) रहने की कसम खाई, ताकि उनका कोई वंश ही न हो! उनके इस महात्याग को देखकर देवता भी रो पड़े और आसमान से फूलों की वर्षा हुई। उसी दिन से उन्हें 'भीष्म' नाम से जाना गया।",
        "estimated_speech_sec": 100.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "राजकुमार देवव्रत को 'भीष्म' क्यों कहा गया?", "image_prompt": "A glorious and handsome young prince Devavrata standing proudly in ancient Hastinapur royal armor, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "वे राजा शांतनु और माता गंगा के पुत्र थे।", "image_prompt": "King Shantanu looking lovingly at his brilliant and strong son, the crown prince Devavrata, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "राजा शांतनु को सत्यवती से प्रेम हो गया।", "image_prompt": "King Shantanu enchanted by a beautiful fisherwoman (Satyavati) standing on a boat by the river Yamuna, 9:16", "approx_sec": 5.0},
            {"slide_index": 4, "caption": "सत्यवती के पिता ने एक कठोर शर्त रखी।", "image_prompt": "An old, stubborn fisherman pointing his finger, demanding that only his grandson will become the king, 9:16", "approx_sec": 6.0},
            {"slide_index": 5, "caption": "शांतनु शर्त नहीं मान सके और उदास हो गए।", "image_prompt": "King Shantanu sitting on his throne, looking depressed and heartbroken, refusing to hurt his son Devavrata, 9:16", "approx_sec": 5.0},
            {"slide_index": 6, "caption": "देवव्रत सत्यवती के पिता के पास गए।", "image_prompt": "Prince Devavrata respectfully visiting the humble fisherman's hut near the river to solve the problem, 9:16", "approx_sec": 5.0},
            {"slide_index": 7, "caption": "उन्होंने पिता की खुशी के लिए सिंहासन त्याग दिया।", "image_prompt": "Devavrata taking off his royal crown and placing it on a wooden table, sacrificing his right to rule, 9:16", "approx_sec": 6.0},
            {"slide_index": 8, "caption": "लेकिन मछुआरे को भविष्य का डर था।", "image_prompt": "The fisherman looking worried, imagining Devavrata's future sons fighting for the throne, 9:16", "approx_sec": 5.0},
            {"slide_index": 9, "caption": "तब देवव्रत ने भयंकर प्रतिज्ञा ली।", "image_prompt": "Devavrata raising his right hand towards the glowing sun, taking a terrible vow with immense determination, 9:16", "approx_sec": 5.0},
            {"slide_index": 10, "caption": "'मैं आजीवन ब्रह्मचारी रहूंगा!'", "image_prompt": "Devavrata vowing never to marry, never to have children, sacrificing his entire personal life for his father, 9:16", "approx_sec": 6.0},
            {"slide_index": 11, "caption": "देवता भी रो पड़े और फूलों की वर्षा हुई।", "image_prompt": "Gods looking down from the heavens in awe, dropping glowing flower petals on the young prince, 9:16", "approx_sec": 6.0},
            {"slide_index": 12, "caption": "उसी दिन से वे 'भीष्म' कहलाए।", "image_prompt": "A majestic cinematic portrait of Bhishma Pitamah, the ultimate symbol of sacrifice, duty, and truth, 9:16", "approx_sec": 5.0}
        ]
    },
    "shikhandi_secret": {
        "story_id": "shikhandi_secret",
        "title": "शिखंडी का रहस्य",
        "category": "महाभारत रहस्य",
        "script_hi": "शिखंडी कौन था और वह भीष्म पितामह की मृत्यु का कारण कैसे बना? शिखंडी का जन्म पिछले जन्म में 'अंबा' नाम की एक राजकुमारी के रूप में हुआ था। भीष्म ने अंबा का अपहरण किया था, लेकिन बाद में उससे विवाह करने से इंकार कर दिया। अपमानित अंबा ने भीष्म से बदला लेने के लिए भगवान शिव की घोर तपस्या की। शिव ने वरदान दिया कि अगले जन्म में वह भीष्म की मृत्यु का कारण बनेगी। अगले जन्म में अंबा ने राजा द्रुपद के यहाँ 'शिखंडिनी' नाम की कन्या के रूप में जन्म लिया, लेकिन बाद में एक यक्ष से लिंग बदलकर वह पुरुष बन गई और उसका नाम 'शिखंडी' पड़ा। कुरुक्षेत्र के युद्ध में, पितामह भीष्म इतने शक्तिशाली थे कि कोई भी उन्हें नहीं हरा सकता था। लेकिन भीष्म का एक उसूल था कि वे किसी भी स्त्री या नपुंसक व्यक्ति पर शस्त्र नहीं उठाएंगे। भगवान कृष्ण ने इसी बात का फायदा उठाया। दसवें दिन के युद्ध में, अर्जुन ने शिखंडी को अपने रथ पर अपने आगे खड़ा कर लिया। जब भीष्म ने शिखंडी को देखा, तो वे पहचान गए कि यह मूल रूप से एक स्त्री (अंबा) है। उन्होंने अपना धनुष नीचे रख दिया। तभी अर्जुन ने शिखंडी के पीछे से छुपकर तीरों की बौछार कर दी और अजेय भीष्म पितामह को बाणों की शय्या पर सुला दिया।",
        "estimated_speech_sec": 100.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "शिखंडी भीष्म की मृत्यु का कारण कैसे बना?", "image_prompt": "A mysterious warrior with both feminine and masculine features (Shikhandi) standing aggressively on a battlefield, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "शिखंडी पिछले जन्म में अंबा थी।", "image_prompt": "Princess Amba crying and looking humiliated, vowing revenge against Bhishma in an ancient palace, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "अंबा ने भीष्म से बदला लेने के लिए तपस्या की।", "image_prompt": "Amba meditating fiercely in a ring of fire, Lord Shiva appearing in the sky to grant her a boon, 9:16", "approx_sec": 6.0},
            {"slide_index": 4, "caption": "शिव ने वरदान दिया कि वह भीष्म को मारेगी।", "image_prompt": "Lord Shiva raising a glowing hand, blessing Amba with the destiny to be the cause of Bhishma's death, 9:16", "approx_sec": 5.0},
            {"slide_index": 5, "caption": "अगले जन्म में उसने कन्या शिखंडिनी के रूप में जन्म लिया।", "image_prompt": "A young girl (Shikhandini) practicing archery and martial arts, determined and fierce, 9:16", "approx_sec": 5.0},
            {"slide_index": 6, "caption": "बाद में एक यक्ष से मदद लेकर वह पुरुष बन गया।", "image_prompt": "A magical glowing Yaksha exchanging genders with Shikhandini in a dark forest, mystical transformation, 9:16", "approx_sec": 6.0},
            {"slide_index": 7, "caption": "भीष्म इतने शक्तिशाली थे कि कोई उन्हें हरा नहीं सकता था।", "image_prompt": "Bhishma Pitamah destroying the Pandava army alone, glowing arrows flying everywhere, invincible, 9:16", "approx_sec": 5.0},
            {"slide_index": 8, "caption": "लेकिन भीष्म किसी स्त्री पर शस्त्र नहीं उठाते थे।", "image_prompt": "Bhishma's strict code of honor, refusing to point his bow at a woman on the battlefield, 9:16", "approx_sec": 5.0},
            {"slide_index": 9, "caption": "कृष्ण ने इसी बात का फायदा उठाया।", "image_prompt": "Lord Krishna smiling strategically and whispering a master plan to a confused Arjuna on the chariot, 9:16", "approx_sec": 5.0},
            {"slide_index": 10, "caption": "अर्जुन ने शिखंडी को अपने आगे खड़ा कर लिया।", "image_prompt": "Shikhandi standing boldly at the front of Arjuna's chariot, holding a bow, Arjuna hiding right behind him, 9:16", "approx_sec": 6.0},
            {"slide_index": 11, "caption": "शिखंडी को देखकर भीष्म ने धनुष रख दिया।", "image_prompt": "Bhishma dropping his heavy bow to the ground and closing his eyes, accepting his fate from Amba, 9:16", "approx_sec": 5.0},
            {"slide_index": 12, "caption": "अर्जुन ने बाणों की शय्या पर सुला दिया।", "image_prompt": "Arjuna shooting hundreds of glowing arrows from behind Shikhandi, piercing Bhishma's armor, causing him to fall, 9:16", "approx_sec": 6.0}
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
print(f"Successfully generated and injected {count} full JSON scripts (Batch 8) into the local database!")
