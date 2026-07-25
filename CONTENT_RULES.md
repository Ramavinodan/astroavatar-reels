# Reels Content Rules — AstroAvatar

**Audience for this file:** any human or AI agent producing Reels in this repo.  
Follow every section before writing scripts, generating OmniVoice TTS, or rendering.  
If unsure, prefer these rules over improvisation.

**Product context:** **AstroAvatar** mobile app growth via Instagram + Facebook Reels (mythology + jyotish education). No founder face. Remotion = programmatic video.  
**Brand lock:** Product name is **AstroAvatar** only. Never use AskMyGuru, AskAstro, or other legacy names in scripts, captions, chips, or CTAs.

---

## 0. One-line mission

**Same welcome + same voice + same outro every time → brand memory. In the middle: one myth that teaches jyotish. Target final video length 1:00–1:30 by writing enough script — never by crushing or padding OmniVoice.**

---

## 1. Platform reality (Reels)

- We make **Instagram / Facebook Reels**, not YouTube documentaries.
- Goal funnel: **stop scroll → recognize channel → learn one idea → CTA (app)**.
- Mute-first: big on-screen Hindi text must carry the story with sound off.
- One Reel = one clear payoff (not a full Purana chapter).

---

## 2. Fixed video structure (EVERY Reel)

Every video MUST contain these three parts in order:

| Part | Name | What | Duration guide |
|---|---|---|---|
| 1 | **Welcome / Intro (brand hook)** | Same signature spoken line + same logo intro clip every episode | ~3–5s spoken |
| 2 | **Story** | Myth / jyotish narrative for this episode only | fills the middle |
| 3 | **Outro / End card** | Always append user `end_card.mp4` (cover-crop) | **5s** (trim if source is longer) |

```text
[ WELCOME / DailyDoseIntro — identical across episodes ]
[ STORY — unique per episode ]
[ OUTRO end_card.mp4 — identical ]
```

### Length control (IMPORTANT — read carefully)

**How length is controlled:** by **script writing only**.  
**How length is NOT controlled:** OmniVoice `--duration`, ffmpeg `atempo`, or any other speech-crushing.

| Rule | Detail |
|---|---|
| Minimum | Full final MP4 (welcome + story + 5s outro) **≥ 60 seconds** |
| Maximum | Full final MP4 **≤ 90 seconds** (1 min 30 sec) |
| Prefer | ~65–85s total when natural |
| How | Write enough narrative script (not ultra-short lines). Never pad with OmniVoice `--duration`. |
| Hard ban | No forced OmniVoice duration / no robotic speed-up / no fake silence padding hacks |
| If too long | **Shorten or split the script** (see §5). Never crush TTS. |
| If too short | **Add story beats** (setup / emotion / takeaway) — still existing myth only. |

Length is controlled by **script writing only**.

### End card technical

- Source: repo root `end_card.mp4` (also `reels-factory/public/end_card.mp4`).
- Fit: **cover-crop** to 1080×1920 (do not letterbox unless user asks).
- Sequence length in Remotion: **150 frames @ 30fps = 5s** (play first 5s of the file).
- Do **not** invent a second CTA card. User’s end card only.

---

## 3. Signature welcome / intro (channel memory)

### Purpose

Repeat the **same opening line + logo intro** so viewers recognize AstroAvatar Daily Dose instantly.

### Rules for the welcome line

- Bolchal Hindi, warm storyteller (not news anchor).
- Short enough to speak naturally in **~3–5 seconds**.
- Same words **every** episode (do not “improve” weekly).
- May be followed by a **one-line episode tease** that changes; the **welcome itself never changes**.
- On-screen chip during intro is fixed.

### 3.1 LOCKED welcome

```text
STATUS: LOCKED
LOCKED_WELCOME_HI: नमस्ते… AstroAvatar की डेली डोज़ में आपका स्वागत है।
ON_SCREEN_CHIP: Daily Dose · AstroAvatar
INTRO_CLIP: Remotion composition DailyDoseIntro (logo: public/brand/astroavatar_logo.png)
INTRO_VISUAL: derive from welcome audio + short hold (see src/timing/rahuKetuTiming.ts INTRO_FRAMES)
INTRO_TTS_ONE_TIME: public/narration/brand/welcome-daily-dose-hi-mixed.wav
  (generate once; do NOT regenerate per episode — regenerate only if voice recipe/text changes)
STORY_TTS: separate file per episode, e.g. narration/rahu-ketu-hi.wav (no welcome text inside)
INTRO_STANDALONE_OUT: reels-factory/out/daily-dose-intro.mp4
LOGO_SOURCE: astroavatar_logo_no_bg.png → public/brand/astroavatar_logo.png
```


Do not substitute another welcome without explicit user approval.

### Episode tease (changes each video)

Immediately after the locked welcome, optional **one short tease**, then story body.

```text
[LOCKED WELCOME]
आज — राहु और केतु कैसे बने।
[STORY BODY…]
```

