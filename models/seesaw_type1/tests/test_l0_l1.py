"""L0/L1: invariance, anomalies, the seesaw mass matrix and its Takagi spectrum."""

import pytest
import sympy as sp

from feynlag_models.checks import (assert_dual_equal, massive_gauge_boson_count,
                                   zero_eigenvalue_count)


def test_validate_invariance_and_anomalies(ss):
    """Dirac Yukawa via H̃ + Majorana mass are gauge invariant and hermitian; the
    gauge-singlet ν_R leaves the anomaly cancellation of `sm` untouched."""
    report = ss.model.validate()
    assert report.ok, report.summary()
    assert report.checks["anomalies"] is not None and report.checks["anomalies"].ok


def test_mass_matrix_entries(ss):
    """m_D = y_ν v/√2 from the Yukawa, M_R from the Majorana term, M_ν symmetric."""
    e = ss.extra
    v = e["ew"].v.s
    assert_dual_equal(e["mD"][0, 0], e["yv"].s * v / sp.sqrt(2), msg="m_D")
    assert_dual_equal(e["MRmat"][0, 0], e["MR"].s, msg="M_R")
    Mnu = e["Mnu"]
    assert Mnu == sp.Matrix([[0, e["mD"][0, 0]], [e["mD"][0, 0], e["MR"].s]])
    assert sp.simplify(Mnu - Mnu.T) == sp.zeros(2, 2)


def test_takagi_spectrum_at_benchmark(ss):
    """U D Uᵀ reconstructs M_ν; one light and one heavy state; the closed-form
    singular values MN1/MN2 registered as parameters agree with the Takagi output."""
    e, vals = ss.extra, ss.values()
    U, D = e["U"], e["D"]
    Mn = sp.Matrix(2, 2, lambda a, b: sp.nsimplify(e["Mnu"][a, b].subs(vals), rational=True))
    recon = (U * D * U.T - Mn).evalf(30)
    assert max(abs(complex(x)) for x in recon) < 1e-20 * float(vals[e["MR"].s])
    m_light, m_heavy = e["masses"][e["light"]], e["masses"][e["heavy"]]
    assert m_light < 1e-6 * m_heavy
    assert abs(m_light - vals[e["MN1"].s]) < 1e-9 * m_light
    assert abs(m_heavy - vals[e["MN2"].s]) < 1e-9 * m_heavy


def test_light_heavy_mixing_at_benchmark(ss):
    """|U[ν_L, N]| ≈ m_D/M_R (V†V ≈ m_ν/M_N, Atre et al. below Eq. 2.5)."""
    e, vals = ss.extra, ss.values()
    V = abs(complex(e["U"][0, e["heavy"]]))
    mD_over_MR = float(vals[e["mDsym"].s] / vals[e["MR"].s])
    assert abs(V - mD_over_MR) / mD_over_MR < 1e-6


def test_goldstone_count_unchanged(ss):
    p, vals = ss.pieces, ss.values()
    W1, W2, W3 = p.W.components
    Mg = ss.model.gauge_mass_matrix([W1, W2, W3, p.B.components[0]])
    assert massive_gauge_boson_count(Mg, vals) == 3
    M_odd = ss.model.mass_matrix([ss.bosons["G0"]])
    M_ch = ss.model.mass_matrix([ss.bosons["Gp"]], charged=True)
    assert zero_eigenvalue_count(M_odd, vals) + 2 * zero_eigenvalue_count(M_ch, vals) == 3


# ------------------------------------------------- feynlag 0.4.0+ API (constructors, coverage)

def _component_level_terms(ss):
    """The pre-0.4.0 component-level ν_R terms, kept as a reference: ``−y_ν L̄ H̃ ν_R + h.c.`` with
    ``H̃ = (H⁰*, −G⁺*)`` and ``−½ M_R ν_Rᵀ C P_L ν_R + h.c.``. They were written with the doublet
    leg on ``i`` and the ν_R leg on ``j``, which for a scalar (flavour-universal, δ_ij) coupling
    is the same as one shared index only at one generation."""
    from feynlag import Bilinear, MajoranaBilinear, diracPL, diracPR
    e, p = ss.extra, ss.pieces
    i, j = p.idx
    Gp, H0 = e["ew"].H.components
    Ll, yv, MR, CPL = p.fermions["Ll"], e["yv"].s, e["MR"].s, e["CPL"]
    nR, nRbar = e["nuR"].nuR, e["nuR"].nuRbar
    LY = -(yv * sp.conjugate(H0) * Bilinear(Ll.nuLbar[i], diracPR, nR[j])
           + yv * (-sp.conjugate(Gp)) * Bilinear(Ll.eLbar[i], diracPR, nR[j]))
    LY += -(yv * H0 * Bilinear(nRbar[j], diracPL, Ll.nuL[i])
            + yv * (-Gp) * Bilinear(nRbar[j], diracPL, Ll.eL[i]))
    op = -sp.Rational(1, 2) * MR * MajoranaBilinear(nR[i], CPL, nR[j])
    return LY, op + sp.conjugate(op)


