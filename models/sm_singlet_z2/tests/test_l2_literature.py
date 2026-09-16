"""L2: Robens–Stefaniak (arXiv:1501.02234v2) Eqs. (3), (6)–(13) and
Pruna–Robens (arXiv:1303.1150v3) Eqs. (2), (5)–(11).

Parameter map (their → ours): λ1 → lam, λ2 → lamS, λ3 → lamHS, x → vS, m² → mu2,
−μ² → muS2/2·(…): with S_theirs = (h0 + x)/√2 their −μ²S² + λ2 S⁴ + λ3 Φ†Φ S² equals our
½ μ_S² S² + ¼ λ_S S⁴ + ½ λ_HS Φ†Φ S² for S_ours = v_S + s. Their rotation (Eq. 10)
h = cα h̃ − sα h0 versus feynlag's h1 = cθ h + sθ s gives α = −θ.
"""

import sympy as sp

from feynlag import diracPR
from feynlag_models.checks import assert_dual_equal


#: The closed forms below are branch-dependent (they contain √ and atan). They are
#: verified in the regime of the benchmark, λ_S v_S² > λ v² (h1 lighter and SM-like),
#: made explicit by the positive dummy D = λ_S v_S² − λ v² (CONVENTIONS.md: positive
#: symbols under square roots).
D = sp.Symbol("D", positive=True)


def _lit(e):
    lam, v = e["ew"].lam.s, e["ew"].v.s
    lamS, lamHS, x = e["lamS"].s, e["lamHS"].s, e["vS"].s
    root = sp.sqrt((lam * v**2 - lamS * x**2) ** 2 + (lamHS * x * v) ** 2)
    return lam, v, lamS, lamHS, x, root


def _branch(e):
    """Substitution fixing the benchmark branch λ_S v_S² = λ v² + D, D > 0."""
    lam, v, lamS, lamHS, x, _ = _lit(e)
    return {lamS: (lam * v**2 + D) / x**2}


def _eq(e, a, b, msg):
    br = _branch(e)
    assert_dual_equal(sp.sympify(a).subs(br), sp.sympify(b).subs(br), msg=msg)


def test_mass_matrix_eq7(xsm):
    """Robens–Stefaniak Eq. (7): M² = [[2λ1 v², λ3 v x], [λ3 v x, 2λ2 x²]]."""
    e = xsm.extra
    lam, v, lamS, lamHS, x, _ = _lit(e)
    M_lit = sp.Matrix([[2 * lam * v**2, lamHS * v * x], [lamHS * v * x, 2 * lamS * x**2]])
    for a in range(2):
        for b in range(2):
            assert_dual_equal(e["M_even"][a, b], M_lit[a, b], msg=f"Eq.(7)[{a},{b}]")


def test_mass_eigenvalues_eq8_eq9(xsm):
    """Eqs. (8),(9): m²_{h,H} = λ1 v² + λ2 x² ∓ √((λ1v² − λ2x²)² + (λ3 x v)²)."""
    e = xsm.extra
    lam, v, lamS, lamHS, x, root = _lit(e)
    m1sq, m2sq = e["MH1"].expr**2, e["MH2"].expr**2
    subs = {e["theta"].s: e["rot"].angle_solution}
    lit_h, lit_H = lam * v**2 + lamS * x**2 - root, lam * v**2 + lamS * x**2 + root
    _eq(e, m1sq.subs(subs), lit_h, "Eq.(8) m_h^2")
    _eq(e, m2sq.subs(subs), lit_H, "Eq.(9) m_H^2")
    # numeric: the ordering (h1 lighter) at the benchmark
    vals = xsm.values()
    assert abs(float(m1sq.subs(vals)) - float(lit_h.subs(vals))) < 1e-6 * float(lit_H.subs(vals))
    assert abs(float(m2sq.subs(vals)) - float(lit_H.subs(vals))) < 1e-6 * float(lit_H.subs(vals))


