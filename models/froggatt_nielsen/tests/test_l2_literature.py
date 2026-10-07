"""L2: the Froggatt-Nielsen texture, determinant, mass and mixing scaling against Leurer, Nir and
Seiberg (LNS-1: hep-ph/9212278v1; LNS-2: hep-ph/9310320v1), and the flavon couplings.

Map (metadata ``conventions_map``): their horizontal charges H(Q), H(f̄) are our q(Q_L), −q(f_R);
their λ is our ε; their S (charge −1) is our φ^*. Their "~" is an order-of-magnitude statement,
so the scaling tests check that X/ε^p tends to a finite, non-zero limit as ε → 0 at random O(1)
coefficients, the precise meaning of X ~ ε^p.
"""

import mpmath as mp
import numpy as np
import sympy as sp

from feynlag_models.checks import assert_dual_equal
from feynlag_models.flavor import ckm_from_yukawas, mp_biunitary, mp_matrix

# LNS-2 Eq. (2.5): the "master model" charges (H(Q), H(d̄), H(ū)) for generations 1, 2, 3
LNS2_H_Q, LNS2_H_DBAR, LNS2_H_UBAR = (3, 2, 0), (3, 2, 2), (3, 1, 0)
# LNS-2 Eq. (2.6): powers of λ in M^d / <φ_d> and M^u / <φ_u>
LNS2_POWERS_D = [[6, 5, 5], [5, 4, 4], [3, 2, 2]]
LNS2_POWERS_U = [[6, 4, 3], [5, 3, 2], [3, 1, 0]]
# LNS-2 Eq. (2.7): det M^d ~ <φ_d>^3 λ^12, det M^u ~ <φ_u>^3 λ^9
LNS2_DET_POWER = {"down": 12, "up": 9}

DPS = 60
N_DRAWS = 20


def test_benchmark_charges_are_lns_master_model(fn):
    """The benchmark charges are LNS-2 Eq. (2.5) under q(Q) = H(Q), q(f_R) = −H(f̄)."""
    q = fn.extra["fn_charges"]
    assert q["QL"] == LNS2_H_Q
    assert q["dR"] == tuple(-h for h in LNS2_H_DBAR)
    assert q["uR"] == tuple(-h for h in LNS2_H_UBAR)


def test_yukawa_texture_lns_eq_2_6(fn):
    """Y^f_ij = c_ij ε^{n_ij}, n_ij = H(Q_i) + H(f̄_j) ≥ 0 (LNS-2 Eq. 2.2), reproduces the
    textures of LNS-2 Eq. (2.6) power by power, and Y is exactly that monomial times c_ij."""
    e = fn.extra
    eps = e["eps"].s
    for sector, expected in (("down", LNS2_POWERS_D), ("up", LNS2_POWERS_U)):
        assert e["powers"][sector].tolist() == expected
        for i in range(3):
            for j in range(3):
                assert_dual_equal(e["Y"][sector][i, j], e["C"][sector][i, j] * eps ** expected[i][j],
                                  msg=f"{sector}[{i},{j}]")


def test_determinant_is_charge_sum_lns_eq_2_19(fn):
    """det Y^f = det(c^f) ε^{Σ_i (H(Q_i) + H(f̄_i))} exactly (LNS-2 Eq. 2.19, n_ij additive and
    non-negative), giving ε^12 (down) and ε^9 (up) as in LNS-2 Eq. (2.7). The numeric SVD
    (FG-6 workaround) agrees: the product of the singular values of Y is |det Y| at the benchmark,
    so m_1 m_2 m_3 = |det Y| (v/√2)^3."""
    e, vals = fn.extra, fn.values()
    eps, q = e["eps"].s, e["fn_charges"]
    for sector, right in (("down", "dR"), ("up", "uR")):
        power = sum(q["QL"][i] - q[right][i] for i in range(3))
        assert power == LNS2_DET_POWER[sector]
        assert_dual_equal(e["Y"][sector].det(), e["C"][sector].det() * eps**power, msg=sector)
        m = mp_biunitary(e["Y"][sector], vals, DPS)[1]
        with mp.workdps(DPS):
            detY = abs(mp.det(mp_matrix(e["Y"][sector], vals, DPS)))
            assert abs(m[0] * m[1] * m[2] / detY - 1) < mp.mpf(10) ** (-40)


