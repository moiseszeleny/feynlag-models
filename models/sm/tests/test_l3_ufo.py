"""L3: the exported UFO imports and every coupling evaluates (round-trip),
and its bosonic couplings match MadGraph's stock ``sm`` entry-by-entry."""

import cmath
import importlib
import math
import sys

import pytest
import sympy as sp

from feynlag_models.ufo import export_ufo


def test_ufo_roundtrip(sm, tmp_path):
    path, report, skipped = export_ufo(sm, tmp_path / "SM_UFO", "SM_UFO")
    assert report.ok, report.failures
    assert not skipped, skipped                      # every fermion key exported
    vals = sm.values()
    g, v = vals[sm.pieces.gw.s], vals[sm.pieces.ew.v.s]
    target = 1j * g**2 * v / 2                       # hWW
    assert any(abs(c - target) < 1e-9 for c in report.couplings.values())
    text = (path / "vertices.py").read_text()
    assert "Identity(1,2)" in text                   # quark vertices carry colour flow
    assert (path / "particles.py").exists()


# --------------------------------------------------------------------------
# The exported bosonic couplings, entry-by-entry against MadGraph's stock `sm`.
#
# `metadata.yaml`'s benchmark IS MadGraph's stock electroweak point
# ((alpha_EW^-1, G_F, M_Z) = (132.50698, 1.16639e-5, 91.1876)), so the exported
# numbers are directly comparable to the model MadGraph ships — no basis
# guesswork. This mirrors feynlag's own `tests/test_ufo_sm_bosonic.py`.
#
# Stock values (MG5 models/sm/couplings.py):
#   GC_4  = i*ee                [a,W-,W+]     GC_53 = i*cw*ee/sw   [W-,W+,Z]
#   GC_5  = i*ee^2              [a,a,W-,W+]   GC_35 = -i*ee^2/sw^2 [W-,W-,W+,W+]
#   GC_36 = i*cw^2*ee^2/sw^2    [W-,W+,Z,Z]   GC_57 = -2i*cw*ee^2/sw [a,W-,W+,Z]
#   GC_72 hWW · GC_81 hZZ · GC_34 hhWW · GC_65 hhZZ
#
# MadGraph's VVVV basis differs from feynlag's, so the quartics are compared in
# the convention-free metric-pair basis c12*M12M34 + c13*M13M24 + c14*M14M23.
# --------------------------------------------------------------------------

METRIC_PAIRS = {                       # (c12, c13, c14) per feynlag structure
    "VVVV1": (0, -1, 1),
    "VVVV2": (-1, 0, 1),
    "VVVV3": (-1, 1, 0),
}


@pytest.fixture(scope="module")
def sm_ufo(sm, tmp_path_factory):
    """The written UFO, imported the way MadGraph does (bare module names)."""
    path = tmp_path_factory.mktemp("bosonic") / "SM_UFO"
    export_ufo(sm, path, "SM_UFO")
    mods = ("object_library", "particles", "parameters", "couplings",
            "lorentz", "vertices")
    saved = list(sys.path)
    sys.path.insert(0, str(path))
    for mod in mods:
        sys.modules.pop(mod, None)
    try:
        ol = importlib.import_module("object_library")
        for mod in mods[1:]:
            importlib.import_module(mod)
        vals = sm.values()
        gw, g1 = vals[sm.pieces.gw.s], vals[sm.pieces.g1.s]
        v = vals[sm.pieces.ew.v.s]
        norm = math.sqrt(gw**2 + g1**2)
        yield ol, dict(gw=gw, g1=g1, v=v, ee=gw * g1 / norm,
                       sw=g1 / norm, cw=gw / norm)
    finally:
        sys.path[:] = saved
        for mod in mods:
            sys.modules.pop(mod, None)


def _vertex(ol, names):
    for vt in ol.all_vertices:
        if sorted(p.name for p in vt.particles) == sorted(names):
            return vt
    raise AssertionError(f"no vertex {names}")


def _evaluate(vt, point):
    """``{lorentz name: complex value}`` at the benchmark point."""
    env = dict(point, complex=complex, cmath=cmath, math=math)
    lor = [l.name for l in vt.lorentz]
    return {lor[j]: complex(eval(cp.value, dict(env)))
            for (i, j), cp in vt.couplings.items()}


