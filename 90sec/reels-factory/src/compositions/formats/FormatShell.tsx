/**
 * Shared episode shell: welcome + story audio + end card.
 * Story visual is injected as children of the story Sequence.
 */
import React from "react";
import {
  AbsoluteFill,
  Audio,
  OffthreadVideo,
  Sequence,
  staticFile,
} from "remotion";
import { DailyDoseIntro } from "../DailyDoseIntro";
import {
  END_CARD_FRAMES,
  INTRO_FRAMES,
  STORY_FILE,
  STORY_FRAMES,
  WELCOME_FILE,
} from "../../timing/rahuKetuTiming";

export type FormatShellProps = {
  narrationFile?: string;
  endCardFile?: string;
  children: React.ReactNode;
};

export const FormatShell: React.FC<FormatShellProps> = ({
  narrationFile = STORY_FILE,
  endCardFile = "end_card.mp4",
  children,
}) => {
  const storyFrom = INTRO_FRAMES;
  const endFrom = INTRO_FRAMES + STORY_FRAMES;

  return (
    <AbsoluteFill style={{ background: "#04060c" }}>
      <Sequence from={0} durationInFrames={INTRO_FRAMES}>
        <DailyDoseIntro narrationFile={WELCOME_FILE} />
      </Sequence>

      <Sequence from={storyFrom} durationInFrames={STORY_FRAMES}>
        <Audio src={staticFile(narrationFile)} />
        {children}
      </Sequence>

      <Sequence from={endFrom} durationInFrames={END_CARD_FRAMES}>
        <AbsoluteFill style={{ background: "#000" }}>
          <OffthreadVideo
            src={staticFile(endCardFile)}
            style={{ width: "100%", height: "100%", objectFit: "cover" }}
          />
        </AbsoluteFill>
      </Sequence>
    </AbsoluteFill>
  );
};

/** On-screen format badge for manager comparison (top-left). */
export const FormatBadge: React.FC<{ label: string; fontFamily: string }> = ({
  label,
  fontFamily,
}) => (
  <div
    style={{
      position: "absolute",
      top: 36,
      left: 28,
      zIndex: 40,
      padding: "8px 14px",
      borderRadius: 8,
      background: "rgba(0,0,0,0.72)",
      border: "1px solid rgba(233,196,106,0.55)",
      color: "#E9C46A",
      fontSize: 22,
      fontWeight: 700,
      fontFamily,
      letterSpacing: 0.5,
    }}
  >
    {label}
  </div>
);
