"""L2: 2HDM type-II couplings against Branco et al. (arXiv:1106.0034) Eq. (16),
Table 2 and the hVV statement after Table 2, and Gunion–Haber (hep-ph/0207010).

Convention note (CONVENTIONS.md): (H, h) = R(α)(ρ1, ρ2), (G⁰, A) = R(β)(η1, η2),
(G⁺, H⁺) = R(β)(H1⁺, H2⁺). The overall phase of A and H⁺ is a convention; the tests
below pin magnitudes and *relative* signs exactly and record the overall sign found
relative to Branco et al. Eq. (16).
"""

import pytest
import sympy as sp

from feynlag import diracPL, diracPR
from feynlag_models.checks import assert_dual_equal


def _rule(rules, *legs):
    return rules[tuple(sorted(legs, key=lambda f: f.sort_key()))]


def _res(e):
    return {e["v1"].s: e["v"].s * sp.cos(e["beta"].s), e["v2"].s: e["v"].s * sp.sin(e["beta"].s)}


def test_hVV_HVV_sin_cos_beta_minus_alpha(thdm):
    """hVV = SM × sin(β−α), HVV = SM × cos(β−α), no AVV (Branco et al. after Table 2;
    GH Sec. 2). SM: hWW = i g m_W, hZZ = i g_Z m_Z."""
    e, b, p = thdm.extra, thdm.bosons, thdm.pieces
    g, gp, v = p.gw.s, p.g1.s, e["v"].s
    al, be = e["alpha"].s, e["beta"].s
    rules = thdm.model.feynman_rules(thdm.boson_list, sector="kinetic",
                                     conjugate_map=thdm.cmap, simplifier=sp.simplify)
    res = _res(e)
    assert_dual_equal(_rule(rules, b["h"], b["Wp"], b["Wm"]).subs(res), sp.I * g**2 * v / 2 * sp.sin(be - al), msg="hWW")
    assert_dual_equal(_rule(rules, b["H"], b["Wp"], b["Wm"]).subs(res), sp.I * g**2 * v / 2 * sp.cos(be - al), msg="HWW")
    assert_dual_equal(_rule(rules, b["h"], b["Z"], b["Z"]).subs(res), sp.I * (g**2 + gp**2) * v / 2 * sp.sin(be - al), msg="hZZ")
    assert_dual_equal(_rule(rules, b["H"], b["Z"], b["Z"]).subs(res), sp.I * (g**2 + gp**2) * v / 2 * sp.cos(be - al), msg="HZZ")
    vectors = {b["Wp"], b["Wm"], b["Z"], b["A"]}
    for key in rules:                      # no A0 V V vertex (A0 Z h / A0 Z H VSS vertices are allowed)
        if len(key) == 3 and b["A0"] in key:
            assert sum(1 for f in key if f in vectors) < 2, key


