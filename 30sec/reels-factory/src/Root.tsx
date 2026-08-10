import "./index.css";
import { Composition } from "remotion";
import { RahuKetuFormatB } from "./compositions/formats/RahuKetuFormatB";
import {
  DynamicSlideshow,
  defaultDynamicSlideshowProps,
} from "./compositions/DynamicSlideshow";
import {
  PremiumIntro,
  INTRO_FRAMES,
  INTRO_FPS,
  premiumIntroDefaults,
} from "./compositions/PremiumIntro";
import type { PremiumIntroProps } from "./compositions/PremiumIntro";

import { DynamicKundli } from "./compositions/DynamicKundli";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="DynamicKundli"
        component={DynamicKundli}
        durationInFrames={616}
        fps={30}
        width={1080}
        height={1920}
      />
      <Composition
        id="DailyDoseIntro"
        component={PremiumIntro}
        durationInFrames={INTRO_FRAMES}
        fps={INTRO_FPS}
        width={1080}
        height={1920}
        defaultProps={premiumIntroDefaults satisfies PremiumIntroProps}
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
