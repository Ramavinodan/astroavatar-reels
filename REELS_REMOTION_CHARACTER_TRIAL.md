# Remotion Reels Trial — Planet Character Generation Handover

**Status:** Trial / spike (not full production pipeline yet)  
**Owner product:** AstroAvatar mobile app  
**Related repos:**
- Mobile app: `/Users/rama.m/workspace/personal2/AstroAvatarMobileApp`
- WhatsApp bot (separate surface): `/Users/rama.m/workspace/personal2/AstroAvatarWhatsapp`

**Document purpose:** Hand this to another agent to execute **Phase 1 only** — generate human-form Hindu mythological characters for the 9 Vedic planets (grahas), so we can later test Remotion animation/compositing for Instagram + Facebook Reels.

---

## 1. What we are trying to achieve

### Business goal
- Grow the **mobile app** to **~10k installs in 30 days** (broader growth plan; this trial is one content engine under that).
- Acquire users via **Instagram Reels + Facebook Reels** (daily content), boost winners, drive installs via bio/OneLink/app CTA.
- Founder will **not show their face** and is **not a video editor**.

### Content strategy goal
- Post **1 Reel per day**.
- Style inspired by the current wave of **Hindu mythology / dharmic cinema** that feels emotional, divine, and mass-relatable (not dry “planet diagram” astrology content).
- Even though astronomically planets are spheres, in **Hindu astrology/mythology grahas are deities** with personality, stories, and human-relatable form.
- Showing grahas in **human/divine form** increases emotional attachment and shareability vs abstract orbs.

### Technical trial goal (THIS document’s scope)
- Trial whether **Remotion** can be our no-face Reel engine.
- **First milestone only:** generate a consistent **character set for each planet**.
- Do **not** build the full daily render pipeline yet until characters exist and look on-brand.

---

## 2. Product context (for the receiving agent)

### Mobile app (primary growth surface)
Flutter app with habitual features:
- Daily guidance
- Panchang / dasha
- AI guru chat + wallet
- VedTV / GyanTV-style video
- Social Status (WhatsApp Status sharing)
- Reports / kundli / match
- Referrals

Backend (prod, from deployment docs):
- `https://astroavatar-mobile-backend-prod.pixenlabs.workers.dev`

App package:
- `com.pixenlabs.astroavatar`

### WhatsApp bot (secondary)
Transactional astrology PDF reports. Weak repeat usage. **Not the primary destination for this Reels trial.** Reels should push the **app**, not the bot.

### Important prior decision
Growth effort (Reels, creators, boosts) should point at the **app**. Remotion content is an acquisition/brand engine for the app.

---

## 3. Why Remotion (and what it can / cannot do)

### Why Remotion
- React/TS programmatic video — fits our engineering skills
- No face-on-camera required
- Repeatable templates for daily posting
- Good for captions, end cards, brand motion, compositing

### Critical constraint (tell the agent clearly)
**Remotion does not magically animate a single flat AI image into a living actor.**

With one still image, Remotion can:
- Zoom / pan (Ken Burns)
- Fade / scale / glow / particles / aura
- Overlay Hindi/English captions
- Add app end card

With one still image, Remotion **cannot** by itself:
- Natural walk cycles
- Independent hand/eye acting
- True lip-sync character performance

### Implication for character generation
Characters must be generated in a way that supports **later animation**, not just pretty posters:
1. **Minimum for trial:** consistent full-body (or 3/4) stills per graha — good enough for Ken Burns + aura Reels.
2. **Preferred for trial:** also produce **layered exports** where possible (body / head / arms / aura / prop) so Remotion can do simple puppet motion later.
3. Optional later phase: AI video clips or Rive rigs — **out of scope for Phase 1**.

---

## 4. Phase 1 scope (DO THIS NOW)

### In scope
Generate **character art for each of the 9 grahas**:

