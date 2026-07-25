import React from "react";
import { Img, interpolate } from "remotion";

type Props = {
  src: string;
  x: number;
  y: number;
  width: number;
  entrance?: number;
  opacity?: number;
  glow?: string;
  label?: string;
  flipX?: boolean;
};

export const CutoutSprite: React.FC<Props> = ({
  src,
  x,
  y,
  width,
  entrance = 1,
  opacity = 1,
  glow,
  label,
  flipX,
}) => {
  const show = interpolate(entrance, [0, 0.2, 1], [0, 1, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const scale = interpolate(entrance, [0, 1], [0.7, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <div
      style={{
        position: "absolute",
        left: x,
        top: y,
        width,
        transform: `translate(-50%, -80%) scale(${scale}) scaleX(${flipX ? -1 : 1})`,
        opacity: show * opacity,
        zIndex: 4,
      }}
    >
      {glow ? (
        <div
          style={{
            position: "absolute",
            inset: "8% 0 0",
            borderRadius: "50%",
            background: `radial-gradient(circle, ${glow}, transparent 70%)`,
            filter: "blur(4px)",
          }}
        />
      ) : null}
      <Img
        src={src}
        style={{
          width: "100%",
          height: "auto",
          objectFit: "contain",
          filter: glow
            ? `drop-shadow(0 0 16px ${glow})`
            : "drop-shadow(0 10px 18px rgba(0,0,0,0.55))",
        }}
      />
      {label ? (
        <div
          style={{
            position: "absolute",
            left: "50%",
            bottom: -4,
            transform: `translateX(-50%) scaleX(${flipX ? -1 : 1})`,
            padding: "3px 10px",
            borderRadius: 999,
            background: "rgba(0,0,0,0.55)",
            border: "1px solid rgba(233,196,106,0.45)",
            color: "#F8F1DE",
            fontSize: 22,
            fontWeight: 700,
            whiteSpace: "nowrap",
          }}
        >
          {label}
        </div>
      ) : null}
    </div>
  );
};