---

## 4. Script rules (story body)

### Language

- Conversational **bolchal Hindi** (day-to-day), not shuddh / textbook.
- Later locales: swap captions + TTS only; visuals stay (see §8).

### Tone

- Pleasant **narrative storyteller** talking to a friend.
- Never flat manual-reading or uninterested news-reader energy.
- Never quiz-mode interrogation.

### Narrative vs curiosity balance

- Roughly **~80% narration / ~20% curiosity**.
- Prefer **1 soft wonder beat** (max 2): thinking-aloud style  
  ✅ `पर अजीब बात ये है… वो मरा ही नहीं।`  
  ❌ `कौन? क्यों? समझे? अब बोलो?`
- Do not dump facts linearly. Tease → reveal → punch.

### Script length (this is the only duration control)

Write welcome + tease + story so that **natural OmniVoice speech** (no duration flag) + 5s outro lands between **60s and 90s**.

Practical guide (bolchal Hindi, narrative pace):

- Welcome is ~3–5s (fixed one-time clip). Outro is 5s.  
- So story speech alone should usually land around **~50–80 seconds**.  
- Prefer fuller storytelling (names, setup, wonder, takeaway) — not telegram-short lines.  
- If draft would run **over ~80s of story speech** → cut or split Reels before TTS.  
- If draft would run **under ~50s of story speech** → expand myth beats before TTS.

### Story body structure

1. Short episode tease (optional, after welcome)  
2. Setup  
3. Turn / climax  
4. One clear jyotish takeaway  

### Existing stories only

- Use real Purana / traditional narratives already on the public internet.
- **Do not invent new myths.** Soft wording OK; plot must be traditional.

### Bad vs good (story body)

```text
❌ BAD: linear encyclopedia dump + stacked quiz questions
✅ GOOD: flowing story + one wonder line + clear “इसीलिए…” takeaway
```

---

## 5. If story is too long

| Option | When |
|---|---|
| **A. Cut short** | Keep setup + climax + takeaway; rewrite script shorter |
| **B. Split into N Reels** | Same myth; cliffhanger on Reel k; payoff on k+1 |

**Never** use OmniVoice `--duration` or `atempo` to force a long script into a short video.

Series rules:

- Reels 1…N-1: welcome + story part + **soft cliffhanger**; outro end card optional (prefer skip or 3s).
- Final Reel: welcome + climax/takeaway + **full 5s end card**.
- Naming: `story-id-part-01`, `part-02`, …

---

## 6. OmniVoice TTS — voice + pleasant tone

### Does “script for 60–90s + no OmniVoice duration” work?

**Yes.** That is the correct approach:

1. **Voice identity** stays consistent via locked instruct + seed (current lock — **no ref clone**).  
2. **Pleasant narrative tone** stays intact because we never crush pacing.  
3. **Length** lands in **60–90s** because the **script** is written long enough (not padded/crushed).

### Voice consistency

**Yes, achievable** when we lock the same generator recipe every episode (proven: 4 identical runs with seed).  
Prefer **1 single pass** for the full story (and 1 for welcome) so there are no mid-video voice seams.

### Locked voice profile (CURRENT)

Update this block only when user explicitly changes voice.

```text
ENGINE: OmniVoice (CLI: omnivoice-infer OR Python OmniVoice.from_pretrained)
MODEL: k2-fsa/OmniVoice
MODE: voice design via --instruct  (NO ref_audio clone)
INSTRUCT: male, middle-aged, indian accent, moderate pitch
LANGUAGE: Hindi
SPEED: 0.95
NUM_STEP: 40
DEVICE: mps (device_map="mps", dtype=float16)
SEED: 42
DURATION: FORBIDDEN  # never pass --duration / duration= to OmniVoice
ATEMPO: FORBIDDEN    # never speed-crush after generate
BASS_POST: torchaudio bass_biquad gain ≈ 8.0 dB, then peak normalize ~0.95
CHUNKS: MINIMIZE — prefer 1 pass for welcome, 1 pass for full story (max 2 if model fails)
BGM: soft pad under voice, volume ≈ 0.10–0.14 vs voice; fade in/out
MIX_OUT: reels-factory/public/narration/<episode>-hi.wav
WELCOME_OUT: reels-factory/public/narration/brand/welcome-daily-dose-hi-mixed.wav
```

### OmniVoice valid instruct keywords (English only, comma+space)

`male`, `female`, `child`, `teenager`, `young adult`, `middle-aged`, `elderly`,  
`low pitch`, `moderate pitch`, `high pitch`, `very low pitch`, `very high pitch`, `whisper`,  
`indian accent`, `american accent`, `british accent`, `australian accent`, `canadian accent`,  
`chinese accent`, `japanese accent`, `korean accent`, `portuguese accent`, `russian accent`

### Generation recipe (agents must follow)

