"""L2: the mass-basis couplings, decoupling, the one-generation limit and Casas–Ibarra.

References (metadata → literature_checks):
- Atre–Han–Pascoli–Zhang, arXiv:0901.3589v2, Eq. (2.5), flavour-general mass-basis currents
  −L = (g/√2) W⁺ Σ_ℓ Σ_m V*_{ℓm} N̄^c_m γ^μ P_L ℓ + (g/2cosθ_W) Z Σ V*_{ℓm} N̄^c_m γ^μ P_L ν_ℓ + h.c.
- Ibarra–Ross, arXiv:hep-ph/0312138v2: with two ν_R one light mass vanishes (Sec. 2, last
  paragraph; Sec. 3), and Eq. (6) gives the general Yukawa in terms of m_2, m_3, the MNS
  matrix and one complex angle z (Casas–Ibarra with R the first two rows of Eq. (5)).
In feynlag's convention n = U* χ, so U is the Takagi factor (rows ν_L[e, μ, τ], ν_R^c[1, 2]).
"""

import sympy as sp

from feynlag import DiracGamma, diracPL, diracPR
from feynlag_models import MODELS_DIR
from feynlag_models import metadata as md
from feynlag_models.checks import numeric_takagi
from .conftest import coupling

mu = sp.Symbol("mu", integer=True)
gL = DiracGamma(mu) * diracPL
DPS = 50


def _num(x):
    return complex(sp.N(x))


def _close(a, b, rel):
    return abs(a - b) <= rel * max(abs(a), abs(b)) + 1e-300


def _takagi_at(ss, point):
    """Numeric Takagi of the model's symbolic M_ν at ``point`` (symbol → exact or 50-digit value)."""
    Mn = ss.extra["Mnu"].applyfunc(lambda x: sp.N(x.subs(point), DPS + 10))
    return numeric_takagi(Mn, dps=DPS)


def _point(ss, yv_values=None, MR_values=None):
    e = ss.extra
    pt = {e["ew"].v.s: sp.nsimplify(ss.benchmark["v"], rational=True)}
    for par in e["yv_params"]:
        val = ss.benchmark[par.name] if yv_values is None else yv_values[par.name]
        pt[par.s] = sp.nsimplify(val, rational=True) if isinstance(val, float) else val
    for k, par in enumerate(e["MR"]):
        val = ss.benchmark[par.name] if MR_values is None else MR_values[k]
        pt[par.s] = sp.nsimplify(val, rational=True)
    return pt


def test_W_coupling_eq_2_5(ss, chi_table):
    """W⁻ ē_a χ_k = (g/√2)·|U[a, k]| for every lepton flavour a and every mass eigenstate k:
    full strength for the light states, the mixing V_{aN} ≈ (m_D M_R⁻¹)_{aN} for N_{1,2}
    (Atre et al. Eq. 2.5, first term)."""
    e, vals = ss.extra, ss.values()
    chiL = e["chi"][0]
    eLbar = ss.pieces.fermions["Ll"].bar_components[1]
    gsq = float(vals[ss.pieces.gw.s]) / 2**0.5
    for a in range(3):
        for k in range(5):
            c = abs(coupling(chi_table, (eLbar[a], gL, chiL[k]), ss.bosons["Wm"], vals))
            expected = gsq * abs(_num(e["U"][a, k]))
            assert _close(c, expected, 1e-10), (a, k, c, expected)
    light_sum = sum(abs(_num(e["U"][0, k]))**2 for k in range(3))
    assert abs(light_sum - 1) < 1e-12        # the light block is unitary up to O(V²)


def test_Z_coupling_eq_2_5(ss, chi_table):
    """Z χ̄_k γ P_L χ_k' = (g_Z/2)·|Σ_a U[a, k] U*[a, k']| (Atre et al. Eq. 2.5, second term,
    summed over the three flavours)."""
    e, vals = ss.extra, ss.values()
    chiL, chiLbar = e["chi"][0], e["chi"][2]
    g, gp = vals[ss.pieces.gw.s], vals[ss.pieces.g1.s]
    gZ2 = float((g**2 + gp**2) ** 0.5 / 2)
    U = e["U"]
    for k in range(5):
        for kk in range(5):
            c = abs(coupling(chi_table, (chiLbar[k], gL, chiL[kk]), ss.bosons["Z"], vals))
            expected = gZ2 * abs(_num(sum(U[a, k] * U[a, kk].conjugate() for a in range(3))))
            # entries that vanish by orthogonality are ~1e-52 on both sides: absolute floor
            assert abs(c - expected) <= 1e-9 * expected + 1e-40 * gZ2, (k, kk, c, expected)


def test_h_nu_N_coupling(ss, chi_table):
    """h χ̄_k P_R χ_k' = |Σ_{a,b} (y_ν^{ab}/√2) U[a, k] U[3+b, k']|: the Dirac Yukawa in the
    mass basis (derived from the Lagrangian, not a literature relation)."""
    e, vals = ss.extra, ss.values()
    chiR, chiLbar = e["chi"][1], e["chi"][2]
    U = e["U"]
    y = e["yv"].subs(vals)
    scale = max(abs(float(x)) for x in y) / 2**0.5
    for k in range(5):
        for kk in range(5):
            c = abs(coupling(chi_table, (chiLbar[k], diracPR, chiR[kk]), ss.bosons["h"], vals))
            expected = abs(_num(sum(y[a, b] / sp.sqrt(2) * U[a, k] * U[3 + b, kk]
                                    for a in range(3) for b in range(2))))
            assert abs(c - expected) <= 1e-9 * scale, (k, kk, c, expected)


