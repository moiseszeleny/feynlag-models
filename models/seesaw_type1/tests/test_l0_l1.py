"""L0/L1: invariance, anomalies, the seesaw mass matrix and its Takagi spectrum."""

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
