#!/usr/bin/env node
/*
 * Regenerate home subject-tile thumbnails (assets/images/Pages/Thumbnails/Files/*.jpeg)
 * from _data/hues.yml + _config.yml order. Each tile = 1920×1080 diagonal
 * gradient in the subject hue + a big translucent ORDER NUMBER baked into the
 * corner (01, 02, …, in categories-ko_order). The home cards overlay the
 * EN/KO names + "Read more" in HTML, so NO title text is baked here.
 *
 * USAGE:  npm i canvas js-yaml   then   node scripts/generate-thumbnails.js
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
const hues = yaml.load(fs.readFileSync(path.join(ROOT, '_data/hues.yml'), 'utf8'));
const config = yaml.load(fs.readFileSync(path.join(ROOT, '_config.yml'), 'utf8'));

// Numbering follows the KO category order (the canonical full list).
const order = config['categories-ko_order'] || [];
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