def test_constructor_terms_are_the_diagonal_component_terms(ss):
    """``yukawa(y_ν, Ll, tilde(H), nuR)`` and ``majorana_mass(M_R, nuR, gamma=C·P_L)`` give the
    flavour-diagonal form of the component-level terms, with the H⁰* and −G⁺* legs, the ½ and the
    ``C P_L`` structure. The reference's ν_R leg on ``j`` becomes ``i`` (one generation: δ_ij), and
    the physics consequences (mass matrix, Takagi spectrum, vertices) are pinned by the other L1/L2
    tests."""
    from feynlag import diracC, diracPL
    LY, LM = _component_level_terms(ss)
    e, (i, j) = ss.extra, ss.pieces.idx
    assert e["CPL"] == diracC * diracPL
    assert sp.expand(e["LYukD"] - LY.xreplace({j: i})) == 0
    assert sp.expand(e["LMaj"] - LM.xreplace({j: i})) == 0
    assert not e["LYukD"].has(j) and not e["LMaj"].has(j)
    terms = {t.name: t for t in ss.model.lagrangian.terms}
    assert terms["yukawa_nu"].sector == "yukawa" and terms["yukawa_nu"].expr == e["LYukD"]
    assert terms["majorana_mass"].sector == "other" and terms["majorana_mass"].expr == e["LMaj"]


def test_mass_blocks_report_majorana_block(ss):
    """``mass_blocks()`` gives the SM Higgs and gauge blocks, and reports, without raising,
    the (ν_L, ν_R) block as not diagonalizable: it has a Majorana mass, which goes through
    ``seesaw_mass_matrix`` + ``diagonalize_takagi`` + ``MajoranaRotation`` (as this model does)."""
    m, b = ss.model, ss.bosons
    scalar = m.mass_blocks(kind="scalar")
    assert [blk.fields for blk in scalar] == [[b["h"]], [b["G0"]], [b["Gp"]]]
    assert [bool(blk.goldstones) for blk in scalar] == [False, True, True]
    p = ss.pieces
    assert [blk.fields for blk in m.mass_blocks(kind="gauge")] == [
        list(p.W.components[:2]), [p.W.components[2], p.B.components[0]]]
    (nu,) = [blk for blk in m.mass_blocks(kind="fermion")
             if blk.fields == [p.fermions["Ll"].nuL]]
    assert nu.right == [ss.extra["nuR"].nuR] and nu.diagonalizable is False
    assert "Majorana" in nu.note and "diagonalize_takagi" in nu.note


def test_physical_registry(ss):
    """Charges (derived from the vacuum), conjugate pairs and Goldstones from ``model.physical``."""
    b = ss.bosons
    assert ss.charges == {b["h"]: 0, b["G0"]: 0, b["Gp"]: 1, b["Gm"]: -1,
                          b["Z"]: 0, b["A"]: 0, b["Wp"]: 1, b["Wm"]: -1}
    assert ss.conjugates == {b["Gp"]: b["Gm"], b["Gm"]: b["Gp"], b["Wp"]: b["Wm"], b["Wm"]: b["Wp"]}
    assert ss.goldstones == (b["G0"], b["Gp"], b["Gm"])