def test_neutral_yukawa_xi_factors_table2(thdm, ftab):
    """Branco et al. Eq. (16) + Table 2 (type II column):
    L = −Σ_f (m_f/v)[ξ_h^f f̄f h + ξ_H^f f̄f H − i ξ_A^f f̄γ5 f A] with
    ξ_h^u = cα/sβ, ξ_h^{d,ℓ} = −sα/cβ, ξ_H^u = sα/sβ, ξ_H^{d,ℓ} = cα/cβ, ξ_A^u = cotβ, ξ_A^{d,ℓ} = tanβ.
    In chiral components f̄γ5f = f̄P_Rf − f̄P_Lf, so the (f̄_L P_R f_R) A coefficient is
    −i(m_f/v)ξ_A and the (f̄_R P_L f_L) A coefficient is +i(m_f/v)ξ_A."""
    e, b, p = thdm.extra, thdm.bosons, thdm.pieces
    v, al, be = e["v"].s, e["alpha"].s, e["beta"].s
    i = p.idx[0]
    yuk = {y.s: y.expr for y in p.yukawa_params.values()}
    res = _res(e)
    Ll, eR, QL, uR, dR = (p.fermions[k] for k in ("Ll", "eR", "QL", "uR", "dR"))
    xi = {
        "t": (sp.cos(al) / sp.sin(be), sp.sin(al) / sp.sin(be), sp.cot(be)),
        "b": (-sp.sin(al) / sp.cos(be), sp.cos(al) / sp.cos(be), sp.tan(be)),
        "tau": (-sp.sin(al) / sp.cos(be), sp.cos(al) / sp.cos(be), sp.tan(be)),
    }
    legs = {
        "t": (QL.bar_components[0], uR.components[0], uR.bar_components[0], QL.components[0], p.masses["MT"].s),
        "b": (QL.bar_components[3], dR.components[0], dR.bar_components[0], QL.components[3], p.masses["MB"].s),
        "tau": (Ll.bar_components[1], eR.components[0], eR.bar_components[0], Ll.components[1], p.masses["MTA"].s),
    }
    a_sign = {}
    for f, (barL, fR, barR, fL, m) in legs.items():
        xh, xH, xA = xi[f]
        cR = {k: ftab[(barL[i], diracPR, fR[i])][1].get((b[k],), 0) for k in ("h", "H", "A0")}
        cL = {k: ftab[(barR[i], diracPL, fL[i])][1].get((b[k],), 0) for k in ("h", "H", "A0")}
        for k, x in (("h", xh), ("H", xH)):
            assert_dual_equal(cR[k].subs(yuk).subs(res), -m / v * x, msg=f"{k} {f}{f} P_R")
            assert_dual_equal(cL[k].subs(yuk).subs(res), -m / v * x, msg=f"{k} {f}{f} P_L")
        # A: opposite-sign chiral pieces (f̄γ5f), magnitude (m_f/v) ξ_A
        cRA, cLA = cR["A0"].subs(yuk).subs(res), cL["A0"].subs(yuk).subs(res)
        assert_dual_equal(cRA, -cLA, msg=f"A {f}{f} chiral antisymmetry")
        ratio = sp.simplify(cRA / (-sp.I * m / v * xA))
        assert ratio in (1, -1), (f, ratio)
        a_sign[f] = int(ratio)
    # the overall A-phase convention is common to all fermions
    assert len(set(a_sign.values())) == 1, a_sign
    thdm.extra["A_sign_vs_branco_eq16"] = a_sign["t"]


def _charged_couplings(thdm, ftab):
    e, b, p = thdm.extra, thdm.bosons, thdm.pieces
    i = p.idx[0]
    yuk = {y.s: y.expr for y in p.yukawa_params.values()}
    res = _res(e)
    Ll, eR, QL, uR, dR = (p.fermions[k] for k in ("Ll", "eR", "QL", "uR", "dR"))
    c_tb_R = ftab[(QL.bar_components[0][i], diracPR, dR.components[0][i])][1][(b["Hp"],)].subs(yuk).subs(res)
    c_tb_L = ftab[(uR.bar_components[0][i], diracPL, QL.components[3][i])][1][(b["Hp"],)].subs(yuk).subs(res)
    c_nul = ftab[(Ll.bar_components[0][i], diracPR, eR.components[0][i])][1][(b["Hp"],)].subs(yuk).subs(res)
    return c_tb_R, c_tb_L, c_nul


def test_charged_higgs_yukawa_eq16(thdm, ftab):
    """Branco et al. Eq. (16), second line (V_ud = 1), read with its bracket:
    −{ (√2/v) ū (m_u ξ_A^u P_L + m_d ξ_A^d P_R) d H⁺ + (√2 m_ℓ ξ_A^ℓ/v) ν̄_L ℓ_R H⁺ } + h.c.
    (identical to Aoki et al. Eq. 6). Pinned here: the magnitudes √2 m_t cotβ/v, √2 m_b tanβ/v and
    the equal sign of the two quark chiralities. The overall H⁺-line sign is a convention
    (metadata discrepancy D-3); the quark–lepton relative sign is the next test."""
    e, p = thdm.extra, thdm.pieces
    v, be = e["v"].s, e["beta"].s
    mt, mb, mtau = (p.masses[k].s for k in ("MT", "MB", "MTA"))
    c_tb_R, c_tb_L, c_nul = _charged_couplings(thdm, ftab)
    lit_R = -sp.sqrt(2) / v * mb * sp.tan(be)          # ū P_R d
    lit_L = -sp.sqrt(2) / v * mt * sp.cot(be)          # ū P_L d
    s = sp.simplify(c_tb_R / lit_R)
    assert s in (1, -1), s
    assert_dual_equal(c_tb_L, s * lit_L, msg="H+ t b P_L (relative sign to P_R)")
    assert_dual_equal(sp.Abs(c_nul), sp.Abs(sp.sqrt(2) / v * mtau * sp.tan(be)), msg="|H+ nu tau|")
    thdm.extra["Hp_sign_vs_branco_eq16"] = int(s)


