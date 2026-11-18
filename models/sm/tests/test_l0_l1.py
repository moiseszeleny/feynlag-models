"""L0 (declared, invariant, anomaly-free) and L1 (tadpoles, spectrum, Goldstones)."""

import sympy as sp

from feynlag import diracPR, fermion_mass_matrix
from feynlag_models.checks import (assert_dual_equal, massive_gauge_boson_count,
                                   zero_eigenvalue_count)


def test_validate_invariance_and_anomalies(sm):
    report = sm.model.validate()
    assert report.ok, report.summary()
    assert report.checks["anomalies"] is not None        # quarks present → really checked
    assert report.checks["anomalies"].ok


def test_tadpole_and_higgs_mass(sm):
    ew = sm.extra["ew"]
    lam, v = ew.lam.s, ew.v.s
    assert_dual_equal(ew.mu2.expr, lam * v**2, msg="mu2")
    M = sm.model.mass_matrix([sm.bosons["h"]])
    assert_dual_equal(M[0, 0], 2 * lam * v**2, msg="m_h^2")


def test_gauge_masses(sm):
    p = sm.pieces
    W1, W2, W3 = p.W.components
    B = p.B.components[0]
    M = sm.model.gauge_mass_matrix([W1, W2, W3, B])
    g, gp, v = p.gw.s, p.g1.s, p.ew.v.s
    assert_dual_equal(M[0, 0], g**2 * v**2 / 4, msg="m_W^2")
    assert_dual_equal(M[1, 1], g**2 * v**2 / 4, msg="m_W^2")
    assert sp.simplify(M.det()) == 0                       # massless photon
    # Z, photon from the (W3, B) block eigenvalues
    block = M.extract([2, 3], [2, 3])
    eig = list(block.eigenvals().keys())
    assert any(sp.simplify(e) == 0 for e in eig)
    assert any(sp.simplify(e - (g**2 + gp**2) * v**2 / 4) == 0 for e in eig)


def test_goldstone_count(sm):
    """#massless would-be Goldstones == #massive gauge bosons (= 3)."""
    p, vals = sm.pieces, sm.values()
    W1, W2, W3 = p.W.components
    Mg = sm.model.gauge_mass_matrix([W1, W2, W3, p.B.components[0]])
    n_massive = massive_gauge_boson_count(Mg, vals)
    M_odd = sm.model.mass_matrix([sm.bosons["G0"]])
    M_ch = sm.model.mass_matrix([sm.bosons["Gp"]], charged=True)
    n_goldstone = (zero_eigenvalue_count(M_odd, vals)
                   + 2 * zero_eigenvalue_count(M_ch, vals))
    assert n_massive == 3
    assert n_goldstone == n_massive
    assert sp.simplify(M_odd[0, 0]) == 0 and sp.simplify(M_ch[0, 0]) == 0


def test_fermion_masses(sm):
    p = sm.pieces
    i, j = p.idx
    Ll, eR, QL, uR, dR = (p.fermions[k] for k in ("Ll", "eR", "QL", "uR", "dR"))
    vac = sm.model.vacuum
    v = p.ew.v.s
    cases = {
        "tau": (p.yukawa["yukawa_tau"], Ll.bar_components[1], eR.components[0], p.masses["MTA"]),
        "t": (p.yukawa["yukawa_t"], QL.bar_components[0], uR.components[0], p.masses["MT"]),
        "b": (p.yukawa["yukawa_b"], QL.bar_components[3], dR.components[0], p.masses["MB"]),
    }
    for name, (L, bar, fld, M) in cases.items():
        m = fermion_mass_matrix(L, bar, fld, vac, 1, (i, j), gamma=diracPR)[0, 0]
        y = sm.params[f"y{'tau' if name == 'tau' else name}"].expr
        assert_dual_equal(m.subs(sm.params.resolve()), M.s, msg=f"m_{name}")
        assert_dual_equal(y, sp.sqrt(2) * M.s / v, msg=f"y_{name}")


# ------------------------------------------------- feynlag 0.4.0 API (constructors, guided basis)

def _component_level_yukawas(p):
    """The SM Yukawas typed component by component (the pre-0.4.0 body of
    ``sm.yukawa_terms``), kept here as the reference the constructors must reproduce:
    ``−y_τ L̄ H e_R − y_b Q̄ H d_R − y_t Q̄ H̃ u_R + h.c.``, ``H̃ = (H⁰*, −G⁺*)``."""
    from feynlag import Bilinear, diracPL
    Ll, eR, QL, uR, dR = (p.fermions[k] for k in ("Ll", "eR", "QL", "uR", "dR"))
    Gp, H0 = p.ew.H.components
    i = p.idx[0]
    ys = {k: q.s for k, q in p.yukawa_params.items()}
    ytau, yb, yt = ys["ytau"], ys["yb"], ys["yt"]

    def colour(bars, gamma, fields):
        return sum(Bilinear(bars[c][i], gamma, fields[c][i]) for c in range(3))

    qu, qd = QL.components[:3], QL.components[3:]
    qub, qdb = QL.bar_components[:3], QL.bar_components[3:]
    L_e = -(ytau * Gp * Bilinear(Ll.nuLbar[i], diracPR, eR.eR[i])
            + ytau * H0 * Bilinear(Ll.eLbar[i], diracPR, eR.eR[i])
            + ytau * sp.conjugate(Gp) * Bilinear(eR.eRbar[i], diracPL, Ll.nuL[i])
            + ytau * sp.conjugate(H0) * Bilinear(eR.eRbar[i], diracPL, Ll.eL[i]))
    L_d = -(yb * Gp * colour(qub, diracPR, dR.components)
            + yb * H0 * colour(qdb, diracPR, dR.components)
            + yb * sp.conjugate(Gp) * colour(dR.bar_components, diracPL, qu)
            + yb * sp.conjugate(H0) * colour(dR.bar_components, diracPL, qd))
    L_u = -(yt * sp.conjugate(H0) * colour(qub, diracPR, uR.components)
            - yt * sp.conjugate(Gp) * colour(qdb, diracPR, uR.components)
            + yt * H0 * colour(uR.bar_components, diracPL, qu)
            - yt * Gp * colour(uR.bar_components, diracPL, qd))
    return {"yukawa_tau": L_e, "yukawa_b": L_d, "yukawa_t": L_u}


