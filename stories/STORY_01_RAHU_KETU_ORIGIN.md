# Story 01 — How Rahu & Ketu Were Born (existing Purana narrative)

**Status:** Shipped trial Reel — see `CONTENT_RULES.md` (final length **60–90s**)  
**Script style:** narrative-first bolchal Hindi (~80% story / ~20% curiosity; max 1–2 wonder beats)  
**Goal:** Teach / make people aware of Hindu astrology via visual Reels  
**Rule:** Existing story only — no invented plot  
**Approved output:** `reels-factory/out/rahu-ketu-origin.mp4`  
**Canonical rules:** always follow `CONTENT_RULES.md` over older timing notes below.  
**Primary sources (public retellings of Purana tradition):**
- [Samudra Manthana — Wikipedia](https://en.wikipedia.org/wiki/Samudra_Manthana) (Vishnu Purana / related Puranic tradition)
- [Times of India — Story of Rahu and Ketu](https://timesofindia.indiatimes.com/astrology/others/story-of-rahu-and-ketu/articleshow/111650701.cms)
- Common Bhagavata / Vishnu Purana retellings of Svarbhanu → Rahu + Ketu and eclipses

**Tone:** Reverent mythic cinema · educational · not horror · not gore  
**End card:** Use provided `end_card.mp4` (720×1280, ~10s) — do **not** invent another CTA card. Upscale/fit to 1080×1920 in Remotion.

---

## 1. Why this story (recommendation)

| Option | Verdict |
|---|---|
| **Rahu–Ketu origin (Samudra Manthan climax)** | **Best first pick** — uses 4 grahas we already have (Surya, Chandra, Rahu, Ketu), explains eclipses + why shadow planets matter in Jyotish |
| Chandra + 27 Nakshatras / Daksha curse | Good later episode (Moon phases) |
| Shani + Ganesha (Brahma Vaivarta variant) | Sensitive (beheading); different versions conflict; skip for v1 |
| Full Samudra Manthan start-to-end | Too long for one Reel; split later |

**Recommended format:** one **60–90s** hero Reel (welcome + story + 5s end card), then optional multi-part series if a myth is too long.

---

## 2. Canonical beats we will use (existing only)

1. After the Ocean of Milk is churned, **amrita** (nectar of immortality) appears.  
2. **Vishnu as Mohini** distributes amrita to the Devas.  
3. Asura **Svarbhanu** disguises himself as a Deva and drinks amrita.  
4. **Surya** and **Chandra** notice and alert Mohini / Vishnu.  
5. Vishnu’s **Sudarshana Chakra** severs Svarbhanu’s head (tasteful, non-gore staging).  
6. Because nectar was already drunk: head → **Rahu**, body → **Ketu** (immortal shadow grahas).  
7. In revenge, Rahu pursues Sun/Moon → **eclipses** (grahana); light returns because he is only a head.  
8. Teaching close: this is why Jyotish treats Rahu/Ketu as powerful *chhaya grahas* (shadow planets), not “empty superstition.”

---

## 3. Visual plan

### A) Single 60–90s Reel (current ship target — timings below are legacy beat notes)

| Time | Visual (Remotion) | On-screen text (silent autoplay) |
|---|---|---|
| 0–3s | Cosmic ocean + faint amrita pot; Mohini appears with kalash | “Amrita was born…” |
| 3–8s | Deva row soft silhouettes; Svarbhanu slides into line (smoke disguise) | “But one Asura hid among the Devas” |
| 8–14s | Surya + Chandra cutouts light up, point/alert; Mohini turns | “Surya & Chandra saw the truth” |
| 14–20s | Tasteful chakra flash / light arc (NO gore); Svarbhanu splits into Rahu + Ketu sprites | “Head became Rahu · Body became Ketu” |
| 20–26s | Rahu arcs toward glowing Sun/Moon → brief darken (eclipse) → light returns | “That’s why eclipses happen” |
| 26–30s | Title card beat: “Rahu & Ketu — the shadow grahas of Jyotish” | Soft hold |
| +10s | **Your** `end_card.mp4` appended | — |

Motion language (not Ken Burns-only):
- Character **enter / slide / orbit** on stage
- Disguise = smoke veil opacity
- Alert = Surya/Chandra aura pulse + move toward Mohini
- Split = crossfade/morph Svarbhanu → Rahu + Ketu with light ring
- Eclipse = vignette + Rahu path over Surya/Chandra

### B) Optional 3-part series (same myth, more education)

1. **Part 1 — The nectar** (Mohini, amrita, disguise) ~20–25s  
2. **Part 2 — The split** (Surya/Chandra expose → Rahu & Ketu born) ~20–25s  
3. **Part 3 — The eclipse lesson** (chase, grahana, what Jyotish means by shadow planets) ~20–25s + end card on part 3 only  

---

## 4. Characters & assets

### Already have (`reels-assets/graha-characters/`)
- Surya, Chandra, Rahu, Ketu (+ full Navagraha cast for later)

### Newly generated (`reels-assets/supporting-characters/`)
| Folder | Role |
|---|---|
| `mohini/` | Vishnu as Mohini distributing amrita |
| `svarbhanu/` | Asura before the split |

Each has: `hero_portrait.png`, `hero_square.png`, `transparent_cutout.png`

### Optional later (not blocking v1)
- Amrita kalash prop PNG  
- Sudarshana chakra glow (can be pure Remotion SVG/particles)  
- Crowd Deva silhouettes (generic, faceless)

### Sensitivity rules
- No blood, no severed-neck gore  
- Split = sacred light / silhouette transition  
- Mohini: reverent, not sexualized (already prompted that way)

---

## 5. Narration scripts (for your TTS)

Speak calmly, mythic, educational. Hinglish recommended for Reels reach.  
Leave ~0.3s breaths at `|`. Target ~30s for Script A.

### Script A — Single 30s Reel (Hinglish)

```text
Samudra Manthan ke baad, amrita nikla — amrit, immortality ka nectar. |
Mohini roop mein Vishnu Devas ko yeh amrita baant rahe the. |
Par asura Svarbhanu ne Deva bankar chupke se amrita pee liya. |
Surya aur Chandra ne uska bhesh pehchan liya, aur satya khol diya. |
Vishnu ke Sudarshan Chakra ne uska sir alag kiya — |
par amrita peene ke baad woh amar reh gaya. |
Sir bana Rahu, shareer bana Ketu — do chhaya graha. |
Isi karan Rahu Surya-Chandra ka peecha karta hai — |
aur jab pakadta hai, grahan hota hai. |
Yahi hai Hindu jyotish mein Rahu-Ketu ki kahani.
```

**Approx timing cues for Remotion markers**

| Cue | Line start |
|---|---|
| 0.0s | Samudra Manthan… |
| 3.5s | Mohini roop… |
| 8.0s | Par asura Svarbhanu… |
| 12.5s | Surya aur Chandra… |
| 17.0s | Vishnu ke Sudarshan… |
| 21.0s | Sir bana Rahu… |
| 25.0s | Isi karan Rahu… |
| 28.5s | Yahi hai Hindu jyotish… |

### Script A — English alt (if you prefer EN TTS)

```text
After the churning of the ocean, amrita appeared — the nectar of immortality. |
As Mohini, Vishnu began giving it to the Devas. |
But the asura Svarbhanu disguised himself and drank it. |
Surya and Chandra saw through the disguise and revealed the truth. |
Vishnu’s Sudarshana Chakra severed his head — |
yet because he had tasted amrita, he could not die. |
The head became Rahu. The body became Ketu — the shadow grahas. |
That is why Rahu chases the Sun and the Moon — |
and when he catches them, an eclipse is born. |
This is the story behind Rahu and Ketu in Hindu astrology.
```

### Script B — Series Part 1 (nectar / disguise) ~22s

```text
Devatas aur asuras ne ksheer sagar matha — Samudra Manthan. |
Ant mein amrita nikla. |
Mohini roop mein Vishnu ne kaha — pehle Devas ko amrita milega. |
Par ek asura, Svarbhanu, Deva ban kar pankti mein baith gaya. |
Woh sochta tha — koi nahi pehchanega.
```

### Script B — Series Part 2 (expose / split) ~22s

```text
Surya aur Chandra — surya aur chandrama — chamakte hain. |
Unhone Svarbhanu ka bhesh turant dekh liya. |
Unhone Mohini ko suchit kiya. |
Sudarshan Chakra chala — sir alag, shareer alag. |
Par amrita peene ke baad dono amar reh gaye. |
Sir — Rahu. Shareer — Ketu.
```

### Script B — Series Part 3 (eclipse / Jyotish lesson) ~22s + end card

```text
Rahu aur Ketu ab chhaya graha ban gaye. |
Surya-Chandra ne unhe pakda tha — isliye Rahu unka peecha karta hai. |
Jab Rahu unhe grahan karta hai, surya grahan ya chandra grahan hota hai. |
Par kyunki Rahu sir hai, prakash wapas aa jata hai. |
Isi liye jyotish mein Rahu-Ketu ko balwan mana jata hai — |
woh dikhte nahi, par jeevan ke chalte-phirte chhaya zaroor chhodte hain.
```

---

## 6. Remotion build checklist (next implementation step)

- [ ] New composition `RahuKetuOrigin` (1080×1920)
- [ ] Wire sprites: Mohini, Svarbhanu, Surya, Chandra, Rahu, Ketu
- [ ] Beat markers synced to TTS audio once you drop `narration.mp3/wav`
- [ ] Big captions for mute viewing
- [ ] Append `public/end_card.mp4` (already copied) via `<OffthreadVideo>` / `<Video>` — scale 720×1280 → cover 1080×1920
- [ ] No duplicate end-card design from us
- [ ] Export sample MP4 for review

---

## 7. Doable? Did you miss anything?

**Doable: yes.**

You already covered the big pieces (existing myth, visuals, TTS script, your end card). Useful extras:

1. **Mute-first captions** — most Reels watch without sound; narrate *and* put short Hindi/Hinglish lines on screen.  
2. **Language lock** — pick Hinglish vs Hindi vs English before TTS voice casting.  
3. **Bed music** — soft temple/cosmic bed under TTS (−18 to −24 dB).  
4. **TTS delivery notes** — calm, slow (~140 wpm), pause at `|`; avoid shouty “myth trailer” energy.  
5. **End card format** — yours is **720×1280 @ 10s**; master Reel is **1080×1920** → we letterbox/cover-scale (confirm preference).  
6. **On-screen disclaimer** (1 line, optional): “As told in the Puranic tradition.”  
7. **Sensitivity QA** — no gore on the chakra beat (brand + platform safety).  
8. **Audio handoff** — you deliver `narration.wav` + optional music; we place markers + ducking.  
9. **Series vs one-shot** — decide before we build (recommend one 30s proof first).

---

## 8. Ask before we build video

Reply with:
1. **Format:** single 30s **or** 3-part series first?  
2. **Language for TTS:** Hinglish / Hindi / English?  
3. **End card fit:** cover-crop to fill 9:16, or centered with cosmic bars?
