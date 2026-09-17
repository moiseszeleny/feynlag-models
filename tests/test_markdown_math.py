"""Markdown files write physics in LaTeX ($…$ or ```math blocks), never as Unicode.

CONVENTIONS.md → "Markdown": LaTeX for physics, backticks for code. This guard strips
fenced blocks and math spans, then rejects math-like Unicode left in prose or hidden in
code spans (a code span holding λ or ² is math in disguise).
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
    files = [ROOT / f for f in out.split() if "/outputs/" not in f and f.split("/")[-1] not in EXCLUDED]
    return sorted(files)


def _strip(text):
    text = re.sub(r"^```.*?^```", "", text, flags=re.S | re.M)       # fenced blocks (incl. ```math)
    text = re.sub(r"\$\$.*?\$\$", "", text, flags=re.S)                # display math
    text = re.sub(r"\$`.*?`\$", "", text)                               # $`…`$ inline math
    text = re.sub(r"(?<!\\)\$[^$\n]+?(?<!\\)\$", "", text)               # $…$ inline math
    return text


def offenders(path):
    text = _strip(path.read_text())
    rel = path.relative_to(ROOT).as_posix()
    problems = []
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
