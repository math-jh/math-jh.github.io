#!/usr/bin/env python3
r"""미분 d 후보를 추출해 AUTO / MATHOP / AMBIG / SKIP 으로 분류한다.

파일을 쓰지 않는다. 결과는 JSONL (stdout 또는 -o).
치환 자체는 dd_apply.py 가 한다 — 이 스크립트는 후보 목록만 만든다.

마스킹: code fence, inline code, ``:::`` 여는 줄, \text{}·\operatorname{} 등
텍스트 인자. 그 바깥의 $...$ / $$...$$ 안만 후보로 본다.
"""
import argparse, glob, json, os, re, sys

FENCE = re.compile(r'^(```|~~~)')
TEXTARG = re.compile(
    r'\\(?:text|textnormal|textrm|textit|textbf|operatorname\*?|mathrm|mathbf'
    r'|mathsf|mathtt|mathcal|mathbb|mathfrak|label|tag|href|url|begin|end)'
    r'\{[^{}]*\}')

def dtokens(body):
    r"""수식 본문에서 '홀로 선 d' 의 offset 목록.

    정규식 lookbehind 로는 \tilde·\prod 처럼 **매크로 이름 안의 d** 를 걸러낼 수
    없다 (\prod( 가 'd(' 로 보인다). 그래서 토큰 단위로 훑는다.
    """
    out, i, n = [], 0, len(body)
    while i < n:
        if body[i] == '\\':
            m = re.match(r'\\[A-Za-z]+|\\.', body[i:])
            i += m.end() if m else 1
            continue
        if body[i] == 'd':
            out.append(i)
        i += 1
    return out

GREEK = (r'mu|nu|theta|vartheta|phi|varphi|psi|omega|sigma|varsigma|tau|rho|varrho'
         r'|lambda|alpha|beta|gamma|delta|zeta|xi|eta|chi|epsilon|varepsilon|kappa'
         r'|iota|pi|varpi|upsilon|Omega|Theta|Phi|Psi|Sigma|Lambda|Delta|Gamma|Xi|Pi')
ACCENT = r'bar|tilde|hat|overline|widetilde|widehat|vec|dot|ddot|check|breve'
# d 뒤에 오면 그 d 는 변수라는 확실한 신호
NOTDIFF = (r'\\(?:in|notin|ni|mid|nmid|to|rightarrow|Rightarrow|leftarrow|mapsto'
           r'|geq|leq|ge|le|neq|ne|equiv|cong|sim|simeq|approx|subseteq|subset'
           r'|supseteq|supset|cdot|cdots|ldots|dots|vdots|times|otimes|oplus|wedge'
           r'|vee|cup|cap|pm|mp|quad|qquad|colon|right|left|big|Big|bigg|Bigg|land'
           r'|lor|circ|ast|star|bullet|leqslant|geqslant|vert|lvert|rvert|Vert'
           r'|end|begin|text|over|choose|atop|hspace|;|,|!|:|\\)')


def math_spans(text):
    """(치환 가능한) 수식 영역 [(start, end)] 를 원문 offset 기준으로 돌려준다."""
    src = list(text)
    infence = False
    pos = 0
    for line in text.split('\n'):
        n = len(line)
        if FENCE.match(line.strip()):
            infence = not infence
            for i in range(pos, pos + n):
                src[i] = '\0'
        elif infence or line.startswith(':::'):
            for i in range(pos, pos + n):
                src[i] = '\0'
        pos += n + 1
    t = ''.join(src)
    t = re.sub(r'`[^`\n]*`', lambda m: '\0' * len(m.group(0)), t)

    spans = []
    for m in re.finditer(r'\$\$(.+?)\$\$', t, re.S):
        if '\0' in m.group(0):
            continue
        spans.append((m.start(1), m.end(1), True))
    blocked = list(t)
    for a, b, _ in spans:
        for i in range(max(0, a - 2), min(b + 2, len(blocked))):
            blocked[i] = '\0'
    for m in re.finditer(r'(?<!\$)\$([^$\n]+?)\$(?!\$)', ''.join(blocked)):
        if '\0' in m.group(0):
            continue
        spans.append((m.start(1), m.end(1), False))
    return sorted(spans)


def operand(body, i):
    r"""body[i] == 'd' 일 때 피연산자의 끝 offset. 없으면 None.

    원자 = \매크로(+악센트면 {..} 인자) | 라틴 한 글자 | 균형 잡힌 (...)
    뒤따르는 아래첨자 한 덩어리는 포함한다 (코퍼스의 \mathop{dx_1} 관례).
    위첨자는 포함하지 않는다 ((dx)^2 와 dx^2 의 뜻이 갈리므로).
    """
    j = i + 1
    if j >= len(body):
        return None
    c = body[j]
    if c == '\\':
        m = re.match(r'\\[A-Za-z]+', body[j:])
        if not m:
            return None
        j += m.end()
        if re.fullmatch(r'\\(?:%s)' % ACCENT, m.group(0)):
            if j < len(body) and body[j] == '{':
                j = balanced(body, j, '{', '}')
                if j is None:
                    return None
            else:
                return None
    elif c.isalpha():
        j += 1
    elif c == '(':
        j = balanced(body, j, '(', ')')
        if j is None:
            return None
    else:
        return None
    # 아래첨자 한 덩어리
    if j < len(body) and body[j] == '_':
        k = j + 1
        if k < len(body) and body[k] == '{':
            k = balanced(body, k, '{', '}')
            if k is None:
                return j
            j = k
        elif k < len(body) and (body[k].isalnum()):
            j = k + 1
        elif k < len(body) and body[k] == '\\':
            m = re.match(r'\\[A-Za-z]+', body[k:])
            if m:
                j = k + m.end()
                # \mathcal{L} 처럼 인자를 받는 매크로면 그 인자까지 포함해야 한다
                # (안 그러면 d\varphi_\mathcal{L} -> \dd{\varphi_\mathcal}{L})
                if j < len(body) and body[j] == '{':
                    j2 = balanced(body, j, '{', '}')
                    if j2 is None:
                        return None
                    j = j2
    return j


