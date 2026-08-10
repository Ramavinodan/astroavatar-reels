# Celebrity Video Generation Rules

This document outlines the standard operating procedure for generating astrology profile videos for celebrities. Follow these rules to maintain consistency across the series.

## 1. Information Gathering
- Ensure there is a Markdown file (e.g., `celebrities/{name}/{name}_details.md`) detailing the celebrity's astrological chart, major life phases, and key Yogas.
- **Key details needed:** Ascendant sign/house, prominent planetary placements (e.g., Dhana Yoga, Neechabhanga Raja Yoga), and Dasha timelines mapping to their real-life achievements.

## 2. Scripting
- Write a 30 to 45-second narration script (roughly 60–80 words).
- **Structure:**
  - **Hook:** Start with a punchy question referencing their biggest real-world achievement (e.g., "How did a bus driver's son become a Pan-India star?").
  - **Ascendant:** Mention the Lagna (Ascendant) and its ruling planet, connecting it to their personality or screen presence.
  - **Yogas (Crucial):** Explicitly name and explain their major Yogas (e.g., Dhana Yoga for wealth, Neechabhanga for overcoming humble beginnings).
  - **Dasha Timeline:** Tie their career milestones to their major planetary Dasha periods.

## 3. Audio Generation (TTS)
- Generate a TTS voiceover matching the script.
- **Command:** Use macOS `say` or a premium TTS API.
  - Example: `say -v "Rishi" -o public/audio/{name}-narration.aiff "Script here..." && ffmpeg -i public/audio/{name}-narration.aiff public/audio/{name}-narration.wav`
- Ensure the final audio is in `.wav` format and placed in `public/audio/`.
- Measure the exact duration of the audio to calculate the Remotion composition frames (`Duration in Seconds * 30 FPS = Total Frames`).

## 4. Visual Format (DynamicKundli)
- **Do NOT generate AI images.** Use the exact format from the 30-second `DynamicKundli` video template.
- The format must center around the `KundliChart` component and display the 12 houses.
- **Animations & Highlights:**
  - Map the narration timing (in frames) to specific houses.
  - When the script mentions a specific house or Yoga, highlight that exact house using the `activeHouses` array prop.
  - Animate the corresponding planetary avatar (e.g., `graha/guru/portrait.png` for Jupiter) moving to that highlighted house.
- **Subtitles:**
  - Include large, glowing, centered text below the Kundli chart that syncs with the narration.

## 5. Rendering & Output
- Register the new composition in `src/Root.tsx`.
- Add a render script in `package.json` (e.g., `"render:{name}": "remotion render {Name}Kundli out/{name}-profile.mp4"`).
- Run the render command.
- **Final Step:** Always copy the final `.mp4` file from the `out/` directory to the celebrity's specific folder in the `celebrities/` directory.
