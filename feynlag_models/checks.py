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


def global_u1_table(fermion_charges, scalar_charges):
    """Charge lookup for :func:`global_u1_violations` (FG-7 workaround: no global U(1) in feynlag).

    ``fermion_charges`` maps a ``WeylFermion`` to one charge per flavour (every gauge component
    shares it; bar legs carry minus it); ``scalar_charges`` maps a scalar component symbol to its
    charge (its ``conjugate`` carries minus it).
    """
    legs = {}
    for F, qs in fermion_charges.items():
        for comp, bar in zip(F.components, F.bar_components):
            for k, q in enumerate(qs):
                legs[(comp, k)], legs[(bar, k)] = sp.Integer(q), -sp.Integer(q)
    return legs, {s: sp.Integer(q) for s, q in scalar_charges.items()}


def _u1_charge(node, legs, scalars):
    from feynlag import Bilinear, PartialMu
    if node.is_Number or node.is_NumberSymbol or node is sp.I:
        return 0
    if isinstance(node, Bilinear):
        total = 0
        for leg in (node.bar, node.field):
            k = leg.indices[0]
            if not k.is_Integer:
                raise ValueError(f"symbolic flavour index in {node}")
            total += legs.get((leg.base, int(k)), 0)
        return total
    if isinstance(node, sp.Pow):
        if node.exp.is_Integer:
            return int(node.exp) * _u1_charge(node.base, legs, scalars)
        if node.base.free_symbols & set(scalars):
            raise ValueError(f"non-integer power of a charged field: {node}")
        return 0
    if isinstance(node, sp.Mul):
        return sum(_u1_charge(f, legs, scalars) for f in node.args)
    if isinstance(node, sp.conjugate):
        return -_u1_charge(node.args[0], legs, scalars)
    if isinstance(node, PartialMu):
        return _u1_charge(node.args[0], legs, scalars)
    if isinstance(node, sp.Symbol):
        return scalars.get(node, 0)
    if node.free_symbols & set(scalars):
        raise ValueError(f"cannot assign a U(1) charge to {type(node).__name__}: {node}")
    return 0       # a function of parameters only (exp(i alpha), ...)


def global_u1_violations(expr, legs, scalars):
    """``[(charge, monomial)]`` for every monomial of ``expand(expr)`` with non-zero total charge."""
    out = []
    for term in sp.Add.make_args(sp.expand(expr)):
        q = _u1_charge(term, legs, scalars)
        if q != 0:
            out.append((q, term))
    return out