def balanced(s, i, op, cl):
    depth = 0
    for k in range(i, len(s)):
        if s[k] == op:
            depth += 1
        elif s[k] == cl:
            depth -= 1
            if depth == 0:
                return k + 1
    return None


def classify(body, i, end):
    """AUTO / AMBIG / SKIP 중 하나."""
    before = body[:i]
    after = body[i + 1:i + 18]
    if before[-1:] in ('^', '_'):
        return 'SKIP', '^d / _d (지수·첨자)'
    if re.match(NOTDIFF, after):
        return 'SKIP', 'd + 관계·이항 매크로'
    if re.match(r'[A-Za-z]{2,}', after):
        return 'SKIP', 'd + 여러 글자'
    if after[:1] in ('_', '^'):
        return 'SKIP', 'd_ / d^'
    # 앞에 글자가 붙은 d (fd\x, Bd\y) 도 미분일 수 있다. 다만 계수인지
    # 두 글자 식별자인지 기계로 못 가르므로 AUTO 에서는 빼고 AMBIG 로 넘긴다.
    coeff = bool(re.search(r'[A-Za-z]$', before))
    if re.match(r'\\[xyz](?![A-Za-z])', after):
        return ('AMBIG' if coeff else 'AUTO'), 'd + 다항식 변수' + (' (앞 글자)' if coeff else '')
    if re.match(r'\\(?:%s)(?![A-Za-z])' % GREEK, after):
        return ('AMBIG' if coeff else 'AUTO'), 'd + 그리스 문자' + (' (앞 글자)' if coeff else '')
    if re.match(r'\\(?:%s)\{' % ACCENT, after):
        return ('AMBIG' if coeff else 'AUTO'), 'd + 악센트' + (' (앞 글자)' if coeff else '')
    if after[:1] == '(':
        return 'AMBIG', 'd(...)' + (' (앞 글자)' if coeff else '')
    if re.match(r'[A-Za-z](?![A-Za-z])', after):
        return 'AMBIG', 'd + 라틴 한 글자' + (' (앞 글자)' if coeff else '')
    return 'SKIP', '그 외'


def scan(path):
    text = open(path, encoding='utf-8').read()
    line_start = [0]
    for m in re.finditer('\n', text):
        line_start.append(m.end())

    def lineno(off):
        lo, hi = 0, len(line_start) - 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if line_start[mid] <= off:
                lo = mid
            else:
                hi = mid - 1
        return lo + 1

    out = []
    for a, b, disp in math_spans(text):
        body = text[a:b]
        holes = [(m.start(), m.end()) for m in TEXTARG.finditer(body)]

        def inhole(k):
            return any(s <= k < e for s, e in holes)

        # 이미 \mathop{d...} 인 것: 통째로 \dd{...} 로 개명
        for m in re.finditer(r'\\mathop\{d([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}', body):
            if inhole(m.start()):
                continue
            out.append(dict(kind='MATHOP', file=path, line=lineno(a + m.start()),
                            start=a + m.start(), end=a + m.end(),
                            old=m.group(0), new='\\dd{%s}' % m.group(1),
                            display=disp, reason='기존 \\mathop{d…}'))
        for i in dtokens(body):
            if inhole(i):
                continue
            if body[max(0, i - 8):i].endswith('\\mathop{'):
                continue  # 위에서 통째로 처리
            end = operand(body, i)
            kind, reason = classify(body, i, end)
            if kind == 'SKIP' or end is None:
                continue
            out.append(dict(kind=kind, file=path, line=lineno(a + i),
                            start=a + i, end=a + end,
                            old=body[i:end], new='\\dd{%s}' % body[i + 1:end],
                            display=disp, reason=reason,
                            context=body[max(0, i - 30):min(len(body), end + 30)]))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-o', '--out')
    ap.add_argument('paths', nargs='*', default=None)
    a = ap.parse_args()
    paths = a.paths or sorted(glob.glob('_posts/**/*.md', recursive=True))
    rows = []
    for p in paths:
        rows.extend(scan(p))
    # 중첩(바깥 후보가 안쪽 후보를 품는 경우)은 자동 치환에서 제외 — 수동 처리
    import collections as _c
    byf = _c.defaultdict(list)
    for r in rows:
        byf[r['file']].append(r)
    for rs in byf.values():
        rs.sort(key=lambda r: (r['start'], -r['end']))
        for i, outer in enumerate(rs):
            for inner in rs[i + 1:]:
                if inner['start'] >= outer['end']:
                    break
                outer['kind'] = 'NESTED'
                inner['kind'] = 'NESTED'
    for n, r in enumerate(rows):
        r['id'] = 'c%05d' % n
    fh = open(a.out, 'w', encoding='utf-8') if a.out else sys.stdout
    for r in rows:
        fh.write(json.dumps(r, ensure_ascii=False) + '\n')
    if a.out:
        fh.close()
    import collections
    c = collections.Counter((r['kind'], r['reason']) for r in rows)
    for (k, why), n in sorted(c.items()):
        print(f'{k:7s} {why:24s} {n:6d}', file=sys.stderr)
    print(f'{"TOTAL":7s} {"":24s} {len(rows):6d}', file=sys.stderr)


if __name__ == '__main__':
    main()
