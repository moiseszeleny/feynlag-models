"""Type-I seesaw with three lepton generations and two right-handed neutrinos.
Parent + delta on ``models/sm`` at ``generations=3``; a sibling of ``seesaw_type1``.

    L ⊃ −Σ_{a,b} y_ν^{ab} L̄_a H̃ ν_R^b − ½ Σ_k M_k ν_R^{kT} C ν_R^k + h.c.,   a = e, μ, τ;  b, k = 1, 2

In the left-handed basis n = (ν_L, ν_R^c) the 5×5 mass matrix is
``M_ν = [[0, m_D], [m_D^T, M_R]]`` with the 3×2 ``m_D = y_ν v/√2`` and ``M_R = diag(M_1, M_2)``.
``rank(m_D M_R⁻¹ m_Dᵀ) ≤ 2``, so the lightest neutrino is massless and the other two light states
carry two independent mass splittings; that is what the one-generation ``seesaw_type1`` cannot do.

The quark sector is ``sm``'s three flavour-diagonal generations **without** CKM mixing, on
purpose: quark mixing does not enter the neutrino sector at tree level.

The Takagi factorisation is numeric at the benchmark: feynlag's ``diagonalize_takagi`` takes its
mpmath route (50 digits) for a numeric matrix larger than 2×2, because the exact one does not
finish on a generic 5×5 (FG-5, resolved in feynlag ``e34b356``).
"""

import sympy as sp

from feynlag import (
    Bilinear, MajoranaBilinear, MajoranaRotation, Model, ParameterSet, WeylFermion,
    diagonalize_takagi, diracC, diracPL, diracPR, fermion_mass_matrix,
    majorana_mass_matrix, seesaw_light_mass, seesaw_mass_matrix, to_physical_basis,
)

from feynlag_models import MODELS_DIR
from feynlag_models import metadata as md
from feynlag_models.bundle import ModelBundle
from feynlag_models.outputs import standard_outputs
from feynlag_models.tex import TEX, external, internal
from models.sm import model as sm

ID = "seesaw_type1_2n"
PARENT = "sm"

FLAVOURS = ("e", "mu", "tau")
N_L, N_R = 3, 2
ZERO_COUPLING = 1e-40   # the numeric Takagi works at 50 digits; smallest physical coupling here ~1e-29


def benchmark_point():
    return md.benchmark_inputs(MODELS_DIR / ID)


def yukawa_name(a, b):
    return f"yv_{FLAVOURS[a]}{b + 1}"


