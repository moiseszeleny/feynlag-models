"""L0/L1: invariance, anomalies, the 5×5 seesaw mass matrix and its Takagi spectrum."""

import signal

import pytest
import sympy as sp

from feynlag import diagonalize_takagi
from feynlag_models.checks import (assert_dual_equal, massive_gauge_boson_count,
                                   numeric_takagi, zero_eigenvalue_count)


def _mass(ss, k):
    return ss.extra["D"][k, k]


def test_validate_invariance_and_anomalies(ss):
    """The 3×2 Dirac Yukawa via H̃ and the two Majorana masses are gauge invariant and
    hermitian; the gauge-singlet ν_R leave the anomaly cancellation of `sm` untouched."""
    report = ss.model.validate()
    assert report.ok, report.summary()
    assert report.checks["anomalies"] is not None and report.checks["anomalies"].ok


@pytest.mark.xfail(strict=True, raises=TimeoutError,
                   reason="FG-5: diagonalize_takagi is symbolic and does not finish on a generic 5×5")
def test_feynlag_takagi_generic_matrix_gap(ss):
    """feynlag's own Takagi factorisation of the benchmark 5×5 within 10 s."""
    def timeout(*_):
        raise TimeoutError
    old = signal.signal(signal.SIGALRM, timeout)
    signal.alarm(10)
    try:
        diagonalize_takagi(ss.extra["Mn"])
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, old)


def test_mass_matrix_entries(ss):
    """feynlag's square fermion_mass_matrix has an exactly zero third column (no ν_R3); the
    3×2 m_D = y_ν v/√2 entry by entry, M_R = diag(M_1, M_2), and M_ν = [[0, m_D], [m_D^T, M_R]]."""
    e = ss.extra
    v = e["ew"].v.s
    assert e["mD_full"].shape == (3, 3)
    assert e["mD_full"][:, 2] == sp.zeros(3, 1)
    assert e["mD"].shape == (3, 2)
    for a in range(3):
        for b in range(2):
            assert_dual_equal(e["mD"][a, b], e["yv"][a, b] * v / sp.sqrt(2), msg=f"m_D[{a},{b}]")
    assert_dual_equal(e["MRmat"][0, 0], e["MR"][0].s, msg="M_1")
    assert_dual_equal(e["MRmat"][1, 1], e["MR"][1].s, msg="M_2")
    assert e["MRmat"][0, 1] == 0 and e["MRmat"][1, 0] == 0
    Mnu = e["Mnu"]
    assert Mnu.shape == (5, 5)
    assert Mnu[:3, :3] == sp.zeros(3, 3)
    assert Mnu[:3, 3:] == e["mD"] and Mnu[3:, :3] == e["mD"].T and Mnu[3:, 3:] == e["MRmat"]
    assert sp.simplify(Mnu - Mnu.T) == sp.zeros(5, 5)


def test_takagi_spectrum_at_benchmark(ss):
    """U D Uᵀ reconstructs M_ν at the benchmark to ~40 digits, U is unitary, D ≥ 0 increasing."""
    e = ss.extra
    U, D, Mn = e["U"], e["D"], e["Mn"]
    assert max(abs(x) for x in (U * D * U.T - Mn).evalf(45)) < 1e-40 * e["Mn"][4, 4]
    assert max(abs(x) for x in (U * U.conjugate().T - sp.eye(5)).evalf(45)) < 1e-40
    masses = [D[k, k] for k in range(5)]
    assert all(m >= 0 for m in masses) and masses == sorted(masses)


def test_light_sector_rank_two(ss):
    """Two ν_R and three lepton doublets: exactly one massless light neutrino, two massive light
    states with distinct masses (two independent Δm²), and two heavy states at M_1, M_2."""
    e, vals = ss.extra, ss.values()
    m = [_mass(ss, k) for k in range(5)]
    assert m[0] < 1e-30 * m[1]
    assert 0 < m[1] < m[2] < 1e-9 * m[3]
    assert (m[2]**2 - m[1]**2) > 1e-3 * m[2]**2
    for k, M in ((3, e["MR"][0].s), (4, e["MR"][1].s)):
        assert abs(m[k] / vals[M] - 1) < 1e-9


def test_seesaw_formula_matrix(ss):
    """The light Takagi masses are the singular values of m_ν = −m_D M_R⁻¹ m_Dᵀ up to
    O(m_D²/M_R²) corrections, including the exact zero."""
    e = ss.extra
    num = {s: sp.nsimplify(val, rational=True) for s, val in ss.values().items()
           if s in e["m_light_approx"].free_symbols}
    _, Dl = numeric_takagi(e["m_light_approx"].subs(num))
    for k in range(3):
        exact, approx = _mass(ss, k), Dl[k, k]
        assert abs(exact - approx) < 1e-9 * _mass(ss, 1), (k, exact, approx)
    for k in (1, 2):
        assert abs(_mass(ss, k) / Dl[k, k] - 1) < 1e-9


def test_light_heavy_mixing_at_benchmark(ss):
    """|U[ν_a, N_m]| ≈ |(m_D M_R⁻¹)_{am}| (V ≈ m_D M_R⁻¹, Atre et al. below Eq. 2.5)."""
    e, vals = ss.extra, ss.values()
    V = (e["mD"] * e["MRmat"].inv()).subs(vals)
    for a in range(3):
        for m in range(2):
            ours = abs(complex(e["U"][a, 3 + m]))
            theirs = abs(float(V[a, m]))
            assert abs(ours - theirs) < 1e-6 * theirs, (a, m, ours, theirs)


def test_goldstone_count_unchanged(ss):
    p, vals = ss.pieces, ss.values()
    W1, W2, W3 = p.W.components
    Mg = ss.model.gauge_mass_matrix([W1, W2, W3, p.B.components[0]])
    assert massive_gauge_boson_count(Mg, vals) == 3
    M_odd = ss.model.mass_matrix([ss.bosons["G0"]])
    M_ch = ss.model.mass_matrix([ss.bosons["Gp"]], charged=True)
    assert zero_eigenvalue_count(M_odd, vals) + 2 * zero_eigenvalue_count(M_ch, vals) == 3
