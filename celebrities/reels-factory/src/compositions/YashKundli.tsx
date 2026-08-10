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

  // Timing constants matching the 41.05s Sarvam audio
  const startHouse1 = Math.floor(fps * 7);  // 7s: 1st house (Ascendant)
  const startHouse9 = Math.floor(fps * 12); // 12s: 9th house (Dhana Yoga)
  const startHouse10 = Math.floor(fps * 20); // 20s: 10th house (Neechabhanga Raja Yoga)
  const startDasha = Math.floor(fps * 28);  // 28s: Dashas (no specific house, maybe highlight 9/10)

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

  // Determine which planet images to show in the moving avatar
  const getPlanetImages = () => {
    if (frame >= startHouse10) return ["guru"]; // Jupiter for 10th house Neechabhanga
    if (frame >= startHouse9) return ["shukra", "surya", "budha"]; // Venus, Sun, Mercury for 9th house Dhana Yoga
    if (frame >= startHouse1) return ["shukra"]; // Venus rules Bharani Nakshatra (1st house)
    return ["surya"]; // Default starting
  };

  const planetImages = getPlanetImages();

  const getPlanetDisplayName = (key: string) => {
    const map: Record<string, string> = {
      shukra: "Venus",
      surya: "Sun",
      budha: "Mercury",
      guru: "Jupiter",
      mangal: "Mars",
      chandra: "Moon",
      shani: "Saturn",
      rahu: "Rahu",
      ketu: "Ketu"
    };
    return map[key] || key;
  };

  // Render subtitles based on timeline
  const getSubtitle = () => {
    if (frame < fps * 7) return "From a bus driver's son to the unstoppable Rocky Bhai, how did Yash conquer Indian cinema? The secret is in his stars!";
    if (frame < fps * 12) return "Born with a Bharani Ascendant ruled by Venus, he was destined for an electrifying screen presence.";
    if (frame < fps * 20) return "But look at his 9th house! Venus, Sun, and Mercury unite to form a massive Dhana Yoga, turning pure artistic talent into a box-office goldmine!";
    if (frame < fps * 28) return "And it doesn't stop there. In his 10th house, Jupiter creates a powerful Neechabhanga Raja Yoga, fueling his incredible self-made rise from humble beginnings to the absolute top!";
    if (frame < fps * 35) return "His Venus Dasha sparked his acting debut, but it was the fiery Sun Dasha that gave the world K G F!";
    return "Now entering his Moon Dasha, get ready for Yash to dominate on a global scale. The stars have spoken!";
  };

  const getYogaHighlight = () => {
    if (frame >= startHouse9 && frame < startHouse10) return "💰 DHANA YOGA";
    if (frame >= startHouse10 && frame < startDasha) return "👑 NEECHABHANGA RAJA YOGA";
    return null;
  };

  const yogaHighlight = getYogaHighlight();

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
        <Audio src={staticFile("audio/bgm-mass.mp3")} volume={0.15} />

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

            {/* The Animating Planet Avatars */}
            <div
              style={{
                position: "absolute",
                left: `calc(50% - 400px + ${currentX * 8}px)`, 
                top: `calc(${currentY * 8}px)`, 
                transform: `translate(-50%, -50%) scale(${scale})`,
                display: "flex",
                flexDirection: "row",
                alignItems: "center",
                justifyContent: "center",
                zIndex: 10,
                transition: "all 0.3s ease",
              }}
            >
              {planetImages.map((planet, idx) => (
                <div
                  key={planet}
                  style={{
                    position: "relative",
                    width: "120px",
                    height: "120px",
                    borderRadius: "50%",
                    overflow: "hidden",
                    border: "4px solid #ff4444",
                    boxShadow: "0 0 30px rgba(255, 50, 50, 0.8)",
                    marginLeft: idx > 0 ? "-40px" : "0", // Overlap effect
                    zIndex: 10 - idx, // Keep first one on top
                    background: "#000"
                  }}
                >
                  <Img
                    src={staticFile(`graha/${planet}/portrait.png`)}
                    style={{ width: "100%", height: "100%", objectFit: "cover" }}
                  />
                  <div
                    style={{
                      position: "absolute",
                      bottom: "0",
                      left: "0",
                      width: "100%",
                      background: "rgba(0, 0, 0, 0.7)",
                      color: "white",
                      fontSize: "14px",
                      fontWeight: "bold",
                      textAlign: "center",
                      padding: "4px 0",
                      textTransform: "uppercase",
                      letterSpacing: "1px",
                    }}
                  >
                    {getPlanetDisplayName(planet)}
                  </div>
                </div>
              ))}
            </div>
            
            {yogaHighlight && (
              <div style={{
                position: "absolute",
                top: "100px",
                left: "50%",
                transform: "translateX(-50%)",
                background: "linear-gradient(90deg, #FFD700, #FFA500)",
                padding: "10px 30px",
                borderRadius: "30px",
                color: "black",
                fontWeight: "bold",
                fontSize: "36px",
                boxShadow: "0 0 20px rgba(255, 215, 0, 0.8)",
                zIndex: 20,
                whiteSpace: "nowrap"
              }}>
                {yogaHighlight}
              </div>
            )}
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
