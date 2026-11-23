"""L0 (declared, invariant, anomaly-free) and L1 (tadpoles, spectrum, Goldstones)."""

import pytest
import sympy as sp

from feynlag import diracPR, fermion_mass_matrix
from feynlag_models.checks import (assert_dual_equal, massive_gauge_boson_count,
                                   zero_eigenvalue_count)


def test_validate_invariance_and_anomalies(ckm):
    report = ckm.model.validate()
    assert report.ok, report.summary()
    assert report.checks["anomalies"] is not None        # quarks present → really checked
    assert report.checks["anomalies"].ok
    # the down Yukawa really is the non-diagonal, complex one
    Yd = ckm.extra["Yd"]
    assert any(Yd[a, b] != 0 for a in range(3) for b in range(3) if a != b)
    assert Yd.has(sp.I)


def test_tadpole_and_higgs_mass(ckm):
    ew = ckm.extra["ew"]
    lam, v = ew.lam.s, ew.v.s
    assert_dual_equal(ew.mu2.expr, lam * v**2, msg="mu2")
    M = ckm.model.mass_matrix([ckm.bosons["h"]])
    assert_dual_equal(M[0, 0], 2 * lam * v**2, msg="m_h^2")


def test_gauge_masses(ckm):
    p = ckm.pieces
    W1, W2, W3 = p.W.components
    M = ckm.model.gauge_mass_matrix([W1, W2, W3, p.B.components[0]])
    g, gp, v = p.gw.s, p.g1.s, p.ew.v.s
    assert_dual_equal(M[0, 0], g**2 * v**2 / 4, msg="m_W^2")
    assert_dual_equal(M[1, 1], g**2 * v**2 / 4, msg="m_W^2")
    eig = list(M.extract([2, 3], [2, 3]).eigenvals().keys())
    assert any(sp.simplify(e) == 0 for e in eig)
    assert any(sp.simplify(e - (g**2 + gp**2) * v**2 / 4) == 0 for e in eig)


def test_goldstone_count(ckm):
    """#massless would-be Goldstones == #massive gauge bosons (= 3)."""
    p, vals = ckm.pieces, ckm.values()
    W1, W2, W3 = p.W.components
    Mg = ckm.model.gauge_mass_matrix([W1, W2, W3, p.B.components[0]])
    M_odd = ckm.model.mass_matrix([ckm.bosons["G0"]])
    M_ch = ckm.model.mass_matrix([ckm.bosons["Gp"]], charged=True)
    n_goldstone = zero_eigenvalue_count(M_odd, vals) + 2 * zero_eigenvalue_count(M_ch, vals)
    assert massive_gauge_boson_count(Mg, vals) == 3
    assert n_goldstone == 3


def _mass_blocks(ckm):
    p = ckm.pieces
    Ll, eR, QL, uR, dR = (p.fermions[k] for k in ("Ll", "eR", "QL", "uR", "dR"))
    return {  # name: (Lagrangian, bar base, field base, mass names)
        "up": (p.yukawa["yukawa_up"], QL.bar_components[0], uR.components[0], ("MU", "MC", "MT")),
        "down": (p.yukawa["yukawa_down"], QL.bar_components[3], dR.components[0], ("MD", "MS", "MB")),
        "lepton": (p.yukawa["yukawa_lepton"], Ll.bar_components[1], eR.components[0], ("ME", "MMU", "MTA")),
    }


