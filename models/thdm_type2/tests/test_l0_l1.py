"""L0/L1 for the type-II 2HDM: invariance, soft Z2 breaking, tadpoles, three mass blocks."""

import sympy as sp

from feynlag import FL_I, FL_J, check_discrete_invariance, diracPR, fermion_mass_matrix
from feynlag_models.checks import (assert_dual_equal, massive_gauge_boson_count,
                                   zero_eigenvalue_count)


def test_validate_invariance_and_anomalies(thdm):
    report = thdm.model.validate()
    assert report.ok, report.summary()
    assert report.checks["anomalies"] is not None and report.checks["anomalies"].ok


def test_z2_softly_broken_only_by_m12sq(thdm):
    """Z2 (H2 → −H2, u_R → −u_R) holds for every potential and Yukawa term except the
    named soft term −m12² (H1†H2 + h.c.), kinetic (Dmu) terms included."""
    Z2 = thdm.extra["Z2"]
    failing = []
    for term in thdm.model.lagrangian:
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
    Ll, eR, QL, uR, dR = (p.fermions[k] for k in ("Ll", "eR", "QL", "uR", "dR"))
    res = thdm.params.resolve()
    cases = {"tau": (p.yukawa["yukawa_tau"], Ll.bar_components[1], eR.components[0], p.masses["MTA"]),
             "t": (p.yukawa["yukawa_t"], QL.bar_components[0], uR.components[0], p.masses["MT"]),
             "b": (p.yukawa["yukawa_b"], QL.bar_components[3], dR.components[0], p.masses["MB"])}
    for name, (L, bar, fld, M) in cases.items():
        m = fermion_mass_matrix(L, bar, fld, thdm.model.vacuum, 1, (FL_I, FL_J), gamma=diracPR)[0, 0]
        assert_dual_equal(m.subs(res), M.s, msg=f"m_{name}")


def test_benchmark_matches_physical_inputs(thdm):
    """The λ_i in metadata.benchmark.inputs are the inversion of
    benchmark.derived_from.physical; feynlag must re-derive that physical point."""
    import math
    from feynlag_models import MODELS_DIR
    from feynlag_models import metadata as md
    phys = md.load(MODELS_DIR / "thdm_type2")["benchmark"]["derived_from"]["physical"]
    e, vals = thdm.extra, thdm.values()
    for name in ("MH0", "MHH", "MA0", "MHp"):
        assert abs(vals[e[name].s] - phys[name]) < 1e-4, (name, vals[e[name].s], phys[name])
    assert abs(vals[e["tanb"].s] - phys["tanb"]) < 1e-12
    assert abs(vals[e["m12sq"].s] - phys["m12sq"]) < 1e-9
    cba = math.cos(vals[e["beta"].s] - vals[e["alpha"].s])
    assert abs(cba - phys["cos_beta_minus_alpha"]) < 1e-5, cba


def _gh_lambdas(v, m_light, m_heavy, tanb, sin_bma, mA, mHp, m12sq):
    """λ1..λ5 from the physical basis, Gunion–Haber Eqs. (10)–(13) with λ6 = λ7 = 0:
    (H, h) = R(α)(ρ1, ρ2), m_H = m_heavy ≥ m_h = m_light, α = β − asin(sin(β − α))."""
    import math
    beta = math.atan(tanb)
    sb, cb = math.sin(beta), math.cos(beta)
    alpha = beta - math.asin(sin_bma)
    c, s = math.cos(alpha), math.sin(alpha)
    # M = Rᵀ diag(m_H², m_h²) R
    M11 = c * c * m_heavy**2 + s * s * m_light**2
    M22 = s * s * m_heavy**2 + c * c * m_light**2
    M12 = c * s * (m_heavy**2 - m_light**2)
    lam5 = m12sq / (sb * cb * v**2) - mA**2 / v**2
    lam4 = lam5 - 2 * (mHp**2 - mA**2) / v**2
    lam345 = (M12 + m12sq) / (v**2 * sb * cb)
    return dict(lam1=(M11 - m12sq * tanb) / (v**2 * cb**2), lam2=(M22 - m12sq / tanb) / (v**2 * sb**2),
                lam3=lam345 - lam4 - lam5, lam4=lam4, lam5=lam5), alpha, (M11, M22, M12)


