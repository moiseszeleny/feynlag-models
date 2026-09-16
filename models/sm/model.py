"""Standard Model root: SU(3)_c × SU(2)_L × U(1)_Y, one Higgs doublet, one
full fermion generation (t, b, τ, ν_τ). Built with feynlag's electroweak
scaffold; every other model in this library is written as *this* + a delta.

``pieces(benchmark, higgs=True)`` returns the declaration-level objects a child
model mutates before assembling the ``Model``; ``build()`` assembles the SM
itself and returns a :class:`~feynlag_models.bundle.ModelBundle`.
"""

import sympy as sp

from feynlag import (
    Bilinear, ExternalParameter, InternalParameter, Model, ParameterSet, SU3,
    WeylFermion, conjugate_pair, diracPL, diracPR, electroweak_gauge,
    electroweak_scaffold,
    fermion_gauge_current, to_physical_basis,
)
from feynlag.export.ufo import UFOParticle

from feynlag_models import MODELS_DIR
from feynlag_models import metadata as md
from feynlag_models.bundle import DiracSpec, ModelBundle, SMPieces
from feynlag_models.outputs import standard_outputs

ID = "sm"
PARENT = None


def benchmark_point(model_id=ID):
    return dict(md.load(MODELS_DIR / model_id)["benchmark"])


# ------------------------------------------------------------------ pieces

def pieces(benchmark=None, higgs=True):
    """Declaration layer of the SM.

    Args:
        benchmark: numeric point (defaults to ``models/sm/metadata.yaml``).
        higgs: include the Higgs doublet, its kinetic/potential terms and the
            Yukawas. A model that replaces the Higgs sector (2HDM) passes
            ``False`` and supplies its own doublets and Yukawas
            (:func:`yukawa_terms`).
    """
    bench = benchmark_point() if benchmark is None else dict(benchmark)
    if higgs:
        ew = electroweak_scaffold(gw=bench["gw"], g1=bench["g1"], v=bench["v"],
                                  mh=bench["MH"])
        SU2L, U1Y, gw_p, g1_p, W, B = ew.SU2L, ew.U1Y, ew.gw, ew.g1, ew.W, ew.B
    else:
        ew = None
        SU2L, U1Y, gw_p, g1_p = electroweak_gauge(gw=bench["gw"], g1=bench["g1"])
        W, B = SU2L.bosons("W"), U1Y.bosons("B")
    gs = ExternalParameter("gs", bench["gs"], positive=True)
    SU3c = SU3("SU3c", coupling=gs)
    G = SU3c.bosons("G")

    i, j = sp.symbols("i j", integer=True)
    Ll = WeylFermion("Ll", reps={SU2L: 2, U1Y: -sp.Rational(1, 2)},
                     chirality="L", nflavors=1, component_names=["nuL", "eL"])
    eR = WeylFermion("eR", reps={U1Y: -1}, chirality="R", nflavors=1,
                     component_names=["eR"])
    QL = WeylFermion("QL", reps={SU2L: 2, U1Y: sp.Rational(1, 6), SU3c: 3},
                     chirality="L", nflavors=1,
                     component_names=["uL_1", "uL_2", "uL_3",
                                      "dL_1", "dL_2", "dL_3"])
    uR = WeylFermion("uR", reps={U1Y: sp.Rational(2, 3), SU3c: 3},
                     chirality="R", nflavors=1,
                     component_names=["uR_1", "uR_2", "uR_3"])
    dR = WeylFermion("dR", reps={U1Y: -sp.Rational(1, 3), SU3c: 3},
                     chirality="R", nflavors=1,
                     component_names=["dR_1", "dR_2", "dR_3"])
    fermions = dict(Ll=Ll, eR=eR, QL=QL, uR=uR, dR=dR)

    # fermion mass inputs (externals) — the Yukawas are internals defined by
    # whichever Higgs sector the model has
    MT = ExternalParameter("MT", bench["MT"], positive=True, unit_dim=1)
    MB = ExternalParameter("MB", bench["MB"], positive=True, unit_dim=1)
    MTA = ExternalParameter("MTA", bench["MTA"], positive=True, unit_dim=1)

    params = [gw_p, g1_p, gs, MT, MB, MTA]
    fields = [W, B, G, Ll, eR, QL, uR, dR]
    p = SMPieces(SU2L=SU2L, U1Y=U1Y, SU3c=SU3c, gw=gw_p, g1=g1_p, gs=gs,
                 W=W, B=B, G=G, idx=(i, j), fermions=fermions,
                 params=params, fields=fields, terms=[], benchmark=bench)
    p.masses = dict(MT=MT, MB=MB, MTA=MTA)

    current = (fermion_gauge_current(Ll, i) + fermion_gauge_current(eR, i)
               + fermion_gauge_current(QL, i) + fermion_gauge_current(uR, i)
               + fermion_gauge_current(dR, i))
    p.add_term(current, "gauge", "fermion_gauge_currents")

    if higgs:
        p.ew = ew
        p.params = [ew.gw, ew.g1, gs, ew.v, ew.lam, ew.mu2, MT, MB, MTA]
        p.fields = [ew.H, ew.W, ew.B, G, Ll, eR, QL, uR, dR]
        from feynlag.models import higgs_lagrangian
        for sector, expr in higgs_lagrangian(ew.H, ew.lam, ew.mu2).items():
            p.add_term(expr, sector, f"higgs_{sector}")
        # y_f = √2 m_f / v   (single generation, CONVENTIONS.md)
        yt = InternalParameter("yt", sp.sqrt(2) * MT.s / ew.v.s)
        yb = InternalParameter("yb", sp.sqrt(2) * MB.s / ew.v.s)
        ytau = InternalParameter("ytau", sp.sqrt(2) * MTA.s / ew.v.s)
        p.params += [yt, yb, ytau]
        p.yukawa_params = dict(yt=yt, yb=yb, ytau=ytau)
        p.yukawa = yukawa_terms(p, ew.H, ew.H, ytau.s, yb.s, yt.s)
        for name, expr in p.yukawa.items():
            p.add_term(expr, "yukawa", name)
    return p


