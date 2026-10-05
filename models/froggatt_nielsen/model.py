"""SM + Froggatt-Nielsen flavon: a global U(1)_FN with per-generation fermion charges.

Parent + delta on ``models/sm_ckm`` (three generations), replacing its Yukawa sector. A complex
gauge-singlet flavon φ with FN charge +1 gets a vev, ``φ = (v_φ + s + i a)/√2``, and every Yukawa
is a higher-dimension operator (CONVENTIONS.md, Froggatt-Nielsen):

    −L ⊃ c^u_ij (φ/Λ)^{n^u_ij} Q̄_i H̃ u_j + c^d_ij (φ/Λ)^{n^d_ij} Q̄_i H d_j
         + c^e_ij (φ/Λ)^{n^e_ij} L̄_i H e_j + h.c.,      n^f_ij = q(F_L,i) − q(f_R,j)

with ``φ^*`` in place of φ when ``n < 0``. After symmetry breaking ``Y^f_ij = c^f_ij ε^{n_ij}``,
``ε = v_φ/(√2 Λ)``. The charges are integer benchmark inputs (``qQ1`` … ``qe3``), so a different
assignment is a different benchmark of this model; H is uncharged.

Two feynlag ``Model``s are built from the same declarations:

* ``extra["model_exact"]`` carries the exact operators (dimension up to 4 + max n). L0
  (invariance, hermiticity, anomalies, mass dimension) and the fermion mass matrices use it.
* ``bundle.model`` replaces every ``φ^n`` by its expansion to **linear order** in the flavon
  fluctuation, ``φ^n → w^{n−1}(n φ − (n−1) w)`` with ``w = v_φ/√2``. That expansion is exact at
  the vacuum and in the one-flavon couplings, and it drops vertices with two or more flavons
  attached to a fermion pair. Spectrum, rotations and vertices use this model: extracting the
  exact operators gives up to 9-boson vertices and is ~10× slower (probe, 2026-10-05).

U(1)_FN is exact in the Lagrangian, so the flavon phase ``a`` is a massless Goldstone. feynlag
has no global U(1) (FEYNLAG_GAPS.md FG-7); invariance is checked in the tests by counting charges
per monomial. The 3×3 Yukawas are generic complex matrices, so masses and V_CKM come from a
numeric biunitary SVD outside feynlag (``feynlag_models.flavor``, FG-6 workaround).
"""

import sympy as sp

from feynlag import (
    Model, ParameterSet, PartialMu, Scalar, dag, diagonalize_orthogonal_2x2,
    to_physical_basis, tex_symbol,
)
from feynlag.export.ufo import UFOParticle

from feynlag_models import MODELS_DIR
from feynlag_models import metadata as md
from feynlag_models.bundle import ModelBundle
from feynlag_models.outputs import standard_outputs
from feynlag_models.tex import TEX, external, internal
from models.sm import model as sm

ID = "froggatt_nielsen"
PARENT = "sm_ckm"

#: benchmark prefix of each multiplet's FN charges (one integer per generation)
CHARGE_KEYS = {"QL": "qQ", "uR": "qu", "dR": "qd", "Ll": "qL", "eR": "qe"}
#: sector → (left multiplet, right multiplet, coefficient prefix)
SECTORS = {"up": ("QL", "uR", "cu"), "down": ("QL", "dR", "cd"), "lepton": ("Ll", "eR", "ce")}


def benchmark_point():
    return md.benchmark_inputs(MODELS_DIR / ID)


def fn_charges(bench):
    """``{multiplet: (q_1, q_2, q_3)}`` from the benchmark; the charges must be integers."""
    out = {}
    for field, key in CHARGE_KEYS.items():
        qs = []
        for k in (1, 2, 3):
            q = bench[f"{key}{k}"]
            if q != int(q):
                raise ValueError(f"FN charge {key}{k} = {q} is not an integer")
            qs.append(int(q))
        out[field] = tuple(qs)
    return out


def fn_powers(charges):
    """``{sector: n}`` with ``n_ij = q(F_L,i) − q(f_R,j)``, the power of φ (φ^* if negative)."""
    return {sector: sp.Matrix(3, 3, lambda i, j: charges[left][i] - charges[right][j])
            for sector, (left, right, _) in SECTORS.items()}


def flavon_power(phi, n):
    """``φ^n`` for ``n ≥ 0``, ``(φ^*)^{|n|}`` for ``n < 0`` (φ has FN charge +1)."""
    return phi**n if n >= 0 else sp.conjugate(phi) ** (-n)


