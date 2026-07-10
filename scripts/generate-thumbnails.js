#!/usr/bin/env node
/*
 * Regenerate home subject-tile thumbnails (assets/images/Pages/Thumbnails/Files/*.jpeg)
 * from _data/categories.yml (subjects, in file order). Each tile = 1920×1080
 * diagonal gradient in the subject hue + a big translucent ORDER NUMBER baked
 * into the corner (01, 02, …). The home cards overlay the EN/KO names +
 * "Read more" in HTML, so NO title text is baked here.
 *
 * The number is the subject's running position in _data/categories.yml — exactly
 * the order the cards appear on the home page. (The order used to live in
 * _config.yml's categories-ko_order and then _data/home_sections.yml; both were
 * folded into _data/categories.yml.)
 *
 * USAGE:  npm i canvas js-yaml
 *         node scripts/generate-thumbnails.js              # 전부 다시 만든다
 *         node scripts/generate-thumbnails.js Toric_Geometry Mirror_Symmetry
 *                                                          # 지정한 타일만
 * 인자를 주면 그 파일명(확장자 제외)만 다시 그린다. 번호는 언제나 전체 순서
 * 기준이므로, 일부만 다시 그려도 나머지 타일과 어긋나지 않는다.
 *
 * Filenames are derived from the English subject name (the part after " / ")
 * with spaces → underscores, e.g. "Math / Algebraic Varieties" →
 * Algebraic_Varieties.jpeg. _includes/subject-grid.html references the same.
 */
const fs = require('fs');
const path = require('path');
const yaml = require('js-yaml');
const { createCanvas } = require('canvas');

const ROOT = path.join(__dirname, '..');
const OUT = path.join(ROOT, 'assets/images/Pages/Thumbnails/Files');
const data = yaml.load(fs.readFileSync(path.join(ROOT, '_data/categories.yml'), 'utf8'));
const hues = data.subjects;

// Numbering follows the master order in _data/categories.yml (= home grid order).
const order = Object.keys(hues);
// 인자가 있으면 그 타일만 (번호는 전체 순서 기준으로 유지).
const only = new Set(process.argv.slice(2).map((a) => a.replace(/\.jpeg$/, '')));
fs.mkdirSync(OUT, { recursive: true });

const W = 1920, H = 1080;
const FACE = 'Liberation Sans, Arial, sans-serif'; // fonts-liberation on Pi + CI
const NUMFACE = 'Liberation Serif, Georgia, "Times New Roman", serif'; // serif baked number

let n = 0;
order.forEach((key, i) => {
  const d = hues[key];
  if (!d) { console.warn('no hue for', key); return; }
  const num = String(i + 1).padStart(2, '0');
  const en = key.split(' / ').pop();
  const file = en.replace(/ /g, '_') + '.jpeg';
  if (only.size && !only.has(file.replace(/\.jpeg$/, ''))) return;

  const hue = d.hue;
  const sat = parseInt(d.sat, 10) + 6;
  const topL = Math.round((d.l || 44) * 0.5 + 8);
  const botL = topL - 14;

  const c = createCanvas(W, H);
  const g = c.getContext('2d');

  const lin = g.createLinearGradient(0, 0, W, H);
  lin.addColorStop(0, `hsl(${hue}, ${sat}%, ${topL}%)`);
  lin.addColorStop(1, `hsl(${hue}, ${sat}%, ${botL}%)`);
  g.fillStyle = lin; g.fillRect(0, 0, W, H);

  const rad = g.createRadialGradient(430, 250, 0, 430, 250, 1150);
  rad.addColorStop(0, `hsla(${hue}, ${sat}%, ${topL + 9}%, 0.5)`);
  rad.addColorStop(1, `hsla(${hue}, ${sat}%, ${topL}%, 0)`);
  g.fillStyle = rad; g.fillRect(0, 0, W, H);

  // big translucent order number, bottom-right (serif). Baseline pushes ~30%
  // of the glyph below the canvas so the card (background-position: bottom)
  // shows it with the lower third cropped.
  g.font = `bold 760px ${NUMFACE}`;
  g.textAlign = 'right';
  g.textBaseline = 'alphabetic';
  g.fillStyle = 'rgba(255,255,255,0.13)';
  g.fillText(num, W - 60, 1190);

  const buf = c.toBuffer('image/jpeg', { quality: 0.9 });
  fs.writeFileSync(path.join(OUT, file), buf);
  console.log('wrote', file, `(#${num}, hue ${hue})`);
  n++;
});
console.log('done —', n, 'tiles.');
