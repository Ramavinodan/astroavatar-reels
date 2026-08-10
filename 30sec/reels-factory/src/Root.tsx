import "./index.css";
import { Composition } from "remotion";
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
    </>
  );
};