def test_constructors_reproduce_component_yukawas(sm):
    """``feynlag.terms.yukawa`` (with ``tilde(H)`` for the up quarks) gives exactly the
    component-level Yukawa sector, term by term."""
    ref = _component_level_yukawas(sm.pieces)
    assert set(ref) == set(sm.pieces.yukawa)
    for name, expr in ref.items():
        assert sp.expand(sm.pieces.yukawa[name] - expr) == 0, name


def test_gauge_rotations_conventions(sm):
    """``mass_blocks``/``diagonalize`` register the CONVENTIONS.md rotations:
    ``(Z, A) = R(−θ_W)(W³, B)`` with ``tan θ_W = g'/g``, and ``W± = (W¹ ∓ iW²)/√2``."""
    from feynlag import rotation_2x2
    p, b = sm.pieces, sm.bosons
    W1, W2, W3 = p.W.components
    B = p.B.components[0]
    rots = {tuple(r.old_fields): r for r in sm.model.rotations}
    assert set(rots) == {(W3, B), (W1, W2)}
    neutral, charged = rots[(W3, B)], rots[(W1, W2)]
    assert list(neutral.new_fields) == [b["Z"], b["A"]]
    assert list(charged.new_fields) == [b["Wp"], b["Wm"]]
    thW = sp.atan(p.g1.s / p.gw.s)
    for M, ref, what in ((neutral.matrix, rotation_2x2(-thW), "Weinberg"),
                         (charged.matrix, sp.Matrix([[1, -sp.I], [1, sp.I]]) / sp.sqrt(2), "W+-")):
        for k in range(4):
            assert_dual_equal(sp.Matrix(M)[k], ref[k], msg=f"{what}[{k}]")


def test_physical_registry(sm):
    """The charges, conjugate pairs and Goldstones the bundle reads from ``model.physical``
    are the SM ones (charges derived from the vacuum, not declared), and the scalar
    ``mass_blocks`` find exactly ``G0`` and ``G+`` as Goldstone directions."""
    b = sm.bosons
    assert sm.charges == {b["h"]: 0, b["G0"]: 0, b["Gp"]: 1, b["Gm"]: -1,
                          b["Z"]: 0, b["A"]: 0, b["Wp"]: 1, b["Wm"]: -1}
    assert sm.conjugates == {b["Gp"]: b["Gm"], b["Gm"]: b["Gp"],
                             b["Wp"]: b["Wm"], b["Wm"]: b["Wp"]}
    assert sm.goldstones == (b["G0"], b["Gp"], b["Gm"])
    blocks = sm.model.mass_blocks(kind="scalar")
    assert {blk.fields[0] for blk in blocks if blk.goldstones} == {b["G0"], b["Gp"]}
    assert [blk.fields for blk in blocks if not blk.goldstones] == [[b["h"]]]


def test_term_coverage(sm):
    """Every potential and Yukawa invariant the SM symmetries allow is present, with
    nothing left over. Coefficients in feynlag's convention (``V = Σ c O``,
    ``L_Yuk = −Σ c O``) are CONVENTIONS.md's ``V = −μ²H†H + λ(H†H)²`` and ``y_f``."""
    tc = sm.model.term_coverage()
    assert tc.complete and not tc.missing
    assert tc.unmatched == {}
    ew, ys = sm.extra["ew"], sm.pieces.yukawa_params
    got = {term.label: c for term, c in tc.present}
    assert got == {"(H†H)": -ew.mu2.s, "(H†H) (H†H)": ew.lam.s,
                   "Ll̄·H eR": ys["ytau"].s, "QL̄·H dR": ys["yb"].s,
                   "QL̄·H̃ uR": ys["yt"].s}
    assert sm.model.missing_terms() == []


def test_summary_and_parameters(sm):
    """``summary()`` lists every field with its representations, and every Lagrangian or
    VEV symbol is a declared parameter or a field (``check_parameters``)."""
    s = sm.model.summary()
    assert s.field_header[:5] == ["field", "type", "SU2L", "U1Y", "SU3c"]
    reps = {row[0]: tuple(str(x) for x in row[1:5]) for row in s.field_rows}
    assert reps == {
        "H": ("scalar", "2", "1/2", "1"), "W": ("vector", "adj", "0", "1"),
        "B": ("vector", "1", "0", "1"), "G": ("vector", "1", "0", "adj"),
        "Ll": ("fermion L", "2", "-1/2", "1"), "eR": ("fermion R", "1", "-1", "1"),
        "QL": ("fermion L", "2", "1/6", "3"), "uR": ("fermion R", "1", "2/3", "3"),
        "dR": ("fermion R", "1", "-1/3", "3"),
    }
    assert "⟨H0⟩ = v/√2" in str(s)
    assert {row[0] for row in s.param_rows} == {q.name for q in sm.params}
    report = sm.model.check_parameters()
    assert report.undeclared == []
