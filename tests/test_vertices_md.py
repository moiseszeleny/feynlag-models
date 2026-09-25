"""Every model's ``outputs/vertices.md`` stays in step with the artifacts beside it.

Both the page and ``vertices.tex`` are committed and written from the same bosonic rules
dictionary, and the fermion part comes from the same table the UFO export uses, so these
checks need no build (seconds). A rule is a table row (``| $`...`$ | $`...`$ |``) or, when too
long for a cell, an interaction line followed by a display-math block.
"""

import math
import re

import pytest

from feynlag_models import metadata as md
from feynlag_models.registry import model_dirs

MODELS = [d for d in model_dirs() if (d / "outputs" / "vertices.tex").exists()]
#: the Dirac fermions each model's page must name (LaTeX, as ``FERMION_TEX`` writes them)
EXPECTED_FERMIONS = {
    "sm": [r"\bar{t} t h", r"\bar{\tau} \tau \gamma"],
    "sm_ckm": [r"\bar{t} t h", r"\bar{c} s W^+", r"\bar{\mu} \nu_\mu W^-"],
    "sm_singlet_z2": [r"\bar{t} t h_1", r"\bar{t} t h_2"],
    "thdm_type2": [r"\bar{t} t h", r"\bar{t} b H^+"],
    "seesaw_type1": [r"\bar{t} t h"],
    "seesaw_type1_2n": [r"\bar{t} t h", r"\bar{c} c h", r"\bar{\mu} \mu \gamma"],
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


#: a Goldstone fermion coupling every model has, and must keep on the page
GOLDSTONE_ROW = r"\bar{\tau} \tau G^0"


@pytest.mark.parametrize("model_dir", MODELS, ids=lambda d: d.name)
def test_goldstone_fermion_vertices_are_on_the_page(model_dir):
    """The page keeps the Goldstone fermion vertices and says so in its own subsection.

    ``fermion_rows`` deliberately does not pass ``drop=bundle.goldstones``, unlike
    ``export_ufo``: a Feynman-gauge calculation needs these. The other half of the policy is
    :func:`test_exported_ufo_has_no_goldstone`.
    """
    part = _part((model_dir / "outputs" / "vertices.md").read_text(), "Fermion vertices")
    heading = re.search(r"^### Fermion pairs with a Goldstone leg \(Feynman gauge\): (\d+) vert(?:ex|ices)$",
                        part, flags=re.M)
    assert heading, f"{model_dir.name}: no Goldstone subsection in the fermion part"
    tail = part[heading.end():]
    assert _rules(tail) == int(heading.group(1))
    assert GOLDSTONE_ROW in tail, GOLDSTONE_ROW


@pytest.mark.parametrize("model_dir", [d for d in MODELS if md.load(d)["outputs"]["ufo"]],
                         ids=lambda d: d.name)
def test_exported_ufo_has_no_goldstone(model_dir):
    """The other half: the unitary-gauge UFO drops every Goldstone, particle and vertex alike."""
    ufo = model_dir / md.load(model_dir)["outputs"]["ufo"]
    for name in ("particles.py", "vertices.py"):
        text = (ufo / name).read_text()
        for goldstone in ("G__plus__", "G__minus__", "G0"):
            assert goldstone not in text, f"{model_dir.name}/{name}: {goldstone}"


def _majorana_couplings(text):
    """``{(vertex, structure): magnitude}`` from the seesaw's numeric table."""
    part = _part(text, "Majorana neutrino vertices")
    rows = re.findall(r"^\| \$`([^`]+)`\$ \| \$`([^`]+)`\$ \| ([0-9.]+e[-+]\d+) \|$", part, flags=re.M)
    return {(v, s): float(c) for v, s, c in rows}


def test_seesaw_majorana_table_shows_the_seesaw_hierarchy():
    """The numeric table must keep the light state unsuppressed and the heavy one at O(V).

    A rotation-direction slip (light and heavy swapped) breaks the first two checks at once.
    Magnitudes cannot see a conjugation (U against U*) mistake; that is pinned symbolically in
    ``models/seesaw_type1/tests/test_l2_literature.py`` against Atre et al. Eq. (2.5). This test
    guards the generated table, not the physics.
    """
    model_dir = next(d for d in MODELS if d.name == "seesaw_type1")
    couplings = _majorana_couplings((model_dir / "outputs" / "vertices.md").read_text())
    bench = md.benchmark_inputs(model_dir)
    gw, g1, v = bench["gw"], bench["g1"], bench["v"]
    mixing = (bench["yv"] * v / math.sqrt(2)) / bench["MR"]          # V = m_D / M_R
    yukawa = bench["yv"] / math.sqrt(2)

    def close(got, want, tol=2e-3):                                  # the table prints 4 digits
        assert abs(got - want) <= tol * abs(want), f"{got} != {want}"

    light_w = couplings[(r"\bar{\nu} \tau W^+", r"\gamma^\mu P_L")]
    light_z = couplings[(r"\bar{\nu} \nu Z", r"\gamma^\mu P_L")]
    close(light_w, gw / math.sqrt(2))                                # unsuppressed
    close(light_z, math.hypot(gw, g1) / 2)
    close(couplings[(r"\bar{N} \tau W^+", r"\gamma^\mu P_L")] / light_w, mixing)      # O(V)
    close(couplings[(r"\bar{N} \nu Z", r"\gamma^\mu P_L")] / light_z, mixing)
    close(couplings[(r"\bar{\nu} N h", "P_R")], yukawa)            # the Dirac Yukawa survives
    close(couplings[(r"\bar{\nu} N h", "P_L")]
          / couplings[(r"\bar{\nu} N h", "P_R")], mixing**2, tol=4e-3)                  # O(V^2)


def test_seesaw_2n_majorana_table_names_each_flavour():
    """Three generations: every charged-lepton leg is named by its flavour. The generic fallback
    names legs by field base only, which printed every charged lepton as tau and listed the
    same vertex twice with different couplings."""
    model_dir = next(d for d in MODELS if d.name == "seesaw_type1_2n")
    part = _part((model_dir / "outputs" / "vertices.md").read_text(), "Majorana neutrino vertices")
    rows = re.findall(r"^\| \$`([^`]+)`\$ \| \$`([^`]+)`\$ \|", part, flags=re.M)
    assert rows and len(rows) == len(set(rows))
    for lep in ("e", r"\mu", r"\tau"):
        for state in ("N_1", "N_2", r"\nu_2", r"\nu_3"):
            assert (rf"\bar{{{state}}} {lep} W^+", r"\gamma^\mu P_L") in rows, (state, lep)
    assert "no closed form" in part


@pytest.mark.parametrize("model_dir", MODELS, ids=lambda d: d.name)
def test_vertices_md_uses_physics_names(model_dir):
    """The raw feynlag symbols of the LaTeX table must not leak into the page."""
    text = (model_dir / "outputs" / "vertices.md").read_text()
    for raw in ("H_{0 r}", "H_{0 i}", "p{\\left(", "\\mathrm{Gm}", "\\mathrm{Gp}",
                "chiL", "chiR", "\\mathrm{tap}", "\\mathrm{vtbar}", "\\mathrm{eL}"):
        assert raw not in text, raw