def build(benchmark=None):
    bench = benchmark_point() if benchmark is None else dict(benchmark)
    p = sm.pieces(bench, higgs=True, generations=3)
    ew = p.ew
    i, j = p.idx

    # --- delta: ν_R (2 flavours), 3×2 Dirac Yukawa via H̃, diagonal Majorana mass ---
    yv = sp.Matrix(N_L, N_R, lambda a, b: 0)
    yv_params = []
    for a in range(N_L):
        for b in range(N_R):
            par = external(yukawa_name(a, b), bench[yukawa_name(a, b)])
            yv_params.append(par)
            yv[a, b] = par.s
    MR = [external(f"MR{k + 1}", bench[f"MR{k + 1}"], positive=True, unit_dim=1)
          for k in range(N_R)]
    nuR = WeylFermion("nuR", reps={}, chirality="R", nflavors=N_R, component_names=["nuR"],
                      tex=r"\nu_R")
    Ll = p.fermions["Ll"]
    Gp, H0 = ew.H.components
    nuL, eL = Ll.components
    nuLbar, eLbar = Ll.bar_components
    nR, nRbar = nuR.components[0], nuR.bar_components[0]
    CPL = diracC * diracPL

    # integer flavour indices throughout (CONVENTIONS.md, three generations)
    LYukD = sp.S.Zero
    for a in range(N_L):
        for b in range(N_R):
            y, yc = yv[a, b], sp.conjugate(yv[a, b])
            LYukD += -(y * sp.conjugate(H0) * Bilinear(nuLbar[a], diracPR, nR[b])
                       + y * (-sp.conjugate(Gp)) * Bilinear(eLbar[a], diracPR, nR[b]))
            LYukD += -(yc * H0 * Bilinear(nRbar[b], diracPL, nuL[a])
                       + yc * (-Gp) * Bilinear(nRbar[b], diracPL, eL[a]))
    LMaj = sp.S.Zero
    for k in range(N_R):
        op = -sp.Rational(1, 2) * MR[k].s * MajoranaBilinear(nR[k], CPL, nR[k])
        LMaj += op + sp.conjugate(op)
    p.add_term(LYukD, "yukawa", "yukawa_nu")
    p.add_term(LMaj, "other", "majorana_mass")
    p.fields.append(nuR)
    p.fermions["nuR"] = nuR
    p.params += [*yv_params, *MR]

    model = Model(ID, gauge_groups=p.gauge_groups, fields=p.fields,
                  parameters=p.params, lagrangian=p.lagrangian())
    model.solve_tadpoles([ew.mu2])
    phys = to_physical_basis(model, ew, tex=TEX)

    # --- seesaw mass matrix (symbolic) ---------------------------------------
    # fermion_mass_matrix is square; no term carries nR[2], so its third column is zero
    mD_full = fermion_mass_matrix(LYukD, nuLbar, nR, model.vacuum, N_L, (i, j), gamma=diracPR)
    mD = mD_full[:, :N_R]
    MRmat = majorana_mass_matrix(LMaj, nR, model.vacuum, N_R, (i, j), gamma=CPL)
    Mnu = seesaw_mass_matrix(mD, MRmat)
    m_light_approx = seesaw_light_mass(mD, MRmat)

    # --- numeric Takagi at the benchmark ---------------------------------------
    numeric = {ew.v.s: bench["v"], **{par.s: bench[par.name] for par in (*yv_params, *MR)}}
    Mn = Mnu.applyfunc(lambda x: sp.nsimplify(x.subs(numeric), rational=True))
    U, Dm = diagonalize_takagi(Mn)   # numeric Mn larger than 2×2 → mpmath at 50 digits
    masses = [float(Dm[k, k]) for k in range(N_L + N_R)]   # increasing
    light, heavy = list(range(N_L)), list(range(N_L, N_L + N_R))

    chiL, chiR = sp.IndexedBase("chiL"), sp.IndexedBase("chiR")
    chiLbar, chiRbar = sp.IndexedBase("chiLbar"), sp.IndexedBase("chiRbar")
    rot = MajoranaRotation(U, nuL, nR, nuLbar, nRbar, chiL, chiR, chiLbar, chiRbar, n_L=N_L)

    bosons = dict(h=phys.h, G0=phys.G0, Gp=phys.Gp, Gm=phys.Gm,
                  Z=phys.Z, A=phys.A, Wp=phys.Wp, Wm=phys.Wm)
    charges = {phys.h: 0, phys.G0: 0, phys.Gp: 1, phys.Gm: -1,
               phys.Z: 0, phys.A: 0, phys.Wp: 1, phys.Wm: -1}
    conjugates = {phys.Gp: phys.Gm, phys.Gm: phys.Gp, phys.Wp: phys.Wm, phys.Wm: phys.Wp}

    g, gp, v = ew.gw.s, ew.g1.s, ew.v.s
    MW = internal("MW", g * v / 2, positive=True, unit_dim=1)
    MZ = internal("MZ", sp.sqrt(g**2 + gp**2) * v / 2, positive=True, unit_dim=1)
    MH = internal("MH", sp.sqrt(2 * ew.lam.s) * v, positive=True, unit_dim=1)
    params = ParameterSet(*p.params, *sm.width_params(bench), MW, MZ, MH)

    # neutrinos are Majorana → not exported (FG-3)
    dirac = [d for d in sm.dirac_specs(p) if d.name not in ("ve", "vm", "vt")]

    return ModelBundle(
        id=ID, model=model, pieces=p, bosons=bosons, cmap=phys.cmap,
        charges=charges, conjugates=conjugates, params=params, benchmark=bench,
        dirac=dirac, boson_particles=sm.ew_boson_particles(bosons),
        goldstones=(phys.G0, phys.Gp, phys.Gm),
        extra=dict(ew=ew, yv=yv, yv_params=yv_params, MR=MR, nuR=nuR,
                   LYukD=LYukD, LMaj=LMaj, CPL=CPL, mD_full=mD_full, mD=mD, MRmat=MRmat,
                   Mnu=Mnu, Mn=Mn, m_light_approx=m_light_approx, U=U, D=Dm, masses=masses,
                   light=light, heavy=heavy, rot=rot, chi=(chiL, chiR, chiLbar, chiRbar),
                   MW=MW, MZ=MZ, MH=MH, ufo=False),
    )