def test_fermion_masses(ckm):
    """Weak basis: M_u = diag(m_u, m_c, m_t), M_e = diag(m_e, m_μ, m_τ) and
    M_d = V diag(m_d, m_s, m_b); the left rotation V† M_d is diagonal with the
    input masses (d'_L = V d_L, d_R unrotated)."""
    vac, res, idx = ckm.model.vacuum, ckm.params.resolve(), ckm.pieces.idx
    V = ckm.extra["V_expr"]
    for name, (L, bar, fld, mnames) in _mass_blocks(ckm).items():
        M = fermion_mass_matrix(L, bar, fld, vac, 3, idx, gamma=diracPR).subs(res)
        D = sp.diag(*(ckm.pieces.masses[n].s for n in mnames))
        if name == "down":
            for a in range(3):
                for b in range(3):
                    assert_dual_equal(M[a, b], (V * D)[a, b], msg=f"M_d[{a},{b}]")
            M = V.conjugate().T * M
        for a in range(3):
            for b in range(3):
                assert_dual_equal(M[a, b], D[a, b], msg=f"{name} mass [{a},{b}]")
    for yn, mn in (("yu", "MU"), ("ys", "MS"), ("ymu", "MMU")):
        assert_dual_equal(ckm.params[yn].expr,
                          sp.sqrt(2) * ckm.pieces.masses[mn].s / ckm.pieces.ew.v.s, msg=yn)


# ------------------------------------------------- feynlag 0.4.0+ API (constructors, coverage)

def _component_level_yukawas_3(p, Hd, Hu, ye, yd, yu):
    """The pre-0.4.0 three-generation Yukawas, typed component by component (the old body of
    ``sm._yukawa_terms_3``), kept as the reference: ``−Y^{ab} F̄_L^a S F_R^b + h.c.`` at integer
    flavour indices, the colour sum written out, ``H̃ = (H⁰*, −G⁺*)``, the h.c. with ``conj(Y^{ab})``."""
    from feynlag import Bilinear, diracPL
    Ll, eR, QL, uR, dR = (p.fermions[k] for k in ("Ll", "eR", "QL", "uR", "dR"))
    Gp_d, H0_d = Hd.components
    Gp_u, H0_u = Hu.components
    qL_u, qL_d = QL.components[:3], QL.components[3:]
    qLbar_u, qLbar_d = QL.bar_components[:3], QL.bar_components[3:]

    def pairs(Y):
        return [(a, b, Y[a, b]) for a in range(3) for b in range(3) if Y[a, b] != 0]

    def colour(bars, gamma, fields, a, b):
        return sum(Bilinear(bars[c][a], gamma, fields[c][b]) for c in range(3))

    L_e = L_d = L_u = sp.S.Zero
    for a, b, y in pairs(ye):
        yc = sp.conjugate(y)
        L_e += -(y * Gp_d * Bilinear(Ll.nuLbar[a], diracPR, eR.eR[b])
                 + y * H0_d * Bilinear(Ll.eLbar[a], diracPR, eR.eR[b]))
        L_e += -(yc * sp.conjugate(Gp_d) * Bilinear(eR.eRbar[b], diracPL, Ll.nuL[a])
                 + yc * sp.conjugate(H0_d) * Bilinear(eR.eRbar[b], diracPL, Ll.eL[a]))
    for a, b, y in pairs(yd):
        yc = sp.conjugate(y)
        L_d += -(y * Gp_d * colour(qLbar_u, diracPR, dR.components, a, b)
                 + y * H0_d * colour(qLbar_d, diracPR, dR.components, a, b))
        L_d += -(yc * sp.conjugate(Gp_d) * colour(dR.bar_components, diracPL, qL_u, b, a)
                 + yc * sp.conjugate(H0_d) * colour(dR.bar_components, diracPL, qL_d, b, a))
    for a, b, y in pairs(yu):
        yc = sp.conjugate(y)
        L_u += -(y * sp.conjugate(H0_u) * colour(qLbar_u, diracPR, uR.components, a, b)
                 + y * (-sp.conjugate(Gp_u)) * colour(qLbar_d, diracPR, uR.components, a, b))
        L_u += -(yc * H0_u * colour(uR.bar_components, diracPL, qL_u, b, a)
                 + yc * (-Gp_u) * colour(uR.bar_components, diracPL, qL_d, b, a))
    return {"yukawa_lepton": L_e, "yukawa_down": L_d, "yukawa_up": L_u}


