"""L2: the seesaw formula and the physical heavy-neutrino couplings.

References (metadata → literature_checks): the seesaw light mass
m_ν ≈ −m_D M_R⁻¹ m_Dᵀ (Minkowski 1977; Gell-Mann–Ramond–Slansky 1979; Yanagida
1979; Mohapatra–Senjanović 1980) and the mass-basis gauge interactions of
Atre–Han–Pascoli–Zhang, arXiv:0901.3589v2, Eq. (2.5):

  −L = (g/√2) W⁺_μ Σ V*_{ℓm'} N̄^c_{m'} γ^μ P_L ℓ + (g/2cosθ_W) Z_μ Σ V*_{ℓm'} N̄^c_{m'} γ^μ P_L ν_ℓ + h.c.

with ν_{aL} = Σ U_{am} ν_{mL} + Σ V_{am'} N^c_{m'L} (Eq. 2.3) and V†V ≈ m_ν/M_N.
In feynlag's convention n = U* χ, so U here is the Takagi factor (rows: ν_L, ν_R^c).
"""

import sympy as sp

from feynlag import DiracGamma, diracPL, diracPR
from feynlag_models.checks import assert_dual_equal
from .conftest import coupling

mu = sp.Symbol("mu", integer=True)
gL = DiracGamma(mu) * diracPL


def test_seesaw_formula_vs_exact_eigenvalue(ss):
    """m_ν(exact) = (√(M_R²+4m_D²) − M_R)/2 = m_D²/M_R · (1 − m_D²/M_R² + …):
    the seesaw formula is the leading term (symbolic series + numeric)."""
    e = ss.extra
    mD, MR = e["mDsym"].s, e["MR"].s
    exact = e["MN1"].expr                       # positive singular value
    approx = -e["m_light_approx"].subs(e["yv"].s * e["ew"].v.s / sp.sqrt(2), mD)
    approx = sp.simplify(approx.subs(e["yv"].s, sp.sqrt(2) * mD / e["ew"].v.s))
    assert sp.simplify(approx - mD**2 / MR) == 0
    eps = sp.Symbol("epsilon", positive=True)
    ratio = sp.series((exact / approx).subs(mD, eps * MR), eps, 0, 4).removeO()
    assert sp.simplify(ratio - (1 - eps**2)) == 0
    vals = ss.values()
    assert abs(float((exact / approx).subs(vals)) - 1) < 1e-12


def test_W_coupling_eq_2_5(ss, chi_table):
    """W⁻ ē χ_k coefficient = (g/√2)·|U[ν_L, k]|: full strength for the light state,
    (g/√2)·V for N with V ≈ m_D/M_R (Atre et al. Eq. 2.5, first term)."""
    e, vals = ss.extra, ss.values()
    chiL = e["chi"][0]
    eLbar = ss.pieces.fermions["Ll"].bar_components[1]
    gsq = float(vals[ss.pieces.gw.s]) / 2**0.5
    for k in range(2):
        c = abs(coupling(chi_table, (eLbar[0], gL, chiL[k]), ss.bosons["Wm"], vals))
        assert abs(c - gsq * abs(complex(e["U"][0, k]))) < 1e-12 * gsq
    c_light = abs(coupling(chi_table, (eLbar[0], gL, chiL[e["light"]]), ss.bosons["Wm"], vals))
    c_heavy = abs(coupling(chi_table, (eLbar[0], gL, chiL[e["heavy"]]), ss.bosons["Wm"], vals))
    V = float(vals[e["mDsym"].s] / vals[e["MR"].s])
    assert abs(c_light / gsq - 1) < 1e-12
    assert abs(c_heavy / gsq - V) / V < 1e-6


def test_Z_coupling_eq_2_5(ss, chi_table):
    """Z χ̄_k χ_k' (P_L) coefficient = (g_Z/2)·|U[ν_L,k] U[ν_L,k']|: g_Z/2 for the light
    pair, (g_Z/2)·V for ν–N (Atre et al. Eq. 2.5, second term)."""
    e, vals = ss.extra, ss.values()
    chiL, chiLbar = e["chi"][0], e["chi"][2]
    g, gp = vals[ss.pieces.gw.s], vals[ss.pieces.g1.s]
    gZ2 = (g**2 + gp**2) ** 0.5 / 2
    for k in range(2):
        for kk in range(2):
            c = abs(coupling(chi_table, (chiLbar[k], gL, chiL[kk]), ss.bosons["Z"], vals))
            expected = gZ2 * abs(complex(e["U"][0, k]) * complex(e["U"][0, kk]))
            assert abs(c - expected) < 1e-12 * gZ2, (k, kk, c, expected)


def test_h_nu_N_coupling(ss, chi_table):
    """h χ̄_k P_R χ_k' coefficient = (y_ν/√2)·|U[ν_L,k] U[ν_R,k']| — the Dirac Yukawa
    in the mass basis (derived; the ν–N entry is the unsuppressed y_ν/√2 = m_D/v)."""
    e, vals = ss.extra, ss.values()
    chiR, chiLbar = e["chi"][1], e["chi"][2]
    y = float(vals[e["yv"].s]) / 2**0.5
    for k in range(2):
        for kk in range(2):
            c = abs(coupling(chi_table, (chiLbar[k], diracPR, chiR[kk]), ss.bosons["h"], vals))
            expected = y * abs(complex(e["U"][0, k]) * complex(e["U"][1, kk]))
            assert abs(c - expected) < 1e-12 * y, (k, kk)
    c_lh = abs(coupling(chi_table, (chiLbar[e["light"]], diracPR, chiR[e["heavy"]]), ss.bosons["h"], vals))
    assert abs(c_lh - y) < 1e-6 * y


def test_decoupling_M_R_to_infinity(ss):
    """The exact 2×2 light–heavy mixing V² = m_D²/(m_D² + m_N²) → 0 as M_R → ∞, with
    V = m_D/M_R + O(m_D³/M_R³); the Takagi factor equals the closed form at the benchmark."""
    e, vals = ss.extra, ss.values()
    mD, MR = e["mDsym"].s, e["MR"].s
    mN = e["MN2"].expr
    V = mD / sp.sqrt(mD**2 + mN**2)
    assert abs(float(V.subs(vals)) - abs(complex(e["U"][0, e["heavy"]]))) < 1e-12
    assert sp.limit(V, MR, sp.oo) == 0
    eps = sp.Symbol("epsilon", positive=True)
    lead = sp.series(V.subs(mD, eps * MR), eps, 0, 3).removeO()
    assert sp.simplify(lead - eps) == 0
