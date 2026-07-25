# reels-factory

Remotion trial for AstroAvatar Reels.

## What this proves

Not Ken Burns-only. Composition **`GrahaMeeting`** stages graha cutouts on a North-Indian-style chart:

1. Host graha appears in a bhava (house)
2. Visitor grahas **fly on arcs** from other houses into that bhava
3. Meeting flash + captions + app CTA end card

This is low-level sprite simulation (idle bob, aura, path motion) — enough to tell “two planets meet in another’s house.” Not lip-sync / full acting.

## Run

```bash
npm run dev                 # Remotion Studio
npm run render:meeting      # → out/graha-meeting.mp4 (1080×1920)
```

## Scene props (future JSON)

See `src/graha/types.ts` → `GrahaMeetingProps`:

- `host` — graha who “owns” / occupies the house mood
- `house` — bhava 1–12
- `visitors` — grahas that travel in and meet
- `visitorOrigins` — optional start houses for fly-in
- `title` / `captions` / `ctaLine`

Default sample: **Shani + Mangal meet in Guru’s house (bhava 7)**.

## Assets

Sprites copied into `public/graha/<id>/cutout.png` from repo root:

`../reels-assets/graha-characters/`

Source of truth for art remains under the remotion CWD `reels-assets/`.
