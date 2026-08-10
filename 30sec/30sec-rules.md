# 30-Second Video Format Rules & Guidelines

This document explains the standard process for generating 30-second short-form reels for daily astrology topics (such as Mangal Dosh, Sade Sati, Rahu/Ketu placements, etc.).

---

## 1. Overview & Objective
- **Target Duration:** 20 to 30 seconds.
- **Aspect Ratio:** 9:16 Vertical (1080x1920).
- **Core Concept:** Highlight a specific astrological topic or planet placement using an interactive, animated Kundli chart.

---

## 2. Visual Structure (`DynamicKundli`)
1. **Background:** Dark cosmic/astrological backdrop with subtle ambient lighting.
2. **Kundli Chart:**
   - Centered square diamond Kundli chart.
   - Houses are numbered 1 through 12.
   - Target houses are highlighted in red/gold when discussed in the narration.
3. **Planet Avatar Animation:**
   - Circular planet god avatar (e.g. `graha/mangal/portrait.png`).
   - Uses spring physics (`remotion` spring API) to animate smoothly between house centers.
4. **Subtitles:**
   - Large, centered text at the bottom.
   - Synced with narration timestamps for high retention.

---

## 3. Audio & Voiceover
- **TTS Generator:** Sarvam AI or macOS system TTS (`say`).
- **Pacing:** Fast-paced, engaging hook in the first 3 seconds.
- **CTA:** End with a strong Call-To-Action (e.g. *"Comment 'MANGAL' to find out your placement!"*).

---

## 4. Technical Setup & Rendering
> **Note:** The `reels-factory` directory is the **Remotion React project**. It contains all the React components, styles, dependencies (`node_modules`), and rendering tools required to build the `.mp4` file.

### How to Render:
1. Navigate to the project folder:
   ```bash
   cd 30sec/reels-factory
   ```
2. Start local studio preview (optional):
   ```bash
   npm run dev
   ```
3. Render the final MP4 video:
   ```bash
   npm run render:mangal
   ```
4. Output files are saved in `30sec/videos/`.

---

## 5. Folder Structure
- **`reels-factory/`**: Remotion React application containing components (`DynamicKundli.tsx`, `KundliChart.tsx`, etc.).
- **`scripts/`**: Helper scripts for TTS generation and catalog topics.
- **`videos/`**: Holds final rendered `.mp4` files and social media posting descriptions (`facebook-post.md`).
- **`30sec-rules.md`**: Standard guidelines for creating 30-second reels.
