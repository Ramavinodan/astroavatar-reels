# Reels Content Rules — AstroAvatar (Fully Automated Production)

**Audience for this file:** Automated AI agents, script generators, and developers producing Reels in this repo.
Follow every section before generating scripts, OmniVoice/Sarvam TTS, AI visuals, or rendering.

**Product context:** **AstroAvatar** mobile app growth via Instagram + Facebook Reels (mythology + jyotish education). No founder face. Programmatic video generation.  
**Brand lock:** Product name is **AstroAvatar** only. Never use legacy or unauthorized names.

---

## 0. Mission & Operational Target

**Fully automated daily 2x video production pipeline running 24/7 on remote VM.**
- **Schedule:** 2 videos daily (08:00 AM & 18:00 PM local time).
- **Delivery:** Delivered directly to user's Telegram account/bot with post caption & hashtags.
- **Intervention:** 0 manual entry points. Self-healing with automated monitoring and error alerts.
- **Target Video Length:** 60s to 90s max (1 min to 1 min 30 sec). Controlled by script length.

---

## 1. Video Visual Format (Format-B Slideshow)

- **Format:** `format-b-slideshow.mp4` (Vertical 9:16 aspect ratio, 1080x1920 @ 30fps).
- **Visual Style:** High-quality AI generated slideshow images (9:16 vertical Indian mythology digital artwork), smooth Ken-Burns pan & zoom effect, bold readable Hindi subtitles, ambient category header badge ("ज्योतिष कथा", "रामायण कथा", "श्रीमद्भगवद्गीता"), and slide progress indicators.
- **No Heavy Puppet/Character Animations:** Simple, elegant slideshow visual transitions with cinematic atmosphere.

---

## 2. Fixed Video Structure (EVERY Reel)

Every video MUST contain these three parts in order:

| Part | Name | Detail | Duration guide |
|---|---|---|---|
| 1 | **Welcome / Intro (brand hook)** | Locked signature spoken line + logo intro clip | ~3–5s spoken |
| 2 | **Story Body (Slideshow)** | Myth / jyotish narrative + visual slides | ~50–80s narration |
| 3 | **Outro / End card** | User `end_card.mp4` (cover-crop) | **5s** (150 frames @ 30fps) |

```text
[ WELCOME / DailyDoseIntro — identical across episodes ]
[ STORY BODY — Format-B Slideshow unique per episode ]
[ OUTRO end_card.mp4 — 5 seconds ]
```

---

## 3. Script Writing & Length Control

### Language & Tone
- Conversational **bolchal Hindi** (day-to-day spoken Hindi), warm storyteller.
- Narrative vs Curiosity: ~80% story narrative / ~20% wonder beat ("पर अजीब बात यह थी...").
- Grounded in authentic Hindu culture, Ramayana, Mahabharata, Bhagavad Gita, Puranas, and Jyotish (astrology) wisdom.

### Length Control (CRITICAL)
- **Minimum total reel duration:** ≥ 60 seconds (1 minute).
- **Maximum total reel duration:** ≤ 90 seconds (1 min 30 seconds).
- **Word count target:** ~130 to 160 Hindi words for the story body (~50–75s speech).
- **Multi-Part Series Handling:** If a story is long, automatically break it into `Part 1`, `Part 2`, etc., with cliffhangers ("भाग 1/2").

---

## 4. TTS & Audio Profile

- **Primary TTS Engine:** OmniVoice / Sarvam AI Hindi TTS (`bulbul:v1` or `meera` voice).
- **Locked Voice Profile:** Male/Female warm Indian storyteller, speed `0.95`.
- **Audio Post-Processing:**
  - Bass boost (~8.0 dB)
  - Peak normalization (~-1.5 dB)
  - Soft ambient background music (BGM) mixed under voice (~0.12 volume).
- **Speech Pacing:** Never crush audio using `--duration` or `atempo`. Script length controls video duration.

---

## 5. Automation, Delivery & System Monitoring

1. **Database:** SQLite `production_history.db` logs topic history, part series, output MP4 paths, and prevents topic duplication.
2. **Telegram Delivery:** Uploads completed `.mp4` video file, title, formatted caption, and trending hashtags directly to Telegram chat.
3. **Monitoring:** Real-time system health checks and instant error notifications sent to Telegram if any stage fails.
