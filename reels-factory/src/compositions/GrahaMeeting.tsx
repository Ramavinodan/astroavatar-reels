import React from "react";
import {
  AbsoluteFill,
  Easing,
  interpolate,
  Sequence,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { loadFont } from "@remotion/google-fonts/Cinzel";
import { KundliChart } from "../components/KundliChart";
import { GrahaSprite } from "../components/GrahaSprite";
import { GRAHA_META } from "../graha/assets";
import {
  defaultOrigins,
  houseCenter,
  toChartPixel,
} from "../graha/houseLayout";
import type { GrahaMeetingProps } from "../graha/types";

const { fontFamily } = loadFont("normal", {
  weights: ["600", "700"],
  subsets: ["latin"],
});

const WIDTH = 1080;
const HEIGHT = 1920;

export const grahaMeetingDefaults: GrahaMeetingProps = {
  host: "guru",
  house: 7,
  visitors: ["shani", "mangal"],
  visitorOrigins: [1, 4],
  title: "When Shani meets Mangal",
  captions: [
    {
      text: "दो ग्रह — एक ही भाव में",
      fromFrame: 45,
      durationInFrames: 70,
    },
    {
      text: "Shani + Mangal enter Guru's house",
      fromFrame: 120,
      durationInFrames: 90,
    },
    {
      text: "Discipline meets fire — pressure + courage",
      fromFrame: 230,
      durationInFrames: 100,
    },
    {
      text: "Not fate alone — how you act in that house",
      fromFrame: 350,
      durationInFrames: 90,
    },
  ],
  ctaLine: "AstroAvatar · Free kundli & daily guidance",
};

/** Quadratic bezier for fly-in arcs (not a straight Ken Burns pan). */
const quad = (
  t: number,
  a: { x: number; y: number },
  b: { x: number; y: number },
  c: { x: number; y: number },
) => {
  const u = 1 - t;
  return {
    x: u * u * a.x + 2 * u * t * b.x + t * t * c.x,
    y: u * u * a.y + 2 * u * t * b.y + t * t * c.y,
  };
};

export const GrahaMeeting: React.FC<GrahaMeetingProps> = (props) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const chartSize = 920;
  const chart = {
    left: (WIDTH - chartSize) / 2,
    top: 420,
    size: chartSize,
  };

  const origins =
    props.visitorOrigins ?? defaultOrigins(props.house, props.visitors.length);

  const chartIn = spring({
    frame,
    fps,
    config: { damping: 18, stiffness: 80 },
  });

  const hostEntrance = interpolate(frame, [20, 55], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  });

  const meetCenter = toChartPixel(houseCenter(props.house), chart);
  // Offset visitors slightly so they don't stack perfectly
  const meetOffsets = [
    { x: -70, y: -10 },
    { x: 70, y: 10 },
    { x: 0, y: -60 },
  ];

  const travelStart = 70;
  const travelEnd = 160;
  const meetFlash = interpolate(frame, [155, 175, 210], [0, 1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const endCardIn = interpolate(frame, [450, 490], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const hostMeta = GRAHA_META[props.host];

  return (
    <AbsoluteFill
      style={{
        background:
          "radial-gradient(ellipse at 50% 20%, #1a2744 0%, #070b14 55%, #04060c 100%)",
        fontFamily,
        color: "#F8F1DE",
      }}
    >
      {/* Cosmic dust */}
      <AbsoluteFill
        style={{
          opacity: 0.35,
          backgroundImage:
            "radial-gradient(1.5px 1.5px at 20% 30%, #fff8, transparent)," +
            "radial-gradient(1px 1px at 70% 20%, #fff6, transparent)," +
            "radial-gradient(1.5px 1.5px at 40% 80%, #fff5, transparent)," +
            "radial-gradient(1px 1px at 85% 60%, #fff4, transparent)",
        }}
      />

      {/* Title */}
      <div
        style={{
          position: "absolute",
          top: 96,
          left: 48,
          right: 48,
          textAlign: "center",
          opacity: interpolate(frame, [0, 25], [0, 1], {
            extrapolateRight: "clamp",
          }),
        }}
      >
        <div
          style={{
            fontSize: 28,
            letterSpacing: 4,
            textTransform: "uppercase",
            color: "rgba(233,196,106,0.85)",
            marginBottom: 12,
          }}
        >
          Graha Meeting
        </div>
        <div style={{ fontSize: 52, fontWeight: 700, lineHeight: 1.15 }}>
          {props.title}
        </div>
        <div
          style={{
            marginTop: 14,
            fontSize: 26,
            color: "rgba(248,241,222,0.75)",
          }}
        >
          in {hostMeta.label}&apos;s house · Bhava {props.house}
        </div>
      </div>

      <div
        style={{
          opacity: chartIn,
          transform: `scale(${0.92 + chartIn * 0.08})`,
        }}
      >
        <KundliChart
          chart={chart}
          activeHouse={props.house}
          appearProgress={chartIn}
        />
      </div>

      {/* Host — already in the house */}
      <GrahaSprite
        id={props.host}
        x={meetCenter.x}
        y={meetCenter.y - 40}
        size={210}
        entrance={hostEntrance}
        role="Host"
        emphasize={frame > 160}
      />

      {/* Visitors fly along arcs into the house */}
      {props.visitors.map((id, i) => {
        const originHouse = origins[i] ?? defaultOrigins(props.house, i + 1)[i];
        const from = toChartPixel(houseCenter(originHouse), chart);
        const to = {
          x: meetCenter.x + (meetOffsets[i]?.x ?? 0),
          y: meetCenter.y + (meetOffsets[i]?.y ?? 0) + 30,
        };
        const control = {
          x: (from.x + to.x) / 2 + (i === 0 ? -180 : 180),
          y: Math.min(from.y, to.y) - 220,
        };

        const t = interpolate(frame, [travelStart + i * 8, travelEnd + i * 8], [0, 1], {
          extrapolateLeft: "clamp",
          extrapolateRight: "clamp",
          easing: Easing.inOut(Easing.cubic),
        });

        const pos = t <= 0 ? from : t >= 1 ? to : quad(t, from, control, to);
        const entrance = interpolate(frame, [travelStart + i * 8 - 10, travelStart + i * 8 + 15], [0, 1], {
          extrapolateLeft: "clamp",
          extrapolateRight: "clamp",
        });

        return (
          <GrahaSprite
            key={id}
            id={id}
            x={pos.x}
            y={pos.y}
            size={185}
            entrance={entrance}
            role="Visitor"
            emphasize={t > 0.95}
          />
        );
      })}

      {/* Meeting impact ring */}
      <div
        style={{
          position: "absolute",
          left: meetCenter.x - 120,
          top: meetCenter.y - 120,
          width: 240,
          height: 240,
          borderRadius: "50%",
          border: "3px solid rgba(233,196,106,0.85)",
          boxShadow: `0 0 40px ${hostMeta.glow}`,
          opacity: meetFlash,
          transform: `scale(${0.6 + meetFlash * 1.4})`,
        }}
      />

      {/* Captions */}
      {props.captions.map((cap, idx) => (
        <Sequence
          key={idx}
          from={cap.fromFrame}
          durationInFrames={cap.durationInFrames}
          layout="none"
        >
          <CaptionCard text={cap.text} />
        </Sequence>
      ))}

      {/* End card */}
      <AbsoluteFill
        style={{
          opacity: endCardIn,
          background: "rgba(4,6,12,0.72)",
          justifyContent: "center",
          alignItems: "center",
          padding: 64,
        }}
      >
        <div style={{ textAlign: "center" }}>
          <div
            style={{
              fontSize: 34,
              color: "rgba(233,196,106,0.9)",
              letterSpacing: 3,
              marginBottom: 18,
            }}
          >
            AstroAvatar
          </div>
          <div style={{ fontSize: 48, fontWeight: 700, marginBottom: 20 }}>
            See this in your kundli
          </div>
          <div style={{ fontSize: 30, color: "rgba(248,241,222,0.85)" }}>
            {props.ctaLine}
          </div>
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

const CaptionCard: React.FC<{ text: string }> = ({ text }) => {
  const frame = useCurrentFrame();
  const opacity = interpolate(frame, [0, 12, 55, 70], [0, 1, 1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const y = interpolate(frame, [0, 12], [28, 0], {
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  });

  return (
    <div
      style={{
        position: "absolute",
        left: 48,
        right: 48,
        bottom: 160,
        opacity,
        transform: `translateY(${y}px)`,
        textAlign: "center",
      }}
    >
      <div
        style={{
          display: "inline-block",
          padding: "22px 28px",
          background: "rgba(0,0,0,0.55)",
          border: "1px solid rgba(233,196,106,0.45)",
          borderRadius: 18,
          fontSize: 40,
          fontWeight: 700,
          lineHeight: 1.25,
          maxWidth: 960,
        }}
      >
        {text}
      </div>
    </div>
  );
};

export const GRAHA_MEETING_DURATION = 540; // 18s @ 30fps
export const GRAHA_MEETING_FPS = 30;
export const GRAHA_MEETING_SIZE = { width: WIDTH, height: HEIGHT };
