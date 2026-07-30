import "./index.css";
import { Composition } from "remotion";
import { RahuKetuFormatB } from "./compositions/formats/RahuKetuFormatB";
import {
  DynamicSlideshow,
  defaultDynamicSlideshowProps,
} from "./compositions/DynamicSlideshow";
import {
  DailyDoseIntro,
  INTRO_FRAMES,
  INTRO_FPS,
  dailyDoseIntroDefaults,
} from "./compositions/DailyDoseIntro";
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
        id="RahuKetuFormatB"
        component={RahuKetuFormatB}
        durationInFrames={1800}
        fps={30}
        width={1080}
        height={1920}
      />
      <Composition
        id="DynamicSlideshow"
        component={DynamicSlideshow}
        fps={30}
        width={1080}
        height={1920}
        defaultProps={defaultDynamicSlideshowProps}
        calculateMetadata={async ({ props }) => {
          const intro = props.introFrames ?? 120;
          const story = props.storyFrames ?? 1500;
          const end = props.endCardFrames ?? 150;
          return {
            durationInFrames: intro + story + end,
          };
        }}
      />
    </>
  );
};