def test_constructors_reproduce_component_yukawas_3gen(ckm):
    """``sm.yukawa_terms`` for three generations builds each nonzero entry with
    ``feynlag.terms.yukawa`` (a placeholder flavour matrix on ``(a, b)``, diagonal entries on
    ``(a, a)``) and equals the component-level reference for the diagonal
    Y_e, Y_u (with ``tilde(H)``) and the complex Y_d = V·diag(y): colour sums, h.c. and
    conjugated couplings included. These are the model's own terms."""
    from models.sm import model as sm
    p, H = ckm.pieces, ckm.extra["ew"].H
    ys = p.yukawa_params
    ye = sm.diagonal_yukawa(ys, sm.YUKAWA_NAMES[3][2])
    yu = sm.diagonal_yukawa(ys, sm.YUKAWA_NAMES[3][0])
    Yd = ckm.extra["Yd"]
    ref = _component_level_yukawas_3(p, H, H, ye, Yd, yu)
    terms = {t.name: t.expr for t in ckm.model.lagrangian.terms}
    for name in ("yukawa_lepton", "yukawa_down", "yukawa_up"):
        assert sp.expand(terms[name] - ref[name]) == 0, name
    assert any(not Yd[a, b].is_real for a in range(3) for b in range(3))   # really complex


def test_mass_blocks_report_flavoured_blocks(ckm):
    """``mass_blocks()``: the SM Higgs and gauge blocks; every charged-lepton and quark block (per
    colour) flavoured and not diagonalizable, pointing to the numeric SVD route; ν_L massless. The
    model keeps the CKM as the input rotation ``d'_L = V d_L`` instead."""
    m, b = ckm.model, ckm.bosons
    assert [blk.fields for blk in m.mass_blocks(kind="scalar")] == [[b["h"]], [b["G0"]], [b["Gp"]]]
    fermion = m.mass_blocks(kind="fermion")
    Ll, QL = ckm.pieces.fermions["Ll"], ckm.pieces.fermions["QL"]
    flavoured = [blk for blk in fermion if blk.fields != [Ll.nuL]]
    assert {str(blk.fields[0]) for blk in flavoured} == {"eL", *(str(c) for c in QL.components)}
    for blk in flavoured:
        assert blk.nflavors == 3 and blk.diagonalizable is False
        assert "diagonalize_svd(method='numeric')" in blk.note
    (nu,) = [blk for blk in fermion if blk.fields == [Ll.nuL]]
    assert nu.diagonalizable is False and "massless" in nu.note


def test_physical_registry(ckm):
    """Charges (derived from the vacuum), conjugate pairs and Goldstones from ``model.physical``."""
    b = ckm.bosons
    assert ckm.charges == {b["h"]: 0, b["G0"]: 0, b["Gp"]: 1, b["Gm"]: -1,
                           b["Z"]: 0, b["A"]: 0, b["Wp"]: 1, b["Wm"]: -1}
    assert ckm.conjugates == {b["Gp"]: b["Gm"], b["Gm"]: b["Gp"], b["Wp"]: b["Wm"], b["Wm"]: b["Wp"]}
    assert ckm.goldstones == (b["G0"], b["Gp"], b["Gm"])


