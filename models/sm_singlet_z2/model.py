"""SM + real singlet scalar S with a Z2 symmetry, spontaneously broken by <S> = v_S.

Parent + delta on ``models/sm``: one real gauge-singlet scalar, a Z2 under
which only S is odd, and the potential terms

    V ⊃ ½ μ_S² S² + ¼ λ_S S⁴ + ½ λ_HS (H†H) S²        (CONVENTIONS.md)

After EWSB the CP-even states (h, s) mix through the portal λ_HS with
``tan 2θ = 2 M12/(M11 − M22)``; every coupling of h1 (h2) to SM particles is
the SM one times cos θ (sin θ).
"""

import sympy as sp

from feynlag import (
    ExternalParameter, InternalParameter, Model, ParameterSet, PartialMu, Scalar,
    ZN, dag, diagonalize_orthogonal_2x2, to_physical_basis,
)
from feynlag.export.ufo import UFOParticle

from feynlag_models import MODELS_DIR
from feynlag_models import metadata as md
from feynlag_models.bundle import ModelBundle
from feynlag_models.checks import scalar_mass_block
from feynlag_models.outputs import standard_outputs
from models.sm import model as sm

ID = "sm_singlet_z2"
PARENT = "sm"


def benchmark_point():
    return md.benchmark_inputs(MODELS_DIR / ID)


def build(benchmark=None):
    bench = benchmark_point() if benchmark is None else dict(benchmark)
    p = sm.pieces(bench, higgs=True)
    ew = p.ew

    # --- delta: the singlet ---------------------------------------------
    vS = ExternalParameter("vS", bench["vS"], positive=True, unit_dim=1)
    lamS = ExternalParameter("lamS", bench["lamS"])
    lamHS = ExternalParameter("lamHS", bench["lamHS"])
    muS2 = InternalParameter("muS2", unit_dim=2)
    S = Scalar("S", reps={}, component_names=["S"], real=True)
    s0 = S.components[0]
    S.expand_vev({s0: vS})
    Z2 = ZN("Z2", 2)
    Z2.assign(1, S)

    HdH = (dag(ew.H) * ew.H.mat)[0]
    V_S = (muS2.s / 2 * s0**2 + lamS.s / 4 * s0**4 + lamHS.s / 2 * HdH * s0**2)
    p.add_term(-V_S, "potential", "singlet_potential")
    p.add_term(sp.Rational(1, 2) * PartialMu(s0) ** 2, "kinetic", "singlet_kinetic")
    p.fields.append(S)
    p.params += [vS, lamS, lamHS, muS2]
    p.discrete_groups = [Z2]

    model = Model(ID, gauge_groups=p.gauge_groups, discrete_groups=[Z2],
                  fields=p.fields, parameters=p.params, lagrangian=p.lagrangian())
    model.solve_tadpoles([ew.mu2, muS2])
    phys = to_physical_basis(model, ew)

    # --- CP-even mixing (h, s) → (h1, h2) ------------------------------------
    # FEYNLAG_GAPS.md FG-1: Model.mass_matrix double-shifts a real VEV'd scalar;
    # scalar_mass_block evaluates the vacuum point once.
    M_even = scalar_mass_block(model, [phys.h, s0])
    h1, h2 = sp.symbols("h1 h2", real=True)
    theta = InternalParameter("theta")
    rot = diagonalize_orthogonal_2x2(M_even, [phys.h, s0], [h1, h2], angle=theta.s)
    theta.define(rot.angle_solution)
    model.rotate(rot)
    m1sq, m2sq = rot.masses_squared(M_even, simplifier=sp.expand)

    bosons = dict(h1=h1, h2=h2, G0=phys.G0, Gp=phys.Gp, Gm=phys.Gm,
                  Z=phys.Z, A=phys.A, Wp=phys.Wp, Wm=phys.Wm)
    charges = {h1: 0, h2: 0, phys.G0: 0, phys.Gp: 1, phys.Gm: -1,
               phys.Z: 0, phys.A: 0, phys.Wp: 1, phys.Wm: -1}
    conjugates = {phys.Gp: phys.Gm, phys.Gm: phys.Gp, phys.Wp: phys.Wm, phys.Wm: phys.Wp}

    g, gp, v = ew.gw.s, ew.g1.s, ew.v.s
    MW = InternalParameter("MW", g * v / 2, positive=True, unit_dim=1)
    MZ = InternalParameter("MZ", sp.sqrt(g**2 + gp**2) * v / 2, positive=True, unit_dim=1)
    MH1 = InternalParameter("MH1", sp.sqrt(m1sq), positive=True, unit_dim=1)
    MH2 = InternalParameter("MH2", sp.sqrt(m2sq), positive=True, unit_dim=1)
    WH2 = ExternalParameter("WH2", bench["WH2"], positive=True, unit_dim=1)
    params = ParameterSet(*p.params, *sm.width_params(bench), WH2, MW, MZ, theta, MH1, MH2)

    b_for_particles = dict(bosons, h=h1)
    boson_particles = sm.ew_boson_particles(b_for_particles, h_mass="MH1") + [
        UFOParticle(h2, 35, "h2", spin=1, mass="MH2", width="WH2")]

    return ModelBundle(
        id=ID, model=model, pieces=p, bosons=bosons, cmap=phys.cmap,
        charges=charges, conjugates=conjugates, params=params, benchmark=bench,
        dirac=sm.dirac_specs(p), boson_particles=boson_particles,
        goldstones=(phys.G0, phys.Gp, phys.Gm),
        extra=dict(ew=ew, S=S, s0=s0, vS=vS, lamS=lamS, lamHS=lamHS, muS2=muS2,
                   Z2=Z2, M_even=M_even, rot=rot, theta=theta,
                   MW=MW, MZ=MZ, MH1=MH1, MH2=MH2, h_weak=phys.h),
    )


def outputs(bundle, out_dir):
    e = bundle.extra
    masses = {"m_h1": e["MH1"].expr, "m_h2": e["MH2"].expr, "theta": e["theta"].expr,
              "m_W": e["MW"].expr, "m_Z": e["MZ"].expr}
    return standard_outputs(bundle, out_dir, "SM_SINGLET_Z2_UFO", masses)
