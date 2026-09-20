"""Every model's ``outputs/vertices.md`` carries exactly the rows of its ``outputs/vertices.tex``.

Both are committed and written from the same rules dictionary, so this needs no build (seconds).
A rule is a table row (``| $`...`$ | $`...`$ |``) or, when too long for a cell, an interaction line
followed by a display-math block.
"""

import re

import pytest

from feynlag_models.registry import model_dirs

MODELS = [d for d in model_dirs() if (d / "outputs" / "vertices.tex").exists()]


def _tex_rows(path):
    return [ln for ln in path.read_text().splitlines() if ln.startswith("$") and "&" in ln]


def _md_rows(text):
    tables = re.findall(r"^\| \$`.*`\$ \| \$`.*`\$ \|$", text, flags=re.M)
    blocks = re.findall(r"^```math$", text, flags=re.M)
    return len(tables) + len(blocks)


@pytest.mark.parametrize("model_dir", MODELS, ids=lambda d: d.name)
def test_vertices_md_matches_vertices_tex(model_dir):
    out = model_dir / "outputs"
    md_path = out / "vertices.md"
    assert md_path.exists(), f"{model_dir.name}: run scripts/build_outputs.py"
    text = md_path.read_text()
    n_tex = len(_tex_rows(out / "vertices.tex"))
    assert _md_rows(text) == n_tex
    assert f", {n_tex} in all," in text                     # the page's own count agrees
    per_section = [int(n) for n in re.findall(r"^#{2,3} .*\): (\d+) vertices$", text, flags=re.M)]
    assert sum(per_section) == n_tex


@pytest.mark.parametrize("model_dir", MODELS, ids=lambda d: d.name)
def test_vertices_md_uses_physics_names(model_dir):
    """The raw feynlag symbols of the LaTeX table must not leak into the page."""
    text = (model_dir / "outputs" / "vertices.md").read_text()
    for raw in ("H_{0 r}", "H_{0 i}", "p{\\left(", "\\mathrm{Gm}", "\\mathrm{Gp}"):
        assert raw not in text, raw
