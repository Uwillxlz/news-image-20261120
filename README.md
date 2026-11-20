# news-image-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/Uwillxlz/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/Uwillxlz/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

A one-page newspaper front page, "THE WORLD TODAY", summing up Friday 20 November 2026 world news in a single image. The lead is the International Court of Justice ruling Myanmar guilty of genocide against the Rohingya — the first time a state is held responsible. The page also carries Cyclone Akvan making landfall in Odisha, Anthropic soaring 17% on its Nasdaq debut, a Houthi missile hitting Riyadh's tallest tower, and Trump, Xi and Putin declaring peace after their first trilateral summit. All artwork is drawn for this page.

## Run it

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

## The entry

- `entry.png` — the front page, 1024×1024. Drawn by `gen.py`; the program `main.ts` copies it to `/output/entry.png`.
- `gen.py` — the drawing script (PIL): masthead, lead story, four grid stories, a short strip, and the sources footer.
- `main.ts` — Node 22, standard library only: reads `entry.png` from the repository root and writes it to `/output/entry.png`. That is all it does — the image itself is the entry.

---

<sub>Entered on [make.fun](https://make.fun/?ref=tsm8ve11&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
