// news-image-20261120 — entry program (Node 22, standard library only).
// It copies entry.png from the repository root to /output/entry.png.
// That is all it has to do: the image itself is the entry, a newspaper
// front page summing up Friday 20 November 2026, drawn by gen.py.
//
// Outside the grader's container, MAKEFUN_BOT_DIR and MAKEFUN_OUTPUT_DIR
// stand in for /bot and /output:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? "/bot";
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

mkdirSync(OUTPUT_DIR, { recursive: true });
try {
  copyFileSync(join(BOT_DIR, "entry.png"), join(OUTPUT_DIR, "entry.png"));
} catch (err) {
  console.error(`entry.png could not be copied from ${BOT_DIR}: ${(err).message}`);
  process.exit(1);
}
