"""L0/L1 for the Z2 real singlet."""

import pytest
import sympy as sp

from feynlag import check_discrete_invariance
from feynlag_models.checks import (assert_dual_equal, massive_gauge_boson_count,
                                   zero_eigenvalue_count)


def test_validate_gauge_hermiticity_dimension_anomalies(xsm):
    """Every term is gauge and Z2 invariant, hermitian and dim ≤ 4; anomalies cancel."""
    report = xsm.model.validate()
    assert report.ok, report.summary()
    assert report.checks["anomalies"] is not None and report.checks["anomalies"].ok


def test_z2_invariance_of_every_term(xsm):
    """Z2 (S → −S) holds term by term, the Dmu-built Higgs kinetic term included."""
    Z2 = xsm.extra["Z2"]
    for term in xsm.model.lagrangian:
        ok, viol = check_discrete_invariance(term.expr, Z2)
        assert ok, (term.name, viol)
    report = xsm.model.check_invariance(hermiticity=False, dimension=False)
    assert report.ok, [(t.name, check) for t, check, _d in report.failures]


def test_tadpoles(xsm):
    """μ² = λ v² + ½ λ_HS v_S²,  μ_S² = −λ_S v_S² − ½ λ_HS v² (derived by hand from V)."""
    e = xsm.extra
    lam, v = e["ew"].lam.s, e["ew"].v.s
    lamS, lamHS, vS = e["lamS"].s, e["lamHS"].s, e["vS"].s
    assert_dual_equal(e["ew"].mu2.expr, lam * v**2 + lamHS * vS**2 / 2, msg="mu2")
    assert_dual_equal(e["muS2"].expr, -lamS * vS**2 - lamHS * v**2 / 2, msg="muS2")


def test_cp_even_mass_matrix(xsm):
    e = xsm.extra
    lam, v = e["ew"].lam.s, e["ew"].v.s
    lamS, lamHS, vS = e["lamS"].s, e["lamHS"].s, e["vS"].s
    expected = sp.Matrix([[2 * lam * v**2, lamHS * v * vS], [lamHS * v * vS, 2 * lamS * vS**2]])
    for a in range(2):
        for b in range(2):
            assert_dual_equal(e["M_even"][a, b], expected[a, b], msg=f"M[{a},{b}]")


def test_spectrum_at_benchmark(xsm):
    """h1 is the lighter, SM-like state; both masses positive; rotation diagonalises M."""
    e, vals = xsm.extra, xsm.values()
    m1, m2 = vals[e["MH1"].s], vals[e["MH2"].s]
    assert 0 < m1 < m2
    assert abs(vals[e["theta"].s]) < 0.3                       # small mixing at the benchmark
    ok, res = e["rot"].check(e["M_even"], simplifier=lambda x: sp.nsimplify(
        sp.simplify(x.subs(e["theta"].s, e["rot"].angle_solution)), rational=False))
    assert ok, res


def test_goldstone_count_unchanged(xsm):
    """Still exactly three massless Goldstones."""
    p, vals = xsm.pieces, xsm.values()
    W1, W2, W3 = p.W.components
    Mg = xsm.model.gauge_mass_matrix([W1, W2, W3, p.B.components[0]])
    assert massive_gauge_boson_count(Mg, vals) == 3
    M_odd = xsm.model.mass_matrix([xsm.bosons["G0"]])
    M_ch = xsm.model.mass_matrix([xsm.bosons["Gp"]], charged=True)
    assert sp.simplify(M_odd[0, 0]) == 0 and sp.simplify(M_ch[0, 0]) == 0
    assert zero_eigenvalue_count(M_odd, vals) + 2 * zero_eigenvalue_count(M_ch, vals) == 3


def test_labels_follow_mixing_with_a_light_singlet():
    """UG-4: the singlet model labels by mixing, not by mass (CONVENTIONS.md). With the singlet
    lighter (M22 < M11; here λ_S = λ_HS = 0.01) the principal-branch θ still keeps h1 h-like,
    so h1 is now the *heavier* state and takes the + root of m²_{1,2} = λv² + λ_S v_S² ± √(…)."""
    import math
    from models.sm_singlet_z2.model import benchmark_point, build
    xsm = build(dict(benchmark_point(), lamS=0.01, lamHS=0.01))
    e, vals = xsm.extra, xsm.values()
    M = e["M_even"].subs(vals)
    assert float(M[1, 1]) < float(M[0, 0])                       # really the light-singlet regime
    th = float(vals[e["theta"].s])
    assert abs(math.cos(th)) > abs(math.sin(th))                  # h1 is h-like
    m1, m2 = float(vals[e["MH1"].s]), float(vals[e["MH2"].s])
    assert m1 > m2 > 0
    lam, v = float(vals[e["ew"].lam.s]), float(vals[e["ew"].v.s])
    lamS, lamHS, x = (float(vals[e[k].s]) for k in ("lamS", "lamHS", "vS"))
    root = math.sqrt((lam * v**2 - lamS * x**2) ** 2 + (lamHS * v * x) ** 2)
    assert abs(m1**2 - (lam * v**2 + lamS * x**2 + root)) < 1e-9 * m1**2
    assert abs(m2**2 - (lam * v**2 + lamS * x**2 - root)) < 1e-9 * m1**2


# ------------------------------------------------- feynlag 0.4.0 API (guided basis, coverage)

