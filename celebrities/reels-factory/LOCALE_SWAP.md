# Locale swap (Hindi → Tamil / Telugu later)

**Yes — visuals stay fixed. Only TTS + subtitles change.**

## How

1. Copy `src/stories/rahuKetu/locale.hi.ts` → `locale.ta.ts` (or `te`)
2. Translate `captions[].text` only (keep `fromFrame` / `durationInFrames` same)
3. Drop TTS audio at `public/narration/rahu-ketu-ta.mp3`
4. Set `narrationFile: "narration/rahu-ketu-ta.mp3"`
5. In Studio / render props, pass `{ locale: rahuKetuLocaleTa }`  
   or temporarily change `rahuKetuDefaults.locale`

No need to re-animate characters or rebuild the composition.

## Hindi (current)

- Captions + script: `src/stories/rahuKetu/locale.hi.ts`
- TTS text for you: `../stories/tts/rahu-ketu-hi.txt`
- After you generate speech, put file at `public/narration/rahu-ketu-hi.mp3` and uncomment `narrationFile` in the locale pack.