def test_labels_follow_mass_at_an_inverted_point():
    """UG-4: at a point with M11 < M22 (α_GH > π/4) h is still the lighter CP-even state
    (CONVENTIONS.md, Gunion–Haber's branch m_H ≥ m_h) and the model's α is α_GH. Point:
    tan β = 2, sin(β − α) = 0.3, m_h = 95, m_H = 125.2, m_A = 300, m_H± = 600 GeV,
    m12² = 6000 GeV² (feynlag-anomalies higgs_95gev step 4)."""
    import math
    from models.thdm_type2.model import benchmark_point, build
    bench = benchmark_point()
    lams, alpha_gh, (M11, M22, _) = _gh_lambdas(bench["v"], 95.0, 125.2, 2.0, 0.3, 300.0, 600.0, 6000.0)
    assert M11 < M22 and alpha_gh > math.pi / 4                  # really the inverted regime
    thdm = build(dict(bench, tanb=2.0, m12sq=6000.0, **lams))
    e, vals = thdm.extra, thdm.values()
    mh, mH = vals[e["MH0"].s], vals[e["MHH"].s]
    assert abs(mh / 95.0 - 1) < 1e-6 and abs(mH / 125.2 - 1) < 1e-6, (mh, mH)
    alpha, beta = vals[e["alpha"].s], vals[e["beta"].s]
    assert abs(alpha - alpha_gh) < 1e-9, (alpha, alpha_gh)
    assert abs(math.sin(beta - alpha) - 0.3) < 1e-9
    # R(α) M Rᵀ is diagonal with the heavier state first, relative to the size of M
    D = e["rot_even"].apply(e["M_even"]).subs(e["alpha"].s, e["rot_even"].angle_solution).subs(vals)
    D = [[float(sp.N(D[i, j])) for j in range(2)] for i in range(2)]
    assert abs(D[0][1]) < 1e-12 * abs(D[0][0]) and D[0][0] > D[1][1] > 0, D


def test_alpha_branch_is_atan2():
    """The branch shift of ``alpha_branch`` turns feynlag's principal ½ atan(2M12/(M11−M22)) into
    ½ atan2(2M12, M11−M22) in all three regions, and R(α) then puts the heavier state first."""
    import math
    from feynlag import diagonalize_orthogonal_2x2
    from models.thdm_type2.model import alpha_branch
    a, H, h = sp.symbols("a H h")
    for M11, M22, M12 in ((5.0, 2.0, 0.7), (2.0, 5.0, 0.7), (2.0, 5.0, -0.7), (5.0, 2.0, -0.7)):
        M = sp.Matrix([[M11, M12], [M12, M22]])
        rot = diagonalize_orthogonal_2x2(M, sp.symbols("r1 r2"), [H, h], angle=a)
        alpha = float(rot.angle_solution) + alpha_branch(M, {}) * math.pi / 2
        assert abs(alpha - math.atan2(2 * M12, M11 - M22) / 2) < 1e-12, (M11, M22, M12)
        mH2, mh2 = (float(x.subs(a, alpha)) for x in rot.masses_squared(M, simplifier=sp.expand))
        assert mH2 > mh2, (M11, M22, M12)


# ------------------------------------------------- feynlag 0.4.0+ API (guided basis, coverage)

def _inverted_bench():
    from models.thdm_type2.model import benchmark_point
    bench = benchmark_point()
    lams, _alpha, _M = _gh_lambdas(bench["v"], 95.0, 125.2, 2.0, 0.3, 300.0, 600.0, 6000.0)
    return dict(bench, tanb=2.0, m12sq=6000.0, **lams)


def _branch_case(bundle):
    import math
    from models.thdm_type2.model import alpha_branch
    e, vals = bundle.extra, bundle.values()
    M, rot = e["M_even"], e["rot_even"]
    k = alpha_branch(M, vals)
    principal = sp.atan(2 * M[0, 1] / (M[0, 0] - M[1, 1])) / 2
    # diagonalize(values=) chose exactly alpha_branch's shift of the principal branch
    assert sp.simplify(rot.angle_solution - principal - k * sp.pi / 2) == 0
    assert sp.simplify(e["alpha"].expr - rot.angle_solution) == 0
    M11, M22, M12 = (float(sp.N(M[a, b].subs(vals))) for a, b in ((0, 0), (1, 1), (0, 1)))
    assert bundle.extra["branch_valid_for"] == (1 if M11 > M22 else -1, 1 if M12 > 0 else -1)
    alpha = float(vals[e["alpha"].s])
    assert alpha == _approx(0.5 * math.atan2(2 * M12, M11 - M22))
    assert vals[e["MHH"].s] >= vals[e["MH0"].s]                  # m_H ≥ m_h
    return k


