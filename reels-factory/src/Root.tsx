import "./index.css";
import { Composition } from "remotion";
import {
  GRAHA_MEETING_DURATION,
  GRAHA_MEETING_FPS,
  GRAHA_MEETING_SIZE,
  GrahaMeeting,
  grahaMeetingDefaults,
} from "./compositions/GrahaMeeting";
import {
  RAHU_KETU_DURATION,
  RAHU_KETU_FPS,
  RahuKetuOrigin,
  rahuKetuDefaults,
} from "./compositions/RahuKetuOrigin";
import {
  DailyDoseIntro,
  INTRO_FRAMES,
  INTRO_FPS,
  dailyDoseIntroDefaults,
} from "./compositions/DailyDoseIntro";
import type { GrahaMeetingProps } from "./graha/types";
import type { RahuKetuOriginProps } from "./compositions/RahuKetuOrigin";
import type { DailyDoseIntroProps } from "./compositions/DailyDoseIntro";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="DailyDoseIntro"
        component={DailyDoseIntro}
        durationInFrames={INTRO_FRAMES}
        fps={INTRO_FPS}
        width={1080}
        height={1920}
        defaultProps={dailyDoseIntroDefaults satisfies DailyDoseIntroProps}
      />
      <Composition
        id="GrahaMeeting"
        component={GrahaMeeting}
        durationInFrames={GRAHA_MEETING_DURATION}
        fps={GRAHA_MEETING_FPS}
        width={GRAHA_MEETING_SIZE.width}
        height={GRAHA_MEETING_SIZE.height}
        defaultProps={grahaMeetingDefaults satisfies GrahaMeetingProps}
      />
      <Composition
        id="RahuKetuOrigin"
        component={RahuKetuOrigin}
        durationInFrames={RAHU_KETU_DURATION}
        fps={RAHU_KETU_FPS}
        width={1080}
        height={1920}
        defaultProps={rahuKetuDefaults satisfies RahuKetuOriginProps}
      />
    </>
  );
};
