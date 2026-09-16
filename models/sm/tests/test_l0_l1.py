"""L0 (declared, invariant, anomaly-free) and L1 (tadpoles, spectrum, Goldstones)."""

import sympy as sp

from feynlag import diracPR, fermion_mass_matrix
from feynlag_models.checks import (assert_dual_equal, massive_gauge_boson_count,
                                   zero_eigenvalue_count)


def test_validate_invariance_and_anomalies(sm):
    report = sm.model.validate()
    assert report.ok, report.summary()
    assert report.checks["anomalies"] is not None        # quarks present → really checked
    assert report.checks["anomalies"].ok


def test_tadpole_and_higgs_mass(sm):
    ew = sm.extra["ew"]
    lam, v = ew.lam.s, ew.v.s
    assert_dual_equal(ew.mu2.expr, lam * v**2, msg="mu2")
    M = sm.model.mass_matrix([sm.bosons["h"]])
    assert_dual_equal(M[0, 0], 2 * lam * v**2, msg="m_h^2")


def test_gauge_masses(sm):
    p = sm.pieces
    W1, W2, W3 = p.W.components
    B = p.B.components[0]
    M = sm.model.gauge_mass_matrix([W1, W2, W3, B])
    g, gp, v = p.gw.s, p.g1.s, p.ew.v.s
    assert_dual_equal(M[0, 0], g**2 * v**2 / 4, msg="m_W^2")
    assert_dual_equal(M[1, 1], g**2 * v**2 / 4, msg="m_W^2")
    assert sp.simplify(M.det()) == 0                       # massless photon
    # Z, photon from the (W3, B) block eigenvalues
    block = M.extract([2, 3], [2, 3])
    eig = list(block.eigenvals().keys())
    assert any(sp.simplify(e) == 0 for e in eig)
    assert any(sp.simplify(e - (g**2 + gp**2) * v**2 / 4) == 0 for e in eig)


def test_goldstone_count(sm):
    """#massless would-be Goldstones == #massive gauge bosons (= 3)."""
    p, vals = sm.pieces, sm.values()
    W1, W2, W3 = p.W.components
    Mg = sm.model.gauge_mass_matrix([W1, W2, W3, p.B.components[0]])
    n_massive = massive_gauge_boson_count(Mg, vals)
    M_odd = sm.model.mass_matrix([sm.bosons["G0"]])
    M_ch = sm.model.mass_matrix([sm.bosons["Gp"]], charged=True)
    n_goldstone = (zero_eigenvalue_count(M_odd, vals)
                   + 2 * zero_eigenvalue_count(M_ch, vals))
    assert n_massive == 3
    assert n_goldstone == n_massive
    assert sp.simplify(M_odd[0, 0]) == 0 and sp.simplify(M_ch[0, 0]) == 0


def test_fermion_masses(sm):
    p = sm.pieces
    i, j = p.idx
    Ll, eR, QL, uR, dR = (p.fermions[k] for k in ("Ll", "eR", "QL", "uR", "dR"))
    vac = sm.model.vacuum
    v = p.ew.v.s
    cases = {
        "tau": (p.yukawa["yukawa_tau"], Ll.bar_components[1], eR.components[0], p.masses["MTA"]),
        "t": (p.yukawa["yukawa_t"], QL.bar_components[0], uR.components[0], p.masses["MT"]),
        "b": (p.yukawa["yukawa_b"], QL.bar_components[3], dR.components[0], p.masses["MB"]),
    }
    for name, (L, bar, fld, M) in cases.items():
        m = fermion_mass_matrix(L, bar, fld, vac, 1, (i, j), gamma=diracPR)[0, 0]
        y = sm.params[f"y{'tau' if name == 'tau' else name}"].expr
        assert_dual_equal(m.subs(sm.params.resolve()), M.s, msg=f"m_{name}")
        assert_dual_equal(y, sp.sqrt(2) * M.s / v, msg=f"y_{name}")
