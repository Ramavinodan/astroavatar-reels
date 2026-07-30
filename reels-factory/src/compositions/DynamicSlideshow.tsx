import React from "react";
import {
  AbsoluteFill,
  Audio,
  Easing,
  Img,
  interpolate,
  OffthreadVideo,
  Sequence,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { loadFont } from "@remotion/google-fonts/Mukta";
import { PremiumIntro } from "./PremiumIntro";

const { fontFamily } = loadFont("normal", {
  weights: ["600", "700"],
  subsets: ["devanagari", "latin"],
});

export type DynamicSlide = {
  file: string;
  caption: string;
  endSec: number;
};

export type DynamicSlideshowProps = {
  narrationFile: string;
  welcomeFile?: string;
  endCardFile?: string;
  category?: string;
  title?: string;
  introFrames?: number;
  storyFrames: number;
  endCardFrames?: number;
  slides: DynamicSlide[];
};

export const defaultDynamicSlideshowProps: DynamicSlideshowProps = {
  narrationFile: "narration/rahu-ketu-hi.wav",
  welcomeFile: "narration/brand/welcome-daily-dose-hi-mixed.wav",
  endCardFile: "end_card.mp4",
  category: "ज्योतिष कथा",
  title: "राहु-केतु की कहानी",
  introFrames: 120,
  storyFrames: 1575, // 52.5 seconds * 30 fps
  endCardFrames: 150, // 5 seconds * 30 fps
  slides: [
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
  ],
};

export const DynamicSlideshow: React.FC<DynamicSlideshowProps> = ({
  narrationFile,
  welcomeFile = "narration/brand/welcome-daily-dose-hi-mixed.wav",
  endCardFile = "end_card.mp4",
  category = "ज्योतिष कथा",
  title = "",
  introFrames = 120,
  storyFrames,
  endCardFrames = 150,
  slides,
}) => {
  const storyFrom = introFrames;
  const endFrom = introFrames + storyFrames;

  return (
    <AbsoluteFill style={{ background: "#04060c", fontFamily }}>
      {/* 1. WELCOME INTRO (0 to introFrames) */}
      <Sequence durationInFrames={introFrames}>
        <PremiumIntro narrationFile={welcomeFile} />
      </Sequence>

      {/* 2. STORY BODY (introFrames to storyFrames) */}
      <Sequence from={storyFrom} durationInFrames={storyFrames}>
        <Audio src={staticFile(narrationFile)} />
        <SlideshowBody category={category} title={title} slides={slides} />
      </Sequence>

      {/* 3. OUTRO END CARD (endFrom to endCardFrames) */}
      <Sequence from={endFrom} durationInFrames={endCardFrames}>
        <AbsoluteFill style={{ background: "#000" }}>
          <OffthreadVideo
            src={staticFile(endCardFile)}
            style={{ width: "100%", height: "100%", objectFit: "cover" }}
          />
        </AbsoluteFill>
      </Sequence>
      
      {/* Permanent Watermark (Top Right) */}
      <div
        style={{
          position: "absolute",
          top: 40,
          right: 40,
          display: "flex",
          alignItems: "center",
          gap: "12px",
          background: "rgba(0, 0, 0, 0.45)",
          padding: "8px 16px",
          borderRadius: 999,
          border: "1px solid rgba(255, 215, 0, 0.3)",
          backdropFilter: "blur(10px)",
          boxShadow: "0 4px 20px rgba(0,0,0,0.5)",
          zIndex: 100
        }}
      >
        <Img 
          src={staticFile("brand/astroavatar_logo.png")} 
          style={{ width: 40, height: 40, objectFit: "contain" }} 
        />
        <span style={{
          color: "#FFD700",
          fontSize: 22,
          fontWeight: 700,
          letterSpacing: 1.5,
          textTransform: "uppercase"
        }}>
          AstroAvatar
        </span>
      </div>
    </AbsoluteFill>
  );
};

const SlideshowBody: React.FC<{
  category: string;
  title: string;
  slides: DynamicSlide[];
}> = ({ category, title, slides }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;

  if (!slides || slides.length === 0) {
    return null;
  }

  let startSec = 0;
  let active = slides[0];
  let slideIndex = 0;

  for (let i = 0; i < slides.length; i++) {
    if (t < slides[i].endSec) {
      active = slides[i];
      slideIndex = i;
      startSec = i === 0 ? 0 : slides[i - 1].endSec;
      break;
    }
    if (i === slides.length - 1) {
      active = slides[i];
      slideIndex = i;
      startSec = i === 0 ? 0 : slides[i - 1].endSec;
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
  const panX = interpolate(
    localFrame,
    [0, durFrames],
    [0, slideIndex % 2 === 0 ? -25 : 25],
    {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    }
  );
  const fade = interpolate(
    localFrame,
    [0, 6, durFrames - 6, durFrames],
    [0, 1, 1, 0.85],
    {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    }
  );
  const capIn = interpolate(localFrame, [3, 12], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill style={{ background: "#04060c", fontFamily }}>
      {/* Background Image with Ken Burns effect */}
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

      {/* Ambient Vignette Gradient Overlay */}
      <AbsoluteFill
        style={{
          background:
            "linear-gradient(180deg, rgba(4,6,12,0.6) 0%, transparent 25%, transparent 58%, rgba(4,6,12,0.85) 100%)",
          pointerEvents: "none",
        }}
      />

      {/* Category Header */}
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
        <div
          style={{
            fontSize: 28,
            color: "rgba(233,196,106,0.95)",
            letterSpacing: 2,
            fontWeight: 700,
            textShadow: "0 2px 8px rgba(0,0,0,0.8)",
          }}
        >
          {category}
        </div>
        {title ? (
          <div
            style={{
              fontSize: 42,
              fontWeight: 700,
              color: "#FFF8E7",
              textShadow: "0 2px 10px rgba(0,0,0,0.9)",
              marginTop: 4,
            }}
          >
            {title}
          </div>
        ) : null}
      </div>

      {/* Subtitle Caption */}
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
            background: "rgba(4,6,12,0.85)",
            border: "1px solid rgba(233,196,106,0.5)",
            color: "#FFF8E7",
            fontSize: 42,
            fontWeight: 700,
            lineHeight: 1.3,
            maxWidth: 980,
            boxShadow: "0 4px 20px rgba(0,0,0,0.6)",
          }}
        >
          {active.caption}
        </div>
      </div>

      {/* Slide Progress Dots */}
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
        {slides.map((_, i) => (
          <div
            key={i}
            style={{
              width: i === slideIndex ? 20 : 8,
              height: 8,
              borderRadius: 4,
              background:
                i === slideIndex
                  ? "rgba(233,196,106,0.95)"
                  : "rgba(255,255,255,0.3)",
            }}
          />

        ))}
      </div>
    </AbsoluteFill>
  );
};
