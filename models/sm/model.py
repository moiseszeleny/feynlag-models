"""Standard Model root: SU(3)_c × SU(2)_L × U(1)_Y, one Higgs doublet, one
full fermion generation (t, b, τ, ν_τ). Built with feynlag's electroweak
scaffold; every other model in this library is written as *this* + a delta.

``pieces(benchmark, higgs=True)`` returns the declaration-level objects a child
model mutates before assembling the ``Model``; ``build()`` assembles the SM
itself and returns a :class:`~feynlag_models.bundle.ModelBundle`.
"""

import sympy as sp

from feynlag import (
    Bilinear, Model, ParameterSet, SU3, WeylFermion, conjugate_pair, diracPL, diracPR,
    electroweak_gauge, electroweak_scaffold, fermion_gauge_current, to_physical_basis,
)
from feynlag.export.ufo import UFOParticle

from feynlag_models import MODELS_DIR
from feynlag_models import metadata as md
from feynlag_models.bundle import DiracSpec, ModelBundle, SMPieces
from feynlag_models.outputs import standard_outputs
from feynlag_models.tex import TEX, external, internal

ID = "sm"
PARENT = None


def benchmark_point(model_id=ID):
    return md.benchmark_inputs(MODELS_DIR / model_id)


# ------------------------------------------------------------------ pieces

#: mass-parameter names per flavour, (up, down, charged lepton) rows
MASS_NAMES = {1: (("MT",), ("MB",), ("MTA",)),
              3: (("MU", "MC", "MT"), ("MD", "MS", "MB"), ("ME", "MMU", "MTA"))}
#: LaTeX names of the weak-basis components declared here (feynlag ``component_tex``);
#: the scaffold's Higgs doublet and W/B take theirs from ``feynlag_models.tex.TEX``
G_TEX = [f"G^{{{a}}}" for a in range(1, 9)]
COLOURS = (1, 2, 3)
FERMION_TEX = {
    "Ll": [r"\nu_L", "e_L"],
    "eR": ["e_R"],
    "QL": [f"u_L^{{{c}}}" for c in COLOURS] + [f"d_L^{{{c}}}" for c in COLOURS],
    "uR": [f"u_R^{{{c}}}" for c in COLOURS],
    "dR": [f"d_R^{{{c}}}" for c in COLOURS],
}
YUKAWA_NAMES = {1: (("yt",), ("yb",), ("ytau",)),
                3: (("yu", "yc", "yt"), ("yd", "ys", "yb"), ("ye", "ymu", "ytau"))}


def flavours(p):
    """Flavour indices used in the Lagrangian: the symbolic ``i`` for one
    generation (unchanged SM), the integers ``0, 1, 2`` for three."""
    return [p.idx[0]] if p.generations == 1 else list(range(p.generations))


