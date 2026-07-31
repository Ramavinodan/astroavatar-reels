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
  weights: ["600", "700", "800"],
  subsets: ["devanagari", "latin"],
});

export const INTRO_FPS = 30;
export const INTRO_FRAMES = INTRO_FRAMES_TIMING;
export const LOCKED_WELCOME_HI = "नमस्ते… AstroAvatar की डेली डोज़ में आपका स्वागत है।";
export const ON_SCREEN_CHIP = "Daily Dose · AstroAvatar";

export type PremiumIntroProps = {
  narrationFile?: string;
  bgFile?: string;
};

export const premiumIntroDefaults: PremiumIntroProps = {
  narrationFile: WELCOME_FILE,
  bgFile: "brand/premium_intro_bg.png",
};

export const PremiumIntro: React.FC<PremiumIntroProps> = ({
  narrationFile,
  bgFile = "brand/premium_intro_bg.png",
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Animations
  const bgScale = interpolate(frame, [0, INTRO_FRAMES], [1.1, 1.0], {
    extrapolateRight: "clamp",
  });
  
  const bgOpacity = interpolate(frame, [0, 15, INTRO_FRAMES - 15, INTRO_FRAMES], [0, 1, 1, 0], {
    extrapolateRight: "clamp",
  });

  const textEntrance = spring({
    frame: frame - 20,
    fps,
    config: { damping: 14, stiffness: 80 },
  });

  const titleY = interpolate(textEntrance, [0, 1], [40, 0]);
  const titleOpacity = interpolate(textEntrance, [0, 1], [0, 1]);

  const chipEntrance = spring({
    frame: frame - 10,
    fps,
    config: { damping: 14, stiffness: 80 },
  });

  const chipY = interpolate(chipEntrance, [0, 1], [30, 0]);
  const chipOpacity = interpolate(chipEntrance, [0, 1], [0, 1]);

  return (
    <AbsoluteFill style={{ backgroundColor: "#02040a", fontFamily }}>
      {/* Premium Cinematic Background */}
      <AbsoluteFill
        style={{
          transform: `scale(${bgScale})`,
          opacity: bgOpacity,
        }}
      >
        <Img
          src={staticFile(bgFile)}
          style={{ width: "100%", height: "100%", objectFit: "cover", opacity: 0.85 }}
        />
        {/* Soft Vignette Overlay */}
        <div
          style={{
            position: "absolute",
            top: 0,
            left: 0,
            right: 0,
            bottom: 0,
            background: "radial-gradient(circle at center, transparent 30%, rgba(0,0,0,0.8) 90%)",
          }}
        />
        <div
          style={{
            position: "absolute",
            bottom: 0,
            left: 0,
            right: 0,
            height: "40%",
            background: "linear-gradient(to top, rgba(0,0,0,0.95), transparent)",
          }}
        />
      </AbsoluteFill>

      {/* Centered App Logo */}
      <div
        style={{
          position: "absolute",
          top: "50%",
          left: "50%",
          transform: `translate(-50%, -50%) scale(1.15) translateY(${titleY}px)`,
          opacity: titleOpacity,
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          filter: "drop-shadow(0 0 20px rgba(0,0,0,0.8))"
        }}
      >
        <Img
          src={staticFile("brand/astroavatar_logo.png")}
          style={{ width: 450, height: "auto" }}
        />
      </div>

      {narrationFile ? <Audio src={staticFile(narrationFile)} /> : null}
    </AbsoluteFill>
  );
};
