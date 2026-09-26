"""Standard Model with three generations and CKM quark mixing.

Parent + delta on ``models/sm``: the same gauge and Higgs sector with all three
fermion generations (``sm.pieces(generations=3)``), and the down-type Yukawa
replaced by the non-diagonal

    Y_d = V diag(y_d, y_s, y_b),     y_f = √2 m_f / v          (CONVENTIONS.md)

in the weak basis where Y_u and Y_e are diagonal. ``V`` is feynlag's exact PDG
standard parametrization (``standard_ckm``; PDG 2024 Eq. 12.3). The mass basis
is reached by the unitary rotation d'_L = V d_L, registered on the ``Model``
for every colour copy (fields and bars separately). The rotation uses the
trigonometric entries of ``V``, so the neutral-current and Higgs couplings
between different down flavours cancel exactly (GIM), and the charged current
carries V_ij. Both are derived, not imposed.

The mass-basis d_L are auxiliary single-component Weyl fields ``dLm1..3`` (one
per colour, three flavours each), never passed to ``Model``: they exist only
so that feynlag's ``bar_partner`` pairs them for vertex extraction and export.
Neutrinos are massless and there is no lepton mixing (it can be rotated away).
"""

import math

import sympy as sp

from feynlag import (InternalParameter, Model, ParameterSet, Rotation, WeylFermion,
                     standard_ckm, to_physical_basis)

from feynlag_models import MODELS_DIR
from feynlag_models import metadata as md
from feynlag_models.bundle import ModelBundle
from feynlag_models.outputs import standard_outputs
from models.sm import model as sm

ID = "sm_ckm"
PARENT = "sm"

#: benchmark keys of the CKM inputs → feynlag parameter names
CKM_INPUTS = {"s12": "th12", "s13": "th13", "s23": "th23", "deltaCP": "deltaCP"}


def benchmark_point():
    return md.benchmark_inputs(MODELS_DIR / ID)


def ckm(bench):
    """``standard_ckm`` with its four externals set from the benchmark.

    Returns ``(params, V, V_expr)``: the 13 parameters, the matrix of internal
    symbols ``Vud…Vtb`` and the same matrix written in the angles.
    """
    params, V = standard_ckm()
    by_name = {q.name: q for q in params}
    for key, name in CKM_INPUTS.items():
        value = bench[key]
        by_name[name].value = math.asin(value) if key != "deltaCP" else value
    V_expr = V.xreplace({q.s: q.expr for q in params if getattr(q, "expr", None) is not None})
    return params, V, V_expr


def mass_basis_down_left():
    """Auxiliary mass-basis ``d_L`` handles, one ``IndexedBase`` per colour."""
    fields = [WeylFermion(f"dLm{c}", reps={}, chirality="L", nflavors=3,
                          component_names=[f"dLm_{c}"],
                          component_tex=[f"{{d'}}_L^{{{c}}}"]) for c in (1, 2, 3)]
    return [f.components[0] for f in fields], [f.bar_components[0] for f in fields]


def build(benchmark=None):
    bench = benchmark_point() if benchmark is None else dict(benchmark)
    p = sm.pieces(bench, higgs=True, generations=3)
    ew = p.ew

    # --- delta: CKM parameters and the non-diagonal down Yukawa ------------
    ckm_params, V, V_expr = ckm(bench)
    ys = p.yukawa_params
    Yd = V_expr * sp.diag(ys["yd"].s, ys["ys"].s, ys["yb"].s)
    L_down = sm.yukawa_terms(p, ew.H, ew.H, sp.zeros(3), Yd, sp.zeros(3))["yukawa_down"]
    p.replace_term("yukawa_down", L_down)
    p.yukawa["yukawa_down"] = L_down
    p.params += ckm_params

    model = Model(ID, gauge_groups=p.gauge_groups, fields=p.fields,
                  parameters=p.params, lagrangian=p.lagrangian())
    model.solve_tadpoles([ew.mu2])
    phys = to_physical_basis(model, ew, gm_tex="G^-")

    # --- mass basis of d_L: d'_L = V d_L, i.e. new = V† old -------------------
    QL = p.fermions["QL"]
    dLm, dLm_bar = mass_basis_down_left()
    rotations = []
    for c in range(3):
        old = [QL.components[3 + c][k] for k in range(3)]
        new = [dLm[c][k] for k in range(3)]
        rotations.append(Rotation(old, new, V_expr.conjugate().T, kind="unitary"))
        old_bar = [QL.bar_components[3 + c][k] for k in range(3)]
        new_bar = [dLm_bar[c][k] for k in range(3)]
        rotations.append(Rotation(old_bar, new_bar, V_expr.T, kind="unitary"))
    for rot in rotations:
        model.rotate(rot)

    bosons = dict(h=phys.h, G0=phys.G0, Gp=phys.Gp, Gm=phys.Gm,
                  Z=phys.Z, A=phys.A, Wp=phys.Wp, Wm=phys.Wm)
    charges = {phys.h: 0, phys.G0: 0, phys.Gp: 1, phys.Gm: -1,
               phys.Z: 0, phys.A: 0, phys.Wp: 1, phys.Wm: -1}
    conjugates = {phys.Gp: phys.Gm, phys.Gm: phys.Gp, phys.Wp: phys.Wm, phys.Wm: phys.Wp}

    g, gp, v = ew.gw.s, ew.g1.s, ew.v.s
    MW = InternalParameter("MW", g * v / 2, positive=True, unit_dim=1)
    MZ = InternalParameter("MZ", sp.sqrt(g**2 + gp**2) * v / 2, positive=True, unit_dim=1)
    MH = InternalParameter("MH", sp.sqrt(2 * ew.lam.s) * v, positive=True, unit_dim=1)
    params = ParameterSet(*p.params, *sm.width_params(bench), MW, MZ, MH)

    return ModelBundle(
        id=ID, model=model, pieces=p, bosons=bosons, cmap=phys.cmap,
        charges=charges, conjugates=conjugates, params=params, benchmark=bench,
        dirac=sm.dirac_specs(p, down_left=dLm),
        boson_particles=sm.ew_boson_particles(bosons),
        goldstones=(phys.G0, phys.Gp, phys.Gm),
        extra=dict(ew=ew, MW=MW, MZ=MZ, MH=MH, V=V, V_expr=V_expr, Yd=Yd,
                   ckm_params=ckm_params, rotations=rotations,
                   dLm=dLm, dLm_bar=dLm_bar),
    )


def outputs(bundle, out_dir):
    e = bundle.extra
    masses = {"$m_h$": e["MH"].expr, "$m_W$": e["MW"].expr, "$m_Z$": e["MZ"].expr}
    labels = {"MU": "m_u", "MC": "m_c", "MT": "m_t", "MD": "m_d", "MS": "m_s",
              "MB": "m_b", "ME": "m_e", "MMU": r"m_\mu", "MTA": r"m_\tau"}
    for name, tex in labels.items():
        masses[f"${tex}$"] = bundle.pieces.masses[name].s
    for row, up in zip(e["V"].tolist(), ("u", "c", "t")):
        for elem, down in zip(row, ("d", "s", "b")):
            masses[rf"$\vert V_{{{up}{down}}}\vert$"] = sp.Abs(bundle.params[str(elem)].expr)
    return standard_outputs(bundle, out_dir, "SM_CKM_UFO", masses)
