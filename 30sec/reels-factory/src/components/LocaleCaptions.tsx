import React from "react";
import { AbsoluteFill, Easing, interpolate, Sequence, useCurrentFrame } from "remotion";
import type { CaptionCue } from "../i18n/types";

type Props = {
  captions: CaptionCue[];
  fontFamily: string;
};

export const LocaleCaptions: React.FC<Props> = ({ captions, fontFamily }) => {
  return (
    <>
      {captions.map((cap, i) => (
        <Sequence
          key={`${i}-${cap.fromFrame}`}
          from={cap.fromFrame}
          durationInFrames={cap.durationInFrames}
          layout="none"
        >
          <CaptionLine text={cap.text} fontFamily={fontFamily} />
        </Sequence>
      ))}
    </>
  );
};

const CaptionLine: React.FC<{ text: string; fontFamily: string }> = ({
  text,
  fontFamily,
}) => {
  const frame = useCurrentFrame();
  const opacity = interpolate(frame, [0, 8, 50, 62], [0, 1, 1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const y = interpolate(frame, [0, 8], [24, 0], {
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  });

  return (
    <AbsoluteFill style={{ pointerEvents: "none" }}>
      <div
        style={{
          position: "absolute",
          left: 40,
          right: 40,
          bottom: 170,
          opacity,
          transform: `translateY(${y}px)`,
          textAlign: "center",
          fontFamily,
        }}
      >
        <div
          style={{
            display: "inline-block",
            padding: "18px 22px",
            background: "rgba(0,0,0,0.62)",
            border: "1px solid rgba(233,196,106,0.4)",
            borderRadius: 16,
            color: "#FFF8E7",
            fontSize: 52,
            fontWeight: 700,
            lineHeight: 1.25,
            maxWidth: 1000,
          }}
        >
          {text}
        </div>
      </div>
    </AbsoluteFill>
  );
};
