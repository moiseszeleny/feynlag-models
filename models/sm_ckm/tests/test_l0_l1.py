"""L0 (declared, invariant, anomaly-free) and L1 (tadpoles, spectrum, Goldstones)."""

import pytest
import sympy as sp

from feynlag import diracPR, fermion_mass_matrix
from feynlag_models.checks import (assert_dual_equal, fermion_mass_block,
                                   massive_gauge_boson_count, zero_eigenvalue_count)


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
    input masses (d'_L = V d_L, d_R unrotated). Masses read with the FG-4 workaround."""
    vac, res = ckm.model.vacuum, ckm.params.resolve()
    V = ckm.extra["V_expr"]
    for name, (L, bar, fld, mnames) in _mass_blocks(ckm).items():
        M = fermion_mass_block(L, bar, fld, vac, 3, gamma=diracPR).subs(res)
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


@pytest.mark.xfail(strict=True, reason="FG-4: fermion_mass_matrix mangles integer flavour indices")
def test_feynlag_fermion_mass_matrix_integer_flavour_gap(ckm):
    """feynlag's own ``fermion_mass_matrix`` on the diagonal up Yukawa should give
    diag(m_u, m_c, m_t); at the pinned commit it does not (FEYNLAG_GAPS.md FG-4)."""
    L, bar, fld, mnames = _mass_blocks(ckm)["up"]
    i, j = ckm.pieces.idx
    M = fermion_mass_matrix(L, bar, fld, ckm.model.vacuum, 3, (i, j), gamma=diracPR)
    M = M.subs(ckm.params.resolve())
    D = sp.diag(*(ckm.pieces.masses[n].s for n in mnames))
    assert sp.simplify(M - D) == sp.zeros(3, 3)
