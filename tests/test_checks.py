"""The FG-5 workaround ``numeric_takagi`` against feynlag's own ``diagonalize_takagi``."""

import pytest
import sympy as sp

from feynlag import diagonalize_takagi, seesaw_mass_matrix
from feynlag_models.checks import numeric_takagi


def _block_seesaw():
    """feynlag's tests/test_seesaw.py 3+3 matrix: diagonal m_D, so it splits into 2×2 blocks."""
    mD = sp.diag(sp.Rational(2, 100), sp.Rational(3, 100), sp.Rational(5, 100))
    MR = sp.diag(sp.Integer(10)**3, 2 * 10**3, 5 * 10**3)
    return seesaw_mass_matrix(mD, MR)


def test_numeric_takagi_matches_feynlag_on_block_matrix():
    M = _block_seesaw()
    U, D = numeric_takagi(M)
    Uf, Df = diagonalize_takagi(M)
    ours = [D[k, k] for k in range(6)]
    theirs = sorted((sp.N(Df[k, k], 40) for k in range(6)), key=abs)
    assert all(abs(a - b) < sp.Float("1e-35") * max(abs(b), 1) for a, b in zip(ours, theirs))
    assert ours == sorted(ours)
    assert max(abs(x) for x in (U * D * U.T - M).evalf(45)) < 1e-40
    assert max(abs(x) for x in (U * U.conjugate().T - sp.eye(6)).evalf(45)) < 1e-40


def test_numeric_takagi_negative_eigenvalue_gets_phase_i():
    U, D = numeric_takagi(sp.Matrix([[0, 1], [1, 0]]))
    assert all(abs(D[k, k] - 1) < 1e-45 for k in range(2))
    assert any(x.has(sp.I) for x in U)
    assert max(abs(x) for x in (U * D * U.T - sp.Matrix([[0, 1], [1, 0]])).evalf(45)) < 1e-40


def test_numeric_takagi_rejects_non_symmetric_or_symbolic():
    with pytest.raises(ValueError):
        numeric_takagi(sp.Matrix([[0, 1], [2, 0]]))
    with pytest.raises(ValueError):
        numeric_takagi(sp.Matrix([[0, sp.Symbol("m")], [sp.Symbol("m"), 1]]))
