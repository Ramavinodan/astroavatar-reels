import React from "react";
import { Img, interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { GRAHA_META, cutoutSrc } from "../graha/assets";
import type { GrahaId } from "../graha/types";

type Props = {
  id: GrahaId;
  x: number;
  y: number;
  size: number;
  /** 0–1 visibility / entrance */
  entrance: number;
  /** Role badge under figure */
  role?: string;
  emphasize?: boolean;
};

/**
 * Low-level character puppet: cutout + idle bob + aura.
 * Not lip-sync; enough to stage graha meetings on a chart.
 */
export const GrahaSprite: React.FC<Props> = ({
  id,
  x,
  y,
  size,
  entrance,
  role,
  emphasize,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const meta = GRAHA_META[id];

  const pop = spring({
    frame: Math.max(0, Math.round(entrance * 20)),
    fps,
    config: { damping: 14, stiffness: 120 },
  });

  const bob = Math.sin(frame / 14 + id.charCodeAt(0)) * 4;
  const auraPulse = 0.65 + 0.35 * Math.sin(frame / 10 + id.length);
  const opacity = interpolate(entrance, [0, 0.15, 1], [0, 1, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const scale = interpolate(entrance, [0, 1], [0.55, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  }) * (0.92 + pop * 0.08) * (emphasize ? 1.08 : 1);

  return (
    <div
      style={{
        position: "absolute",
        left: x,
        top: y + bob,
        width: size,
        height: size * 1.35,
        transform: `translate(-50%, -70%) scale(${scale})`,
        opacity,
        zIndex: emphasize ? 5 : 3,
      }}
    >
      <div
        style={{
          position: "absolute",
          inset: "10% 5% 0",
          borderRadius: "50%",
          background: `radial-gradient(circle, ${meta.glow}, transparent 70%)`,
          opacity: auraPulse,
          filter: "blur(2px)",
        }}
      />
      <Img
        src={cutoutSrc(id)}
        style={{
          width: "100%",
          height: "100%",
          objectFit: "contain",
          filter: emphasize
            ? `drop-shadow(0 0 18px ${meta.glow})`
            : `drop-shadow(0 8px 16px rgba(0,0,0,0.55))`,
        }}
      />
      <div
        style={{
          position: "absolute",
          left: "50%",
          bottom: -6,
          transform: "translateX(-50%)",
          padding: "4px 10px",
          borderRadius: 999,
          background: "rgba(0,0,0,0.55)",
          border: `1px solid ${meta.color}`,
          color: "#F8F1DE",
          fontSize: 18,
          fontFamily: "Cinzel, Georgia, serif",
          fontWeight: 700,
          whiteSpace: "nowrap",
        }}
      >
        {meta.label}
        {role ? ` · ${role}` : ""}
      </div>
    </div>
  );
};
