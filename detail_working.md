# AstroAvatar Reels Generator - Detailed Working Guide

This document explains the complete end-to-end architecture and pipeline for generating AstroAvatar videos. It is specifically written to provide 100% context to any AI agent (like Cursor) working on this repository, detailing how data flows, how assets are generated, and how the final video is assembled.

---

## 1. System Overview & Database

The entire system is driven by a local SQLite database: `production_history.db`.
All operations are fully local to this Mac (the VM is no longer used).

### Core Database Tables:
*   **`topic_catalog`**: Stores all available video topics. The most critical column is `pregenerated_json`. This column contains the **full AI-generated script, subtitle captions, and image prompts** for the video.
*   **`production_logs`**: Tracks successfully generated videos. Once a video is rendered successfully, a row is inserted here with `status='SUCCESS'` so it is not processed again.

---

## 2. The Core Pipeline (`scripts/pipeline_runner.py`)

The `pipeline_runner.py` is the orchestrator. When executed (`python3 scripts/pipeline_runner.py`), it performs the following steps:

### Step A: Topic Selection
*   Calls `get_next_topic()` from `scripts/topic_catalog.py`.
*   It selects a topic from `topic_catalog` where `used_count = 0` (or lowest) and `pregenerated_json IS NOT NULL`.

### Step B: Script Loading
*   Loads the `pregenerated_json` for the selected topic.
*   The JSON format includes:
    *   `script_hi`: The exact, full Hindi narration script to be spoken.
    *   `slides`: An array of slide objects. Each slide contains a `caption` (the on-screen subtitle), `image_prompt` (English prompt for image generation), and `approx_sec` (rough duration).

### Step C: Image Verification (Cursor Agent Instruction ⚠️)
*   The pipeline checks if all images required for the slides exist in the folder: `reels-factory/public/pregenerated_images/<story_id>/`.
*   **Agent Instruction for Image Generation**: If an image is missing, the pipeline will **HALT** with an error. Since you (Cursor) have the ability to generate images, you must:
    1. Read the `image_prompt` from the JSON for the missing slide.
    2. Generate an image (9:16 aspect ratio).
    3. Save the image to `reels-factory/public/pregenerated_images/<story_id>/slide_<slide_index>.png`.
    4. Do this in bulk for all slides before running the pipeline.

### Step D: Text-to-Speech (TTS) Generation (`scripts/tts_generator.py`)
*   Extracts the `script_hi` and sends it to the local `omnivoice-infer` CLI.
*   The raw audio is saved to `reels-factory/public/narration/<story_id>-raw.wav`.
*   **Post-processing**: `ffmpeg` is used to apply bass boost (~8dB) and peak normalization, saving the final audio to `<story_id>-hi.wav`.
*   **Timestamp Calculation**: The pipeline calculates the exact duration of the final audio file and proportionally distributes this time across all slides (based on their `approx_sec` weights) to give each slide a precise `endSec` timestamp. This ensures the visuals stay perfectly perfectly synced with the voiceover.

### Step E: Remotion Video Rendering
*   The pipeline prepares a JSON properties file (`props_<timestamp>.json`) containing the slides, precise timestamps, and audio paths, saving it to `reels-factory/out/`.
*   It invokes the local Remotion renderer via command line:
    `npx remotion render src/Root.tsx DynamicSlideshow <output_mp4_path> --props=<props_file>`
*   Remotion reads `reels-factory/src/compositions/DynamicSlideshow.tsx` to compose the video.

### Step F: Finalizing & Logging
*   The rendered video is moved to the root `videos/` folder with the naming convention `videos/<story_id>.mp4`.
*   A success record is inserted into `production_logs`.

---

## 3. Video Composition (`DynamicSlideshow.tsx`)

The video is assembled using React Remotion, and consists of three main sequences:

1.  **Intro Sequence (`PremiumIntro.tsx`)**: 
    *   Plays for the first `introFrames` (e.g., 4 seconds / 120 frames).
    *   Uses an astrology-themed background (like a Navagraha/Mandala image) and the AstroAvatar logo perfectly centered. No text captions are used in the intro.
2.  **Story Body (`SlideshowBody`)**:
    *   Plays the generated TTS audio (`<story_id>-hi.wav`).
    *   Cycles through the generated slide images.
    *   Applies a Ken Burns effect (slow zooming/panning) to the images.
    *   Displays the `caption` (subtitle) text from the JSON over the image.
    *   A permanent AstroAvatar watermark is displayed in the top right.
3.  **Outro Sequence (End Card)**:
    *   Plays for exactly 5 seconds (`endCardFrames` = 150).
    *   Uses a pre-existing `end_card.mp4` video.
    *   *Note: `end_card.mp4` is actually a 10-second video that was manually fast-forwarded to 5 seconds using `ffmpeg`, so Remotion just plays the physical file normally.*

---

## 4. How to Generate Scripts for Future Videos (Agent Instruction ⚠️)

To generate the scripts and assets for the remaining 60+ videos in the database, the agent should follow this exact format.

1. **Pick a topic** from `topic_catalog` that lacks a `pregenerated_json`.
2. **Generate the JSON**. You must output a JSON object matching this exact schema:

```json
{
  "story_id": "unique_topic_id",
  "title": "Hindi Title",
  "category": "Astrology / Myth Category",
  "script_hi": "The complete, detailed Hindi narration text. This is what the voiceover will speak word-for-word.",
  "estimated_speech_sec": 75.0,
  "part_info": { "current_part": 1, "total_parts": 1 },
  "slides": [
    {
      "slide_index": 1,
      "caption": "Short, punchy Hindi subtitle summarizing this part of the script.",
      "image_prompt": "Highly detailed, descriptive english prompt for image generation (9:16 aspect ratio).",
      "approx_sec": 5.0
    }
  ]
}
```

3. **Important Rules for Script Generation**:
   *   The `script_hi` is the single source of truth for the voiceover. It should be continuous and detailed.
   *   The `caption` for each slide should be a condensed, easy-to-read on-screen subtitle that roughly aligns with what is being spoken in the `script_hi` during that slide's duration.
   *   Save this JSON directly into the `pregenerated_json` column for that topic's row in `topic_catalog`.

4. **Generate the Images**: After saving the JSON, use your image generation capabilities to process every `image_prompt` in the JSON, and save the 9:16 images to `reels-factory/public/pregenerated_images/<story_id>/slide_<index>.png`.

Once the JSON is in the database and the images are in the folder, simply run `python3 scripts/pipeline_runner.py` to produce the final video!
