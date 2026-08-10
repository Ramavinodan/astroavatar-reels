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

export const DynamicKundli: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Timing constants matching the 20.5s audio script
  const startHouse1 = fps * 8; // 8 seconds in
  const startHouse4 = Math.floor(fps * 9.5); // 9.5 seconds in
  const startHouse7 = fps * 11; // 11 seconds in
  const startHouse8 = Math.floor(fps * 12.5); // 12.5 seconds in
  const startHouse12 = fps * 14; // 14 seconds in

  // Determine current target house based on frame
  const currentTargetHouse = useMemo(() => {
    if (frame >= startHouse12) return 12;
    if (frame >= startHouse8) return 8;
    if (frame >= startHouse7) return 7;
    if (frame >= startHouse4) return 4;
    if (frame >= startHouse1) return 1;
    return 0; // 0 means center of the board
  }, [frame, startHouse1, startHouse4, startHouse7, startHouse8, startHouse12]);

  // Spring animation logic for transitions
  // We compute a progress value for the latest transition
  const getTransitionProgress = () => {
    let delay = 0;
    if (frame >= startHouse12) delay = startHouse12;
    else if (frame >= startHouse8) delay = startHouse8;
    else if (frame >= startHouse7) delay = startHouse7;
    else if (frame >= startHouse4) delay = startHouse4;
    else if (frame >= startHouse1) delay = startHouse1;

    if (delay === 0) {
      // Intro animation from scale 0 to center
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
    if (frame >= startHouse12) return 8;
    if (frame >= startHouse8) return 7;
    if (frame >= startHouse7) return 4;
    if (frame >= startHouse4) return 1;
    if (frame >= startHouse1) return 0;
    return 0;
  }, [frame, startHouse1, startHouse4, startHouse7, startHouse8, startHouse12]);

  // Interpolate X and Y coordinates
  const prevCoords = previousHouse === 0 ? { x: 50, y: 50 } : KUNDLI_HOUSE_CENTERS[previousHouse];
  const targetCoords = currentTargetHouse === 0 ? { x: 50, y: 50 } : KUNDLI_HOUSE_CENTERS[currentTargetHouse];

  const currentX = interpolate(transitionProgress, [0, 1], [prevCoords.x, targetCoords.x]);
  const currentY = interpolate(transitionProgress, [0, 1], [prevCoords.y, targetCoords.y]);
  const scale = currentTargetHouse === 0 ? interpolate(transitionProgress, [0, 1], [0, 1]) : 1;

  // Render subtitles based on timeline (English translation)
  const getSubtitle = () => {
    if (frame < fps * 5) return "Facing repeated delays in your marriage?";
    if (frame < fps * 8) return "Or constant arguments for no reason? It could be Mangal Dosh.";
    if (frame < fps * 14) return "If Mars sits in the 1st, 4th, 7th, 8th, or 12th house, it makes you a Manglik.";
    if (frame < fps * 17) return "This can cause massive tension in married life.";
    return "Do you have Mangal Dosh? Comment 'MANGAL' to find out!";
  };

  return (
    <AbsoluteFill
      style={{
        backgroundColor: "#0d0e15",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        padding: "40px",
      }}
    >
      <Audio src={staticFile("audio/mangal.wav")} />

      {/* Background decoration */}
      <div
        style={{
          position: "absolute",
          width: "100%",
          height: "100%",
          background: "radial-gradient(circle at center, rgba(30, 20, 50, 0.8) 0%, rgba(10, 10, 15, 1) 100%)",
          zIndex: 0,
        }}
      />

      <div style={{ zIndex: 1, position: "relative", width: "100%", display: "flex", justifyContent: "center", marginTop: "100px" }}>
        {/* Pass the currently active house so KundliChart can highlight it red */}
        <KundliChart activeHouses={currentTargetHouse > 0 ? [currentTargetHouse] : []} />

        {/* The Animating Mars Avatar */}
        <div
          style={{
            position: "absolute",
            // The KundliChart is 800x800. We position relative to that grid.
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
          }}
        >
          <Img
            src={staticFile("graha/mangal/portrait.png")}
            style={{ width: "100%", height: "100%", objectFit: "cover" }}
          />
        </div>
      </div>

      {/* Subtitles Area */}
      <div
        style={{
          zIndex: 1,
          marginTop: "120px",
          width: "90%",
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
            fontSize: "48px",
            lineHeight: "1.4",
            margin: 0,
            textShadow: "0 4px 20px rgba(0,0,0,0.8)",
          }}
        >
          {getSubtitle()}
        </h1>
      </div>
    </AbsoluteFill>
  );
};
