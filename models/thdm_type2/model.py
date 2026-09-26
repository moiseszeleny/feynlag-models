"""Type-II 2HDM, CP-conserving, with a softly broken Z2. Parent + delta on
``models/sm`` with the Higgs sector *replaced* (``sm.pieces(higgs=False)``).

Potential (CONVENTIONS.md; Gunion–Haber / Branco et al. form, all real):

    V = m11² H1†H1 + m22² H2†H2 − m12² (H1†H2 + h.c.) + ½λ1 (H1†H1)² + ½λ2 (H2†H2)²
        + λ3 (H1†H1)(H2†H2) + λ4 |H1†H2|² + ½λ5 [(H1†H2)² + h.c.]

Z2: H2 → −H2 (softly broken only by m12²); type II: u_R odd (couples to H̃2),
d_R and e_R even (couple to H1). Rotations: (H, h) = R(α)(ρ1, ρ2),
(G⁰, A) = R(β)(η1, η2), (G⁺, H⁺) = R(β)(H1⁺, H2⁺), tan β = v2/v1.
"""

import sympy as sp

from feynlag import (
    Dmu, ExternalParameter, InternalParameter, Model, ParameterSet, Rotation,
    Scalar, ZN, charged_current_rotation, conjugate_pair, dag,
    diagonalize_orthogonal_2x2, rotation_2x2, weinberg_rotation,
)
from feynlag.export.ufo import UFOParticle

from feynlag_models import MODELS_DIR
from feynlag_models import metadata as md
from feynlag_models.bundle import ModelBundle
from feynlag_models.outputs import standard_outputs
from models.sm import model as sm

ID = "thdm_type2"
PARENT = "sm"


def benchmark_point():
    return md.benchmark_inputs(MODELS_DIR / ID)


