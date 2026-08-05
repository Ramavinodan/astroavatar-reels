import React from "react";
import {
  AbsoluteFill,
  Easing,
  Img,
  interpolate,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { loadFont } from "@remotion/google-fonts/Mukta";
import { FormatBadge, FormatShell } from "./FormatShell";

const { fontFamily } = loadFont("normal", {
  weights: ["600", "700"],
  subsets: ["devanagari", "latin"],
});

/**
 * FORMAT B — Sentence slideshow: one full-bleed plate per script beat + Ken Burns.
 * Timed across the full ~52.5s story narration.
 */
type Slide = {
  file: string;
  caption: string;
  /** Cumulative end time in story seconds */
  endSec: number;
};

const SLIDES: Slide[] = [
  { file: "formats/slideshow/slide-01-title.png", caption: "आज — राहु और केतु कैसे बने", endSec: 3.2 },
  { file: "formats/slideshow/slide-02-listen.png", caption: "सुनो… एक पुरानी बात", endSec: 6.0 },
  { file: "formats/slideshow/slide-03-churn.png", caption: "देवता-असुर समुद्र मंथन कर रहे थे", endSec: 11.5 },
  { file: "formats/slideshow/slide-04-amrita.png", caption: "अमृत निकला — अमर होने वाला अमृत", endSec: 15.5 },
  { file: "formats/slideshow/slide-05-mohini.png", caption: "मोहिनी रूप में अमृत बाँटने लगीं", endSec: 20.0 },
  { file: "formats/slideshow/slide-06-sneak.png", caption: "एक असुर चुपके से लाइन में घुस आया", endSec: 24.0 },
  { file: "formats/slideshow/slide-07-svarbhanu.png", caption: "उसका नाम था स्वर्भानु", endSec: 27.0 },
  { file: "formats/slideshow/slide-08-drank-surya.png", caption: "अमृत पी लिया · सूर्य-चंद्र ने पकड़ा", endSec: 32.0 },
  { file: "formats/slideshow/slide-09-alert.png", caption: "भेस पकड़ लिया · सच खोल दिया", endSec: 35.5 },
  { file: "formats/slideshow/slide-10-chakra.png", caption: "सुदर्शन चक्र · सिर अलग · शरीर अलग", endSec: 40.0 },
  { file: "formats/slideshow/slide-11-alive-rahu.png", caption: "पर अजीब बात… वो मरा ही नहीं", endSec: 44.0 },
  { file: "formats/slideshow/slide-12-ketu.png", caption: "सिर बना राहु · शरीर बना केतु", endSec: 47.5 },
  { file: "formats/slideshow/slide-13-eclipse.png", caption: "इसीलिए ग्रहण लगता है", endSec: 50.5 },
  { file: "formats/slideshow/slide-14-remember.png", caption: "ये सिर्फ अँधेरा नहीं — एक पुरानी कथा", endSec: 52.5 },
];

export const RahuKetuFormatB: React.FC = () => (
  <FormatShell>
    <FormatBBody />
  </FormatShell>
);

const FormatBBody: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;

  let startSec = 0;
  let active = SLIDES[0];
  let slideIndex = 0;
  for (let i = 0; i < SLIDES.length; i++) {
    if (t < SLIDES[i].endSec) {
      active = SLIDES[i];
      slideIndex = i;
      startSec = i === 0 ? 0 : SLIDES[i - 1].endSec;
      break;
    }
    if (i === SLIDES.length - 1) {
      active = SLIDES[i];
      slideIndex = i;
      startSec = SLIDES[i - 1].endSec;
    }
  }

  const localT = t - startSec;
  const dur = Math.max(0.35, active.endSec - startSec);
  const localFrame = localT * fps;
  const durFrames = dur * fps;

  const scale = interpolate(localFrame, [0, durFrames], [1.0, 1.08], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.quad),
  });
  const panX = interpolate(localFrame, [0, durFrames], [0, slideIndex % 2 === 0 ? -30 : 30], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const fade = interpolate(localFrame, [0, 8, durFrames - 8, durFrames], [0, 1, 1, 0.85], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const capIn = interpolate(localFrame, [4, 14], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill style={{ background: "#04060c", fontFamily }}>
      <FormatBadge label="FORMAT B · Sentence slideshow" fontFamily={fontFamily} />

      <AbsoluteFill style={{ opacity: fade, overflow: "hidden" }}>
        <Img
          src={staticFile(active.file)}
          style={{
            width: "110%",
            height: "110%",
            objectFit: "cover",
            transform: `translate(${panX - 5}%, -5%) scale(${scale})`,
            transformOrigin: "50% 40%",
          }}
        />
      </AbsoluteFill>

      <AbsoluteFill
        style={{
          background:
            "linear-gradient(180deg, rgba(4,6,12,0.45) 0%, transparent 22%, transparent 62%, rgba(4,6,12,0.75) 100%)",
          pointerEvents: "none",
        }}
      />

      <div
        style={{
          position: "absolute",
          top: 100,
          left: 40,
          right: 40,
          textAlign: "center",
          zIndex: 10,
        }}
      >
        <div style={{ fontSize: 30, color: "rgba(233,196,106,0.9)", letterSpacing: 2 }}>
          ज्योतिष कथा
        </div>
        <div style={{ fontSize: 44, fontWeight: 700, color: "#FFF8E7" }}>
          राहु-केतु की कहानी
        </div>
      </div>

      <div
        style={{
          position: "absolute",
          left: 40,
          right: 40,
          bottom: 120,
          textAlign: "center",
          opacity: capIn,
          zIndex: 12,
        }}
      >
        <div
          style={{
            display: "inline-block",
            padding: "18px 28px",
            borderRadius: 18,
            background: "rgba(0,0,0,0.72)",
            border: "1px solid rgba(233,196,106,0.4)",
            color: "#FFF8E7",
            fontSize: 44,
            fontWeight: 700,
            lineHeight: 1.3,
            maxWidth: 980,
          }}
        >
          {active.caption}
        </div>
      </div>

      {/* Progress dots */}
      <div
        style={{
          position: "absolute",
          bottom: 48,
          left: 0,
          right: 0,
          display: "flex",
          justifyContent: "center",
          gap: 6,
          zIndex: 12,
        }}
      >
        {SLIDES.map((_, i) => (
          <div
            key={i}
            style={{
              width: i === slideIndex ? 18 : 8,
              height: 8,
              borderRadius: 4,
              background:
                i === slideIndex ? "rgba(233,196,106,0.95)" : "rgba(255,255,255,0.28)",
            }}
          />
        ))}
      </div>
    </AbsoluteFill>
  );
};
