"""Numeric biunitary decomposition (feynlag_models.flavor, FG-6 workaround)."""

import itertools

import mpmath as mp
import numpy as np
import pytest
import sympy as sp

from feynlag_models.flavor import (ckm_from_yukawas, mass_spectrum, mp_biunitary,
                                   numeric_biunitary)

RNG = np.random.default_rng(20261005)


def _random_complex(n=3):
    return RNG.normal(size=(n, n)) + 1j * RNG.normal(size=(n, n))


RANDOM = [_random_complex() for _ in range(5)]


@pytest.mark.parametrize("M", RANDOM)
def test_reconstruction_mpmath(M):
    with mp.workdps(30):
        UL, m, UR = mp_biunitary(M, dps=30)
        A = mp.matrix(M.tolist())
        R = UL * mp.diag(m) * UR.H - A
        assert mp.mnorm(R, 1) / mp.mnorm(A, 1) < mp.mpf("1e-20")


@pytest.mark.parametrize("M", RANDOM)
def test_reconstruction_unitarity_ordering_float(M):
    UL, m, UR = numeric_biunitary(M)
    assert np.allclose(UL @ np.diag(m) @ UR.conj().T, M, rtol=0, atol=1e-12)
    assert np.allclose(UL.conj().T @ UL, np.eye(3), atol=1e-12)
    assert np.allclose(UR.conj().T @ UR, np.eye(3), atol=1e-12)
    assert np.all(m >= 0) and np.all(np.diff(m) >= 0)


@pytest.mark.parametrize("M", RANDOM)
def test_masses_match_numpy_svd(M):
    _, m, _ = numeric_biunitary(M)
    assert np.allclose(m, np.sort(np.linalg.svd(M, compute_uv=False)), rtol=1e-12, atol=0)


def test_sympy_input_with_values():
    a, b = sp.symbols("a b")
    M = sp.Matrix([[a, sp.I * b, 0], [0, a, b], [b, 0, 2 * a]])
    vals = {a: sp.Rational(3, 2), b: sp.Rational(1, 3)}
    _, m, _ = numeric_biunitary(M, values=vals)
    Mn = np.array(M.subs(vals).evalf(), dtype=complex)
    assert np.allclose(m, np.sort(np.linalg.svd(Mn, compute_uv=False)), rtol=1e-12)
    with pytest.raises(ValueError):
        numeric_biunitary(M)


def _hierarchical(a, b, eps=sp.Rational(1, 1000)):
    """Exact ``c_ij eps^(a_i+b_j)`` with O(1) complex rational ``c_ij``."""
    c = RNG.integers(1, 10, size=(3, 3, 2))
    return sp.Matrix(3, 3, lambda i, j: (c[i, j, 0] + sp.I * c[i, j, 1]) / 7
                     * eps ** (a[i] + b[j]))


@pytest.mark.parametrize("powers,dps", [((2, 1, 0), 30), ((3, 1, 0), 40)])
def test_hierarchical_det(powers, dps):
    M = _hierarchical(powers, powers)
    exact = sp.Abs(sp.expand(M.det()))
    _, m, _ = numeric_biunitary(M, dps=dps)
    assert abs(np.prod(m) / float(exact) - 1) < 1e-15
    with mp.workdps(dps):  # tighter, in mpmath itself
        mm = mp_biunitary(M, dps=dps)[1]
        ex = mp.mpf(str(sp.N(exact, dps + 5)))
        assert abs(mm[0] * mm[1] * mm[2] / ex - 1) < mp.mpf("1e-20")
    # the lightest mass is ~eps^(2 a_1) times the heaviest: mpmath resolves it to 1e-15
    m_light_exact = float(exact) / (m[1] * m[2])
    assert abs(m[0] / m_light_exact - 1) < 1e-15
    if powers == (3, 1, 0):
        m_np = np.sort(np.linalg.svd(np.array(M.evalf(), dtype=complex), compute_uv=False))
        assert m[0] / m[2] < 1e-15
        # LAPACK keeps graded matrices partly accurate, but loses ~8 digits here
        assert abs(m_np[0] / m_light_exact - 1) > 1e-12


def _is_permutation(A, tol=1e-12):
    return any(np.allclose(A, np.eye(3)[list(p)], atol=tol)
               for p in itertools.permutations(range(3)))


def test_ckm_unitary_random():
    V = ckm_from_yukawas(RANDOM[0], RANDOM[1])
    assert np.allclose(V.conj().T @ V, np.eye(3), atol=1e-12)


def test_ckm_diagonal_yukawas():
    Yu = np.diag([1e-5, 7e-3, 0.99]) * np.exp(1j * np.array([0.3, -1.1, 2.0]))
    Yd = np.diag([2.7e-5, 5.5e-4, 2.4e-2])
    assert np.allclose(np.abs(ckm_from_yukawas(Yu, Yd)), np.eye(3), atol=1e-12)
    Yd_perm = np.diag([2.4e-2, 2.7e-5, 5.5e-4])     # unsorted input: still a permutation
    assert _is_permutation(np.abs(ckm_from_yukawas(Yu, Yd_perm)))


def test_mass_spectrum():
    v = sp.Symbol("v")
    Y = np.diag([0.99, 1e-5, 7e-3])
    m = mass_spectrum(Y, v, values={v: 246})
    assert np.allclose(m, 246 / np.sqrt(2) * np.array([1e-5, 7e-3, 0.99]), rtol=1e-14)