def yukawa_terms(p, Hd, Hu, ye, yd, yu):
    """The single-generation Yukawa Lagrangian, one term per fermion.

    ``−y_e L̄ H_d e_R − y_d Q̄ H_d d_R − y_u Q̄ H̃_u u_R + h.c.`` with
    ``H̃ = (H⁰*, −H⁺*)`` written inline (CONVENTIONS.md). ``Hd``/``Hu`` are the
    doublets coupling to down-type/leptons and up-type quarks (both ``H`` in
    the SM; ``H1``/``H2`` in a type-II 2HDM). The couplings ``ye, yd, yu`` are
    real SymPy symbols.
    """
    i = p.idx[0]
    Ll, eR, QL, uR, dR = (p.fermions[k] for k in ("Ll", "eR", "QL", "uR", "dR"))
    Gp_d, H0_d = Hd.components
    Gp_u, H0_u = Hu.components
    nuL, eL = Ll.components
    nuLbar, eLbar = Ll.bar_components
    eRc, eRbar = eR.components[0], eR.bar_components[0]
    qL_u, qL_d = QL.components[:3], QL.components[3:]
    qLbar_u, qLbar_d = QL.bar_components[:3], QL.bar_components[3:]

    def colour_sum(bars, gamma, fields):
        return sum(Bilinear(bars[c][i], gamma, fields[c][i]) for c in range(3))

    L_e = -(ye * Gp_d * Bilinear(nuLbar[i], diracPR, eRc[i])
            + ye * H0_d * Bilinear(eLbar[i], diracPR, eRc[i]))
    L_e += -(ye * sp.conjugate(Gp_d) * Bilinear(eRbar[i], diracPL, nuL[i])
             + ye * sp.conjugate(H0_d) * Bilinear(eRbar[i], diracPL, eL[i]))

    L_d = -(yd * Gp_d * colour_sum(qLbar_u, diracPR, dR.components)
            + yd * H0_d * colour_sum(qLbar_d, diracPR, dR.components))
    L_d += -(yd * sp.conjugate(Gp_d) * colour_sum(dR.bar_components, diracPL, qL_u)
             + yd * sp.conjugate(H0_d) * colour_sum(dR.bar_components, diracPL, qL_d))

    L_u = -(yu * sp.conjugate(H0_u) * colour_sum(qLbar_u, diracPR, uR.components)
            + yu * (-sp.conjugate(Gp_u)) * colour_sum(qLbar_d, diracPR, uR.components))
    L_u += -(yu * H0_u * colour_sum(uR.bar_components, diracPL, qL_u)
             + yu * (-Gp_u) * colour_sum(uR.bar_components, diracPL, qL_d))
    return {"yukawa_tau": L_e, "yukawa_b": L_d, "yukawa_t": L_u}


