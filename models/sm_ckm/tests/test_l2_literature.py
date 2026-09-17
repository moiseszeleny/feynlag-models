"""L2: CKM structure against the PDG 2024 CKM review (see metadata → literature_checks)."""

import pytest
import sympy as sp

from feynlag import Bilinear, DiracGamma, diracPL, diracPR, extract_fermion_vertices
from feynlag_models.checks import assert_dual_equal

mu = sp.Symbol("mu", integer=True)
gL, gR = DiracGamma(mu) * diracPL, DiracGamma(mu) * diracPR


def _angles(ckm):
    by_name = {q.name: q.s for q in ckm.extra["ckm_params"]}
    return [by_name[n] for n in ("th12", "th13", "th23", "deltaCP")]


@pytest.fixture(scope="module")
def table(ckm):
    return ckm.fermion_table()


def _coupling(table, bar, gamma, fld, boson):
    return table.get((bar, gamma, fld), {}).get(1, {}).get((boson,), sp.S.Zero)


def test_ckm_standard_parametrization_and_unitarity(ckm):
    """V is the product R23 · U13(δ) · R12 of PDG 2024 Eq. (12.3), first form, built
    here independently of feynlag's element-by-element matrix; and V†V = 1."""
    th12, th13, th23, d = _angles(ckm)
    c, s = sp.cos, sp.sin
    R23 = sp.Matrix([[1, 0, 0], [0, c(th23), s(th23)], [0, -s(th23), c(th23)]])
    U13 = sp.Matrix([[c(th13), 0, s(th13) * sp.exp(-sp.I * d)], [0, 1, 0],
                     [-s(th13) * sp.exp(sp.I * d), 0, c(th13)]])
    R12 = sp.Matrix([[c(th12), s(th12), 0], [-s(th12), c(th12), 0], [0, 0, 1]])
    pdg = R23 * U13 * R12
    V = ckm.extra["V_expr"]
    syms = [th12, th13, th23, d]
    for a in range(3):
        for b in range(3):
            assert_dual_equal(V[a, b], pdg[a, b], syms, msg=f"V[{a},{b}]")
    VdV = V.conjugate().T * V
    for a in range(3):
        for b in range(3):
            assert_dual_equal(VdV[a, b], 1 if a == b else 0, syms, msg=f"(V†V)[{a},{b}]")


def test_charged_current_ckm(ckm, table):
    """W⁺ ū_i d_j = i (g/√2) V_ij γ^μ P_L and W⁻ d̄_j u_i = i (g/√2) V*_ij γ^μ P_L
    (coefficients shown without the i). PDG 2024 Eq. (12.2) has −g/√2: the global
    gauge-coupling sign of discrepancy D-1 (a convention, as in models/sm).
    Cross-check: feynlag's direct CKM insertion (examples/sm_ckm.py) extracts the same."""
    p, b, e = ckm.pieces, ckm.bosons, ckm.extra
    g = p.gw.s
    QL = p.fermions["QL"]
    ubar, uL = QL.bar_components[0], QL.components[0]
    dL, dLbar = e["dLm"][0], e["dLm_bar"][0]
    V, Vsym = e["V_expr"], e["V"]
    defs = {q.s: q.expr for q in e["ckm_params"] if getattr(q, "expr", None) is not None}

    L_insert = g / sp.sqrt(2) * b["Wp"] * sum(
        Vsym[i, j] * Bilinear(ubar[i], gL, dL[j]) for i in range(3) for j in range(3))
    inserted = extract_fermion_vertices(sp.expand(L_insert), [b["Wp"]])

    for i in range(3):
        for j in range(3):
            cp = _coupling(table, ubar[i], gL, dL[j], b["Wp"])
            assert_dual_equal(cp, g / sp.sqrt(2) * V[i, j], msg=f"W+ u{i} d{j}")
            ref = inserted[(ubar[i], gL, dL[j])][1][(b["Wp"],)].xreplace(defs)
            assert_dual_equal(cp, ref, msg=f"W+ u{i} d{j} vs insertion")
            cm = _coupling(table, dLbar[j], gL, uL[i], b["Wm"])
            assert_dual_equal(cm, g / sp.sqrt(2) * sp.conjugate(V[i, j]), msg=f"W- d{j} u{i}")
            # no right-handed charged current
            assert _coupling(table, ubar[i], gR, dL[j], b["Wp"]) == 0


