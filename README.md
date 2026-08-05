# AstroAvatar Reels Factory

No-face Instagram/Facebook Reels for **AstroAvatar** — Vedic mythology + jyotish education, built with Remotion + OmniVoice.

## Source of truth

Read **[`CONTENT_RULES.md`](./CONTENT_RULES.md)** before writing scripts, generating TTS, or rendering.

## Quick start

```bash
cd reels-factory
npm install
npm run dev          # Remotion Studio
npm run render:rahu-ketu
```

## Layout

| Path | What |
|---|---|
| `CONTENT_RULES.md` | Agent/human production bible |
| `30sec/` | **Phase 1 Pipeline:** 15-30s Reels for new audience acquisition |
| `90sec/` | **Phase 2 Pipeline:** 60-90s Reels for established audience depth |
| `[30sec|90sec]/reels-factory/` | Remotion project |
| `[30sec|90sec]/scripts/` | Python orchestration, generation, DB |
| `[30sec|90sec]/sql/` | Database and queries |
| `[30sec|90sec]/videos/` | Output MP4s |

## Current approved cut

`reels-factory/out/rahu-ketu-origin.mp4` — welcome + Rahu–Ketu origin story + end card (~61s).