def _approx(x):
    import pytest
    return pytest.approx(x, rel=1e-12, abs=1e-14)


def test_diagonalize_branch_matches_alpha_branch(thdm):
    """``diagonalize(even, names=["H", "h"], angle=alpha, values=…)`` puts the heavier state first:
    its angle is the principal ½ atan(2M12/(M11 − M22)) shifted by ``alpha_branch``·π/2, i.e.
    Gunion–Haber's ½ atan2(2M12, M11 − M22) (CONVENTIONS.md, UG-4), with ``branch_valid_for`` the
    signs of (M11 − M22, M12). At the benchmark (M11 > M22, no shift) and at the inverted point of
    ``test_labels_follow_mass_at_an_inverted_point`` (M11 < M22, shift +π/2)."""
    from models.thdm_type2.model import build
    assert _branch_case(thdm) == 0
    assert _branch_case(build(_inverted_bench())) == 1


def test_goldstone_fixed_rotations(thdm):
    """The CP-odd and charged blocks rotate by ``rotation_2x2(β)`` fixed by the Goldstone
    direction (v1, v2)/v: (η1, η2) → (G0, A0), (H1⁺, H2⁺) → (G⁺, H⁺), with tan β = v2/v1 attached;
    G⁻ and H⁻ are the conjugate partners."""
    from feynlag import rotation_2x2
    e, b = thdm.extra, thdm.bosons
    beta = e["beta"].s
    H1, H2 = e["H1"], e["H2"]
    for rot, old, new in ((e["rot_odd"], [H1.H10_i, H2.H20_i], [b["G0"], b["A0"]]),
                          (e["rot_ch"], [H1.H1p, H2.H2p], [b["Gp"], b["Hp"]])):
        assert list(rot.old_fields) == old and list(rot.new_fields) == new
        assert sp.Matrix(rot.matrix) == rotation_2x2(beta)
        assert rot.angle_relation == sp.Eq(sp.tan(beta), e["v2"].s / e["v1"].s)
    assert thdm.cmap == {sp.conjugate(b["Gp"]): b["Gm"], sp.conjugate(b["Hp"]): b["Hm"]}
    assert sp.simplify(e["beta"].expr - sp.atan(e["tanb"].s)) == 0


def test_physical_registry(thdm):
    """Charges (derived from the vacuum), conjugate pairs and Goldstones from ``model.physical``."""
    b = thdm.bosons
    assert thdm.charges == {b["h"]: 0, b["H"]: 0, b["A0"]: 0, b["G0"]: 0, b["Gp"]: 1, b["Gm"]: -1,
                            b["Hp"]: 1, b["Hm"]: -1, b["Z"]: 0, b["A"]: 0, b["Wp"]: 1, b["Wm"]: -1}
    assert thdm.conjugates == {b["Gp"]: b["Gm"], b["Gm"]: b["Gp"], b["Hp"]: b["Hm"],
                               b["Hm"]: b["Hp"], b["Wp"]: b["Wm"], b["Wm"]: b["Wp"]}
    assert thdm.goldstones == (b["G0"], b["Gp"], b["Gm"])
    assert list(b) == ["h", "H", "A0", "G0", "Gp", "Gm", "Hp", "Hm", "Z", "A", "Wp", "Wm"]


def test_term_coverage(thdm):
    """On the Model as built (Z2 not declared: m12² breaks it softly) the potential and Yukawas
    contain the CONVENTIONS.md terms, ``V = m11²H1†H1 + m22²H2†H2 − m12²(H1†H2 + h.c.) + ½λ1(H1†H1)²
    + ½λ2(H2†H2)² + λ3(H1†H1)(H2†H2) + λ4|H1†H2|² + ½λ5[(H1†H2)² + h.c.]`` and the type-II
    Yukawas, with no remainder. What is missing is exactly what a hard Z2 forbids: λ6, λ7 and the
    wrong-doublet Yukawas."""
    e, ys = thdm.extra, thdm.pieces.yukawa_params
    l1, l2, l3, l4, l5 = (q.s for q in e["lams"])
    tc = thdm.model.term_coverage()
    assert tc.unmatched == {}
    assert {t.label: c for t, c in tc.present} == {
        "(H1†H1)": e["m11sq"].s, "(H2†H2)": e["m22sq"].s, "(H1†H2)": -e["m12sq"].s,
        "(H1†H1) (H1†H1)": l1 / 2, "(H2†H2) (H2†H2)": l2 / 2, "(H1†H1) (H2†H2)": l3,
        "(H1†H2) (H2†H1)": l4, "(H1†H2) (H1†H2)": l5 / 2,
        "Ll̄·H1 eR": ys["ytau"].s, "QL̄·H1 dR": ys["yb"].s, "QL̄·H2̃ uR": ys["yt"].s,
    }
    assert {t.label for t in tc.missing} == {"(H1†H1) (H1†H2)", "(H1†H2) (H2†H2)",
                                             "Ll̄·H2 eR", "QL̄·H2 dR", "QL̄·H1̃ uR"}