def build(benchmark=None):
    bench = benchmark_point() if benchmark is None else dict(benchmark)
    p = sm.pieces(bench, higgs=False)
    SU2L, U1Y = p.SU2L, p.U1Y

    # --- parameters: (v, tanβ, m12², λ1..λ5) external; v1, v2, m11², m22² internal
    v = ExternalParameter("v", bench["v"], positive=True, unit_dim=1)
    tanb = ExternalParameter("tanb", bench["tanb"], positive=True)
    m12sq = ExternalParameter("m12sq", bench["m12sq"], unit_dim=2)
    lams = [ExternalParameter(f"lam{k}", bench[f"lam{k}"]) for k in range(1, 6)]
    l1, l2, l3, l4, l5 = (q.s for q in lams)
    beta = InternalParameter("beta", sp.atan(tanb.s))
    v1 = InternalParameter("v1", v.s * sp.cos(beta.s), positive=True, unit_dim=1)
    v2 = InternalParameter("v2", v.s * sp.sin(beta.s), positive=True, unit_dim=1)
    m11sq = InternalParameter("m11sq", unit_dim=2)
    m22sq = InternalParameter("m22sq", unit_dim=2)

    # --- fields ------------------------------------------------------------
    H1 = Scalar("H1", reps={SU2L: 2, U1Y: sp.Rational(1, 2)}, component_names=["H1p", "H10"],
                component_tex=["H_1^+", "H_1^0"])
    H2 = Scalar("H2", reps={SU2L: 2, U1Y: sp.Rational(1, 2)}, component_names=["H2p", "H20"],
                component_tex=["H_2^+", "H_2^0"])
    H1.expand_vev({H1.components[1]: v1})
    H2.expand_vev({H2.components[1]: v2})
    Z2 = ZN("Z2", 2)
    Z2.assign(1, H2)
    Z2.assign(1, p.fermions["uR"])          # type II: u_R odd with H2

    H1dH1 = (dag(H1) * H1.mat)[0]
    H2dH2 = (dag(H2) * H2.mat)[0]
    H1dH2 = (dag(H1) * H2.mat)[0]
    V_even = (m11sq.s * H1dH1 + m22sq.s * H2dH2
              + l1 / 2 * H1dH1**2 + l2 / 2 * H2dH2**2
              + l3 * H1dH1 * H2dH2 + l4 * H1dH2 * sp.conjugate(H1dH2)
              + l5 / 2 * (H1dH2**2 + sp.conjugate(H1dH2)**2))
    V_soft = -m12sq.s * (H1dH2 + sp.conjugate(H1dH2))
    p.add_term(-V_even, "potential", "thdm_potential")
    p.add_term(-V_soft, "potential", "soft_z2_breaking")
    for k, H in ((1, H1), (2, H2)):
        DH = Dmu(H)
        p.add_term((dag(DH) * DH)[0], "kinetic", f"thdm_kinetic_{k}")

    # type-II Yukawas: y_b = √2 m_b/v1, y_τ = √2 m_τ/v1, y_t = √2 m_t/v2
    MT, MB, MTA = (p.masses[k] for k in ("MT", "MB", "MTA"))
    yt = InternalParameter("yt", sp.sqrt(2) * MT.s / v2.s)
    yb = InternalParameter("yb", sp.sqrt(2) * MB.s / v1.s)
    ytau = InternalParameter("ytau", sp.sqrt(2) * MTA.s / v1.s)
    p.yukawa_params = dict(yt=yt, yb=yb, ytau=ytau)
    p.yukawa = sm.yukawa_terms(p, H1, H2, ytau.s, yb.s, yt.s)
    for name, expr in p.yukawa.items():
        p.add_term(expr, "yukawa", name)

    p.fields = [H1, H2] + p.fields
    p.params = [p.gw, p.g1, p.gs, v, tanb, m12sq, *lams, MT, MB, MTA,
                beta, v1, v2, m11sq, m22sq, yt, yb, ytau]
    p.discrete_groups = [Z2]

    # the Model is declared WITHOUT Z2 because m12² breaks it softly (so
    # Model.validate would fail); tests check Z2 term by term
    model = Model(ID, gauge_groups=p.gauge_groups, fields=p.fields,
                  parameters=p.params, lagrangian=p.lagrangian())
    model.solve_tadpoles([m11sq, m22sq])

    # --- physical basis --------------------------------------------------------
    Z, A = weinberg_rotation(model, SU2L, U1Y)
    Wp, Wm = charged_current_rotation(model, SU2L)
    rho1, rho2 = sp.Symbol("H10_r", real=True), sp.Symbol("H20_r", real=True)
    eta1, eta2 = sp.Symbol("H10_i", real=True), sp.Symbol("H20_i", real=True)
    H1p, H2p = H1.components[0], H2.components[0]

    M_even = model.mass_matrix([rho1, rho2])
    M_odd = model.mass_matrix([eta1, eta2])
    M_ch = model.mass_matrix([H1p, H2p], charged=True)

    Hh, h = sp.symbols("H h", real=True)
    alpha = InternalParameter("alpha")
    rot_even = diagonalize_orthogonal_2x2(M_even, [rho1, rho2], [Hh, h], angle=alpha.s)
    alpha.define(rot_even.angle_solution)
    G0, A0 = sp.symbols("G0 A0", real=True)
    rot_odd = Rotation([eta1, eta2], [G0, A0], rotation_2x2(beta.s))
    Gp, Hp = sp.symbols("Gp Hp")
    rot_ch = Rotation([H1p, H2p], [Gp, Hp], rotation_2x2(beta.s))
    for r in (rot_even, rot_odd, rot_ch):
        model.rotate(r)
    Gm, cmapG = conjugate_pair(Gp, "Gm")
    Hm, cmapH = conjugate_pair(Hp, "Hm")
    cmap = {**cmapG, **cmapH}

    mHH2, mh2 = rot_even.masses_squared(M_even, simplifier=sp.expand)
    mA2 = rot_odd.masses_squared(M_odd, simplifier=sp.simplify)[1]
    mHp2 = rot_ch.masses_squared(M_ch, simplifier=sp.simplify)[1]

    bosons = dict(h=h, H=Hh, A0=A0, G0=G0, Gp=Gp, Gm=Gm, Hp=Hp, Hm=Hm, Z=Z, A=A, Wp=Wp, Wm=Wm)
    charges = {h: 0, Hh: 0, A0: 0, G0: 0, Gp: 1, Gm: -1, Hp: 1, Hm: -1, Z: 0, A: 0, Wp: 1, Wm: -1}
    conjugates = {Gp: Gm, Gm: Gp, Hp: Hm, Hm: Hp, Wp: Wm, Wm: Wp}

    g, gp = p.gw.s, p.g1.s
    MW = InternalParameter("MW", g * v.s / 2, positive=True, unit_dim=1)
    MZ = InternalParameter("MZ", sp.sqrt(g**2 + gp**2) * v.s / 2, positive=True, unit_dim=1)
    MH0 = InternalParameter("MH0", sp.sqrt(mh2), positive=True, unit_dim=1)
    MHH = InternalParameter("MHH", sp.sqrt(mHH2), positive=True, unit_dim=1)
    MA0 = InternalParameter("MA0", sp.sqrt(mA2), positive=True, unit_dim=1)
    MHp = InternalParameter("MHp", sp.sqrt(mHp2), positive=True, unit_dim=1)
    widths = [ExternalParameter(n, bench[n], positive=True, unit_dim=1)
              for n in ("WHH", "WA0", "WHp")]
    params = ParameterSet(*p.params, *sm.width_params(bench), *widths, alpha,
                          MW, MZ, MH0, MHH, MA0, MHp)

    boson_particles = sm.ew_boson_particles(dict(bosons, h=h), h_mass="MH0") + [
        UFOParticle(Hh, 35, "h2", spin=1, mass="MHH", width="WHH"),
        UFOParticle(A0, 36, "h3", spin=1, mass="MA0", width="WA0"),
        UFOParticle(Hp, 37, "h+", antiname="h-", spin=1, mass="MHp", width="WHp",
                    charge=1, antisymbol=Hm),
    ]

    return ModelBundle(
        id=ID, model=model, pieces=p, bosons=bosons, cmap=cmap,
        charges=charges, conjugates=conjugates, params=params, benchmark=bench,
        dirac=sm.dirac_specs(p), boson_particles=boson_particles,
        goldstones=(G0, Gp, Gm),
        extra=dict(H1=H1, H2=H2, Z2=Z2, v=v, tanb=tanb, beta=beta, v1=v1, v2=v2,
                   m12sq=m12sq, lams=lams, m11sq=m11sq, m22sq=m22sq,
                   M_even=M_even, M_odd=M_odd, M_ch=M_ch,
                   rot_even=rot_even, rot_odd=rot_odd, rot_ch=rot_ch, alpha=alpha,
                   MW=MW, MZ=MZ, MH0=MH0, MHH=MHH, MA0=MA0, MHp=MHp,
                   rho=(rho1, rho2), eta=(eta1, eta2)),
    )


def outputs(bundle, out_dir):
    e = bundle.extra
    masses = {"$m_h$": e["MH0"].expr, "$m_H$": e["MHH"].expr, "$m_A$": e["MA0"].expr,
              r"$m_{H^\pm}$": e["MHp"].expr, r"$\alpha$": e["alpha"].expr, r"$\beta$": e["beta"].expr,
              "$m_W$": e["MW"].expr, "$m_Z$": e["MZ"].expr}
    return standard_outputs(bundle, out_dir, "THDM_TYPE2_UFO", masses)
