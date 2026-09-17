"""L2: Feynman rules against textbook / PDG expressions (see metadata → literature_checks)."""

import sympy as sp

from feynlag import DiracGamma, diracPL, diracPR
from feynlag_models.checks import assert_dual_equal

mu = sp.Symbol("mu", integer=True)
gL, gR = DiracGamma(mu) * diracPL, DiracGamma(mu) * diracPR


def _rule(rules, *legs):
    key = tuple(sorted(legs, key=lambda f: f.sort_key()))
    return rules[key]


def test_hVV_and_hff(sm):
    """hWW = i g m_W g^{μν}, hZZ = i g_Z m_Z g^{μν}, hhVV; h f f̄ = −i m_f/v.
    PDG 2024 EW review: L_HV of Eq. (10.4) with M_W, M_Z of Eqs. (10.5b,c), and the
    Yukawa term −(m_i H/v) ψ̄ψ of Eq. (10.2)."""
    b, p = sm.bosons, sm.pieces
    g, gp, v = p.gw.s, p.g1.s, p.ew.v.s
    mW, mZ = g * v / 2, sp.sqrt(g**2 + gp**2) * v / 2
    rules = sm.model.feynman_rules(sm.boson_list, sector="kinetic",
                                   conjugate_map=sm.cmap, simplifier=sp.simplify)
    assert_dual_equal(_rule(rules, b["h"], b["Wp"], b["Wm"]), sp.I * g * mW, msg="hWW")
    assert_dual_equal(_rule(rules, b["h"], b["Z"], b["Z"]), sp.I * sp.sqrt(g**2 + gp**2) * mZ, msg="hZZ")
    assert_dual_equal(_rule(rules, b["h"], b["h"], b["Wp"], b["Wm"]), sp.I * g**2 / 2, msg="hhWW")
    assert_dual_equal(_rule(rules, b["h"], b["h"], b["Z"], b["Z"]), sp.I * (g**2 + gp**2) / 2, msg="hhZZ")

    tab = sm.fermion_table()
    i = p.idx[0]
    for name, bar, fld, M in (
            ("tau", p.fermions["Ll"].bar_components[1], p.fermions["eR"].components[0], p.masses["MTA"]),
            ("t", p.fermions["QL"].bar_components[0], p.fermions["uR"].components[0], p.masses["MT"]),
            ("b", p.fermions["QL"].bar_components[3], p.fermions["dR"].components[0], p.masses["MB"])):
        coeff = tab[(bar[i], diracPR, fld[i])][1][(b["h"],)]
        coeff = coeff.subs(sm.params.resolve())
        assert_dual_equal(sp.I * coeff, -sp.I * M.s / v, msg=f"h {name} {name}")


def test_gauge_currents(sm):
    """Z f f̄: i g_Z γ^μ (T³ − Q s_W²) per chirality; γ f f̄: i e Q γ^μ;
    W ν̄ ℓ: i g/√2 γ^μ P_L. PDG 2024 EW review Eqs. (10.2), (10.3), (10.6), (10.7):
    g_V − g_A γ5 = 2(T³ P_L − Q s_W²) and (1 − γ5) = 2 P_L reproduce these up to the global
    sign g → −g of the gauge couplings (metadata discrepancy D-1, a convention)."""
    b, p = sm.bosons, sm.pieces
    g, gp = p.gw.s, p.g1.s
    gZ = sp.sqrt(g**2 + gp**2)
    sw2 = gp**2 / (g**2 + gp**2)
    e = g * gp / gZ
    tab = sm.fermion_table()
    i = p.idx[0]
    Ll, eR, QL, uR, dR = (p.fermions[k] for k in ("Ll", "eR", "QL", "uR", "dR"))
    nuL, eL = Ll.components
    nuLbar, eLbar = Ll.bar_components
    # (bar, gamma, field, T3, Q)
    legs = [
        (nuLbar, gL, nuL, sp.Rational(1, 2), 0),
        (eLbar, gL, eL, -sp.Rational(1, 2), -1),
        (eR.bar_components[0], gR, eR.components[0], 0, -1),
        (QL.bar_components[0], gL, QL.components[0], sp.Rational(1, 2), sp.Rational(2, 3)),
        (QL.bar_components[3], gL, QL.components[3], -sp.Rational(1, 2), -sp.Rational(1, 3)),
        (uR.bar_components[0], gR, uR.components[0], 0, sp.Rational(2, 3)),
        (dR.bar_components[0], gR, dR.components[0], 0, -sp.Rational(1, 3)),
    ]
    for bar, gam, fld, T3, Q in legs:
        entry = tab[(bar[i], gam, fld[i])][1]
        assert_dual_equal(entry.get((b["Z"],), 0), gZ * (T3 - Q * sw2), msg=f"Z {fld}")
        assert_dual_equal(entry.get((b["A"],), 0), e * Q, msg=f"A {fld}")
    cW = tab[(nuLbar[i], gL, eL[i])][1][(b["Wp"],)]
    assert_dual_equal(cW, g / sp.sqrt(2), msg="W nu e")
    cWq = tab[(QL.bar_components[0][i], gL, QL.components[3][i])][1][(b["Wp"],)]
    assert_dual_equal(cWq, g / sp.sqrt(2), msg="W t b")


def test_higgs_self_couplings(sm):
    """h³ = −3i m_h²/v, h⁴ = −3i m_h²/v² (feynlag test_scalar_pipeline_sm)."""
    b, p = sm.bosons, sm.pieces
    lam, v = p.ew.lam.s, p.ew.v.s
    mh2 = 2 * lam * v**2
    rules = sm.model.feynman_rules(sm.boson_list, sector="potential",
                                   conjugate_map=sm.cmap, simplifier=sp.simplify)
    assert_dual_equal(_rule(rules, b["h"], b["h"], b["h"]), -3 * sp.I * mh2 / v, msg="hhh")
    assert_dual_equal(_rule(rules, b["h"], b["h"], b["h"], b["h"]), -3 * sp.I * mh2 / v**2, msg="hhhh")


def test_charge_and_hermiticity_pairing(sm):
    """Every bosonic vertex conserves charge; declared charges agree with the
    vacuum-derived operator; every vertex has its hermitian partner."""
    report = sm.model.validate(invariance=False, anomalies=False,
                               charges=sm.charges, fields=sm.boson_list,
                               conjugate_map=sm.cmap, conjugates=sm.conjugates)
    assert report.ok, report.summary()
    for name in ("charge_conservation", "charge_consistency", "hermiticity_pairing"):
        assert report.checks[name] is not None and report.checks[name].ok
