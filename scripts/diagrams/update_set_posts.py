import re
from pathlib import Path

widths = {
    'Functions-1': '12.56em',
    'Functions-2': '14.24em',
    'Functions-3': '9.84em',
    'Functions-4': '5.62em',
    'Functions-5': '5.62em',
    'Functions-6': '5.28em',
    'Retraction_and_Section-1': '5.54em',
    'Retraction_and_Section-2': '5.59em',
    'Retraction_and_Section-3': '5.94em',
    'Retraction_and_Section-4': '5.94em',
    'Sum_of_Sets-1': '13.49em',
    'Product_of_Sets-1': '6.00em',
    'Product_of_Sets-2': '13.37em',
    'Product_of_Sets-3': '13.03em',
    'Property_of_Products-1': '18.53em',
    'Property_of_Products-2': '24.93em',
    'Property_of_Products-3': '8.51em',
    'Property_of_Products-4': '17.00em',
    'Property_of_Products-5': '14.31em',
    'Property_of_Products-6': '16.81em',
    'Examples_of_Equivalence-2': '6.67em',
    'Examples_of_Equivalence-3': '12.57em',
    'Examples_of_Equivalence-4': '7.95em',
    'Examples_of_Equivalence-5': '6.57em',
    'Examples_of_Equivalence-6': '8.11em',
    'Examples_of_Equivalence-7': '18.05em',
    'Examples_of_Equivalence-8': '26.00em',
    'Examples_of_Equivalence-9': '20.50em',
    'Elements_in_Ordered_Set-1': '0.58em',
    'Elements_in_Ordered_Set-2': '6.04em',
    'Elements_in_Ordered_Set-3': '20.75em',
    'Limits-1': '12.45em',
    'Limits-2': '7.11em',
    'Limits-3': '13.58em',
    'Limits-4': '12.45em',
    'Directed_Set-1': '20.75em',
}

def repl(m):
    alt = m.group(1)
    name = m.group(2)
    rest = m.group(3)
    w = widths.get(name)
    if w is None:
        return m.group(0)
    return f'![{alt}](/assets/images/Math/Set_Theory/{name}.svg){{:style="width:{w}"{rest}'

posts_dir = Path('_posts/Math/Set_Theory')
for f in posts_dir.rglob('*.md'):
    text = f.read_text(encoding='utf-8')
    new_text = re.sub(
        r'!\[([^\]]*)\]\(/assets/images/Math/Set_Theory/([A-Za-z_][A-Za-z0-9_]*-\d+)\.png\)\{:style="width:[^"]*"([^}]*)\}',
        repl,
        text
    )
    # also handle {:width="...px"} form
    new_text = re.sub(
        r'!\[([^\]]*)\]\(/assets/images/Math/Set_Theory/([A-Za-z_][A-Za-z0-9_]*-\d+)\.png\)\{:width="[^"]*"([^}]*)\}',
        repl,
        new_text
    )
    if new_text != text:
        f.write_text(new_text, encoding='utf-8')
        print(f'updated {f}')

print('done')
