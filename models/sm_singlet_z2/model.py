"""SM + real singlet scalar S with a Z2 symmetry, spontaneously broken by <S> = v_S.

Parent + delta on ``models/sm``: one real gauge-singlet scalar, a Z2 under
which only S is odd, and the potential terms

    V ⊃ ½ μ_S² S² + ¼ λ_S S⁴ + ½ λ_HS (H†H) S²        (CONVENTIONS.md)

After EWSB the CP-even states (h, s) mix through the portal λ_HS with
``tan 2θ = 2 M12/(M11 − M22)``; every coupling of h1 (h2) to SM particles is
the SM one times cos θ (sin θ).
"""

import sympy as sp

from feynlag import Model, Scalar, ZN, conjugate_pair, inner, kinetic
from feynlag.export.ufo import UFOParticle

from feynlag_models import MODELS_DIR
from feynlag_models import metadata as md
from feynlag_models.bundle import ModelBundle
from feynlag_models.outputs import standard_outputs
from feynlag_models.tex import TEX
from models.sm import model as sm

ID = "sm_singlet_z2"
PARENT = "sm"


def benchmark_point():
    return md.benchmark_inputs(MODELS_DIR / ID)


def scalar_blocks(model):
    """``(even, G0, Gp)`` from ``model.mass_blocks(kind="scalar")``: the CP-even ``(H0_r, S)``
    block that the portal mixes, and the Goldstone-tagged ``G0`` and ``G+`` (1×1, kept as is)."""
    blocks = model.mass_blocks(kind="scalar")
    (even,) = [b for b in blocks if b.size == 2 and b.cp == "even"]
    (G0,) = [b.fields[0] for b in blocks if b.size == 1 and b.goldstones and not b.complex]
    (Gp,) = [b.fields[0] for b in blocks if b.size == 1 and b.goldstones and b.complex]
    if len(blocks) != 3:
        raise ValueError(f"expected the (h, S) block, G0 and G+, got {blocks}")
    return even, G0, Gp


def build(benchmark=None):
    bench = benchmark_point() if benchmark is None else dict(benchmark)
    p = sm.pieces(bench, higgs=True)
    ew = p.ew

    # --- delta: the singlet ---------------------------------------------
    P = p.params
    vS = P.external("vS", bench["vS"], tex=TEX["vS"], positive=True, unit_dim=1)
    lamS = P.external("lamS", bench["lamS"], tex=TEX["lamS"])
    lamHS = P.external("lamHS", bench["lamHS"], tex=TEX["lamHS"])
    muS2 = P.internal("muS2", tex=TEX["muS2"], unit_dim=2)
    S = Scalar("S", reps={}, component_names=["S"], real=True, tex="S")
    s0 = S.S
    S.expand_vev({s0: vS})
    Z2 = ZN("Z2", 2)
    Z2.assign(1, S)

    V_S = (muS2.s / 2 * s0**2 + lamS.s / 4 * s0**4
           + lamHS.s / 2 * inner(ew.H, ew.H) * s0**2)
    p.add_term(-V_S, "potential", "singlet_potential")
    # ½(∂S)², the canonical term of a real scalar (feynlag ≥ 0.5.1; FG-8 resolved)
    p.add_term(sum(expr for expr, _sector in kinetic(S)), "kinetic", "singlet_kinetic")
    p.fields.append(S)
    p.discrete_groups = [Z2]

    g, gp, v = ew.gw.s, ew.g1.s, ew.v.s
    P.add(*sm.width_params(bench))
    WH2 = P.external("WH2", bench["WH2"], tex=TEX["WH2"], positive=True, unit_dim=1)
    MW = P.internal("MW", g * v / 2, tex=TEX["MW"], positive=True, unit_dim=1)
    MZ = P.internal("MZ", sp.sqrt(g**2 + gp**2) * v / 2, tex=TEX["MZ"], positive=True,
                    unit_dim=1)
    theta = P.internal("theta", tex=TEX["theta"])       # defined by diagonalize below

    model = Model(ID, gauge_groups=p.gauge_groups, discrete_groups=[Z2],
                  fields=p.fields, parameters=P, lagrangian=p.lagrangian())
    model.solve_tadpoles([ew.mu2, muS2])
    Z, A, Wp, Wm = sm.ew_gauge_basis(model)

    # --- CP-even mixing (h, s) → (h1, h2) ------------------------------------
    # symbolic tan 2θ route, principal branch θ = ½ atan(2 M12/(M11 − M22)): h1 is the
    # h-like state (labels follow mixing, CONVENTIONS.md / UG-4). No values=, which would
    # reorder the states by mass instead.
    even, G0, Gp = scalar_blocks(model)
    h_weak = even.fields[0]
    mix = model.diagonalize(even, names=["h1", "h2"], tex=TEX, angle=theta)
    h1, h2 = mix.new_fields
    rot, M_even = mix.rotation, even.matrix
    m1sq, m2sq = mix.masses_squared
    MH1 = P.internal("MH1", sp.sqrt(m1sq), tex=TEX["MH1"], positive=True, unit_dim=1)
    MH2 = P.internal("MH2", sp.sqrt(m2sq), tex=TEX["MH2"], positive=True, unit_dim=1)

    Gm, cmap = conjugate_pair(Gp, "Gm", tex=TEX["Gm"])
    model.physical.add_bosons([G0, Gp, Gm], goldstones=[G0, Gp, Gm])
    model.physical.add_conjugate_pair(Gp, Gm, cmap)
    phys = model.physical

    bosons = dict(h1=h1, h2=h2, G0=G0, Gp=Gp, Gm=Gm, Z=Z, A=A, Wp=Wp, Wm=Wm)
    b_for_particles = dict(bosons, h=h1)
    boson_particles = sm.ew_boson_particles(b_for_particles, h_mass="MH1") + [
        UFOParticle(h2, 35, "h2", spin=1, mass="MH2", width="WH2")]

    return ModelBundle(
        id=ID, model=model, pieces=p, bosons=bosons, cmap=dict(phys.cmap),
        charges=phys.charges, conjugates=dict(phys.conjugates), params=P, benchmark=bench,
        dirac=sm.dirac_specs(p), boson_particles=boson_particles,
        goldstones=tuple(phys.goldstones),
        extra=dict(ew=ew, S=S, s0=s0, vS=vS, lamS=lamS, lamHS=lamHS, muS2=muS2,
                   Z2=Z2, M_even=M_even, rot=rot, theta=theta,
                   MW=MW, MZ=MZ, MH1=MH1, MH2=MH2, h_weak=h_weak),
    )


def outputs(bundle, out_dir):
    e = bundle.extra
    masses = {"$m_{h_1}$": e["MH1"].expr, "$m_{h_2}$": e["MH2"].expr, r"$\theta$": e["theta"].expr,
              "$m_W$": e["MW"].expr, "$m_Z$": e["MZ"].expr}
    return standard_outputs(bundle, out_dir, "SM_SINGLET_Z2_UFO", masses)
