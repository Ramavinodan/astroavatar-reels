# Narration audio (locale swap)

Drop TTS files here. Visuals never change.

| File | Locale / role |
|---|---|
| `brand/welcome-daily-dose-hi-mixed.wav` | Locked one-time welcome (Hindi) |
| `rahu-ketu-hi.wav` | Hindi story (primary) |
| `rahu-ketu-ta.wav` | Tamil story (later) |
| `rahu-ketu-te.wav` | Telugu story (later) |
| `bgm-soft.wav` | Soft pad under voice |
| `episode_durations.json` | Derived frame counts for Remotion |

Then set `narrationFile` in the matching `locale.*.ts` pack.

**Voice lock + recipe:** see repo root `CONTENT_RULES.md` §6.  
**Scripts:** `stories/tts/welcome-hi.txt` + `stories/tts/<episode>-hi.txt` (story only).