def pieces(benchmark=None, higgs=True, generations=1):
    """Declaration layer of the SM.

    Args:
        benchmark: numeric point (defaults to ``models/sm/metadata.yaml``).
        higgs: include the Higgs doublet, its kinetic/potential terms and the
            Yukawas. A model that replaces the Higgs sector (2HDM) passes
            ``False`` and supplies its own doublets and Yukawas
            (:func:`yukawa_terms`).
        generations: 1 (third generation only, the SM card) or 3 (every
            flavour, diagonal Yukawas; a child inserts quark mixing).
    """
    if generations not in (1, 3):
        raise ValueError("generations must be 1 or 3")
    bench = benchmark_point() if benchmark is None else dict(benchmark)
    if higgs:
        ew = electroweak_scaffold(gw=bench["gw"], g1=bench["g1"], v=bench["v"],
                                  mh=bench["MH"], tex=TEX)
        SU2L, U1Y, gw_p, g1_p, W, B = ew.SU2L, ew.U1Y, ew.gw, ew.g1, ew.W, ew.B
    else:
        ew = None
        SU2L, U1Y, gw_p, g1_p = electroweak_gauge(gw=bench["gw"], g1=bench["g1"], tex=TEX)
        W = SU2L.bosons("W", component_tex=[TEX[f"W_{a}"] for a in (1, 2, 3)])
        B = U1Y.bosons("B", tex=TEX["B"])
    gs = external("gs", bench["gs"], positive=True)
    SU3c = SU3("SU3c", coupling=gs)
    G = SU3c.bosons("G", component_tex=G_TEX)

    i, j = sp.symbols("i j", integer=True)
    Ll = WeylFermion("Ll", reps={SU2L: 2, U1Y: -sp.Rational(1, 2)},
                     chirality="L", nflavors=generations, component_names=["nuL", "eL"],
                     component_tex=FERMION_TEX["Ll"])
    eR = WeylFermion("eR", reps={U1Y: -1}, chirality="R", nflavors=generations,
                     component_names=["eR"], component_tex=FERMION_TEX["eR"])
    QL = WeylFermion("QL", reps={SU2L: 2, U1Y: sp.Rational(1, 6), SU3c: 3},
                     chirality="L", nflavors=generations,
                     component_names=["uL_1", "uL_2", "uL_3",
                                      "dL_1", "dL_2", "dL_3"],
                     component_tex=FERMION_TEX["QL"])
    uR = WeylFermion("uR", reps={U1Y: sp.Rational(2, 3), SU3c: 3},
                     chirality="R", nflavors=generations,
                     component_names=["uR_1", "uR_2", "uR_3"],
                     component_tex=FERMION_TEX["uR"])
    dR = WeylFermion("dR", reps={U1Y: -sp.Rational(1, 3), SU3c: 3},
                     chirality="R", nflavors=generations,
                     component_names=["dR_1", "dR_2", "dR_3"],
                     component_tex=FERMION_TEX["dR"])
    fermions = dict(Ll=Ll, eR=eR, QL=QL, uR=uR, dR=dR)

    # fermion mass inputs (externals) — the Yukawas are internals defined by
    # whichever Higgs sector the model has
    mass_names = [n for row in MASS_NAMES[generations] for n in row]
    masses = {n: external(n, bench[n], positive=True, unit_dim=1)
              for n in mass_names}

    params = [gw_p, g1_p, gs, *masses.values()]
    fields = [W, B, G, Ll, eR, QL, uR, dR]
    p = SMPieces(SU2L=SU2L, U1Y=U1Y, SU3c=SU3c, gw=gw_p, g1=g1_p, gs=gs,
                 W=W, B=B, G=G, idx=(i, j), fermions=fermions,
                 params=params, fields=fields, terms=[], benchmark=bench,
                 generations=generations)
    p.masses = masses

    current = sum(fermion_gauge_current(F, k)
                  for k in flavours(p) for F in (Ll, eR, QL, uR, dR))
    p.add_term(current, "gauge", "fermion_gauge_currents")

    if higgs:
        p.ew = ew
        p.params = [ew.gw, ew.g1, gs, ew.v, ew.lam, ew.mu2, *masses.values()]
        p.fields = [ew.H, ew.W, ew.B, G, Ll, eR, QL, uR, dR]
        from feynlag.models import higgs_lagrangian
        for sector, expr in higgs_lagrangian(ew.H, ew.lam, ew.mu2).items():
            p.add_term(expr, sector, f"higgs_{sector}")
        # y_f = √2 m_f / v   (diagonal in flavour, CONVENTIONS.md)
        ys = {}
        for yrow, mrow in zip(YUKAWA_NAMES[generations], MASS_NAMES[generations]):
            for yn, mn in zip(yrow, mrow):
                ys[yn] = internal(yn, sp.sqrt(2) * masses[mn].s / ew.v.s)
        p.params += list(ys.values())
        p.yukawa_params = ys
        yu, yd, ye = (diagonal_yukawa(ys, row) for row in YUKAWA_NAMES[generations])
        p.yukawa = yukawa_terms(p, ew.H, ew.H, ye, yd, yu)
        for name, expr in p.yukawa.items():
            p.add_term(expr, "yukawa", name)
    return p


