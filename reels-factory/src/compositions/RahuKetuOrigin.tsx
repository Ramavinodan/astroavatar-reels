import React from "react";
import {
  AbsoluteFill,
  Audio,
  Easing,
  interpolate,
  Sequence,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { OffthreadVideo } from "remotion";
import { loadFont } from "@remotion/google-fonts/Mukta";
import { CutoutSprite } from "../components/CutoutSprite";
import { LocaleCaptions } from "../components/LocaleCaptions";
import type { LocalePack } from "../i18n/types";
import { rahuKetuLocaleHi } from "../stories/rahuKetu/locale.hi";
import { DailyDoseIntro } from "./DailyDoseIntro";
import {
  END_CARD_FRAMES,
  INTRO_FRAMES,
  RAHU_KETU_DURATION,
  RAHU_KETU_FPS,
  STORY_FILE,
  STORY_FRAMES,
  WELCOME_FILE,
} from "../timing/rahuKetuTiming";

const { fontFamily } = loadFont("normal", {
  weights: ["600", "700"],
  subsets: ["devanagari", "latin"],
});

export const STORY_BODY_FRAMES = STORY_FRAMES;
export { END_CARD_FRAMES, RAHU_KETU_DURATION, RAHU_KETU_FPS };

/** Map original 18s beat frames → story-segment length. */
const T = (frameOn18s: number) =>
  Math.round((frameOn18s * STORY_BODY_FRAMES) / 540);

export type RahuKetuOriginProps = {
  locale: LocalePack;
  endCardFile: string;
};

export const rahuKetuDefaults: RahuKetuOriginProps = {
  locale: rahuKetuLocaleHi,
  endCardFile: "end_card.mp4",
};

const src = {
  mohini: staticFile("supporting/mohini/cutout.png"),
  svarbhanu: staticFile("supporting/svarbhanu/cutout.png"),
  surya: staticFile("graha/surya/cutout.png"),
  chandra: staticFile("graha/chandra/cutout.png"),
  rahu: staticFile("graha/rahu/cutout.png"),
  ketu: staticFile("graha/ketu/cutout.png"),
};

/**
 * Visuals are language-agnostic. Swap `locale` (captions + TTS file) for
 * Tamil/Telugu later — same composition, same assets.
 */
export const RahuKetuOrigin: React.FC<RahuKetuOriginProps> = ({
  locale,
  endCardFile,
}) => {
  const storyFrom = INTRO_FRAMES;
  const endFrom = INTRO_FRAMES + STORY_BODY_FRAMES;

  return (
    <AbsoluteFill style={{ background: "#04060c" }}>
      {/* Welcome = one-time brand audio inside intro. Story audio is separate. */}
      <Sequence from={0} durationInFrames={INTRO_FRAMES}>
        <DailyDoseIntro narrationFile={WELCOME_FILE} />
      </Sequence>

      <Sequence from={storyFrom} durationInFrames={STORY_BODY_FRAMES}>
        <Audio src={staticFile(locale.narrationFile ?? STORY_FILE)} />
        <StoryBody locale={locale} />
      </Sequence>

      <Sequence from={endFrom} durationInFrames={END_CARD_FRAMES}>
        <EndCardCover src={staticFile(endCardFile)} />
      </Sequence>
    </AbsoluteFill>
  );
};

const EndCardCover: React.FC<{ src: string }> = ({ src }) => {
  return (
    <AbsoluteFill style={{ background: "#000" }}>
      <OffthreadVideo
        src={src}
        style={{
          width: "100%",
          height: "100%",
          objectFit: "cover",
        }}
      />
    </AbsoluteFill>
  );
};

const StoryBody: React.FC<{ locale: LocalePack }> = ({ locale }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // --- Scene timing (scaled to narration length) ---
  const mohiniIn = interpolate(frame, [0, T(20)], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const svarIn = interpolate(frame, [T(70), T(100)], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const suryaIn = interpolate(frame, [T(160), T(190)], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const chandraIn = interpolate(frame, [T(170), T(200)], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Svarbhanu slides from right into center-left "deva line"
  const svarX = interpolate(frame, [T(70), T(140)], [980, 320], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.inOut(Easing.cubic),
  });
  const smoke = interpolate(frame, [T(90), T(150), T(210)], [0.7, 0.35, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Split beat
  const splitT = interpolate(frame, [T(300), T(340)], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.inOut(Easing.cubic),
  });
  const chakraFlash = interpolate(frame, [T(295), T(310), T(330)], [0, 1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const svarOut = interpolate(frame, [T(310), T(340)], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const rahuKetuIn = interpolate(frame, [T(320), T(360)], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Eclipse chase
  const chaseT = interpolate(frame, [T(400), T(480)], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.inOut(Easing.quad),
  });
  const eclipse = interpolate(frame, [T(440), T(465), T(510)], [0, 0.72, 0.15], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const bob = Math.sin(frame / 16) * 5;
  const amritaPulse = 0.55 + 0.45 * Math.sin(frame / 10);

  // Mohini center stage early, then shifts slightly
  const mohiniX = interpolate(frame, [0, T(200), T(300)], [540, 700, 780], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // After split, Surya/Chandra move to eclipse positions
  const sunX = interpolate(frame, [T(200), T(400), T(480)], [780, 780, 540], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const sunY = interpolate(frame, [T(200), T(400), T(480)], [520, 520, 620], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const moonX = interpolate(frame, [T(200), T(400), T(480)], [920, 920, 620], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const rahuChaseX = interpolate(chaseT, [0, 1], [280, 500], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const rahuChaseY = interpolate(chaseT, [0, 1], [900, 640], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill
      style={{
        background:
          "radial-gradient(ellipse at 50% 30%, #1b2a4a 0%, #0a1020 50%, #04060c 100%)",
        fontFamily,
      }}
    >
      {/* Cosmic milk ocean shimmer */}
      <div
        style={{
          position: "absolute",
          left: 0,
          right: 0,
          bottom: 0,
          height: 420,
          background:
            "linear-gradient(180deg, transparent, rgba(180,200,230,0.12) 40%, rgba(210,220,240,0.22))",
          opacity: interpolate(frame, [0, T(40)], [0.4, 0.85], {
            extrapolateRight: "clamp",
          }),
        }}
      />

      {/* Amrita glow orb */}
      <div
        style={{
          position: "absolute",
          left: mohiniX - 40,
          top: 380 + bob,
          width: 80,
          height: 80,
          borderRadius: "50%",
          background: `radial-gradient(circle, rgba(255,220,120,${0.9 * amritaPulse}), rgba(255,180,40,0.15) 55%, transparent 70%)`,
          boxShadow: "0 0 40px rgba(255,200,80,0.55)",
          opacity: mohiniIn * (frame < T(320) ? 1 : 0.2),
          zIndex: 5,
        }}
      />

      <CutoutSprite
        src={src.mohini}
        x={mohiniX}
        y={820 + bob}
        width={340}
        entrance={mohiniIn}
        glow="rgba(233,196,106,0.45)"
        label={frame < T(280) ? "मोहिनी" : undefined}
        opacity={interpolate(frame, [T(280), T(340)], [1, 0.25], {
          extrapolateLeft: "clamp",
          extrapolateRight: "clamp",
        })}
      />

      {/* Svarbhanu approaching / disguised */}
      {frame < T(350) ? (
        <CutoutSprite
          src={src.svarbhanu}
          x={svarX}
          y={880 + bob * 0.6}
          width={300}
          entrance={svarIn}
          glow="rgba(123,44,191,0.4)"
          label="स्वर्भानु"
          opacity={svarOut}
        />
      ) : null}

      {/* Smoke disguise veil over Svarbhanu */}
      <div
        style={{
          position: "absolute",
          left: svarX - 120,
          top: 620,
          width: 240,
          height: 320,
          borderRadius: "50%",
          background:
            "radial-gradient(circle, rgba(160,140,200,0.35), transparent 70%)",
          opacity: smoke * svarIn,
          filter: "blur(8px)",
          zIndex: 6,
          pointerEvents: "none",
        }}
      />

      <CutoutSprite
        src={src.surya}
        x={sunX}
        y={sunY + bob * 0.4}
        width={220}
        entrance={suryaIn}
        glow="rgba(240,180,41,0.55)"
        label="सूर्य"
      />
      <CutoutSprite
        src={src.chandra}
        x={moonX}
        y={540 + bob * 0.3}
        width={200}
        entrance={chandraIn}
        glow="rgba(180,210,240,0.5)"
        label="चंद्र"
      />

      {/* Chakra flash — tasteful, no gore */}
      <div
        style={{
          position: "absolute",
          left: 200,
          top: 640,
          width: 220,
          height: 220,
          borderRadius: "50%",
          border: "4px solid rgba(255,220,120,0.9)",
          boxShadow:
            "0 0 50px rgba(255,200,80,0.8), inset 0 0 30px rgba(255,220,120,0.4)",
          opacity: chakraFlash,
          transform: `scale(${0.5 + chakraFlash * 1.6}) rotate(${frame * 8}deg)`,
          zIndex: 8,
        }}
      />
      <AbsoluteFill
        style={{
          background: `radial-gradient(circle at 30% 45%, rgba(255,230,150,${chakraFlash * 0.55}), transparent 45%)`,
          zIndex: 7,
          pointerEvents: "none",
        }}
      />

      {/* Split light ring */}
      <div
        style={{
          position: "absolute",
          left: 200,
          top: 700,
          width: 200,
          height: 200,
          borderRadius: "50%",
          border: "2px solid rgba(233,196,106,0.7)",
          opacity: splitT * (1 - chaseT),
          transform: `scale(${0.8 + splitT * 1.2})`,
          zIndex: 7,
        }}
      />

      {/* Rahu + Ketu emerge */}
      <CutoutSprite
        src={src.rahu}
        x={frame < T(400) ? 260 + splitT * 20 : rahuChaseX}
        y={frame < T(400) ? 860 + bob : rahuChaseY}
        width={240}
        entrance={rahuKetuIn}
        glow="rgba(123,44,191,0.55)"
        label="राहु"
      />
      <CutoutSprite
        src={src.ketu}
        x={420 + splitT * 40}
        y={920 + bob * 0.5}
        width={230}
        entrance={rahuKetuIn}
        glow="rgba(156,102,68,0.45)"
        label="केतु"
        opacity={interpolate(frame, [T(400), T(430)], [1, 0.55], {
          extrapolateLeft: "clamp",
          extrapolateRight: "clamp",
        })}
      />

      {/* Eclipse vignette */}
      <AbsoluteFill
        style={{
          background: `radial-gradient(circle at 50% 40%, transparent 20%, rgba(0,0,0,${eclipse}) 75%)`,
          zIndex: 9,
          pointerEvents: "none",
        }}
      />

      {/* Title chip top */}
      <div
        style={{
          position: "absolute",
          top: 72,
          left: 40,
          right: 40,
          textAlign: "center",
          opacity: interpolate(frame, [0, 18], [0, 1], {
            extrapolateRight: "clamp",
          }),
          zIndex: 10,
        }}
      >
        <div
          style={{
            fontSize: 34,
            letterSpacing: 3,
            color: "rgba(233,196,106,0.9)",
            marginBottom: 10,
          }}
        >
          ज्योतिष कथा
        </div>
        <div style={{ fontSize: 52, fontWeight: 700, color: "#FFF8E7", lineHeight: 1.15 }}>
          राहु-केतु की कहानी
        </div>
      </div>

      <LocaleCaptions captions={locale.captions} fontFamily={fontFamily} />

      {/* tiny fps-safe unused hush */}
      <div style={{ display: "none" }}>{fps}</div>
    </AbsoluteFill>
  );
};
