"""Numeric biunitary (singular-value) decomposition of complex Dirac mass/Yukawa matrices.

FG-6 workaround: feynlag 0.2.0's ``diagonalize_svd`` is symbolic and real-only, so complex
3x3 flavour matrices are decomposed here, outside feynlag, with ``mpmath.svd_c``.

Convention: ``M = UL * diag(m) * UR^†`` with ``m`` real, non-negative and ascending (light to
heavy, the SM generation order u, c, t). For a Lagrangian ``-Qbar_i Y_ij H f_Rj`` the left
rotation is ``UL``. Each column of ``UL`` and ``UR`` is fixed only up to a phase common to
both (and a degenerate block only up to a unitary rotation), so rotations and the CKM matrix
are physical only up to rephasing; ``|V|`` and the masses are physical.
"""

import mpmath as mp
import numpy as np
import sympy as sp


def _to_mpc(x, values, dps):
    """One matrix entry as an ``mpmath.mpc`` at ``dps`` digits."""
    if isinstance(x, (complex, float, int, np.number)) and not values:
        return mp.mpc(complex(x))
    x = sp.sympify(x)
    if values:
        x = x.subs(values)
    re, im = sp.N(x, dps + 5).as_real_imag()
    if re.free_symbols or im.free_symbols:
        raise ValueError(f"entry {x} is not numeric; pass `values`")
    return mp.mpc(mp.mpf(str(sp.N(re, dps + 5))), mp.mpf(str(sp.N(im, dps + 5))))


def mp_matrix(M, values=None, dps=30):
    """``M`` (SymPy Matrix, nested list or numpy array) as an ``mpmath.matrix``."""
    rows = sp.Matrix(M).tolist() if isinstance(M, sp.MatrixBase) else np.asarray(M, dtype=object).tolist()
    with mp.workdps(dps):
        return mp.matrix([[_to_mpc(x, values, dps) for x in row] for row in rows])


def mp_biunitary(M, values=None, dps=30):
    """``(UL, m, UR)`` as mpmath objects at ``dps`` digits; see :func:`numeric_biunitary`."""
    with mp.workdps(dps):
        A = mp_matrix(M, values, dps)
        U, S, Vh = mp.svd_c(A)          # A = U diag(S) Vh, S descending
        n = len(S)
        order = sorted(range(n), key=lambda i: S[i])
        UL = mp.matrix(A.rows, n)
        UR = mp.matrix(A.cols, n)
        for k, i in enumerate(order):
            for r in range(A.rows):
                UL[r, k] = U[r, i]
            for r in range(A.cols):
                UR[r, k] = mp.conj(Vh[i, r])
        return UL, [S[i] for i in order], UR


def _np(A):
    return np.array([[complex(A[i, j]) for j in range(A.cols)] for i in range(A.rows)])


def numeric_biunitary(M, values=None, dps=30):
    """``(UL, masses, UR)`` with ``M = UL diag(masses) UR^†``, masses ascending.

    Computed with ``mpmath.svd_c`` at ``dps`` digits (hierarchies of 1e-6 and below lose
    digits in float64) and returned as numpy arrays. Columns are defined up to a common
    phase per column.
    """
    UL, m, UR = mp_biunitary(M, values, dps)
    return _np(UL), np.array([float(x) for x in m]), _np(UR)


def ckm_from_yukawas(Yu, Yd, values=None, dps=30):
    """``V = UL_u^† UL_d`` for ``-Qbar Y H f_R`` Yukawas; rows u,c,t and columns d,s,b.

    Only ``|V|`` (and rephasing invariants) is physical.
    """
    with mp.workdps(dps):
        ULu = mp_biunitary(Yu, values, dps)[0]
        ULd = mp_biunitary(Yd, values, dps)[0]
        return _np(ULu.H * ULd)


def mass_spectrum(Y, v, values=None, dps=30):
    """Ascending Dirac masses ``v/sqrt(2)`` times the singular values of ``Y``."""
    with mp.workdps(dps):
        vv = _to_mpc(v, values, dps).real
        return np.array([float(vv / mp.sqrt(2) * s) for s in mp_biunitary(Y, values, dps)[1]])
