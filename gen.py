#!/usr/bin/env python3
"""Draw the 20 November 2026 front page for news-image-20261120.

A newspaper front page, 1024x1024, drawn with PIL only: no network, no
randomness, no timestamps, so the output is byte-identical on every run.
Run:  python3 gen.py   (writes entry.png in this directory)
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (248, 243, 232)
INK = (20, 20, 20)
RED = (160, 30, 30)
GREY = (107, 100, 85)
RULE = (20, 20, 20)
NAVY = (30, 44, 74)
GOLD = (201, 162, 39)
TEAL = (47, 168, 160)
DARKBLUE = (20, 50, 74)
DARKGREEN = (18, 58, 36)
PALE = (223, 227, 230)

SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF_R = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS_R = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Wrap text to lines that fit max_w pixels."""
    lines, cur = [], ""
    for word in text.split(" "):
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, lines, fnt, fill, leading):
    for i, line in enumerate(lines):
        draw.text((x, y + i * leading), line, font=fnt, fill=fill)
    return y + len(lines) * leading


def centre(draw, y, text, fnt, fill):
    w = draw.textlength(text, font=fnt)
    draw.text(((W - w) / 2, y), text, font=fnt, fill=fill)


# ---------------------------------------------------------------- illustrations
def draw_scales(draw, x0, y0, x1, y1):
    """Courthouse columns with golden scales of justice, full-width band."""
    draw.rectangle([x0, y0, x1, y1], fill=PALE)
    # ground band
    draw.rectangle([x0, y1 - 14, x1, y1], fill=NAVY)
    # pediment, apex up, centred over the middle columns
    cx = (x0 + x1) // 2
    draw.polygon([(cx - 230, y0 + 32), (cx + 230, y0 + 32), (cx, y0 + 6)],
                 fill=NAVY)
    # entablature band under the pediment, same width
    draw.rectangle([cx - 230, y0 + 32, cx + 230, y0 + 40], fill=NAVY)
    # columns, wider and taller
    for i in range(6):
        cx0 = x0 + 52 + i * 152
        draw.rectangle([cx0, y0 + 40, cx0 + 40, y1 - 14], fill=(239, 230, 204),
                       outline=NAVY, width=2)
    # scales of justice, large, centred, in front of the columns
    sx, sy = cx, y0 + 48
    draw.line([sx, sy, sx, sy + 56], fill=GOLD, width=7)
    draw.line([sx - 58, sy + 8, sx + 58, sy + 8], fill=GOLD, width=6)
    for dx in (-58, 58):
        draw.line([sx + dx, sy + 8, sx + dx, sy + 34], fill=GOLD, width=3)
        draw.polygon([(sx + dx - 20, sy + 34), (sx + dx + 20, sy + 34),
                      (sx + dx, sy + 52)], fill=GOLD)
    draw.ellipse([sx - 8, sy - 9, sx + 8, sy + 7], fill=GOLD)
    draw.rectangle([sx - 26, sy + 56, sx + 26, sy + 62], fill=GOLD)


def draw_cyclone(draw, x0, y0, x1, y1):
    """Cyclone spiral on a dark sea."""
    draw.rectangle([x0, y0, x1, y1], fill=DARKBLUE)
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
    for r, col, wd in ((46, (255, 255, 255), 5), (36, TEAL, 5),
                       (26, (255, 255, 255), 4), (16, TEAL, 4)):
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=col, width=wd)
    draw.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=(214, 48, 48))


def draw_chart(draw, x0, y0, x1, y1):
    """Rising market chart with bars."""
    draw.rectangle([x0, y0, x1, y1], fill=DARKGREEN)
    # bars
    bw, gap = 16, 10
    heights = (26, 40, 56)
    for i, h in enumerate(heights):
        bx = x0 + 14 + i * (bw + gap)
        draw.rectangle([bx, y1 - 14 - h, bx + bw, y1 - 14], fill=GOLD)
    # rising line with arrowhead
    pts = [(x0 + 12, y1 - 30), (x0 + 34, y1 - 52), (x0 + 58, y1 - 44),
           (x0 + 82, y1 - 72), (x0 + 100, y1 - 84)]
    draw.line(pts, fill=(255, 255, 255), width=4, joint="curve")
    ax, ay = pts[-1]
    draw.polygon([(ax, ay - 12), (ax + 12, ay + 2), (ax - 2, ay + 8)],
                 fill=(255, 255, 255))
    draw.text((x0 + 8, y0 + 6), "+17%", font=font(SANS_B, 20),
              fill=(255, 255, 255))


