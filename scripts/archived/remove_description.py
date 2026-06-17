from pathlib import Path

files = [
    Path('/home/junhyeok/math-jh.github.io/assets/diagrams/Math/Category_Theory/Limits.tex'),
    Path('/home/junhyeok/math-jh.github.io/assets/diagrams/Math/Scheme_Theory/Affine_Schemes.tex'),
]

for p in files:
    text = p.read_text(encoding='utf-8')
    new_text = text.replace('{description}', '').replace('" description', '"')
    if new_text != text:
        p.write_text(new_text, encoding='utf-8')
        print(f'fixed {p}')
    else:
        print(f'no change {p}')

print('done')
