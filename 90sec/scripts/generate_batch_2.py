import sqlite3
import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "production_history.db")

batch_data = {
    "mahabharata_karna_kavach": {
        "story_id": "mahabharata_karna_kavach",
        "title": "कर्ण के कवच कुंडल का दान",
        "category": "महाभारत रहस्य",
        "script_hi": "दानवीर कर्ण के कवच और कुंडल का रहस्य क्या है? सूर्यपुत्र कर्ण जब जन्म लिए थे, तो उनके शरीर पर जन्म से ही अभेद्य कवच और कुंडल थे। जब तक ये उनके शरीर पर थे, दुनिया का कोई भी अस्त्र-शस्त्र उन्हें मार नहीं सकता था। कुरुक्षेत्र के युद्ध से पहले, देवराज इंद्र को अपने पुत्र अर्जुन की चिंता सताने लगी। वे जानते थे कि कर्ण को हराना असंभव है। इसलिए इंद्र ने एक गरीब ब्राह्मण का भेष बनाया और कर्ण के पास दान मांगने पहुंच गए। कर्ण, जो हर सुबह सूर्य पूजा के बाद किसी को भी खाली हाथ नहीं लौटाते थे, तुरंत समझ गए कि यह कोई साधारण ब्राह्मण नहीं, बल्कि स्वयं इंद्र हैं। इसके बावजूद, कर्ण ने बिना एक पल की हिचकिचाहट के अपने शरीर से चिपके हुए कवच और कुंडल को अपने ही हाथों से काट कर निकाल दिया और इंद्र को दान में दे दिया। उनका यह निस्वार्थ त्याग और वचनबद्धता ही उन्हें महाभारत का सबसे महान दानवीर बनाती है, जिसे इतिहास आज भी सम्मान से याद करता है।",
        "estimated_speech_sec": 75.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "कर्ण के कवच कुंडल का रहस्य?", "image_prompt": "A majestic portrait of Karna with glowing golden armor (Kavach) and earrings (Kundal) naturally attached to his body, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "जब तक ये उनके शरीर पर थे...", "image_prompt": "Karna standing invincible on a battlefield, arrows deflecting off his glowing golden chest armor, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "कोई भी अस्त्र उन्हें मार नहीं सकता था।", "image_prompt": "A glowing magical shield surrounding Karna, divine lighting, ancient Indian warrior style, 9:16", "approx_sec": 5.0},
            {"slide_index": 4, "caption": "इंद्र को अपने पुत्र अर्जुन की चिंता सताने लगी।", "image_prompt": "Lord Indra looking worried while watching Arjuna practice archery from the heavens, celestial clouds, 9:16", "approx_sec": 5.0},
            {"slide_index": 5, "caption": "इंद्र ने एक गरीब ब्राह्मण का भेष बनाया।", "image_prompt": "Lord Indra disguised as an old, frail Brahmin holding a walking stick, entering a royal camp, 9:16", "approx_sec": 5.0},
            {"slide_index": 6, "caption": "और कर्ण के पास दान मांगने पहुंच गए।", "image_prompt": "The disguised Brahmin standing before Karna, who has just finished his morning sun worship by the river, 9:16", "approx_sec": 5.0},
            {"slide_index": 7, "caption": "कर्ण तुरंत समझ गए कि यह इंद्र हैं।", "image_prompt": "Karna looking deeply into the eyes of the old Brahmin, realizing his true divine identity, intense gaze, 9:16", "approx_sec": 6.0},
            {"slide_index": 8, "caption": "इसके बावजूद, कर्ण पीछे नहीं हटे।", "image_prompt": "Karna taking out a sharp dagger with a determined and calm expression on his face, 9:16", "approx_sec": 5.0},
            {"slide_index": 9, "caption": "उन्होंने बिना हिचकिचाहट के अपना कवच काट दिया।", "image_prompt": "Karna painfully peeling off the glowing golden armor from his own chest, blood dripping slightly, dramatic, 9:16", "approx_sec": 6.0},
            {"slide_index": 10, "caption": "और इंद्र को दान में दे दिया।", "image_prompt": "Karna handing over the glowing armor and earrings to the shocked Brahmin, ultimate sacrifice, 9:16", "approx_sec": 5.0},
            {"slide_index": 11, "caption": "इंद्र इस त्याग को देखकर लज्जित हो गए।", "image_prompt": "The Brahmin revealing his true form as Lord Indra, looking down in shame and awe at Karna, 9:16", "approx_sec": 6.0},
            {"slide_index": 12, "caption": "यही कारण है कि वे सबसे महान दानवीर कहलाए।", "image_prompt": "A glorious silhouette of Karna with the sun rising behind him, representing eternal glory, 9:16", "approx_sec": 4.0}
        ]
    },
    "jyotish_jupiter_gurus": {
        "story_id": "jyotish_jupiter_gurus",
        "title": "गुरु ग्रह और ज्ञान का रहस्य",
        "category": "नक्षत्र एवं ग्रह ज्ञान",
        "script_hi": "वैदिक ज्योतिष में गुरु यानी बृहस्पति ग्रह को इतना शुभ क्यों माना जाता है? नवग्रहों में देवगुरु बृहस्पति ज्ञान, भाग्य, धर्म और विस्तार के कारक हैं। जिस व्यक्ति की कुंडली में गुरु मजबूत होता है, वह इंसान चाहे कितनी भी बड़ी मुसीबत में क्यों न फँस जाए, कोई न कोई अदृश्य शक्ति उसे बचा ही लेती है। गुरु वह प्रकाश है जो अज्ञान के अंधेरे को दूर करता है। अगर राहु भ्रम है, तो गुरु उस भ्रम को तोड़ने वाला सच है। एक मजबूत गुरु आपको सिर्फ धन ही नहीं, बल्कि सम्मान, नैतिकता और आंतरिक शांति भी देता है। भगवान राम की कुंडली में भी गुरु लग्न में विराजमान थे, जिसने उन्हें हर विपत्ति में सही रास्ता दिखाया और मर्यादा पुरुषोत्तम बनाया। इसलिए, जब आपके जीवन में गुरु ग्रह की दशा आती है, तो यह आपको अध्यात्म, सच्चे गुरुओं का सान्निध्य और जीवन का असली उद्देश्य प्रदान करती है। गुरु कृपा के बिना जीवन में कोई भी बड़ी सफलता प्राप्त करना असंभव है।",
        "estimated_speech_sec": 75.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "गुरु ग्रह को इतना शुभ क्यों माना जाता है?", "image_prompt": "A glowing majestic yellow planet Jupiter (Brihaspati) in the cosmos, radiating golden divine light, astrology art, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "बृहस्पति ज्ञान, भाग्य और धर्म के कारक हैं।", "image_prompt": "An ancient sage teaching a group of students under a banyan tree, peaceful golden hour lighting, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "जिसकी कुंडली में गुरु मजबूत होता है...", "image_prompt": "A glowing golden aura protecting a person standing calmly in the middle of chaos, 9:16", "approx_sec": 5.0},
            {"slide_index": 4, "caption": "उसे अदृश्य शक्ति बचा ही लेती है।", "image_prompt": "A divine golden hand coming down from the heavens to shield a person from a falling rock, 9:16", "approx_sec": 5.0},
            {"slide_index": 5, "caption": "गुरु वह प्रकाश है जो अज्ञान को दूर करता है।", "image_prompt": "A massive glowing candle illuminating a pitch black room, symbolic representation of wisdom, 9:16", "approx_sec": 5.0},
            {"slide_index": 6, "caption": "अगर राहु भ्रम है, तो गुरु सच है।", "image_prompt": "A bright golden light cutting through thick, dark, smoky illusions, cosmic battle of energies, 9:16", "approx_sec": 6.0},
            {"slide_index": 7, "caption": "यह सिर्फ धन नहीं, सम्मान भी देता है।", "image_prompt": "A respected king or scholar being bowed to by the public, representing honor and ethics, 9:16", "approx_sec": 5.0},
            {"slide_index": 8, "caption": "भगवान राम की कुंडली में भी गुरु लग्न में थे।", "image_prompt": "Lord Rama standing tall with his bow, a subtle glowing yellow aura (Jupiter) surrounding his form, 9:16", "approx_sec": 6.0},
            {"slide_index": 9, "caption": "जिसने उन्हें हर विपत्ति में सही रास्ता दिखाया।", "image_prompt": "A glowing compass pointing towards the light in a dark forest, symbolic of divine guidance, 9:16", "approx_sec": 5.0},
            {"slide_index": 10, "caption": "गुरु ग्रह की दशा आपको अध्यात्म की ओर ले जाती है।", "image_prompt": "A person meditating deeply, floating slightly with a glowing golden third eye and crown chakra, 9:16", "approx_sec": 6.0},
            {"slide_index": 11, "caption": "सच्चे गुरुओं का सान्निध्य प्राप्त होता है।", "image_prompt": "A seeker touching the feet of a glowing divine guru, receiving blessings and knowledge, 9:16", "approx_sec": 5.0},
            {"slide_index": 12, "caption": "गुरु कृपा के बिना बड़ी सफलता असंभव है।", "image_prompt": "A grand golden lotus blooming in the cosmos, representing ultimate success and divine grace, 9:16", "approx_sec": 4.0}
        ]
    },
    "gita_vishvarupa": {
        "story_id": "gita_vishvarupa",
        "title": "श्री कृष्ण का विश्वरूप दर्शन",
        "category": "श्रीमद्भगवद्गीता",
        "script_hi": "महाभारत के युद्ध में जब श्री कृष्ण ने अपना विश्वरूप दिखाया तो क्या हुआ? गीता के ग्यारहवें अध्याय में, जब अर्जुन ने भगवान से उनके असली ब्रह्मांडीय रूप को देखने की विनती की, तो कृष्ण ने मुस्कुराते हुए कहा कि तुम इन साधारण आँखों से मुझे नहीं देख सकते। इसलिए, कृष्ण ने अर्जुन को 'दिव्य दृष्टि' प्रदान की। जैसे ही अर्जुन ने आँखें खोलीं, उन्होंने देखा कि कृष्ण के शरीर में हजारों सूर्य एक साथ चमक रहे हैं। उनके अनगिनत मुख, अनगिनत हाथ और आँखें थीं। उस रूप में संपूर्ण ब्रह्मांड, सभी देवता, ग्रह, तारे, भूत, भविष्य और वर्तमान एक ही पल में दिखाई दे रहे थे। अर्जुन ने देखा कि कौरवों की पूरी सेना, भीष्म और द्रोण सब भगवान के मुख रूपी काल में समा रहे हैं। इस भयंकर और विशाल रूप को देखकर अर्जुन कांप उठे और उन्होंने हाथ जोड़कर कृष्ण से विनती की कि वे अपने सौम्य रूप में वापस आ जाएं। यह दर्शन हमें बताता है कि यह संपूर्ण सृष्टि ईश्वर का ही विस्तार है।",
        "estimated_speech_sec": 75.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "जब श्री कृष्ण ने अपना विश्वरूप दिखाया...", "image_prompt": "Lord Krishna transforming on the Kurukshetra battlefield, glowing light expanding from his body, epic scale, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "अर्जुन ने असली रूप देखने की विनती की।", "image_prompt": "Arjuna kneeling with folded hands in front of Krishna on the chariot, pleading respectfully, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "साधारण आँखों से यह रूप नहीं देखा जा सकता।", "image_prompt": "Krishna touching Arjuna's forehead with a glowing finger, granting him divine vision (Divya Drishti), 9:16", "approx_sec": 6.0},
            {"slide_index": 4, "caption": "कृष्ण के शरीर में हजारों सूर्य चमक रहे थे।", "image_prompt": "A blinding golden light radiating like a thousand suns, abstract divine energy, 9:16", "approx_sec": 5.0},
            {"slide_index": 5, "caption": "अनगिनत मुख, अनगिनत हाथ और आँखें...", "image_prompt": "The cosmic Vishvarupa of Krishna, featuring thousands of heads and arms holding various weapons, cosmic scale, 9:16", "approx_sec": 6.0},
            {"slide_index": 6, "caption": "संपूर्ण ब्रह्मांड उनके भीतर था।", "image_prompt": "Galaxies, stars, and planets swirling inside the colossal glowing body of Lord Krishna, 9:16", "approx_sec": 5.0},
            {"slide_index": 7, "caption": "भूत, भविष्य और वर्तमान एक ही पल में।", "image_prompt": "A surreal visual of time flowing like a glowing river inside the cosmic form of God, 9:16", "approx_sec": 5.0},
            {"slide_index": 8, "caption": "कौरवों की सेना उनके मुख में समा रही थी।", "image_prompt": "Warriors of the Kaurava army, including chariots, being pulled into the fiery, terrifying mouth of Time (Kaal), 9:16", "approx_sec": 6.0},
            {"slide_index": 9, "caption": "यह देखकर अर्जुन कांप उठे।", "image_prompt": "Arjuna trembling with fear and awe, shielding his eyes from the overwhelming blinding light, 9:16", "approx_sec": 5.0},
            {"slide_index": 10, "caption": "उन्होंने कृष्ण से सौम्य रूप में आने की विनती की।", "image_prompt": "Arjuna bowing completely to the ground in surrender, praying for the terrifying vision to stop, 9:16", "approx_sec": 5.0},
            {"slide_index": 11, "caption": "कृष्ण वापस अपने मुस्कुराते हुए रूप में आ गए।", "image_prompt": "Lord Krishna back in his beautiful two-armed form, smiling kindly at Arjuna, soft warm light, 9:16", "approx_sec": 6.0},
            {"slide_index": 12, "caption": "संपूर्ण सृष्टि ईश्वर का ही विस्तार है।", "image_prompt": "A beautiful cosmic lotus flower dissolving into the shape of the universe, spiritual peace, 9:16", "approx_sec": 4.0}
        ]
    },
    "shiva_neelkanth_origin": {
        "story_id": "shiva_neelkanth_origin",
        "title": "भगवान शिव ने विष क्यों पिया?",
        "category": "शिव पुराण",
        "script_hi": "भगवान शिव को नीलकंठ क्यों कहा जाता है? जब देवताओं और असुरों ने मिलकर क्षीरसागर (समुद्र) का मंथन किया, तो उसमें से चौदह अनमोल रत्न निकले। लेकिन अमृत से पहले, समुद्र से 'हलाहल' नाम का एक बेहद भयंकर और जानलेवा विष निकला। उस विष की गर्मी इतनी भयानक थी कि उससे पूरा ब्रह्मांड जलने लगा। देवता, असुर और मनुष्य, सब प्राण बचाने के लिए भगवान शिव की शरण में कैलाश पहुंचे। सृष्टि की रक्षा के लिए, महादेव ने उस भयंकर विष को अपनी अंजुली में लिया और पी गए। लेकिन अगर वह विष उनके पेट में जाता, तो उनके हृदय में बसने वाले भगवान राम को कष्ट होता। इसलिए माता पार्वती ने तुरंत शिव जी का गला पकड़ लिया, और विष उनके गले में ही रुक गया। उस भयानक विष के प्रभाव से भगवान शिव का कंठ (गला) पूरी तरह से नीला पड़ गया। उसी दिन से महादेव को 'नीलकंठ' के नाम से जाना जाने लगा। यह कथा हमें सिखाती है कि महान वही है जो दूसरों की भलाई के लिए बुराई का विष स्वयं पी ले।",
        "estimated_speech_sec": 80.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "भगवान शिव को नीलकंठ क्यों कहा जाता है?", "image_prompt": "Close up of Lord Shiva's majestic face with a glowing blue throat, serene expression, snowy background, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "जब समुद्र का मंथन हुआ...", "image_prompt": "Gods and Demons pulling the giant serpent Vasuki to churn the cosmic ocean around Mount Mandara, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "उसमें से चौदह अनमोल रत्न निकले।", "image_prompt": "Glowing magical artifacts like a divine horse, elephant, and gems emerging from the churning ocean, 9:16", "approx_sec": 5.0},
            {"slide_index": 4, "caption": "लेकिन अमृत से पहले हलाहल विष निकला।", "image_prompt": "A bubbling cauldron of dark, green toxic smoke emerging from the ocean, melting everything nearby, 9:16", "approx_sec": 5.0},
            {"slide_index": 5, "caption": "उस विष से पूरा ब्रह्मांड जलने लगा।", "image_prompt": "The toxic green smoke spreading across the cosmos, stars fading, beings coughing and collapsing, 9:16", "approx_sec": 5.0},
            {"slide_index": 6, "caption": "सभी देवता शिव जी की शरण में कैलाश पहुंचे।", "image_prompt": "Gods like Indra and Brahma folding hands in front of Lord Shiva who is meditating on a tiger skin, 9:16", "approx_sec": 5.0},
            {"slide_index": 7, "caption": "महादेव ने विष को अपनी अंजुली में लिया...", "image_prompt": "Lord Shiva holding the dark, glowing, toxic poison in his cupped hands, completely fearless, 9:16", "approx_sec": 6.0},
            {"slide_index": 8, "caption": "और उसे पी गए! ", "image_prompt": "Lord Shiva swallowing the glowing green poison, intense dramatic lighting from below, epic, 9:16", "approx_sec": 5.0},
            {"slide_index": 9, "caption": "माता पार्वती ने तुरंत उनका गला पकड़ लिया।", "image_prompt": "Goddess Parvati rushing and placing her gentle hands firmly on Shiva's throat to stop the poison, 9:16", "approx_sec": 6.0},
            {"slide_index": 10, "caption": "विष गले में ही रुक गया।", "image_prompt": "The toxic energy concentrating and glowing brightly right at Shiva's throat, turning it deep blue, 9:16", "approx_sec": 5.0},
            {"slide_index": 11, "caption": "उसी दिन से वे 'नीलकंठ' कहलाए।", "image_prompt": "A divine portrait of Shiva with a beautiful blue throat, radiating peace and cosmic balance, 9:16", "approx_sec": 5.0},
            {"slide_index": 12, "caption": "महान वही है जो दूसरों के लिए विष पी ले।", "image_prompt": "A symbolic image of a glowing blue lotus growing out of dark toxic mud, signifying sacrifice and purity, 9:16", "approx_sec": 5.0}
        ]
    },
    "jyotish_mars_manglik": {
        "story_id": "jyotish_mars_manglik",
        "title": "मंगल दोष का सच्चा रहस्य",
        "category": "ज्योतिष कथा",
        "script_hi": "मंगल दोष (मांगलिक) का नाम सुनते ही लोग शादियों से क्यों डरने लगते हैं? वैदिक ज्योतिष में मंगल ग्रह को अग्नि, युद्ध, और ऊर्जा का सेनापति कहा गया है। जब मंगल जन्म कुंडली के प्रथम, चतुर्थ, सप्तम, अष्टम या द्वादश भाव में बैठता है, तो उसे 'मंगल दोष' कहा जाता है। लोग सोचते हैं कि मांगलिक होने का मतलब है कि शादी टूट जाएगी या जीवनसाथी को खतरा है। लेकिन यह एक बहुत बड़ा भ्रम है! मंगल दोष वास्तव में आपके अंदर मौजूद अत्यधिक ऊर्जा (Energy) और आक्रामकता को दर्शाता है। एक मांगलिक व्यक्ति बहुत तेज़, महत्वाकांक्षी और उग्र स्वभाव का होता है। यदि उसकी शादी किसी शांत (Non-Manglik) व्यक्ति से हो जाए, तो उनकी ऊर्जा आपस में टकराती है और झगड़े होते हैं। इसलिए मांगलिक की शादी मांगलिक से की जाती है, ताकि दोनों की 'फायर एनर्जी' बराबर रहे और एक-दूसरे को समझ सकें। मंगल दोष कोई श्राप नहीं है, बल्कि यह वह ऊर्जा है जो आपको जीवन में बड़े लक्ष्य हासिल करने की शक्ति देती है। बस इसे सही दिशा देने की जरूरत है!",
        "estimated_speech_sec": 80.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "मंगल दोष का नाम सुनते ही डर क्यों?", "image_prompt": "A glowing red Mars planet with an aggressive fiery aura, casting a shadow over a wedding mandap, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "मंगल ग्रह ऊर्जा और युद्ध का सेनापति है।", "image_prompt": "Lord Mangala (Mars) as a fierce red warrior god holding a spear, riding a ram, intense energy, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "जब मंगल खास भावों में बैठता है...", "image_prompt": "An astrology Kundali chart with a glowing red 'Mangal' (Mars) in the 7th house (marriage house), 9:16", "approx_sec": 5.0},
            {"slide_index": 4, "caption": "तो उसे 'मंगल दोष' कहा जाता है।", "image_prompt": "A magnifying glass focusing on the red planet in the chart, warning signs or glowing red light, 9:16", "approx_sec": 5.0},
            {"slide_index": 5, "caption": "लोग सोचते हैं इससे जीवनसाथी को खतरा है।", "image_prompt": "A silhouette of a worried couple standing apart, a crack forming in the ground between them, 9:16", "approx_sec": 6.0},
            {"slide_index": 6, "caption": "लेकिन यह एक बहुत बड़ा भ्रम है!", "image_prompt": "A bright light shattering the crack, revealing a strong glowing chain linking two hands together, 9:16", "approx_sec": 5.0},
            {"slide_index": 7, "caption": "मंगल दोष आपके अंदर अत्यधिक ऊर्जा को दर्शाता है।", "image_prompt": "A person meditating with a powerful red fiery aura bursting from their core, symbolizing immense inner energy, 9:16", "approx_sec": 6.0},
            {"slide_index": 8, "caption": "मांगलिक व्यक्ति बहुत तेज़ और महत्वाकांक्षी होता है।", "image_prompt": "A modern successful person standing confidently on a mountain peak, red sky background, victorious, 9:16", "approx_sec": 6.0},
            {"slide_index": 9, "caption": "शांत व्यक्ति से शादी होने पर ऊर्जा टकराती है।", "image_prompt": "A raging fire on one side and calm water on the other side clashing and creating steam and chaos, 9:16", "approx_sec": 5.0},
            {"slide_index": 10, "caption": "इसलिए मांगलिक की शादी मांगलिक से की जाती है।", "image_prompt": "Two bright, matching bonfires burning together harmoniously in a dark forest, beautiful and balanced, 9:16", "approx_sec": 6.0},
            {"slide_index": 11, "caption": "ताकि दोनों की 'फायर एनर्जी' बराबर रहे।", "image_prompt": "A glowing red string of fate strongly connecting a happy couple, radiating warmth and strength, 9:16", "approx_sec": 5.0},
            {"slide_index": 12, "caption": "यह कोई श्राप नहीं, आपकी ताकत है!", "image_prompt": "A fierce red lion standing proudly, symbolizing strength, courage, and pure unbridled energy, 9:16", "approx_sec": 5.0}
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
print(f"Successfully generated and injected {count} full JSON scripts (Batch 2) into the local database!")
