import type { HouseNumber } from "./types";

export type Point = { x: number; y: number };

/**
 * Approximate house centers for a North-Indian style diamond chart.
 * Coordinates are 0–1 within the chart square (top-left origin).
 */
const HOUSE_CENTERS: Record<HouseNumber, Point> = {
  1: { x: 0.5, y: 0.22 },
  2: { x: 0.72, y: 0.28 },
  3: { x: 0.78, y: 0.5 },
  4: { x: 0.72, y: 0.72 },
  5: { x: 0.5, y: 0.78 },
  6: { x: 0.28, y: 0.72 },
  7: { x: 0.22, y: 0.5 },
  8: { x: 0.28, y: 0.28 },
  9: { x: 0.38, y: 0.38 },
  10: { x: 0.62, y: 0.38 },
  11: { x: 0.62, y: 0.62 },
  12: { x: 0.38, y: 0.62 },
};

/** Classic North Indian house order around the diamond (visual labels). */
export const HOUSE_LABELS: HouseNumber[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];

export const houseCenter = (house: HouseNumber): Point => HOUSE_CENTERS[house];

export const toChartPixel = (
  p: Point,
  chart: { left: number; top: number; size: number },
): Point => ({
  x: chart.left + p.x * chart.size,
  y: chart.top + p.y * chart.size,
});

/** Sensible default fly-in origins when not specified. */
export const defaultOrigins = (
  house: HouseNumber,
  count: number,
): HouseNumber[] => {
  const opposite = ((((house - 1 + 6) % 12) + 1) as HouseNumber);
  const near = ((((house - 1 + 3) % 12) + 1) as HouseNumber);
  const far = ((((house - 1 + 9) % 12) + 1) as HouseNumber);
  return [opposite, near, far].slice(0, count) as HouseNumber[];
};
