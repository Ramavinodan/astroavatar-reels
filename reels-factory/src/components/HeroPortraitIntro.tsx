import React from "react";
import { AbsoluteFill, Easing, Img, interpolate, useCurrentFrame } from "remotion";

type Props = {
  src: string;
  label: string;
  glow: string;
  /** Local frame within the hero Sequence (0-based). */
  localFrame: number;
  durationInFrames: number;
  fontFamily: string;
};

/**
 * Full-size portrait reveal for a character's first mention in narration.
 */
export const HeroPortraitIntro: React.FC<Props> = ({
  src,
  label,
  glow,
  localFrame,
  durationInFrames,
  fontFamily,
}) => {
  const fadeIn = Math.min(18, Math.floor(durationInFrames * 0.25));
  const fadeOutStart = Math.max(fadeIn + 6, durationInFrames - 14);

  const opacity = interpolate(
    localFrame,
    [0, fadeIn, fadeOutStart, durationInFrames],
    [0, 1, 1, 0],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
  );

  const scale = interpolate(localFrame, [0, durationInFrames], [1.0, 1.06], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.quad),
  });

  const rise = interpolate(localFrame, [0, fadeIn], [40, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  });

  const labelIn = interpolate(localFrame, [8, 22], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill
      style={{
        zIndex: 12,
        pointerEvents: "none",
        opacity,
        fontFamily,
      }}
    >
      {/* Soft focus veil so portrait owns the frame */}
      <AbsoluteFill
        style={{
          background:
            "radial-gradient(ellipse at 50% 42%, rgba(8,12,28,0.15) 0%, rgba(4,6,12,0.72) 70%)",
        }}
      />

      <div
        style={{
          position: "absolute",
          left: "50%",
          top: 120,
          width: 1080,
          transform: `translateX(-50%) translateY(${rise}px) scale(${scale})`,
          transformOrigin: "50% 35%",
        }}
      >
        <div
          style={{
            position: "absolute",
            left: "5%",
            right: "5%",
            top: "5%",
            bottom: "12%",
            borderRadius: "50%",
            background: `radial-gradient(circle, ${glow}, transparent 68%)`,
            filter: "blur(22px)",
            opacity: 0.9,
          }}
        />
        <Img
          src={src}
          style={{
            width: "100%",
            height: 1280,
            objectFit: "cover",
            objectPosition: "50% 18%",
            borderRadius: 8,
            filter: `drop-shadow(0 18px 40px rgba(0,0,0,0.65)) drop-shadow(0 0 28px ${glow})`,
          }}
        />
        <div
          style={{
            marginTop: 16,
            textAlign: "center",
            opacity: labelIn,
          }}
        >
          <span
            style={{
              display: "inline-block",
              padding: "10px 28px",
              borderRadius: 999,
              background: "rgba(0,0,0,0.62)",
              border: "1.5px solid rgba(233,196,106,0.55)",
              color: "#FFF8E7",
              fontSize: 48,
              fontWeight: 700,
              letterSpacing: 1,
            }}
          >
            {label}
          </span>
        </div>
      </div>
    </AbsoluteFill>
  );
};

/** Wrapper that reads global story frame and maps to local hero progress. */
export const HeroPortraitFromGlobal: React.FC<{
  src: string;
  label: string;
  glow: string;
  startFrame: number;
  durationInFrames: number;
  fontFamily: string;
}> = ({ src, label, glow, startFrame, durationInFrames, fontFamily }) => {
  const frame = useCurrentFrame();
  if (frame < startFrame || frame >= startFrame + durationInFrames) {
    return null;
  }
  return (
    <HeroPortraitIntro
      src={src}
      label={label}
      glow={glow}
      localFrame={frame - startFrame}
      durationInFrames={durationInFrames}
      fontFamily={fontFamily}
    />
  );
};
