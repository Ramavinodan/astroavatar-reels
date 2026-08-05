import React from "react";
import { AbsoluteFill, interpolate, useCurrentFrame } from "remotion";
import { STORY_PHASES } from "../stories/rahuKetu/characterIntroBeats";

type Tint = "setup" | "gold" | "purple" | "eclipse" | "neutral";

type Props = {
  /** Story-local tint driven by current beat */
  tint?: Tint;
};

const STARS = Array.from({ length: 48 }, (_, i) => {
  const seed = (i + 1) * 9973;
  const x = (seed % 1000) / 10; // 0–100
  const y = ((seed * 7) % 900) / 10; // 0–90 (keep off ocean a bit)
  const size = 1.5 + (seed % 25) / 10;
  const phase = (seed % 60) / 10;
  return { x, y, size, phase };
});

/**
 * Layered cosmic milk-ocean background — no external plates.
 */
export const CosmicStoryBg: React.FC<Props> = ({ tint = "neutral" }) => {
  const frame = useCurrentFrame();
  const t = frame / 30;

  const oceanDrift = interpolate(frame % 240, [0, 240], [0, 40], {
    extrapolateRight: "clamp",
  });

  const goldBoost =
    tint === "gold" || tint === "setup"
      ? 1
      : tint === "neutral"
        ? 0.35
        : 0.15;
  const purpleBoost = tint === "purple" ? 1 : tint === "eclipse" ? 0.45 : 0.2;
  const eclipseDark = tint === "eclipse" ? 1 : 0;

  const amritaPulse = 0.45 + 0.55 * Math.sin(frame / 11);

  return (
    <AbsoluteFill style={{ overflow: "hidden", background: "#04060c" }}>
      {/* Base radial sky */}
      <AbsoluteFill
        style={{
          background:
            "radial-gradient(ellipse at 50% 28%, #243a62 0%, #121a32 42%, #060912 78%, #02040a 100%)",
        }}
      />

      {/* Gold nebula (Mohini / amrita) */}
      <div
        style={{
          position: "absolute",
          left: -80,
          top: 120,
          width: 720,
          height: 720,
          borderRadius: "50%",
          background:
            "radial-gradient(circle, rgba(233,196,106,0.22), transparent 68%)",
          opacity: 0.35 + 0.45 * goldBoost,
          filter: "blur(8px)",
          transform: `translate(${Math.sin(frame / 40) * 12}px, ${Math.cos(frame / 50) * 8}px)`,
        }}
      />

      {/* Amethyst nebula (Svarbhanu / Rahu) */}
      <div
        style={{
          position: "absolute",
          right: -120,
          top: 280,
          width: 780,
          height: 780,
          borderRadius: "50%",
          background:
            "radial-gradient(circle, rgba(123,44,191,0.28), transparent 70%)",
          opacity: 0.25 + 0.55 * purpleBoost,
          filter: "blur(10px)",
          transform: `translate(${Math.cos(frame / 45) * 14}px, ${Math.sin(frame / 55) * 10}px)`,
        }}
      />

      {/* Starfield */}
      {STARS.map((s, i) => {
        const twinkle =
          0.35 +
          0.65 *
            (0.5 + 0.5 * Math.sin(frame / (14 + s.phase) + s.phase));
        return (
          <div
            key={i}
            style={{
              position: "absolute",
              left: `${s.x}%`,
              top: `${s.y}%`,
              width: s.size,
              height: s.size,
              borderRadius: "50%",
              background: "rgba(255,248,230,0.95)",
              opacity: twinkle * (1 - eclipseDark * 0.55),
              boxShadow: s.size > 2.5 ? "0 0 6px rgba(255,230,180,0.7)" : undefined,
            }}
          />
        );
      })}

      {/* Soft amrita bloom during setup / gold */}
      <div
        style={{
          position: "absolute",
          left: "50%",
          top: 360,
          width: 160,
          height: 160,
          marginLeft: -80,
          borderRadius: "50%",
          background: `radial-gradient(circle, rgba(255,220,120,${0.55 * amritaPulse * goldBoost}), rgba(255,180,40,0.08) 55%, transparent 72%)`,
          opacity: goldBoost > 0.2 && t < STORY_PHASES.actionStartSec ? 1 : 0.15,
          boxShadow: "0 0 50px rgba(255,200,80,0.35)",
          zIndex: 1,
        }}
      />

      {/* Milk ocean band */}
      <div
        style={{
          position: "absolute",
          left: -60,
          right: -60,
          bottom: 0,
          height: 520,
          background:
            "linear-gradient(180deg, transparent 0%, rgba(170,195,230,0.08) 28%, rgba(210,220,240,0.18) 55%, rgba(230,235,245,0.28) 100%)",
          opacity: 0.85 - eclipseDark * 0.35,
          zIndex: 1,
        }}
      />
      <div
        style={{
          position: "absolute",
          left: -80 + oceanDrift,
          right: -120,
          bottom: 40,
          height: 180,
          background:
            "linear-gradient(90deg, transparent, rgba(255,255,255,0.07) 40%, rgba(200,220,255,0.12) 55%, transparent 80%)",
          filter: "blur(6px)",
          opacity: 0.7 - eclipseDark * 0.3,
          zIndex: 2,
        }}
      />
      {/* Ocean horizon line shimmer */}
      <div
        style={{
          position: "absolute",
          left: 0,
          right: 0,
          bottom: 380,
          height: 3,
          background:
            "linear-gradient(90deg, transparent, rgba(255,240,200,0.35), transparent)",
          opacity: 0.5 + 0.3 * Math.sin(frame / 20),
          zIndex: 2,
        }}
      />

      {/* Top text-safe vignette */}
      <AbsoluteFill
        style={{
          background:
            "linear-gradient(180deg, rgba(4,6,12,0.55) 0%, transparent 18%, transparent 72%, rgba(4,6,12,0.35) 100%)",
          zIndex: 3,
          pointerEvents: "none",
        }}
      />

      {/* Eclipse darkness overlay boost */}
      {eclipseDark > 0 ? (
        <AbsoluteFill
          style={{
            background: `radial-gradient(circle at 50% 38%, transparent 18%, rgba(0,0,0,${0.55 * eclipseDark}) 75%)`,
            zIndex: 3,
            pointerEvents: "none",
          }}
        />
      ) : null}
    </AbsoluteFill>
  );
};

export const resolveStoryTint = (frame: number, fps = 30): Tint => {
  const t = frame / fps;
  if (t < STORY_PHASES.setupEndSec) return "setup";
  if (t >= 13.2 && t < 17.5) return "gold";
  if (t >= 22.2 && t < 26.5) return "purple";
  if (t >= 43.0 && t < 48.2) return "purple";
  if (t >= STORY_PHASES.eclipseStartSec) return "eclipse";
  return "neutral";
};
