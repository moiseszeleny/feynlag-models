"""L0 (declared, invariant, anomaly-free) and L1 (tadpoles, spectrum, Goldstones, fermion masses)."""

import sympy as sp

from feynlag import (ZN, Model, check_discrete_invariance, check_global_invariance, diracPR,
                     fermion_mass_matrix)
from feynlag_models.checks import (assert_dual_equal, massive_gauge_boson_count,
                                   zero_eigenvalue_count)
from models.froggatt_nielsen.model import SECTORS, benchmark_flavour, fn_symmetry, mass_basis


def test_validate_exact_operators(fn):
    """The exact c (φ/Λ)^n operators: gauge invariant, U(1)_FN invariant, hermitian,
    anomaly-free, and of mass dimension 4 once Λ is counted (each 1/Λ^n balances φ^n)."""
    report = fn.extra["model_exact"].validate()
    assert report.ok, report.summary()
    assert report.checks["anomalies"] is not None and report.checks["anomalies"].ok
    for Y in fn.extra["Y_exact"].values():          # really higher-dimension, really complex
        assert Y.has(fn.extra["phi"]) and Y.has(sp.I)


def test_global_u1_fn_every_term(fn):
    """U(1)_FN (φ: +1, fermions: per-generation benchmark charges, H: 0) is declared on the exact
    model as a feynlag ``GlobalU1`` and holds in every term; one wrong charge breaks exactly the
    Yukawa it enters, and a Z_N with one charge per multiplet cannot express the symmetry."""
    model = fn.extra["model_exact"]
    assert model.global_groups == [fn.extra["U1_FN"]]
    report = model.check_invariance(hermiticity=False, dimension=False)
    assert not report.failures, report.failures
    # the check has teeth: one wrong u_R charge breaks the up Yukawa and nothing else
    wrong = dict(fn.extra["fn_charges"], uR=(-3, -1, 1))
    bad = fn_symmetry(fn.pieces, fn.extra["phiF"], wrong, name="U1_FN_wrong")
    probe = Model("fn_wrong_charges", gauge_groups=[], global_groups=[bad],
                  fields=model.fields, lagrangian=model.lagrangian)
    report = probe.check_invariance(hermiticity=False, dimension=False)
    assert {(term.name, label) for term, label, _ in report.failures} == {
        ("yukawa_up", "global:U1_FN_wrong")}
    # why a GlobalU1: the closest discrete group, a Z_N with the first-generation charges,
    # flags the off-diagonal entries of the same (U(1)_FN-invariant) up Yukawa
    p, q = fn.pieces, fn.extra["fn_charges"]
    Z = ZN("Z_FN", 64)
    Z.assign(1, fn.extra["phiF"])
    for k in ("QL", "uR"):
        Z.assign(q[k][0] % 64, p.fermions[k])
    assert check_global_invariance(fn.extra["L_exact"]["yukawa_up"], fn.extra["U1_FN"])[0]
    assert not check_discrete_invariance(fn.extra["L_exact"]["yukawa_up"], Z)[0]


def test_flavon_powers_follow_the_charges(fn):
    """Y^f_ij carries φ^n (φ^* when n < 0) with n = q(F_L,i) − q(f_R,j), and the linearised
    operator agrees with it at the vacuum and to first order in the flavon fluctuation."""
    e = fn.extra
    phi, w = e["phi"], e["vphi"].s / sp.sqrt(2)
    x = sp.Symbol("x")
    for sector, (left, right, _) in SECTORS.items():
        n = e["powers"][sector]
        for i in range(3):
            for j in range(3):
                nij = e["fn_charges"][left][i] - e["fn_charges"][right][j]
                assert n[i, j] == nij
                ex, lin = e["Y_exact"][sector][i, j], e["Y_linear"][sector][i, j]
                field = phi if nij >= 0 else sp.conjugate(phi)
                ex, lin = (y.subs(field, w + x) for y in (ex, lin))
                assert sp.simplify(ex.subs(x, 0) - lin.subs(x, 0)) == 0
                assert sp.simplify(sp.diff(ex, x).subs(x, 0) - sp.diff(lin, x)) == 0
                assert sp.diff(lin, x, 2) == 0


def test_tadpoles(fn):
    """μ² = λ v² + ½ λ_Hφ v_φ²,  μ_φ² = λ_φ v_φ² + ½ λ_Hφ v² (by hand from V, CONVENTIONS.md)."""
    e = fn.extra
    lam, v = e["ew"].lam.s, e["ew"].v.s
    lamPhi, lamHPhi, vphi = e["lamPhi"].s, e["lamHPhi"].s, e["vphi"].s
    assert_dual_equal(e["ew"].mu2.expr, lam * v**2 + lamHPhi * vphi**2 / 2, msg="mu2")
    assert_dual_equal(e["muPhi2"].expr, lamPhi * vphi**2 + lamHPhi * v**2 / 2, msg="muPhi2")