def test_term_coverage(ckm):
    """The potential is fully recognised (``V = −μ²H†H + λ(H†H)²``). The Yukawas sit at explicit
    integer flavour indices, which ``term_coverage`` documents as unmatched (``TermCoverage``
    docstring: "explicit integer flavour indices"): the three Yukawa operators are reported
    missing and the whole Yukawa sector, nothing else, is the remainder. Their content is pinned
    instead by ``test_constructors_reproduce_component_yukawas_3gen`` and the L2 tests.

    ``term_coverage`` decomposes only the ``P_R`` half of each fermion term (feynlag
    ``general.py``, ``_canonical_fermion_half``), so this test does not check the conjugated
    ``P_L`` half or its phase; that half is covered by
    ``test_constructors_reproduce_component_yukawas_3gen``."""
    tc = ckm.model.term_coverage()
    ew = ckm.extra["ew"]
    assert {t.label: c for t, c in tc.present} == {"(H†H)": -ew.mu2.s, "(H†H) (H†H)": ew.lam.s}
    assert {t.label for t in tc.missing} == {"Ll̄·H eR", "QL̄·H̃ uR", "QL̄·H dR"}
    assert set(tc.unmatched) == {"yukawa"}
    # the remainder is exactly the P_R half of the Yukawa sector (the other half is its h.c.)
    from feynlag import Bilinear, expand_bilinear
    L_yuk = sp.expand(expand_bilinear(sp.expand(sum(
        t.expr for t in ckm.model.lagrangian.terms if t.sector in ("yukawa", "other")))))
    pr_half = sum(term for term in sp.Add.make_args(L_yuk)
                  if all(b.gamma == diracPR for b in term.atoms(Bilinear)))
    assert pr_half != 0
    assert sp.expand(expand_bilinear(sp.expand(tc.unmatched["yukawa"])) - pr_half) == 0


def test_summary_and_parameters(ckm):
    """``summary()``: three flavours of each SM fermion; every parameter listed in order and
    ``check_parameters()`` finds no undeclared symbol."""
    s = ckm.model.summary()
    rows = {r[0]: tuple(str(x) for x in r[1:6]) for r in s.field_rows}
    for f in ("Ll", "eR", "QL", "uR", "dR"):
        assert rows[f][-1] == "3", (f, rows[f])
    assert rows["QL"][:4] == ("fermion L", "2", "1/6", "3")
    assert [r[0] for r in s.param_rows] == [q.name for q in ckm.params]
    assert ckm.model.check_parameters().undeclared == []


def test_integer_diagonal_flavour_matrix_entry(ckm):
    """With integer flavour indices, ``Y[a, a]`` is an ordinary diagonal entry: ``yukawa(Y, …,
    indices=(0, 0))`` returns ``−Y[0,0] L̄^0 H e_R^0 + h.c.``, equal to the scalar form on the one
    index with ``y → Y[0,0]`` (FG-11, resolved in feynlag 0.5.2; up to 0.5.1 it raised
    ``ValueError``, a check meant for symbolic indices). ``sm._flavour_matrix_term`` relies on it."""
    from feynlag import yukawa
    p, H = ckm.pieces, ckm.extra["ew"].H
    Y, y = sp.IndexedBase("Y"), sp.Symbol("y")
    Ll, eR = p.fermions["Ll"], p.fermions["eR"]
    term = yukawa(Y, Ll, H, eR, indices=(0, 0))
    assert term.has(Y[0, 0]) and term.has(Ll.eLbar[0]) and term.has(eR.eR[0])
    scalar = yukawa(y, Ll, H, eR, indices=0)
    assert sp.expand(term.xreplace({Y[0, 0]: y, sp.conjugate(Y[0, 0]): sp.conjugate(y)})
                     - scalar) == 0
    i = sp.Symbol("i", integer=True)                 # a repeated *symbolic* index is still refused
    with pytest.raises(ValueError):
        yukawa(Y, Ll, H, eR, indices=(i, i))


def test_scalar_coupling_integer_off_diagonal_raises(ckm):
    """With real flavour indices a scalar coupling on ``(a, b)``, ``a != b``, would move an
    off-diagonal Yukawa onto the diagonal; ``yukawa`` raises ``ValueError`` instead (FG-9, resolved
    in feynlag 0.5.2; up to 0.5.1 it silently returned the ``(0, 0)`` entry). The one-index
    diagonal form is unchanged."""
    from feynlag import yukawa
    p, H = ckm.pieces, ckm.extra["ew"].H
    QL, dR = p.fermions["QL"], p.fermions["dR"]
    y = sp.Symbol("y")
    diag = yukawa(y, QL, H, dR, indices=0)
    assert diag.has(dR.dR_1[0]) and not diag.has(dR.dR_1[1])
    with pytest.raises(ValueError, match="flavour-universal"):
        yukawa(y, QL, H, dR, indices=(0, 1))