def test_summary_and_parameters(thdm):
    """``summary()``: two hypercharge-½ doublets replace the SM Higgs; every parameter is listed
    and ``check_parameters()`` finds no undeclared symbol."""
    assert thdm.params is thdm.pieces.params        # one ParameterSet, extended in place
    s = thdm.model.summary()
    assert s.field_header[:5] == ["field", "type", "SU2L", "U1Y", "SU3c"]
    rows = {r[0]: tuple(str(x) for x in r[1:5]) for r in s.field_rows}
    assert rows["H1"] == rows["H2"] == ("scalar", "2", "1/2", "1")
    assert set(rows) == {"H1", "H2", "W", "B", "G", "Ll", "eR", "QL", "uR", "dR"}
    assert [r[0] for r in s.param_rows] == [q.name for q in thdm.params]
    assert thdm.model.check_parameters().undeclared == []


def test_mA_mHp_forms_symbolically_equal_to_previous(thdm):
    """``diagonalize`` writes ``m_A² = (v1²+v2²)(m12² − λ5 v1v2)/(v1v2)`` and
    ``m_H±² = (v1²+v2²)(2m12² − (λ4+λ5)v1v2)/(2v1v2)``; the forms exported before the 0.4.0
    migration had ``(v1 cos β + v2 sin β)²`` in place of ``v1² + v2²``. With ``v1 = v cos β``,
    ``v2 = v sin β`` (v, β > 0) the two are symbolically identical."""
    e = thdm.extra
    v1, v2, beta, m12 = e["v1"].s, e["v2"].s, e["beta"].s, e["m12sq"].s
    l4, l5 = e["lams"][3].s, e["lams"][4].s
    mA2, mHp2 = sp.expand(e["MA0"].expr ** 2), sp.expand(e["MHp"].expr ** 2)
    assert sp.expand(mA2 - (v1**2 + v2**2) * (m12 - l5 * v1 * v2) / (v1 * v2)) == 0
    assert sp.expand(mHp2 - (v1**2 + v2**2) * (2 * m12 - (l4 + l5) * v1 * v2) / (2 * v1 * v2)) == 0
    c2 = (v1 * sp.cos(beta) + v2 * sp.sin(beta)) ** 2
    old_mA2 = c2 * (m12 - l5 * v1 * v2) / (v1 * v2)
    old_mHp2 = c2 * (m12 - (l4 + l5) * v1 * v2 / 2) / (v1 * v2)
    v, b = sp.symbols("v b", positive=True)
    on_vev = {v1: v * sp.cos(b), v2: v * sp.sin(b), beta: b}
    for new, old in ((mA2, old_mA2), (mHp2, old_mHp2)):
        assert sp.simplify((old - new).subs(on_vev)) == 0


def test_lagrangian_params_snapshot(thdm):
    """The benchmark snapshot ``diagonalize(values=…)`` evaluates is exactly the Lagrangian parameters:
    the inputs, the β/v1/v2 and m11²/m22² internals and the Yukawas, in the bundle's order. It
    excludes the widths and the mass and angle internals declared after it (``alpha`` is not
    defined until ``diagonalize`` itself)."""
    lp, names = thdm.extra["lagrangian_params"], [q.name for q in thdm.params]
    assert lp is not thdm.params
    assert [q.name for q in lp] == names[:len(lp)] == [
        "gw", "g1", "gs", "v", "tanb", "m12sq", "lam1", "lam2", "lam3", "lam4", "lam5",
        "MT", "MB", "MTA", "beta", "v1", "v2", "m11sq", "m22sq", "yt", "yb", "ytau"]
    assert names[len(lp):] == ["WZ", "WW", "WH", "WT", "WHH", "WA0", "WHp",
                               "alpha", "MW", "MZ", "MH0", "MHH", "MA0", "MHp"]
    assert all(lp[q.name] is thdm.params[q.name] for q in lp)
