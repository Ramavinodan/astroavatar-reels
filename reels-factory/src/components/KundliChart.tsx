import React from "react";
import { AbsoluteFill, interpolate, useCurrentFrame } from "remotion";
import { houseCenter, type Point } from "../graha/houseLayout";
import type { HouseNumber } from "../graha/types";

type Props = {
  chart: { left: number; top: number; size: number };
  activeHouse: HouseNumber;
  appearProgress: number;
};

export const KundliChart: React.FC<Props> = ({
  chart,
  activeHouse,
  appearProgress,
}) => {
  const frame = useCurrentFrame();
  const { left, top, size } = chart;
  const pulse = 0.45 + 0.55 * Math.sin(frame / 12);

  const strokeOpacity = interpolate(appearProgress, [0, 1], [0, 0.9]);
  const active = houseCenter(activeHouse);
  const activePx: Point = {
    x: left + active.x * size,
    y: top + active.y * size,
  };

  const mid = size / 2;

  return (
    <AbsoluteFill style={{ pointerEvents: "none" }}>
      <svg
        width={size}
        height={size}
        style={{
          position: "absolute",
          left,
          top,
          opacity: strokeOpacity,
          overflow: "visible",
        }}
      >
        <defs>
          <radialGradient id="houseGlow" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stopColor="rgba(233,196,106,0.55)" />
            <stop offset="100%" stopColor="rgba(233,196,106,0)" />
          </radialGradient>
        </defs>

        {/* Outer square */}
        <rect
          x={2}
          y={2}
          width={size - 4}
          height={size - 4}
          fill="rgba(8,12,24,0.55)"
          stroke="rgba(233,196,106,0.85)"
          strokeWidth={3}
        />

        {/* Diagonals + mid cross → North Indian diamond feel */}
        <line x1={2} y1={2} x2={size - 2} y2={size - 2} stroke="rgba(233,196,106,0.55)" strokeWidth={2} />
        <line x1={size - 2} y1={2} x2={2} y2={size - 2} stroke="rgba(233,196,106,0.55)" strokeWidth={2} />
        <line x1={mid} y1={2} x2={mid} y2={size - 2} stroke="rgba(233,196,106,0.4)" strokeWidth={1.5} />
        <line x1={2} y1={mid} x2={size - 2} y2={mid} stroke="rgba(233,196,106,0.4)" strokeWidth={1.5} />

        {/* Inner diamond */}
        <polygon
          points={`${mid},8 ${size - 8},${mid} ${mid},${size - 8} 8,${mid}`}
          fill="none"
          stroke="rgba(233,196,106,0.65)"
          strokeWidth={2}
        />

        {/* House numbers */}
        {([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] as HouseNumber[]).map((h) => {
          const c = houseCenter(h);
          const isActive = h === activeHouse;
          return (
            <text
              key={h}
              x={c.x * size}
              y={c.y * size}
              textAnchor="middle"
              dominantBaseline="middle"
              fill={isActive ? "#F6E7B0" : "rgba(230,220,190,0.45)"}
              fontSize={isActive ? 28 : 18}
              fontFamily="Cinzel, Georgia, serif"
              fontWeight={700}
            >
              {h}
            </text>
          );
        })}
      </svg>

      {/* Active house aura (screen space) */}
      <div
        style={{
          position: "absolute",
          left: activePx.x - 90,
          top: activePx.y - 90,
          width: 180,
          height: 180,
          borderRadius: "50%",
          background: "radial-gradient(circle, rgba(233,196,106,0.35), transparent 70%)",
          opacity: appearProgress * (0.55 + 0.45 * pulse),
          transform: `scale(${0.9 + pulse * 0.15})`,
        }}
      />
    </AbsoluteFill>
  );
};
