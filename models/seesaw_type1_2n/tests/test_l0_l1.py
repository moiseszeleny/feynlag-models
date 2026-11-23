"""L0/L1: invariance, anomalies, the 5×5 seesaw mass matrix and its Takagi spectrum."""

import sympy as sp

from feynlag import diagonalize_takagi
from feynlag_models.checks import (assert_dual_equal, massive_gauge_boson_count,
                                   zero_eigenvalue_count)


def _mass(ss, k):
    return ss.extra["D"][k, k]


def test_validate_invariance_and_anomalies(ss):
    """The 3×2 Dirac Yukawa via H̃ and the two Majorana masses are gauge invariant and
    hermitian; the gauge-singlet ν_R leave the anomaly cancellation of `sm` untouched."""
    report = ss.model.validate()
    assert report.ok, report.summary()
    assert report.checks["anomalies"] is not None and report.checks["anomalies"].ok


def test_mass_matrix_entries(ss):
    """The 3×2 m_D (the (ν_L, ν_R) block of ``mass_blocks``) = y_ν v/√2 entry by entry, and agrees
    with feynlag's square ``fermion_mass_matrix``, whose third column is exactly zero (no ν_R3);
    M_R = diag(M_1, M_2), and M_ν = [[0, m_D], [m_D^T, M_R]]."""
    from feynlag import diracPR, fermion_mass_matrix
    e, p = ss.extra, ss.pieces
    v = e["ew"].v.s
    Ll, nR = p.fermions["Ll"], e["nuR"].nuR
    full = fermion_mass_matrix(e["LYukD"], Ll.nuLbar, nR, ss.model.vacuum, 3, p.idx, gamma=diracPR)
    assert full.shape == (3, 3) and full[:, 2] == sp.zeros(3, 1)
    assert e["mD"].shape == (3, 2)
    assert sp.simplify(e["mD"] - full[:, :2]) == sp.zeros(3, 2)
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
    _, Dl = diagonalize_takagi(e["m_light_approx"].subs(num), method="numeric")
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


def test_majorana_table_precision(ss):
    """The light-neutrino Higgs couplings are 10⁻²³–10⁻²⁹, left after cancellations of ~20 orders
    between products of the 50-digit Takagi matrix: in double precision their printed digits
    were wrong (``3.211e-28`` for 3.172e-28, ``8.460e-28`` for 8.445e-28, ``1.493e-29`` for
    1.286e-29, ``3.930e-29`` for 4.049e-29, ``7.892e-23`` for 4.841e-23). The table now evaluates
    at 40 digits with exact inputs. Each of the five is checked against an independent Takagi
    factorisation at 100 digits, evaluated at 120."""
    from feynlag import MajoranaRotation, diagonalize_takagi, extract_fermion_vertices
    from models.seesaw_type1_2n.model import N_L, _state_tex, majorana_vertex_markdown
    e, p = ss.extra, ss.pieces
    U100, _D = diagonalize_takagi(e["Mn"], dps=100)
    Ll, nuR = p.fermions["Ll"], e["nuR"]
    chiL, chiR, chiLbar, chiRbar = e["chi"]
    rot = MajoranaRotation(U100, Ll.components[0], nuR.components[0], Ll.bar_components[0],
                           nuR.bar_components[0], chiL, chiR, chiLbar, chiRbar, n_L=N_L)
    table = extract_fermion_vertices(rot.apply(ss.physical_fermion_lagrangian(), (), 1), ss.boson_list)
    exact = {k: sp.nsimplify(v, rational=True) for k, v in ss.values().items() if isinstance(v, float)}
    printed = majorana_vertex_markdown(ss).splitlines()
    h = ss.bosons["h"]
    # all five magnitudes the 40-digit evaluation corrected (each printed for h and G0, both orderings)
    for a, b in ((2, 1), (1, 2), (0, 1), (0, 2), (0, 4)):
        (key,) = [k for k in table if k[0] == chiLbar[a] and k[2] == chiR[b]]
        want = abs(complex(sp.N(sp.sympify(table[key][1][(h,)]).subs(exact), 120)))
        label = rf"| $`\bar{{{_state_tex(a)}}} {_state_tex(b)} h`$ | $`P_R`$ | "
        rows = [l for l in printed if l.startswith(label)]
        assert rows == [label + f"{want:.3e} |"], (a, b, rows, want)


# ------------------------------------------------- feynlag 0.4.0 API (constructors, guided basis)

