/**
 * Derived from natural OmniVoice lengths (no duration force).
 * Source: public/narration/episode_durations.json
 * Voice: instruct `male, middle-aged, indian accent, moderate pitch` (no ref clone).
 * Target final Reel: 60–90s.
 */
export const WELCOME_FILE = "narration/brand/welcome-daily-dose-hi-mixed.wav";
export const STORY_FILE = "narration/rahu-ketu-hi.wav";

export const INTRO_FRAMES = 125; // ~3.68s welcome + short hold
export const STORY_FRAMES = 1575; // ~52.5s story — single pass
export const END_CARD_FRAMES = 150; // 5s
export const RAHU_KETU_FPS = 30;
export const RAHU_KETU_DURATION = INTRO_FRAMES + STORY_FRAMES + END_CARD_FRAMES;