def test_term_coverage(ss):
    """The potential and every dim-4 Yukawa the fields allow are present, ``y_ν`` on ``L̄ H̃ ν_R``
    included (feynlag's ``L = −Σ c O``). The bare Majorana mass is the only remainder, because
    feynlag's operator basis does not enumerate it (FG-10). At dim 5 the Weinberg operator is
    absent, as it should be at tree level in the type-I seesaw. [physics judgment]"""
    from feynlag import FL_I, MajoranaBilinear
    e, ys = ss.extra, ss.pieces.yukawa_params
    tc = ss.model.term_coverage()
    assert {t.label: c for t, c in tc.present} == {
        "(H†H)": -e["ew"].mu2.s, "(H†H) (H†H)": e["ew"].lam.s,
        "Ll̄·H eR": ys["ytau"].s, "QL̄·H dR": ys["yb"].s, "QL̄·H̃ uR": ys["yt"].s,
        "Ll̄·H̃ nuR": e["yv"].s}
    assert tc.missing == []
    nR = e["nuR"].nuR
    majorana_half = -e["MR"].s * MajoranaBilinear(nR[FL_I], e["CPL"], nR[FL_I]) / 2   # diagonal
    assert set(tc.unmatched) == {"yukawa"}
    assert sp.expand(tc.unmatched["yukawa"] - majorana_half) == 0
    assert [t.label for t in ss.model.term_coverage(max_dim=5).missing] == ["(Ll·εH)² [Weinberg]"]


def test_summary_and_parameters(ss):
    """``summary()``: ν_R is a right-handed gauge singlet; every parameter is listed in order and
    ``check_parameters()`` finds no undeclared symbol."""
    s = ss.model.summary()
    rows = {r[0]: tuple(str(x) for x in r[1:5]) for r in s.field_rows}
    assert rows["nuR"] == ("fermion R", "1", "0", "1")
    assert rows["Ll"] == ("fermion L", "2", "-1/2", "1")
    assert set(rows) == {"H", "W", "B", "G", "Ll", "eR", "QL", "uR", "dR", "nuR"}
    assert [r[0] for r in s.param_rows] == [q.name for q in ss.params]
    assert ss.model.check_parameters().undeclared == []


@pytest.mark.xfail(strict=True, reason="FG-9: feynlag.terms silently ignores indices=(i, j) for a "
                   "scalar coupling instead of raising ValueError")
def test_feynlag_scalar_coupling_indices_gap(ss):
    """A scalar coupling is flavour-universal (δ_ij), so an explicit pair of distinct leg indices
    contradicts it; ``yukawa`` and ``majorana_mass`` should raise ``ValueError``. feynlag 0.5.1 drops
    the second index without a word and returns the term on ``(i, i)``."""
    import pytest
    from feynlag import majorana_mass, tilde, yukawa
    e, p = ss.extra, ss.pieces
    i, j = p.idx
    with pytest.raises(ValueError):
        yukawa(e["yv"], p.fermions["Ll"], tilde(e["ew"].H), e["nuR"], indices=(i, j))
    with pytest.raises(ValueError):
        majorana_mass(e["MR"], e["nuR"], indices=(i, j))


@pytest.mark.xfail(strict=True, reason="FG-10: term_coverage/suggest_yukawa do not enumerate the "
                   "bare Majorana mass of a gauge-singlet fermion")
def test_feynlag_majorana_mass_coverage_gap(ss):
    """The gauge-invariant ``−½ M_R ν_Rᵀ C P_L ν_R + h.c.`` should be a recognised invariant
    (coefficient ∝ M_R) rather than an unmatched remainder."""
    tc = ss.model.term_coverage()
    assert tc.unmatched == {}
    assert any(c.has(ss.extra["MR"].s) for _t, c in tc.present)


@pytest.mark.xfail(strict=True, reason="FG-10: no bare Majorana mass for a fermion in a real "
                   "non-singlet representation (SU(2) triplet): majorana_mass refuses it and "
                   "suggest_yukawa does not enumerate it")
def test_feynlag_triplet_majorana_gap():
    """A type-III-like triplet Σ (SU(2) 3, Y = 0) has the gauge-invariant bare Majorana mass
    ``−½ M Σ^a C P_L Σ^a + h.c.`` (feynlag's ``check_invariance`` agrees). It should be built by
    ``majorana_mass`` and offered by ``suggest_yukawa``; feynlag 0.5.1 raises on the first and
    returns nothing from the second."""
    from feynlag import WeylFermion, electroweak_scaffold, majorana_mass
    from feynlag.suggest import suggest_yukawa
    ew = electroweak_scaffold()
    Sig = WeylFermion("Sig", reps={ew.SU2L: 3, ew.U1Y: 0}, chirality="R", nflavors=1,
                      component_names=["S1", "S2", "S3"])
    M, i = sp.Symbol("M", positive=True), sp.Symbol("i", integer=True)
    term = majorana_mass(M, Sig, indices=i)
    assert term != 0
    basis = suggest_yukawa([Sig], [ew.H], [ew.SU2L, ew.U1Y], max_dim=4, verify=False)
    assert basis, "no bare Majorana mass offered for the triplet"
