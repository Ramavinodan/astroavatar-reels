import sqlite3
import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "production_history.db")

batch_data = {
    "jatayu_sacrifice": {
        "story_id": "jatayu_sacrifice",
        "title": "जटायु का बलिदान",
        "category": "रामायण कथा",
        "script_hi": "रामायण में गिद्धराज जटायु का बलिदान क्यों इतना महान है? जब रावण माता सीता का हरण करके उन्हें पुष्पक विमान में लंका ले जा रहा था, तब सीता जी ने मदद के लिए पुकार लगाई। उनकी आवाज़ सुनकर वृद्ध जटायु वहां आ गए। जटायु जानते थे कि रावण एक अत्यंत शक्तिशाली राक्षस है और वे अब बहुत बूढ़े हो चुके हैं। फिर भी, एक असहाय स्त्री की रक्षा करना उन्होंने अपना धर्म समझा। जटायु ने रावण के रथ पर भयंकर हमला कर दिया। उन्होंने अपने पंजों और चोंच से रावण को लहूलुहान कर दिया और उसका रथ तोड़ डाला। अंततः रावण ने छल से अपनी तलवार निकालकर जटायु के दोनों पंख काट दिए। जटायु लहूलुहान होकर ज़मीन पर गिर पड़े। जब भगवान राम सीता को खोजते हुए वहां पहुंचे, तब प्राण त्यागने से पहले जटायु ने ही राम को बताया कि रावण सीता को दक्षिण दिशा की ओर ले गया है। श्री राम ने पिता के समान जटायु का अंतिम संस्कार अपने हाथों से किया। जटायु का बलिदान सिखाता है कि परिणाम चाहे जो हो, धर्म और रक्षा के लिए लड़ना ही असली वीरता है।",
        "estimated_speech_sec": 85.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "गिद्धराज जटायु का बलिदान महान क्यों है?", "image_prompt": "A majestic giant vulture (Jatayu) flying in the ancient Indian skies, wise and powerful, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "रावण पुष्पक विमान में सीता का हरण कर रहा था।", "image_prompt": "Demon king Ravana flying in his magical floating chariot (Pushpaka Vimana) with a captive Goddess Sita, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "सीता जी ने मदद के लिए पुकार लगाई।", "image_prompt": "Goddess Sita looking out of the flying chariot, crying and throwing her jewelry down as a trail, 9:16", "approx_sec": 5.0},
            {"slide_index": 4, "caption": "वृद्ध जटायु ने उनकी आवाज़ सुनी।", "image_prompt": "Old but strong Jatayu perched on a high mountain cliff, looking up sharply at the sky with fierce eyes, 9:16", "approx_sec": 5.0},
            {"slide_index": 5, "caption": "जटायु ने बिना डरे रावण पर हमला कर दिया।", "image_prompt": "Jatayu flying fiercely towards Ravana's chariot, clashing mid-air, dynamic action scene, 9:16", "approx_sec": 6.0},
            {"slide_index": 6, "caption": "उन्होंने रावण के रथ को तोड़ डाला।", "image_prompt": "Jatayu using his sharp talons and beak to destroy the wooden parts of the magical chariot, 9:16", "approx_sec": 5.0},
            {"slide_index": 7, "caption": "लेकिन रावण ने छल से तलवार निकाल ली।", "image_prompt": "Furious Ravana drawing a large glowing dark sword, preparing to strike the giant bird, 9:16", "approx_sec": 5.0},
            {"slide_index": 8, "caption": "और जटायु के दोनों पंख काट दिए।", "image_prompt": "Ravana slashing the sword, cutting Jatayu's massive wings, blood in the air, tragic moment, 9:16", "approx_sec": 6.0},
            {"slide_index": 9, "caption": "जटायु ज़मीन पर गिर पड़े।", "image_prompt": "The giant wounded bird falling heavily into the forest dirt, losing his strength, 9:16", "approx_sec": 5.0},
            {"slide_index": 10, "caption": "श्री राम ने उन्हें खोजते हुए पाया।", "image_prompt": "Lord Rama kneeling down in the forest, gently resting the dying Jatayu's head on his lap, crying, 9:16", "approx_sec": 6.0},
            {"slide_index": 11, "caption": "जटायु ने रावण की दिशा बताई।", "image_prompt": "Jatayu weakly pointing his wing towards the South, speaking his final words to Lord Rama, 9:16", "approx_sec": 5.0},
            {"slide_index": 12, "caption": "श्री राम ने अपने हाथों से अंतिम संस्कार किया।", "image_prompt": "Lord Rama performing the holy cremation rituals for Jatayu, fire glowing, divine respect, 9:16", "approx_sec": 5.0}
        ]
    },
    "kumbhakarna_sleep": {
        "story_id": "kumbhakarna_sleep",
        "title": "कुंभकर्ण की नींद का रहस्य",
        "category": "रामायण कथा",
        "script_hi": "रावण का भाई कुंभकर्ण 6 महीने सोता और 1 दिन क्यों जागता था? कुंभकर्ण एक विशाल और अत्यंत शक्तिशाली राक्षस था, जिसके शरीर और भूख का कोई अंत नहीं था। एक बार कुंभकर्ण ने अपने भाई रावण और विभीषण के साथ ब्रह्मा जी की घोर तपस्या की। ब्रह्मा जी प्रसन्न होकर वरदान देने आए। लेकिन देवी सरस्वती जानती थीं कि अगर कुंभकर्ण ने कोई भयंकर वरदान मांग लिया, तो वह भूख से पूरी दुनिया को खा जाएगा। इसलिए सरस्वती जी ने कुंभकर्ण की जीभ (वाणी) पर वास कर लिया। कुंभकर्ण असल में ब्रह्मा जी से 'इंद्रासन' (इंद्र का सिंहासन) मांगना चाहता था, लेकिन सरस्वती के प्रभाव के कारण उसके मुँह से 'निद्रासन' (हमेशा की नींद) निकल गया! ब्रह्मा जी ने तुरंत 'तथास्तु' कह दिया। रावण ने ब्रह्मा जी से विनती की कि वे इस वरदान को थोड़ा बदल दें। तब ब्रह्मा जी ने वरदान में सुधार किया कि कुंभकर्ण 6 महीने तक सोएगा और सिर्फ 1 दिन के लिए जागेगा। जब रामायण के युद्ध में उसे जगाया गया, तो उसने रावण को समझाया था कि राम साक्षात ईश्वर हैं, लेकिन फिर भी उसने एक भाई के नाते रावण की तरफ से युद्ध किया और वीरगति को प्राप्त हुआ।",
        "estimated_speech_sec": 95.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "कुंभकर्ण 6 महीने क्यों सोता था?", "image_prompt": "A gigantic, muscular demon, Kumbhakarna, sleeping heavily inside a massive, dark cave, snoring loudly, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "वह एक विशाल और शक्तिशाली राक्षस था।", "image_prompt": "Kumbhakarna walking, his footsteps shaking the earth, towering over normal sized trees and humans, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "उसने ब्रह्मा जी की घोर तपस्या की।", "image_prompt": "Kumbhakarna standing on one leg in a forest, meditating with folded hands, fire all around him, 9:16", "approx_sec": 5.0},
            {"slide_index": 4, "caption": "ब्रह्मा जी प्रसन्न होकर वरदान देने आए।", "image_prompt": "Lord Brahma appearing in the sky, sitting on a lotus, glowing with divine golden light, 9:16", "approx_sec": 5.0},
            {"slide_index": 5, "caption": "सरस्वती जी को चिंता हुई कि यह दुनिया खा जाएगा।", "image_prompt": "Goddess Saraswati holding her Veena, looking worried from the heavens down at the hungry demon, 9:16", "approx_sec": 6.0},
            {"slide_index": 6, "caption": "उन्होंने कुंभकर्ण की जीभ पर वास कर लिया।", "image_prompt": "A magical glowing white aura of Goddess Saraswati entering the mouth of Kumbhakarna, 9:16", "approx_sec": 5.0},
            {"slide_index": 7, "caption": "वह 'इंद्रासन' मांगना चाहता था...", "image_prompt": "A thought bubble of Kumbhakarna showing him sitting proudly on the golden throne of heaven, 9:16", "approx_sec": 5.0},
            {"slide_index": 8, "caption": "पर मुँह से 'निद्रासन' निकल गया!", "image_prompt": "Kumbhakarna speaking the wrong word, looking immediately confused and shocked at himself, 9:16", "approx_sec": 5.0},
            {"slide_index": 9, "caption": "ब्रह्मा जी ने 'तथास्तु' कह दिया।", "image_prompt": "Lord Brahma raising his right hand and granting the boon, golden magical dust sealing the fate, 9:16", "approx_sec": 5.0},
            {"slide_index": 10, "caption": "रावण के कहने पर वरदान में सुधार हुआ।", "image_prompt": "Ravana pleading with Lord Brahma, and Brahma holding up 6 fingers indicating 6 months of sleep, 9:16", "approx_sec": 6.0},
            {"slide_index": 11, "caption": "युद्ध में उठने पर उसने रावण को सच बताया।", "image_prompt": "A giant Kumbhakarna eating massive piles of food while advising Ravana that Rama is God, 9:16", "approx_sec": 6.0},
            {"slide_index": 12, "caption": "फिर भी भाई के लिए लड़कर वीरगति पाई।", "image_prompt": "Giant Kumbhakarna fighting bravely on the battlefield of Lanka, holding a massive mace, loyal to the end, 9:16", "approx_sec": 5.0}
        ]
    },
    "ravana_shiva_tandava": {
        "story_id": "ravana_shiva_tandava",
        "title": "रावण और शिव तांडव स्तोत्र",
        "category": "शिव पुराण",
        "script_hi": "शिव तांडव स्तोत्र की रचना रावण ने किस भयंकर परिस्थिति में की थी? लंकापति रावण अत्यंत अभिमानी और शक्तिशाली था। एक बार वह अपने पुष्पक विमान में जा रहा था, लेकिन उसका विमान कैलाश पर्वत के ऊपर से नहीं जा सका क्योंकि वहां शिव और पार्वती बैठे थे। रावण के अहंकार को ठेस पहुंची और उसने सोचा कि वह पूरे कैलाश पर्वत को ही उखाड़ कर लंका ले जाएगा! उसने अपनी बीस भुजाओं से कैलाश को नीचे से उठा लिया। पर्वत हिलने लगा। तब भगवान शिव ने मुस्कुराते हुए केवल अपने पैर का अंगूठा पर्वत पर दबा दिया। शिव के अंगूठे का भार इतना भयंकर था कि पर्वत वापस अपनी जगह बैठ गया और रावण के हाथ पर्वत के नीचे बुरी तरह कुचले गए। रावण दर्द से भयंकर चीखने लगा, जिसकी आवाज़ पूरे ब्रह्मांड में गूंज गई। जब रावण को एहसास हुआ कि वह साक्षात महादेव से टकराया है, तो उसने क्षमा मांगने के लिए संस्कृत में एक अत्यंत शक्तिशाली और लयबद्ध कविता गानी शुरू की, जिसे 'शिव तांडव स्तोत्र' कहा जाता है। उसकी इस अनन्य भक्ति से प्रसन्न होकर शिव ने उसे माफ कर दिया और उसे एक शक्तिशाली तलवार 'चंद्रहास' भेंट की।",
        "estimated_speech_sec": 95.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "शिव तांडव स्तोत्र की रचना कैसे हुई?", "image_prompt": "Demon King Ravana singing passionately with his 10 heads, magical glowing Sanskrit verses floating in the air, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "रावण पुष्पक विमान में जा रहा था।", "image_prompt": "Ravana flying proudly in his magnificent floating Vimana above the clouds, arrogant expression, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "कैलाश पर्वत ने उसका रास्ता रोक दिया।", "image_prompt": "The majestic, glowing, snow-covered Mount Kailash standing tall, blocking the path of the Vimana, 9:16", "approx_sec": 5.0},
            {"slide_index": 4, "caption": "अहंकारी रावण ने पर्वत को उखाड़ने की ठानी।", "image_prompt": "Ravana jumping down and placing his twenty muscular arms under the massive mountain, trying to lift it, 9:16", "approx_sec": 6.0},
            {"slide_index": 5, "caption": "पर्वत हिलने लगा!", "image_prompt": "The entire Mount Kailash shaking, rocks falling, causing a massive earthquake in the region, 9:16", "approx_sec": 5.0},
            {"slide_index": 6, "caption": "शिव जी ने मुस्कुराकर अपना अंगूठा दबाया।", "image_prompt": "Lord Shiva, sitting peacefully with Parvati, slightly pressing down his glowing big toe on the ground, 9:16", "approx_sec": 6.0},
            {"slide_index": 7, "caption": "रावण के हाथ बुरी तरह कुचले गए।", "image_prompt": "The massive mountain crashing back down, trapping and crushing Ravana's multiple hands under the heavy rocks, 9:16", "approx_sec": 5.0},
            {"slide_index": 8, "caption": "वह दर्द से भयंकर चीखने लगा।", "image_prompt": "Ravana screaming in extreme agony, his ten faces showing intense pain, veins popping, 9:16", "approx_sec": 5.0},
            {"slide_index": 9, "caption": "उसे अपनी गलती का एहसास हुआ।", "image_prompt": "Ravana closing his eyes, realizing he challenged the supreme Lord Shiva, surrendering completely, 9:16", "approx_sec": 5.0},
            {"slide_index": 10, "caption": "उसने 'शिव तांडव स्तोत्र' गाना शुरू किया।", "image_prompt": "Ravana using his trapped arms to play music on his own nerves, singing the rhythmic Tandava Stotram, 9:16", "approx_sec": 6.0},
            {"slide_index": 11, "caption": "भक्ति से प्रसन्न होकर शिव ने उसे माफ किया।", "image_prompt": "Lord Shiva appearing before the freed Ravana, looking pleased and blessing him with a glowing hand, 9:16", "approx_sec": 5.0},
            {"slide_index": 12, "caption": "और उसे 'चंद्रहास' खड्ग भेंट की।", "image_prompt": "Lord Shiva giving Ravana a terrifying, glowing crescent moon-shaped sword (Chandrahas), 9:16", "approx_sec": 5.0}
        ]
    },
    "shabari_berries": {
        "story_id": "shabari_berries",
        "title": "शबरी के जूठे बेर",
        "category": "रामायण कथा",
        "script_hi": "भगवान राम ने शबरी के जूठे बेर क्यों खाए? शबरी एक भीलनी (आदिवासी) महिला थी, जो मातंग ऋषि के आश्रम में रहती थी। ऋषि ने प्राण त्यागने से पहले शबरी को वरदान दिया था कि एक दिन स्वयं भगवान राम उससे मिलने उसकी कुटिया में आएंगे। इस विश्वास के साथ शबरी हज़ारों दिनों तक रोज़ जंगल का रास्ता साफ करती और ताज़े मीठे बेर चुनकर लाती। बेर मीठे हैं या खट्टे, यह जांचने के लिए वह हर एक बेर को थोड़ा सा चखकर (जूठा करके) रखती थी। कई सालों के इंतज़ार के बाद, जब शबरी अत्यंत बूढ़ी हो गई, तब अंततः श्री राम लक्ष्मण के साथ सीता माता की खोज करते हुए वहां पहुंचे। शबरी की खुशी का ठिकाना नहीं रहा। उसने प्रेम भाव से अपने चखे हुए जूठे बेर राम को दिए। लक्ष्मण जी यह देखकर अचंभित रह गए और उन्होंने जूठे बेर खाने से मना कर दिया। लेकिन श्री राम, जो केवल सच्ची भक्ति के भूखे हैं, ने बड़े प्रेम और आनंद से उन जूठे बेरों को खाया। यह कथा हमें सिखाती है कि भगवान के लिए ना कोई जात-पात है, ना छुआछूत; वे केवल मन का सच्चा भाव देखते हैं।",
        "estimated_speech_sec": 95.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "भगवान राम ने शबरी के जूठे बेर क्यों खाए?", "image_prompt": "Lord Rama smiling warmly while eating a small wild berry (ber) from a leaf plate held by an old tribal woman, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "शबरी मातंग ऋषि के आश्रम में रहती थी।", "image_prompt": "Young tribal woman Shabari respectfully serving an old, wise sage (Matanga Rishi) in a simple forest ashram, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "ऋषि ने कहा था, 'राम तुमसे मिलने आएंगे।'", "image_prompt": "The dying sage blessing Shabari, pointing towards the path with a glowing hand, instilling deep faith, 9:16", "approx_sec": 6.0},
            {"slide_index": 4, "caption": "वह रोज़ राम के इंतज़ार में रास्ता साफ करती।", "image_prompt": "Old Shabari diligently sweeping the dirt path with a broom made of leaves, eagerly waiting, 9:16", "approx_sec": 5.0},
            {"slide_index": 5, "caption": "और रोज़ ताज़े मीठे बेर चुनकर लाती।", "image_prompt": "Old Shabari carefully picking wild berries from bushes in the forest, holding a small woven basket, 9:16", "approx_sec": 5.0},
            {"slide_index": 6, "caption": "बेर मीठे हों, इसलिए वह उन्हें चखकर रखती।", "image_prompt": "Shabari taking a small bite of a berry, checking if it is sweet, and putting the good ones in a bowl, 9:16", "approx_sec": 6.0},
            {"slide_index": 7, "caption": "सालों बाद, अंततः राम और लक्ष्मण वहां पहुंचे।", "image_prompt": "Lord Rama and Lakshmana, carrying their bows, walking towards Shabari's humble hut, divine glow, 9:16", "approx_sec": 5.0},
            {"slide_index": 8, "caption": "शबरी की खुशी का ठिकाना नहीं रहा।", "image_prompt": "Shabari falling to her knees with tears of extreme joy flowing from her eyes upon seeing Lord Rama, 9:16", "approx_sec": 5.0},
            {"slide_index": 9, "caption": "उसने प्रेम से अपने जूठे बेर परोसे।", "image_prompt": "Shabari lovingly offering the bowl of pre-tasted berries to Lord Rama with trembling, devoted hands, 9:16", "approx_sec": 5.0},
            {"slide_index": 10, "caption": "लक्ष्मण जी यह देखकर अचंभित रह गए।", "image_prompt": "Lakshmana looking shocked and hesitant, refusing to eat the half-bitten berries, 9:16", "approx_sec": 5.0},
            {"slide_index": 11, "caption": "लेकिन राम ने बड़े आनंद से उन्हें खाया।", "image_prompt": "Lord Rama eating the berry with closed eyes, showing an expression of extreme satisfaction and bliss, 9:16", "approx_sec": 6.0},
            {"slide_index": 12, "caption": "भगवान केवल मन का सच्चा भाव देखते हैं।", "image_prompt": "A glowing lotus floating in a simple clay bowl, symbolizing pure devotion over social status, 9:16", "approx_sec": 5.0}
        ]
    },
    "setu_bandhan_squirrel": {
        "story_id": "setu_bandhan_squirrel",
        "title": "राम सेतु और छोटी गिलहरी",
        "category": "रामायण कथा",
        "script_hi": "राम सेतु के निर्माण में एक छोटी सी गिलहरी का क्या योगदान था? जब श्री राम की वानर सेना लंका जाने के लिए समुद्र पर विशाल पत्थरों से राम सेतु बना रही थी, तब बड़े-बड़े वानर और भालू भारी-भरकम चट्टानें और पहाड़ उठाकर समुद्र में डाल रहे थे। उस समय एक छोटी सी गिलहरी भी राम की भक्ति में वहां आ गई। वह पहले समुद्र के पानी में जाकर गीली होती, फिर रेत में लेट जाती जिससे रेत उसके शरीर पर चिपक जाती, और फिर पुल पर जाकर उस रेत को झाड़ देती थी। गिलहरी बार-बार ऐसा कर रही थी, ताकि पत्थरों के बीच की दरारें भर जाएं। कुछ वानरों ने उसे देखकर मज़ाक उड़ाया और कहा कि तेरी चुटकी भर रेत से यह महासागर कैसे पटेगा? जब श्री राम ने यह देखा, तो उन्होंने वानरों को रोका। भगवान राम ने उस छोटी सी गिलहरी को अपने हाथ में उठाया और प्यार से उसकी पीठ पर अपनी तीन उंगलियां फेरीं। कहते हैं कि आज भी गिलहरियों की पीठ पर जो तीन सफेद धारियां होती हैं, वो भगवान राम के उंगलियों के ही निशान हैं! यह कथा बताती है कि सेवा का आकार नहीं, बल्कि उसके पीछे का समर्पण और भाव मायने रखता है।",
        "estimated_speech_sec": 95.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "राम सेतु बनाने में गिलहरी का क्या योगदान था?", "image_prompt": "A cute little Indian palm squirrel holding a tiny pebble, standing in front of the massive ocean, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "वानर सेना समुद्र पर विशाल सेतु बना रही थी।", "image_prompt": "Giant muscular Vanaras (monkey warriors) throwing massive boulders with 'Rama' written on them into the sea, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "एक छोटी सी गिलहरी भी वहां आ गई।", "image_prompt": "The tiny squirrel looking up with deep devotion at the giant boulders being placed in the water, 9:16", "approx_sec": 5.0},
            {"slide_index": 4, "caption": "वह पहले समुद्र के पानी में गीली होती...", "image_prompt": "The small squirrel dipping itself into the ocean waves, getting its fur completely wet, 9:16", "approx_sec": 5.0},
            {"slide_index": 5, "caption": "फिर रेत में लेटकर रेत चिपकाती।", "image_prompt": "The wet squirrel rolling around in the golden beach sand, covering itself completely in sand, 9:16", "approx_sec": 5.0},
            {"slide_index": 6, "caption": "और पुल पर जाकर रेत को झाड़ देती।", "image_prompt": "The sandy squirrel standing on the massive rocks of the bridge, vigorously shaking the sand into the gaps, 9:16", "approx_sec": 6.0},
            {"slide_index": 7, "caption": "ताकि पत्थरों के बीच की दरारें भर जाएं।", "image_prompt": "Close up of the tiny sand grains filling the small gaps between the giant floating boulders, 9:16", "approx_sec": 5.0},
            {"slide_index": 8, "caption": "वानरों ने उसका मज़ाक उड़ाया।", "image_prompt": "A giant monkey warrior laughing and pointing a finger at the tiny squirrel, mocking its small effort, 9:16", "approx_sec": 5.0},
            {"slide_index": 9, "caption": "श्री राम ने वानरों को रोका।", "image_prompt": "Lord Rama standing tall, gently raising his hand to stop the monkeys from mocking, showing kindness, 9:16", "approx_sec": 5.0},
            {"slide_index": 10, "caption": "उन्होंने गिलहरी को प्यार से हाथ में उठाया।", "image_prompt": "Lord Rama holding the tiny sandy squirrel tenderly in his glowing lotus-like hands, smiling warmly, 9:16", "approx_sec": 5.0},
            {"slide_index": 11, "caption": "और उसकी पीठ पर अपनी उंगलियां फेरीं।", "image_prompt": "Lord Rama gently stroking the squirrel's back with his three fingers, leaving three glowing white stripes, 9:16", "approx_sec": 6.0},
            {"slide_index": 12, "caption": "सेवा का आकार नहीं, समर्पण मायने रखता है।", "image_prompt": "A close up of a beautiful squirrel with three distinct stripes on its back, sitting near a floating stone, 9:16", "approx_sec": 5.0}
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
print(f"Successfully generated and injected {count} full JSON scripts (Batch 6) into the local database!")
