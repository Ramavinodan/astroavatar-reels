import type { LocalePack } from "../../i18n/types";

/**
 * Story-only narration (welcome is separate one-time brand clip).
 * Natural OmniVoice length ~52.5s — single pass, instruct voice, no duration force.
 */
export const rahuKetuLocaleHi: LocalePack = {
  locale: "hi",
  narrationFile: "narration/rahu-ketu-hi.wav",
  captions: [
    {
      text: "आज — राहु और केतु कैसे बने",
      fromFrame: 0,
      durationInFrames: 110,
    },
    {
      text: "सुनो… एक पुरानी बात",
      fromFrame: 110,
      durationInFrames: 100,
    },
    {
      text: "देवता-असुर समुद्र मंथन कर रहे थे",
      fromFrame: 210,
      durationInFrames: 180,
    },
    {
      text: "अमृत निकला · मोहिनी बाँट रही थीं",
      fromFrame: 390,
      durationInFrames: 240,
    },
    {
      text: "स्वर्भानु चुपके से घुस आया",
      fromFrame: 630,
      durationInFrames: 210,
    },
    {
      text: "सूर्य-चंद्र ने भेस पकड़ा · चक्र चला",
      fromFrame: 840,
      durationInFrames: 260,
    },
    {
      text: "पर अजीब बात… वो मरा ही नहीं",
      fromFrame: 1100,
      durationInFrames: 200,
    },
    {
      text: "सिर बना राहु · शरीर बना केतु",
      fromFrame: 1300,
      durationInFrames: 140,
    },
    {
      text: "इसीलिए ग्रहण लगता है",
      fromFrame: 1440,
      durationInFrames: 135,
    },
  ],
};

export const RAHU_KETU_TTS_SCRIPT_HI = `
आज — राहु और केतु कैसे बने।
सुनो… एक पुरानी बात।
बहुत पहले देवता और असुर मिलकर समुद्र मंथन कर रहे थे।
मंथन के बाद निकला अमृत — अमर होने वाला अमृत।
भगवान विष्णु मोहिनी रूप में आए, और अमृत देवताओं को बाँटने लगे।
सब शांत बैठे थे… पर एक असुर चुपके से लाइन में घुस आया।
उसका नाम था स्वर्भानु।
उसने देवता बनकर अमृत पी लिया।
पर सूर्य और चंद्र सोए नहीं थे।
उन्होंने भेस पकड़ लिया, और सच खोल दिया।
फिर सुदर्शन चक्र चला… सिर अलग हो गया, शरीर अलग।
पर अजीब बात ये है… वो मरा ही नहीं।
क्योंकि अमृत उसके गले उतर चुका था।
सिर बन गया राहु… शरीर बन गया केतु।
दोनों छाया ग्रह बन गए।
इसीलिए आज भी, जब राहु सूरज या चाँद को पकड़ता है… ग्रहण लग जाता है।
अब जब अगली बार ग्रहण दिखे, याद रखना — ये सिर्फ अँधेरा नहीं, एक पुरानी कथा है।
`.trim();
