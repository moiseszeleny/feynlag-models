"""Every model's ``outputs/vertices.md`` stays in step with the artifacts beside it.

Both the page and ``vertices.tex`` are committed and written from the same bosonic rules
dictionary, and the fermion part comes from the same table the UFO export uses, so these
checks need no build (seconds). A rule is a table row (``| $`...`$ | $`...`$ |``) or, when too
long for a cell, an interaction line followed by a display-math block.
"""

import re

import pytest

from feynlag_models.registry import model_dirs

MODELS = [d for d in model_dirs() if (d / "outputs" / "vertices.tex").exists()]
#: the Dirac fermions each model's page must name (LaTeX, as ``FERMION_TEX`` writes them)
EXPECTED_FERMIONS = {
    "sm": [r"\bar{t} t h", r"\bar{\tau} \tau \gamma"],
    "sm_ckm": [r"\bar{t} t h", r"\bar{c} s W^+", r"\bar{\mu} \nu_\mu W^-"],
    "sm_singlet_z2": [r"\bar{t} t h_1", r"\bar{t} t h_2"],
    "thdm_type2": [r"\bar{t} t h", r"\bar{t} b H^+"],
    "seesaw_type1": [r"\bar{t} t h"],
}


def _tex_rows(path):
    return [ln for ln in path.read_text().splitlines() if ln.startswith("$") and "&" in ln]


def _part(text, heading):
    """The slice of the page under a top-level ``## heading …`` up to the next one."""
    start = re.search(rf"^## {heading}.*$", text, flags=re.M)
    assert start, heading
    nxt = re.search(r"^## ", text[start.end():], flags=re.M)
    return text[start.start():start.end() + (nxt.start() if nxt else len(text))]


def _rules(text):
    return (len(re.findall(r"^\| \$`.*`\$ \| \$`.*`\$ \|$", text, flags=re.M))
            + len(re.findall(r"^```math$", text, flags=re.M)))


@pytest.mark.parametrize("model_dir", MODELS, ids=lambda d: d.name)
def test_bosonic_part_matches_vertices_tex(model_dir):
    out = model_dir / "outputs"
    md_path = out / "vertices.md"
    assert md_path.exists(), f"{model_dir.name}: run scripts/build_outputs.py"
    text = md_path.read_text()
    n_tex = len(_tex_rows(out / "vertices.tex"))
    bosonic = _part(text, "Bosonic vertices")
    assert _rules(bosonic) == n_tex
    assert f"## Bosonic vertices: {n_tex} in all" in text
    assert f"{n_tex} bosonic" in text                       # the page's own summary line
    per_section = [int(n) for n in re.findall(r"^#{3,4} .*: (\d+) vert(?:ex|ices)$", bosonic, flags=re.M)]
    assert sum(per_section) == n_tex


@pytest.mark.parametrize("model_dir", MODELS, ids=lambda d: d.name)
def test_fermion_part_is_present_and_counted(model_dir):
    text = (model_dir / "outputs" / "vertices.md").read_text()
    part = _part(text, "Fermion vertices")
    declared = int(re.search(r"^## Fermion vertices: (\d+) in all$", part, flags=re.M).group(1))
    assert declared > 0
    assert _rules(part) == declared
    per_section = [int(n) for n in re.findall(r"^### .*: (\d+) vert(?:ex|ices)$", part, flags=re.M)]
    assert sum(per_section) == declared
    for vertex in EXPECTED_FERMIONS[model_dir.name]:
        assert vertex in part, vertex


def test_sm_ckm_charged_current_carries_ckm_angles():
    """What distinguishes sm_ckm's page from sm's: V_ij in the quark charged current."""
    text = (next(d for d in MODELS if d.name == "sm_ckm") / "outputs" / "vertices.md").read_text()
    part = _part(text, "Fermion vertices")
    assert r"\bar{u} b W^+" in part                          # a flavour-changing W vertex exists
    assert r"\theta_{12}" in part and r"\delta" in part      # written in the CKM angles


def test_seesaw_majorana_section_is_numeric():
    """The Majorana couplings have no closed form; the page gives magnitudes and says so."""
    text = (next(d for d in MODELS if d.name == "seesaw_type1") / "outputs" / "vertices.md").read_text()
    part = _part(text, "Majorana neutrino vertices")
    assert "no closed form" in part
    assert re.search(r"\| \d\.\d{3}e[-+]\d{2} \|", part)     # magnitudes, not formulas
    assert r"\bar{N} \tau W^+" in part and r"\bar{\nu} \nu Z" in part


@pytest.mark.parametrize("model_dir", MODELS, ids=lambda d: d.name)
def test_vertices_md_uses_physics_names(model_dir):
    """The raw feynlag symbols of the LaTeX table must not leak into the page."""
    text = (model_dir / "outputs" / "vertices.md").read_text()
    for raw in ("H_{0 r}", "H_{0 i}", "p{\\left(", "\\mathrm{Gm}", "\\mathrm{Gp}",
                "chiL", "chiR", "\\mathrm{tap}", "\\mathrm{vtbar}", "\\mathrm{eL}"):
        assert raw not in text, raw
