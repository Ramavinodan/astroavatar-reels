import sqlite3
import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "production_history.db")

batch_data = {
    "krishna_birth": {
        "story_id": "krishna_birth",
        "title": "श्री कृष्ण का जन्म और कारागार",
        "category": "विष्णु पुराण",
        "script_hi": "भगवान श्री कृष्ण ने एक अंधेरी जेल में जन्म क्यों लिया? मथुरा का क्रूर राजा कंस अपनी बहन देवकी से बहुत प्रेम करता था। लेकिन जब देवकी का विवाह वासुदेव से हुआ, तो आकाशवाणी हुई कि देवकी का आठवां पुत्र ही कंस की मृत्यु का कारण बनेगा। मौत के डर से कांपते हुए कंस ने तुरंत अपनी बहन और बहनोई को एक अंधेरी कालकोठरी में डाल दिया और उनके एक-एक करके 7 बच्चों को बेरहमी से मार डाला। जब भाद्रपद मास की अष्टमी की आधी रात को आठवें पुत्र के रूप में श्री कृष्ण का जन्म हुआ, तो चमत्कार होने लगे। कालकोठरी में अचानक दिव्य प्रकाश फैल गया, जेल के सारे ताले अपने आप खुल गए और सभी पहरेदार गहरी नींद में सो गए। वासुदेव ने तुरंत नवजात कृष्ण को एक टोकरी में रखा और उफनती हुई यमुना नदी को पार करके उन्हें गोकुल में सुरक्षित नंद बाबा के घर छोड़ आए। यह कथा हमें सिखाती है कि चाहे बुराई कितनी भी ताकतवर क्यों न हो, जब भगवान आते हैं तो हर ताला और हर बेड़ी अपने आप टूट जाती है।",
        "estimated_speech_sec": 90.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "श्री कृष्ण ने एक अंधेरी जेल में जन्म क्यों लिया?", "image_prompt": "A dark, ancient stone dungeon with heavy iron bars, mysterious glowing blue light inside, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "कंस ने देवकी और वासुदेव को जेल में डाल दिया।", "image_prompt": "Cruel king Kansa pointing an angry finger, chaining Devaki and Vasudeva in a dark dungeon, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "आकाशवाणी थी कि आठवां पुत्र कंस को मारेगा।", "image_prompt": "King Kansa looking terrified as a divine lightning storm forms a face in the night sky, 9:16", "approx_sec": 5.0},
            {"slide_index": 4, "caption": "कंस ने उनके 7 बच्चों को मार डाला।", "image_prompt": "Devaki crying in the dark dungeon holding an empty blanket, immense sorrow, heavy chains, 9:16", "approx_sec": 5.0},
            {"slide_index": 5, "caption": "अष्टमी की आधी रात को चमत्कार हुआ।", "image_prompt": "A brilliant, blinding golden light suddenly filling the dark dungeon, baby Krishna appearing, 9:16", "approx_sec": 6.0},
            {"slide_index": 6, "caption": "श्री कृष्ण का जन्म हुआ।", "image_prompt": "Vasudeva and Devaki kneeling respectfully before the glowing, divine baby Lord Krishna with four arms, 9:16", "approx_sec": 5.0},
            {"slide_index": 7, "caption": "जेल के ताले अपने आप खुल गए।", "image_prompt": "Heavy iron padlocks glowing magically and breaking open on their own, dropping to the floor, 9:16", "approx_sec": 5.0},
            {"slide_index": 8, "caption": "सभी पहरेदार गहरी नींद में सो गए।", "image_prompt": "Fierce demon guards lying on the floor in a deep magical slumber, completely unaware, 9:16", "approx_sec": 5.0},
            {"slide_index": 9, "caption": "वासुदेव ने कृष्ण को टोकरी में रखा।", "image_prompt": "Vasudeva gently placing the glowing baby in a wicker basket on his head, heavy rain falling, 9:16", "approx_sec": 6.0},
            {"slide_index": 10, "caption": "और उफनती यमुना नदी पार की।", "image_prompt": "Vasudeva walking through the flooded, raging Yamuna river at night, the giant snake Sheshnaag providing an umbrella, 9:16", "approx_sec": 6.0},
            {"slide_index": 11, "caption": "कृष्ण को गोकुल में सुरक्षित छोड़ आए।", "image_prompt": "Vasudeva secretly placing baby Krishna next to a sleeping Yashoda in a cozy village house, 9:16", "approx_sec": 5.0},
            {"slide_index": 12, "caption": "भगवान के आने पर हर बेड़ी टूट जाती है।", "image_prompt": "A broken iron chain lying on the floor next to a blooming glowing blue lotus, symbol of freedom, 9:16", "approx_sec": 5.0}
        ]
    },
    "putana_salvation": {
        "story_id": "putana_salvation",
        "title": "पूतना का उद्धार",
        "category": "विष्णु पुराण",
        "script_hi": "श्री कृष्ण ने बाल रूप में ही भयंकर राक्षसी पूतना का वध कैसे किया? गोकुल में श्री कृष्ण के जन्म की खबर सुनकर राजा कंस बौखला गया। उसने नवजात बच्चों को मारने के लिए 'पूतना' नाम की एक बेहद खतरनाक और मायावी राक्षसी को भेजा। पूतना एक अत्यंत सुंदर और ममतामयी स्त्री का रूप धारण करके गोकुल पहुंची। उसने अपने स्तनों (छाती) पर एक अत्यंत भयंकर और जानलेवा विष (ज़हर) लगा रखा था, ताकि दूध पिलाते ही बच्चा मर जाए। कोई उसे पहचान नहीं पाया और उसने माता यशोदा से आज्ञा लेकर बाल कृष्ण को गोद में उठा लिया। पूतना ने प्यार का नाटक करते हुए कृष्ण को विषैला दूध पिलाना शुरू किया। लेकिन भगवान को कौन मार सकता है? बाल कृष्ण ने दूध के साथ-साथ पूतना के प्राण भी चूस लिए! पूतना दर्द से चीखने लगी और वह अपने असली, भयंकर राक्षसी रूप में वापस आ गई। विशाल राक्षसी ज़मीन पर गिरकर मर गई, लेकिन खेलते हुए बाल कृष्ण उसकी छाती पर बिल्कुल सुरक्षित थे। भगवान ने पूतना को इसलिए मोक्ष दिया, क्योंकि उसने एक पल के लिए ही सही, लेकिन माँ (माता) का रूप धारण किया था।",
        "estimated_speech_sec": 95.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "बाल कृष्ण ने राक्षसी पूतना का वध कैसे किया?", "image_prompt": "A beautiful but eerie woman with a fake sweet smile entering a vibrant Indian village, carrying hidden darkness, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "कंस ने पूतना राक्षसी को गोकुल भेजा।", "image_prompt": "King Kansa secretly ordering a giant terrifying demoness (Putana) in a dark corner of his palace, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "पूतना ने एक सुंदर स्त्री का रूप धारण किया।", "image_prompt": "The terrifying demoness magically transforming into a gorgeous, richly dressed motherly woman, 9:16", "approx_sec": 5.0},
            {"slide_index": 4, "caption": "उसने अपने शरीर पर भयंकर विष लगा रखा था।", "image_prompt": "A glowing green toxic aura radiating slightly from the woman's chest, hidden by her beautiful clothes, 9:16", "approx_sec": 5.0},
            {"slide_index": 5, "caption": "उसने यशोदा से आज्ञा लेकर कृष्ण को गोद में लिया।", "image_prompt": "Putana holding glowing baby Krishna lovingly in her arms, Yashoda looking on innocently, 9:16", "approx_sec": 6.0},
            {"slide_index": 6, "caption": "पूतना ने कृष्ण को विषैला दूध पिलाना शुरू किया।", "image_prompt": "Baby Krishna drinking the milk with his eyes closed playfully, immune to the dark green poison entering him, 9:16", "approx_sec": 6.0},
            {"slide_index": 7, "caption": "लेकिन कृष्ण ने उसके प्राण चूस लिए!", "image_prompt": "Putana's beautiful face suddenly twisting in immense pain and horror, gasping for air, 9:16", "approx_sec": 5.0},
            {"slide_index": 8, "caption": "वह दर्द से चीखने लगी।", "image_prompt": "Putana screaming loudly, her disguise fading away, revealing her terrifying, huge demon skin, 9:16", "approx_sec": 5.0},
            {"slide_index": 9, "caption": "पूतना अपने भयंकर राक्षसी रूप में आ गई।", "image_prompt": "A gigantic, scary demoness crashing through the trees and falling heavily to the ground, causing an earthquake, 9:16", "approx_sec": 6.0},
            {"slide_index": 10, "caption": "विशाल राक्षसी मर गई, पर कृष्ण सुरक्षित थे।", "image_prompt": "Baby Krishna crawling happily and playing on the massive fallen demoness, completely unharmed and glowing, 9:16", "approx_sec": 6.0},
            {"slide_index": 11, "caption": "कृष्ण ने पूतना को भी मोक्ष दिया।", "image_prompt": "A glowing, pure soul leaving the giant demon body and travelling towards the divine heavens, 9:16", "approx_sec": 5.0},
            {"slide_index": 12, "caption": "क्योंकि उसने एक पल के लिए ही सही, माँ का रूप लिया था।", "image_prompt": "Lord Krishna playfully smiling, a divine peacock feather glowing on his head, representing pure unconditional grace, 9:16", "approx_sec": 5.0}
        ]
    },
    "govardhan_puja": {
        "story_id": "govardhan_puja",
        "title": "गोवर्धन पर्वत और इंद्र का कोप",
        "category": "विष्णु पुराण",
        "script_hi": "श्री कृष्ण ने अपनी छोटी उंगली पर गोवर्धन पर्वत क्यों उठाया था? गोकुल के लोग हर साल बारिश के देवता, इंद्र की पूजा करते थे ताकि अच्छी बारिश हो और फसल अच्छी हो। लेकिन बाल कृष्ण ने लोगों को समझाया कि इंद्र केवल अपना काम कर रहे हैं। हमें इंद्र के बजाय 'गोवर्धन पर्वत' की पूजा करनी चाहिए, जो हमारी गायों को चारा और हमें पानी देता है। गोकुलवासियों ने कृष्ण की बात मान ली और इंद्र की पूजा बंद कर दी। जब इंद्र देव को यह बात पता चली, तो उनके अहंकार को गहरी ठेस पहुंची। गुस्से में आकर इंद्र ने गोकुल पर भयंकर तूफ़ान और प्रलयंकारी बारिश शुरू कर दी। पूरा गांव डूबने लगा और लोग घबरा गए। तब श्री कृष्ण ने अपने चमत्कार से विशाल गोवर्धन पर्वत को अपनी बायीं हाथ की सबसे छोटी उंगली (कनिष्ठा) पर उठा लिया! सभी गांव वालों और जानवरों ने उस विशाल पर्वत के नीचे शरण ली। 7 दिन और 7 रात तक लगातार बारिश होती रही, लेकिन कृष्ण ने पर्वत को हिलने तक नहीं दिया। अंततः इंद्र का अहंकार टूट गया, वे कृष्ण के चरणों में गिर पड़े और क्षमा मांगी।",
        "estimated_speech_sec": 95.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "कृष्ण ने छोटी उंगली पर गोवर्धन पर्वत क्यों उठाया?", "image_prompt": "Young boy Krishna balancing a massive, glowing mountain on his pinky finger effortlessly, smiling warmly, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "गोकुल के लोग इंद्र की पूजा करते थे।", "image_prompt": "Villagers of Gokul offering lots of food and sweets to a statue of Lord Indra, hoping for rain, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "कृष्ण ने कहा, गोवर्धन पर्वत की पूजा करो।", "image_prompt": "Young Krishna pointing towards the lush green Govardhan mountain, surrounded by happy cows, 9:16", "approx_sec": 5.0},
            {"slide_index": 4, "caption": "इंद्र देव के अहंकार को ठेस पहुंची।", "image_prompt": "Lord Indra looking furious in the heavens, sitting on his white elephant, holding his lightning bolt, 9:16", "approx_sec": 5.0},
            {"slide_index": 5, "caption": "इंद्र ने भयंकर तूफ़ान और प्रलयंकारी बारिश शुरू कर दी।", "image_prompt": "Apocalyptic black storm clouds, heavy rain, and fierce lightning striking the helpless village of Gokul, 9:16", "approx_sec": 6.0},
            {"slide_index": 6, "caption": "पूरा गांव डूबने लगा।", "image_prompt": "Panicking villagers and cows trying to find shelter as floodwaters rise rapidly around their mud houses, 9:16", "approx_sec": 5.0},
            {"slide_index": 7, "caption": "तब श्री कृष्ण ने विशाल पर्वत उठा लिया!", "image_prompt": "Krishna magically lifting the entire massive Govardhan mountain from its base, glowing divine aura, 9:16", "approx_sec": 6.0},
            {"slide_index": 8, "caption": "सभी गांव वालों ने पर्वत के नीचे शरण ली।", "image_prompt": "Hundreds of villagers and cows standing safely under the giant floating mountain, looking at Krishna in awe, 9:16", "approx_sec": 6.0},
            {"slide_index": 9, "caption": "7 दिन और 7 रात तक लगातार बारिश हुई।", "image_prompt": "Furious storm continuing outside, but inside under the mountain it is completely dry, warm, and safe, 9:16", "approx_sec": 5.0},
            {"slide_index": 10, "caption": "कृष्ण ने पर्वत को हिलने तक नहीं दिया।", "image_prompt": "Close up of young Krishna's little pinky finger effortlessly holding up millions of tons of solid rock, 9:16", "approx_sec": 5.0},
            {"slide_index": 11, "caption": "अंततः इंद्र का अहंकार टूट गया।", "image_prompt": "The rain stopping, sunlight piercing the clouds, Lord Indra realizing his terrible mistake and arrogance, 9:16", "approx_sec": 5.0},
            {"slide_index": 12, "caption": "इंद्र ने कृष्ण के चरणों में गिरकर क्षमा मांगी।", "image_prompt": "Lord Indra bowing down, touching the small feet of Lord Krishna, completely humbled, divine peace, 9:16", "approx_sec": 6.0}
        ]
    },
    "kalia_mardan": {
        "story_id": "kalia_mardan",
        "title": "कालिया नाग का मर्दन",
        "category": "विष्णु पुराण",
        "script_hi": "बाल कृष्ण ने कालिया नाग के हज़ार फनों पर नृत्य क्यों किया? यमुना नदी के एक बहुत गहरे हिस्से में कालिया नाम का एक भयंकर और अत्यंत विषैला नाग अपने परिवार के साथ आकर रहने लगा था। कालिया नाग के ज़हर की गर्मी और तीव्रता इतनी अधिक थी कि नदी का पानी खौलने लगा था और वहां जाने वाले सभी पक्षी, जानवर और इंसान मर जाते थे। एक दिन, कृष्ण अपने ग्वाल-बालों (दोस्तों) के साथ वहां गेंद खेल रहे थे। अचानक उनकी गेंद पानी में गिर गई। सभी ने कृष्ण को रोका, लेकिन कृष्ण तुरंत एक ऊंचे पेड़ से उस ज़हरीली नदी में कूद गए। पानी के अंदर कालिया नाग ने कृष्ण को अपने खतरनाक कुंडलियों में जकड़ लिया। लेकिन बाल कृष्ण ने अपने शरीर का आकार इतना बड़ा कर लिया कि नाग की पकड़ छूट गई। इसके बाद, कृष्ण ने छलांग लगाई और कालिया नाग के विशाल फनों पर खड़े हो गए। कालिया नाग ने जितने फन उठाए, कृष्ण ने अपनी बांसुरी बजाते हुए उन पर नृत्य करके उन्हें कुचल दिया। नाग की पत्नियों ने कृष्ण से दया की भीख मांगी। कृष्ण ने कालिया को माफ कर दिया और उसे यमुना छोड़कर समुद्र में जाने का आदेश दिया।",
        "estimated_speech_sec": 95.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "कृष्ण ने कालिया नाग के फनों पर नृत्य क्यों किया?", "image_prompt": "Young boy Krishna gracefully dancing on the multiple glowing heads of a giant dark serpent in a river, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "यमुना नदी में कालिया नाग रहने लगा था।", "image_prompt": "A terrifying, massive multi-headed black serpent (Kaliya) swimming in the Yamuna river, looking evil, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "नाग के ज़हर से नदी का पानी खौलने लगा था।", "image_prompt": "The river water bubbling, turning dark green with poison, dead fish and birds floating on the surface, 9:16", "approx_sec": 5.0},
            {"slide_index": 4, "caption": "एक दिन कृष्ण की गेंद पानी में गिर गई।", "image_prompt": "Young Krishna and his cowherd friends looking worried as a small ball splashes into the toxic river, 9:16", "approx_sec": 5.0},
            {"slide_index": 5, "caption": "कृष्ण ऊंचे पेड़ से उस ज़हरीली नदी में कूद गए!", "image_prompt": "Young Krishna fearlessly diving off a high Kadamba tree branch directly into the dark poisonous water, 9:16", "approx_sec": 6.0},
            {"slide_index": 6, "caption": "कालिया नाग ने कृष्ण को जकड़ लिया।", "image_prompt": "The giant serpent fiercely wrapping its thick coils tightly around young Krishna underwater, toxic bubbles, 9:16", "approx_sec": 5.0},
            {"slide_index": 7, "caption": "कृष्ण ने अपने शरीर का आकार बड़ा कर लिया।", "image_prompt": "Krishna expanding his divine form, forcing the giant snake to release its grip in pain, glowing light, 9:16", "approx_sec": 6.0},
            {"slide_index": 8, "caption": "कृष्ण ने छलांग लगाई और नाग के फनों पर खड़े हो गए।", "image_prompt": "Krishna jumping high out of the water and landing perfectly on the giant extended hoods of the serpent, 9:16", "approx_sec": 6.0},
            {"slide_index": 9, "caption": "बांसुरी बजाते हुए फनों को कुचल दिया।", "image_prompt": "Krishna playing his flute with one hand and dancing vigorously, stomping down the snake's heads, 9:16", "approx_sec": 5.0},
            {"slide_index": 10, "caption": "नाग की पत्नियों ने दया की भीख मांगी।", "image_prompt": "The snake wives (Naginis) rising from the water with folded hands, begging Krishna to spare their husband, 9:16", "approx_sec": 5.0},
            {"slide_index": 11, "caption": "कृष्ण ने कालिया को समुद्र में जाने का आदेश दिया।", "image_prompt": "Lord Krishna pointing a commanding finger, ordering the defeated snake to leave the river forever, 9:16", "approx_sec": 6.0},
            {"slide_index": 12, "caption": "यमुना का पानी फिर से शुद्ध हो गया।", "image_prompt": "The Yamuna river returning to a sparkling, crystal clear blue, lotuses blooming, peaceful nature, 9:16", "approx_sec": 5.0}
        ]
    },
    "sudama_rice": {
        "story_id": "sudama_rice",
        "title": "सुदामा के चावल",
        "category": "विष्णु पुराण",
        "script_hi": "भगवान श्री कृष्ण और सुदामा की मित्रता की कहानी इतनी खास क्यों है? सुदामा एक बहुत ही गरीब ब्राह्मण थे और बचपन में कृष्ण के सहपाठी थे। कई सालों बाद, जब सुदामा के परिवार के पास खाने के लिए कुछ नहीं बचा, तो उनकी पत्नी ने उन्हें द्वारकाधीश कृष्ण से मदद मांगने भेजा। सुदामा संकोच में थे, कि द्वारका का राजा उन्हें पहचानेगा भी या नहीं? भेंट के लिए उनकी पत्नी ने पड़ोसियों से मांगकर थोड़ी सी सूखी 'पोहे' (चावल) एक फटे हुए कपड़े में बांधकर दी। जब सुदामा द्वारका के शानदार महल पहुंचे, तो उनके फटे कपड़े देखकर पहरेदारों ने उन्हें रोक लिया। लेकिन जैसे ही कृष्ण ने सुदामा का नाम सुना, वे नंगे पैर दौड़ते हुए गेट पर आ गए! उन्होंने सुदामा को गले लगाया, उन्हें अपने सिंहासन पर बैठाया और अपने आंसुओं से उनके पैर धोए। सुदामा को अपनी गरीब भेंट (चावल) देने में शर्म आ रही थी, लेकिन कृष्ण ने उसे छीनकर बड़े प्रेम से खाया। सुदामा ने बिना कुछ मांगे विदाई ली। लेकिन जब वे अपने गांव लौटे, तो उन्होंने देखा कि उनकी टूटी झोपड़ी एक सोने के महल में बदल चुकी थी! भगवान अपने सच्चे मित्र को बिना मांगे ही सब कुछ दे देते हैं।",
        "estimated_speech_sec": 95.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "कृष्ण और सुदामा की मित्रता इतनी खास क्यों है?", "image_prompt": "Lord Krishna and poor Sudama embracing each other tightly, glowing divine friendship, highly emotional, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "सुदामा एक बहुत ही गरीब ब्राह्मण थे।", "image_prompt": "Sudama sitting in a broken, leaky mud hut, wearing torn clothes, looking thin and very poor, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "उनकी पत्नी ने सूखी चावल की पोटली दी।", "image_prompt": "Sudama's wife sadly tying a handful of dry puffed rice (poha) into a torn, dirty piece of cloth, 9:16", "approx_sec": 5.0},
            {"slide_index": 4, "caption": "सुदामा द्वारका के शानदार महल पहुंचे।", "image_prompt": "Poor Sudama standing in awe outside the massive, glowing, golden gates of Dwarka palace, 9:16", "approx_sec": 5.0},
            {"slide_index": 5, "caption": "पहरेदारों ने उन्हें रोक लिया।", "image_prompt": "Heavily armored royal guards blocking poor Sudama with their spears, looking at him with suspicion, 9:16", "approx_sec": 5.0},
            {"slide_index": 6, "caption": "लेकिन कृष्ण नंगे पैर दौड़ते हुए आए!", "image_prompt": "Lord Krishna in royal attire, completely ignoring protocol, running barefoot desperately towards the palace gate, 9:16", "approx_sec": 6.0},
            {"slide_index": 7, "caption": "उन्होंने सुदामा को गले लगा लिया।", "image_prompt": "King Krishna hugging the poor, dirty beggar Sudama tightly, tears flowing from Krishna's eyes, 9:16", "approx_sec": 5.0},
            {"slide_index": 8, "caption": "कृष्ण ने आंसुओं से उनके पैर धोए।", "image_prompt": "Krishna making Sudama sit on the royal throne and washing Sudama's blistered feet with a golden pot, 9:16", "approx_sec": 6.0},
            {"slide_index": 9, "caption": "सुदामा को चावल देने में शर्म आ रही थी।", "image_prompt": "Sudama trying to hide the small torn pouch of dry rice behind his back, feeling deeply ashamed, 9:16", "approx_sec": 5.0},
            {"slide_index": 10, "caption": "कृष्ण ने छीनकर बड़े प्रेम से खाया।", "image_prompt": "Lord Krishna playfully snatching the pouch and eating a handful of dry rice with immense joy and bliss, 9:16", "approx_sec": 6.0},
            {"slide_index": 11, "caption": "सुदामा ने बिना कुछ मांगे विदाई ली।", "image_prompt": "Sudama walking back on the forest path, empty-handed but smiling, completely content just seeing his friend, 9:16", "approx_sec": 5.0},
            {"slide_index": 12, "caption": "उनका गांव सोने के महल में बदल चुका था!", "image_prompt": "Sudama looking shocked as his broken hut is now a magnificent golden palace filled with wealth, divine grace, 9:16", "approx_sec": 5.0}
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
print(f"Successfully generated and injected {count} full JSON scripts (Batch 7) into the local database!")