def _draw(rng):
    """Random O(1) c_ij: |c| uniform in [0.5, 2], phase uniform, as the benchmark draw."""
    return rng.uniform(0.5, 2.0, (3, 3)) * np.exp(1j * rng.uniform(0, 2 * np.pi, (3, 3)))


def _point(fn, cu, cd, eps):
    e = fn.extra
    vals = {e["eps"].s: sp.Float(eps, DPS)}
    for sector, c in (("up", cu), ("down", cd)):
        for k, (pa, pg) in enumerate(zip(e["c_abs"][sector], e["c_arg"][sector])):
            vals[pa.s] = sp.Float(abs(c.flat[k]), DPS)
            vals[pg.s] = sp.Float(float(np.angle(c.flat[k])), DPS)
    return vals


def _limits(fn, observable, eps_values=(1e-3, 1e-4)):
    """``observable(vals)`` divided by its predicted power, at two small ε, for N_DRAWS draws."""
    rng = np.random.default_rng(20261005)
    out = []
    for _ in range(N_DRAWS):
        cu, cd = _draw(rng), _draw(rng)
        out.append([observable(_point(fn, cu, cd, eps), eps) for eps in eps_values])
    return out


def _assert_finite_limit(ratios, label):
    """r(ε) = X/ε^p: converged between ε = 1e-3 and 1e-4 (5%) and an O(1) number (1e-2 … 1e2)."""
    for k, (r3, r4) in enumerate(ratios):
        assert abs(r4 / r3 - 1) < 0.05, f"{label} draw {k}: X/eps^p = {r3:.4g}, {r4:.4g}"
        assert 1e-2 < r4 < 1e2, f"{label} draw {k}: limit {r4:.4g} is not O(1)"


def test_mass_scaling_lns_eq_2_4(fn):
    """m_{f_i}/(v/√2) ~ ε^{H(Q_i) + H(f̄_i)}, i.e. m_i/m_j ~ λ^{H(Q_i)−H(Q_j)+H(f̄_i)−H(f̄_j)}
    (LNS-2 Eq. 2.4): at random O(1) c_ij each singular value of Y^f over ε^{n_ii} tends to a
    finite O(1) limit."""
    e = fn.extra
    for sector in ("up", "down"):
        n = e["powers"][sector]

        def masses(vals, eps, sector=sector, n=n):
            m = mp_biunitary(e["Y"][sector], vals, DPS)[1]
            return [float(m[i]) / eps ** n[i, i] for i in range(3)]

        draws = _limits(fn, masses)
        for i in range(3):
            _assert_finite_limit([(d[0][i], d[1][i]) for d in draws], f"{sector} m_{i + 1}")


def test_ckm_scaling_lns_eq_2_3(fn):
    """|V_ij| ~ λ^{|H(Q_i) − H(Q_j)|} (LNS-2 Eq. 2.3; LNS-1 Eq. 5.7): |V_us| ~ ε, |V_cb| ~ ε²,
    |V_ub| ~ ε³ for H(Q) = (3, 2, 0), each tending to a finite O(1) limit over ε^p; and
    |V_ub| ~ |V_us V_cb| (LNS-1 Eq. 5.8)."""
    e = fn.extra
    q = e["fn_charges"]["QL"]
    pairs = [(0, 1), (1, 2), (0, 2)]

    def mixing(vals, eps):
        V = ckm_from_yukawas(e["Y"]["up"], e["Y"]["down"], vals, DPS)
        return [abs(V[i, j]) / eps ** abs(q[i] - q[j]) for i, j in pairs]

    draws = _limits(fn, mixing)
    for k, (i, j) in enumerate(pairs):
        _assert_finite_limit([(d[0][k], d[1][k]) for d in draws], f"|V_{i + 1}{j + 1}|")
    # V_ub / (V_us V_cb) is O(1) too: the three powers add up
    assert [abs(q[0] - q[2])] == [abs(q[0] - q[1]) + abs(q[1] - q[2])]
    for d in draws:
        assert 1e-2 < d[1][2] / (d[1][0] * d[1][1]) < 1e2


