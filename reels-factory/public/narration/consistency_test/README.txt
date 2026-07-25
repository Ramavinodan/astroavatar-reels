Voice consistency test — 4 runs, identical code/params

STORY: (same every run)
नमस्ते... AstroAvatar की डेली डोज़ में आपका स्वागत है। आज — राहु और केतु कैसे बने। सुनो... एक पुरानी बात। समुद्र मंथन में अमृत निकला। विष्णु मोहिनी रूप में उसे देवताओं को बाँट रहे थे। तभी एक असुर बीच में घुस आया, और अमृत पी गया। सूर्य चंद्र ने पकड़ लिया। चक्र चला। सिर अलग हो गया। पर अजीब बात ये है... वो मरा ही नहीं। सिर बन गया राहु, शरीर बन गया केतु। इसीलिए आज भी, जब राहु सूरज चाँद को पकड़ता है... ग्रहण लग जाता है।

PARAMS:
  model: k2-fsa/OmniVoice
  instruct: male, middle-aged, indian accent, moderate pitch
  language: Hindi
  speed: 0.95
  num_step: 40
  duration: 22.0
  seed: 42
  bass_biquad gain: 8.0
  device: mps
  generation: single-pass (one generate call per run)

Listen to run_01.wav … run_04.wav back-to-back.
If they sound the same → consistency usable for daily Reels.
If they drift → we need ref_audio clone lock or accept small variation.
