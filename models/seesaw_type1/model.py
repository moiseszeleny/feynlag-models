"""Type-I seesaw: SM + one right-handed neutrino ν_R with a Dirac Yukawa and a
Majorana mass. Parent + delta on ``models/sm``.

    L ⊃ −y_ν L̄ H̃ ν_R − ½ M_R ν_Rᵀ C ν_R + h.c.

After EWSB, in the left-handed basis n = (ν_L, ν_R^c) the symmetric mass matrix
``M_ν = [[0, m_D], [m_D, M_R]]`` with ``m_D = y_ν v/√2`` is Takagi-diagonalised
(``M_ν = U D Uᵀ``); for ``M_R ≫ m_D`` the light state has ``m_ν ≈ −m_D²/M_R``
and the heavy one ``≈ M_R``, mixed by ``V ≈ m_D/M_R``. The physical heavy-neutrino
couplings come from feynlag's ``MajoranaRotation`` (the mass eigenstates are
Majorana, mixing ν_L with ν_R^c), following ``examples/sm_seesaw.py``.
"""

import sympy as sp

from feynlag import (
    Bilinear, ExternalParameter, InternalParameter, MajoranaBilinear,
    MajoranaRotation, Model, ParameterSet, WeylFermion, diagonalize_takagi,
    diracC, diracPL, diracPR, fermion_mass_matrix, majorana_mass_matrix,
    seesaw_light_mass, seesaw_mass_matrix, to_physical_basis,
)

from feynlag_models import MODELS_DIR
from feynlag_models import metadata as md
from feynlag_models.bundle import ModelBundle
from feynlag_models.outputs import standard_outputs
from models.sm import model as sm

ID = "seesaw_type1"
PARENT = "sm"


def benchmark_point():
    return md.benchmark_inputs(MODELS_DIR / ID)


def _num(x):
    return complex(sp.N(x))


def build(benchmark=None):
    bench = benchmark_point() if benchmark is None else dict(benchmark)
    p = sm.pieces(bench, higgs=True)
    ew = p.ew
    i, j = p.idx

    # --- delta: ν_R, Dirac Yukawa via H̃, Majorana mass ------------------
    yv = ExternalParameter("yv", bench["yv"], positive=True)
    MR = ExternalParameter("MR", bench["MR"], positive=True, unit_dim=1)
    nuR = WeylFermion("nuR", reps={}, chirality="R", nflavors=1, component_names=["nuR"],
                      tex=r"\nu_R")
    Ll = p.fermions["Ll"]
    Gp, H0 = ew.H.components
    nuL, eL = Ll.components
    nuLbar, eLbar = Ll.bar_components
    nR, nRbar = nuR.components[0], nuR.bar_components[0]
    CPL = diracC * diracPL

    LYukD = -(yv.s * sp.conjugate(H0) * Bilinear(nuLbar[i], diracPR, nR[j])
              + yv.s * (-sp.conjugate(Gp)) * Bilinear(eLbar[i], diracPR, nR[j]))
    LYukD += -(yv.s * H0 * Bilinear(nRbar[j], diracPL, nuL[i])
               + yv.s * (-Gp) * Bilinear(nRbar[j], diracPL, eL[i]))
    op = -sp.Rational(1, 2) * MR.s * MajoranaBilinear(nR[i], CPL, nR[j])
    LMaj = op + sp.conjugate(op)
    p.add_term(LYukD, "yukawa", "yukawa_nu")
    p.add_term(LMaj, "other", "majorana_mass")
    p.fields.append(nuR)
    p.fermions["nuR"] = nuR
    p.params += [yv, MR]

    model = Model(ID, gauge_groups=p.gauge_groups, fields=p.fields,
                  parameters=p.params, lagrangian=p.lagrangian())
    model.solve_tadpoles([ew.mu2])
    phys = to_physical_basis(model, ew, gm_tex="G^-")

    # --- seesaw mass matrix (symbolic) and Takagi at the benchmark ----------
    mD = fermion_mass_matrix(LYukD, nuLbar, nR, model.vacuum, 1, (i, j), gamma=diracPR)
    MRmat = majorana_mass_matrix(LMaj, nR, model.vacuum, 1, (i, j), gamma=CPL)
    Mnu = seesaw_mass_matrix(mD, MRmat)
    m_light_approx = seesaw_light_mass(mD, MRmat)[0, 0]

    numeric = {yv.s: bench["yv"], ew.v.s: bench["v"], MR.s: bench["MR"]}
    Mn = sp.Matrix(2, 2, lambda a, b: sp.nsimplify(Mnu[a, b].subs(numeric), rational=True))
    U, Dm = diagonalize_takagi(Mn)
    masses = [abs(_num(Dm[k, k])) for k in range(2)]
    light = 0 if masses[0] < masses[1] else 1
    heavy = 1 - light

    chiL, chiR = sp.IndexedBase("chiL"), sp.IndexedBase("chiR")
    chiLbar, chiRbar = sp.IndexedBase("chiLbar"), sp.IndexedBase("chiRbar")
    rot = MajoranaRotation(U, nuL, nR, nuLbar, nRbar, chiL, chiR, chiLbar, chiRbar, n_L=1)

    bosons = dict(h=phys.h, G0=phys.G0, Gp=phys.Gp, Gm=phys.Gm,
                  Z=phys.Z, A=phys.A, Wp=phys.Wp, Wm=phys.Wm)
    charges = {phys.h: 0, phys.G0: 0, phys.Gp: 1, phys.Gm: -1,
               phys.Z: 0, phys.A: 0, phys.Wp: 1, phys.Wm: -1}
    conjugates = {phys.Gp: phys.Gm, phys.Gm: phys.Gp, phys.Wp: phys.Wm, phys.Wm: phys.Wp}

    g, gp, v = ew.gw.s, ew.g1.s, ew.v.s
    MW = InternalParameter("MW", g * v / 2, positive=True, unit_dim=1)
    MZ = InternalParameter("MZ", sp.sqrt(g**2 + gp**2) * v / 2, positive=True, unit_dim=1)
    MH = InternalParameter("MH", sp.sqrt(2 * ew.lam.s) * v, positive=True, unit_dim=1)
    mDsym = InternalParameter("mD", yv.s * v / sp.sqrt(2), positive=True, unit_dim=1)
    # exact 2×2 Takagi singular values of [[0, m_D], [m_D, M_R]]; the light one is
    # written in the rationalised form 2m_D²/(√(M_R²+4m_D²) + M_R) (identical to
    # (√(M_R²+4m_D²) − M_R)/2) so the UFO param card does not lose ~10 digits to cancellation
    MN1 = InternalParameter("MN1", 2 * mDsym.s**2 / (sp.sqrt(MR.s**2 + 4 * mDsym.s**2) + MR.s), positive=True, unit_dim=1)
    MN2 = InternalParameter("MN2", (sp.sqrt(MR.s**2 + 4 * mDsym.s**2) + MR.s) / 2, positive=True, unit_dim=1)
    params = ParameterSet(*p.params, *sm.width_params(bench), MW, MZ, MH, mDsym, MN1, MN2)

    dirac = [d for d in sm.dirac_specs(p) if d.name != "vt"]   # neutrinos are Majorana → not exported (FG-3)

    return ModelBundle(
        id=ID, model=model, pieces=p, bosons=bosons, cmap=phys.cmap,
        charges=charges, conjugates=conjugates, params=params, benchmark=bench,
        dirac=dirac, boson_particles=sm.ew_boson_particles(bosons),
        goldstones=(phys.G0, phys.Gp, phys.Gm),
        extra=dict(ew=ew, yv=yv, MR=MR, nuR=nuR, LYukD=LYukD, LMaj=LMaj, CPL=CPL,
                   mD=mD, MRmat=MRmat, Mnu=Mnu, m_light_approx=m_light_approx,
                   U=U, D=Dm, masses=masses, light=light, heavy=heavy,
                   rot=rot, chi=(chiL, chiR, chiLbar, chiRbar),
                   MW=MW, MZ=MZ, MH=MH, mDsym=mDsym, MN1=MN1, MN2=MN2, ufo=False),
    )