def test_unitarity_and_benchmark_spectrum(fn):
    """At the benchmark (ε = 0.2, LNS-2's λ ~ 0.2): V is unitary and the masses are ordered
    m_1 < m_2 < m_3 in each sector (singular values of c ε^n, numeric SVD)."""
    e, vals = fn.extra, fn.values()
    V = ckm_from_yukawas(e["Yu"], e["Yd"], vals, DPS)
    assert np.allclose(V.conj().T @ V, np.eye(3), atol=1e-12)
    for sector in ("up", "down", "lepton"):
        m = mp_biunitary(e["Y"][sector], vals, DPS)[1]
        assert 0 < m[0] < m[1] < m[2]


def _assert_flavon_couplings(fn):
    """Down-sector one-flavon couplings of ``fn`` against
    −M_ij (h/v + (|n_ij| s + i n_ij a)/v_φ), entry by entry."""
    from feynlag import diracPR
    e, b = fn.extra, fn.bosons
    table = fn.fermion_table()
    p = fn.pieces
    QL, dR = p.fermions["QL"], p.fermions["dR"]
    v, vphi = e["ew"].v.s, e["vphi"].s
    th = e["theta"].s
    resolve = {e["eps"].s: e["eps"].expr}
    M = (v / sp.sqrt(2) * e["Y"]["down"]).subs(resolve)
    n = e["powers"]["down"]
    for i in range(3):
        for j in range(3):
            key = (QL.bar_components[3][i], diracPR, dR.components[0][j])
            got = table[key][1]
            ns, na = abs(n[i, j]), n[i, j]            # s and a weights: |n| s + i n a
            expected = {
                b["h1"]: -M[i, j] * (sp.cos(th) / v + ns * sp.sin(th) / vphi),
                b["h2"]: -M[i, j] * (-sp.sin(th) / v + ns * sp.cos(th) / vphi),
                b["a"]: -sp.I * M[i, j] * na / vphi,
            }
            for boson, coeff in expected.items():
                assert_dual_equal(got.get((boson,), 0), coeff, msg=f"{boson} d[{i},{j}] (n={n[i, j]})")


def test_flavon_couplings(fn):
    """One-flavon couplings from the linearised operators, weak basis (physics judgment; LNS do
    not state them):  L ⊃ −M_ij (h/v + (|n_ij| s + i n_ij a)/v_φ) d̄_{L,i} d_{R,j} + h.c.,
    M = v Y/√2, with h = c_θ h_1 − s_θ h_2, s = s_θ h_1 + c_θ h_2 (CONVENTIONS.md R(θ)).
    φ^n (n ≥ 0) gives n(s + i a); (φ^*)^{|n|} (n < 0) gives |n|(s − i a) = |n| s + i n a.
    At the benchmark every n_ij ≥ 0; ``test_flavon_couplings_negative_powers`` covers n < 0."""
    _assert_flavon_couplings(fn)


def test_flavon_couplings_negative_powers():
    """Same couplings at a charge set with negative powers: qd1 = +4 gives n^d_i1 = (−1, −2, −4),
    so those entries come from (φ^*)^{|n|} and their s coupling has the sign of |n|, not n."""
    from models.froggatt_nielsen.model import benchmark_point, build
    bench = dict(benchmark_point(), qd1=4)
    fn_neg = build(bench)
    n = fn_neg.extra["powers"]["down"]
    assert [n[i, 0] for i in range(3)] == [-1, -2, -4]
    assert all(n[i, j] >= 0 for i in range(3) for j in (1, 2))
    _assert_flavon_couplings(fn_neg)
