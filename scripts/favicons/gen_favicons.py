#!/usr/bin/env python3
"""Generate the full favicon / app-icon set as the brand mark: a navy tile with
a centered brass open square ("the black box"). Same mark as the inline SVG tab
favicon in _includes/head.html.

Mark (32-unit grid): navy tile, open square x8..24 brass stroke w3. 색의 단일
출처는 _data/brand.yml. Everything is drawn directly with PIL (supersampled for
clean edges) — no SVG rasteriser needed. Re-run after a brand-colour change.

Outputs to assets/favicons/: favicon-16/32, favicon.ico, apple-touch-icon (180),
android-chrome-192/512, mstile-150. safari-pinned-tab.svg 는 수동 관리(모노크롬
마스크라 색은 head/custom.html 의 mask-icon color 가 정한다), site.webmanifest
는 Liquid 가 brand.yml 을 직접 읽는다.
"""
import os

import yaml
from PIL import Image, ImageDraw

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "assets", "favicons")
_BRAND = yaml.safe_load(open(os.path.join(
    os.path.dirname(__file__), "..", "..", "_data", "brand.yml"), encoding="utf-8"))


def _rgb(hexstr: str) -> tuple:
    h = hexstr.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


NAVY = _rgb(_BRAND["navy"])
BRASS = _rgb(_BRAND["brass"])
SS = 8                  # supersample factor for anti-aliasing


def mark(size):
    """Brass open-box mark at `size`px (opaque navy bg, no transparency)."""
    S = size * SS
    img = Image.new("RGB", (S, S), NAVY)
    d = ImageDraw.Draw(img)
    s = S / 32.0
    x0, x1 = 8 * s, 24 * s          # open square spans 8..24 on the 32 grid
    w = max(1, round(3 * s))        # stroke width 3 on the 32 grid
    d.rectangle([x0, x0, x1, x1], outline=BRASS, width=w)
    return img.resize((size, size), Image.LANCZOS)


def main():
    os.makedirs(OUT, exist_ok=True)
    png = {
        "favicon-16x16.png": 16,
        "favicon-32x32.png": 32,
        "apple-touch-icon.png": 180,
        "android-chrome-192x192.png": 192,
        "android-chrome-512x512.png": 512,
        "mstile-150x150.png": 150,
    }
    for name, sz in png.items():
        mark(sz).save(os.path.join(OUT, name))
        print("wrote", name, f"({sz}x{sz})")
    # multi-size .ico from a crisp 64px master
    mark(64).save(os.path.join(OUT, "favicon.ico"),
                  sizes=[(16, 16), (32, 32), (48, 48)])
    print("wrote favicon.ico (16/32/48)")


if __name__ == "__main__":
    main()
