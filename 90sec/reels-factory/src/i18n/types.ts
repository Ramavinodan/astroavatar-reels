/**
 * Language pack — visuals stay language-agnostic.
 * Swap this object (captions + narration audio) for Tamil/Telugu later.
 */
export type CaptionCue = {
  text: string;
  fromFrame: number;
  durationInFrames: number;
};

export type LocalePack = {
  /** e.g. "hi" | "ta" | "te" */
  locale: string;
  /** Optional TTS file under public/, e.g. "narration/rahu-ketu-hi.mp3" */
  narrationFile?: string;
  captions: CaptionCue[];
};
