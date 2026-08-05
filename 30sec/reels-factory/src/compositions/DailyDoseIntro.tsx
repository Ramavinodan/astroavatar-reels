import React from "react";
import {
  AbsoluteFill,
  Audio,
  Easing,
  Img,
  interpolate,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { loadFont } from "@remotion/google-fonts/Mukta";
import {
  INTRO_FRAMES as INTRO_FRAMES_TIMING,
  WELCOME_FILE,
} from "../timing/rahuKetuTiming";

const { fontFamily } = loadFont("normal", {
  weights: ["600", "700"],
  subsets: ["devanagari", "latin"],
});

/** Locked brand intro — ONE-TIME welcome audio; reuse visual every episode. */
export const INTRO_FPS = 30;
export const INTRO_FRAMES = INTRO_FRAMES_TIMING;
export const LOCKED_WELCOME_HI =
  "नमस्ते… AstroAvatar की डेली डोज़ में आपका स्वागत है।";
export const ON_SCREEN_CHIP = "Daily Dose · AstroAvatar";

export type DailyDoseIntroProps = {
  /** One-time welcome TTS (do not regenerate per episode). */
  narrationFile?: string;
  logoFile?: string;
};

export const dailyDoseIntroDefaults: DailyDoseIntroProps = {
  narrationFile: WELCOME_FILE,
  logoFile: "brand/astroavatar_logo.png",
};

export const DailyDoseIntro: React.FC<DailyDoseIntroProps> = ({
  narrationFile,
  logoFile = "brand/astroavatar_logo.png",
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const entrance = spring({
    frame,
    fps,
    config: { damping: 16, stiffness: 90 },
  });

  const logoScale = interpolate(entrance, [0, 1], [0.55, 1]);
  const logoOpacity = interpolate(frame, [0, 12], [0, 1], {
    extrapolateRight: "clamp",
  });
  const glowPulse = 0.55 + 0.45 * Math.sin(frame / 14);
  const spin = interpolate(frame, [0, INTRO_FRAMES], [0, 8], {
    extrapolateRight: "clamp",
  });
  const textIn = interpolate(frame, [35, 55], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  });
  const welcomeIn = interpolate(frame, [50, 75], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const ringScale = interpolate(frame, [10, 90], [0.7, 1.15], {
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill
      style={{
        background:
          "radial-gradient(ellipse at 50% 40%, #1a2744 0%, #0a1020 55%, #04060c 100%)",
        fontFamily,
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      {/* soft stars */}
      <AbsoluteFill
        style={{
          opacity: 0.4,
          backgroundImage:
            "radial-gradient(1.5px 1.5px at 18% 22%, #fff8, transparent)," +
            "radial-gradient(1px 1px at 72% 30%, #fff6, transparent)," +
            "radial-gradient(1.5px 1.5px at 40% 78%, #fff5, transparent)," +
            "radial-gradient(1px 1px at 85% 65%, #fff4, transparent)",
        }}
      />

      {/* aura ring behind logo */}
      <div
        style={{
          position: "absolute",
          width: 520,
          height: 520,
          borderRadius: "50%",
          border: "2px solid rgba(233,196,106,0.35)",
          boxShadow: `0 0 ${40 + glowPulse * 30}px rgba(233,196,106,0.25)`,
          transform: `scale(${ringScale})`,
          opacity: logoOpacity * 0.85,
        }}
      />

      <div
        style={{
          position: "absolute",
          top: "18%",
          width: 420,
          height: 420,
          opacity: logoOpacity,
          transform: `scale(${logoScale}) rotate(${spin}deg)`,
          filter: `drop-shadow(0 0 ${24 + glowPulse * 18}px rgba(233,196,106,0.45))`,
        }}
      >
        <Img
          src={staticFile(logoFile)}
          style={{ width: "100%", height: "100%", objectFit: "contain" }}
        />
      </div>

      <div
        style={{
          position: "absolute",
          top: "58%",
          left: 48,
          right: 48,
          textAlign: "center",
          opacity: textIn,
          transform: `translateY(${(1 - textIn) * 16}px)`,
        }}
      >
        <div
          style={{
            display: "inline-block",
            padding: "10px 22px",
            borderRadius: 999,
            border: "1px solid rgba(233,196,106,0.55)",
            background: "rgba(0,0,0,0.45)",
            color: "#F6E7B0",
            fontSize: 28,
            fontWeight: 700,
            letterSpacing: 1.5,
            marginBottom: 22,
          }}
        >
          {ON_SCREEN_CHIP}
        </div>
        <div
          style={{
            opacity: welcomeIn,
            color: "#FFF8E7",
            fontSize: 44,
            fontWeight: 700,
            lineHeight: 1.35,
            textShadow: "0 4px 24px rgba(0,0,0,0.65)",
          }}
        >
          {LOCKED_WELCOME_HI}
        </div>
      </div>

      {narrationFile ? <Audio src={staticFile(narrationFile)} /> : null}
    </AbsoluteFill>
  );
};
