r"""Markdown files write physics in LaTeX that GitHub actually renders.

CONVENTIONS.md, section "Markdown": LaTeX for physics, backticks for code. This guard
enforces four rules, each found by comparing GitHub's rendered math with the source:

1. no formula Unicode (Greek letters, superscripts, ...) outside math or inside code spans;
2. a plain dollar span must not contain a backslash followed by ASCII punctuation
   (Markdown eats the backslash: a thin space becomes a comma, braces vanish); use the
   backtick-delimited form instead;
3. no ``<`` or ``>`` inside math (GitHub double-escapes them); use ``\lt`` and ``\gt``;
4. no indented ``math`` fence (inside a list item it renders as a code block).
"""

import re
import subprocess

import pytest

from feynlag_models import ROOT

#: Unicode that only appears in formulas
MATH_CHARS = re.compile(
    "[⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻₀₁₂₃₄₅₆₇₈₉"
    "αβγδεζηθικλμνξπρστυφχψωΓΔΘΛΞΠΣΦΨΩ"
    "√∓±≈≪≫∝†∂⊃≥≤∞⟨⟩→∑∫ℓū"
    "̃̄]"                       # combining tilde / macron (H̃, ψ̄)
)

#: generated files (their generators are tested elsewhere) and files that are not prose
EXCLUDED = {"GENEALOGY.md"}

#: (file, exact code-span text) pairs that are genuine code despite matching MATH_CHARS
ALLOWED_CODE = set()


def _markdown_files():
    out = subprocess.run(["git", "ls-files", "*.md"], cwd=ROOT, capture_output=True, text=True).stdout
    # generated pages under outputs/ (spectrum.md, vertices.md) are checked too: they are written by
    # code, so a regression there would otherwise ship unseen
    files = [ROOT / f for f in out.split() if f.split("/")[-1] not in EXCLUDED]
    return sorted(files)


def _strip(text):
    text = re.sub(r"^```.*?^```", "", text, flags=re.S | re.M)       # fenced blocks (incl. ```math)
    text = re.sub(r"\$\$.*?\$\$", "", text, flags=re.S)                # display math
    text = re.sub(r"\$`.*?`\$", "", text)                               # $`…`$ inline math
    text = re.sub(r"(?<!\\)\$[^$\n]+?(?<!\\)\$", "", text)               # $…$ inline math
    return text


BACKSLASH_PUNCT = re.compile(r"\\[!-/:-@\[-`{-~]")


def _math_spans(text):
    """``(kind, tex)`` for every math span: ``display``, ``backtick`` or ``plain``."""
    spans = []
    for m in re.finditer(r"^[ \t]*```math\n(.*?)^[ \t]*```", text, flags=re.S | re.M):
        spans.append(("display", m.group(1)))
    body = re.sub(r"^[ \t]*```.*?^[ \t]*```", "", text, flags=re.S | re.M)
    spans += [("backtick", m.group(1)) for m in re.finditer(r"\$`(.+?)`\$", body)]
    body = re.sub(r"\$`.+?`\$", "", body)
    body = re.sub(r"`[^`\n]+`", "", body)
    spans += [("plain", m.group(1)) for m in re.finditer(r"(?<!\\)\$([^$\n]+?)(?<!\\)\$", body)]
    return spans


def render_offenders(text, rel="<text>"):
    """Rules 2–4: constructs that GitHub's Markdown pipeline mangles."""
    problems = []
    for m in re.finditer(r"^([ \t]+)```math\s*$", text, flags=re.M):
        line = text[:m.start()].count("\n") + 1
        problems.append(f"{rel}:{line}: indented math fence renders as a code block; put it at top level")
    for kind, tex in _math_spans(text):
        if kind == "display" and re.search(r"\\\\[ \t]*$", tex, flags=re.M):
            problems.append(f"{rel}: display math line ends in a double backslash (read as a hard break); continue the row on the same line")
        if kind == "plain" and BACKSLASH_PUNCT.search(tex):
            problems.append(f"{rel}: plain dollar math with backslash-punctuation, use the backtick form: {tex[:60]}")
        if "<" in tex or ">" in tex:
            problems.append(f"{rel}: '<' or '>' in math, use \\lt / \\gt: {tex[:60]}")
    return problems


def offenders(path):
    raw = path.read_text()
    rel = path.relative_to(ROOT).as_posix()
    problems = render_offenders(raw, rel)
    text = _strip(raw)
    for n, line in enumerate(text.splitlines(), 1):
        for code in re.findall(r"`([^`]+)`", line):
            if MATH_CHARS.search(code) and (rel, code) not in ALLOWED_CODE:
                problems.append(f"{rel}: code span with math: `{code}`")
        prose = re.sub(r"`[^`]+`", "", line)
        prose = re.sub(r"\]\([^)]*\)", "]", prose)                       # link targets
        found = sorted(set(MATH_CHARS.findall(prose)))
        if found:
            problems.append(f"{rel}: prose math {''.join(found)!r}: {prose.strip()[:90]}")
    return problems


@pytest.mark.parametrize("path", _markdown_files(), ids=lambda p: p.relative_to(ROOT).as_posix())
def test_markdown_physics_is_latex(path):
    problems = offenders(path)
    assert not problems, "\n".join(problems)


@pytest.mark.parametrize("snippet, fragment", [
    ("A thin space $a\\,b$ here.", "backslash-punctuation"),
    ("Braces $\\{x\\}$ here.", "backslash-punctuation"),
    ("Order $a > b$ here.", "'<' or '>'"),
    ("Order $`a < b`$ here.", "'<' or '>'"),
    ("- item\n\n  ```math\n  x = 1\n  ```\n", "indented math fence"),
    ("```math\na \\\\\nb\n```\n", "double backslash"),
])
def test_render_rules_reject(snippet, fragment):
    problems = render_offenders(snippet)
    assert any(fragment in p for p in problems), problems


def test_render_rules_accept_good_forms():
    good = "Thin $`a\\,b`$, order $a \\gt b$, plain $x_1$.\n\n```math\nx = 1\n```\n"
    assert render_offenders(good) == []