| Graha | Common name | Personality / visual cues (use as art direction) |
|---|---|---|
| Surya | Sun | Royal, radiant, authoritative; gold/red; lotus / chariot cues |
| Chandra | Moon | Calm, emotional, luminous; silver/white/blue; water / crescent cues |
| Mangal | Mars | Warrior energy; red/orange; spear / armor cues |
| Budha | Mercury | Youthful, clever, communicative; green; book/scroll cues |
| Guru (Brihaspati) | Jupiter | Wise, benevolent teacher; yellow/gold; scripture / blessing mudra |
| Shukra | Venus | Grace, beauty, arts, love; white/pastel/silver; lotus / aesthetic richness |
| Shani | Saturn | Austere, just, disciplined; dark blue/black; staff; crow/vulture symbolism (tasteful) |
| Rahu | North node | Intense, smoky, ambitious, shadow; unconventional; serpent/smoke cues (not horror-gore) |
| Ketu | South node | Detached, mystical, moksha-leaning; ash/smoke/spiritual; serpent/flag cues (reverent) |

### Deliverables expected from Phase 1
Create a folder in **this Remotion trial repo (CWD)** only — mobile app / WhatsApp repos are context, not asset homes:

```
reels-assets/graha-characters/
  README.md                 # style lock + usage notes
  surya/
  chandra/
  mangal/
  budha/
  guru/
  shukra/
  shani/
  rahu/
  ketu/
```

For **each** graha, produce at least:

1. `hero_portrait.png` — vertical 1080×1920-friendly composition (or 1024×1536+), deity clearly readable on phone
2. `hero_square.png` — 1:1 crop/variant for experiments
3. `transparent_cutout.png` — subject on transparent background (for Remotion layering)
4. `prompt.txt` — exact prompt(s) used
5. `style_notes.md` — what to keep consistent

**Preferred extras (if feasible in same pass):**
- Layered PSDs or separate PNGs: `body.png`, `head.png`, `arm_left.png`, `arm_right.png`, `aura.png`, `prop.png`
- 2 expression variants: `neutral_blessing.png`, `intense_warning.png` (useful for myth “truth” hooks)

### Out of scope for Phase 1
- Remotion project setup
- Daily JSON → MP4 pipeline
- Voiceover / lip sync
- Full walk-cycle animation
- Posting automation to IG/FB
- WhatsApp bot integration
- Final ad boosting

---

## 5. Art / brand style guide (must follow)

### Tone
- **Reverent mythic cinema**, not comic meme, not horror, not cheap cartoon
- Emotionally warm, divine, India-native
- Inspired by the *feeling* of modern Hindu mythological films (devotion, destiny, moral clarity) — **not** copying any specific film’s copyrighted character designs

### Visual rules
- Consistent art style across all 9 (same lighting model, anatomy style, line/paint treatment)
- Readable at Reel size: strong silhouette, not ultra-busy detail
- Vertical-friendly framing (headroom for captions in upper/lower thirds)
- Dark cosmic / temple atmosphere backgrounds OK, but cutout version must isolate the figure
- Include subtle graha identity props/colors so viewers instantly know who it is
- **No real celebrity likeness**
- **No offensive / sexualized deity depiction**
- Prefer blessing mudra / calm authority over aggression (Mangal/Shani can be stern, not violent-gore)

### Language / caption context (for later; don’t generate final Reels yet)
Reels will be Hindi or Hinglish, 12–20 seconds, structure roughly:
1. God appears
2. Hook (fear/hope/myth)
3. 2–3 truths
4. Soft remedy / insight
5. App CTA: AstroAvatar — free kundli / daily guidance

Phase 1 only needs characters that can carry that tone visually.

---

## 6. Suggested generation method for the agent

Use whatever image model/tool is available (e.g. Cursor GenerateImage, external image models, etc.), but enforce consistency:

1. Lock a **master style prompt** first (generate 2–3 Surya/Shani tests, pick one style).
2. Reuse the same style block for all 9.
3. Generate, then crop/export cutouts.
4. If consistency breaks, regenerate with reference-image workflow if the tool supports it.
5. Store prompts so another agent can reproduce.