def draw_tower(draw, x0, y0, x1, y1):
    """Skyscraper at dusk with broken windows near the top."""
    draw.rectangle([x0, y0, x1, y1], fill=(43, 43, 58))
    draw.rectangle([x0, y1 - 18, x1, y1], fill=(201, 106, 58))
    tx0, tx1 = x0 + 34, x1 - 34
    draw.rectangle([tx0, y0 + 10, tx1, y1 - 18], fill=(28, 34, 51))
    # lit windows
    for r in range(6):
        for c in range(3):
            wx = tx0 + 8 + c * 14
            wy = y0 + 20 + r * 13
            draw.rectangle([wx, wy, wx + 7, wy + 6], fill=GOLD)
    # broken windows: red jagged marks near the top
    for (bx, by) in ((tx0 + 8, y0 + 20), (tx0 + 36, y0 + 33),
                     (tx0 + 22, y0 + 46)):
        draw.line([(bx, by), (bx + 5, by + 5), (bx + 10, by),
                   (bx + 5, by + 8)], fill=(214, 48, 48), width=2)


def draw_flags(draw, x0, y0, x1, y1):
    """Three flags side by side: US, China, Russia."""
    w = (x1 - x0) // 3
    # US: stripes + canton
    draw.rectangle([x0, y0, x0 + w, y1], fill=(255, 255, 255))
    for i in range(7):
        if i % 2 == 0:
            draw.rectangle([x0, y0 + i * (y1 - y0) // 7,
                            x0 + w, y0 + (i + 1) * (y1 - y0) // 7],
                           fill=(178, 34, 52))
    draw.rectangle([x0, y0, x0 + w // 2, y0 + (y1 - y0) * 4 // 7],
                   fill=(60, 59, 110))
    for r in range(3):
        for c in range(3):
            draw.ellipse([x0 + 5 + c * 7, y0 + 6 + r * 12,
                          x0 + 9 + c * 7, y0 + 10 + r * 12],
                         fill=(255, 255, 255))
    # China: red field, gold stars
    cx0 = x0 + w
    draw.rectangle([cx0, y0, cx0 + w, y1], fill=(222, 41, 16))
    draw.polygon([(cx0 + 14, y0 + 12), (cx0 + 18, y0 + 22), (cx0 + 28, y0 + 22),
                  (cx0 + 20, y0 + 28), (cx0 + 23, y0 + 38), (cx0 + 14, y0 + 32),
                  (cx0 + 5, y0 + 38), (cx0 + 8, y0 + 28), (cx0, y0 + 22),
                  (cx0 + 10, y0 + 22)], fill=GOLD)
    # Russia: white / blue / red bands
    rx0 = x0 + 2 * w
    h3 = (y1 - y0) // 3
    draw.rectangle([rx0, y0, rx0 + w, y0 + h3], fill=(255, 255, 255))
    draw.rectangle([rx0, y0 + h3, rx0 + w, y0 + 2 * h3], fill=(0, 57, 166))
    draw.rectangle([rx0, y0 + 2 * h3, rx0 + w, y1], fill=(213, 0, 50))


# ---------------------------------------------------------------- page
def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 44                      # side margin
    CW = W - 2 * M              # content width

    # masthead
    centre(d, 26, "THE WORLD TODAY", font(SERIF_B, 66), INK)
    centre(d, 100, "FRIDAY 20 NOVEMBER 2026", font(SANS_B, 25), RED)
    centre(d, 132, "THE DAY'S WORLD NEWS — IN ONE PAGE",
           font(SANS_R, 15), GREY)
    d.line([M, 156, W - M, 156], fill=RULE, width=3)
    d.line([M, 163, W - M, 163], fill=RULE, width=1)

    # ---- lead: ICJ
    d.text((M, 178), "THE HAGUE  ·  WORLD COURT",
           font=font(SANS_B, 19), fill=RED)
    d.text((M, 204), "MYANMAR GUILTY", font=font(SERIF_B, 76), fill=INK)
    d.text((M, 288), "OF GENOCIDE", font=font(SERIF_B, 76), fill=INK)
    deck = ("The International Court of Justice rules Myanmar committed "
            "genocide against the Rohingya — the first time a state is held "
            "responsible. Some 10,000 killed in 2017; reparations ordered.")
    text_block(d, M, 384, wrap(d, deck, font(SERIF_R, 24), CW),
               font(SERIF_R, 24), INK, 30)
    draw_scales(d, M, 472, W - M, 592)
    d.line([M, 606, W - M, 606], fill=RULE, width=2)

    # ---- grid: 2 x 2
    stories = [
        ("WEATHER  ·  SOUTH ASIA", "CYCLONE AKVAN MAKES LANDFALL",
         "Crosses the coast near Gopalpur at noon, winds to 110 km/h; "
         "300,000+ evacuated.",
         draw_cyclone),
        ("BUSINESS  ·  TECH", "ANTHROPIC SOARS 17% ON DEBUT",
         "Shares close at $97.17 after the $81.3bn IPO — the largest ever "
         "— having opened at $111.50.", draw_chart),
        ("MIDDLE EAST  ·  CONFLICT", "MISSILE HITS RIYADH'S TALLEST TOWER",
         "A Houthi missile strikes the 80-storey PIF Tower; windows blown "
         "out on 7–8 floors. No injuries.", draw_tower),
        ("ASIA  ·  DIPLOMACY", "TRUMP, XI, PUTIN DECLARE PEACE",
         "First trilateral summit ends with a joint declaration on peace; "
         "Ukraine first on the agenda.", draw_flags),
    ]
    row_y = [622, 772]
    col_x = [M, M + CW // 2 + 12]
    for i, (kick, head, body, art) in enumerate(stories):
        x = col_x[i % 2]
        y = row_y[i // 2]
        art(d, x, y + 6, x + 108, y + 114)
        tx = x + 122
        tw = CW // 2 - 134
        d.text((tx, y), kick, font=font(SANS_B, 15), fill=RED)
        text_block(d, tx, y + 22,
                   wrap(d, head, font(SERIF_B, 26), tw),
                   font(SERIF_B, 26), INK, 30)
        hl = wrap(d, head, font(SERIF_B, 26), tw)
        by = y + 22 + len(hl) * 30 + 4
        text_block(d, tx, by, wrap(d, body, font(SERIF_R, 17), tw),
                   font(SERIF_R, 17), INK, 21)
    d.line([W // 2, 622, W // 2, 912], fill=(180, 172, 150), width=1)
    d.line([M, 762, W - M, 762], fill=(180, 172, 150), width=1)

    # ---- strip
    d.line([M, 926, W - M, 926], fill=RULE, width=2)
    d.text((M, 938), "ALSO ON FRIDAY", font=font(SANS_B, 16), fill=RED)
    strip = ("Trump pardons Pete Rose  ·  Australia, Canada, Italy and the "
             "UK urge Gaza aid access as floods hit")
    text_block(d, M, 960, wrap(d, strip, font(SERIF_R, 17), CW),
               font(SERIF_R, 17), INK, 21)

    # ---- footer
    d.text((M, 996), "Sources: UN News · Reuters · The Wall Street Journal · "
           "India Meteorological Dept. · Nasdaq",
           font=font(SANS_R, 13), fill=GREY)
    ft = "All artwork drawn for this page"
    d.text((W - M - d.textlength(ft, font=font(SANS_R, 13)), 996), ft,
           font=font(SANS_R, 13), fill=GREY)

    img.save("entry.png")


if __name__ == "__main__":
    main()
