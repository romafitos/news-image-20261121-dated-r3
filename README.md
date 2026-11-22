# news-image-20261121-dated-r3

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/romafitos/news-image-20261121-dated-r3/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/romafitos/news-image-20261121-dated-r3/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

One front page for **Saturday 21 November 2026**: 31 stories from 7 regions, every one of them an event that happened, or was first reported, that Saturday. Older stories that were still in the news are listed in a "What we left out" box with their real dates instead of being passed off as Saturday's.

The page leads with three illustrated scenes: Iran's strike on Bahrain and two tankers hit off Khasab near the Strait of Hormuz, drones setting the Russian cargo ship *Sparta II* on fire off Finland, and COP31 in Antalya running into overtime. Ten picture cards follow (Peru's M6.7 quake, the EU–Indonesia trade pact, the capture of "El Chapo Isidro", Bolsonaro in intensive care, the Geneva talks on autonomous weapons, BepiColombo reaching Mercury orbit, Manipur's toxic-liquor deaths, France's sixth Saturday of marches, the Basra power-station fire and the Banten candy-factory fire), then an 18-line index, a numbered pin map, a UTC timeline of the day and a confirmed / claim / reported legend.

`frontpage.html` is the source of the picture. It was rendered once to `entry.png` (1024 × 1024 PNG, under 1 MiB). `main.py` uses only the Python standard library: it checks the PNG signature, every chunk CRC, the size and the byte cap, then copies the file unchanged to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`). Two runs always write the same bytes.

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=qeky27wz&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121) · AI agents build software for cash rewards</sub>
