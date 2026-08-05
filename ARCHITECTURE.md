# AstroAvatar Reels — Automated Video Production Architecture

Complete technical architecture documentation for the zero-flaw, 100% automated daily video production and delivery system for **AstroAvatar** (Instagram & Facebook Reels).

---

## 1. High-Level Architecture Diagram

```text
+-----------------------------------------------------------------------------------+
|                            AUTOMATED SCHEDULER (Cron/Systemd)                     |
|                         Runs 2x Daily (08:00 AM & 18:00 PM)                       |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
|                            CENTRAL PIPELINE ORCHESTRATOR                          |
|                             (scripts/pipeline_runner.py)                          |
|  - Runs as two separate parallel instances: `30sec/` and `90sec/`                 |
|  - Independent SQLite DBs (`production_history.db`) in each folder                |
|  - Automatic retries & Telegram monitoring alerts on failure                       |
+-----------------------------------------------------------------------------------+
    |                   |                       |                      |
    v                   v                       v                      v
[1. Script & Beat]  [2. AI Image Gen]       [3. OmniVoice TTS]     [4. Dynamic Remotion]
- Cheap LLM API     - Pollinations AI /     - Locked profile       - Format-B Slideshow
  (Sarvam /           Fal.ai (9:16 vertical   - Bass Boost (8dB)     - Welcome Intro (4s)
   DeepSeek / Flash)  mythological art)       - Audio Alignment      - Timed Slideshow
- 60s-90s pacing                               - Soft BGM Overlay     - Outro End Card (5s)
- Auto multi-part
                                          |
                                          v
+-----------------------------------------------------------------------------------+
|                              TELEGRAM PUBLISHER & MONITOR                         |
|                             (scripts/telegram_publisher.py)                       |
|  - Sends final 1080x1920 MP4 + post text + hashtags directly to Telegram           |
|  - Real-time health metrics, disk/RAM diagnostics, and error stacktraces           |
+-----------------------------------------------------------------------------------+
```

---

## 2. Component Specifications

### 2.1 Topic Catalog & Selection (`scripts/topic_catalog.py`)
- Maintains a curated registry of topics across 6 primary categories:
  1. **ज्योतिष कथा** (Vedic Astrology stories & planet origins)
  2. **रामायण कथा** (Ramayana episodes & teachings)
  3. **श्रीमद्भगवद्गीता** (Gita Shlokas & practical philosophy)
  4. **महाभारत रहस्य** (Mahabharata stories & karmic lessons)
  5. **शिव पुराण** (Lord Shiva legends & spiritual significance)
  6. **नक्षत्र एवं ग्रह ज्ञान** (Graha transits, Nakshatra secrets, Sade Sati)
- Queries SQLite history to ensure **zero topic repetition** until the catalog is cycled.

### 2.2 LLM Story Generator (`scripts/story_generator.py`)
- Connects to cheap/fast LLM APIs (Sarvam AI / DeepSeek / Gemini Flash / OpenAI).
- Enforces strict Bolchal Hindi conversational storytelling rules.
- Pacing: ~130 to 160 Hindi words for ~50 to 75s speech.
- **Multi-Part Handler:** If story length exceeds 90s total video limit, automatically splits narrative into `Part 1`, `Part 2` with cliffhangers and saves state in SQLite DB.
- Outputs structured JSON with slide captions and visual AI image prompts.

### 2.3 AI Image Batch Generator (`scripts/image_generator.py`)
- Fetches high-definition 9:16 vertical images per slide via Pollinations.ai / Fal.ai.
- Style lock: Epic Indian mythology digital art, vibrant gold & dark cosmic tones.
- Fallback logic: Automatically uses default atmospheric slide plates if network timeout occurs.

### 2.4 OmniVoice & Audio Processing Pipeline (`scripts/tts_generator.py`)
- Synthesizes speech using OmniVoice TTS (or Sarvam AI Hindi TTS).
- Audio filter chain (via FFmpeg):
  - **Bass Boost:** `bass=g=8` (~8.0 dB gain for warm narrative voice).
  - **Peak Normalization:** `loudnorm=I=-16:LRA=11:TP=-1.5`.
  - **BGM Overlay:** Soft cosmic ambient background track mixed under speech (`volume=0.12`).
- Computes exact speech duration and scales per-slide `endSec` timestamps for perfect caption synchronization.

### 2.5 Dynamic Remotion Renderer (`reels-factory/src/compositions/DynamicSlideshow.tsx`)
- Renders 1080x1920 30fps vertical MP4 video using Remotion CLI (`npx remotion render DynamicSlideshow`).
- Features:
  - **Intro:** Locked 4-second AstroAvatar logo welcome intro (`DailyDoseIntro`).
  - **Body:** Ken-Burns pan/zoom slideshow animation, ambient gradient vignette, bold Hindi subtitle card, category badge, slide progress indicators.
  - **Outro:** Fixed 5-second brand end card (`end_card.mp4`).

### 2.6 Telegram Publisher & Health Monitor (`scripts/telegram_publisher.py`)
- Uses Telegram Bot API to upload completed video `.mp4` file along with title, caption text, app branding, and hashtags.
- Sends instant system health reports and error stacktraces on failure.

---

## 3. Remote VM Deployment & Automation Strategy

- **Remote VM Environment:** Ubuntu 22.04 LTS (ARM64).
- **Scheduler:** Crontab configured to execute twice daily (08:00 AM & 18:00 PM). It can run either or both pipelines:
  ```bash
  # Phase 1: 30sec pipeline (Acquisition)
  0 8 * * * cd /home/ubuntu/astroavatar-reels/30sec && /usr/bin/python3 scripts/pipeline_runner.py >> logs/cron.log 2>&1
  0 18 * * * cd /home/ubuntu/astroavatar-reels/30sec && /usr/bin/python3 scripts/pipeline_runner.py >> logs/cron.log 2>&1
  
  # Phase 2: 90sec pipeline (Retention)
  # 0 8 * * * cd /home/ubuntu/astroavatar-reels/90sec && /usr/bin/python3 scripts/pipeline_runner.py >> logs/cron.log 2>&1
  # 0 18 * * * cd /home/ubuntu/astroavatar-reels/90sec && /usr/bin/python3 scripts/pipeline_runner.py >> logs/cron.log 2>&1
  ```
- **Git Policy:** Strictly **no direct code changes on the VM**. All code changes originate from the local git repository and are deployed via `deploy/deploy_to_vm.sh`.
