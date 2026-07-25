# Graha Characters — Phase 1 Style Lock

**Status:** Phase 1 complete (trial assets)  
**Product:** AstroAvatar Reels acquisition engine  
**Date:** 2026-07-25  

## Purpose

Consistent human-form divine character set for the 9 Vedic grahas, ready for Remotion Ken Burns + caption + end-card tests (Phase 2). Not a full animation pipeline yet.

## Style lock decision

Locked after Shani / Mangal / Guru style tests in `_style-lock/`.

**Master style block (reuse exactly):**

```text
Cinematic Indian mythological divine character portrait, reverent sacred tone,
high-end mythic film key art, detailed traditional attire and jewelry,
soft volumetric light, temple-cosmic atmosphere, highly readable silhouette,
vertical mobile composition, consistent painted-cinematic style across series,
no photoreal celebrity face, no horror, no gore, no modern clothing, no watermark, no text
```

**Series conventions:**
- Vertical 1024×1536 hero portraits (9:16-friendly)
- Centered figure on stone/platform or cosmic ground
- Temple silhouettes + nebula/cosmos backgrounds
- Strong silhouette, readable on phone
- Headroom for future captions in upper/lower thirds
- Reverent mythic cinema tone (not cartoon, not horror, not meme)

Reference style-lock images: `_style-lock/stylelock_shani_v1.png`, `stylelock_mangal_v1.png`, `stylelock_guru_v1.png`.

## Folder layout

```
graha-characters/
  README.md
  _style-lock/          # style-lock tests (keep)
  surya|chandra|mangal|budha|guru|shukra|shani|rahu|ketu/
    hero_portrait.png       # 1024×1536 full scene
    hero_square.png         # 1080×1080 center crop
    transparent_cutout.png  # RGBA subject isolation (rembg)
    prompt.txt
    style_notes.md
```

## Per-graha identity (quick glance)

| Folder | Graha | Palette / cues |
|---|---|---|
| `surya/` | Sun | Gold/red, solar aura, lotus/chariot cues |
| `chandra/` | Moon | Silver/blue, crescent, water/mist |
| `mangal/` | Mars | Red/orange, spear, warrior armor |
| `budha/` | Mercury | Green/emerald, book/scroll |
| `guru/` | Jupiter | Yellow/gold, scripture, blessing mudra |
| `shukra/` | Venus | White/pastel/silver, lotus, grace |
| `shani/` | Saturn | Dark blue/black, staff, crow (tasteful) |
| `rahu/` | N. node | Smoke/violet, intense, serpent ornament |
| `ketu/` | S. node | Ash/smoke, mystical, serpent/moksha cues |

## Generation method used

1. Cursor `GenerateImage` with locked master style + graha identity lines
2. Reference images (`reference_image_paths`) from style-lock set for consistency
3. Square crops via ImageMagick center-extent → 1080×1080
4. Transparent cutouts via `rembg` (Python API) from hero portraits

## Failed / rejected attempts

- None discarded after lock; first Shani/Mangal/Guru trio accepted as the series look.
- CLI `rembg i` failed (`ModuleNotFoundError: filetype`); fixed via `pip install filetype` + Python `rembg.remove`.

## Known gaps

- **No layered puppet parts** yet (`body.png`, `head.png`, arms, aura, prop) — Phase 1 preferred extras skipped to prioritize series consistency.
- **No expression variants** (`neutral_blessing` / `intense_warning`) yet.
- Cutouts are automatic rembg masks — may leave faint halo/edge artifacts; refine before heavy compositing if needed.
- Ketu depiction leans serpent-form / mystical (valid myth cue); confirm brand comfort before heavy use.
- Assets live in this Remotion trial repo under `reels-assets/`; mobile app repo is context only. Remotion project not scaffolded yet (Phase 2).

## Phase 2 recommendation

**First Remotion test character: Shani** (`shani/hero_portrait.png` + `transparent_cutout.png`).

Why: strongest silhouette, high emotional weight for myth-truth hooks, dark cosmic BG works with glow/aura overlays, style-lock anchor.

Suggested first template: `GodTalk` — appear + aura → Hindi/Hinglish captions → AstroAvatar end card (1080×1920).

## Reproducibility

Each graha folder has `prompt.txt` (exact prompts) and `style_notes.md` (what to keep consistent). Always append the master style block above when regenerating.
