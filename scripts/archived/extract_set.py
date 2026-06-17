import re
from collections import OrderedDict, defaultdict
from pathlib import Path

src = Path('assets/diagrams/Math/Set_Theory/Set_theory.tex')
text = src.read_text(encoding='utf-8')

_, archive = text.split(r'\end{document}', 1)
lines = archive.splitlines()

# Mapping from scratch filename stem to (article, number)
mapping = {
    'Functions_1-1': ('Functions', 1),
    'Functions_1-2': ('Functions', 2),
    'Functions_1-3': ('Functions', 3),
    'Functions_1-4': ('Functions', 4),
    'Functions_1-5': ('Functions', 5),
    'Functions_1-6': ('Functions', 6),
    'Functions_2-1': ('Retraction_and_Section', 1),
    'Functions_2-2': ('Retraction_and_Section', 2),
    'Functions_2-3': ('Retraction_and_Section', 3),
    'Functions_2-4': ('Retraction_and_Section', 4),
    'Sum_of_sets-1': ('Sum_of_Sets', 1),
    'Product_of_sets-1': ('Product_of_Sets', 1),
    'Product_of_sets-2': ('Product_of_Sets', 2),
    'Product_of_sets-3': ('Product_of_Sets', 3),
    'Product_of_sets-4': ('Property_of_Products', 1),
    'Product_of_sets-5': ('Property_of_Products', 2),
    'Product_of_sets-6': ('Property_of_Products', 3),
    'Product_of_sets-7': ('Property_of_Products', 4),
    'Product_of_sets-8': ('Property_of_Products', 5),
    'Product_of_sets-9': ('Property_of_Products', 6),
    'Equivalence_relations-1': ('Examples_of_Equivalence', 2),
    'Equivalence_relations-2': ('Examples_of_Equivalence', 3),
    'Equivalence_relations-3': ('Examples_of_Equivalence', 4),
    'Equivalence_relations-4': ('Examples_of_Equivalence', 5),
    'Equivalence_relations-5': ('Examples_of_Equivalence', 6),
    'Equivalence_relations-6': ('Examples_of_Equivalence', 7),
    'Equivalence_relations-7': ('Examples_of_Equivalence', 8),
    'Equivalence_relations-8': ('Examples_of_Equivalence', 9),
    'Elements_in_ordered_set-1': ('Elements_in_Ordered_Set', 1),
    'Elements_in_ordered_set-2': ('Elements_in_Ordered_Set', 2),
    'Elements_in_ordered_set-3': ('Elements_in_Ordered_Set', 3),
    'Elements_in_ordered_set-4': ('Elements_in_Ordered_Set', 4),
    'Elements_in_ordered_set-5': ('Elements_in_Ordered_Set', 5),
    'Limits-1': ('Limits', 1),
    'Limits-2': ('Limits', 2),
    'Limits-3': ('Limits', 3),
    'Limits-4': ('Limits', 4),
}

figures = OrderedDict()
cur_key = None
cur_lines = []

for ln in lines:
    m = re.match(r'%\s*([A-Za-z_][A-Za-z0-9_]*-\d+)', ln)
    if m:
        if cur_key and cur_lines:
            figures.setdefault(cur_key, []).append(cur_lines)
        cur_key = m.group(1)
        cur_lines = []
    elif cur_key is not None:
        cur_lines.append(ln)

if cur_key and cur_lines:
    figures.setdefault(cur_key, []).append(cur_lines)

# choose last block if multiple
selected = {k: blocks[-1] for k, blocks in figures.items()}

def transform(line):
    # color substitutions
    line = re.sub(r'\bgray\b', 'black!50', line)
    line = re.sub(r'\bgray!(\d+)', r'black!\1', line)
    line = re.sub(r'\bred\b', 'accent1', line)
    line = re.sub(r'\bred!(\d+)', r'accent1!\1', line)
    line = re.sub(r'\bblue\b', 'accent2', line)
    line = re.sub(r'\bblue!(\d+)', r'accent2!\1', line)
    line = re.sub(r'\bgreen\b', 'accent3', line)
    line = re.sub(r'\bgreen!(\d+)', r'accent3!\1', line)
    line = re.sub(r'\bviolet\b', 'accent2', line)
    line = re.sub(r'\bviolet!(\d+)', r'accent2!\1', line)
    line = re.sub(r'\borange\b', 'accent1', line)
    line = re.sub(r'\borange!(\d+)', r'accent1!\1', line)
    return line

articles = defaultdict(list)
for stem, (art, num) in mapping.items():
    if stem not in selected:
        print(f'warning: {stem} not found in scratch')
        continue
    articles[art].append((num, selected[stem]))

# Also use Elements_in_ordered_set-3 for Directed_Set-1
if 'Elements_in_ordered_set-3' in selected:
    articles['Directed_Set'].append((1, selected['Elements_in_ordered_set-3']))

for art in articles:
    articles[art].sort(key=lambda x: x[0])

preamble = r'''\documentclass[border=2pt]{standalone}
\usepackage{amsmath, amsthm, amsfonts}
\usepackage{tikz-cd, kotex}
\usepackage{quiver}
\usepackage{Operators}
\usepackage{palette}
\usepackage{diagram-style}
\begin{document}

'''

out_dir = Path('assets/diagrams/Math/Set_Theory')
for art, figs in articles.items():
    body = []
    for num, fig_lines in figs:
        body.append(f'%%FIG diagram ({art}-{num}.svg)\n')
        for ln in fig_lines:
            body.append(transform(ln) + '\n')
    doc = preamble + ''.join(body) + r'\end{document}' + '\n'
    (out_dir / f'{art}.tex').write_text(doc, encoding='utf-8')
    print(f'wrote {art}.tex with {len(figs)} figures')

print('done')