def dirac_specs(p, masses=("MT", "MB", "MTA")):
    """The four Dirac fermions of one generation (ν_τ left-handed only)."""
    Ll, eR, QL, uR, dR = (p.fermions[k] for k in ("Ll", "eR", "QL", "uR", "dR"))
    t, tb, b, bb = sp.symbols("t tbar b bbar")
    ta, tap, vt, vtb = sp.symbols("ta tap vt vtbar")
    return [
        DiracSpec("t", QL.components[0], uR.components[0], t, tb, 6, sp.Rational(2, 3),
                  masses[0], "t~", color=3, width="WT",
                  copies=(*QL.components[1:3], *uR.components[1:])),
        DiracSpec("b", QL.components[3], dR.components[0], b, bb, 5, -sp.Rational(1, 3),
                  masses[1], "b~", color=3,
                  copies=(*QL.components[4:], *dR.components[1:])),
        DiracSpec("ta-", Ll.components[1], eR.components[0], ta, tap, 15, -1,
                  masses[2], "ta+"),
        DiracSpec("vt", Ll.components[0], None, vt, vtb, 16, 0, "ZERO", "vt~"),
    ]


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
    return [ExternalParameter(n, bench[n], positive=True, unit_dim=1)
            for n in ("WZ", "WW", "WH", "WT")]


# ------------------------------------------------------------------- build

def build(benchmark=None):
    p = pieces(benchmark, higgs=True)
    ew = p.ew
    model = Model("SM", gauge_groups=p.gauge_groups, fields=p.fields,
                  parameters=p.params, lagrangian=p.lagrangian())
    model.solve_tadpoles([ew.mu2])
    phys = to_physical_basis(model, ew)
    bosons = dict(h=phys.h, G0=phys.G0, Gp=phys.Gp, Gm=phys.Gm,
                  Z=phys.Z, A=phys.A, Wp=phys.Wp, Wm=phys.Wm)
    charges = {phys.h: 0, phys.G0: 0, phys.Gp: 1, phys.Gm: -1,
               phys.Z: 0, phys.A: 0, phys.Wp: 1, phys.Wm: -1}
    conjugates = {phys.Gp: phys.Gm, phys.Gm: phys.Gp, phys.Wp: phys.Wm, phys.Wm: phys.Wp}

    g, gp, v = ew.gw.s, ew.g1.s, ew.v.s
    MW = InternalParameter("MW", g * v / 2, positive=True, unit_dim=1)
    MZ = InternalParameter("MZ", sp.sqrt(g**2 + gp**2) * v / 2, positive=True, unit_dim=1)
    MH = InternalParameter("MH", sp.sqrt(2 * ew.lam.s) * v, positive=True, unit_dim=1)
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
    masses = {"m_h": e["MH"].expr, "m_W": e["MW"].expr, "m_Z": e["MZ"].expr,
              "m_t": bundle.pieces.masses["MT"].s, "m_b": bundle.pieces.masses["MB"].s,
              "m_tau": bundle.pieces.masses["MTA"].s}
    return standard_outputs(bundle, out_dir, "SM_UFO", masses)
