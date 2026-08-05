/**
 * First-mention hero intro windows for Rahu–Ketu story narration (~52.5s).
 * Derived from script + caption blocks in locale.hi.ts (no Whisper).
 * Nudge `startSec` by ±0.3–0.5s if a name lands early/late after listen.
 */
export type CharacterId =
  | "mohini"
  | "svarbhanu"
  | "surya"
  | "chandra"
  | "rahu"
  | "ketu";

export type CharacterIntroBeat = {
  id: CharacterId;
  label: string;
  /** Story-local seconds when hero portrait starts */
  startSec: number;
  /** Hero portrait duration in seconds */
  durationSec: number;
  glow: string;
  portraitFile: string;
  cutoutFile: string;
};

export const CHARACTER_INTROS: CharacterIntroBeat[] = [
  {
    id: "mohini",
    label: "मोहिनी",
    startSec: 13.2,
    durationSec: 3.0,
    glow: "rgba(233,196,106,0.55)",
    portraitFile: "supporting/mohini/portrait.png",
    cutoutFile: "supporting/mohini/cutout.png",
  },
  {
    id: "svarbhanu",
    label: "स्वर्भानु",
    startSec: 22.2,
    durationSec: 3.0,
    glow: "rgba(123,44,191,0.5)",
    portraitFile: "supporting/svarbhanu/portrait.png",
    cutoutFile: "supporting/svarbhanu/cutout.png",
  },
  {
    id: "surya",
    label: "सूर्य",
    startSec: 28.0,
    durationSec: 2.2,
    glow: "rgba(240,180,41,0.6)",
    portraitFile: "graha/surya/portrait.png",
    cutoutFile: "graha/surya/cutout.png",
  },
  {
    id: "chandra",
    label: "चंद्र",
    startSec: 30.5,
    durationSec: 2.2,
    glow: "rgba(180,210,240,0.55)",
    portraitFile: "graha/chandra/portrait.png",
    cutoutFile: "graha/chandra/cutout.png",
  },
  {
    id: "rahu",
    label: "राहु",
    startSec: 43.0,
    durationSec: 2.5,
    glow: "rgba(123,44,191,0.6)",
    portraitFile: "graha/rahu/portrait.png",
    cutoutFile: "graha/rahu/cutout.png",
  },
  {
    id: "ketu",
    label: "केतु",
    startSec: 45.5,
    durationSec: 2.5,
    glow: "rgba(156,102,68,0.5)",
    portraitFile: "graha/ketu/portrait.png",
    cutoutFile: "graha/ketu/cutout.png",
  },
];

/** Action / phase anchors (story-local seconds). */
export const STORY_PHASES = {
  setupEndSec: 13.0,
  /** After Surya/Chandra reveal — chakra + split staging */
  actionStartSec: 33.0,
  chakraSec: 34.5,
  splitSec: 36.5,
  /** After Ketu hero — eclipse chase */
  eclipseStartSec: 48.2,
} as const;

export const secToFrame = (sec: number, fps = 30) => Math.round(sec * fps);

export const getActiveHero = (frame: number, fps = 30): CharacterIntroBeat | null => {
  const t = frame / fps;
  for (const beat of CHARACTER_INTROS) {
    if (t >= beat.startSec && t < beat.startSec + beat.durationSec) {
      return beat;
    }
  }
  return null;
};

export const isInHeroWindow = (frame: number, fps = 30) =>
  getActiveHero(frame, fps) !== null;