def physical_neutrino_lagrangian(bundle):
    """Yukawa + gauge sectors with the weak neutrinos rotated to the Majorana χ_k."""
    e = bundle.extra
    L = bundle.physical_fermion_lagrangian()
    return e["rot"].apply(L, bundle.pieces.idx, 1)


def majorana_vertex_markdown(bundle):
    """The mass-basis neutrino couplings as a numeric table at the benchmark.

    The Majorana states have no Dirac assignment, so they are absent from the generic
    fermion table (FG-3), and the Takagi rotation is solved numerically at the benchmark:
    symbolically these coefficients are numeric radicals, not formulas. Their magnitudes
    are what the L2 tests check against Atre et al. Eq. (2.5), so the page prints those.
    """
    from feynlag import extract_fermion_vertices
    from feynlag_models.outputs import numeric_fermion_markdown

    e = bundle.extra
    chiL, chiR, chiLbar, chiRbar = e["chi"]
    light, heavy = e["light"], e["heavy"]
    names = {}
    for base, bar in ((chiL, False), (chiR, False), (chiLbar, True), (chiRbar, True)):
        for k, tex in ((light, r"\nu"), (heavy, "N")):
            names[(base, k)] = rf"\bar{{{tex}}}" if bar else tex
    table = extract_fermion_vertices(physical_neutrino_lagrangian(bundle), bundle.boson_list)
    table = {k: v for k, v in table.items()
             if any(x.base in (chiL, chiR, chiLbar, chiRbar) for x in (k[0], k[2]))}
    ratio = float(bundle.values()[e["mDsym"].s] / bundle.values()[e["MR"].s])
    mantissa, exponent = f"{ratio:.2e}".split("e")
    note = (r"$`\nu`$ and $N$ are the light and heavy Majorana mass eigenstates ($`\chi_k`$ in the code). "
            "The mixing is a Takagi rotation solved numerically at the benchmark, so these couplings have no "
            "closed form here; magnitudes are given instead, and the tests pin them against Atre et al. "
            "Eq. (2.5) (`tests/test_l2_literature.py`). The heavy state is suppressed by "
            rf"$`V \approx m_D/M_R = {mantissa} \times 10^{{{int(exponent)}}}`$ relative to the light one.")
    return numeric_fermion_markdown(bundle, table, names,
                                    "Majorana neutrino vertices (numeric)", note)


def outputs(bundle, out_dir):
    e = bundle.extra
    masses = {"$m_h$": e["MH"].expr, "$m_W$": e["MW"].expr, "$m_Z$": e["MZ"].expr,
              "$m_D$": e["mDsym"].expr, r"$m_\nu$ (exact)": e["MN1"].expr, "$m_N$ (exact)": e["MN2"].expr,
              r"$m_\nu$ (seesaw approximation)": -e["m_light_approx"]}
    return standard_outputs(bundle, out_dir, "SEESAW_TYPE1_UFO", masses, ufo=False,
                            extra_vertex_sections=[majorana_vertex_markdown(bundle)])