def diagonal_yukawa(ys, names):
    """A single-generation coupling symbol, or a diagonal 3×3 ``Matrix``."""
    if len(names) == 1:
        return ys[names[0]].s
    return sp.diag(*(ys[n].s for n in names))


def yukawa_terms(p, Hd, Hu, ye, yd, yu):
    """The Yukawa Lagrangian, one term per fermion type.

    ``−Y_e^{ab} L̄_a H_d e_R^b − Y_d^{ab} Q̄_a H_d d_R^b − Y_u^{ab} Q̄_a H̃_u u_R^b + h.c.``
    with ``H̃ = (H⁰*, −H⁺*)`` written inline (CONVENTIONS.md). ``Hd``/``Hu`` are the
    doublets coupling to down-type/leptons and up-type quarks (both ``H`` in
    the SM; ``H1``/``H2`` in a type-II 2HDM).

    One generation: ``ye, yd, yu`` are real SymPy symbols and the terms carry
    the symbolic flavour index. Three generations: they are 3×3 matrices
    (possibly complex, e.g. ``Y_d = V diag(y)``) and the flavour sums are
    written out with integer indices; the h.c. carries ``conjugate(Y^{ab})``.
    The returned names are ``yukawa_tau/b/t`` (one generation) or
    ``yukawa_lepton/down/up`` (three).
    """
    Ll, eR, QL, uR, dR = (p.fermions[k] for k in ("Ll", "eR", "QL", "uR", "dR"))
    Gp_d, H0_d = Hd.components
    Gp_u, H0_u = Hu.components
    nuL, eL = Ll.components
    nuLbar, eLbar = Ll.bar_components
    eRc, eRbar = eR.components[0], eR.bar_components[0]
    qL_u, qL_d = QL.components[:3], QL.components[3:]
    qLbar_u, qLbar_d = QL.bar_components[:3], QL.bar_components[3:]

    if p.generations == 1:
        i = p.idx[0]
        pairs = lambda Y: [(i, i, Y)]                       # noqa: E731
    else:
        pairs = lambda Y: [(a, b, Y[a, b]) for a in range(3)   # noqa: E731
                           for b in range(3) if Y[a, b] != 0]

    def colour_sum(bars, gamma, fields, a, b):
        return sum(Bilinear(bars[c][a], gamma, fields[c][b]) for c in range(3))

    L_e = L_d = L_u = sp.S.Zero
    for a, b, y in pairs(ye):
        yc = y if p.generations == 1 else sp.conjugate(y)
        L_e += -(y * Gp_d * Bilinear(nuLbar[a], diracPR, eRc[b])
                 + y * H0_d * Bilinear(eLbar[a], diracPR, eRc[b]))
        L_e += -(yc * sp.conjugate(Gp_d) * Bilinear(eRbar[b], diracPL, nuL[a])
                 + yc * sp.conjugate(H0_d) * Bilinear(eRbar[b], diracPL, eL[a]))
    for a, b, y in pairs(yd):
        yc = y if p.generations == 1 else sp.conjugate(y)
        L_d += -(y * Gp_d * colour_sum(qLbar_u, diracPR, dR.components, a, b)
                 + y * H0_d * colour_sum(qLbar_d, diracPR, dR.components, a, b))
        L_d += -(yc * sp.conjugate(Gp_d) * colour_sum(dR.bar_components, diracPL, qL_u, b, a)
                 + yc * sp.conjugate(H0_d) * colour_sum(dR.bar_components, diracPL, qL_d, b, a))
    for a, b, y in pairs(yu):
        yc = y if p.generations == 1 else sp.conjugate(y)
        L_u += -(y * sp.conjugate(H0_u) * colour_sum(qLbar_u, diracPR, uR.components, a, b)
                 + y * (-sp.conjugate(Gp_u)) * colour_sum(qLbar_d, diracPR, uR.components, a, b))
        L_u += -(yc * H0_u * colour_sum(uR.bar_components, diracPL, qL_u, b, a)
                 + yc * (-Gp_u) * colour_sum(uR.bar_components, diracPL, qL_d, b, a))
    if p.generations == 1:
        return {"yukawa_tau": L_e, "yukawa_b": L_d, "yukawa_t": L_u}
    return {"yukawa_lepton": L_e, "yukawa_down": L_d, "yukawa_up": L_u}


