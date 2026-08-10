import "./index.css";
import { Composition } from "remotion";
import { YashKundli } from "./compositions/YashKundli";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="YashKundli"
        component={YashKundli}
        durationInFrames={1232}
        fps={30}
        width={1080}
        height={1920}
      />
    </>
  );
};
