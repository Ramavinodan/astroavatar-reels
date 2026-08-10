import React, { useMemo } from "react";
import {
  AbsoluteFill,
  Img,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
  staticFile,
  Audio,
} from "remotion";
import { KundliChart, KUNDLI_HOUSE_CENTERS } from "../components/KundliChart";
import { BrandedBackground } from "../components/BrandedBackground";

export const YashKundli: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Timing constants matching the 43.16s audio script
  const startHouse1 = Math.floor(fps * 7.5); // 7.5s: 1st house (Ascendant)
  const startHouse9 = Math.floor(fps * 13);  // 13.0s: 9th house (Dhana Yoga)
  const startHouse10 = Math.floor(fps * 22); // 22.0s: 10th house (Neechabhanga Raja Yoga)
  const startDasha = Math.floor(fps * 29);   // 29.0s: Dashas (no specific house, maybe center or highlight 9/10)

  // Determine current target house based on frame
  const currentTargetHouse = useMemo(() => {
    if (frame >= startHouse10 && frame < startDasha) return 10;
    if (frame >= startHouse9 && frame < startHouse10) return 9;
    if (frame >= startHouse1 && frame < startHouse9) return 1;
    if (frame >= startDasha) return 0; // Return to center during Dasha talk
    return 0; // 0 means center of the board
  }, [frame, startHouse1, startHouse9, startHouse10, startDasha]);

  const activeHouses = useMemo(() => {
    if (frame >= startHouse10 && frame < startDasha) return [10];
    if (frame >= startHouse9 && frame < startHouse10) return [9];
    if (frame >= startHouse1 && frame < startHouse9) return [1];
    if (frame >= startDasha) return [1, 9, 10]; // Highlight all key houses at the end
    return [];
  }, [frame, startHouse1, startHouse9, startHouse10, startDasha]);

  // Spring animation logic for transitions
  const getTransitionProgress = () => {
    let delay = 0;
    if (frame >= startDasha) delay = startDasha;
    else if (frame >= startHouse10) delay = startHouse10;
    else if (frame >= startHouse9) delay = startHouse9;
    else if (frame >= startHouse1) delay = startHouse1;

    if (delay === 0) {
      return spring({
        frame,
        fps,
        config: { damping: 12 },
      });
    }

    return spring({
      frame: frame - delay,
      fps,
      config: { damping: 14, stiffness: 90 },
    });
  };

  const transitionProgress = getTransitionProgress();

  // Get previous house to interpolate from
  const previousHouse = useMemo(() => {
    if (frame >= startDasha) return 10;
    if (frame >= startHouse10) return 9;
    if (frame >= startHouse9) return 1;
    if (frame >= startHouse1) return 0;
    return 0;
  }, [frame, startHouse1, startHouse9, startHouse10, startDasha]);

  const prevCoords = previousHouse === 0 ? { x: 50, y: 50 } : KUNDLI_HOUSE_CENTERS[previousHouse as keyof typeof KUNDLI_HOUSE_CENTERS];
  const targetCoords = currentTargetHouse === 0 ? { x: 50, y: 50 } : KUNDLI_HOUSE_CENTERS[currentTargetHouse as keyof typeof KUNDLI_HOUSE_CENTERS];

  const currentX = interpolate(transitionProgress, [0, 1], [prevCoords.x, targetCoords.x]);
  const currentY = interpolate(transitionProgress, [0, 1], [prevCoords.y, targetCoords.y]);
  const scale = currentTargetHouse === 0 && frame < startDasha ? interpolate(transitionProgress, [0, 1], [0, 1]) : 1;

  // Determine which planet image to show in the moving avatar
  const getPlanetImage = () => {
    if (frame >= startHouse10) return "guru"; // Jupiter for 10th house Neechabhanga
    if (frame >= startHouse9) return "shukra"; // Venus for 9th house Dhana Yoga
    if (frame >= startHouse1) return "shukra"; // Venus rules Bharani Nakshatra (1st house)
    return "surya"; // Default starting
  };

  // Render subtitles based on timeline
  const getSubtitle = () => {
    if (frame < fps * 7.5) return "How did a bus driver's son become the Rocking Star of Indian Cinema? Let's decode Yash's Kundli.";
    if (frame < fps * 13) return "He has a Bharani Ascendant ruled by Venus, giving him magnetic screen presence.";
    if (frame < fps * 22) return "But the real magic lies in his 9th house! Venus, Sun, and Mercury form a rare Dhana Yoga here, translating artistic talent into massive wealth.";
    if (frame < fps * 29) return "And in his 10th house, Jupiter creates a Neechabhanga Raja Yoga, driving his self-made rise to the top.";
    if (frame < fps * 36) return "His Venus Dasha started his acting journey, but the Sun Dasha brought global stardom with K G F!";
    return "Next is his Moon Dasha, which points to major international ventures. Yash's stars were truly aligned for greatness!";
  };

  return (
    <BrandedBackground>
      <AbsoluteFill
        style={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
          padding: "40px",
        }}
      >
        <Audio src={staticFile("audio/yash-narration-full.wav")} />

        <div
          style={{
            zIndex: 1,
            position: "relative",
            width: "880px",
            height: "880px",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            marginTop: "100px",
            background: "rgba(0, 0, 0, 0.4)",
            backdropFilter: "blur(20px)",
            borderRadius: "40px",
            border: "1px solid rgba(255,255,255,0.1)",
            boxShadow: "0 20px 50px rgba(0,0,0,0.4)",
          }}
        >
          <div style={{ position: "relative", width: "800px", height: "800px" }}>
            <KundliChart activeHouses={activeHouses} />

            {/* The Animating Planet Avatar */}
            <div
              style={{
                position: "absolute",
                left: `calc(50% - 400px + ${currentX * 8}px)`, 
                top: `calc(${currentY * 8}px)`, 
                transform: `translate(-50%, -50%) scale(${scale})`,
                width: "120px",
                height: "120px",
                borderRadius: "50%",
                overflow: "hidden",
                border: "4px solid #ff4444",
                boxShadow: "0 0 30px rgba(255, 50, 50, 0.8)",
                zIndex: 10,
                transition: "background 0.3s ease",
              }}
            >
              <Img
                src={staticFile(`graha/${getPlanetImage()}/portrait.png`)}
                style={{ width: "100%", height: "100%", objectFit: "cover" }}
              />
            </div>
          </div>
        </div>

        {/* Subtitles Area */}
        <div
          style={{
            zIndex: 1,
            marginTop: "80px",
            width: "95%",
            padding: "40px",
            background: "rgba(255,255,255,0.05)",
            backdropFilter: "blur(10px)",
            borderRadius: "20px",
            border: "1px solid rgba(255,255,255,0.1)",
            textAlign: "center",
          }}
        >
          <h1
            style={{
              fontFamily: "'Inter', sans-serif",
              color: "white",
              fontSize: "42px",
              lineHeight: "1.4",
              margin: 0,
              textShadow: "0 4px 20px rgba(0,0,0,0.8)",
            }}
          >
            {getSubtitle()}
          </h1>
        </div>
      </AbsoluteFill>
    </BrandedBackground>
  );
};
