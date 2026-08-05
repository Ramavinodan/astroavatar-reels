import sqlite3
import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "production_history.db")

batch_data = {
    "mahabharata_abhimanyu_chakravyuh": {
        "story_id": "mahabharata_abhimanyu_chakravyuh",
        "title": "अभिमन्यु और चक्रव्यूह का ज्ञान",
        "category": "महाभारत रहस्य",
        "script_hi": "महाभारत के सबसे युवा योद्धा अभिमन्यु ने चक्रव्यूह का रहस्य कैसे जाना? जब अभिमन्यु अपनी माता सुभद्रा के गर्भ में थे, तब एक रात अर्जुन ने सुभद्रा को चक्रव्यूह भेदने की युद्ध नीति सुनानी शुरू की। अर्जुन ने विस्तार से बताया कि चक्रव्यूह के छह द्वारों को कैसे तोड़ा जाता है। गर्भ में पल रहा शिशु अभिमन्यु यह सब सुन रहा था। लेकिन जैसे ही अर्जुन सातवें और अंतिम द्वार से बाहर निकलने की तकनीक बताने लगे, सुभद्रा को नींद आ गई। चूँकि माता सो गई थीं, इसलिए शिशु अभिमन्यु अंतिम द्वार का रहस्य नहीं सुन सका। वर्षों बाद, कुरुक्षेत्र के युद्ध में जब द्रोणाचार्य ने चक्रव्यूह की रचना की और अर्जुन वहाँ नहीं थे, तब 16 वर्षीय अभिमन्यु ने अकेले ही चक्रव्यूह में प्रवेश किया। उसने वीरता से छह द्वार तोड़ दिए, लेकिन बाहर निकलने का ज्ञान न होने के कारण कौरवों ने कायरता से उसे घेर लिया और मार डाला। यह कहानी सिखाती है कि गर्भ में पल रहा बच्चा भी बाहरी दुनिया के ज्ञान को ग्रहण करता है।",
        "estimated_speech_sec": 75.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "अभिमन्यु ने चक्रव्यूह का रहस्य कैसे जाना?", "image_prompt": "A glorious and brave 16-year-old warrior Abhimanyu holding his bow, standing alone on a battlefield, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "जब अभिमन्यु सुभद्रा के गर्भ में थे...", "image_prompt": "Pregnant Goddess Subhadra resting peacefully, glowing divine aura around her womb, ancient Indian bedroom, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "अर्जुन ने उन्हें चक्रव्यूह भेदने की नीति सुनाई।", "image_prompt": "Arjuna sitting beside pregnant Subhadra, enthusiastically explaining military strategy using hand gestures, 9:16", "approx_sec": 5.0},
            {"slide_index": 4, "caption": "गर्भ में पल रहा शिशु सब सुन रहा था।", "image_prompt": "A mystical glowing visualization of a baby inside the womb absorbing golden knowledge floating from outside, 9:16", "approx_sec": 5.0},
            {"slide_index": 5, "caption": "अर्जुन ने छह द्वार तोड़ने का रहस्य बताया।", "image_prompt": "A top-down view of a complex, glowing, spinning military formation (Chakravyuh) made of soldiers, 9:16", "approx_sec": 6.0},
            {"slide_index": 6, "caption": "लेकिन जब बाहर निकलने की बारी आई...", "image_prompt": "Arjuna leaning in to tell the final secret, dramatic candlelight casting shadows, 9:16", "approx_sec": 5.0},
            {"slide_index": 7, "caption": "सुभद्रा को नींद आ गई।", "image_prompt": "Subhadra deeply asleep, breathing peacefully, missing the rest of the conversation, 9:16", "approx_sec": 5.0},
            {"slide_index": 8, "caption": "कुरुक्षेत्र के युद्ध में जब अर्जुन नहीं थे...", "image_prompt": "Dronacharya confidently commanding the massive Kaurava army to form the deadly Chakravyuh formation, 9:16", "approx_sec": 6.0},
            {"slide_index": 9, "caption": "16 वर्षीय अभिमन्यु ने अकेले प्रवेश किया।", "image_prompt": "Young Abhimanyu fearlessly charging alone towards the massive spinning wall of enemy soldiers, 9:16", "approx_sec": 5.0},
            {"slide_index": 10, "caption": "उसने वीरता से छह द्वार तोड़ दिए।", "image_prompt": "Abhimanyu fighting fiercely, arrows flying everywhere, destroying chariots, heroic battle scene, 9:16", "approx_sec": 5.0},
            {"slide_index": 11, "caption": "लेकिन बाहर निकलने का ज्ञान न होने के कारण...", "image_prompt": "Abhimanyu surrounded by seven great Kaurava warriors attacking him simultaneously from all sides, tragic, 9:16", "approx_sec": 6.0},
            {"slide_index": 12, "caption": "गर्भ का ज्ञान भी असर डालता है।", "image_prompt": "A beautiful golden lotus blooming out of a broken chariot wheel, signifying his eternal glory, 9:16", "approx_sec": 4.0}
        ]
    },
    "shiva_parvati_vivah": {
        "story_id": "shiva_parvati_vivah",
        "title": "शिव और पार्वती का अद्भुत विवाह",
        "category": "शिव पुराण",
        "script_hi": "भगवान शिव की बारात दुनिया की सबसे अनोखी बारात क्यों थी? जब माता पार्वती ने शिव जी को पति रूप में पाने के लिए कठोर तपस्या की, तो शिव जी ने उनका प्रस्ताव स्वीकार कर लिया। विवाह के दिन, जब राजा हिमाचल के महल में शिव जी की बारात आई, तो सभी लोग डर के मारे कांप उठे। क्योंकि शिव जी किसी सजे हुए रथ पर नहीं, बल्कि एक बैल (नंदी) पर सवार थे। उनके शरीर पर भस्म लगी थी, गले में सांप लिपटे थे, और उनकी बारात में देवी-देवताओं के साथ-साथ भूत, प्रेत, पिशाच, चुड़ैलें और भयंकर दिखने वाले गण नाच रहे थे। पार्वती की माता मैनावती यह भयानक दृश्य देखकर बेहोश हो गईं। उन्होंने कहा कि मैं अपनी बेटी का विवाह ऐसे वैरागी से नहीं करूंगी! तब पार्वती जी ने शिव जी से प्रार्थना की कि वे अपने असली दिव्य रूप में आएं। शिव जी ने उनकी बात मानकर अपना सबसे सुंदर और चंद्र-समान रूप 'चंद्रशेखर' धारण किया। उनका यह मनमोहक रूप देखकर सभी देवी-देवता और इंसान मंत्रमुग्ध हो गए, और फिर बड़े हर्षोल्लास के साथ उनका विवाह संपन्न हुआ।",
        "estimated_speech_sec": 85.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "शिव जी की बारात सबसे अनोखी क्यों थी?", "image_prompt": "Lord Shiva covered in ash, wearing leopard skin, sitting on Nandi the bull, leading a wild procession, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "पार्वती जी ने कठोर तपस्या की थी।", "image_prompt": "Goddess Parvati meditating deeply in a freezing snow-covered forest, glowing with inner spiritual heat, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "विवाह के दिन जब बारात महल पहुंची...", "image_prompt": "A beautiful ancient Indian palace decorated with flowers and lights for a grand royal wedding, 9:16", "approx_sec": 5.0},
            {"slide_index": 4, "caption": "सभी लोग डर के मारे कांप उठे!", "image_prompt": "Royal guests and queens looking absolutely terrified and running away in panic, 9:16", "approx_sec": 5.0},
            {"slide_index": 5, "caption": "बारात में भूत, प्रेत और पिशाच नाच रहे थे।", "image_prompt": "Creepy, weird-looking ghosts, goblins, and dancing skeletons celebrating wildly in the wedding procession, 9:16", "approx_sec": 6.0},
            {"slide_index": 6, "caption": "शिव जी के शरीर पर भस्म और सांप थे।", "image_prompt": "Close up of Lord Shiva looking wildly calm, snakes wrapped around his neck, ash on his skin, 9:16", "approx_sec": 5.0},
            {"slide_index": 7, "caption": "पार्वती की माता यह देखकर बेहोश हो गईं।", "image_prompt": "Queen Mainavati fainting into the arms of her maids after seeing the terrifying bridegroom, 9:16", "approx_sec": 5.0},
            {"slide_index": 8, "caption": "उन्होंने कहा, 'मैं अपनी बेटी का विवाह नहीं करूंगी!'", "image_prompt": "The furious queen pointing her finger towards the palace doors, crying and refusing the marriage, 9:16", "approx_sec": 6.0},
            {"slide_index": 9, "caption": "तब पार्वती जी ने शिव जी से प्रार्थना की...", "image_prompt": "Goddess Parvati dressed as a beautiful bride, praying with folded hands to Lord Shiva in her mind, 9:16", "approx_sec": 5.0},
            {"slide_index": 10, "caption": "शिव जी ने 'चंद्रशेखर' रूप धारण किया।", "image_prompt": "Lord Shiva transforming into the most incredibly handsome cosmic prince, glowing with divine white light, 9:16", "approx_sec": 6.0},
            {"slide_index": 11, "caption": "सभी लोग उनका रूप देखकर मंत्रमुग्ध हो गए।", "image_prompt": "The crowd of royals and gods looking in complete awe and devotion at the beautiful Lord Shiva, 9:16", "approx_sec": 5.0},
            {"slide_index": 12, "caption": "और विवाह बड़े हर्षोल्लास से संपन्न हुआ।", "image_prompt": "Lord Shiva and Goddess Parvati taking the wedding vows around the holy fire, raining flower petals, 9:16", "approx_sec": 5.0}
        ]
    },
    "ganesha_head": {
        "story_id": "ganesha_head",
        "title": "गणेश जी को हाथी का सिर कैसे मिला?",
        "category": "शिव पुराण",
        "script_hi": "भगवान गणेश को हाथी का सिर कैसे मिला? एक बार माता पार्वती कैलाश पर्वत पर स्नान करने जा रही थीं। द्वार पर पहरा देने के लिए कोई नहीं था, इसलिए उन्होंने अपने शरीर के उबटन (हल्दी) से एक सुंदर बालक की मूर्ति बनाई और उसमें प्राण डाल दिए। यह बालक गणेश थे। माता ने उन्हें आदेश दिया कि जब तक वे स्नान कर रही हैं, कोई भी अंदर न आ पाए। थोड़ी देर बाद भगवान शिव वहां पहुंचे। बालक गणेश शिव को नहीं पहचानते थे, इसलिए उन्होंने महादेव को अंदर जाने से रोक दिया। शिव जी को बहुत क्रोध आया। उनके गणों ने बालक से युद्ध किया, लेकिन गणेश ने सबको हरा दिया। अंततः क्रोध में आकर शिव जी ने अपने त्रिशूल से गणेश का सिर धड़ से अलग कर दिया। जब पार्वती जी बाहर आईं और अपने पुत्र को मृत देखा, तो वे क्रोध से पूरी सृष्टि को नष्ट करने लगीं। उन्हें शांत करने के लिए, शिव जी ने भगवान विष्णु को उत्तर दिशा में भेजा। विष्णु जी एक ऐसे हाथी का सिर ले आए जो उत्तर की ओर सिर करके सो रहा था। शिव जी ने वह सिर बालक के धड़ पर लगा दिया और उन्हें पुनर्जीवित कर दिया। तभी से वे 'गजानन' कहलाए।",
        "estimated_speech_sec": 85.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "गणेश जी को हाथी का सिर कैसे मिला?", "image_prompt": "A cute and divine boy made of glowing golden turmeric clay, opening his eyes for the first time, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "माता पार्वती ने उबटन से बालक बनाया।", "image_prompt": "Goddess Parvati lovingly touching the cheek of the newly created boy, ancient Indian cave setting, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "और उसे पहरा देने का आदेश दिया।", "image_prompt": "The boy holding a wooden staff, standing bravely guard outside a large beautifully carved wooden door, 9:16", "approx_sec": 5.0},
            {"slide_index": 4, "caption": "तभी वहां भगवान शिव आ गए।", "image_prompt": "Lord Shiva arriving at the door holding his Trishul, glowing with divine authority, 9:16", "approx_sec": 5.0},
            {"slide_index": 5, "caption": "गणेश ने उन्हें अंदर जाने से रोक दिया।", "image_prompt": "The little boy boldly blocking the path of the giant Lord Shiva with his staff, confident expression, 9:16", "approx_sec": 6.0},
            {"slide_index": 6, "caption": "शिव जी को बहुत क्रोध आया।", "image_prompt": "Lord Shiva looking furious, his eyes burning with anger, dark clouds gathering above, 9:16", "approx_sec": 5.0},
            {"slide_index": 7, "caption": "उन्होंने त्रिशूल से बालक का सिर काट दिया।", "image_prompt": "A glowing Trishul flying through the air and slicing, dramatic silhouette lighting, 9:16", "approx_sec": 5.0},
            {"slide_index": 8, "caption": "पार्वती जी क्रोध से सृष्टि नष्ट करने लगीं!", "image_prompt": "Goddess Parvati transforming into a terrifying angry form, cosmic fire erupting around her, 9:16", "approx_sec": 6.0},
            {"slide_index": 9, "caption": "शिव जी ने तुरंत उपाय सोचा।", "image_prompt": "Lord Shiva looking deeply remorseful and commanding Lord Vishnu to find a solution, 9:16", "approx_sec": 5.0},
            {"slide_index": 10, "caption": "विष्णु जी एक हाथी का सिर लेकर आए।", "image_prompt": "Lord Vishnu holding the magnificent, glowing head of a divine elephant (Airavata species), 9:16", "approx_sec": 5.0},
            {"slide_index": 11, "caption": "शिव जी ने सिर लगाकर उन्हें पुनर्जीवित किया।", "image_prompt": "Lord Shiva attaching the elephant head to the boy's body, golden healing magic sealing it, 9:16", "approx_sec": 6.0},
            {"slide_index": 12, "caption": "और वे 'गजानन' कहलाए!", "image_prompt": "Lord Ganesha in his complete elephant-headed form, smiling and holding a laddu, glowing aura, 9:16", "approx_sec": 5.0}
        ]
    },
    "kartikeya_peacock": {
        "story_id": "kartikeya_peacock",
        "title": "कार्तिकेय और मोर की सवारी",
        "category": "शिव पुराण",
        "script_hi": "भगवान कार्तिकेय (मुरुगन) की सवारी मोर कैसे बना? तारकासुर का वध करने के बाद, उसके भाई शूरपद्मन (Surapadman) ने देवताओं पर हमला कर दिया। शूरपद्मन बहुत ही मायावी और शक्तिशाली असुर था। उसे वरदान था कि वह शिव की शक्ति के अलावा किसी भी चीज़ से नहीं मर सकता। इसलिए भगवान कार्तिकेय, जो शिव के तेज़ से उत्पन्न हुए थे, ने उससे युद्ध किया। युद्ध के दौरान, शूरपद्मन ने बचने के लिए एक विशाल आम के पेड़ का रूप धारण कर लिया। भगवान कार्तिकेय ने अपने दिव्य 'वेल' (भाले) से उस पेड़ को दो हिस्सों में चीर दिया। पेड़ का एक हिस्सा एक सुंदर 'मोर' बन गया और दूसरा हिस्सा एक 'मुर्गा' बन गया। शूरपद्मन ने अपनी गलती मान ली और भगवान की शरण में आ गया। कार्तिकेय ने उसकी वीरता से प्रसन्न होकर मोर को अपना शाश्वत वाहन (सवारी) बना लिया और मुर्गे को अपने युद्ध के झंडे (ध्वज) पर स्थान दिया। इस तरह, भगवान कार्तिकेय ने अपने सबसे बड़े शत्रु को अपनी शरण देकर हमेशा के लिए अपने साथ जोड़ लिया।",
        "estimated_speech_sec": 80.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "कार्तिकेय की सवारी मोर कैसे बना?", "image_prompt": "Lord Kartikeya (Murugan) looking fiercely handsome, sitting on a majestic glowing peacock, holding a spear, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "शूरपद्मन नाम के असुर ने हमला किया।", "image_prompt": "A terrifying demon Surapadman radiating dark energy, standing aggressively on a battlefield, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "वह बहुत मायावी और शक्तिशाली था।", "image_prompt": "The demon transforming his shape magically into shadows and beasts, dark magic aura, 9:16", "approx_sec": 5.0},
            {"slide_index": 4, "caption": "भगवान कार्तिकेय ने उससे युद्ध किया।", "image_prompt": "Lord Kartikeya holding his glowing golden Vel (spear), charging towards the demon, dynamic action, 9:16", "approx_sec": 6.0},
            {"slide_index": 5, "caption": "असुर ने एक विशाल आम के पेड़ का रूप ले लिया।", "image_prompt": "A massive, terrifying, dark magical mango tree with roots tearing up the ground, glowing red eyes in the bark, 9:16", "approx_sec": 6.0},
            {"slide_index": 6, "caption": "कार्तिकेय ने अपने दिव्य 'वेल' से प्रहार किया।", "image_prompt": "Lord Kartikeya throwing the glowing golden Vel straight at the massive tree, sparks flying, 9:16", "approx_sec": 5.0},
            {"slide_index": 7, "caption": "और पेड़ को दो हिस्सों में चीर दिया।", "image_prompt": "The glowing spear splitting the massive tree perfectly down the middle, blinding light bursting out, 9:16", "approx_sec": 5.0},
            {"slide_index": 8, "caption": "एक हिस्सा सुंदर मोर बन गया...", "image_prompt": "One half of the tree magically transforming into a gigantic, beautiful blue and green peacock, 9:16", "approx_sec": 5.0},
            {"slide_index": 9, "caption": "और दूसरा हिस्सा एक मुर्गा बन गया।", "image_prompt": "The other half transforming into a bright, colorful, aggressive rooster, mythological style, 9:16", "approx_sec": 5.0},
            {"slide_index": 10, "caption": "असुर ने कार्तिकेय की शरण ली।", "image_prompt": "The peacock bowing its head in deep respect to Lord Kartikeya, admitting defeat and seeking grace, 9:16", "approx_sec": 6.0},
            {"slide_index": 11, "caption": "कार्तिकेय ने मोर को अपनी सवारी बना लिया।", "image_prompt": "Lord Kartikeya affectionately petting the giant peacock and sitting on its back, divine golden aura, 9:16", "approx_sec": 5.0},
            {"slide_index": 12, "caption": "और मुर्गे को अपने झंडे पर स्थान दिया।", "image_prompt": "A majestic war flag fluttering in the wind with the emblem of a glowing rooster on it, 9:16", "approx_sec": 4.0}
        ]
    },
    "ganga_descent": {
        "story_id": "ganga_descent",
        "title": "गंगा का धरती पर अवतरण",
        "category": "शिव पुराण",
        "script_hi": "गंगा नदी धरती पर कैसे आई? राजा भगीरथ के साठ हज़ार पूर्वज कपिल मुनि के श्राप से भस्म हो गए थे। उनकी मुक्ति के लिए भगीरथ ने कठोर तपस्या की ताकि पवित्र गंगा नदी स्वर्ग से धरती पर आ सके। माता गंगा धरती पर आने को तैयार हो गईं, लेकिन उनका वेग इतना प्रचंड था कि अगर वे सीधे धरती पर गिरतीं, तो पूरी पृथ्वी पाताल में बह जाती। इस विनाश को रोकने के लिए, भगीरथ ने भगवान शिव की तपस्या की। महादेव ने उनकी प्रार्थना सुनी और अपने बाल खोलकर हिमालय पर खड़े हो गए। जब गंगा स्वर्ग से भयंकर गर्जना के साथ नीचे गिरीं, तो शिव जी ने उन्हें अपनी जटाओं (बालों) में कैद कर लिया! गंगा कई दिनों तक शिव जी की जटाओं में भटकती रहीं। फिर, महादेव ने अपनी एक जटा खोली और गंगा को एक शांत नदी के रूप में धरती पर बहने दिया। इसी जल से भगीरथ के पूर्वजों को मोक्ष मिला। तभी से भगवान शिव को 'गंगाधर' भी कहा जाता है।",
        "estimated_speech_sec": 80.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "गंगा नदी स्वर्ग से धरती पर कैसे आई?", "image_prompt": "A glowing heavenly river flowing through the cosmos among the stars in Swarga (Heaven), 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "राजा भगीरथ के पूर्वज भस्म हो गए थे।", "image_prompt": "Sixty thousand princes burning into ashes from the fiery gaze of Sage Kapila, ancient myth, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "भगीरथ ने गंगा को धरती पर लाने की तपस्या की।", "image_prompt": "King Bhagiratha standing on one leg in deep meditation, praying towards the heavens, snowy peaks, 9:16", "approx_sec": 5.0},
            {"slide_index": 4, "caption": "लेकिन गंगा का वेग बहुत प्रचंड था।", "image_prompt": "A terrifyingly massive waterfall of cosmic water threatening to crush the earth, apocalyptic feeling, 9:16", "approx_sec": 5.0},
            {"slide_index": 5, "caption": "धरती पाताल में बह जाती!", "image_prompt": "The globe of Earth cracking and sinking into deep dark cosmic waters, dramatic disaster concept, 9:16", "approx_sec": 5.0},
            {"slide_index": 6, "caption": "भगीरथ ने भगवान शिव से प्रार्थना की।", "image_prompt": "King Bhagiratha begging with folded hands in front of Lord Shiva's massive meditating form, 9:16", "approx_sec": 5.0},
            {"slide_index": 7, "caption": "महादेव ने अपने बाल खोल दिए।", "image_prompt": "Lord Shiva standing tall on Mount Kailash, opening his massive, infinitely long matted hair (Jata), 9:16", "approx_sec": 6.0},
            {"slide_index": 8, "caption": "गंगा भयंकर गर्जना के साथ नीचे गिरीं...", "image_prompt": "The powerful glowing river crashing down directly from the sky onto Shiva's head, splashing wildly, 9:16", "approx_sec": 5.0},
            {"slide_index": 9, "caption": "और शिव जी की जटाओं में कैद हो गईं!", "image_prompt": "The massive river trapped and swirling endlessly inside the cosmic maze of Shiva's matted hair, 9:16", "approx_sec": 6.0},
            {"slide_index": 10, "caption": "गंगा का अहंकार टूट गया।", "image_prompt": "Goddess Ganga looking humbled and calm, floating gently within the hair of Shiva, 9:16", "approx_sec": 5.0},
            {"slide_index": 11, "caption": "शिव जी ने एक जटा से उन्हें बाहर निकाला।", "image_prompt": "Lord Shiva pulling out one strand of hair, releasing a gentle, calm, sparkling stream of water, 9:16", "approx_sec": 5.0},
            {"slide_index": 12, "caption": "तभी से महादेव 'गंगाधर' कहलाए।", "image_prompt": "A beautiful majestic portrait of Lord Shiva with the river Ganga sprouting from his hair, divine peace, 9:16", "approx_sec": 5.0}
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
print(f"Successfully generated and injected {count} full JSON scripts (Batch 3) into the local database!")