#: three-generation UFO names, PDG codes and widths (FeynRules SM names)
_GEN3 = dict(
    up=(("u", 2), ("c", 4), ("t", 6)),
    down=(("d", 1), ("s", 3), ("b", 5)),
    lepton=(("e-", 11), ("mu-", 13), ("ta-", 15)),
    neutrino=(("ve", 12), ("vm", 14), ("vt", 16)),
)


def dirac_specs(p, masses=("MT", "MB", "MTA"), down_left=None):
    """The Dirac fermions (neutrinos left-handed only).

    One generation: t, b, τ, ν_τ keyed by ``IndexedBase`` (symbolic flavour
    index). Three generations: all twelve, each ``DiracSpec`` carrying its
    integer ``flavor``. ``down_left`` optionally replaces the left-handed
    down-quark colour components (a child that rotates ``d_L`` to the mass
    basis passes the mass-basis handles); ``masses`` is ignored for three
    generations (``MASS_NAMES`` is used).
    """
    Ll, eR, QL, uR, dR = (p.fermions[k] for k in ("Ll", "eR", "QL", "uR", "dR"))
    dL = list(down_left) if down_left is not None else list(QL.components[3:])
    if p.generations == 3:
        return _dirac_specs_3(Ll, eR, QL, uR, dR, dL)
    t, tb, b, bb = sp.symbols("t tbar b bbar")
    ta, tap, vt, vtb = sp.symbols("ta tap vt vtbar")
    return [
        DiracSpec("t", QL.components[0], uR.components[0], t, tb, 6, sp.Rational(2, 3),
                  masses[0], "t~", color=3, width="WT",
                  copies=(*QL.components[1:3], *uR.components[1:])),
        DiracSpec("b", dL[0], dR.components[0], b, bb, 5, -sp.Rational(1, 3),
                  masses[1], "b~", color=3,
                  copies=(*dL[1:], *dR.components[1:])),
        DiracSpec("ta-", Ll.components[1], eR.components[0], ta, tap, 15, -1,
                  masses[2], "ta+"),
        DiracSpec("vt", Ll.components[0], None, vt, vtb, 16, 0, "ZERO", "vt~"),
    ]


def _dirac_specs_3(Ll, eR, QL, uR, dR, dL):
    up_m, down_m, lep_m = MASS_NAMES[3]
    specs = []

    def anti(name):
        return name[:-1] + "+" if name.endswith("-") else name + "~"

    def syms(name):
        stem = name.rstrip("-")
        return sp.symbols(f"{stem} {stem}bar")

    for k in range(3):
        name, pdg = _GEN3["up"][k]
        specs.append(DiracSpec(name, QL.components[0], uR.components[0], *syms(name), pdg,
                               sp.Rational(2, 3), up_m[k], anti(name), color=3,
                               width="WT" if name == "t" else "ZERO",
                               copies=(*QL.components[1:3], *uR.components[1:]), flavor=k))
        name, pdg = _GEN3["down"][k]
        specs.append(DiracSpec(name, dL[0], dR.components[0], *syms(name), pdg,
                               -sp.Rational(1, 3), down_m[k], anti(name), color=3,
                               copies=(*dL[1:], *dR.components[1:]), flavor=k))
        name, pdg = _GEN3["lepton"][k]
        specs.append(DiracSpec(name, Ll.components[1], eR.components[0], *syms(name), pdg,
                               -1, lep_m[k], anti(name), flavor=k))
        name, pdg = _GEN3["neutrino"][k]
        specs.append(DiracSpec(name, Ll.components[0], None, *syms(name), pdg,
                               0, "ZERO", anti(name), flavor=k))
    return specs