def test_charged_higgs_quark_lepton_relative_sign_eq16(thdm, ftab):
    """Branco et al. Eq. (16) / Aoki et al. Eq. (6): the common minus in front of the bracket
    multiplies BOTH the quark and the lepton term, so ν̄_L τ_R H⁺ = −√2 m_τ tanβ/v in their
    convention, with the same overall sign s as ū P_R d H⁺ (discrepancy D-1, resolved)."""
    e, p = thdm.extra, thdm.pieces
    v, be = e["v"].s, e["beta"].s
    mb, mtau = p.masses["MB"].s, p.masses["MTA"].s
    c_tb_R, _c_tb_L, c_nul = _charged_couplings(thdm, ftab)
    s = sp.simplify(c_tb_R / (-sp.sqrt(2) / v * mb * sp.tan(be)))
    assert s in (1, -1), s
    assert_dual_equal(c_nul, s * (-sp.sqrt(2) / v * mtau * sp.tan(be)), msg="H+ nu tau (Eq. 16 sign)")


def test_charged_higgs_quark_lepton_same_sign_derived(thdm, ftab):
    """Hand derivation from L ⊃ −y_b Q̄ H1 d_R − y_τ L̄ H1 e_R with H1⁺ = cβ G⁺ − sβ H⁺:
    both give +y sβ (ψ̄_L P_R ψ_R) H⁺, i.e. +√2 m_b tanβ/v and +√2 m_τ tanβ/v with our H⁺ phase
    (the opposite overall sign to Branco/Aoki is discrepancy D-3, a convention)."""
    e, p = thdm.extra, thdm.pieces
    v, be = e["v"].s, e["beta"].s
    mb, mtau = p.masses["MB"].s, p.masses["MTA"].s
    c_tb_R, _c_tb_L, c_nul = _charged_couplings(thdm, ftab)
    assert_dual_equal(c_tb_R, sp.sqrt(2) / v * mb * sp.tan(be), msg="H+ t b P_R (derived)")
    assert_dual_equal(c_nul, sp.sqrt(2) / v * mtau * sp.tan(be), msg="H+ nu tau (derived)")


