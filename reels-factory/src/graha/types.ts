export type GrahaId =
  | "surya"
  | "chandra"
  | "mangal"
  | "budha"
  | "guru"
  | "shukra"
  | "shani"
  | "rahu"
  | "ketu";

/** Vedic house number 1–12 (bhava). */
export type HouseNumber = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12;

export type CaptionBeat = {
  text: string;
  fromFrame: number;
  durationInFrames: number;
};

/**
 * Declarative scene: "visitors meet in host's house".
 * Future daily JSON can feed this shape.
 */
export type GrahaMeetingProps = {
  host: GrahaId;
  house: HouseNumber;
  visitors: GrahaId[];
  /** Optional starting houses for fly-in (defaults: opposite / nearby). */
  visitorOrigins?: HouseNumber[];
  title: string;
  captions: CaptionBeat[];
  ctaLine: string;
};
