"""L0/L1 for the type-II 2HDM: invariance, soft Z2 breaking, tadpoles, three mass blocks."""

import sympy as sp

from feynlag import check_discrete_invariance, diracPR, fermion_mass_matrix
from feynlag_models.checks import (assert_dual_equal, massive_gauge_boson_count,
                                   zero_eigenvalue_count)


def test_validate_invariance_and_anomalies(thdm):
    report = thdm.model.validate()
    assert report.ok, report.summary()
    assert report.checks["anomalies"] is not None and report.checks["anomalies"].ok


def test_z2_softly_broken_only_by_m12sq(thdm):
    """Z2 (H2 → −H2, u_R → −u_R) holds for every potential and Yukawa term except the
    named soft term −m12² (H1†H2 + h.c.). Kinetic (Dmu) terms are skipped: FG-2."""
    Z2 = thdm.extra["Z2"]
    failing = []
    for term in thdm.model.lagrangian:
        if term.sector == "kinetic":
            continue
        ok, _ = check_discrete_invariance(term.expr, Z2)
        if not ok:
            failing.append(term.name)
    assert failing == ["soft_z2_breaking"], failing


def test_tadpoles_gunion_haber_eq6_eq7(thdm):
    """GH Eqs. (6),(7) with λ6 = λ7 = 0: m11² = m12² tβ − ½v²(λ1 cβ² + λ345 sβ²) (and 1↔2),
    written in v1 = v cβ, v2 = v sβ: m11² = m12² v2/v1 − ½λ1 v1² − ½λ345 v2²."""
    e = thdm.extra
    v1, v2, m12 = e["v1"].s, e["v2"].s, e["m12sq"].s
    l1, l2, l3, l4, l5 = (q.s for q in e["lams"])
    l345 = l3 + l4 + l5
    assert_dual_equal(e["m11sq"].expr, m12 * v2 / v1 - l1 * v1**2 / 2 - l345 * v2**2 / 2, msg="m11sq")
    assert_dual_equal(e["m22sq"].expr, m12 * v1 / v2 - l2 * v2**2 / 2 - l345 * v1**2 / 2, msg="m22sq")


def test_mass_blocks(thdm):
    """CP-even block = Branco et al. Eq. (7) (= GH Eqs. 12–13); CP-odd and charged blocks
    ∝ [[v2², −v1v2], [−v1v2, v1²]] with one zero eigenvalue each (Goldstones)."""
    e = thdm.extra
    v1, v2, m12 = e["v1"].s, e["v2"].s, e["m12sq"].s
    l1, l2, l3, l4, l5 = (q.s for q in e["lams"])
    l345 = l3 + l4 + l5
    M_even_lit = sp.Matrix([[m12 * v2 / v1 + l1 * v1**2, -m12 + l345 * v1 * v2],
                            [-m12 + l345 * v1 * v2, m12 * v1 / v2 + l2 * v2**2]])
    G = sp.Matrix([[v2**2, -v1 * v2], [-v1 * v2, v1**2]])
    M_odd_lit = (m12 / (v1 * v2) - l5) * G
    M_ch_lit = (m12 / (v1 * v2) - (l4 + l5) / 2) * G
    for name, M, lit in (("even", e["M_even"], M_even_lit), ("odd", e["M_odd"], M_odd_lit),
                         ("charged", e["M_ch"], M_ch_lit)):
        for a in range(2):
            for b in range(2):
                assert_dual_equal(M[a, b], lit[a, b], msg=f"M_{name}[{a},{b}]")
    assert sp.simplify(e["M_odd"].det()) == 0 and sp.simplify(e["M_ch"].det()) == 0


def test_mA_mHp_gunion_haber_eq10_eq11(thdm):
    """GH Eq. (10): m_A² = m12²/(sβcβ) − λ5 v²; Eq. (11): m_H±² = m_A² + ½v²(λ5 − λ4)."""
    e = thdm.extra
    v, beta, m12 = e["v"].s, e["beta"].s, e["m12sq"].s
    l1, l2, l3, l4, l5 = (q.s for q in e["lams"])
    res = {e["v1"].s: v * sp.cos(beta), e["v2"].s: v * sp.sin(beta)}
    mA2 = (e["MA0"].expr**2).subs(res)
    mHp2 = (e["MHp"].expr**2).subs(res)
    mA2_lit = m12 / (sp.sin(beta) * sp.cos(beta)) - l5 * v**2
    assert_dual_equal(mA2, mA2_lit, msg="m_A^2")
    assert_dual_equal(mHp2, mA2_lit + v**2 * (l5 - l4) / 2, msg="m_H+^2")


def test_spectrum_and_rotations_at_benchmark(thdm):
    e, vals = thdm.extra, thdm.values()
    mh, mH, mA, mHp = (vals[e[k].s] for k in ("MH0", "MHH", "MA0", "MHp"))
    assert 0 < mh < mH and mA > 0 and mHp > 0
    alpha_sol = e["rot_even"].angle_solution
    ok, res = e["rot_even"].check(e["M_even"], simplifier=lambda x: sp.nsimplify(
        sp.simplify(x.subs(e["alpha"].s, alpha_sol)), rational=False))
    assert ok, res
    for rot, M in ((e["rot_odd"], e["M_odd"]), (e["rot_ch"], e["M_ch"])):
        ok, res = rot.check(M.subs({e["v1"].s: e["v"].s * sp.cos(e["beta"].s),
                                    e["v2"].s: e["v"].s * sp.sin(e["beta"].s)}))
        assert ok, res


def test_goldstone_count_and_gauge_masses(thdm):
    p, e, vals = thdm.pieces, thdm.extra, thdm.values()
    W1, W2, W3 = p.W.components
    Mg = thdm.model.gauge_mass_matrix([W1, W2, W3, p.B.components[0]])
    assert massive_gauge_boson_count(Mg, vals) == 3
    n_g = zero_eigenvalue_count(e["M_odd"], vals) + 2 * zero_eigenvalue_count(e["M_ch"], vals)
    assert n_g == 3
    v1, v2, g = e["v1"].s, e["v2"].s, p.gw.s
    assert_dual_equal(Mg[0, 0], g**2 * (v1**2 + v2**2) / 4, msg="m_W^2 = g^2 v^2/4")


def test_fermion_masses(thdm):
    """m_b = y_b v1/√2, m_τ = y_τ v1/√2, m_t = y_t v2/√2 — equal to the inputs."""
    p, e = thdm.pieces, thdm.extra
    i, j = p.idx
    Ll, eR, QL, uR, dR = (p.fermions[k] for k in ("Ll", "eR", "QL", "uR", "dR"))
    res = thdm.params.resolve()
    cases = {"tau": (p.yukawa["yukawa_tau"], Ll.bar_components[1], eR.components[0], p.masses["MTA"]),
             "t": (p.yukawa["yukawa_t"], QL.bar_components[0], uR.components[0], p.masses["MT"]),
             "b": (p.yukawa["yukawa_b"], QL.bar_components[3], dR.components[0], p.masses["MB"])}
    for name, (L, bar, fld, M) in cases.items():
        m = fermion_mass_matrix(L, bar, fld, thdm.model.vacuum, 1, (i, j), gamma=diracPR)[0, 0]
        assert_dual_equal(m.subs(res), M.s, msg=f"m_{name}")