### Example master style block (adapt freely, keep locked once chosen)

```text
Cinematic Indian mythological divine character portrait, reverent sacred tone,
high-end mythic film key art, detailed traditional attire and jewelry,
soft volumetric light, temple-cosmic atmosphere, highly readable silhouette,
vertical mobile composition, consistent painted-cinematic style across series,
no photoreal celebrity face, no horror, no gore, no modern clothing, no watermark, no text
```

Then append graha-specific identity lines (color, prop, mood).

---

## 7. Success criteria for this trial phase

Phase 1 is successful if:

1. All **9 grahas** have usable hero + transparent cutout assets.
2. They look like **one family/series** (same style).
3. Each is recognizable as that graha within 1 second on a phone.
4. Assets are clean enough to drop into Remotion for a Ken Burns + caption test in Phase 2.
5. Folder structure + prompts are documented so work is reproducible.

**Nice-to-have success:** layered parts for at least Shani, Mangal, Guru, Chandra (highest-use emotional set).

---

## 8. Phase 2 — chart simulation (in progress / scaffolded)

Implemented under `reels-factory/` (not Ken Burns-only):

1. Remotion project scaffolded: `reels-factory/`
2. First template: **`GrahaMeeting`** (chart-stage simulation)
   - Host graha appears in a bhava
   - Visitor grahas fly on arcs into that house and meet
   - Captions + app CTA end card
3. Sample MP4: `reels-factory/out/graha-meeting.mp4` (1080×1920) — Shani + Mangal meet in Guru’s house
4. Next: tighten chart geometry, more scene types, then daily JSON automation

### Remotion capability reminder for Phase 2
- Cutout sprites on a kundli stage → **graha meetings / house placements** = yes
- Feed AI images → aura / bob / path motion / captions = yes
- Expect full human acting or high-quality lip-sync from one PNG = no
- Better character acting later via layers / Rive / short AI video inserts

---

## 9. Broader growth context (why this matters)

### Target channels
- Instagram Reels
- Facebook Reels
- Boost only posts that already show organic traction
- CTA → app install (not face-led personal brand)

### Content operating model (post-trial)
- 1 video/day
- No traditional editing workflow
- Template-driven generation
- Formats later: myth vs truth, rashi tag-bait, remedy, app demo

### Why characters first
Without a locked divine cast, Remotion templates will look generic. Characters are the brand moat for this content line.

---

## 10. Instructions to the receiving agent

Please:
1. Read this full document.
2. Execute **Phase 1 only** (character generation + asset packaging + prompts).
3. Prefer quality/consistency over quantity of pose variants.
4. Start style lock with **Shani + Mangal + Guru** if iterating, then complete all 9.
5. Write a short `reels-assets/graha-characters/README.md` summarizing style lock decisions and any failed attempts. Keep all generated assets under this Remotion CWD only.
6. Do **not** start Remotion scaffolding unless Phase 1 deliverables are done and clearly organized.
7. Ask before spending on paid APIs if not already available in the environment.

### Done definition
Comment/PR-style summary listing:
- paths to all 9 character folders
- which files exist per graha
- style prompt used
- known gaps (e.g. layering not done)
- recommendation for Phase 2 first Remotion test character (likely Shani)

---

## 11. Quick reference — project names / branding

- Product name for all Reels / CTA / watermark copy: **AstroAvatar** only
- Do not use AskMyGuru, AskAstro, or other legacy names in new content
- Social growth feature already exists in app: **Social Status** (WhatsApp Status sharing). Reels are a separate top-of-funnel engine; they can later complement Status virality.

---

## 12. One-line mission for Phase 1

**Create a consistent, reverent, human-form divine character set for the 9 Vedic grahas so we can trial Remotion-based no-face mythology-style Reels that drive mobile app installs.**
