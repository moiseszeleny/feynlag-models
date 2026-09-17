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