def test_cp_even_mass_matrix_and_spectrum(fn):
    """(h, s) block [[2λv², λ_Hφ v v_φ], [λ_Hφ v v_φ, 2λ_φ v_φ²]]; h1 is the lighter state."""
    e, vals = fn.extra, fn.values()
    lam, v = e["ew"].lam.s, e["ew"].v.s
    lamPhi, lamHPhi, vphi = e["lamPhi"].s, e["lamHPhi"].s, e["vphi"].s
    expected = sp.Matrix([[2 * lam * v**2, lamHPhi * v * vphi],
                          [lamHPhi * v * vphi, 2 * lamPhi * vphi**2]])
    for a in range(2):
        for b in range(2):
            assert_dual_equal(e["M_even"][a, b], expected[a, b], msg=f"M[{a},{b}]")
    assert 0 < vals[e["MH1"].s] < vals[e["MH2"].s]
    ok, res = e["rot"].check(e["M_even"], simplifier=lambda x: sp.nsimplify(
        sp.simplify(x.subs(e["theta"].s, e["rot"].angle_solution)), rational=False))
    assert ok, res


def test_goldstone_count(fn):
    """Three would-be Goldstones (eaten by W±, Z) plus the flavon phase a, the Goldstone of the
    spontaneously broken global U(1)_FN: four massless real scalars."""
    p, vals, b = fn.pieces, fn.values(), fn.bosons
    W1, W2, W3 = p.W.components
    Mg = fn.model.gauge_mass_matrix([W1, W2, W3, p.B.components[0]])
    assert massive_gauge_boson_count(Mg, vals) == 3
    M_odd = fn.model.mass_matrix([b["G0"], b["a"]])
    M_ch = fn.model.mass_matrix([b["Gp"]], charged=True)
    assert all(sp.simplify(x) == 0 for x in M_odd) and sp.simplify(M_ch[0, 0]) == 0
    assert zero_eigenvalue_count(M_odd, vals) + 2 * zero_eigenvalue_count(M_ch, vals) == 4


def _mass_blocks(fn, L):
    p = fn.pieces
    Ll, eR, QL, uR, dR = (p.fermions[k] for k in ("Ll", "eR", "QL", "uR", "dR"))
    return {"up": (L["yukawa_up"], QL.bar_components[0], uR.components[0]),
            "down": (L["yukawa_down"], QL.bar_components[3], dR.components[0]),
            "lepton": (L["yukawa_lepton"], Ll.bar_components[1], eR.components[0])}


def test_fermion_mass_matrices(fn):
    """M_f = (v/√2) c^f_ij ε^{n_ij}, ε = v_φ/(√2 Λ), from the exact operators and identically
    from the linearised ones (feynlag's fermion_mass_matrix, both vacua)."""
    e, idx = fn.extra, fn.pieces.idx
    v = e["ew"].v.s
    eps = {e["eps"].s: e["eps"].expr}
    for model, L in ((e["model_exact"], e["L_exact"]), (fn.model, e["L_linear"])):
        for sector, (Lf, bar, fld) in _mass_blocks(fn, L).items():
            M = fermion_mass_matrix(Lf, bar, fld, model.vacuum, 3, idx, gamma=diracPR)
            expected = (v / sp.sqrt(2) * e["Y"][sector]).subs(eps)
            for a in range(3):
                for b in range(3):
                    assert_dual_equal(M[a, b], expected[a, b], msg=f"{model.name} {sector}[{a},{b}]")


DPS = 60
TOL = sp.Float("1e-40", DPS)


def _max_abs(M):
    return max(abs(x) for x in M)


def test_mass_basis_diagonalises_yukawas(fn):
    """feynlag's numeric SVD (``model.mass_basis``) at the benchmark, for Y_u, Y_d, Y_e:
    R_L Y R_R† = diag(y) to 1e-40, y real, non-negative and ascending, R_L and R_R unitary to
    1e-40. ``mass_basis`` returns only Re D_kk, so the off-diagonal entries and Im D_kk are
    checked here from the rotations themselves."""
    vals = fn.values()
    for sector in SECTORS:
        R_L, R_R, y = mass_basis(fn.extra["Y"][sector], vals, DPS)
        Yn = sp.Matrix(fn.extra["Y"][sector]).subs(vals).evalf(DPS + 10)
        D = (R_L * Yn * R_R.H).evalf(DPS)
        assert _max_abs(D - sp.diag(*y)) < TOL, sector                      # off-diagonal and Im D_kk
        assert all(abs(sp.im(D[k, k])) < TOL for k in range(3)), sector
        assert all(yk >= 0 for yk in y) and y[0] < y[1] < y[2], (sector, y)
        for name, R in (("R_L", R_L), ("R_R", R_R)):
            assert _max_abs((R * R.H).evalf(DPS) - sp.eye(3)) < TOL, (sector, name)


def test_benchmark_flavour_values_match_spectrum_md(fn):
    """Regression pin: |V_us|, |V_cb|, |V_ub|, m_t, m_b at the benchmark equal the values printed
    in ``outputs/spectrum.md`` (6 significant figures), so a regenerated output cannot change
    them silently."""
    masses, absV = benchmark_flavour(fn)
    printed = {"|V_us|": (absV[0, 1], 0.191037), "|V_cb|": (absV[1, 2], 0.100278),
               "|V_ub|": (absV[0, 2], 0.0377582), "m_t": (masses["up"][2], 94.927),
               "m_b": (masses["down"][2], 12.4581)}
    for name, (value, expected) in printed.items():
        assert float(f"{float(value):.6g}") == expected, (name, value)
