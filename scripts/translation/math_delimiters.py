"""Deterministic `$...$` → `$$...$$` normalizer for the math blog, with a safety gate.

The blog writes ALL top-level math — inline and display alike — as `$$...$$`
(GUIDELINE-New/Edit §2, GUIDELINE-Translation): single `$` is unsafe because
kramdown parses `_`/`*` inside `$...$` as emphasis before KaTeX runs, breaking
the math. The translation model (kimi), however, reflexively downgrades inline
`$$x$$` to standard-markdown `$x$`. That (a) violates the rule and (b) collapses
the `$$`-block count, so translate_worker's KO/EN count check mismatches and
fires the expensive interactive-claude verify pass — which times out on large
posts (see the 2026-07-07 Characteristic_Classes incident: en=51 vs ko=518).

`normalize_math_delimiters` — mask, then promote:
  1. Hide every span that must stay verbatim, replacing it with a placeholder:
       - `$$...$$` display blocks — this ALSO protects their interior single `$`
         (`\\text{$k$-forms on $\\mathbb{R}^n$}`, `\\tag{$\\ast$}`), the documented
         exception (GUIDELINE §2);
       - fenced code ``` ``` ``` and inline code `` `...` ``;
       - the interior of protected inline tags <cap>/<phrase>/<em>/<em-ko>.
  2. In what remains (top-level prose), promote every BALANCED `$...$` to `$$...$$`.
  3. Restore the placeholders.

`normalize_if_safe` wraps it with a gate. A body with an ODD count of unescaped
`$` (a pre-existing translation defect — a dropped/added `$`) cannot be promoted
unambiguously: left-to-right pairing desyncs and can pull a `$$`-display opener
into an inline span, corrupting a downstream `\\text{$k$}`/`\\tag{$\\ast$}`. The
gate refuses such bodies (and any residual `$$`-inside-`\\text{}` corruption)
and returns the text UNCHANGED so the caller can flag it for manual repair
instead of shipping a broken file.

Both functions are idempotent and promotion-only (never `$$`→`$`).
"""
import re

# Spans kept verbatim. `\1` binds the protected-tag name for the close tag.
# `$$...$$` is masked whole, so its interior single `$` (\text/\tag) is protected.
_PROTECT = re.compile(
    r"```.*?```"                                    # fenced code block
    r"|`[^`\n]*`"                                   # inline code
    r"|\$\$.*?\$\$"                                 # display math block
    r"|<(cap|phrase|em-ko|em)\b[^>]*>.*?</\1\s*>",  # protected inline tags
    re.DOTALL,
)

# A balanced top-level inline span: unescaped `$`, no `$` inside, unescaped closing
# `$`. `(?!\$)` avoids biting a stray `$$` remnant. A lone `$` never matches.
_INLINE = re.compile(r"(?<!\\)\$(?!\$)([^$]*?)(?<!\\)\$")

# LaTeX text-mode groups whose interior legitimately holds single `$`; a `$$`
# appearing inside one is a promotion-corruption signature.
_TEXTISH = re.compile(
    r"\\(?:text|tag|mbox|hbox|textrm|textbf|textit|textsf|textnormal|"
    r"operatorname|substack)\s*\{"
)


def normalize_math_delimiters(text: str) -> str:
    stash = []

    def hide(m):
        stash.append(m.group(0))
        return f"\x00{len(stash) - 1}\x00"

    masked = _PROTECT.sub(hide, text)
    masked = _INLINE.sub(lambda m: "$$" + m.group(1) + "$$", masked)
    return re.sub(r"\x00(\d+)\x00", lambda m: stash[int(m.group(1))], masked)


def _dollar2_inside_textgroup(s: str) -> bool:
    """True if any `\\text{...}`/`\\tag{...}`-style group contains `$$` (corruption)."""
    for m in _TEXTISH.finditer(s):
        depth, j, n = 1, m.end(), len(s)
        while j < n and depth:
            c = s[j]
            if c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
            elif s[j:j + 2] == "$$":
                return True
            j += 1
    return False


def normalize_if_safe(text):
    """Return (normalized, True) if promotion is provably non-corrupting, else
    (text_unchanged, False). Unsafe = odd `$` parity (imbalance/desync risk),
    non-`$` content changed, `$$` leaked into a `\\text{}`/`\\tag{}` group, or a
    non-idempotent result."""
    if len(re.findall(r"(?<!\\)\$", text)) % 2 == 1:
        return text, False
    norm = normalize_math_delimiters(text)
    if text.replace("$", "") != norm.replace("$", ""):
        return text, False
    if _dollar2_inside_textgroup(norm):
        return text, False
    if normalize_math_delimiters(norm) != norm:
        return text, False
    return norm, True


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == "--selftest":
        cases = [
            (r"a $x$ b", r"a $$x$$ b"),
            (r"$H_k$ inline", r"$$H_k$$ inline"),
            (r"$$H_k$$ already", r"$$H_k$$ already"),
            (r"map $$f\colon X\to Y$$ mix $g$", r"map $$f\colon X\to Y$$ mix $$g$$"),
            (r"$$\Omega=\{\text{$k$-forms on $\mathbb{R}^n$}\}$$",
             r"$$\Omega=\{\text{$k$-forms on $\mathbb{R}^n$}\}$$"),
            (r"$$0\to A\to B\to 0\tag{$\ast$}$$", r"$$0\to A\to B\to 0\tag{$\ast$}$$"),
            (r"chain $$D\tag{$\ast$}$$ and $g$", r"chain $$D\tag{$\ast$}$$ and $$g$$"),
            (r"see <cap>$x$</cap> and <phrase>$y$</phrase> then $z$",
             r"see <cap>$x$</cap> and <phrase>$y$</phrase> then $$z$$"),
            (r"<em>emph $y$ word</em> $z$", r"<em>emph $y$ word</em> $$z$$"),
            (r"<em-ko>나가는</em-ko> $w$", r"<em-ko>나가는</em-ko> $$w$$"),
            (r"costs \$5 and $q$", r"costs \$5 and $$q$$"),
            ("code `$x$` and $y$", "code `$x$` and $$y$$"),
            (r"$$A$$$$B$$", r"$$A$$$$B$$"),
        ]
        ok = True
        for src, exp in cases:
            got = normalize_math_delimiters(src)
            if got != exp:
                ok = False
                print(f"FAIL\n  in : {src}\n  exp: {exp}\n  got: {got}")
            else:
                print(f"ok   norm  {src}")
        for src, _ in cases:
            a = normalize_math_delimiters(src)
            if normalize_math_delimiters(a) != a:
                ok = False
                print(f"NOT IDEMPOTENT: {src!r}")
        # safety gate: odd-$ body must be refused unchanged; a body whose promotion
        # would leak $$ into \text{} must be refused.
        gate = [
            (r"$$D\tag{$\ast$}$$ has a stray $ here", False),   # odd $
            (r"clean $a$ and $$B$$", True),                     # even, safe
            (r"$$\text{$k$}$$ plus $m$", True),                 # even, \text protected
        ]
        for src, exp_safe in gate:
            out, safe = normalize_if_safe(src)
            if safe != exp_safe or (not safe and out != src):
                ok = False
                print(f"GATE FAIL: {src!r} -> safe={safe} (exp {exp_safe}), out={out!r}")
            else:
                print(f"ok   gate  safe={safe}  {src}")
        sys.exit(0 if ok else 1)

    sys.stdout.write(normalize_math_delimiters(sys.stdin.read()))