def _branco_potential_masses():
    """m_A², m_H±² from Branco et al. Eq. (2) with plain SymPy (no feynlag).

    Φ_a = (φ_a⁺, (v_a + ρ_a + i η_a)/√2); the conjugate of φ_a⁺ is an independent symbol so the
    charged mass matrix is ∂²V/∂φ̄_i∂φ_j. Tadpoles ∂V/∂ρ_a = 0 fix m11², m22². Each block has one
    Goldstone, so the physical mass² is the trace.
    """
    v1, v2 = sp.symbols("v1 v2", positive=True)
    m11, m22, m12 = sp.symbols("m11sq m22sq m12sq", real=True)
    l1, l2, l3, l4, l5 = sp.symbols("lam1:6", real=True)
    r1, r2, e1, e2 = sp.symbols("rho1 rho2 eta1 eta2", real=True)
    p1, p2, q1, q2 = sp.symbols("p1 p2 p1bar p2bar")
    n1, n2 = (v1 + r1 + sp.I * e1) / sp.sqrt(2), (v2 + r2 + sp.I * e2) / sp.sqrt(2)
    n1b, n2b = (v1 + r1 - sp.I * e1) / sp.sqrt(2), (v2 + r2 - sp.I * e2) / sp.sqrt(2)
    P11, P22 = q1 * p1 + n1b * n1, q2 * p2 + n2b * n2
    P12, P21 = q1 * p2 + n1b * n2, q2 * p1 + n2b * n1        # Φ1†Φ2, Φ2†Φ1
    V = (m11 * P11 + m22 * P22 - m12 * (P12 + P21) + l1 / 2 * P11**2 + l2 / 2 * P22**2
         + l3 * P11 * P22 + l4 * P12 * P21 + l5 / 2 * (P12**2 + P21**2))
    zero = {r1: 0, r2: 0, e1: 0, e2: 0, p1: 0, p2: 0, q1: 0, q2: 0}
    tad = sp.solve([sp.diff(V, r1).subs(zero), sp.diff(V, r2).subs(zero)], [m11, m22], dict=True)[0]
    Vt = sp.expand(V.subs(tad))
    M_odd = sp.Matrix(2, 2, lambda i, j: sp.diff(Vt, (e1, e2)[i], (e1, e2)[j]).subs(zero))
    M_ch = sp.Matrix(2, 2, lambda i, j: sp.diff(Vt, (q1, q2)[i], (p1, p2)[j]).subs(zero))
    syms = dict(v1=v1, v2=v2, m12=m12, l4=l4, l5=l5)
    return sp.simplify(M_odd.trace()), sp.simplify(M_ch.trace()), syms


def test_mA_mHp_independent_of_feynlag():
    """Branco et al. Eq. (2) → m_A² = [m12²/(v1v2) − λ5] v², m_H±² = [m12²/(v1v2) − (λ4+λ5)/2] v²
    (= Gunion–Haber Eqs. 10–11), derived without feynlag. Grounds discrepancy D-2."""
    mA2, mHp2, s = _branco_potential_masses()
    v2sum = s["v1"]**2 + s["v2"]**2
    pref = s["m12"] / (s["v1"] * s["v2"])
    assert_dual_equal(mA2, (pref - s["l5"]) * v2sum, msg="m_A^2 from Eq. (2)")
    assert_dual_equal(mHp2, (pref - (s["l4"] + s["l5"]) / 2) * v2sum, msg="m_H+^2 from Eq. (2)")


@pytest.mark.xfail(strict=True, reason="discrepancy D-2: Branco et al. arXiv v1-v3 print m_A^2 with -2 lam5 and "
                   "m_+^2 with -lam4 - lam5, inconsistent with their own Eq. (2); published text not checked")
def test_mA_mHp_branco_arxiv_text_eq5_6():
    mA2, mHp2, s = _branco_potential_masses()
    v2sum = s["v1"]**2 + s["v2"]**2
    pref = s["m12"] / (s["v1"] * s["v2"])
    assert_dual_equal(mA2, (pref - 2 * s["l5"]) * v2sum, msg="Branco printed m_A^2")
    assert_dual_equal(mHp2, (pref - s["l4"] - s["l5"]) * v2sum, msg="Branco printed m_+^2")


def test_alignment_limit_recovers_sm_h(thdm):
    """cos(β−α) → 0: every h coupling → SM (Branco et al. Table 2 with α = β − π/2:
    ξ_h^u = cα/sβ → 1, ξ_h^d = −sα/cβ → 1; hVV → SM). GH: the decoupling/alignment limit."""
    e = thdm.extra
    al, be = e["alpha"].s, e["beta"].s
    lim = {al: be - sp.pi / 2}
    assert sp.simplify((sp.cos(al) / sp.sin(be)).subs(lim)) == 1
    assert sp.simplify((-sp.sin(al) / sp.cos(be)).subs(lim)) == 1
    assert sp.simplify(sp.sin(be - al).subs(lim)) == 1
    # and the model's benchmark is near alignment: |cos(β−α)| small
    vals = thdm.values()
    import math
    cba = math.cos(vals[be] - vals[al])
    assert abs(cba) < 0.2, cba