1. Write story script so natural speech + fixed welcome + 5s outro lands **60–90s**.  
2. Save story text: `stories/tts/<episode>-hi.txt` (**no welcome line** — welcome is one-time brand audio).  
3. Generate with locked profile — **no duration argument anywhere**.  
4. **Minimize chunks:** default **1 single pass** for the whole story. Only split (max 2) if generation fails on length. Multi-chunk seams cause mid-video voice jumps.  
5. Welcome = one-time file under `narration/brand/` — regenerate only when the locked voice recipe changes; use the **same** instruct/settings as story.  
6. Bass (~8 dB) + normalize; mix soft BGM on story.  
7. Remotion duration follows actual audio lengths (+ intro hold + 5s end card).  
8. If total &lt; 60s → expand script. If total &gt; 90s → cut/split. Never crush TTS.

### Anti-patterns (voice / tone)

- ❌ Passing `--duration` / `duration=` to OmniVoice  
- ❌ `atempo` / speed-up to hit an old 30s/42s cap  
- ❌ New random instruct / ref each episode  
- ❌ Splitting story into many chunks (causes mid-video voice jumps)  
- ❌ Stacking quiz questions in TTS  
- ❌ Generating welcome with different voice settings than story  
- ❌ Cloning `omnivoice/audio2.wav` / elderly ref unless user explicitly asks  

### Known failure mode (do not repeat)

Forcing OmniVoice `duration` keeps **voice identity** but destroys **pleasant narrative tone** (flat / rushed reader).  
Consistency of voice ≠ quality of tone. Protect tone by never forcing duration.

---

## 7. Visual / Remotion rules

- Composition size: **1080×1920**, **30 fps**.
- Not Ken Burns-only — sprites must move (enter, meet, chase, split, aura).
- No gore; tasteful light/silhouette for violent myth beats.
- Captions ≥ ~48–52px; titles readable on phone.
- Locale captions timed to narration; mute-first.
- Welcome on-screen chip identical across episodes.
- Composition length = **actual narration frames + intro hold if needed + 5s outro** (derive from audio; don’t invent a fake cap).
- Project: `reels-factory/`. Assets: `reels-assets/` + `reels-factory/public/`.
- Locale swap later: `reels-factory/LOCALE_SWAP.md`.

---

## 8. Locale / South India later

- Visuals language-agnostic.
- Swap: `LocalePack` captions + `narrationFile`.
- Primary: bolchal Hindi.
- Welcome line translated once and locked per locale.

---

## 9. File / naming conventions

```text
stories/tts/welcome-hi.txt            # locked welcome only (one-time TTS)
stories/tts/<episode>-hi.txt          # story spoken script ONLY (no welcome line)
stories/STORY_*.md                    # story research / beats
reels-factory/public/narration/       # episode wav + bgm
reels-factory/public/narration/brand/ # one-time welcome wav
reels-factory/src/stories/<id>/locale.hi.ts
reels-factory/src/timing/*Timing.ts   # INTRO/STORY/END frames from audio
reels-factory/out/<episode>.mp4       # final render
CONTENT_RULES.md                      # this file — source of truth
```

---

## 10. Pre-ship checklist

- [ ] Welcome = **exact** `LOCKED_WELCOME_HI`  
- [ ] Story narrative-first (≤2 wonder beats)  
- [ ] Final video length between **60s and 90s**  
- [ ] OmniVoice generated with **no duration / no atempo / no ref clone** (unless user asks)  
- [ ] Story TTS = **1 single pass** when possible (avoid multi-chunk seams)  
- [ ] Welcome + story use same locked instruct profile  
- [ ] Outro = `end_card.mp4` cover-crop **5s**  
- [ ] Soft BGM under voice  
- [ ] Big mute-safe captions  
- [ ] Existing myth only  
- [ ] Locale pack + TTS script committed  

---

## 11. Agent workflow (do in order)

1. Read this entire file.  
2. Research existing myth if new episode.  
3. Write story script (no welcome) so full Reel lands **1:00–1:30**.  
4. Generate OmniVoice story with **locked voice profile** — **never pass duration**. Reuse one-time welcome clip.  
5. Build/adjust Remotion to match **actual** audio length; append 5s end card.  
6. Render; confirm total is **60–90s**; run checklist §10.

---

## 12. Current episode notes (Rahu–Ketu)

- Composition: `RahuKetuOrigin` + reusable `DailyDoseIntro`  
- Welcome: **LOCKED** (Daily Dose line)  
- Voice lock: `male, middle-aged, indian accent, moderate pitch` + seed 42 + speed 0.95 + bass 8 dB (see §6) — **no ref clone**  
- TTS: welcome 1 pass + story 1 pass  
- Outro: `end_card.mp4` 5s cover-crop  
- Duration policy: **final video 60–90s via script length; no OmniVoice duration force**  
- Approved cut: `reels-factory/out/rahu-ketu-origin.mp4` (~61s)