def test_gim_no_tree_level_fcnc(ckm, table):
    """Derived (not imposed): after d'_L = V d_L the Z, γ, h and G⁰ couplings of
    d̄_i d_j vanish for i ≠ j, and the diagonal ones are the one-generation SM
    values Z: g_Z(T³ − Q s_W²), γ: e Q, h: −m_q/v. The cancellation is the
    unitarity Σ_i V_ij V*_ik = δ_jk stated in PDG 2024 Sec. 12.1."""
    p, b, e = ckm.pieces, ckm.bosons, ckm.extra
    g, gp, v = p.gw.s, p.g1.s, p.ew.v.s
    gZ = sp.sqrt(g**2 + gp**2)
    sw2, eQ = gp**2 / (g**2 + gp**2), g * gp / gZ
    dL, dLbar = e["dLm"][0], e["dLm_bar"][0]
    dR, dRbar = p.fermions["dR"].components[0], p.fermions["dR"].bar_components[0]
    res = ckm.params.resolve()
    masses = [p.masses[n].s for n in ("MD", "MS", "MB")]
    Q, T3 = -sp.Rational(1, 3), -sp.Rational(1, 2)
    for i in range(3):
        for j in range(3):
            for boson in ("Z", "A"):
                cL = sp.simplify(_coupling(table, dLbar[i], gL, dL[j], b[boson]))
                cR = sp.simplify(_coupling(table, dRbar[i], gR, dR[j], b[boson]))
                if i != j:
                    assert cL == 0 and cR == 0, (boson, i, j, cL, cR)
            for boson in ("h", "G0"):
                y = sp.simplify(_coupling(table, dLbar[i], diracPR, dR[j], b[boson]))
                if i != j:
                    assert y == 0, (boson, i, j, y)
        cZ = _coupling(table, dLbar[i], gL, dL[i], b["Z"])
        assert_dual_equal(cZ, gZ * (T3 - Q * sw2), msg=f"Z d{i}L")
        assert_dual_equal(_coupling(table, dRbar[i], gR, dR[i], b["Z"]), gZ * (-Q * sw2), msg=f"Z d{i}R")
        assert_dual_equal(_coupling(table, dLbar[i], gL, dL[i], b["A"]), eQ * Q, msg=f"A d{i}")
        ch = _coupling(table, dLbar[i], diracPR, dR[i], b["h"]).subs(res)
        assert_dual_equal(sp.I * ch, -sp.I * masses[i] / v, msg=f"h d{i} d{i}")


def test_jarlskog_invariant(ckm):
    """J = Im(V_us V_cb V*_ub V*_cs), the definition of PDG 2024 Sec. 12.1 with
    (i,j,k,l) = (u,s,c,b). Its closed form c12 c23 c13² s12 s23 s13 sin δ is derived
    here, not quoted. At the benchmark (the central angles of Eq. 12.28) J lies in the
    fit band J = (3.12 +0.13 −0.12) × 10⁻⁵ quoted just above Eq. (12.28)."""
    th12, th13, th23, d = _angles(ckm)
    V = ckm.extra["V_expr"]
    J = sp.im(sp.expand(V[0, 1] * V[1, 2] * sp.conjugate(V[0, 2]) * sp.conjugate(V[1, 1])))
    c, s = sp.cos, sp.sin
    closed = c(th12) * c(th23) * c(th13)**2 * s(th12) * s(th23) * s(th13) * s(d)
    assert_dual_equal(J, closed, [th12, th13, th23, d], msg="J")
    J_num = float(closed.subs(ckm.values()))
    assert 3.00e-5 <= J_num <= 3.25e-5, J_num


#: PDG 2024 Eq. (12.27): fit magnitudes (central, −err, +err)
PDG_ABS_V = [
    [(0.97435, 0.00016, 0.00016), (0.22501, 0.00068, 0.00068), (0.003732, 0.000085, 0.000090)],
    [(0.22487, 0.00068, 0.00068), (0.97349, 0.00016, 0.00016), (0.04183, 0.00069, 0.00079)],
    [(0.00858, 0.00017, 0.00019), (0.04111, 0.00068, 0.00077), (0.999118, 0.000034, 0.000029)],
]


def test_ckm_magnitudes_at_benchmark(ckm):
    """The benchmark angles (central values of PDG 2024 Eq. 12.28) give every |V_ij|
    inside the 1σ band of the fit magnitudes, Eq. (12.27); the sines are the inputs."""
    vals = ckm.values()
    V = ckm.extra["V_expr"]
    for i in range(3):
        for j in range(3):
            central, lo, hi = PDG_ABS_V[i][j]
            mag = abs(complex(V[i, j].subs(vals)))
            assert central - lo <= mag <= central + hi, (i, j, mag)
    th12, th13, th23, _ = _angles(ckm)
    for th, key in ((th12, "s12"), (th13, "s13"), (th23, "s23")):
        assert abs(float(sp.sin(th).subs(vals)) - ckm.benchmark[key]) < 1e-12


def test_charge_and_hermiticity_pairing(ckm):
    """Every bosonic vertex conserves charge; declared charges agree with the
    vacuum-derived operator; every vertex has its hermitian partner."""
    report = ckm.model.validate(invariance=False, anomalies=False,
                                charges=ckm.charges, fields=ckm.boson_list,
                                conjugate_map=ckm.cmap, conjugates=ckm.conjugates)
    assert report.ok, report.summary()
    for name in ("charge_conservation", "charge_consistency", "hermiticity_pairing"):
        assert report.checks[name] is not None and report.checks[name].ok
