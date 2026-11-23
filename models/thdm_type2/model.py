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

from feynlag import Model, ParameterSet, Scalar, ZN, inner, kinetic
from feynlag.export.ufo import UFOParticle

from feynlag_models import MODELS_DIR
from feynlag_models import metadata as md
from feynlag_models.bundle import ModelBundle
from feynlag_models.outputs import standard_outputs
from feynlag_models.tex import TEX
from models.sm import model as sm

ID = "thdm_type2"
PARENT = "sm"


def benchmark_point():
    return md.benchmark_inputs(MODELS_DIR / ID)


def alpha_branch(M_even, values):
    """``k`` such that ``½ atan(2M12/(M11−M22)) + k π/2 = ½ atan2(2M12, M11−M22)`` at ``values``.

    ``0`` when M11 > M22 (the principal branch is already Gunion–Haber's), ``±1`` with the sign of
    M12 otherwise. The closed form then holds in the benchmark's region of sign(M11 − M22) and
    sign(M12); a point across M11 = M22 needs its own build.

    ``build()`` no longer calls this: ``Model.diagonalize(..., values=)`` applies the same rule
    (heavier state first). It stays as the independent reference the branch test compares with.
    """
    M11, M22, M12 = (float(sp.N(M_even[a, b].subs(values))) for a, b in ((0, 0), (1, 1), (0, 1)))
    if abs(M11 - M22) <= 1e-12 * max(abs(M11), abs(M22)):
        raise ValueError("M11 = M22: the CP-even labels are not defined at this point")
    if M11 > M22:
        return 0
    return 1 if M12 > 0 else -1


def scalar_blocks(model):
    """``(even, odd, charged)`` from ``model.mass_blocks(kind="scalar")``: the CP-even (ρ1, ρ2),
    the CP-odd (η1, η2) and the charged (H1⁺, H2⁺) blocks, the last two with the Goldstone
    direction (v1, v2)/v."""
    blocks = model.mass_blocks(kind="scalar")
    (even,) = [b for b in blocks if b.cp == "even"]
    (odd,) = [b for b in blocks if b.cp == "odd"]
    (charged,) = [b for b in blocks if b.complex]
    if len(blocks) != 3 or any(b.size != 2 for b in blocks):
        raise ValueError(f"expected three 2x2 scalar blocks, got {blocks}")
    return even, odd, charged