def ew_boson_particles(b, h_mass="MH", h_width="WH"):
    """UFO particles for the SM electroweak bosons + Goldstones."""
    return [
        UFOParticle(b["h"], 25, "h", spin=1, mass=h_mass, width=h_width),
        UFOParticle(b["G0"], 250, "G0", spin=1, mass="MZ", goldstone=True),
        UFOParticle(b["Gp"], 251, "G+", antiname="G-", spin=1, mass="MW",
                    charge=1, antisymbol=b["Gm"], goldstone=True),
        UFOParticle(b["A"], 22, "a", spin=3),
        UFOParticle(b["Z"], 23, "Z", spin=3, mass="MZ", width="WZ"),
        UFOParticle(b["Wp"], 24, "W+", antiname="W-", spin=3, mass="MW", width="WW",
                    charge=1, antisymbol=b["Wm"]),
    ]


def width_params(bench):
    return [external(n, bench[n], positive=True, unit_dim=1)
            for n in ("WZ", "WW", "WH", "WT")]


# ------------------------------------------------------------------- build

def build(benchmark=None):
    p = pieces(benchmark, higgs=True)
    ew = p.ew
    model = Model("SM", gauge_groups=p.gauge_groups, fields=p.fields,
                  parameters=p.params, lagrangian=p.lagrangian())
    model.solve_tadpoles([ew.mu2])
    phys = to_physical_basis(model, ew, tex=TEX)
    bosons = dict(h=phys.h, G0=phys.G0, Gp=phys.Gp, Gm=phys.Gm,
                  Z=phys.Z, A=phys.A, Wp=phys.Wp, Wm=phys.Wm)
    charges = {phys.h: 0, phys.G0: 0, phys.Gp: 1, phys.Gm: -1,
               phys.Z: 0, phys.A: 0, phys.Wp: 1, phys.Wm: -1}
    conjugates = {phys.Gp: phys.Gm, phys.Gm: phys.Gp, phys.Wp: phys.Wm, phys.Wm: phys.Wp}

    g, gp, v = ew.gw.s, ew.g1.s, ew.v.s
    MW = internal("MW", g * v / 2, positive=True, unit_dim=1)
    MZ = internal("MZ", sp.sqrt(g**2 + gp**2) * v / 2, positive=True, unit_dim=1)
    MH = internal("MH", sp.sqrt(2 * ew.lam.s) * v, positive=True, unit_dim=1)
    params = ParameterSet(*p.params, *width_params(p.benchmark), MW, MZ, MH)

    return ModelBundle(
        id=ID, model=model, pieces=p, bosons=bosons, cmap=phys.cmap,
        charges=charges, conjugates=conjugates, params=params,
        benchmark=p.benchmark, dirac=dirac_specs(p),
        boson_particles=ew_boson_particles(bosons),
        goldstones=(phys.G0, phys.Gp, phys.Gm),
        extra=dict(ew=ew, MW=MW, MZ=MZ, MH=MH),
    )


def outputs(bundle, out_dir):
    e = bundle.extra
    masses = {"$m_h$": e["MH"].expr, "$m_W$": e["MW"].expr, "$m_Z$": e["MZ"].expr,
              "$m_t$": bundle.pieces.masses["MT"].s, "$m_b$": bundle.pieces.masses["MB"].s,
              r"$m_\tau$": bundle.pieces.masses["MTA"].s}
    return standard_outputs(bundle, out_dir, "SM_UFO", masses)