def _component_level_neutrino_terms(ss):
    """The Dirac Yukawa and Majorana mass typed component by component (the pre-0.4.0 body of
    ``build``), kept here as the reference the constructors must reproduce:
    ``−Σ_ab y_ν^{ab} L̄_a H̃ ν_R^b − ½ Σ_k M_k ν_R^{kT} C P_L ν_R^k + h.c.``, ``H̃ = (H⁰*, −G⁺*)``."""
    from feynlag import Bilinear, MajoranaBilinear, diracPL, diracPR
    from models.seesaw_type1_2n.model import N_L, N_R
    e, p = ss.extra, ss.pieces
    Gp, H0 = e["ew"].H.components
    Ll = p.fermions["Ll"]
    nuL, eL = Ll.components
    nuLbar, eLbar = Ll.bar_components
    nR, nRbar = e["nuR"].components[0], e["nuR"].bar_components[0]
    yv, CPL = e["yv"], e["CPL"]
    LYukD = sp.S.Zero
    for a in range(N_L):
        for b in range(N_R):
            y, yc = yv[a, b], sp.conjugate(yv[a, b])
            LYukD += -(y * sp.conjugate(H0) * Bilinear(nuLbar[a], diracPR, nR[b])
                       + y * (-sp.conjugate(Gp)) * Bilinear(eLbar[a], diracPR, nR[b]))
            LYukD += -(yc * H0 * Bilinear(nRbar[b], diracPL, nuL[a])
                       + yc * (-Gp) * Bilinear(nRbar[b], diracPL, eL[a]))
    LMaj = sp.S.Zero
    for k in range(N_R):
        op = -sp.Rational(1, 2) * e["MR"][k].s * MajoranaBilinear(nR[k], CPL, nR[k])
        LMaj += op + sp.conjugate(op)
    return LYukD, LMaj


def test_constructors_reproduce_component_neutrino_terms(ss):
    """``sm._flavour_matrix_term`` on the 3×2 ``y_ν`` with ``tilde(H)`` (off-diagonal entries on
    ``indices=(a, b)`` through a placeholder flavour matrix, diagonal entries included) and one
    ``majorana_mass`` per ``k`` give exactly the component-level terms, both halves included."""
    from feynlag import expand_bilinear
    LYukD, LMaj = _component_level_neutrino_terms(ss)
    X = lambda z: sp.expand(expand_bilinear(sp.expand(z)))   # noqa: E731
    assert X(ss.extra["LYukD"] - LYukD) == 0
    assert X(ss.extra["LMaj"] - LMaj) == 0


def test_mass_blocks_report_sm_blocks(ss):
    """``mass_blocks`` gives the SM Higgs and gauge blocks (what ``sm.ew_gauge_basis`` and
    ``sm.sm_higgs_states`` read); the fermion blocks are pinned in ``test_fermion_mass_blocks``."""
    m, b, p = ss.model, ss.bosons, ss.pieces
    scalar = m.mass_blocks(kind="scalar")
    assert [blk.fields for blk in scalar] == [[b["h"]], [b["G0"]], [b["Gp"]]]
    assert [bool(blk.goldstones) for blk in scalar] == [False, True, True]
    assert all(blk.diagonalizable for blk in scalar)
    assert [blk.fields for blk in m.mass_blocks(kind="gauge")] == [
        list(p.W.components[:2]), [p.W.components[2], p.B.components[0]]]


def test_physical_registry(ss):
    """Charges (derived from the vacuum), conjugate pairs and Goldstones from ``model.physical``."""
    b = ss.bosons
    assert ss.charges == {b["h"]: 0, b["G0"]: 0, b["Gp"]: 1, b["Gm"]: -1,
                          b["Z"]: 0, b["A"]: 0, b["Wp"]: 1, b["Wm"]: -1}
    assert ss.conjugates == {b["Gp"]: b["Gm"], b["Gm"]: b["Gp"], b["Wp"]: b["Wm"], b["Wm"]: b["Wp"]}
    assert ss.goldstones == (b["G0"], b["Gp"], b["Gm"])