def build(benchmark=None):
    bench = benchmark_point() if benchmark is None else dict(benchmark)
    p = sm.pieces(bench, higgs=False)
    SU2L, U1Y = p.SU2L, p.U1Y

    # --- parameters: (v, tanβ, m12², λ1..λ5) external; v1, v2, m11², m22² internal
    # (declared once, in the order the UFO parameter card has always had). pieces(higgs=False)
    # declares gw, g1, gs and the masses; the set is rebuilt in the 2HDM order and becomes p.params
    P = p.params = ParameterSet(p.gw, p.g1, p.gs)
    v = P.external("v", bench["v"], tex=TEX["v"], positive=True, unit_dim=1)
    tanb = P.external("tanb", bench["tanb"], tex=TEX["tanb"], positive=True)
    m12sq = P.external("m12sq", bench["m12sq"], tex=TEX["m12sq"], unit_dim=2)
    lams = [P.external(f"lam{k}", bench[f"lam{k}"], tex=TEX[f"lam{k}"]) for k in range(1, 6)]
    l1, l2, l3, l4, l5 = (q.s for q in lams)
    MT, MB, MTA = (p.masses[k] for k in ("MT", "MB", "MTA"))
    P.add(MT, MB, MTA)
    beta = P.internal("beta", sp.atan(tanb.s), tex=TEX["beta"])
    v1 = P.internal("v1", v.s * sp.cos(beta.s), tex=TEX["v1"], positive=True, unit_dim=1)
    v2 = P.internal("v2", v.s * sp.sin(beta.s), tex=TEX["v2"], positive=True, unit_dim=1)
    m11sq = P.internal("m11sq", tex=TEX["m11sq"], unit_dim=2)
    m22sq = P.internal("m22sq", tex=TEX["m22sq"], unit_dim=2)

    # --- fields ------------------------------------------------------------
    H1 = Scalar("H1", reps={SU2L: 2, U1Y: sp.Rational(1, 2)}, component_names=["H1p", "H10"],
                component_tex=["H_1^+", "H_1^0"])
    H2 = Scalar("H2", reps={SU2L: 2, U1Y: sp.Rational(1, 2)}, component_names=["H2p", "H20"],
                component_tex=["H_2^+", "H_2^0"])
    H1.expand_vev({H1.H10: v1}, tex=TEX)
    H2.expand_vev({H2.H20: v2}, tex=TEX)
    Z2 = ZN("Z2", 2)
    Z2.assign(1, H2)
    Z2.assign(1, p.fermions["uR"])          # type II: u_R odd with H2

    H1dH1, H2dH2, H1dH2 = inner(H1, H1), inner(H2, H2), inner(H1, H2)
    V_even = (m11sq.s * H1dH1 + m22sq.s * H2dH2
              + l1 / 2 * H1dH1**2 + l2 / 2 * H2dH2**2
              + l3 * H1dH1 * H2dH2 + l4 * H1dH2 * sp.conjugate(H1dH2)
              + l5 / 2 * (H1dH2**2 + sp.conjugate(H1dH2)**2))
    V_soft = -m12sq.s * (H1dH2 + sp.conjugate(H1dH2))
    p.add_term(-V_even, "potential", "thdm_potential")
    p.add_term(-V_soft, "potential", "soft_z2_breaking")
    for k, H in ((1, H1), (2, H2)):
        p.add_term(sum(expr for expr, _sector in kinetic(H)), "kinetic", f"thdm_kinetic_{k}")

    # type-II Yukawas: y_b = √2 m_b/v1, y_τ = √2 m_τ/v1, y_t = √2 m_t/v2
    yt = P.internal("yt", sp.sqrt(2) * MT.s / v2.s, tex=TEX["yt"])
    yb = P.internal("yb", sp.sqrt(2) * MB.s / v1.s, tex=TEX["yb"])
    ytau = P.internal("ytau", sp.sqrt(2) * MTA.s / v1.s, tex=TEX["ytau"])
    p.yukawa_params = dict(yt=yt, yb=yb, ytau=ytau)
    p.yukawa = sm.yukawa_terms(p, H1, H2, ytau.s, yb.s, yt.s)
    for name, expr in p.yukawa.items():
        p.add_term(expr, "yukawa", name)

    p.fields = [H1, H2] + p.fields
    lagrangian_params = ParameterSet(*P)   # snapshot: the Lagrangian parameters, before widths
    p.discrete_groups = [Z2]

    P.add(*sm.width_params(bench))
    WHH, WA0, WHp = (P.external(n, bench[n], tex=TEX[n], positive=True, unit_dim=1)
                     for n in ("WHH", "WA0", "WHp"))
    alpha = P.internal("alpha", tex=TEX["alpha"])          # defined by diagonalize below
    g, gp = p.gw.s, p.g1.s
    MW = P.internal("MW", g * v.s / 2, tex=TEX["MW"], positive=True, unit_dim=1)
    MZ = P.internal("MZ", sp.sqrt(g**2 + gp**2) * v.s / 2, tex=TEX["MZ"], positive=True,
                    unit_dim=1)

    # the Model is declared WITHOUT Z2 because m12² breaks it softly (so
    # Model.validate would fail); tests check Z2 term by term
    model = Model(ID, gauge_groups=p.gauge_groups, fields=p.fields,
                  parameters=P, lagrangian=p.lagrangian())
    model.solve_tadpoles([m11sq, m22sq])
    # the Lagrangian parameters at the benchmark (tadpoles solved; alpha is not defined yet)
    values = lagrangian_params.numeric()

    # --- physical basis --------------------------------------------------------
    Z, A, Wp, Wm = sm.ew_gauge_basis(model)
    even, odd, charged = scalar_blocks(model)
    # (H, h) = R(α)(ρ1, ρ2) on Gunion–Haber's branch α = ½ atan2(2M12, M11 − M22), so m_H ≥ m_h
    # (CONVENTIONS.md, UG-4): values= makes diagonalize put the heavier state first, shifting
    # the principal ½ atan(…) by ±π/2 when M11 < M22, exactly as alpha_branch does
    mix_even = model.diagonalize(even, names=["H", "h"], tex=TEX, angle=alpha, values=values)
    # (G⁰, A) = R(β)(η1, η2) and (G⁺, H⁺) = R(β)(H1⁺, H2⁺), fixed by the Goldstone directions
    mix_odd = model.diagonalize(odd, names=["G0", "A0"], tex=TEX, angle=beta)
    mix_ch = model.diagonalize(charged, names=["Gp", "Hp"], conjugate_names=["Gm", "Hm"],
                               tex=TEX, angle=beta)
    Hh, h = mix_even.new_fields
    G0, A0 = mix_odd.new_fields
    Gp, Hp = mix_ch.new_fields
    phys = model.physical
    Gm, Hm = phys.conjugates[Gp], phys.conjugates[Hp]
    rot_even, rot_odd, rot_ch = mix_even.rotation, mix_odd.rotation, mix_ch.rotation
    M_even, M_odd, M_ch = even.matrix, odd.matrix, charged.matrix

    mHH2, mh2 = mix_even.masses_squared
    mA2, mHp2 = mix_odd.masses_squared[1], mix_ch.masses_squared[1]
    MH0 = P.internal("MH0", sp.sqrt(mh2), tex=TEX["MH0"], positive=True, unit_dim=1)
    MHH = P.internal("MHH", sp.sqrt(mHH2), tex=TEX["MHH"], positive=True, unit_dim=1)
    MA0 = P.internal("MA0", sp.sqrt(mA2), tex=TEX["MA0"], positive=True, unit_dim=1)
    MHp = P.internal("MHp", sp.sqrt(mHp2), tex=TEX["MHp"], positive=True, unit_dim=1)

    bosons = dict(h=h, H=Hh, A0=A0, G0=G0, Gp=Gp, Gm=Gm, Hp=Hp, Hm=Hm, Z=Z, A=A, Wp=Wp, Wm=Wm)
    boson_particles = sm.ew_boson_particles(dict(bosons, h=h), h_mass="MH0") + [
        UFOParticle(Hh, 35, "h2", spin=1, mass="MHH", width="WHH"),
        UFOParticle(A0, 36, "h3", spin=1, mass="MA0", width="WA0"),
        UFOParticle(Hp, 37, "h+", antiname="h-", spin=1, mass="MHp", width="WHp",
                    charge=1, antisymbol=Hm),
    ]

    return ModelBundle(
        id=ID, model=model, pieces=p, bosons=bosons, cmap=dict(phys.cmap),
        charges=phys.charges, conjugates=dict(phys.conjugates), params=P, benchmark=bench,
        dirac=sm.dirac_specs(p), boson_particles=boson_particles,
        goldstones=tuple(phys.goldstones),
        extra=dict(H1=H1, H2=H2, Z2=Z2, v=v, tanb=tanb, beta=beta, v1=v1, v2=v2,
                   m12sq=m12sq, lams=lams, m11sq=m11sq, m22sq=m22sq,
                   M_even=M_even, M_odd=M_odd, M_ch=M_ch,
                   rot_even=rot_even, rot_odd=rot_odd, rot_ch=rot_ch, alpha=alpha,
                   MW=MW, MZ=MZ, MH0=MH0, MHH=MHH, MA0=MA0, MHp=MHp,
                   rho=tuple(even.fields), eta=tuple(odd.fields),
                   branch_valid_for=mix_even.branch_valid_for),
    )


def outputs(bundle, out_dir):
    e = bundle.extra
    masses = {"$m_h$": e["MH0"].expr, "$m_H$": e["MHH"].expr, "$m_A$": e["MA0"].expr,
              r"$m_{H^\pm}$": e["MHp"].expr, r"$\alpha$": e["alpha"].expr, r"$\beta$": e["beta"].expr,
              "$m_W$": e["MW"].expr, "$m_Z$": e["MZ"].expr}
    return standard_outputs(bundle, out_dir, "THDM_TYPE2_UFO", masses)
