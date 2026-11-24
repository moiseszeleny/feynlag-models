"""L0 (declared, invariant, anomaly-free) and L1 (tadpoles, spectrum, Goldstones, fermion masses)."""

import pytest
import sympy as sp

from feynlag import (FL_I, FL_J, ZN, Model, check_discrete_invariance, check_global_invariance, diracPR,
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
    spontaneously broken global U(1)_FN: four real scalars massless at tree level (a is an
    axiflavon once QCD is included; see ``test_u1_fn_colour_anomaly_coefficient``)."""
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
    e, idx = fn.extra, (FL_I, FL_J)
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


# ------------------------------------------------- feynlag 0.4.0 API (constructors, guided basis)

INTEGER_INDEX_YUKAWAS = {"Ll̄·H eR", "QL̄·H̃ uR", "QL̄·H dR"}


def test_constructors_reproduce_component_yukawas_exact_and_linear(fn):
    """``L_exact`` (``c (φ/Λ)^n``, ``φ*`` for ``n < 0``) and ``L_linear`` (the linear expansion), both
    built entry by entry through ``sm.yukawa_terms`` (``feynlag.terms.yukawa``, the placeholder
    route for field-dependent entries), equal the component-level pre-0.4.0 terms, both halves
    included; the h.c. carries ``conj(Y^{ab})``, i.e. ``φ*`` where the entry has ``φ`` and back."""
    import importlib.util
    from feynlag import expand_bilinear
    from feynlag_models import MODELS_DIR
    spec = importlib.util.spec_from_file_location(
        "_sm_ckm_l0_l1", MODELS_DIR / "sm_ckm" / "tests" / "test_l0_l1.py")
    ref_mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ref_mod)
    from models.froggatt_nielsen.model import benchmark_point, build
    X = lambda z: sp.expand(expand_bilinear(sp.expand(z)))   # noqa: E731
    # the benchmark (every n_ij >= 0) and a charge set with n < 0 entries: qd1 = +4 gives
    # n^d_i1 = (-1, -2, -4), built from (φ*)^{|n|} (as in test_flavon_couplings_negative_powers)
    fn_neg = build(dict(benchmark_point(), qd1=4))
    for bundle, negative in ((fn, False), (fn_neg, True)):
        e, p = bundle.extra, bundle.pieces
        H, phi = e["ew"].H, e["phi"]
        assert any(Y.has(sp.conjugate(phi)) for Y in e["Y_exact"].values()) is negative
        for tag in ("exact", "linear"):
            Y, L = e[f"Y_{tag}"], e[f"L_{tag}"]
            ref = ref_mod._component_level_yukawas_3(p, H, H, Y["lepton"], Y["down"], Y["up"])
            assert set(ref) == set(L)
            for name in ref:
                assert X(L[name] - ref[name]) == 0, (negative, tag, name)


def test_flavon_kinetic_and_potential_constructors(fn):
    """``kinetic(phiF)`` is ``(∂φ)*(∂φ)`` (φ is complex, FG-8 does not apply) and the potential's
    ``inner`` products are ``φ*φ`` and ``H†H``, the hand-written forms."""
    from feynlag import PartialMu, dag
    e = fn.extra
    phi, H = e["phi"], e["ew"].H
    terms = {t.name: t.expr for t in fn.extra["model_exact"].lagrangian.terms}
    assert sp.expand(terms["flavon_kinetic"]
                     - PartialMu(sp.conjugate(phi)) * PartialMu(phi)) == 0
    a2, HdH = phi * sp.conjugate(phi), (dag(H) * H.mat)[0]
    V = -e["muPhi2"].s * a2 + e["lamPhi"].s * a2**2 + e["lamHPhi"].s * HdH * a2
    assert sp.expand(terms["flavon_potential"] + V) == 0


def test_mass_blocks_report_scalar_gauge_and_flavoured_blocks(fn):
    """``mass_blocks`` on the linearised model: the CP-even ``(H0_r, phi_r)`` block, the eaten
    ``G0``/``G+`` and the CP-odd flavon ``a`` (U(1)_FN Goldstone, massless at tree level, not eaten, so not
    Goldstone-tagged); the SM gauge blocks; every charged fermion block flavoured, i.e. not
    diagonalizable symbolically (numeric SVD via ``mass_basis``), and ``ν_L`` massless."""
    m, b, p, e = fn.model, fn.bosons, fn.pieces, fn.extra
    scalar = m.mass_blocks(kind="scalar")
    assert [blk.fields for blk in scalar] == [[e["h_weak"], e["s0"]], [b["G0"]], [b["a"]], [b["Gp"]]]
    assert [bool(blk.goldstones) for blk in scalar] == [False, True, False, True]
    assert scalar[0].cp == "even" and scalar[2].cp == "odd"
    assert sp.simplify(m.mass_matrix([b["a"]])[0, 0].subs(fn.params.resolve())) == 0
    assert [blk.fields for blk in m.mass_blocks(kind="gauge")] == [
        list(p.W.components[:2]), [p.W.components[2], p.B.components[0]]]
    fermion = m.mass_blocks(kind="fermion")
    Ll = p.fermions["Ll"]
    (nu,) = [blk for blk in fermion if blk.fields == [Ll.nuL]]
    assert "massless" in nu.note
    flavoured = [blk for blk in fermion if blk is not nu]
    assert len(flavoured) == 7                      # e, and u, d per colour
    assert all(blk.diagonalizable is False and "flavoured" in blk.note for blk in flavoured)


def test_physical_registry(fn):
    """Charges (derived from the vacuum), conjugate pairs and Goldstones from ``model.physical``:
    the flavon phase ``a`` is a neutral physical state, not among the eaten Goldstones."""
    b = fn.bosons
    assert fn.charges == {b["h1"]: 0, b["h2"]: 0, b["a"]: 0, b["G0"]: 0, b["Gp"]: 1, b["Gm"]: -1,
                          b["Z"]: 0, b["A"]: 0, b["Wp"]: 1, b["Wm"]: -1}
    assert fn.conjugates == {b["Gp"]: b["Gm"], b["Gm"]: b["Gp"], b["Wp"]: b["Wm"], b["Wm"]: b["Wp"]}
    assert fn.goldstones == (b["G0"], b["Gp"], b["Gm"])


def test_term_coverage_model_exact(fn):
    """``term_coverage`` on ``model_exact``. Present: the whole potential, in feynlag's
    ``V = Σ c O`` (``−μ²``, ``−μ_φ²``, ``λ``, ``λ_Hφ``, ``λ_φ``). Missing: only the three Yukawa
    operators. The FN Yukawas sit at explicit integer flavour indices and are operators above
    dimension 4, both outside the operator basis (``TermCoverage`` documents the integer-index
    case). The declared ``GlobalU1`` is imposed on the suggestions since feynlag 0.5.2 (FG-13,
    resolved), so no U(1)_FN-violating flavon operator (``φ²``, ``φ H†H``, …) is listed; that is
    pinned by ``test_term_coverage_imposes_global_symmetry``.

    The remainder is exactly the ``P_R`` half of the FN Yukawas. ``term_coverage`` decomposes only
    that half (feynlag ``general.py``, ``_canonical_fermion_half``), so the conjugated half and its
    phase are covered by ``test_constructors_reproduce_component_yukawas_exact_and_linear``."""
    from feynlag import Bilinear, expand_bilinear
    e = fn.extra
    ex = e["model_exact"]
    tc = ex.term_coverage()
    assert {t.label: c for t, c in tc.present} == {
        "(H†H)": -e["ew"].mu2.s, "phi phi†": -e["muPhi2"].s, "(H†H) (H†H)": e["ew"].lam.s,
        "phi phi† (H†H)": e["lamHPhi"].s, "phi phi phi† phi†": e["lamPhi"].s}
    assert {t.label for t in tc.missing} == INTEGER_INDEX_YUKAWAS
    assert set(tc.unmatched) == {"yukawa"}
    L_fer = sp.expand(expand_bilinear(sp.expand(sum(
        t.expr for t in ex.lagrangian.terms if t.sector in ("yukawa", "other")))))
    pr_half = sum(term for term in sp.Add.make_args(L_fer)
                  if all(x.gamma == diracPR for x in term.atoms(Bilinear)))
    assert pr_half.has(e["phi"])                    # the FN operators (every n_ij >= 0 here)
    assert sp.expand(expand_bilinear(sp.expand(tc.unmatched["yukawa"])) - pr_half) == 0


def test_summary_and_parameters(fn):
    """``summary()`` of both models: the flavon is a complex gauge singlet with U(1)_FN charge 1 on
    ``model_exact``; every parameter is listed in order and none is undeclared."""
    assert fn.params is fn.pieces.params        # one ParameterSet, extended in place
    ex = fn.extra["model_exact"]
    s = ex.summary()
    assert s.field_header[:6] == ["field", "type", "SU2L", "U1Y", "SU3c", "U1_FN"]
    rows = {r[0]: tuple(str(x) for x in r[1:6]) for r in s.field_rows}
    assert rows["phi"] == ("scalar", "1", "0", "1", "1")
    assert set(rows) == {"H", "W", "B", "G", "Ll", "eR", "QL", "uR", "dR", "phi"}
    for model, params in ((ex, list(ex.parameters)), (fn.model, list(fn.params))):
        assert [r[0] for r in model.summary().param_rows] == [q.name for q in params]
        assert model.check_parameters().undeclared == []
    # the exact model has no linearised-model internals
    assert {q.name for q in ex.parameters}.isdisjoint({"MW", "MZ", "theta", "MH1", "MH2"})


def test_consumer_interface(fn):
    """feynlag-anomalies ``flavor_puzzle`` reads ``Yu``, ``Yd``, ``c_params``, ``eps``, ``ew``, ``powers``
    and ``mass_basis``: ``Y = C·ε^|n|`` in exactly the ``c_params`` and ``eps`` symbols."""
    e = fn.extra
    syms = {q.s for q in e["c_params"]} | {e["eps"].s}
    for sector, key in (("up", "Yu"), ("down", "Yd")):
        Y, n, C = e[key], e["powers"][sector], e["C"][sector]
        assert Y.free_symbols <= syms
        assert all(sp.expand(Y[i, j] - C[i, j] * e["eps"].s ** abs(n[i, j])) == 0
                   for i in range(3) for j in range(3))
    y = mass_basis(e["Yu"], fn.values())[2]
    assert list(y) == sorted(y)


def test_term_coverage_imposes_global_symmetry(fn):
    """``term_coverage`` decomposes on the operator basis "for the model's own fields and declared
    symmetries", the declared ``GlobalU1`` U(1)_FN included: no missing operator carries net FN
    charge (FG-13, resolved in feynlag 0.5.2; up to 0.5.1 ``φ²``, ``φ H†H``, ``φ³``, ``φ²φ*``,
    ``φ² H†H``, ``φ⁴`` and ``φ³φ*`` were listed as missing)."""
    e = fn.extra
    try:                                                        # setup: U(1)_FN declared and holds
        ex, U = e["model_exact"], e["U1_FN"]
        if ex.global_groups != [U] or not ex.validate().ok:
            raise RuntimeError("U(1)_FN is not declared on model_exact, or validate() fails")
        missing = ex.term_coverage().missing
    except Exception as exc:
        pytest.fail(f"setup: {exc!r}")
    violating = []
    for t in missing:
        try:
            ok = check_global_invariance(t.expr, U)[0]
        except ValueError:     # a Yukawa suggestion on symbolic flavour indices: no per-generation
            continue           # charge to check (the integer-index limitation)
        if not ok:
            violating.append(t.label)
    assert violating == [], violating
    # the seven operators feynlag 0.5.1 listed (net FN charges 2, 1, 3, 1, 2, 4, 2) are gone
    old = {"phi phi", "phi (H†H)", "phi phi phi", "phi phi phi†", "phi phi (H†H)",
           "phi phi phi phi", "phi phi phi phi†"}
    assert old.isdisjoint(t.label for t in missing)


def test_without_keeps_order_kinds_and_tex():
    """``_without`` (``ParameterSet`` has no removal method) drops exactly the named parameters and
    keeps the remaining ones as the same objects, in order, with their kind and tex."""
    from feynlag import ParameterSet
    from models.froggatt_nielsen.model import _without
    from models.sm import model as sm
    from models.sm_ckm.model import benchmark_point as ckm_benchmark
    P = sm.pieces(ckm_benchmark(), generations=3).params      # three-generation mass inputs
    dropped = [n for row in sm.MASS_NAMES[3] for n in row] + ["yt", "ytau"]
    Q = _without(P, dropped)
    assert isinstance(Q, ParameterSet) and Q is not P
    kept = [q for q in P if q.name not in dropped]
    assert [q.name for q in Q] == [q.name for q in kept] and len(kept) == len(P) - len(dropped)
    for a, b in zip(Q, kept):
        assert a is b and type(a) is type(b) and a.tex == b.tex
    assert [q.name for q in P][:3] == ["gw", "g1", "gs"]       # P itself is untouched
    assert len(P) == len(Q) + len(dropped)
