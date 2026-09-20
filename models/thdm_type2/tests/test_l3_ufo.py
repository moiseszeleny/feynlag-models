"""L3: UFO export of the 2HDM (h, H, A, H± + SM) imports and round-trips, and its
vector–scalar–scalar couplings are pinned against MadGraph's stock ``sm``."""

import cmath
import importlib
import math
import sys

import pytest

from feynlag_models.ufo import export_ufo


def test_ufo_roundtrip(thdm, tmp_path):
    path, report, skipped = export_ufo(thdm, tmp_path / "THDM_UFO", "THDM_TYPE2_UFO")
    assert report.ok, report.failures
    assert not skipped, skipped
    vals = thdm.values()
    e = thdm.extra
    g, v = vals[thdm.pieces.gw.s], vals[e["v"].s]
    target = 1j * g**2 * v / 2 * cmath.sin(vals[e["beta"].s] - vals[e["alpha"].s])   # hWW
    assert any(abs(c - target) < 1e-9 for c in report.couplings.values())
    names = (path / "particles.py").read_text()
    for n in ("'h'", "'h2'", "'h3'", "'h+'", "'h-'"):
        assert n in names, n


# --------------------------------------------------------------------------
# The ten VSS1 couplings, against MadGraph's stock `sm`.
#
# feynlag's writer (>= efffdb0) gives every VSS1 vertex an unconditional -1. Before it, nothing did,
# so all ten couplings below had the wrong sign in the exported UFO (REPORT.md). Nothing else pinned
# them: the SM UFO has no VSS vertex in unitary gauge, so `models/sm` cannot.
#
# The 2HDM's second doublet, in the Higgs basis, couples to the gauge bosons exactly like the SM
# doublet, with rho_perp = cos(b-a) h - sin(b-a) H. So each 2HDM VSS vertex is a stock Goldstone
# vertex times cos(b-a) or -sin(b-a). The benchmark IS the stock electroweak point (see
# `models/sm/tests/test_l3_ufo.py`). Stock values (MG5 models/sm/couplings.py, vertices.py):
#
#   V_11 [a, G-, G+]  GC_3  = -i ee                        V_58 [Z, G-, G+]  GC_61 = -i cw ee/(2 sw) + i ee sw/(2 cw)
#   V_42 [W-, G+, H]  GC_37 = -ee/(2 sw)                   V_48 [W+, G-, H]  GC_37
#   V_57 [Z, G0, H]  GC_60 = -cw ee/(2 sw) - ee sw/(2 cw)
#   V_41 [W-, G0, G+] GC_39 = +i ee/(2 sw)                 V_47 [W+, G0, G-] GC_38 = -i ee/(2 sw)
#
# Two conventions map a stock Goldstone vertex onto the 2HDM export:
#   * feynlag's charged Goldstone carries i^(-q) relative to MadGraph's, and the writer undoes it on
#     Goldstone legs only (`feynlag/export/ufo/legs.py`, `charged_goldstone_phase`). H± is not a
#     Goldstone, so it gets no phase: a stock vertex with one G^q leg is divided by i^q.
#   * VSS1 = P(1,2) - P(1,3) is antisymmetric in its scalars, so a reversed scalar order flips it.
#
# Six vertices are pinned absolutely. The four with an A have one more convention, the sign of A
# relative to MadGraph's G0, which no physical result depends on; the test fixes neither its value
# nor its origin, only that it is a sign and the same for all four. The four charged W vertices are
# not conjugate pairs, so they also tell an unconditional -1 apart from a pair-only one.
# --------------------------------------------------------------------------

_UFO_MODULES = ("object_library", "particles", "parameters", "couplings", "lorentz", "vertices")


@pytest.fixture(scope="module")
def thdm_ufo(thdm, tmp_path_factory):
    """The written UFO imported the way MadGraph does (bare module names), restoring
    ``sys.path`` and any modules of the same names on exit."""
    path = tmp_path_factory.mktemp("vss") / "THDM_TYPE2_UFO"
    export_ufo(thdm, path, "THDM_TYPE2_UFO")
    saved_path = list(sys.path)
    saved_modules = {m: sys.modules.pop(m) for m in _UFO_MODULES if m in sys.modules}
    sys.path.insert(0, str(path))
    try:
        ol = importlib.import_module("object_library")
        for mod in _UFO_MODULES[1:]:
            importlib.import_module(mod)
        env = dict(cmath=cmath, complex=complex, math=math)          # the UFO's own parameters
        for prm in ol.all_parameters:
            env[prm.name] = eval(prm.value, dict(env)) if isinstance(prm.value, str) else prm.value
        yield ol, env
    finally:
        sys.path[:] = saved_path
        for mod in _UFO_MODULES:
            sys.modules.pop(mod, None)
        sys.modules.update(saved_modules)


def _close(got, want, label):
    assert abs(got - want) < 1e-9 * max(1.0, abs(want)), f"{label}: {got} != {want}"


def test_vss_couplings_match_stock_sm(thdm, thdm_ufo):
    ol, env = thdm_ufo
    vss = {tuple(p.name for p in vt.particles): vt
           for vt in ol.all_vertices if any(l.name == "VSS1" for l in vt.lorentz)}

    def exported(names):
        vt = vss[names]
        assert [l.name for l in vt.lorentz] == ["VSS1"], names
        (cp,) = vt.couplings.values()
        return complex(eval(cp.value, dict(env)))

    # expected values come from the bundle, not from the UFO's own parameter table
    vals, e = thdm.values(), thdm.extra
    gw, g1 = (float(complex(vals[x.s]).real) for x in (thdm.pieces.gw, thdm.pieces.g1))
    alpha, beta = (float(complex(vals[e[k].s]).real) for k in ("alpha", "beta"))
    norm = math.hypot(gw, g1)
    ee, sw, cw = gw * g1 / norm, g1 / norm, gw / norm
    s, c = math.sin(beta - alpha), math.cos(beta - alpha)
    GC_3 = -1j * ee
    GC_61 = -(cw * ee * 1j) / (2 * sw) + (ee * 1j * sw) / (2 * cw)
    GC_37 = -ee / (2 * sw)
    GC_60 = -(cw * ee) / (2 * sw) - (ee * sw) / (2 * cw)
    GC_39, GC_38 = 1j * ee / (2 * sw), -1j * ee / (2 * sw)

    absolute = {
        ("a", "h-", "h+"): GC_3,
        ("Z", "h-", "h+"): GC_61,
        ("W-", "h+", "h"): c * GC_37 / 1j,
        ("W+", "h-", "h"): c * GC_37 / -1j,
        ("W-", "h2", "h+"): s * GC_37 / 1j,       # scalars reversed w.r.t. stock: the sign is in -sin
        ("W+", "h2", "h-"): s * GC_37 / -1j,
    }
    with_a = {
        ("Z", "h3", "h"): c * GC_60,
        ("Z", "h3", "h2"): -s * GC_60,
        ("W-", "h3", "h+"): GC_39 / 1j,
        ("W+", "h3", "h-"): GC_38 / -1j,
    }
    assert set(vss) == set(absolute) | set(with_a), sorted(set(vss) ^ (set(absolute) | set(with_a)))

    for names, want in absolute.items():
        _close(exported(names), want, str(names))

    first = next(iter(with_a))
    sign_of_a = exported(first) / with_a[first]
    assert abs(sign_of_a.imag) < 1e-9 and abs(abs(sign_of_a.real) - 1) < 1e-9, sign_of_a
    for names, want in with_a.items():
        _close(exported(names), sign_of_a.real * want, f"{names} (sign of A = {sign_of_a.real:+.0f})")