def test_mass_blocks_cp_even_no_double_shift(xsm):
    """``mass_blocks`` finds the CP-even (H0_r, S) block with the analytic entries
    (2λv², λ_HS v v_S, 2λ_S v_S²), so the real-scalar double vacuum shift of FG-1 is absent
    on this path too; G0 and G+ are separate 1×1 blocks with Goldstone directions."""
    e = xsm.extra
    lam, v = e["ew"].lam.s, e["ew"].v.s
    lamS, lamHS, vS = e["lamS"].s, e["lamHS"].s, e["vS"].s
    blocks = xsm.model.mass_blocks(kind="scalar")
    (even,) = [b for b in blocks if b.size == 2]
    assert even.cp == "even" and even.fields == [e["h_weak"], e["s0"]]
    expected = sp.Matrix([[2 * lam * v**2, lamHS * v * vS], [lamHS * v * vS, 2 * lamS * vS**2]])
    assert (even.matrix - expected).applyfunc(sp.expand) == sp.zeros(2, 2)
    gold = {b.fields[0] for b in blocks if b.size == 1 and b.goldstones}
    assert gold == {xsm.bosons["G0"], xsm.bosons["Gp"]}


def test_diagonalize_keeps_mixing_labels(xsm):
    """``diagonalize`` (no ``values=``) registers ``rotation_2x2(θ)`` with the principal
    ``θ = ½ atan(2M12/(M11 − M22))``: h1 is the h-like row, as CONVENTIONS.md and UG-4 fix."""
    from feynlag import rotation_2x2
    e = xsm.extra
    M, th = e["M_even"], e["theta"].s
    assert list(e["rot"].old_fields) == [e["h_weak"], e["s0"]]
    assert list(e["rot"].new_fields) == [xsm.bosons["h1"], xsm.bosons["h2"]]
    assert sp.Matrix(e["rot"].matrix) == rotation_2x2(th)
    principal = sp.atan(2 * M[0, 1] / (M[0, 0] - M[1, 1])) / 2
    assert sp.simplify(e["rot"].angle_solution - principal) == 0
    assert sp.simplify(e["theta"].expr - principal) == 0


def test_physical_registry(xsm):
    """Charges (derived from the vacuum), conjugate pairs and Goldstones from ``model.physical``."""
    b = xsm.bosons
    assert xsm.charges == {b["h1"]: 0, b["h2"]: 0, b["G0"]: 0, b["Gp"]: 1, b["Gm"]: -1,
                           b["Z"]: 0, b["A"]: 0, b["Wp"]: 1, b["Wm"]: -1}
    assert xsm.conjugates == {b["Gp"]: b["Gm"], b["Gm"]: b["Gp"], b["Wp"]: b["Wm"], b["Wm"]: b["Wp"]}
    assert xsm.goldstones == (b["G0"], b["Gp"], b["Gm"])


def test_term_coverage(xsm):
    """Every invariant H, S and the Z2 allow at dim ≤ 4 is present, nothing is left over, and
    no Z2-odd operator (S, S³, H†H S) appears. Coefficients in feynlag's ``V = Σ c O``
    convention are CONVENTIONS.md's ``V = −μ²H†H + λ(H†H)² + ½μ_S²S² + ¼λ_S S⁴ + ½λ_HS(H†H)S²``;
    the Yukawas (``L = −Σ c O``) are the SM ones."""
    e, ys = xsm.extra, xsm.pieces.yukawa_params
    tc = xsm.model.term_coverage()
    assert tc.complete and tc.unmatched == {}
    got = {t.label: c for t, c in tc.present}
    assert got == {
        "(H†H)": -e["ew"].mu2.s, "(H†H) (H†H)": e["ew"].lam.s,
        "S S": e["muS2"].s / 2, "S S S S": e["lamS"].s / 4, "S S (H†H)": e["lamHS"].s / 2,
        "Ll̄·H eR": ys["ytau"].s, "QL̄·H dR": ys["yb"].s, "QL̄·H̃ uR": ys["yt"].s,
    }


def test_summary_and_parameters(xsm):
    """``summary()``: S is a real gauge singlet, odd under Z2, and the SM fields are even;
    ``check_parameters()`` finds no undeclared symbol."""
    s = xsm.model.summary()
    assert s.field_header[:6] == ["field", "type", "SU2L", "U1Y", "SU3c", "Z2"]
    rows = {r[0]: tuple(str(x) for x in r[1:6]) for r in s.field_rows}
    assert rows["S"] == ("real scalar", "1", "0", "1", "1")
    assert rows["H"] == ("scalar", "2", "1/2", "1", "")
    assert set(rows) == {"H", "W", "B", "G", "Ll", "eR", "QL", "uR", "dR", "S"}
    assert {r[0] for r in s.param_rows} == {q.name for q in xsm.params}
    assert xsm.model.check_parameters().undeclared == []


@pytest.mark.xfail(strict=True, reason="FG-8: feynlag.terms.kinetic gives (∂S)² for a real "
                   "scalar, twice the canonical ½(∂S)²")
def test_feynlag_kinetic_real_scalar_gap(xsm):
    """``kinetic(S)`` for the real singlet should be the canonical ``½(∂_μS)²``
    (CONVENTIONS.md, Gauge and kinetic terms). feynlag writes ``(D_μφ)†(D^μφ)`` for every
    scalar, which for a real field is ``(∂S)²``. The model keeps its hand-written term."""
    from feynlag import PartialMu, kinetic
    s0 = xsm.extra["s0"]
    expr = sum(t for t, _sector in kinetic(xsm.extra["S"]))
    assert sp.expand(expr - sp.Rational(1, 2) * PartialMu(s0) ** 2) == 0
