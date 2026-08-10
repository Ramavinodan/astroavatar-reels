import React from "react";
import { AbsoluteFill } from "remotion";

export const KundliChart: React.FC<{ activeHouses: number[] }> = ({ activeHouses }) => {
  // SVG points for 100x100 viewbox
  const outerSquare = "0,0 100,0 100,100 0,100 0,0";
  const innerDiamond = "50,0 100,50 50,100 0,50 50,0";

  // Define polygons for each of the 12 houses to allow highlighting
  const houses = [
    { id: 1, points: "50,0 25,25 50,50 75,25" },
    { id: 2, points: "0,0 50,0 25,25" },
    { id: 3, points: "0,0 25,25 0,50" },
    { id: 4, points: "0,50 25,25 50,50 25,75" },
    { id: 5, points: "0,50 25,75 0,100" },
    { id: 6, points: "0,100 25,75 50,100" },
    { id: 7, points: "50,50 25,75 50,100 75,75" },
    { id: 8, points: "50,100 75,75 100,100" },
    { id: 9, points: "100,50 75,75 100,100" },
    { id: 10, points: "50,50 75,75 100,50 75,25" },
    { id: 11, points: "100,0 75,25 100,50" },
    { id: 12, points: "50,0 75,25 100,0" },
  ];

  return (
    <div
      style={{
        position: "relative",
        width: "800px",
        height: "800px",
        margin: "0 auto",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
      }}
    >
      {/* Glassmorphism background box */}
      <div
        style={{
          position: "absolute",
          width: "100%",
          height: "100%",
          background: "rgba(20, 20, 30, 0.4)",
          backdropFilter: "blur(12px)",
          WebkitBackdropFilter: "blur(12px)",
          border: "2px solid rgba(255, 215, 0, 0.3)",
          boxShadow: "0 0 40px rgba(255, 215, 0, 0.1)",
          borderRadius: "20px",
          padding: "20px",
        }}
      >
        <svg
          viewBox="0 0 100 100"
          style={{
            width: "100%",
            height: "100%",
            filter: "drop-shadow(0px 0px 8px rgba(255, 215, 0, 0.5))",
          }}
        >
          {/* Base lines for structure */}
          <polyline points={outerSquare} fill="none" stroke="#FFD700" strokeWidth="1" />
          <polyline points={innerDiamond} fill="none" stroke="#FFD700" strokeWidth="1" />
          <line x1="0" y1="0" x2="100" y2="100" stroke="#FFD700" strokeWidth="1" />
          <line x1="100" y1="0" x2="0" y2="100" stroke="#FFD700" strokeWidth="1" />

          {/* Highlight active houses */}
          {houses.map((house) => (
            <polygon
              key={house.id}
              points={house.points}
              fill={activeHouses.includes(house.id) ? "rgba(255, 50, 50, 0.6)" : "transparent"}
              stroke="#FFD700"
              strokeWidth="0.5"
              style={{
                transition: "fill 0.3s ease-in-out",
              }}
            />
          ))}

          {/* House Numbers */}
          {Object.entries(KUNDLI_HOUSE_CENTERS).map(([houseId, coords]) => (
            <text
              key={`text-${houseId}`}
              x={coords.x}
              y={coords.y}
              fill="rgba(255, 215, 0, 0.5)"
              fontSize="4"
              fontWeight="bold"
              fontFamily="sans-serif"
              textAnchor="middle"
              dominantBaseline="middle"
            >
              {houseId}
            </text>
          ))}
        </svg>
      </div>
    </div>
  );
};

// Export house center coordinates for absolute positioning of planets (relative to 800x800 container)
// These percentages correspond to the visual center of each house polygon.
export const KUNDLI_HOUSE_CENTERS = {
  1: { x: 50, y: 25 },
  2: { x: 25, y: 15 },
  3: { x: 15, y: 25 },
  4: { x: 25, y: 50 },
  5: { x: 15, y: 75 },
  6: { x: 25, y: 85 },
  7: { x: 50, y: 75 },
  8: { x: 75, y: 85 },
  9: { x: 85, y: 75 },
  10: { x: 75, y: 50 },
  11: { x: 85, y: 25 },
  12: { x: 75, y: 15 },
};
