"""UFO export of a :class:`~feynlag_models.bundle.ModelBundle` (unitary gauge).

Follows the validated recipe of feynlag's ``scripts/export_sm_ufo.py`` (the
MadGraph benchmark): bosonic vertices straight from ``Model.vertices``, the
triple-gauge couplings from ``cubic_couplings`` with the documented sign flip
for the complex ``W±`` basis, and flavour-resolved FFS/FFV vertices flattened
from ``extract_fermion_vertices``.

Not exported (documented limitation, see FEYNLAG_GAPS.md / NEXT_STEPS): quartic
gauge self-couplings in the rotated basis, Goldstone vertices (unitary gauge),
Majorana-fermion vertices.
"""

from pathlib import Path

import sympy as sp

from feynlag import (DiracGamma, cubic_couplings, diracPL, diracPR,
                     verify_ufo_numeric)
from feynlag.export.ufo import write_ufo

_mu = sp.Symbol("mu", integer=True)
LEFT_STRUCTURES = {diracPL, DiracGamma(_mu) * diracPL}
RIGHT_STRUCTURES = {diracPR, DiracGamma(_mu) * diracPR}


def _is_left(gamma):
    g = gamma
    if g == diracPL or g == diracPR:
        return g == diracPL
    # γ^μ P_{L,R} with whatever index symbol
    if g.is_Mul and diracPL in g.args:
        return True
    if g.is_Mul and diracPR in g.args:
        return False
    raise ValueError(f"unsupported Dirac structure for UFO export: {gamma}")


def _chirality_of(gamma):
    return "left" if _is_left(gamma) else "right"


def flatten_fermion_vertices(table, dirac_specs, bosons, drop=()):
    """``extract_fermion_vertices`` output → ``write_ufo(fermion_vertices=…)`` dicts.

    Groups the chiral keys ``(bar, Γ, field)`` of one Dirac pair and one boson
    into a single UFO vertex with ``left``/``right`` slots. Keys whose legs are
    not in any ``DiracSpec`` (e.g. Majorana states) are returned in ``skipped``.
    """
    base_map, color_of, ignored = {}, {}, set()
    for d in dirac_specs:
        base_map.update(d.bases)
        color_of[d.particle] = color_of[d.antiparticle] = d.color
        ignored |= d.ignored_bases
    merged, skipped = {}, []
    def spec_key(leg):
        # flavour-resolved specs are keyed by (base, integer index)
        flavoured = (leg.base, leg.indices[0])
        return flavoured if flavoured in base_map else leg.base

    for (bar, gamma, fld), by_n in table.items():
        if bar.base in ignored or fld.base in ignored:
            continue
        bar_base, fld_base = spec_key(bar), spec_key(fld)
        if bar_base not in base_map or fld_base not in base_map:
            skipped.append((bar, gamma, fld))
            continue
        for boson_tuple, coeff in by_n.get(1, {}).items():
            boson = boson_tuple[0]
            if boson in drop or boson not in bosons:
                continue
            coeff = sp.simplify(coeff)
            if coeff == 0:
                continue
            key = (base_map[bar_base], base_map[fld_base], boson)
            slot = _chirality_of(gamma)
            colored = color_of[key[0]] != 1 and color_of[key[1]] != 1
            entry = merged.setdefault(key, {"bar": key[0], "field": key[1],
                                            "bosons": (boson,), "left": 0, "right": 0,
                                            "color": "Identity(1,2)" if colored else "1"})
            entry[slot] = sp.simplify(entry[slot] + coeff)
    return list(merged.values()), skipped


def triple_gauge(bundle):
    """``{(A,Wp,Wm): gAWW, (Z,Wp,Wm): gZWW}`` with the benchmark-validated sign."""
    p = bundle.pieces
    g, gp = p.gw.s, p.g1.s
    cw, sw = g / sp.sqrt(g**2 + gp**2), gp / sp.sqrt(g**2 + gp**2)
    b = bundle.bosons
    Uc = sp.Matrix([[1 / sp.sqrt(2), 1 / sp.sqrt(2), 0, 0],
                    [sp.I / sp.sqrt(2), -sp.I / sp.sqrt(2), 0, 0],
                    [0, 0, cw, sw]])
    cubic = cubic_couplings(p.SU2L, physical=[b["Wp"], b["Wm"], b["Z"], b["A"]], U=Uc)
    # sign flip: see CONVENTIONS.md ("Feynman rules and export") and feynlag's
    # docs/benchmark.md — the complex-W± basis comes out opposite to MG's VVV1.
    return {(b["A"], b["Wp"], b["Wm"]): -sp.simplify(cubic.get((b["A"], b["Wp"], b["Wm"]), 0)),
            (b["Z"], b["Wp"], b["Wm"]): -sp.simplify(cubic.get((b["Z"], b["Wp"], b["Wm"]), 0))}


def bosonic_vertices(bundle, sectors=("potential", "kinetic")):
    """Scalar/gauge vertices from the physical Lagrangian, Goldstone legs dropped."""
    verts = []
    for sector in sectors:
        verts += bundle.model.vertices(bundle.boson_list, sector=sector,
                                       conjugate_map=bundle.cmap,
                                       simplifier=sp.simplify)
    drop = set(bundle.goldstones)
    return [v for v in verts if not (set(v.particles) & drop)]


def export_ufo(bundle, path, model_name):
    """Write the UFO directory and return ``(path, report, skipped_fermion_keys)``."""
    drop = set(bundle.goldstones)
    particles = [p for p in bundle.ufo_particles() if p.symbol not in drop]
    table = bundle.fermion_table()
    fermion_vertices, skipped = flatten_fermion_vertices(
        table, bundle.dirac, set(bundle.boson_list), drop=drop)
    write_ufo(path, model_name, bundle.params, particles,
              bosonic_vertices=bosonic_vertices(bundle),
              vvv=triple_gauge(bundle),
              fermion_vertices=fermion_vertices)
    report = verify_ufo_numeric(path)
    return path, report, skipped


_LORENTZ_CLASS = {"FFSL": "FFS", "FFSR": "FFS", "FFVL": "FFV", "FFVR": "FFV"}


def exported_vertex_classes(path):
    """Vertex classes present in a written UFO, read from its ``vertices.py``."""
    import re
    names = set(re.findall(r"L\.([A-Z]+\d*)", (Path(path) / "vertices.py").read_text()))
    classes = set()
    for n in names:
        base = _LORENTZ_CLASS.get(n, re.sub(r"\d+$", "", n))
        classes.add("FFFF" if base.startswith("FFFF") else base)
    return classes
