# Phase 2 status

**Doable?** Yes — with sprite staging, not photoreal acting.

## Proof

- Studio: `cd reels-factory && npm run dev`
- Renders:
  - `reels-factory/out/graha-meeting.mp4` — chart/sprite demo
  - `reels-factory/out/daily-dose-intro.mp4` — locked welcome
  - `reels-factory/out/rahu-ketu-origin.mp4` — full episode (~61s)
- Compositions: `GrahaMeeting`, `DailyDoseIntro`, `RahuKetuOrigin`

## Rules

Source of truth: repo root `CONTENT_RULES.md`  
- Final Reel length **60–90s**  
- Voice: instruct `male, middle-aged, indian accent, moderate pitch` (no ref clone)  
- Structure: welcome + story + 5s `end_card.mp4`

## Model

JSON-shaped props drive host / house / visitors. Locale packs swap captions + TTS only.

## Limits (accepted)

- Low-level motion (paths, bob, aura, meeting flash) — not lip-sync
- Chart layout is approximate North-Indian visual, not ephemeris-accurate yet
