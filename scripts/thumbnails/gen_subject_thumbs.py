#!/usr/bin/env python3
"""Generate subject thumbnails for the home feature_row (option A).

Each thumbnail is a diagonal HSL gradient matching that subject's hero colour
(same hue/sat as _data/hues.yml, lightness 26%→13% like the subject hero) with
the English subject name centred in the site's sans-serif (Roboto, the Latin
fallback of the blog's $sans-serif). No reference/credit text.

Used ONLY as feature_row tile images; overwrites the existing .jpeg files.
Re-run after adding a subject (extend SUBJECTS below).
"""
import colorsys, os
import numpy as np
from PIL import Image, ImageDraw, ImageFont

OUT = "/home/junhyeok/math-jh.github.io/assets/images/Pages/Thumbnails/Files"
FONT = "/usr/share/fonts/truetype/roboto/unhinted/RobotoTTF/Roboto-Bold.ttf"
W, H = 1920, 1080

# filename(without .jpeg) -> (English title, hue, saturation%)
# hue/sat mirror _data/hues.yml. Algebraic_Geometry is the umbrella tile
# (links to algebraic_varieties → hue 9). Misc tiles are achromatic.
SUBJECTS = [
    ("Algebraic_Geometry",   "Algebraic Geometry",   9,   42),
    ("Algebraic_Structures", "Algebraic Structures", 204, 42),
    ("Algebraic_Topology",   "Algebraic Topology",   156, 42),
    ("Calculus",             "Calculus",             281, 42),
    ("Category_Theory",      "Category Theory",      306, 42),
    ("Commutative_Algebra",  "Commutative Algebra",  231, 42),
    ("Field_Theory",         "Field Theory",         222, 42),
    ("Group_Theory",         "Group Theory",         209, 42),
    ("Homological_Algebra",  "Homological Algebra",  227, 42),
    ("Linear_Algebra",       "Linear Algebra",       249, 42),
    ("Manifold",             "Manifolds",            84,  42),
    ("Multilinear_Algebra",  "Multilinear Algebra",  218, 42),
    ("Riemannian_Geometry",  "Riemannian Geometry",  116, 42),
    ("Ring_Theory",          "Ring Theory",          213, 42),
    ("Set_Theory",           "Set Theory",           274, 42),
    ("Symplectic_Geometry",  "Symplectic Geometry",  1,   42),
    ("Topology",             "Topology",             124, 42),
    ("Blog_Development",     "Blog Development",      0,   0),
    ("Peripherals",          "Peripherals",          0,   0),
]


def hsl_rgb(hue, sat, light):
    """hsl(hue°, sat%, light%) -> (r,g,b) 0..255, matching CSS HSL."""
    r, g, b = colorsys.hls_to_rgb(hue / 360.0, light / 100.0, sat / 100.0)
    return np.array([r * 255, g * 255, b * 255])


def gradient(hue, sat):
    """135°-ish diagonal: lighter (L26) top-left → darker (L13) bottom-right,
    interpolated in sRGB like CSS linear-gradient."""
    start = hsl_rgb(hue, sat, 26)
    end = hsl_rgb(hue, sat, 13)
    yy, xx = np.mgrid[0:H, 0:W]
    t = (xx + yy) / (W + H - 2)            # 0 top-left .. 1 bottom-right
    arr = start[None, None, :] * (1 - t)[..., None] + end[None, None, :] * t[..., None]
    arr += np.random.normal(0, 1.3, arr.shape)   # dither to kill JPEG banding
    return Image.fromarray(np.clip(arr, 0, 255).astype("uint8"), "RGB")


def fit_font(draw, lines, max_w, max_h):
    """Largest Roboto-Bold size where every line fits max_w and the block fits max_h."""
    size = 320
    while size > 20:
        font = ImageFont.truetype(FONT, size)
        line_h = font.getbbox("Hg")[3] - font.getbbox("Hg")[1]
        gap = int(line_h * 0.18)
        widths = [draw.textlength(ln, font=font) for ln in lines]
        block_h = line_h * len(lines) + gap * (len(lines) - 1)
        if max(widths) <= max_w and block_h <= max_h:
            return font, line_h, gap
        size -= 4
    return ImageFont.truetype(FONT, 20), 24, 4


def render(title):
    # 1 word → 1 line; 2+ words → one word per line (visually balanced on 16:9)
    words = title.split()
    return words if len(words) >= 2 else [title]


def main():
    os.makedirs(OUT, exist_ok=True)
    for fname, title, hue, sat in SUBJECTS:
        img = gradient(hue, sat)
        draw = ImageDraw.Draw(img)
        lines = render(title)
        font, line_h, gap = fit_font(draw, lines, int(W * 0.80), int(H * 0.62))
        block_h = line_h * len(lines) + gap * (len(lines) - 1)
        y = (H - block_h) / 2
        for ln in lines:
            tw = draw.textlength(ln, font=font)
            # subtle shadow for legibility on the gradient, then white text
            draw.text(((W - tw) / 2 + 3, y + 3), ln, font=font, fill=(0, 0, 0, 90))
            draw.text(((W - tw) / 2, y), ln, font=font, fill=(245, 245, 245))
            y += line_h + gap
        path = os.path.join(OUT, fname + ".jpeg")
        img.save(path, "JPEG", quality=92)
        print(f"  {fname:24s} hue={hue:>3} sat={sat}%  -> {path}")


if __name__ == "__main__":
    main()