def test_term_coverage(ss):
    """The potential is fully recognised (``V = −μ²H†H + λ(H†H)²``). The Yukawas sit at explicit
    integer flavour indices, which ``term_coverage`` documents as unmatched (``TermCoverage``
    docstring: "explicit integer flavour indices"), so the four Yukawa operators, ``L̄ H̃ ν_R``
    included, are reported missing. The bare ``ν_R`` Majorana mass is in feynlag's operator basis
    since 0.5.2 (FG-10, resolved), but the model writes it at integer flavour indices too
    (``majorana_mass(M_k, ν_R, indices=k)``), so it is listed missing for the same documented
    reason, not matched. The remainder is exactly the Yukawa and Majorana sector.

    ``term_coverage`` decomposes only the ``P_R`` / ``C P_L`` half of each fermion term (feynlag
    ``general.py``, ``_canonical_fermion_half``), so this test does not check the conjugated half
    or its phase; that half is covered by ``test_constructors_reproduce_component_neutrino_terms``
    (and, for the charged leptons and quarks, by ``sm_ckm``'s constructor test of the same helper)."""
    from feynlag import Bilinear, MajoranaBilinear, diracPR, expand_bilinear
    e = ss.extra
    CPL = e["CPL"]
    tc = ss.model.term_coverage()
    assert {t.label: c for t, c in tc.present} == {"(H†H)": -e["ew"].mu2.s,
                                                   "(H†H) (H†H)": e["ew"].lam.s}
    assert {t.label for t in tc.missing} == {"Ll̄·H eR", "Ll̄·H̃ nuR", "QL̄·H̃ uR", "QL̄·H dR",
                                             "½ nuRᵀCnuR [Majorana]"}
    assert set(tc.unmatched) == {"yukawa"}
    L_fer = sp.expand(expand_bilinear(sp.expand(sum(
        t.expr for t in ss.model.lagrangian.terms if t.sector in ("yukawa", "other")))))
    half = sum(term for term in sp.Add.make_args(L_fer)
               if all(x.gamma in (diracPR, CPL) for x in term.atoms(Bilinear, MajoranaBilinear)))
    assert half.has(MajoranaBilinear) and half.has(e["nuR"].nuR[1])
    assert sp.expand(expand_bilinear(sp.expand(tc.unmatched["yukawa"])) - half) == 0


def test_summary_and_parameters(ss):
    """``summary()``: ν_R is a right-handed gauge singlet with two flavours; every parameter is
    listed in order and ``check_parameters()`` finds no undeclared symbol."""
    s = ss.model.summary()
    rows = {r[0]: tuple(str(x) for x in r[1:5]) for r in s.field_rows}
    assert rows["nuR"] == ("fermion R", "1", "0", "1")
    assert rows["Ll"] == ("fermion L", "2", "-1/2", "1")
    assert set(rows) == {"H", "W", "B", "G", "Ll", "eR", "QL", "uR", "dR", "nuR"}
    assert [r[0] for r in s.param_rows] == [q.name for q in ss.params]
    assert ss.model.check_parameters().undeclared == []


def test_consumer_interface(ss):
    """feynlag-anomalies ``neutrino_mass`` substitutes trial Yukawas for ``yv_params[k].s`` into the
    symbolic ``Mnu`` and fixes ``v`` and ``M_k`` from the benchmark: those symbols must be exactly
    ``Mnu``'s, the Yukawas in a-major order, and the Takagi masses increasing."""
    e = ss.extra
    from models.seesaw_type1_2n.model import yukawa_name
    assert [q.name for q in e["yv_params"]] == [yukawa_name(a, b) for a in range(3) for b in range(2)]
    assert e["Mnu"].free_symbols == ({q.s for q in e["yv_params"]} | {q.s for q in e["MR"]}
                                     | {e["ew"].v.s})
    assert e["masses"] == sorted(e["masses"]) and len(e["masses"]) == 5


def test_fermion_mass_blocks(ss):
    """``mass_blocks(kind="fermion")`` reports the 3×2 (ν_L, ν_R) block, which the model reads as
    ``m_D``: not diagonalizable, with the Majorana note (the seesaw / Takagi route the model takes).
    The charged-lepton and per-colour quark blocks are flavoured, pointing to the numeric SVD.
    (FG-12, resolved in feynlag 0.5.2; up to 0.5.1 the unequal flavour counts raised
    ``NotImplementedError`` and took the whole fermion report with them.)"""
    m, p, e = ss.model, ss.pieces, ss.extra
    Ll, QL = p.fermions["Ll"], p.fermions["QL"]
    fermion = m.mass_blocks(kind="fermion")
    (nu,) = [blk for blk in fermion if blk.fields == [Ll.nuL]]
    assert nu.right == [e["nuR"].nuR] and nu.matrix.shape == (3, 2)
    # this block is what the model reads as e["mD"]; its entries are checked against y_ν v/√2 and the
    # square fermion_mass_matrix in test_mass_matrix_entries
    assert nu.diagonalizable is False
    assert all(s in nu.note for s in ("Majorana", "seesaw_mass_matrix", "diagonalize_takagi"))
    flavoured = [blk for blk in fermion if blk is not nu]
    assert {str(blk.fields[0]) for blk in flavoured} == {"eL", *(str(c) for c in QL.components)}
    for blk in flavoured:
        assert blk.nflavors == 3 and blk.diagonalizable is False
        assert "diagonalize_svd(method='numeric')" in blk.note
    assert len(m.mass_blocks()) == len(fermion) + 5        # a bare call no longer raises