def physical_neutrino_lagrangian(bundle):
    """Yukawa + gauge sectors with the weak neutrinos rotated to the Majorana χ_k.

    Every flavour index is already an integer, so ``apply`` gets no index symbols: passing
    ``pieces.idx`` would sum each term once per index combination.
    """
    return bundle.extra["rot"].apply(bundle.physical_fermion_lagrangian(), (), 1)


def _state_tex(k):
    return rf"\nu_{k + 1}" if k < N_L else f"N_{k - N_L + 1}"


def majorana_vertex_markdown(bundle):
    """The mass-basis neutrino couplings as a numeric table at the benchmark.

    The Majorana states have no Dirac assignment, so they are absent from the generic
    fermion table (FG-3), and the Takagi rotation is numeric: magnitudes are printed.
    """
    from feynlag import extract_fermion_vertices
    from feynlag_models.outputs import numeric_fermion_markdown

    e = bundle.extra
    chiL, chiR, chiLbar, chiRbar = e["chi"]
    names = {}
    for base, bar in ((chiL, False), (chiR, False), (chiLbar, True), (chiRbar, True)):
        for k in range(N_L + N_R):
            names[(base, k)] = rf"\bar{{{_state_tex(k)}}}" if bar else _state_tex(k)
    # charged-lepton legs by flavour (the generic fallback names by base, one generation)
    Ll, eR = bundle.pieces.fermions["Ll"], bundle.pieces.fermions["eR"]
    for base, bar in ((Ll.components[1], False), (Ll.bar_components[1], True),
                      (eR.components[0], False), (eR.bar_components[0], True)):
        for a, tex in enumerate(("e", r"\mu", r"\tau")):
            names[(base, a)] = rf"\bar{{{tex}}}" if bar else tex
    table = extract_fermion_vertices(physical_neutrino_lagrangian(bundle), bundle.boson_list)
    vals = bundle.values()
    kept = {}
    for key, orders in table.items():
        if not any(x.base in (chiL, chiR, chiLbar, chiRbar) for x in (key[0], key[2])):
            continue
        orders = {n: {b: c for b, c in by_boson.items()
                      if abs(complex(sp.N(sp.sympify(c).subs(vals)))) > ZERO_COUPLING}
                  for n, by_boson in orders.items()}
        orders = {n: d for n, d in orders.items() if d}
        if orders:
            kept[key] = orders
    note = (r"$`\nu_{1,2,3}`$ and $`N_{1,2}`$ are the light and heavy Majorana mass eigenstates "
            r"($`\chi_k`$ in the code), ordered by mass; $`\nu_1`$ is massless. The Takagi rotation is "
            "solved numerically at the benchmark, so these couplings have no closed form here; "
            "magnitudes are given instead, and the tests pin them against Atre et al. Eq. (2.5) "
            "(`tests/test_l2_literature.py`). Couplings below $`10^{-40}`$ vanish at the 50-digit "
            r"working precision (for example $`Z\bar\nu_i\nu_j`$ with $`i \ne j`$) and are omitted.")
    table = kept
    return numeric_fermion_markdown(bundle, table, names,
                                    "Majorana neutrino vertices (numeric)", note)


def outputs(bundle, out_dir):
    e = bundle.extra
    masses = {"$m_h$": e["MH"].expr, "$m_W$": e["MW"].expr, "$m_Z$": e["MZ"].expr}
    # rank(M_ν) = 4 exactly, so m_ν1 = 0; the Takagi returns it as ~1e-49 working-precision noise
    masses[rf"$m_{{{_state_tex(0)}}}$ (exact, rank 2)"] = sp.S.Zero
    for k in range(1, N_L + N_R):
        masses[rf"$m_{{{_state_tex(k)}}}$ (Takagi)"] = sp.Float(e["masses"][k], 15)
    return standard_outputs(bundle, out_dir, "SEESAW_TYPE1_2N_UFO", masses, ufo=False,
                            extra_vertex_sections=[majorana_vertex_markdown(bundle)])
