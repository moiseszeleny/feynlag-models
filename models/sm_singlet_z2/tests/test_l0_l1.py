"""L0/L1 for the Z2 real singlet."""

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
