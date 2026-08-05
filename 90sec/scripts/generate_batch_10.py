import sqlite3
import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "production_history.db")

batch_data = {
    "chandra_curse": {
        "story_id": "chandra_curse",
        "title": "चंद्रमा को क्षय रोग का श्राप",
        "category": "नक्षत्र एवं ग्रह ज्ञान",
        "script_hi": "चंद्रमा का आकार हर दिन घटता और बढ़ता क्यों है? इसके पीछे राजा दक्ष का एक भयंकर श्राप है। प्रजापति दक्ष ने अपनी 27 पुत्रियों (जो कि 27 नक्षत्र हैं) का विवाह चंद्र देव से किया था। दक्ष ने शर्त रखी थी कि चंद्रमा अपनी सभी 27 पत्नियों को एक समान प्रेम देंगे। लेकिन चंद्रमा अपनी एक पत्नी 'रोहिणी' से सबसे ज़्यादा प्रेम करते थे और बाकी 26 पत्नियों को समय नहीं देते थे। जब दक्ष को यह बात पता चली, तो उन्होंने क्रोध में आकर चंद्रमा को श्राप दे दिया कि 'तुम्हारा सारा तेज़ और सुंदरता धीरे-धीरे खत्म हो जाएगी और तुम्हें क्षय रोग (Tuberculosis) हो जाएगा!' श्राप के कारण चंद्रमा काले पड़ने लगे और उनका आकार सिकुड़ने लगा। पूरे ब्रह्मांड में हाहाकार मच गया। मृत्यु के करीब पहुंच चुके चंद्रमा ने भगवान शिव की घोर तपस्या की। शिव जी ने प्रसन्न होकर चंद्रमा को अपनी जटाओं में धारण कर लिया और उन्हें मृत्यु से बचा लिया। शिव के वरदान से श्राप का प्रभाव आधा हो गया। यही कारण है कि 15 दिन तक चंद्रमा का आकार घटता है (कृष्ण पक्ष), लेकिन अगले 15 दिन शिव की कृपा से वह फिर से बढ़ने लगता है (शुक्ल पक्ष)।",
        "estimated_speech_sec": 105.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "चंद्रमा का आकार हर दिन घटता-बढ़ता क्यों है?", "image_prompt": "A glowing silver full moon transitioning into a thin crescent moon in the night sky, mystical, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "प्रजापति दक्ष ने अपनी 27 पुत्रियों का विवाह चंद्रमा से किया।", "image_prompt": "Moon God (Chandra Dev) glowing beautifully, surrounded by 27 beautiful goddesses representing the Nakshatras, 9:16", "approx_sec": 6.0},
            {"slide_index": 3, "caption": "शर्त थी कि वे सबको समान प्रेम देंगे।", "image_prompt": "King Daksha holding up a finger, giving a strict warning to the Moon God during the grand wedding, 9:16", "approx_sec": 5.0},
            {"slide_index": 4, "caption": "लेकिन चंद्रमा केवल 'रोहिणी' से प्रेम करते थे।", "image_prompt": "Moon God spending all his time lovingly with Goddess Rohini, ignoring the other sad 26 wives in the background, 9:16", "approx_sec": 6.0},
            {"slide_index": 5, "caption": "दक्ष को यह बात पता चली।", "image_prompt": "The 26 crying daughters complaining to their angry father, King Daksha, ancient palace setting, 9:16", "approx_sec": 5.0},
            {"slide_index": 6, "caption": "क्रोध में उन्होंने चंद्रमा को क्षय रोग का श्राप दिया।", "image_prompt": "King Daksha furiously throwing cursed water from his pot, a dark energy flying towards the Moon God, 9:16", "approx_sec": 5.0},
            {"slide_index": 7, "caption": "चंद्रमा काले पड़ने लगे और सिकुड़ने लगे।", "image_prompt": "The glowing Moon God coughing, looking very sick, his skin turning dark and body shrinking, 9:16", "approx_sec": 5.0},
            {"slide_index": 8, "caption": "ब्रह्मांड में हाहाकार मच गया।", "image_prompt": "The earth plunged into deep darkness, plants withering, gods panicking in the heavens, 9:16", "approx_sec": 5.0},
            {"slide_index": 9, "caption": "चंद्रमा ने भगवान शिव की तपस्या की।", "image_prompt": "A very weak, thin Moon God praying desperately in front of a Shiva Linga, dying light, 9:16", "approx_sec": 5.0},
            {"slide_index": 10, "caption": "शिव जी ने उन्हें अपनी जटाओं में धारण कर लिया।", "image_prompt": "Lord Shiva gracefully lifting the crescent moon and placing it on his beautiful matted hair, glowing blue aura, 9:16", "approx_sec": 6.0},
            {"slide_index": 11, "caption": "शिव के वरदान से श्राप आधा हो गया।", "image_prompt": "The Moon regaining its bright silver glow while resting safely on Lord Shiva's head, 9:16", "approx_sec": 5.0},
            {"slide_index": 12, "caption": "इसीलिए 15 दिन चंद्रमा घटता है, और 15 दिन बढ़ता है।", "image_prompt": "A time-lapse view of the lunar phases, from full moon to new moon, beautiful cosmic astrology art, 9:16", "approx_sec": 6.0}
        ]
    },
    "brihaspati_shukracharya": {
        "story_id": "brihaspati_shukracharya",
        "title": "देवगुरु बृहस्पति और दैत्यगुरु शुक्राचार्य",
        "category": "नक्षत्र एवं ग्रह ज्ञान",
        "script_hi": "वैदिक ज्योतिष में देवगुरु बृहस्पति और दैत्यगुरु शुक्राचार्य दोनों को 'गुरु' क्यों माना जाता है? बृहस्पति (Jupiter) देवताओं के गुरु हैं, जो धर्म, नीति, सात्विक ज्ञान और आध्यात्मिकता का प्रतीक हैं। दूसरी ओर, शुक्राचार्य (Venus) दैत्यों (असुरों) के गुरु हैं, जो भौतिक सुख, सुंदरता, कला और सांसारिक ज्ञान के प्रतीक हैं। दोनों ही परम ज्ञानी हैं, लेकिन दोनों का रास्ता अलग है। एक बार देवताओं और असुरों के बीच भयंकर युद्ध हुआ। देवताओं के गुरु बृहस्पति के पास अच्छी नीतियां थीं, लेकिन असुरों के गुरु शुक्राचार्य के पास एक ऐसा रहस्य था, जो बृहस्पति के पास नहीं था—'संजीवनी विद्या'! इस विद्या से शुक्राचार्य मरे हुए असुरों को फिर से ज़िंदा कर देते थे। इसीलिए युद्ध में असुर बार-बार उठ खड़े होते थे। शुक्राचार्य ने यह विद्या भगवान शिव की उल्टे लटक कर घोर तपस्या करके प्राप्त की थी। ज्योतिष में आज भी बृहस्पति आपको 'आंतरिक शांति' (Inner Peace) देते हैं, जबकि शुक्र आपको 'बाहरी सुख और धन' (Material Wealth) देते हैं। जीवन में सफल होने के लिए इंसान को इन दोनों गुरुओं के ज्ञान की आवश्यकता होती है।",
        "estimated_speech_sec": 105.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "बृहस्पति और शुक्राचार्य दोनों ही 'गुरु' क्यों हैं?", "image_prompt": "A majestic split-screen cosmic portrait: Glowing golden Jupiter on one side, and bright shining Venus on the other, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "बृहस्पति देवताओं के गुरु हैं।", "image_prompt": "Guru Brihaspati, wearing yellow robes, teaching divine knowledge to Lord Indra and other gods, peaceful, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "वे धर्म और आध्यात्मिकता के प्रतीक हैं।", "image_prompt": "A glowing golden ancient book (Vedas) radiating pure spiritual light, symbolizing divine wisdom, 9:16", "approx_sec": 5.0},
            {"slide_index": 4, "caption": "शुक्राचार्य दैत्यों के गुरु हैं।", "image_prompt": "Guru Shukracharya with one eye, wearing white/silver robes, teaching powerful spells to fierce demons, 9:16", "approx_sec": 5.0},
            {"slide_index": 5, "caption": "वे भौतिक सुख, कला और धन के प्रतीक हैं।", "image_prompt": "A luxurious ancient palace filled with gold, jewels, beautiful art, and romantic lighting, 9:16", "approx_sec": 5.0},
            {"slide_index": 6, "caption": "देवताओं और असुरों के बीच भयंकर युद्ध हुआ।", "image_prompt": "An epic cosmic battle between glowing gods and dark demons in the heavens, weapons clashing, 9:16", "approx_sec": 5.0},
            {"slide_index": 7, "caption": "शुक्राचार्य के पास एक रहस्य था...", "image_prompt": "Shukracharya holding a glowing magical vial of Sanjeevani, radiating intense green healing energy, 9:16", "approx_sec": 5.0},
            {"slide_index": 8, "caption": "'संजीवनी विद्या'! वे मरे हुओं को ज़िंदा कर देते थे।", "image_prompt": "Shukracharya chanting mantras over dead demons on the battlefield, the demons magically waking up and glowing, 9:16", "approx_sec": 6.0},
            {"slide_index": 9, "caption": "उन्होंने शिव की उल्टे लटक कर तपस्या की थी।", "image_prompt": "Shukracharya hanging upside down from a tree over a smoky fire, meditating fiercely on Lord Shiva, 9:16", "approx_sec": 5.0},
            {"slide_index": 10, "caption": "बृहस्पति आंतरिक शांति देते हैं।", "image_prompt": "A person meditating calmly in a glowing yellow aura, feeling absolute inner peace and connection with God, 9:16", "approx_sec": 5.0},
            {"slide_index": 11, "caption": "जबकि शुक्र बाहरी सुख और धन देते हैं।", "image_prompt": "A person enjoying immense luxury, beautiful clothes, and success in a bright, diamond-like aura, 9:16", "approx_sec": 5.0},
            {"slide_index": 12, "caption": "सफल जीवन के लिए दोनों का ज्ञान ज़रूरी है।", "image_prompt": "A beautiful balanced scale holding a glowing golden lotus (spiritual) and a diamond (material), perfect harmony, 9:16", "approx_sec": 6.0}
        ]
    },
    "manglik_energy": {
        "story_id": "manglik_energy",
        "title": "मंगल दोष: ऊर्जा या श्राप?",
        "category": "नक्षत्र एवं ग्रह ज्ञान",
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
    },
    "budh_tara_birth": {
        "story_id": "budh_tara_birth",
        "title": "बुध (Mercury) का रहस्यमयी जन्म",
        "category": "नक्षत्र एवं ग्रह ज्ञान",
        "script_hi": "बुध ग्रह (Mercury) को ज्योतिष में सबसे बुद्धिमान और चतुर क्यों माना जाता है? बुध के जन्म की कथा बहुत ही रहस्यमयी है। देवगुरु बृहस्पति की पत्नी का नाम 'तारा' था। तारा बहुत ही सुंदर थीं, लेकिन वे अपने पति बृहस्पति की अत्यधिक धार्मिक और व्यस्त दिनचर्या से खुश नहीं थीं। एक दिन, चंद्रमा (Moon God) ने तारा को देखा और दोनों एक-दूसरे के प्रेम में पड़ गए। तारा ने बृहस्पति का घर छोड़ दिया और चंद्रमा के साथ रहने लगीं। बृहस्पति को बहुत क्रोध आया और उन्होंने युद्ध की घोषणा कर दी। देवताओं और असुरों के बीच भयंकर युद्ध छिड़ गया, जिसे 'तारकामय युद्ध' कहा जाता है। अंततः ब्रह्मा जी ने बीच-बचाव किया और तारा को बृहस्पति के पास वापस भेज दिया। लेकिन तब तक तारा गर्भवती हो चुकी थीं। जब बच्चे का जन्म हुआ, तो वह इतना सुंदर, बुद्धिमान और तेज़ था कि देवता हैरान रह गए। बृहस्पति और चंद्रमा दोनों ने उस बच्चे पर अपना हक़ जताया। ब्रह्मा जी के पूछने पर तारा ने सच बताया कि यह चंद्रमा का पुत्र है। यह बालक ही 'बुध ग्रह' बना। बुध के पास चंद्रमा (पिता) जैसी कल्पना और बृहस्पति (सौतेले पिता) जैसा ज्ञान है, इसलिए वह ज्योतिष में बुद्धि और व्यापार (Intelligence and Business) का सबसे शक्तिशाली ग्रह है।",
        "estimated_speech_sec": 110.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "बुध ग्रह सबसे चतुर और बुद्धिमान क्यों है?", "image_prompt": "A glowing green planet Mercury surrounded by mathematical symbols and ancient scripts, cosmic intelligence, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "देवगुरु बृहस्पति की पत्नी तारा बहुत सुंदर थीं।", "image_prompt": "Goddess Tara, wearing beautiful celestial clothes, looking slightly sad sitting in Guru Brihaspati's ashram, 9:16", "approx_sec": 5.0},
            {"slide_index": 3, "caption": "वे बृहस्पति की व्यस्त दिनचर्या से खुश नहीं थीं।", "image_prompt": "Guru Brihaspati completely immersed in reading heavy glowing ancient books, ignoring his wife Tara in the background, 9:16", "approx_sec": 6.0},
            {"slide_index": 4, "caption": "चंद्रमा और तारा एक-दूसरे के प्रेम में पड़ गए।", "image_prompt": "The handsome Moon God glowing in silver light, holding Goddess Tara's hand tenderly under a starry sky, 9:16", "approx_sec": 5.0},
            {"slide_index": 5, "caption": "बृहस्पति को बहुत क्रोध आया।", "image_prompt": "Guru Brihaspati looking furious, his yellow aura turning into a fiery orange, raising a staff in anger, 9:16", "approx_sec": 5.0},
            {"slide_index": 6, "caption": "देवताओं में 'तारकामय युद्ध' छिड़ गया।", "image_prompt": "Gods fighting each other in the cosmos, Moon God on a chariot shooting arrows of light, epic war, 9:16", "approx_sec": 5.0},
            {"slide_index": 7, "caption": "ब्रह्मा जी ने युद्ध रुकवाया और तारा को वापस भेजा।", "image_prompt": "Lord Brahma appearing massive in the sky, raising his hand, stopping the war and restoring order, 9:16", "approx_sec": 5.0},
            {"slide_index": 8, "caption": "तारा ने एक अत्यंत सुंदर और बुद्धिमान बालक को जन्म दिया।", "image_prompt": "Goddess Tara holding a newborn boy who is naturally glowing with a bright green intelligent aura, 9:16", "approx_sec": 6.0},
            {"slide_index": 9, "caption": "चंद्रमा और बृहस्पति दोनों ने हक़ जताया।", "image_prompt": "Moon God and Guru Brihaspati both pulling the arms of the glowing child, arguing over fatherhood, 9:16", "approx_sec": 5.0},
            {"slide_index": 10, "caption": "तारा ने बताया कि यह चंद्रमा का पुत्र है।", "image_prompt": "Goddess Tara looking down shyly but speaking the truth in front of Lord Brahma, pointing to the Moon God, 9:16", "approx_sec": 6.0},
            {"slide_index": 11, "caption": "यह बालक ही 'बुध ग्रह' बना।", "image_prompt": "The young boy growing into Lord Budha (Mercury), holding a book and riding a mythical lion-elephant creature (Yali), 9:16", "approx_sec": 6.0},
            {"slide_index": 12, "caption": "बुध के पास दोनों (चंद्रमा और गुरु) के गुण हैं।", "image_prompt": "A split aura behind Lord Budha, silver imagination of Moon on one side, golden wisdom of Jupiter on the other, 9:16", "approx_sec": 6.0}
        ]
    },
    "kaal_sarp_dosh": {
        "story_id": "kaal_sarp_dosh",
        "title": "काल सर्प दोष का असली मतलब",
        "category": "नक्षत्र एवं ग्रह ज्ञान",
        "script_hi": "ज्योतिष में काल सर्प दोष क्या होता है और इससे लोग इतना क्यों डरते हैं? हिंदू धर्म में राहु को 'सर्प का सिर' (Snake's head) और केतु को 'सर्प की पूंछ' (Snake's tail) माना जाता है। जब किसी व्यक्ति की जन्म कुंडली में बाकी सभी 7 ग्रह (सूर्य, चंद्र, मंगल, बुध, गुरु, शुक्र, शनि) राहु और केतु के बीच में आकर फंस जाते हैं, तो उसे 'काल सर्प दोष' कहा जाता है। इसका मतलब है कि व्यक्ति की किस्मत और ग्रहों की ताकत को एक 'सांप' ने जकड़ लिया है। लोग डरते हैं कि इस दोष से जीवन में गरीबी, बीमारियां, काम में रुकावटें और दुर्भाग्य आता है। लेकिन डरने की कोई बात नहीं है! इतिहास में कई महान लोगों की कुंडली में काल सर्प दोष था, जैसे धीरूभाई अंबानी और सचिन तेंदुलकर। यह दोष इंसान के जीवन में शुरुआती संघर्ष (Struggle) बहुत बढ़ा देता है, लेकिन अगर व्यक्ति कड़ी मेहनत करे और हार न माने, तो 35-40 साल की उम्र के बाद यही दोष उसे दुनिया के सबसे ऊंचे शिखर पर पहुंचा देता है। काल सर्प दोष श्राप नहीं, बल्कि एक कठिन परीक्षा है।",
        "estimated_speech_sec": 95.0,
        "part_info": { "current_part": 1, "total_parts": 1 },
        "slides": [
            {"slide_index": 1, "caption": "काल सर्प दोष क्या होता है?", "image_prompt": "A glowing Vedic astrology Kundali chart heavily entangled in the thick coils of a giant dark serpent, 9:16", "approx_sec": 5.0},
            {"slide_index": 2, "caption": "राहु 'सर्प का सिर' है और केतु 'सर्प की पूंछ'।", "image_prompt": "A huge terrifying shadow snake in space, head representing Rahu (North node) and tail representing Ketu (South node), 9:16", "approx_sec": 6.0},
            {"slide_index": 3, "caption": "जब सभी 7 ग्रह राहु और केतु के बीच फंस जाते हैं...", "image_prompt": "Seven glowing colorful planets perfectly trapped in a line inside the belly of the giant cosmic snake, 9:16", "approx_sec": 5.0},
            {"slide_index": 4, "caption": "तो उसे 'काल सर्प दोष' कहते हैं।", "image_prompt": "The jaws of the snake closing in around a glowing golden sun, dark mystical vibes, astrology concept, 9:16", "approx_sec": 5.0},
            {"slide_index": 5, "caption": "लोग सोचते हैं इससे सिर्फ दुर्भाग्य आता है।", "image_prompt": "A person sitting with head in hands, looking depressed, surrounded by a subtle dark snake-like aura, 9:16", "approx_sec": 5.0},
            {"slide_index": 6, "caption": "काम में रुकावटें और संघर्ष बढ़ जाता है।", "image_prompt": "A person trying to climb a steep, rocky mountain, but thick snake-like vines keep pulling him down, 9:16", "approx_sec": 5.0},
            {"slide_index": 7, "caption": "लेकिन डरने की कोई बात नहीं है!", "image_prompt": "A bright golden light suddenly piercing through the dark snake vines, breaking them apart, 9:16", "approx_sec": 5.0},
            {"slide_index": 8, "caption": "कई महान लोगों की कुंडली में यह दोष था।", "image_prompt": "Silhouettes of highly successful people standing proudly on a mountain peak, holding trophies and wealth, 9:16", "approx_sec": 5.0},
            {"slide_index": 9, "caption": "यह शुरुआती संघर्ष बहुत बढ़ा देता है।", "image_prompt": "A blacksmith hammering a glowing red hot piece of metal very hard, forging it into something strong, 9:16", "approx_sec": 5.0},
            {"slide_index": 10, "caption": "लेकिन अगर आप मेहनत करें और हार न मानें...", "image_prompt": "A warrior passionately fighting through a dark storm with a glowing sword of determination, never giving up, 9:16", "approx_sec": 6.0},
            {"slide_index": 11, "caption": "तो यही दोष आपको सबसे ऊंचे शिखर पर पहुंचाता है।", "image_prompt": "The same person standing at the absolute top of the world, bathed in golden sunlight, extremely successful, 9:16", "approx_sec": 6.0},
            {"slide_index": 12, "caption": "यह श्राप नहीं, एक कठिन परीक्षा है।", "image_prompt": "A giant beautiful golden serpent protecting a massive treasure, symbolizing wealth through hard trials, 9:16", "approx_sec": 5.0}
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
print(f"Successfully generated and injected {count} full JSON scripts (Batch 10) into the local database!")
