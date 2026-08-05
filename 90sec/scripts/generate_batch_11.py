import sqlite3
import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "production_history.db")

batch_data = {
    "pitru_dosh": {
        "story_id": "pitru_dosh",
        "title": "पितृ दोष: पूर्वजों का ऋण",
        "category": "नक्षत्र एवं ग्रह ज्ञान",
        "script_hi": "कुंडली में पितृ दोष क्या होता है और यह क्यों लगता है? हिंदू धर्म में माना जाता है कि हमारे पूर्वज (Ancestors) मृत्यु के बाद पितृ लोक में निवास करते हैं और अपने वंशजों की भलाई चाहते हैं। लेकिन अगर किसी व्यक्ति ने पिछले जन्मों में अपने माता-पिता, बुजुर्गों या गुरुओं का अपमान किया हो, उन्हें भूखा रखा हो, या उनके अंतिम संस्कार (श्राद्ध) ठीक से न किए हों, तो उसकी कुंडली में 'पितृ दोष' बन जाता है। ज्योतिष में जब सूर्य या बृहस्पति (गुरु) के साथ राहु या केतु बैठ जाएं, तो यह दोष माना जाता है। पितृ दोष होने पर व्यक्ति को जीवन में बिना वजह के संघर्ष, घर में कलह, संतान प्राप्ति में बाधाएं, और आर्थिक नुकसान का सामना करना पड़ता है। ऐसा लगता है जैसे कोई अदृश्य शक्ति उसे आगे बढ़ने से रोक रही हो। लेकिन इसका निवारण संभव है! पितृ पक्ष (श्राद्ध) के दौरान अपने पूर्वजों के नाम पर गरीबों को भोजन कराने, कौवे, गाय और कुत्ते को खाना खिलाने, और बुजुर्गों का सम्मान करने से यह दोष कट जाता है। पूर्वज खुश होकर ऐसा आशीर्वाद देते हैं, जो किसी भी ग्रह की दशा को बदल सकता है।",
        "estimated_speech_sec": 105.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "कुंडली में पितृ दोष क्या होता है?", "image_prompt": "A glowing Vedic astrology chart covered by the subtle, slightly sad, ethereal shadows of ancient ancestors, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "मृत्यु के बाद पूर्वज पितृ लोक में निवास करते हैं।", "image_prompt": "A peaceful glowing heavenly realm (Pitru Loka) with calm souls wrapped in white light, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "अगर किसी ने अपने बुजुर्गों का अपमान किया हो...", "image_prompt": "A dark flashback of an arrogant young man shouting at his crying old parents, bad karma forming, 9:16", "approx_sec": 5.0},
            {"slide_index": 4, "caption": "या उनका अंतिम संस्कार (श्राद्ध) ठीक से न किया हो।", "image_prompt": "A neglected and forgotten holy riverbank where sacred rituals (Pind Daan) are supposed to happen, 9:16", "approx_sec": 5.0},
            {"slide_index": 5, "caption": "तो जन्म कुंडली में 'पितृ दोष' बन जाता है।", "image_prompt": "The Sun God (Surya) trapped by the dark, smoky shadow of Rahu in a Kundali, casting darkness, 9:16", "approx_sec": 6.0},
            {"slide_index": 6, "caption": "पितृ दोष से जीवन में बिना वजह संघर्ष होता है।", "image_prompt": "A man trying very hard to push a cart up a hill, but invisible chains are pulling him back, 9:16", "approx_sec": 5.0},
            {"slide_index": 7, "caption": "घर में कलह और आर्थिक नुकसान होता है।", "image_prompt": "A dark cloud hovering over a nice home, money turning to ash, representing negative family energy, 9:16", "approx_sec": 5.0},
            {"slide_index": 8, "caption": "लेकिन इसका निवारण संभव है!", "image_prompt": "A bright ray of golden sunlight breaking through the dark clouds, bringing hope and positive energy, 9:16", "approx_sec": 5.0},
            {"slide_index": 9, "caption": "पितृ पक्ष में गरीबों को भोजन कराएं।", "image_prompt": "A person respectfully serving warm food on banana leaves to poor and hungry people, 9:16", "approx_sec": 5.0},
            {"slide_index": 10, "caption": "कौवे, गाय और कुत्ते को खाना खिलाएं।", "image_prompt": "A person offering bread (roti) to a black crow, a gentle cow, and a dog, receiving silent blessings, 9:16", "approx_sec": 6.0},
            {"slide_index": 11, "caption": "बुजुर्गों का सम्मान करें।", "image_prompt": "A person bowing down and touching the feet of their old parents, who are smiling and blessing them, 9:16", "approx_sec": 5.0},
            {"slide_index": 12, "caption": "पूर्वजों का आशीर्वाद किसी भी ग्रह दशा को बदल सकता है।", "image_prompt": "Glowing ethereal hands from the heavens gently showering golden light over the person's head, 9:16", "approx_sec": 6.0}
        ]
    },
    "guru_chandal_yoga": {
        "story_id": "guru_chandal_yoga",
        "title": "गुरु चांडाल योग",
        "category": "नक्षत्र एवं ग्रह ज्ञान",
        "script_hi": "गुरु चांडाल योग क्या है और यह इंसान की बुद्धि को कैसे भ्रष्ट कर देता है? वैदिक ज्योतिष में बृहस्पति (गुरु) को सबसे पवित्र ग्रह माना गया है, जो ज्ञान, धर्म और अच्छे चरित्र का प्रतीक है। वहीं राहु को एक 'चांडाल' या राक्षस माना गया है, जो भ्रम, झूठ, लालच और शॉर्टकट का प्रतीक है। जब किसी व्यक्ति की कुंडली में गुरु और राहु एक साथ एक ही घर में बैठ जाएं, तो 'गुरु चांडाल योग' का निर्माण होता है। इसका मतलब है कि एक महान संत (गुरु) के पास आकर एक क्रूर राक्षस (राहु) बैठ गया है। इस योग के प्रभाव से व्यक्ति की बुद्धि अक्सर गलत दिशा में काम करने लगती है। वह व्यक्ति अत्यंत बुद्धिमान और चतुर तो होता है, लेकिन वह अपनी बुद्धि का इस्तेमाल लोगों को धोखा देने, झूठ बोलने और गलत तरीकों से पैसा कमाने में कर सकता है। ऐसे लोगों को अक्सर धर्म और नैतिकता पर विश्वास नहीं होता। हालांकि, अगर कुंडली में गुरु की स्थिति बहुत मज़बूत हो, तो वह राहु की नकारात्मकता को दबा देता है, और व्यक्ति एक बड़ा कूटनीतिज्ञ (Diplomat) या राजनेता बन सकता है।",
        "estimated_speech_sec": 100.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "गुरु चांडाल योग क्या है?", "image_prompt": "A cosmic clash in an astrology chart: A pure golden light (Jupiter) mixing with dark toxic smoke (Rahu), 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "बृहस्पति ज्ञान, धर्म और सात्विकता के प्रतीक हैं।", "image_prompt": "A glowing, peaceful saint meditating, radiating pure golden light and divine wisdom, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "राहु भ्रम, झूठ और चांडाल प्रवृत्ति का प्रतीक है।", "image_prompt": "A dark, shadowy demonic figure whispering manipulative lies, surrounded by dark smoky illusions, 9:16", "approx_sec": 5.0},
            {"slide_index": 4, "caption": "जब गुरु और राहु एक साथ बैठ जाएं...", "image_prompt": "The peaceful saint and the shadowy demon sitting forcedly next to each other on the same mat, 9:16", "approx_sec": 5.0},
            {"slide_index": 5, "caption": "तो 'गुरु चांडाल योग' बनता है।", "image_prompt": "The toxic dark smoke of the demon trying to cover the pure golden light of the saint, creating chaos, 9:16", "approx_sec": 5.0},
            {"slide_index": 6, "caption": "इससे इंसान की बुद्धि भ्रष्ट हो सकती है।", "image_prompt": "A human brain glowing with bright light but infected with creeping dark thorny vines, 9:16", "approx_sec": 5.0},
            {"slide_index": 7, "caption": "व्यक्ति चतुर होता है, लेकिन गलत दिशा में।", "image_prompt": "A very smart looking person playing chess, but hiding extra pieces behind his back to cheat, 9:16", "approx_sec": 6.0},
            {"slide_index": 8, "caption": "वह झूठ और शॉर्टकट से पैसा कमाना चाहता है।", "image_prompt": "A person stepping on broken, dangerous stairs to quickly grab a bag of gold, ignoring the safe path, 9:16", "approx_sec": 6.0},
            {"slide_index": 9, "caption": "उसे धर्म और नैतिकता पर विश्वास नहीं होता।", "image_prompt": "A person walking confidently away from a glowing temple, walking into a dark alley of gambling, 9:16", "approx_sec": 5.0},
            {"slide_index": 10, "caption": "लेकिन अगर गुरु अत्यंत मज़बूत हो...", "image_prompt": "The pure golden light suddenly blasting outward, completely destroying and purifying the dark smoke, 9:16", "approx_sec": 5.0},
            {"slide_index": 11, "caption": "तो वह राहु की नकारात्मकता को दबा देता है।", "image_prompt": "The saint successfully chaining the shadow demon, controlling its dark energy with pure wisdom, 9:16", "approx_sec": 5.0},
            {"slide_index": 12, "caption": "ऐसा व्यक्ति एक महान राजनेता बन सकता है।", "image_prompt": "A highly confident and successful leader standing at a podium, mastering both diplomacy and strategy, 9:16", "approx_sec": 6.0}
        ]
    },
    "gajakesari_yoga": {
        "story_id": "gajakesari_yoga",
        "title": "गजकेसरी योग: सफलता का राज",
        "category": "नक्षत्र एवं ग्रह ज्ञान",
        "script_hi": "गजकेसरी योग क्या है और यह किसी को राजा कैसे बना देता है? ज्योतिष में 'गज' का अर्थ हाथी (Elephant) और 'केसरी' का अर्थ शेर (Lion) होता है। हाथी बुद्धिमानी, स्थिरता और धन का प्रतीक है, जबकि शेर साहस, नेतृत्व और पराक्रम का प्रतीक है। जब किसी व्यक्ति की जन्म कुंडली में चंद्रमा और बृहस्पति (गुरु) एक साथ बैठ जाएं, या एक-दूसरे से केंद्र (1, 4, 7, 10वें घर) में हों, तो यह अत्यंत शुभ 'गजकेसरी योग' बनता है। चंद्रमा हमारा 'मन' है और गुरु 'ज्ञान'। जब मन को सही ज्ञान का मार्गदर्शन मिल जाए, तो इंसान जीवन में कोई भी गलत फैसला नहीं लेता। इस योग वाले लोग बहुत ही आकर्षक, दयालु, दूरदर्शी और शानदार वक्ता (Speaker) होते हैं। चाहे वे कितने भी गरीब परिवार में क्यों न जन्म लें, अपनी मेहनत और ज्ञान के बल पर वे समाज में उच्च पद, अपार धन और बहुत सम्मान प्राप्त करते हैं। भगवान राम की कुंडली में भी प्रथम भाव में गुरु और चंद्र साथ बैठे थे, जिन्होंने उन्हें मर्यादा पुरुषोत्तम और महान चक्रवर्ती सम्राट बनाया।",
        "estimated_speech_sec": 100.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "गजकेसरी योग क्या है?", "image_prompt": "A majestic glowing white elephant (Gaja) and a fierce golden lion (Kesari) standing together peacefully, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "हाथी बुद्धिमानी और धन का प्रतीक है।", "image_prompt": "A royal elephant heavily decorated with gold and jewels, symbolizing enormous wealth and stability, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "शेर साहस और नेतृत्व का प्रतीक है।", "image_prompt": "A powerful male lion standing on a high cliff roaring, symbolizing absolute fearless leadership, 9:16", "approx_sec": 5.0},
            {"slide_index": 4, "caption": "जब चंद्रमा और गुरु एक साथ बैठें...", "image_prompt": "Astrology chart showing a beautiful silver Moon and a glowing golden Jupiter happily sitting in the same house, 9:16", "approx_sec": 5.0},
            {"slide_index": 5, "caption": "तो यह अत्यंत शुभ 'गजकेसरी योग' बनता है।", "image_prompt": "A massive burst of golden and silver cosmic light blending together, creating an aura of ultimate success, 9:16", "approx_sec": 6.0},
            {"slide_index": 6, "caption": "चंद्रमा हमारा मन है, और गुरु ज्ञान।", "image_prompt": "A human head silhouette, with a glowing silver moon in the center of the brain wrapped by golden wisdom light, 9:16", "approx_sec": 5.0},
            {"slide_index": 7, "caption": "ज्ञान मिलने पर मन गलत फैसले नहीं लेता।", "image_prompt": "A person standing at a crossroads, easily choosing the glowing bright path instead of the dark one, 9:16", "approx_sec": 5.0},
            {"slide_index": 8, "caption": "ऐसे लोग शानदार वक्ता और दूरदर्शी होते हैं।", "image_prompt": "A charismatic speaker addressing a massive crowd, golden light radiating from his words, people listening in awe, 9:16", "approx_sec": 6.0},
            {"slide_index": 9, "caption": "गरीब परिवार में जन्म लेकर भी...", "image_prompt": "A child reading a book under a street lamp in a poor village, determined and glowing with potential, 9:16", "approx_sec": 5.0},
            {"slide_index": 10, "caption": "वे समाज में उच्च पद और अपार धन पाते हैं।", "image_prompt": "The same person, now an adult, sitting in a massive corporate office or royal throne, highly successful, 9:16", "approx_sec": 6.0},
            {"slide_index": 11, "caption": "भगवान राम की कुंडली में भी यह योग था।", "image_prompt": "Lord Rama standing beautifully with his bow, a combined golden and silver aura (Jupiter-Moon) shining around him, 9:16", "approx_sec": 5.0},
            {"slide_index": 12, "caption": "जिसने उन्हें महान सम्राट बनाया।", "image_prompt": "Lord Rama wearing the royal crown in Ayodhya, loved by his people, ruling the perfect kingdom (Ram Rajya), 9:16", "approx_sec": 5.0}
        ]
    },
    "kemdrum_dosh": {
        "story_id": "kemdrum_dosh",
        "title": "केमद्रुम दोष: चंद्रमा का अकेलापन",
        "category": "नक्षत्र एवं ग्रह ज्ञान",
        "script_hi": "केमद्रुम दोष क्या है और यह इंसान को अंदर से खोखला क्यों कर देता है? वैदिक ज्योतिष में चंद्रमा हमारे 'मन', 'भावनाओं' (Emotions) और 'शांति' का कारक है। चंद्रमा एक ऐसा ग्रह है जिसे हमेशा किसी न किसी सहारे की ज़रूरत होती है। जब जन्म कुंडली में चंद्रमा के आगे वाले घर में और पीछे वाले घर में कोई भी ग्रह न हो, और चंद्रमा बिल्कुल अकेला बैठा हो, तो इसे 'केमद्रुम दोष' कहते हैं। इसका मतलब है कि व्यक्ति का 'मन' पूरी तरह से अकेला और असुरक्षित है। ऐसे लोग अक्सर बहुत ज़्यादा ओवरथिंकिंग (Overthinking) करते हैं, उन्हें हर समय एक अजीब सा डर या खालीपन सताता है। चाहे उनके पास कितना भी पैसा या परिवार क्यों न हो, उन्हें अंदर से अकेलापन ही महसूस होता है। कई बार यह दोष व्यक्ति को डिप्रेशन में डाल सकता है और उसके बने-बनाए काम बिगाड़ सकता है। लेकिन इसे ठीक किया जा सकता है! जो व्यक्ति रोज़ाना भगवान शिव की आराधना करता है, शिवलिंग पर जल चढ़ाता है और अपनी माता की सेवा करता है, उसके जीवन से चंद्रमा का यह अकेलापन (केमद्रुम दोष) हमेशा के लिए खत्म हो जाता है।",
        "estimated_speech_sec": 105.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "केमद्रुम दोष इंसान को खोखला क्यों कर देता है?", "image_prompt": "A glowing silver moon floating completely alone in a vast, dark, empty void of space, feeling isolated, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "चंद्रमा हमारे 'मन' और 'भावनाओं' का कारक है।", "image_prompt": "A glowing silver moon placed inside the human heart, radiating soft, emotional, and sensitive energy, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "चंद्रमा को हमेशा सहारे की ज़रूरत होती है।", "image_prompt": "The Moon happily holding hands with bright colorful planets like Jupiter and Venus on both sides, 9:16", "approx_sec": 5.0},
            {"slide_index": 4, "caption": "जब चंद्रमा के आगे और पीछे कोई ग्रह न हो...", "image_prompt": "An astrology chart where the Moon sits alone in a box, and the boxes before and after it are completely empty, 9:16", "approx_sec": 6.0},
            {"slide_index": 5, "caption": "तो 'केमद्रुम दोष' बनता है।", "image_prompt": "The lone Moon slowly losing its glow, surrounded by a dark, cold, isolating mist, 9:16", "approx_sec": 5.0},
            {"slide_index": 6, "caption": "व्यक्ति का मन पूरी तरह से अकेला हो जाता है।", "image_prompt": "A silhouette of a person sitting alone in the dark, hugging their knees, feeling completely abandoned, 9:16", "approx_sec": 5.0},
            {"slide_index": 7, "caption": "वे बहुत ज़्यादा ओवरथिंकिंग करते हैं।", "image_prompt": "A person's head surrounded by hundreds of tangled, chaotic thoughts and dark scribbles, causing stress, 9:16", "approx_sec": 5.0},
            {"slide_index": 8, "caption": "भीड़ में भी उन्हें खालीपन सताता है।", "image_prompt": "A person standing in a crowded, colorful party, but they appear grey, isolated, and completely disconnected, 9:16", "approx_sec": 5.0},
            {"slide_index": 9, "caption": "यह दोष बने-बनाए काम बिगाड़ सकता है।", "image_prompt": "A beautifully built house of cards suddenly collapsing due to a slight, sad breeze, representing sudden failures, 9:16", "approx_sec": 5.0},
            {"slide_index": 10, "caption": "लेकिन इसे ठीक किया जा सकता है!", "image_prompt": "A warm, bright light appearing at the end of a dark tunnel, bringing hope and healing, 9:16", "approx_sec": 5.0},
            {"slide_index": 11, "caption": "रोज़ाना भगवान शिव की आराधना करें।", "image_prompt": "A person peacefully pouring holy water (Jal) on a dark stone Shiva Linga, blue divine light glowing, 9:16", "approx_sec": 6.0},
            {"slide_index": 12, "caption": "माता की सेवा करने से यह दोष खत्म होता है।", "image_prompt": "A person lovingly massaging their old mother's feet, the mother smiling, completely curing the lonely moon, 9:16", "approx_sec": 6.0}
        ]
    },
    "ashwini_nakshatra": {
        "story_id": "ashwini_nakshatra",
        "title": "अश्विनी कुमार: देवताओं के वैद्य",
        "category": "नक्षत्र एवं ग्रह ज्ञान",
        "script_hi": "वैदिक ज्योतिष के पहले नक्षत्र 'अश्विनी' का रहस्य क्या है? अश्विनी नक्षत्र का प्रतीक 'घोड़े का सिर' (Horse's head) है, जो तेज़ गति, ऊर्जा और शुरुआत का प्रतीक है। इस नक्षत्र के देवता 'अश्विनी कुमार' हैं। अश्विनी कुमार सूर्यदेव और उनकी पत्नी संजना (जो घोड़ी के रूप में तपस्या कर रही थीं) के जुड़वां (Twin) पुत्र हैं। ये दोनों जुड़वां भाई अत्यंत रूपवान, युवा और स्वर्ण के समान चमकने वाले देवता हैं। सबसे बड़ी बात यह है कि अश्विनी कुमार 'देवताओं के वैद्य' (Doctors of the Gods) हैं। उनके पास हर प्रकार की बीमारी को ठीक करने और यहां तक कि बुढ़ापे को फिर से जवानी में बदलने की जादुई औषधियां (Medicines) हैं! जो व्यक्ति अश्विनी नक्षत्र में जन्म लेता है, वह घोड़ों की तरह तेज़ तर्रार, फुर्तीला और आकर्षक होता है। ऐसे लोगों को दूसरों की सेवा करने और उन्हें ठीक करने (Healing) का बहुत शौक होता है, इसलिए ये बहुत अच्छे डॉक्टर, वैद्य या हीलर बनते हैं। यह नक्षत्र इंसान को नई शुरुआत करने की असीम ऊर्जा देता है।",
        "estimated_speech_sec": 100.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "पहले नक्षत्र 'अश्विनी' का रहस्य क्या है?", "image_prompt": "The glowing first Nakshatra in the starry night sky, forming the distinct shape of a beautiful horse's head, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "यह तेज़ गति और शुरुआत का प्रतीक है।", "image_prompt": "A majestic white horse galloping at lightning speed across the cosmos, leaving a trail of stardust, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "इसके देवता 'अश्विनी कुमार' हैं।", "image_prompt": "Two incredibly handsome, glowing golden twin gods riding a golden chariot drawn by fast horses, 9:16", "approx_sec": 5.0},
            {"slide_index": 4, "caption": "वे सूर्यदेव और संजना के जुड़वां पुत्र हैं।", "image_prompt": "Sun God and Goddess Sanjana (in the magical form of a beautiful mare) blessing the two twin boys, 9:16", "approx_sec": 6.0},
            {"slide_index": 5, "caption": "वे 'देवताओं के वैद्य' (Doctors) हैं।", "image_prompt": "The Ashwini Kumars grinding glowing magical herbs in an ancient mortar and pestle in the heavens, 9:16", "approx_sec": 5.0},
            {"slide_index": 6, "caption": "उनके पास जादुई औषधियां हैं।", "image_prompt": "Glowing, magical potions and celestial herbs that radiate intense golden healing light, 9:16", "approx_sec": 5.0},
            {"slide_index": 7, "caption": "वे बुढ़ापे को जवानी में बदल सकते हैं! ", "image_prompt": "The twin gods offering a glowing potion to an old, frail sage, who magically transforms back into a strong young man, 9:16", "approx_sec": 6.0},
            {"slide_index": 8, "caption": "अश्विनी नक्षत्र में जन्मे लोग फुर्तीले होते हैं।", "image_prompt": "A very active, sharp-looking young person winning a running race, looking fresh and full of energy, 9:16", "approx_sec": 5.0},
            {"slide_index": 9, "caption": "वे बहुत आकर्षक और रूपवान होते हैं।", "image_prompt": "A highly charismatic person walking into a room, everyone looking at them, glowing magnetic aura, 9:16", "approx_sec": 5.0},
            {"slide_index": 10, "caption": "इन्हें दूसरों को ठीक (Heal) करने का शौक होता है।", "image_prompt": "A person lovingly bandaging the paw of an injured dog, radiating warmth and care, 9:16", "approx_sec": 5.0},
            {"slide_index": 11, "caption": "इसलिए ये बेहतरीन डॉक्टर या वैद्य बनते हैं।", "image_prompt": "A highly successful modern doctor or Ayurveda practitioner smiling, glowing with healing energy, 9:16", "approx_sec": 5.0},
            {"slide_index": 12, "caption": "यह नक्षत्र नई शुरुआत की असीम ऊर्जा देता है।", "image_prompt": "A beautiful sunrise over a calm ocean, symbolizing a fresh, energetic, and powerful new beginning, 9:16", "approx_sec": 5.0}
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
print(f"Successfully generated and injected {count} full JSON scripts (Batch 11) into the local database!")
