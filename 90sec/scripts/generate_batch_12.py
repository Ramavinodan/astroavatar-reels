import sqlite3
import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "production_history.db")

batch_data = {
    "ardra_nakshatra": {
        "story_id": "ardra_nakshatra",
        "title": "आर्द्रा नक्षत्र: शिव का आंसू",
        "category": "नक्षत्र एवं ग्रह ज्ञान",
        "script_hi": "ज्योतिष में आर्द्रा नक्षत्र को 'शिव का आंसू' और 'तूफ़ान' क्यों कहा जाता है? आर्द्रा का अर्थ होता है 'नमी' या 'आंसू की बूंद' (Teardrop)। इस नक्षत्र के देवता भगवान शिव का सबसे भयंकर रूप 'रुद्र' (तूफ़ान के देवता) हैं। कथा के अनुसार, जब प्रजापति ब्रह्मा अपनी ही बनाई हुई सृष्टि (एक स्त्री) के प्रति आकर्षित होकर अपना नियंत्रण खो बैठे, तो पूरे ब्रह्मांड में हाहाकार मच गया। धर्म की रक्षा के लिए भगवान शिव प्रकट हुए। शिव का क्रोध इतना भयंकर था कि उन्होंने एक शिकारी 'रुद्र' का रूप धारण किया और अपना भयानक तीर ब्रह्मा जी पर छोड़ दिया। शिव के इस विनाशकारी क्रोध और करुणा के मिश्रण से जो आंसू की बूंद गिरी, वही 'आर्द्रा नक्षत्र' बनी। जो लोग आर्द्रा नक्षत्र में जन्म लेते हैं, उनके जीवन में अक्सर बड़े तूफ़ान (Bigger Transformations) आते हैं। उनका जीवन एक आंसुओं और संघर्ष की प्रक्रिया से होकर गुज़रता है, लेकिन यह संघर्ष उन्हें अंदर से बहुत मज़बूत और ज्ञानी बना देता है। जैसे भयंकर बारिश और तूफ़ान के बाद आकाश बिल्कुल साफ और शुद्ध हो जाता है, वैसे ही आर्द्रा नक्षत्र के लोग जीवन के कष्टों के बाद एकदम शुद्ध और ज्ञानी होकर उभरते हैं।",
        "estimated_speech_sec": 105.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "आर्द्रा नक्षत्र को 'शिव का आंसू' क्यों कहा जाता है?", "image_prompt": "A glowing, perfect teardrop floating in space, reflecting a massive cosmic storm inside it, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "आर्द्रा का अर्थ 'नमी' या 'आंसू' होता है।", "image_prompt": "A beautiful glowing tear falling from a divine eye, turning into a glowing star in the night sky, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "इसके देवता शिव का भयंकर रूप 'रुद्र' हैं।", "image_prompt": "Lord Shiva in his fierce Rudra form, dark stormy aura, holding a powerful bow, lightning flashing, 9:16", "approx_sec": 5.0},
            {"slide_index": 4, "caption": "ब्रह्मा जी अपना नियंत्रण खो बैठे थे।", "image_prompt": "Lord Brahma looking confused and enchanted, universe spinning out of control, cosmic imbalance, 9:16", "approx_sec": 5.0},
            {"slide_index": 5, "caption": "धर्म की रक्षा के लिए शिव शिकारी बने।", "image_prompt": "Lord Shiva transforming into a fierce, tribal hunter (Rudra) aiming a glowing red arrow, 9:16", "approx_sec": 6.0},
            {"slide_index": 6, "caption": "उन्होंने ब्रह्मा जी पर बाण छोड़ दिया।", "image_prompt": "A glowing arrow flying across the cosmos, restoring balance but causing immense fear and awe, 9:16", "approx_sec": 5.0},
            {"slide_index": 7, "caption": "शिव के क्रोध और करुणा से एक आंसू गिरा।", "image_prompt": "A single, glowing, pure teardrop falling from Lord Shiva's fierce eye, containing immense power, 9:16", "approx_sec": 6.0},
            {"slide_index": 8, "caption": "वही आंसू 'आर्द्रा नक्षत्र' बना।", "image_prompt": "The teardrop expanding into a bright, intense star cluster amidst dark stormy space clouds, 9:16", "approx_sec": 5.0},
            {"slide_index": 9, "caption": "इन लोगों के जीवन में बड़े तूफ़ान आते हैं।", "image_prompt": "A person standing strong on a cliff while a massive hurricane and storm rages around them, 9:16", "approx_sec": 5.0},
            {"slide_index": 10, "caption": "संघर्ष उन्हें मज़बूत और ज्ञानी बनाता है।", "image_prompt": "A blacksmith pulling a glowing, perfectly forged sword out of a very hot, burning fire, 9:16", "approx_sec": 5.0},
            {"slide_index": 11, "caption": "जैसे तूफ़ान के बाद आकाश साफ हो जाता है...", "image_prompt": "Dark storm clouds clearing up rapidly, revealing a breathtakingly clear, sunny, and pure blue sky, 9:16", "approx_sec": 6.0},
            {"slide_index": 12, "caption": "वैसे ही ये लोग दुखों के बाद शुद्ध होकर उभरते हैं।", "image_prompt": "A glowing, peaceful person meditating, surrounded by a pure white aura, completely transformed and calm, 9:16", "approx_sec": 6.0}
        ]
    },
    "pushya_nakshatra": {
        "story_id": "pushya_nakshatra",
        "title": "पुष्य नक्षत्र: सबसे शुभ तारा",
        "category": "नक्षत्र एवं ग्रह ज्ञान",
        "script_hi": "ज्योतिष में 'पुष्य नक्षत्र' को सभी 27 नक्षत्रों का राजा और सबसे शुभ क्यों माना जाता है? पुष्य का अर्थ होता है 'पोषण करना' (To Nourish) या पालना। इस नक्षत्र का प्रतीक गाय का 'थन' (Cow's udder) है, जो बिना किसी स्वार्थ के सबको दूध और जीवन देता है। इसके देवता देवगुरु बृहस्पति हैं, जो धर्म और ज्ञान के प्रतीक हैं। ज्योतिष के अनुसार, अगर आकाश में पुष्य नक्षत्र हो, तो उस समय किया गया कोई भी काम—जैसे शादी, नया व्यापार, या सोना खरीदना—हमेशा सफल होता है। यह नक्षत्र इतना शक्तिशाली है कि अगर जन्म कुंडली में कई सारे बुरे योग या श्राप (Dosh) भी हों, लेकिन चंद्रमा पुष्य नक्षत्र में हो, तो यह अकेला तारा सभी बुरे योगों को नष्ट कर देता है! पुष्य नक्षत्र में जन्मे लोग बहुत दयालु, दूसरों की मदद करने वाले, धार्मिक और भरोसेमंद होते हैं। वे समाज में एक 'पिता' या 'गुरु' की तरह काम करते हैं। वे जीवन में धीरे-धीरे लेकिन बहुत ठोस और स्थायी (Permanent) सफलता प्राप्त करते हैं, जिसे कोई उनसे छीन नहीं सकता।",
        "estimated_speech_sec": 95.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "पुष्य नक्षत्र को सबसे शुभ क्यों माना जाता है?", "image_prompt": "A glowing, incredibly bright and pure golden star (Pushya Nakshatra) shining above all other stars, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "पुष्य का अर्थ 'पोषण करना' होता है।", "image_prompt": "A mother gently and lovingly feeding her baby, radiating a soft, warm, golden nourishing light, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "इसका प्रतीक गाय का थन (Udder) है।", "image_prompt": "A divine, glowing white cow (Kamadhenu) standing peacefully, symbolizing infinite nourishment and selfless giving, 9:16", "approx_sec": 5.0},
            {"slide_index": 4, "caption": "इसके देवता देवगुरु बृहस्पति हैं।", "image_prompt": "Guru Brihaspati sitting peacefully, giving blessings, surrounded by a pure yellow and golden aura, 9:16", "approx_sec": 5.0},
            {"slide_index": 5, "caption": "पुष्य नक्षत्र में किया गया हर काम सफल होता है।", "image_prompt": "A successful opening of a new shop or business, decorated with flowers, glowing with prosperity, 9:16", "approx_sec": 6.0},
            {"slide_index": 6, "caption": "यह सभी बुरे योगों को नष्ट कर देता है!", "image_prompt": "A single bright golden star shooting a beam of light that shatters dark, negative astrological clouds, 9:16", "approx_sec": 6.0},
            {"slide_index": 7, "caption": "पुष्य में जन्मे लोग बहुत दयालु होते हैं।", "image_prompt": "A kind-hearted person happily distributing warm food and clothes to poor children on the street, 9:16", "approx_sec": 5.0},
            {"slide_index": 8, "caption": "वे दूसरों की बिना स्वार्थ मदद करते हैं।", "image_prompt": "A person helping an old woman cross a busy road, glowing with a subtle aura of kindness, 9:16", "approx_sec": 5.0},
            {"slide_index": 9, "caption": "वे समाज में एक गुरु की तरह होते हैं।", "image_prompt": "A wise teacher sitting under a banyan tree, surrounded by students listening to him with deep respect, 9:16", "approx_sec": 5.0},
            {"slide_index": 10, "caption": "उन्हें धीरे-धीरे सफलता मिलती है...", "image_prompt": "A strong, thick oak tree growing slowly but steadily, its roots going very deep into the earth, 9:16", "approx_sec": 5.0},
            {"slide_index": 11, "caption": "लेकिन वह सफलता बहुत ठोस और स्थायी होती है।", "image_prompt": "A magnificent, unshakable stone castle built on top of a solid rock mountain, completely indestructible, 9:16", "approx_sec": 6.0},
            {"slide_index": 12, "caption": "जिसे कोई उनसे छीन नहीं सकता।", "image_prompt": "A glowing golden crown resting securely on a velvet pillow, protected by divine light, 9:16", "approx_sec": 5.0}
        ]
    },
    "magha_nakshatra": {
        "story_id": "magha_nakshatra",
        "title": "मघा नक्षत्र: शाही सिंहासन",
        "category": "नक्षत्र एवं ग्रह ज्ञान",
        "script_hi": "मघा नक्षत्र में जन्मे लोग अक्सर 'राजा' या बड़े नेता क्यों बनते हैं? 'मघा' का अर्थ होता है 'महान' (The Great)। यह सिंह (Leo) राशि में आता है और इसका प्रतीक एक 'शाही सिंहासन' (Royal Throne) है। इस नक्षत्र के देवता हमारे 'पितृ' (Ancestors) हैं, जो हमें अपना आशीर्वाद और परंपराएं (Traditions) विरासत में देते हैं। मघा नक्षत्र व्यक्ति को जन्म से ही एक शाही अंदाज़, नेतृत्व (Leadership) की क्षमता और बहुत अधिक मान-सम्मान देता है। इन लोगों को साधारण जीवन पसंद नहीं होता; ये जो भी करते हैं, बड़े पैमाने पर करते हैं। वे अपने परिवार की इज्ज़त और पूर्वजों की परंपराओं से गहराई से जुड़े होते हैं। लेकिन इस नक्षत्र की सबसे बड़ी चेतावनी यह है कि यदि व्यक्ति में अहंकार (Ego) आ जाए, तो वह एक क्रूर तानाशाह (Dictator) भी बन सकता है। जो लोग मघा नक्षत्र में जन्म लेते हैं, अगर वे अपने पूर्वजों का सम्मान करें और अपनी शक्ति का इस्तेमाल दूसरों की भलाई के लिए करें, तो वे समाज में राजा, बड़े अधिकारी, या टॉप बॉस बनते हैं।",
        "estimated_speech_sec": 95.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "मघा नक्षत्र वाले राजा या नेता क्यों बनते हैं?", "image_prompt": "A majestic, glowing constellation forming the shape of a grand royal throne in the starry night sky, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "'मघा' का अर्थ होता है 'महान'।", "image_prompt": "A grand, heavily jeweled golden crown resting on a red velvet pillow, glowing with royal authority, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "इसका प्रतीक शाही सिंहासन है।", "image_prompt": "A huge, intimidating golden throne in an empty, grand palace hall, waiting for a powerful king, 9:16", "approx_sec": 5.0},
            {"slide_index": 4, "caption": "इसके देवता हमारे 'पितृ' (पूर्वज) हैं।", "image_prompt": "Glowing, translucent figures of ancient kings and ancestors looking down from the heavens, giving blessings, 9:16", "approx_sec": 5.0},
            {"slide_index": 5, "caption": "यह जन्म से ही शाही अंदाज़ देता है।", "image_prompt": "A confident person walking down a hallway, naturally commanding respect, people bowing slightly, 9:16", "approx_sec": 6.0},
            {"slide_index": 6, "caption": "इन्हें साधारण जीवन पसंद नहीं होता।", "image_prompt": "A person rejecting a small, plain wooden chair and pointing towards a grand, luxurious leather seat, 9:16", "approx_sec": 5.0},
            {"slide_index": 7, "caption": "ये पूर्वजों की परंपराओं से जुड़े होते हैं।", "image_prompt": "A person respectfully holding an ancient family sword or relic, honoring their proud family bloodline, 9:16", "approx_sec": 5.0},
            {"slide_index": 8, "caption": "लेकिन इनमें अहंकार भी आ सकता है।", "image_prompt": "A leader looking down arrogantly from a high balcony, intoxicated by power and wealth, 9:16", "approx_sec": 5.0},
            {"slide_index": 9, "caption": "अहंकार से ये तानाशाह बन सकते हैं।", "image_prompt": "A dark silhouette of a cruel dictator pointing a commanding finger, surrounded by a fearful, dark aura, 9:16", "approx_sec": 5.0},
            {"slide_index": 10, "caption": "अगर शक्ति का सही इस्तेमाल करें...", "image_prompt": "A benevolent king happily distributing gold and food to his cheering, happy citizens, 9:16", "approx_sec": 5.0},
            {"slide_index": 11, "caption": "तो ये समाज के टॉप बॉस बनते हैं।", "image_prompt": "A modern highly successful CEO standing confidently at the head of a massive corporate boardroom table, 9:16", "approx_sec": 6.0},
            {"slide_index": 12, "caption": "मघा नक्षत्र महानता का प्रतीक है।", "image_prompt": "A roaring golden lion standing proudly on a mountain peak with the sun rising behind it, 9:16", "approx_sec": 5.0}
        ]
    },
    "mula_nakshatra": {
        "story_id": "mula_nakshatra",
        "title": "मूल नक्षत्र: विनाश और जड़ें",
        "category": "नक्षत्र एवं ग्रह ज्ञान",
        "script_hi": "मूल नक्षत्र को इतना रहस्यमयी और डरावना क्यों माना जाता है? 'मूल' का अर्थ होता है 'जड़' (Root) या आधार। इस नक्षत्र का प्रतीक पेड़ों की एक बंधी हुई जड़ है। इसके देवता 'निरृति' हैं, जो विनाश (Destruction) और मृत्यु की देवी हैं। यही कारण है कि मूल नक्षत्र को 'गंडमूल' माना जाता है, जिसमें जन्म लेना जीवन में बहुत बड़े बदलाव लाता है। यह नक्षत्र व्यक्ति को भौतिक चीज़ों (पैसे, रिश्ते) से पूरी तरह दूर कर देता है। इस नक्षत्र में जन्मे लोग अक्सर जीवन में एक बार अपना सब कुछ खो देते हैं (विनाश)। लेकिन यह विनाश एक बुरे अंत के लिए नहीं, बल्कि एक नई शुरुआत के लिए होता है! मूल नक्षत्र इंसान को जड़ों तक ले जाता है, यानी उसे जीवन की 'असली सच्चाई' (Spirituality) खोजना सिखाता है। ये लोग बहुत अच्छे खोजी (Researchers), वैज्ञानिक, या जासूस बनते हैं, क्योंकि ये हर चीज़ की गहराई (जड़) तक जाना पसंद करते हैं। एक बार जब ये लोग अध्यात्म (God) से जुड़ जाते हैं, तो ये दुनिया के सबसे ज्ञानी और शक्तिशाली इंसान बनते हैं।",
        "estimated_speech_sec": 100.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "मूल नक्षत्र इतना रहस्यमयी क्यों है?", "image_prompt": "A glowing constellation in the shape of tangled, deep tree roots floating in a mysterious dark cosmos, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "'मूल' का अर्थ होता है 'जड़' (Root)।", "image_prompt": "Massive, glowing ancient tree roots digging extremely deep into the dark, hidden layers of the earth, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "इसकी देवी 'निरृति' (विनाश) हैं।", "image_prompt": "Goddess Nirriti, looking terrifying and mysterious in dark clothes, holding a sword of destruction, 9:16", "approx_sec": 5.0},
            {"slide_index": 4, "caption": "इसमें जन्म लेना बड़े बदलाव लाता है।", "image_prompt": "A massive, powerful tornado ripping through a landscape, completely tearing down old, weak structures, 9:16", "approx_sec": 5.0},
            {"slide_index": 5, "caption": "ये भौतिक चीज़ों (पैसे) से दूर हो जाते हैं।", "image_prompt": "A person calmly dropping a bag of gold coins and walking away into a deep, misty forest, 9:16", "approx_sec": 6.0},
            {"slide_index": 6, "caption": "कई बार ये अपना सब कुछ खो देते हैं।", "image_prompt": "A wealthy person's mansion completely burning down to ashes in a fierce fire, absolute loss, 9:16", "approx_sec": 5.0},
            {"slide_index": 7, "caption": "लेकिन यह विनाश नई शुरुआत के लिए है!", "image_prompt": "A tiny, bright green glowing sprout growing out of the black, burnt ashes of the destroyed house, 9:16", "approx_sec": 6.0},
            {"slide_index": 8, "caption": "मूल नक्षत्र इंसान को जीवन की सच्चाई सिखाता है।", "image_prompt": "A person sitting deeply in meditation inside a dark cave, a glowing third eye opening on their forehead, 9:16", "approx_sec": 6.0},
            {"slide_index": 9, "caption": "ये हर चीज़ की गहराई तक जाना पसंद करते हैं।", "image_prompt": "A focused researcher or detective looking through a glowing magnifying glass at ancient, hidden texts, 9:16", "approx_sec": 5.0},
            {"slide_index": 10, "caption": "ये बहुत अच्छे वैज्ञानिक या जासूस बनते हैं।", "image_prompt": "A brilliant scientist making a massive breakthrough in a high-tech lab, surrounded by glowing data, 9:16", "approx_sec": 5.0},
            {"slide_index": 11, "caption": "अध्यात्म से जुड़ने पर ये अत्यंत ज्ञानी बनते हैं।", "image_prompt": "A person levitating slightly, surrounded by a massive, powerful golden aura of pure spiritual knowledge, 9:16", "approx_sec": 5.0},
            {"slide_index": 12, "caption": "जड़ जितनी गहरी होगी, पेड़ उतना ऊंचा होगा।", "image_prompt": "A magnificent, towering glowing tree touching the sky, supported by equally deep and massive roots, 9:16", "approx_sec": 6.0}
        ]
    },
    "revati_nakshatra": {
        "story_id": "revati_nakshatra",
        "title": "रेवती नक्षत्र: अंतिम यात्रा",
        "category": "नक्षत्र एवं ग्रह ज्ञान",
        "script_hi": "27वें और अंतिम नक्षत्र 'रेवती' को मोक्ष और पूर्णता का प्रतीक क्यों माना जाता है? रेवती नक्षत्र मीन (Pisces) राशि में आता है, जो राशि चक्र की बिल्कुल आखिरी मंज़िल है। इसका प्रतीक 'मछलियों का एक जोड़ा' (Two Fishes) या 'ढोलक' (Drum) है। इसके देवता 'पूषन' हैं, जो सूर्य का वह रूप हैं जो लोगों को अंधेरे से बाहर निकालते हैं और जानवरों-पक्षियों की रक्षा करते हैं। चूंकि यह अंतिम नक्षत्र है, इसलिए रेवती में जन्म लेने वाले लोग बहुत ही आध्यात्मिक (Spiritual), दयालु और पुरानी आत्मा (Old Souls) होते हैं। ऐसा लगता है जैसे उन्होंने दुनिया बहुत देख ली है और अब उन्हें केवल शांति चाहिए। उन्हें जानवरों से बहुत प्यार होता है और वे किसी को दुखी नहीं देख सकते। रेवती नक्षत्र एक यात्रा के अंत और मोक्ष (Moksha) का सूचक है। ये लोग बहुत अच्छी नींद लेते हैं, सपनों की दुनिया (Dream World) में खोए रहते हैं, और बहुत रचनात्मक (Creative) होते हैं। यदि ये लोग अपने भटकाव को रोक लें, तो ये जीवन की सबसे ऊंची आध्यात्मिक अवस्था (Enlightenment) को प्राप्त करते हैं, जहाँ आत्मा परमात्मा से मिल जाती है।",
        "estimated_speech_sec": 105.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "अंतिम नक्षत्र 'रेवती' मोक्ष का प्रतीक क्यों है?", "image_prompt": "A glowing, mystical constellation at the very edge of the universe, fading into pure golden light, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "यह राशि चक्र की बिल्कुल आखिरी मंज़िल है।", "image_prompt": "A beautiful cosmic clock showing the 12 zodiac signs, with a glowing light pointing at the final sign (Pisces), 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "इसका प्रतीक मछलियों का एक जोड़ा या ढोलक है।", "image_prompt": "Two glowing, magical Koi fishes swimming gracefully in a circle inside a cosmic, starry ocean, 9:16", "approx_sec": 5.0},
            {"slide_index": 4, "caption": "देवता 'पूषन' अंधेरे से बाहर निकालते हैं।", "image_prompt": "The gentle Sun God (Pushan) holding a glowing lantern, guiding lost souls safely out of a dark forest, 9:16", "approx_sec": 6.0},
            {"slide_index": 5, "caption": "ये लोग पुरानी आत्मा (Old Souls) होते हैं।", "image_prompt": "A young person with incredibly deep, wise, glowing eyes, looking like they have lived a thousand lives, 9:16", "approx_sec": 5.0},
            {"slide_index": 6, "caption": "उन्हें केवल शांति और सुकून चाहिए।", "image_prompt": "A person sitting peacefully on a mountain edge at sunset, enjoying absolute silence and calm breezes, 9:16", "approx_sec": 5.0},
            {"slide_index": 7, "caption": "उन्हें जानवरों से बहुत प्यार होता है।", "image_prompt": "A person sitting in a forest, happily surrounded by deer, birds, and rabbits resting comfortably near them, 9:16", "approx_sec": 5.0},
            {"slide_index": 8, "caption": "वे किसी को दुखी नहीं देख सकते।", "image_prompt": "A person gently wiping the tears of a crying stranger on the street, glowing with intense empathy, 9:16", "approx_sec": 5.0},
            {"slide_index": 9, "caption": "ये सपनों की दुनिया में खोए रहते हैं।", "image_prompt": "A person sleeping peacefully, floating in a beautiful, highly creative, magical glowing dreamscape, 9:16", "approx_sec": 5.0},
            {"slide_index": 10, "caption": "ये बहुत रचनात्मक (Creative) होते हैं।", "image_prompt": "An artist passionately painting a magnificent, otherworldly cosmic canvas that seems to come alive, 9:16", "approx_sec": 5.0},
            {"slide_index": 11, "caption": "रेवती एक यात्रा के अंत का सूचक है।", "image_prompt": "A lone traveler walking towards a massive, glowing, golden door at the end of a long, dark path, 9:16", "approx_sec": 5.0},
            {"slide_index": 12, "caption": "जहाँ आत्मा परमात्मा से मिल जाती है।", "image_prompt": "A glowing human soul seamlessly merging into a massive, warm, infinite ocean of divine golden light, 9:16", "approx_sec": 6.0}
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
print(f"Successfully generated and injected {count} full JSON scripts (Batch 12) into the local database!")