def _metric_pairs(vt, point):
    c12 = c13 = c14 = 0j
    for name, val in _evaluate(vt, point).items():
        d12, d13, d14 = METRIC_PAIRS[name]
        c12, c13, c14 = c12 + d12 * val, c13 + d13 * val, c14 + d14 * val
    return c12, c13, c14


def _close(got, want, label):
    assert abs(got - want) < 1e-9 * max(1.0, abs(want)), f"{label}: {got} != {want}"


def test_cubic_gauge_couplings_match_stock_sm(sm_ufo):
    """The field->particle leg sign, now derived by feynlag's writer rather
    than hand-applied here. A caller-side flip would double-count and land
    these on the wrong sign — nothing pinned that before."""
    ol, p = sm_ufo
    _close(_evaluate(_vertex(ol, ["a", "W-", "W+"]), p)["VVV1"],
           1j * p["ee"], "AWW")                                       # GC_4
    _close(_evaluate(_vertex(ol, ["W-", "W+", "Z"]), p)["VVV1"],
           1j * p["cw"] * p["ee"] / p["sw"], "ZWW")                   # GC_53


def test_quartic_gauge_couplings_match_stock_sm(sm_ufo):
    """Never exported before the feynlag `gauge_basis` pin."""
    ol, p = sm_ufo
    for names, want in [
            (["a", "a", "W-", "W+"], 1j * p["ee"] ** 2),                       # GC_5
            (["W-", "W-", "W+", "W+"], -1j * p["ee"] ** 2 / p["sw"] ** 2),     # GC_35
            (["W-", "W+", "Z", "Z"],
             1j * p["cw"] ** 2 * p["ee"] ** 2 / p["sw"] ** 2)]:                # GC_36
        c12, c13, c14 = _metric_pairs(_vertex(ol, names), p)
        _close(c14, want, f"{names} M14M23")
        _close(c13, want, f"{names} M13M24")
        _close(c12, -2 * want, f"{names} M12M34")

    # MG's VVVV5 shape: all three coefficients differ, so this one cannot be
    # matched by a lucky overall factor (the 3x assembly bug feynlag fixed).
    c12, c13, c14 = _metric_pairs(_vertex(ol, ["a", "W-", "W+", "Z"]), p)
    want = -2j * p["cw"] * p["ee"] ** 2 / p["sw"]                              # GC_57
    _close(c14, want, "AWWZ M14M23")
    _close(c13, -want / 2, "AWWZ M13M24")
    _close(c12, -want / 2, "AWWZ M12M34")


def test_scalar_vector_couplings_match_stock_sm(sm_ufo):
    ol, p = sm_ufo
    ee2, sw2, cw2 = p["ee"] ** 2, p["sw"] ** 2, p["cw"] ** 2
    _close(_evaluate(_vertex(ol, ["W-", "W+", "h"]), p)["VVS1"],
           1j * ee2 * p["v"] / (2 * sw2), "hWW")                       # GC_72
    _close(_evaluate(_vertex(ol, ["Z", "Z", "h"]), p)["VVS1"],
           1j * ee2 * p["v"] / (2 * sw2 * cw2), "hZZ")                 # GC_81
    _close(_evaluate(_vertex(ol, ["W-", "W+", "h", "h"]), p)["VVSS1"],
           1j * ee2 / (2 * sw2), "hhWW")                               # GC_34
    _close(_evaluate(_vertex(ol, ["Z", "Z", "h", "h"]), p)["VVSS1"],
           1j * ee2 / (2 * sw2 * cw2), "hhZZ")                         # GC_65


def test_no_four_photon_and_no_photon_higgs_vertex(sm_ufo):
    """Both are forbidden at tree level; the quartic assembly must not leak
    a four-photon vertex in, and the extractor must not leak an h-photon one."""
    ol, _ = sm_ufo
    for vt in ol.all_vertices:
        names = sorted(p.name for p in vt.particles)
        assert names != ["a"] * 4
        assert not ("a" in names and "h" in names)