def linear_flavon_power(phi, n, w):
    """``φ^n`` to linear order around ``⟨φ⟩ = w``: ``w^{n−1}(n φ − (n−1) w)`` (``φ^*`` if n < 0)."""
    x, m = (phi, n) if n >= 0 else (sp.conjugate(phi), -n)
    return w ** (m - 1) * (m * x - (m - 1) * w)


def coefficient_params(bench, prefix):
    """The 3×3 complex ``c_ij = |c| exp(i α)``: (matrix, [abs params], [arg params])."""
    absp = [[external(f"{prefix}{i + 1}{j + 1}_abs", bench[f"{prefix}{i + 1}{j + 1}_abs"])
             for j in range(3)] for i in range(3)]
    argp = [[external(f"{prefix}{i + 1}{j + 1}_arg", bench[f"{prefix}{i + 1}{j + 1}_arg"])
             for j in range(3)] for i in range(3)]
    C = sp.Matrix(3, 3, lambda i, j: absp[i][j].s * sp.exp(sp.I * argp[i][j].s))
    return C, [q for row in absp for q in row], [q for row in argp for q in row]


def build(benchmark=None):
    bench = benchmark_point() if benchmark is None else dict(benchmark)
    # sm.pieces declares the mass inputs MU…MTA and the diagonal Yukawas they fix; here the masses
    # are outputs, so pieces gets dummy values and those parameters are dropped below
    dropped = [n for row in sm.MASS_NAMES[3] for n in row]
    p = sm.pieces({**bench, **{n: 1.0 for n in dropped}}, higgs=True, generations=3)
    dropped += [n for row in sm.YUKAWA_NAMES[3] for n in row]
    p.params = [q for q in p.params if q.name not in dropped]
    p.masses, p.yukawa_params = {}, {}
    ew = p.ew

    # --- delta: the flavon -------------------------------------------------------
    vphi = external("vphi", bench["vphi"], positive=True, unit_dim=1)
    Lam = external("Lam", bench["Lam"], positive=True, unit_dim=1)
    lamPhi = external("lamPhi", bench["lamPhi"])
    lamHPhi = external("lamHPhi", bench["lamHPhi"])
    muPhi2 = internal("muPhi2", unit_dim=2)
    eps = internal("eps", vphi.s / (sp.sqrt(2) * Lam.s), positive=True)
    phiF = Scalar("phi", reps={}, component_names=["phi"], tex=r"\phi")
    phi = phiF.components[0]
    phiF.expand_vev({phi: vphi}, tex=TEX)
    _vev, s0, a0 = phiF.vev_expansions[phi]

    absphi2 = phi * sp.conjugate(phi)
    HdH = (dag(ew.H) * ew.H.mat)[0]
    V_phi = -muPhi2.s * absphi2 + lamPhi.s * absphi2**2 + lamHPhi.s * HdH * absphi2
    p.add_term(-V_phi, "potential", "flavon_potential")
    p.add_term(PartialMu(sp.conjugate(phi)) * PartialMu(phi), "kinetic", "flavon_kinetic")
    p.fields.append(phiF)

    # --- delta: FN Yukawas (exact operators) ----------------------------------------
    charges = fn_charges(bench)
    powers = fn_powers(charges)
    C, c_abs, c_arg, Y, Y_exact, Y_linear = {}, {}, {}, {}, {}, {}
    w = vphi.s / sp.sqrt(2)
    for sector, (_l, _r, prefix) in SECTORS.items():
        C[sector], c_abs[sector], c_arg[sector] = coefficient_params(bench, prefix)
        n = powers[sector]
        Y[sector] = sp.Matrix(3, 3, lambda i, j: C[sector][i, j] * eps.s ** abs(n[i, j]))
        Y_exact[sector] = sp.Matrix(3, 3, lambda i, j:
                                    C[sector][i, j] * flavon_power(phi / Lam.s, n[i, j]))
        Y_linear[sector] = sp.Matrix(3, 3, lambda i, j: C[sector][i, j]
                                     * linear_flavon_power(phi, n[i, j], w) / Lam.s ** abs(n[i, j]))
    L_exact = sm.yukawa_terms(p, ew.H, ew.H, Y_exact["lepton"], Y_exact["down"], Y_exact["up"])
    L_linear = sm.yukawa_terms(p, ew.H, ew.H, Y_linear["lepton"], Y_linear["down"], Y_linear["up"])
    for name, expr in L_exact.items():
        p.replace_term(name, expr)
    c_params = [q for sector in SECTORS for q in (*c_abs[sector], *c_arg[sector])]
    p.params += [vphi, Lam, lamPhi, lamHPhi, muPhi2, eps, *c_params]

    model_exact = Model(f"{ID}_exact", gauge_groups=p.gauge_groups, fields=p.fields,
                        parameters=p.params, lagrangian=p.lagrangian())

    # --- the linearised model: spectrum, rotations, vertices --------------------------
    for name, expr in L_linear.items():
        p.replace_term(name, expr)
    p.yukawa = dict(L_linear)
    model = Model(ID, gauge_groups=p.gauge_groups, fields=p.fields,
                  parameters=p.params, lagrangian=p.lagrangian())
    model.solve_tadpoles([ew.mu2, muPhi2])
    phys = to_physical_basis(model, ew, tex=TEX)

    # --- CP-even mixing (h, s) → (h1, h2), as in sm_singlet_z2 ----------------------
    M_even = model.mass_matrix([phys.h, s0])
    h1, h2 = (tex_symbol(name, TEX[name], real=True) for name in ("h1", "h2"))
    theta = internal("theta")
    rot = diagonalize_orthogonal_2x2(M_even, [phys.h, s0], [h1, h2], angle=theta.s)
    theta.define(rot.angle_solution)
    model.rotate(rot)
    m1sq, m2sq = rot.masses_squared(M_even, simplifier=sp.expand)

    bosons = dict(h1=h1, h2=h2, a=a0, G0=phys.G0, Gp=phys.Gp, Gm=phys.Gm,
                  Z=phys.Z, A=phys.A, Wp=phys.Wp, Wm=phys.Wm)
    bcharges = {h1: 0, h2: 0, a0: 0, phys.G0: 0, phys.Gp: 1, phys.Gm: -1,
                phys.Z: 0, phys.A: 0, phys.Wp: 1, phys.Wm: -1}
    conjugates = {phys.Gp: phys.Gm, phys.Gm: phys.Gp, phys.Wp: phys.Wm, phys.Wm: phys.Wp}

    g, gp, v = ew.gw.s, ew.g1.s, ew.v.s
    MW = internal("MW", g * v / 2, positive=True, unit_dim=1)
    MZ = internal("MZ", sp.sqrt(g**2 + gp**2) * v / 2, positive=True, unit_dim=1)
    MH1 = internal("MH1", sp.sqrt(m1sq), positive=True, unit_dim=1)
    MH2 = internal("MH2", sp.sqrt(m2sq), positive=True, unit_dim=1)
    params = ParameterSet(*p.params, *sm.width_params(bench), MW, MZ, theta, MH1, MH2)

    boson_particles = sm.ew_boson_particles(dict(bosons, h=h1), h_mass="MH1") + [
        UFOParticle(h2, 35, "h2", spin=1, mass="MH2", width="ZERO"),
        UFOParticle(a0, 9000005, "a0", spin=1, mass="ZERO", width="ZERO")]

    return ModelBundle(
        id=ID, model=model, pieces=p, bosons=bosons, cmap=phys.cmap,
        charges=bcharges, conjugates=conjugates, params=params, benchmark=bench,
        dirac=sm.dirac_specs(p), boson_particles=boson_particles,
        goldstones=(phys.G0, phys.Gp, phys.Gm),
        extra=dict(ew=ew, phi=phi, phiF=phiF, s0=s0, a0=a0, vphi=vphi, Lam=Lam, lamPhi=lamPhi,
                   lamHPhi=lamHPhi, muPhi2=muPhi2, eps=eps, fn_charges=charges, powers=powers,
                   C=C, c_abs=c_abs, c_arg=c_arg, c_params=c_params,
                   Y=Y, Yu=Y["up"], Yd=Y["down"], Ye=Y["lepton"],
                   Y_exact=Y_exact, Y_linear=Y_linear, L_exact=L_exact, L_linear=L_linear,
                   model_exact=model_exact, M_even=M_even, rot=rot, theta=theta,
                   MW=MW, MZ=MZ, MH1=MH1, MH2=MH2, h_weak=phys.h, ufo=False),
    )


def outputs(bundle, out_dir):
    e = bundle.extra
    masses = {"$m_{h_1}$": e["MH1"].expr, "$m_{h_2}$": e["MH2"].expr, r"$\theta$": e["theta"].expr,
              "$m_a$": sp.S.Zero, "$m_W$": e["MW"].expr, "$m_Z$": e["MZ"].expr,
              r"$\epsilon$": e["eps"].expr}
    return standard_outputs(bundle, out_dir, "FROGGATT_NIELSEN_UFO", masses, ufo=False)
