"""Model-independent verification helpers (dual symbolic + numeric checks)."""

import sympy as sp
from feynlag import numeric_equal


def free_symbols(*exprs):
    syms = set()
    for e in exprs:
        syms |= sp.sympify(e).free_symbols
    return sorted(syms, key=str)


def dual_equal(a, b, symbols=None, seed=0, n_points=12, tol=1e-9):
    """``a == b`` both symbolically (``simplify(a−b) == 0``) and numerically.

    Returns ``(symbolic_ok, numeric_ok, detail)``; tests assert on both so a
    failure names which route broke (CONVENTIONS.md dual-verification rule).
    """
    a, b = sp.sympify(a), sp.sympify(b)
    diff = sp.simplify(a - b)
    symbolic_ok = diff == 0
    symbols = symbols or free_symbols(a, b)
    if symbols:
        numeric_ok, detail = numeric_equal(a, b, symbols, seed=seed,
                                           n_points=n_points, tol=tol)
    else:
        numeric_ok, detail = abs(complex(a - b)) < tol, complex(a - b)
    return symbolic_ok, numeric_ok, (diff, detail)


def assert_dual_equal(a, b, symbols=None, seed=0, msg=""):
    s_ok, n_ok, detail = dual_equal(a, b, symbols=symbols, seed=seed)
    assert s_ok, f"{msg} symbolic residual: {detail[0]}"
    assert n_ok, f"{msg} numeric mismatch: {detail[1]}"


def numeric_matrix(M, values):
    """Substitute a numeric point and return a float/complex SymPy Matrix."""
    return sp.Matrix(M).subs(values).evalf()


def numeric_takagi(M, dps=50):
    """Takagi factorisation ``M = U D Uᵀ`` of a real symmetric numeric matrix at ``dps`` digits.

    Workaround for FG-5: feynlag's ``diagonalize_takagi`` diagonalises symbolically and does not
    finish on a generic ``N > 2`` matrix. Same convention as ``diagonalize_takagi`` (``U = Oᵀ``
    times a factor ``i`` on each column with a negative eigenvalue, ``D ≥ 0``); columns are ordered
    by increasing mass. High precision matters: a seesaw spectrum spans ~14 orders of magnitude.
    """
    import mpmath

    M = sp.Matrix(M)
    if M.free_symbols or sp.simplify(M - M.T) != sp.zeros(*M.shape):
        raise ValueError("numeric_takagi needs a numeric symmetric matrix")
    if any(sp.im(sp.N(x)) != 0 for x in M):
        raise ValueError("numeric_takagi handles real matrices only")
    n = M.rows
    with mpmath.workdps(dps):
        A = mpmath.matrix([[mpmath.mpf(str(sp.N(x, dps + 10))) for x in row]
                           for row in M.tolist()])
        E, Q = mpmath.eigsy(A)
        order = sorted(range(n), key=lambda k: abs(E[k]))
        U = sp.Matrix([[sp.Float(str(Q[a, k]), dps) * (sp.I if E[k] < 0 else 1) for k in order]
                       for a in range(n)])
        D = sp.diag(*[sp.Float(str(abs(E[k])), dps) for k in order])
    return U, D


def zero_eigenvalue_count(M, values, tol=1e-8):
    """Number of (numerically) vanishing eigenvalues of ``M`` at ``values``.

    Relative to the largest |eigenvalue|; used for Goldstone counting.
    """
    Mn = numeric_matrix(M, values)
    if Mn.shape == (0, 0):
        return 0
    eig = [complex(e) for e in Mn.eigenvals(multiple=True)]
    scale = max(abs(e) for e in eig) or 1.0
    return sum(1 for e in eig if abs(e) / scale < tol)


def massive_gauge_boson_count(M_gauge, values, tol=1e-8):
    """Rank of the gauge mass matrix at a numeric point (= broken generators)."""
    n = sp.Matrix(M_gauge).shape[0]
    return n - zero_eigenvalue_count(M_gauge, values, tol=tol)


def only_failures(report, names):
    """True if an ``InvarianceReport``'s failing terms are exactly ``names``.

    Used to pin *softly broken* symmetries: the only invariance failure must
    be the named soft term(s).
    """
    failing = sorted(term.name for term, _check, _d in report.failures)
    return failing == sorted(names), failing
