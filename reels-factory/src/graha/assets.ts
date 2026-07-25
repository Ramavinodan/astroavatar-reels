import { staticFile } from "remotion";
import type { GrahaId } from "./types";

export const GRAHA_META: Record<
  GrahaId,
  { label: string; short: string; color: string; glow: string }
> = {
  surya: { label: "Surya", short: "Su", color: "#F0B429", glow: "rgba(240,180,41,0.55)" },
  chandra: { label: "Chandra", short: "Mo", color: "#C9D6E3", glow: "rgba(180,210,240,0.5)" },
  mangal: { label: "Mangal", short: "Ma", color: "#E85D04", glow: "rgba(232,93,4,0.55)" },
  budha: { label: "Budha", short: "Me", color: "#2D6A4F", glow: "rgba(45,160,90,0.5)" },
  guru: { label: "Guru", short: "Ju", color: "#E9C46A", glow: "rgba(233,196,106,0.55)" },
  shukra: { label: "Shukra", short: "Ve", color: "#E8D5C4", glow: "rgba(232,213,196,0.5)" },
  shani: { label: "Shani", short: "Sa", color: "#4A6FA5", glow: "rgba(74,111,165,0.55)" },
  rahu: { label: "Rahu", short: "Ra", color: "#7B2CBF", glow: "rgba(123,44,191,0.5)" },
  ketu: { label: "Ketu", short: "Ke", color: "#9C6644", glow: "rgba(156,102,68,0.5)" },
};

export const cutoutSrc = (id: GrahaId) => staticFile(`graha/${id}/cutout.png`);
export const portraitSrc = (id: GrahaId) => staticFile(`graha/${id}/portrait.png`);
