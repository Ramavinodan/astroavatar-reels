import React from "react";
import { AbsoluteFill, Img, staticFile } from "remotion";

export const BrandedBackground: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  return (
    <AbsoluteFill
      style={{
        backgroundColor: "#ffffff", // Fallback light color
        overflow: "hidden",
      }}
    >
      {/* Light Abstract Generated Background */}
      <AbsoluteFill>
        <Img
          src={staticFile("bg_light.png")}
          style={{ width: "100%", height: "100%", objectFit: "cover" }}
        />
        {/* Subtle dark overlay so the yellow Kundli chart still pops */}
        <div
          style={{
            position: "absolute",
            width: "100%",
            height: "100%",
            background: "linear-gradient(to bottom, rgba(0,0,0,0.1), rgba(0,0,0,0.5))",
          }}
        />
      </AbsoluteFill>

      {/* AstroAvatar Branding Header */}
      <div
        style={{
          position: "absolute",
          top: "60px",
          width: "auto",
          left: "50%",
          transform: "translateX(-50%)",
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          gap: "15px",
          zIndex: 50, // Keep branding above other elements
          opacity: 0.9,
          background: "rgba(0, 0, 0, 0.4)",
          backdropFilter: "blur(20px)",
          padding: "15px 40px",
          borderRadius: "50px",
          border: "1px solid rgba(255,255,255,0.1)",
          boxShadow: "0 10px 30px rgba(0,0,0,0.3)",
        }}
      >
        <div
          style={{
            width: "60px",
            height: "60px",
            borderRadius: "50%",
            overflow: "hidden",
            border: "2px solid rgba(255, 215, 0, 0.4)",
            boxShadow: "0 0 15px rgba(255, 215, 0, 0.2)",
          }}
        >
          <Img
            src={staticFile("logo.png")}
            style={{ width: "100%", height: "100%", objectFit: "cover" }}
          />
        </div>
        <h2
          style={{
            fontFamily: "'Outfit', 'Inter', sans-serif",
            fontSize: "36px",
            color: "rgba(255, 255, 255, 0.9)",
            letterSpacing: "4px",
            textTransform: "uppercase",
            margin: 0,
            textShadow: "0 2px 10px rgba(0,0,0,0.5)",
            fontWeight: 600,
          }}
        >
          AstroAvatar
        </h2>
      </div>

      {/* Children Content Layer (Kundli Chart, Text, etc) */}
      <AbsoluteFill style={{ zIndex: 10 }}>
        {children}
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