def test_mixing_angle_eq11_eq12(xsm):
    """Eqs. (11),(12): sin 2α = λ3 x v/√·, cos 2α = (λ2 x² − λ1 v²)/√· with α = −θ,
    i.e. tan 2θ = λ3 x v/(λ1 v² − λ2 x²) (feynlag's tan-2θ relation)."""
    e = xsm.extra
    lam, v, lamS, lamHS, x, root = _lit(e)
    tan2theta = e["rot"].angle_relation.rhs
    assert_dual_equal(tan2theta, lamHS * x * v / (lam * v**2 - lamS * x**2), msg="tan 2θ")
    theta = e["rot"].angle_solution
    _eq(e, sp.sin(-2 * theta), lamHS * x * v / root, "Eq.(11) sin 2α")
    _eq(e, sp.cos(2 * theta), (lamS * x**2 - lam * v**2) / root, "Eq.(12) cos 2α")


def test_coupling_rescaling(xsm):
    """Below Eq. (10): h (H) couplings to SM particles are the SM ones × cos α (sin α).
    Checked on h1VV, h1ZZ and h1 f f̄ for f = t, b, τ (cos θ = cos α)."""
    e, b, p = xsm.extra, xsm.bosons, xsm.pieces
    th = e["theta"].s
    g, gp, v = p.gw.s, p.g1.s, p.ew.v.s
    rules = xsm.model.feynman_rules(xsm.boson_list, sector="kinetic",
                                    conjugate_map=xsm.cmap, simplifier=sp.simplify)

    def rule(*legs):
        return rules[tuple(sorted(legs, key=lambda f: f.sort_key()))]

    assert_dual_equal(rule(b["h1"], b["Wp"], b["Wm"]), sp.I * g**2 * v / 2 * sp.cos(th), msg="h1WW")
    assert_dual_equal(rule(b["h2"], b["Wp"], b["Wm"]), -sp.I * g**2 * v / 2 * sp.sin(th), msg="h2WW")
    assert_dual_equal(rule(b["h1"], b["Z"], b["Z"]), sp.I * (g**2 + gp**2) * v / 2 * sp.cos(th), msg="h1ZZ")
    # sum rule: g²(h1VV) + g²(h2VV) = g²(hVV)_SM
    assert_dual_equal(rule(b["h1"], b["Wp"], b["Wm"])**2 + rule(b["h2"], b["Wp"], b["Wm"])**2,
                      (sp.I * g**2 * v / 2)**2, msg="sum rule")

    tab = xsm.fermion_table()
    i = p.idx[0]
    yuk = {y.s: y.expr for y in p.yukawa_params.values()}
    for name, bar, fld, M in (
            ("tau", p.fermions["Ll"].bar_components[1], p.fermions["eR"].components[0], p.masses["MTA"]),
            ("t", p.fermions["QL"].bar_components[0], p.fermions["uR"].components[0], p.masses["MT"]),
            ("b", p.fermions["QL"].bar_components[3], p.fermions["dR"].components[0], p.masses["MB"])):
        c1 = tab[(bar[i], diracPR, fld[i])][1][(b["h1"],)].subs(yuk)
        c2 = tab[(bar[i], diracPR, fld[i])][1][(b["h2"],)].subs(yuk)
        assert_dual_equal(sp.I * c1, -sp.I * M.s / v * sp.cos(th), msg=f"h1 {name}{name}")
        assert_dual_equal(sp.I * c2, sp.I * M.s / v * sp.sin(th), msg=f"h2 {name}{name}")


def test_lambda3_from_masses_eq13(xsm):
    """Eq. (13): λ3 = (m_H² − m_h²) sin 2α/(2 v x)."""
    e = xsm.extra
    lam, v, lamS, lamHS, x, root = _lit(e)
    theta = e["rot"].angle_solution
    subs = {e["theta"].s: theta}
    m1sq, m2sq = (e["MH1"].expr**2).subs(subs), (e["MH2"].expr**2).subs(subs)
    _eq(e, (m2sq - m1sq) * sp.sin(-2 * theta) / (2 * v * x), lamHS, "Eq.(13)")


def test_decoupling_lamHS_to_zero(xsm):
    """λ_HS → 0 ⇒ θ → 0 and the SM Higgs mass is recovered (physics: no portal, no mixing)."""
    e = xsm.extra
    lam, v = e["ew"].lam.s, e["ew"].v.s
    theta0 = sp.simplify(e["rot"].angle_solution.subs(e["lamHS"].s, 0))
    assert theta0 == 0
    m1sq = (e["MH1"].expr**2).subs(e["theta"].s, e["rot"].angle_solution).subs(e["lamHS"].s, 0)
    assert sp.simplify(m1sq - 2 * lam * v**2) == 0
