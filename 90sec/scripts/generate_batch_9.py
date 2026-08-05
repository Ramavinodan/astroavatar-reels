import sqlite3
import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "production_history.db")

batch_data = {
    "ashwatthama_curse": {
        "story_id": "ashwatthama_curse",
        "title": "अश्वत्थामा का श्राप",
        "category": "महाभारत रहस्य",
        "script_hi": "महाभारत के अंत में अश्वत्थामा को अमरता का भयंकर श्राप क्यों मिला? अश्वत्थामा गुरु द्रोणाचार्य के पुत्र थे और एक जन्मजात मणि (रत्न) के साथ पैदा हुए थे, जो उन्हें भूख, प्यास, बीमारी और थकावट से बचाता था। कुरुक्षेत्र के युद्ध के अंतिम दिन, जब दुर्योधन मरने की हालत में था, तब अश्वत्थामा ने रात के अंधेरे में पांडवों के शिविर पर कायरता से हमला कर दिया। उसने सोते हुए द्रौपदी के पांच मासूम बेटों की हत्या कर दी। इस जघन्य पाप से पांडव क्रोधित हो उठे। भगवान कृष्ण के साथ अर्जुन ने अश्वत्थामा को घेर लिया। अपनी हार तय देखकर अश्वत्थामा ने दुनिया को खत्म करने वाला 'ब्रह्मास्त्र' चला दिया। कृष्ण के आदेश पर अर्जुन ने भी ब्रह्मास्त्र चलाया, लेकिन ऋषि व्यास ने दोनों अस्त्रों को टकराने से रोक दिया और वापस लेने को कहा। अर्जुन ने अपना अस्त्र वापस ले लिया, लेकिन अश्वत्थामा को यह विद्या नहीं आती थी। गुस्से में उसने अपना ब्रह्मास्त्र उत्तरा के गर्भ (गर्भ में पल रहे शिशु परीक्षित) पर मोड़ दिया। इस अत्यंत नीच कृत्य से भगवान कृष्ण को भयंकर क्रोध आया। उन्होंने अश्वत्थामा के माथे से वह दिव्य मणि छीन ली और श्राप दिया कि 3000 वर्षों तक वह खून और पीब से रिसते घावों के साथ, बिना भोजन और आश्रय के इस धरती पर भटकता रहेगा और मौत की भीख मांगेगा लेकिन मर नहीं सकेगा।",
        "estimated_speech_sec": 105.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "अश्वत्थामा को अमरता का भयंकर श्राप क्यों मिला?", "image_prompt": "Ashwatthama looking terrifying in the dark, a glowing magical red gem (Mani) shining brightly on his forehead, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "दुर्योधन मरने की हालत में था।", "image_prompt": "Duryodhana lying on the battlefield at night, bleeding, holding Ashwatthama's hand tightly with a final wish, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "अश्वत्थामा ने रात में कायरता से हमला किया।", "image_prompt": "Ashwatthama holding a bloody sword, sneaking into the quiet, dark Pandava sleeping camp at midnight, 9:16", "approx_sec": 5.0},
            {"slide_index": 4, "caption": "उसने द्रौपदी के पांच मासूम बेटों की हत्या कर दी।", "image_prompt": "Draupadi crying intensely in the morning, holding the lifeless bodies of her five young sons, complete tragedy, 9:16", "approx_sec": 6.0},
            {"slide_index": 5, "caption": "कृष्ण और अर्जुन ने अश्वत्थामा को घेर लिया।", "image_prompt": "Lord Krishna and Arjuna angrily confronting a terrified Ashwatthama near a riverbank, bows drawn, 9:16", "approx_sec": 5.0},
            {"slide_index": 6, "caption": "अश्वत्थामा ने 'ब्रह्मास्त्र' चला दिया।", "image_prompt": "Ashwatthama chanting a mantra on a blade of grass, turning it into a massive, blinding, world-destroying nuclear weapon (Brahmastra), 9:16", "approx_sec": 6.0},
            {"slide_index": 7, "caption": "ऋषि व्यास ने अस्त्र वापस लेने को कहा।", "image_prompt": "Sage Vyasa appearing magically in the sky, raising his hand to stop the two colliding celestial weapons, 9:16", "approx_sec": 5.0},
            {"slide_index": 8, "caption": "अश्वत्थामा को अस्त्र वापस लेना नहीं आता था।", "image_prompt": "Ashwatthama looking panicked and helpless as his destructive weapon spins out of his control, 9:16", "approx_sec": 5.0},
            {"slide_index": 9, "caption": "उसने अस्त्र को उत्तरा के गर्भ पर मोड़ दिया।", "image_prompt": "The glowing destructive weapon flying rapidly towards the womb of pregnant Princess Uttara, cruel magic, 9:16", "approx_sec": 6.0},
            {"slide_index": 10, "caption": "भगवान कृष्ण को भयंकर क्रोध आया।", "image_prompt": "Lord Krishna looking extremely furious, his eyes burning with divine anger, cosmic aura exploding, 9:16", "approx_sec": 5.0},
            {"slide_index": 11, "caption": "उन्होंने अश्वत्थामा के माथे से मणि छीन ली।", "image_prompt": "Lord Krishna forcefully tearing the glowing red gem from Ashwatthama's forehead, blood pouring down his face, 9:16", "approx_sec": 6.0},
            {"slide_index": 12, "caption": "और 3000 साल तक तड़पने का श्राप दिया।", "image_prompt": "A horrific, zombie-like Ashwatthama wandering alone in a dark, empty forest, cursed with eternal suffering, 9:16", "approx_sec": 5.0}
        ]
    },
    "gandhari_curse": {
        "story_id": "gandhari_curse",
        "title": "गांधारी का श्री कृष्ण को श्राप",
        "category": "महाभारत रहस्य",
        "script_hi": "माता गांधारी ने साक्षात भगवान श्री कृष्ण को श्राप क्यों दिया? कुरुक्षेत्र के युद्ध में जब गांधारी के 100 पुत्र (कौरव) मारे गए, तो गांधारी का हृदय दुख से फट गया। वह युद्ध के मैदान में अपने मृत पुत्रों, खासकर दुर्योधन की लाश देखकर फूट-फूट कर रोने लगी। उसी समय भगवान श्री कृष्ण सांत्वना देने के लिए वहां पहुंचे। अपने पुत्रों की जली-कटी लाशें देखकर गांधारी का दुख भयानक क्रोध में बदल गया। उसने अपनी आंखों पर बंधी पट्टी के पीछे से चीखते हुए श्री कृष्ण से कहा, 'हे जनार्दन! तुम साक्षात ईश्वर हो। तुम चाहते तो यह विनाशकारी युद्ध रोक सकते थे, लेकिन तुमने मेरे 100 पुत्रों को मरने दिया! जिस तरह तुमने मेरे कुरु वंश का नाश किया है, उसी तरह आज से 36 साल बाद तुम्हारा पूरा यादव वंश भी आपस में लड़-कट कर खत्म हो जाएगा! और तुम भी एक साधारण शिकारी के तीर से मारे जाओगे!' श्री कृष्ण ने मुस्कुराते हुए इस भयानक श्राप को सहर्ष स्वीकार कर लिया। क्योंकि वे जानते थे कि भविष्य में उनके अपने यादव वंश का भी अहंकार बढ़ जाएगा और उनका अंत भी निश्चित है। भगवान होकर भी कर्म के विधान का सम्मान करना, यही कृष्ण की महानता है।",
        "estimated_speech_sec": 100.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "गांधारी ने साक्षात ईश्वर को श्राप क्यों दिया?", "image_prompt": "Queen Gandhari wearing a white blindfold, crying in extreme agony on a bloody battlefield, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "कुरुक्षेत्र में उसके 100 पुत्र मारे गए थे।", "image_prompt": "The battlefield littered with broken chariots and the dead bodies of the Kaurava princes, vultures flying, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "वह दुर्योधन की लाश देखकर फूट-फूट कर रोई।", "image_prompt": "Gandhari falling to her knees and hugging the massive, bloody dead body of Duryodhana, heartbreaking sorrow, 9:16", "approx_sec": 6.0},
            {"slide_index": 4, "caption": "उसी समय श्री कृष्ण सांत्वना देने पहुंचे।", "image_prompt": "Lord Krishna walking gracefully onto the tragic battlefield, radiating a calm, golden divine light, 9:16", "approx_sec": 5.0},
            {"slide_index": 5, "caption": "गांधारी का दुख भयंकर क्रोध में बदल गया।", "image_prompt": "Gandhari fiercely turning towards Krishna, pointing her finger aggressively at him, furious aura, 9:16", "approx_sec": 5.0},
            {"slide_index": 6, "caption": "'तुम चाहते तो यह युद्ध रोक सकते थे!'", "image_prompt": "Close up of Gandhari shouting at Krishna, tears streaming from under her tight blindfold, 9:16", "approx_sec": 5.0},
            {"slide_index": 7, "caption": "'जिस तरह तुमने मेरे कुरु वंश का नाश किया है...'", "image_prompt": "A blazing fire destroying the Kuru flags and royal emblems, symbolizing the end of a dynasty, 9:16", "approx_sec": 5.0},
            {"slide_index": 8, "caption": "'36 साल बाद तुम्हारा यादव वंश भी खत्म हो जाएगा!'", "image_prompt": "A dark futuristic vision showing Yadava warriors drunkenly fighting and killing each other with iron grass near the ocean, 9:16", "approx_sec": 6.0},
            {"slide_index": 9, "caption": "'और तुम भी एक साधारण शिकारी के तीर से मारे जाओगे!'", "image_prompt": "A vision of an ordinary hunter accidentally shooting a glowing arrow towards the foot of Lord Krishna in a forest, 9:16", "approx_sec": 6.0},
            {"slide_index": 10, "caption": "श्री कृष्ण ने मुस्कुराकर श्राप स्वीकार कर लिया।", "image_prompt": "Lord Krishna standing peacefully, hands folded in respect, accepting the terrible curse with a gentle, knowing smile, 9:16", "approx_sec": 6.0},
            {"slide_index": 11, "caption": "वे जानते थे कि यादव वंश का भी अंत निश्चित है।", "image_prompt": "A massive ocean wave completely swallowing the glowing golden city of Dwarka, cosmic destruction, 9:16", "approx_sec": 5.0},
            {"slide_index": 12, "caption": "भगवान भी कर्म के विधान का सम्मान करते हैं।", "image_prompt": "A glowing balance scale in the cosmos, symbolizing ultimate Karma that applies equally to everyone, even God, 9:16", "approx_sec": 5.0}
        ]
    },
    "karna_wheel": {
        "story_id": "karna_wheel",
        "title": "कर्ण के रथ का पहिया",
        "category": "महाभारत रहस्य",
        "script_hi": "कुरुक्षेत्र में कर्ण के रथ का पहिया ज़मीन में क्यों धंस गया था? कर्ण महाभारत का सबसे महान और अजेय योद्धा था, लेकिन उसके अंतिम समय में उसकी शक्तियों ने उसका साथ छोड़ दिया। इसके पीछे एक भयंकर श्राप था। एक बार कर्ण अनजाने में अपने रथ से एक गरीब ब्राह्मण की गाय के बछड़े को कुचल देता है। वह ब्राह्मण क्रोधित होकर कर्ण को श्राप देता है कि 'जिस तरह तूने एक असहाय बछड़े की जान ली है, उसी तरह जब तू अपनी ज़िंदगी के सबसे महत्वपूर्ण युद्ध में होगा, तो तेरे रथ का पहिया ज़मीन में धंस जाएगा और तू असहाय मारा जाएगा!' यह श्राप महाभारत के 17वें दिन सच साबित हुआ। अर्जुन और कर्ण के बीच भयंकर युद्ध चल रहा था, तभी कर्ण के रथ का बायां पहिया अचानक गीली मिट्टी में धंस गया। कर्ण ने युद्ध रोककर पहिया निकालने की कोशिश की। उसने अर्जुन से कहा कि निहत्थे पर वार करना धर्म नहीं है। लेकिन तब भगवान कृष्ण ने कर्ण को याद दिलाया कि जब अभिमन्यु को छह महारथियों ने मिलकर मारा था, तब धर्म कहां था? जब द्रौपदी का चीरहरण हो रहा था, तब धर्म कहां था? कृष्ण के आदेश पर अर्जुन ने तीर चलाया और रथ का पहिया निकालते हुए निहत्थे कर्ण का सिर धड़ से अलग कर दिया।",
        "estimated_speech_sec": 105.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "कर्ण के रथ का पहिया ज़मीन में क्यों धंस गया?", "image_prompt": "A majestic glowing chariot wheel stuck deep into thick, dark mud on a bloody battlefield, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "कर्ण एक अजेय योद्धा था।", "image_prompt": "Karna standing tall on his glowing chariot, pulling his heavy bow with golden arrows flying towards the enemy, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "लेकिन उसे एक भयंकर श्राप मिला था।", "image_prompt": "A flashback showing an angry Brahmin pointing a cursing finger at Karna, dark clouds overhead, 9:16", "approx_sec": 5.0},
            {"slide_index": 4, "caption": "एक बार उसने अनजाने में गाय का बछड़ा कुचल दिया था।", "image_prompt": "A small innocent calf lying dead near the large wooden wheel of Karna's chariot in a peaceful forest, 9:16", "approx_sec": 6.0},
            {"slide_index": 5, "caption": "ब्राह्मण ने असहाय मरने का श्राप दिया।", "image_prompt": "The glowing curse leaving the Brahmin's mouth and attaching itself to Karna's chariot wheel, 9:16", "approx_sec": 5.0},
            {"slide_index": 6, "caption": "महाभारत के 17वें दिन श्राप सच हुआ।", "image_prompt": "Epic battle between Arjuna's glowing white chariot and Karna's golden chariot, massive energy waves, 9:16", "approx_sec": 5.0},
            {"slide_index": 7, "caption": "कर्ण के रथ का पहिया अचानक धंस गया।", "image_prompt": "The heavy golden wheel of Karna's chariot abruptly sinking deep into soft, muddy soil, tilting the chariot, 9:16", "approx_sec": 6.0},
            {"slide_index": 8, "caption": "कर्ण पहिया निकालने लगा।", "image_prompt": "Karna stepping down from the chariot without his bow, trying desperately with both hands to lift the heavy wheel from the mud, 9:16", "approx_sec": 6.0},
            {"slide_index": 9, "caption": "उसने अर्जुन से युद्ध रोकने को कहा।", "image_prompt": "Karna holding up one hand towards Arjuna, asking for a fair fight, looking exhausted and helpless, 9:16", "approx_sec": 5.0},
            {"slide_index": 10, "caption": "लेकिन कृष्ण ने उसे उसके पुराने पाप याद दिलाए।", "image_prompt": "Lord Krishna pointing a stern finger at Karna, looking extremely angry, reminding him of Abhimanyu and Draupadi, 9:16", "approx_sec": 6.0},
            {"slide_index": 11, "caption": "'जब अभिमन्यु को मारा, तब धर्म कहां था?'", "image_prompt": "A brief flashback bubble of young Abhimanyu being surrounded and killed mercilessly by multiple warriors, 9:16", "approx_sec": 5.0},
            {"slide_index": 12, "caption": "अर्जुन ने तीर चलाकर कर्ण का वध कर दिया।", "image_prompt": "A glowing magical arrow (Anjalika) flying perfectly and severing Karna's head while he is still holding the wheel, 9:16", "approx_sec": 6.0}
        ]
    },
    "yaksha_prashna": {
        "story_id": "yaksha_prashna",
        "title": "यक्ष प्रश्न और युधिष्ठिर का धर्म",
        "category": "महाभारत रहस्य",
        "script_hi": "युधिष्ठिर को धर्मराज क्यों कहा जाता है? वनवास के दौरान एक दिन पांडवों को बहुत ज़ोर की प्यास लगी। नकुल पानी की तलाश में एक झील के पास पहुंचे। जैसे ही वे पानी पीने लगे, एक रहस्यमयी आवाज़ (यक्ष) ने कहा, 'पहले मेरे सवालों के जवाब दो, वरना पानी पीते ही मर जाओगे।' नकुल ने बात नहीं मानी और पानी पीते ही उनकी मृत्यु हो गई। एक-एक करके सहदेव, अर्जुन और भीम भी वहां गए, उन्होंने भी अहंकार में यक्ष की चेतावनी नहीं मानी और मारे गए। अंत में युधिष्ठिर वहां पहुंचे। अपने चारों भाइयों की लाशें देखकर वे दुखी हुए, लेकिन उन्होंने यक्ष का सम्मान किया। यक्ष ने जीवन, मृत्यु और धर्म से जुड़े अत्यंत गहरे और कठिन प्रश्न पूछे। जैसे: 'दुनिया का सबसे बड़ा आश्चर्य क्या है?' युधिष्ठिर ने उत्तर दिया: 'रोज़ लोग मरते हैं, फिर भी जो ज़िंदा हैं वे सोचते हैं कि वे कभी नहीं मरेंगे, यही सबसे बड़ा आश्चर्य है।' युधिष्ठिर की बुद्धिमानी और विनम्रता से यक्ष अत्यंत प्रसन्न हुआ। यक्ष ने कहा, 'मैं तुम्हारे किसी एक भाई को जीवित कर सकता हूं, किसे चुनोगे?' युधिष्ठिर ने अपनी सौतेली माँ के बेटे 'नकुल' को चुना, ताकि दोनों माताओं का एक-एक बेटा ज़िंदा रहे। युधिष्ठिर का यह निस्वार्थ न्याय देखकर यक्ष (जो स्वयं यमराज थे) ने उनके चारों भाइयों को जीवित कर दिया।",
        "estimated_speech_sec": 105.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "युधिष्ठिर को धर्मराज क्यों कहा जाता है?", "image_prompt": "Yudhishthira standing peacefully near a mystical glowing lake in a dense ancient forest, holding a wooden staff, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "वनवास के दौरान पांडवों को प्यास लगी।", "image_prompt": "The five Pandava brothers looking extremely exhausted, sweating, and thirsty in a hot, dry forest, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "यक्ष ने कहा, 'पहले मेरे सवालों के जवाब दो।'", "image_prompt": "A mysterious, glowing, giant spirit (Yaksha) hovering above the clear blue lake, raising a warning hand, 9:16", "approx_sec": 5.0},
            {"slide_index": 4, "caption": "चारों भाइयों ने चेतावनी नहीं मानी और मारे गए।", "image_prompt": "Bhima, Arjuna, Nakula, and Sahadeva lying lifeless on the grassy bank near the cursed lake water, 9:16", "approx_sec": 6.0},
            {"slide_index": 5, "caption": "अंत में युधिष्ठिर वहां पहुंचे।", "image_prompt": "Yudhishthira arriving at the lake, looking shocked and heartbroken seeing his four invincible brothers dead, 9:16", "approx_sec": 5.0},
            {"slide_index": 6, "caption": "उन्होंने यक्ष का सम्मान किया।", "image_prompt": "Yudhishthira calmly folding his hands in deep respect towards the giant glowing Yaksha spirit, 9:16", "approx_sec": 5.0},
            {"slide_index": 7, "caption": "यक्ष ने बहुत गहरे प्रश्न पूछे।", "image_prompt": "The glowing Yaksha asking questions, magical question marks and symbols floating in the air, 9:16", "approx_sec": 5.0},
            {"slide_index": 8, "caption": "'दुनिया का सबसे बड़ा आश्चर्य क्या है?'", "image_prompt": "An hourglass with sand falling, surrounded by unaware people celebrating life, a symbol of mortality, 9:16", "approx_sec": 6.0},
            {"slide_index": 9, "caption": "'लोग मरते हैं, फिर भी सोचते हैं कि वे अमर हैं।'", "image_prompt": "Yudhishthira answering wisely, glowing aura of wisdom and truth radiating from his calm face, 9:16", "approx_sec": 6.0},
            {"slide_index": 10, "caption": "यक्ष ने कहा, 'किसी एक भाई को ज़िंदा करूंगा।'", "image_prompt": "The Yaksha pointing towards the four dead bodies, asking Yudhishthira to make the ultimate difficult choice, 9:16", "approx_sec": 5.0},
            {"slide_index": 11, "caption": "युधिष्ठिर ने अपनी सौतेली माँ के बेटे नकुल को चुना।", "image_prompt": "Yudhishthira pointing selflessly towards Nakula, ensuring fairness for his stepmother Madri, pure justice, 9:16", "approx_sec": 6.0},
            {"slide_index": 12, "caption": "यक्ष (यमराज) ने चारों भाइयों को जीवित कर दिया।", "image_prompt": "The Yaksha revealing his true form as Yamaraja (God of Death), blessing all four brothers who wake up magically, 9:16", "approx_sec": 5.0}
        ]
    },
    "surya_sanjana_chhaya": {
        "story_id": "surya_sanjana_chhaya",
        "title": "सूर्यदेव और छाया का रहस्य",
        "category": "नक्षत्र एवं ग्रह ज्ञान",
        "script_hi": "शनिदेव की माता का नाम 'छाया' (परछाई) क्यों था? सूर्यदेव का विवाह विश्वकर्मा की पुत्री संजना से हुआ था। संजना सूर्यदेव से बहुत प्रेम करती थीं, लेकिन वे सूर्य की असहनीय गर्मी और तेज़ को बर्दाश्त नहीं कर पा रही थीं। उनका शरीर जलने लगा था। इसलिए, एक दिन संजना ने अपनी ही परछाई (छाया) को एक जीवित स्त्री का रूप दिया, जिसका नाम 'स्वर्णा' (छाया) रखा। संजना ने छाया से कहा कि तुम मेरी जगह सूर्यदेव की पत्नी बनकर रहो, मैं अपने पिता के घर जा रही हूं। संजना के जाने के बाद छाया सूर्यदेव के साथ रहने लगी। चूँकि छाया एक परछाई थी, इसलिए उसे सूर्य की गर्मी से कोई परेशानी नहीं हुई। छाया और सूर्यदेव से जिस पुत्र का जन्म हुआ, वही 'शनि देव' हैं। शनि का रंग अपनी माता छाया (परछाई) के कारण बिल्कुल काला था। जब सूर्यदेव ने पहली बार अपने काले पुत्र को देखा, तो उन्होंने छाया पर शक किया और शनि को अपना पुत्र मानने से इंकार कर दिया। इसी घटना के कारण सूर्य और शनि (पिता और पुत्र) के बीच आज तक भयंकर दुश्मनी मानी जाती है, जो वैदिक ज्योतिष का एक बहुत बड़ा नियम है।",
        "estimated_speech_sec": 100.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "शनिदेव की माता का नाम 'छाया' क्यों था?", "image_prompt": "A beautiful dark silhouette of a woman (Chhaya) standing against a blindingly bright golden sun, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "सूर्यदेव का विवाह संजना से हुआ था।", "image_prompt": "Sun God (Surya) glowing intensely with golden fire, standing next to his beautiful but sweating wife, Sanjana, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "संजना सूर्य का भयंकर तेज़ बर्दाश्त नहीं कर पा रही थीं।", "image_prompt": "Sanjana trying to shield her eyes and face from the extreme blinding heat radiating from her husband, 9:16", "approx_sec": 6.0},
            {"slide_index": 4, "caption": "उन्होंने अपनी परछाई को जीवित स्त्री बना दिया।", "image_prompt": "Sanjana using magic, her dark shadow on the wall slowly transforming into a real, identical-looking woman, 9:16", "approx_sec": 6.0},
            {"slide_index": 5, "caption": "छाया सूर्यदेव की पत्नी बनकर रहने लगी।", "image_prompt": "The shadow woman (Chhaya) standing comfortably next to the blazing Sun God, completely unaffected by the heat, 9:16", "approx_sec": 5.0},
            {"slide_index": 6, "caption": "संजना तपस्या करने जंगल चली गईं।", "image_prompt": "The real Sanjana walking away into a cool, green forest, wearing simple ascetic clothes, finding peace, 9:16", "approx_sec": 5.0},
            {"slide_index": 7, "caption": "छाया और सूर्यदेव से एक पुत्र का जन्म हुआ।", "image_prompt": "Chhaya holding a newborn baby in her arms, the baby radiating a dark, mysterious cosmic blue aura, 9:16", "approx_sec": 5.0},
            {"slide_index": 8, "caption": "वही पुत्र 'शनि देव' हैं।", "image_prompt": "Young Lord Shani, looking serious and majestic, with a dark blue complexion, holding a staff, 9:16", "approx_sec": 5.0},
            {"slide_index": 9, "caption": "परछाई की वजह से शनि का रंग काला था।", "image_prompt": "Close up of Lord Shani's beautiful but dark, shadow-like complexion, glowing with deep cosmic justice, 9:16", "approx_sec": 5.0},
            {"slide_index": 10, "caption": "सूर्यदेव ने शनि को अपना पुत्र मानने से इंकार कर दिया।", "image_prompt": "Sun God looking suspiciously and angrily at the dark baby, refusing to accept him as a child of light, 9:16", "approx_sec": 6.0},
            {"slide_index": 11, "caption": "सूर्य और शनि में भयंकर दुश्मनी हो गई।", "image_prompt": "A cosmic clash between a bright blazing golden sun and a dark, ringed planet with blue aura, astrology concept, 9:16", "approx_sec": 5.0},
            {"slide_index": 12, "caption": "यह ज्योतिष का बहुत बड़ा रहस्य है।", "image_prompt": "An intricate Vedic astrology chart glowing in space, highlighting the opposite positions of Sun and Saturn, 9:16", "approx_sec": 5.0}
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
print(f"Successfully generated and injected {count} full JSON scripts (Batch 9) into the local database!")