def test_decoupling_M_R_to_infinity(ss):
    """Scaling M_1, M_2 by λ = 1, 10, 100: every light–heavy mixing |U[a, N_m]| falls as 1/λ and
    the light masses as 1/λ (V ≈ m_D M_R⁻¹ → 0, m_ν ≈ −m_D M_R⁻¹ m_Dᵀ → 0)."""
    MR = [ss.benchmark["MR1"], ss.benchmark["MR2"]]
    ref = None
    for lam in (1, 10, 100):
        U, D = _takagi_at(ss, _point(ss, MR_values=[lam * m for m in MR]))
        mix = [abs(U[a, 3 + m]) * lam for a in range(3) for m in range(2)]
        light = [D[k, k] * lam for k in (1, 2)]
        if ref is None:
            ref = (mix, light)
            continue
        assert all(_close(x, r, 1e-9) for x, r in zip(mix, ref[0])), lam
        assert all(_close(x, r, 1e-9) for x, r in zip(light, ref[1])), lam


def test_single_generation_limit_matches_seesaw_type1(ss):
    """Only y_ν^{τ1} = seesaw_type1's y_ν on, M_1 = its M_R: the spectrum is {0, 0, m_ν, m_N, M_2}
    with m_ν, m_N and the mixing |U[τ, N_1]| equal to seesaw_type1's at its own benchmark."""
    from models.seesaw_type1.model import build as build_one
    one = build_one()
    vals1 = one.values()
    b1 = md.benchmark_inputs(MODELS_DIR / "seesaw_type1")
    yv = {par.name: 0.0 for par in ss.extra["yv_params"]}
    yv["yv_tau1"] = b1["yv"]
    U, D = _takagi_at(ss, _point(ss, yv_values=yv, MR_values=[b1["MR"], ss.benchmark["MR2"]]))
    m = [D[k, k] for k in range(5)]
    assert m[0] < 1e-40 and m[1] < 1e-40
    assert _close(float(m[2]), float(vals1[one.extra["MN1"].s]), 1e-12)
    assert _close(float(m[3]), float(vals1[one.extra["MN2"].s]), 1e-12)
    assert _close(float(m[4]), ss.benchmark["MR2"], 1e-12)
    V_one = abs(complex(one.extra["U"][0, one.extra["heavy"]]))
    assert _close(float(abs(U[2, 3])), V_one, 1e-10)
    assert all(abs(U[a, 3]) < 1e-40 for a in (0, 1))


def test_casas_ibarra_two_rhn_eq_6(ss):
    """Ibarra–Ross Eq. (6): with R the first two rows of Eq. (5), the Yukawa
    y_ν^{a1} ⟨H⁰⟩ = √M_1 (√m_2 cos z U_{a2} + √m_3 sin z U_{a3}),
    y_ν^{a2} ⟨H⁰⟩ = √M_2 (−√m_2 sin z U_{a2} + √m_3 cos z U_{a3})
    (real U and z, the + reflection, ⟨H⁰⟩ = v/√2) fed into the model's M_ν returns the light
    masses {0, m_2, m_3} and the input mixing |U| exactly, up to O(m_D²/M_R²).
    The inputs are arbitrary numbers, not oscillation data."""
    m2, m3 = sp.Rational(1, 10**11), sp.Rational(5, 10**11)            # 0.01 eV, 0.05 eV
    z = sp.Rational(3, 10)
    t12, t13, t23 = sp.Rational(59, 100), sp.Rational(15, 100), sp.Rational(84, 100)
    R12 = sp.Matrix([[sp.cos(t12), sp.sin(t12), 0], [-sp.sin(t12), sp.cos(t12), 0], [0, 0, 1]])
    R13 = sp.Matrix([[sp.cos(t13), 0, sp.sin(t13)], [0, 1, 0], [-sp.sin(t13), 0, sp.cos(t13)]])
    R23 = sp.Matrix([[1, 0, 0], [0, sp.cos(t23), sp.sin(t23)], [0, -sp.sin(t23), sp.cos(t23)]])
    Uin = R23 * R13 * R12
    M1, M2 = (sp.nsimplify(ss.benchmark[n], rational=True) for n in ("MR1", "MR2"))
    vev = sp.nsimplify(ss.benchmark["v"], rational=True) / sp.sqrt(2)
    col1 = sp.sqrt(M1) * (sp.sqrt(m2) * sp.cos(z) * Uin[:, 1] + sp.sqrt(m3) * sp.sin(z) * Uin[:, 2])
    col2 = sp.sqrt(M2) * (-sp.sqrt(m2) * sp.sin(z) * Uin[:, 1] + sp.sqrt(m3) * sp.cos(z) * Uin[:, 2])
    names = ("e", "mu", "tau")
    yv = {}
    for a in range(3):
        yv[f"yv_{names[a]}1"] = sp.N(col1[a] / vev, DPS + 10)
        yv[f"yv_{names[a]}2"] = sp.N(col2[a] / vev, DPS + 10)
    U, D = _takagi_at(ss, _point(ss, yv_values=yv))
    assert D[0, 0] < 1e-40
    assert _close(D[1, 1], sp.N(m2, DPS), 1e-12)
    assert _close(D[2, 2], sp.N(m3, DPS), 1e-12)
    for a in range(3):
        for k in range(3):
            assert abs(abs(U[a, k]) - abs(sp.N(Uin[a, k], DPS))) < 1e-12, (a, k)
