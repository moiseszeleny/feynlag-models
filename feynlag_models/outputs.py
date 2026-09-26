"""Standard ``outputs/`` content shared by every model."""

import sympy as sp

from feynlag import latex_feynman_table

from .tex import TEX
from .ufo import export_ufo


def tex_names(bundle):
    """``{Symbol: LaTeX}`` for every parameter, from :data:`feynlag_models.tex.TEX`.

    The symbols carry the same tex themselves; an explicit ``symbol_names`` map still wins in
    ``sympy.latex``, which keeps these tables independent of how a symbol was declared.
    """
    return {p.symbol: TEX[p.name] for p in bundle.params if p.name in TEX}


def _math(expr, symbol_names):
    """Inline Markdown math for a table cell (a bare ``|`` would split the cell)."""
    tex = sp.latex(expr, symbol_names=symbol_names)
    tex = tex.replace(r"\left|", r"\left\vert ").replace(r"\right|", r"\right\vert ")
    # GitHub double-escapes < and > inside math (CONVENTIONS.md, "Markdown")
    tex = tex.replace("<", r" \lt ").replace(">", r" \gt ")
    return f"$`{tex}`$"


_VECTOR_KEYS = ("A", "Z", "Wp", "Wm")
#: section order and titles of the vertex classes (V = vector, S = scalar)
CLASS_TITLES = {
    "SSS": "Cubic scalar", "SSSS": "Quartic scalar", "VSS": "Vector and two scalars",
    "VVS": "Two vectors and a scalar", "VVSS": "Two vectors and two scalars",
}
#: LaTeX names of the Dirac fermions, keyed by the ``DiracSpec.name`` (the UFO name)
FERMION_TEX = {
    "u": "u", "c": "c", "t": "t", "d": "d", "s": "s", "b": "b",
    "e-": "e", "mu-": r"\mu", "ta-": r"\tau",
    "ve": r"\nu_e", "vm": r"\nu_\mu", "vt": r"\nu_\tau",
}
#: a rule whose TeX is longer than this leaves the table for a display block
LONG_TEX = 140
#: fermion rules carry two projectors, so they get more room before being displayed
FERMION_LONG_TEX = 210


def field_names(bundle):
    """``{field Symbol: LaTeX}`` for the bundle's physical bosons (matched by identity)."""
    return {sym: TEX.get(sym.name, rf"\mathrm{{{key}}}") for key, sym in bundle.bosons.items()}


def _rule_tex(expr, symbol_names, fields):
    """LaTeX of a Feynman-rule coefficient: physics parameter names, momenta as ``p_{field}``."""
    names = dict(symbol_names)
    swaps = {}
    for atom in expr.atoms(sp.core.function.AppliedUndef):
        if atom.func.__name__ == "p" and atom.args[0] in fields:
            dummy = sp.Symbol("p_" + str(atom.args[0]))
            names[dummy] = "{p_{" + fields[atom.args[0]] + "}}"
            swaps[atom] = dummy
    tex = sp.latex(expr.xreplace(swaps), symbol_names=names)
    tex = tex.replace(r"\left|", r"\left\vert ").replace(r"\right|", r"\right\vert ")
    # GitHub double-escapes < and > inside math (CONVENTIONS.md, "Markdown")
    return tex.replace("<", r" \lt ").replace(">", r" \gt ")


def fermion_names(bundle):
    """``{Symbol: LaTeX}`` for the particle and antiparticle symbols of every ``DiracSpec``."""
    out = {}
    for spec in bundle.dirac:
        tex = FERMION_TEX.get(spec.name, rf"\mathrm{{{spec.name}}}")
        out[spec.particle] = tex
        base, _, sub = tex.partition("_")
        out[spec.antiparticle] = rf"\bar{{{base}}}" + (f"_{sub}" if sub else "")
    return out


def fermion_base_names(bundle):
    """``{IndexedBase: LaTeX}`` for the Weyl components of every ``DiracSpec`` and their bars."""
    from feynlag import bar_partner
    out = {}
    for spec in bundle.dirac:
        tex = FERMION_TEX.get(spec.name, rf"\mathrm{{{spec.name}}}")
        base, _, sub = tex.partition("_")
        bar = rf"\bar{{{base}}}" + (f"_{sub}" if sub else "")
        for component in (spec.left, spec.right):
            if component is None:
                continue
            out[component] = tex
            out[bar_partner(component)] = bar
    return out


def _chiral_rule(left, right, vector, symbol_names):
    """``i γ^μ (c_L P_L + c_R P_R)`` (or without ``γ^μ`` for a scalar), as LaTeX."""
    gamma = r"\gamma^\mu " if vector else ""
    if left == right:                               # vector-like: the projectors sum to 1
        return rf"i {gamma}\left({sp.latex(left, symbol_names=symbol_names)}\right)"
    parts = [(c, proj) for c, proj in ((left, "P_L"), (right, "P_R")) if c != 0]
    if len(parts) == 1:                             # purely left- or right-handed
        coeff, proj = parts[0]
        return rf"i {gamma}\left({sp.latex(coeff, symbol_names=symbol_names)}\right) {proj}"
    terms = [rf"\left({sp.latex(c, symbol_names=symbol_names)}\right) {proj}" for c, proj in parts]
    return rf"i {gamma}\left[{' + '.join(terms)}\right]"


def _refined(expr, assumption):
    """``simplify``, with the mixing angles' first-quadrant assumption applied if there is one.

    The ``Abs`` that carries the assumption (``|cos beta|``) appears while simplifying, so the
    refinement goes between two ``simplify`` passes.
    """
    expr = sp.simplify(expr)
    if assumption is not None:
        expr = sp.simplify(sp.refine(expr, assumption))
    return expr


def fermion_rows(bundle):
    """``(rows, skipped)``: one ``(interaction, rule TeX, class, goldstone)`` per fermion vertex.

    Reuses :func:`feynlag_models.ufo.flatten_fermion_vertices`, so the same flattening rules as
    the UFO export apply: one boson leg, chiral keys merged, colour copies dropped, gluon
    couplings (which carry no boson from ``boson_list``) absent. **The Goldstone vertices are
    kept**, unlike in the export, which passes ``drop=bundle.goldstones`` because its UFO is in
    unitary gauge; a Feynman-gauge calculation needs them, so they are flagged here and the page
    gives them their own subsection.
    Yukawa internals are resolved (``h t t̄`` reads ``−m_t/v``, not ``y_t/√2``), but a mixing
    angle defined by an ``atan`` solution is left as its symbol (substituting it would replace
    ``sin(alpha)`` by a page-wide closed form and hide the physics), with its tangent written as
    ``tan(angle)`` and the angle taken in the first quadrant, as every benchmark has it.
    """
    from .ufo import flatten_fermion_vertices
    verts, skipped = flatten_fermion_vertices(bundle.fermion_table(), bundle.dirac,
                                              set(bundle.boson_list))
    fields = field_names(bundle)
    fermions = fermion_names(bundle)
    names = tex_names(bundle)
    vectors = {bundle.bosons[k] for k in _VECTOR_KEYS if k in bundle.bosons}
    goldstones = set(bundle.goldstones)
    resolve, angles = {}, {}
    for sym, expr in bundle.params.resolve().items():
        if expr.has(sp.atan):
            # a mixing angle: keep the angle symbol, and write its tangent as tan(angle)
            # so v_1 = v cos(atan(tanb)) collapses to v cos(beta) instead of v/sqrt(tanb^2+1)
            if isinstance(expr, sp.atan) and expr.args[0].is_Symbol:
                angles[expr.args[0]] = sp.tan(sym)
        else:
            resolve[sym] = expr
    resolve = {sym: expr.xreplace(angles) for sym, expr in resolve.items()} | angles
    # the benchmarks all sit in the first quadrant (tan of the angle is a positive input),
    # so cos and sin of a mixing angle are positive and the |cos| SymPy keeps can be refined away
    quadrant = sp.And(*[sp.Q.positive(f(a)) for a in (t.args[0] for t in angles.values())
                        for f in (sp.cos, sp.sin)]) if angles else None
    rows = []
    for entry in verts:
        boson = entry["bosons"][0]
        vector = boson in vectors
        left, right = (_refined(sp.sympify(entry[slot]).subs(resolve), quadrant)
                       for slot in ("left", "right"))
        if left == 0 and right == 0:
            continue
        interaction = " ".join([fermions.get(entry["bar"], str(entry["bar"])),
                                fermions.get(entry["field"], str(entry["field"])),
                                fields.get(boson, str(boson))])
        rows.append((interaction, _chiral_rule(left, right, vector, names),
                     "FFV" if vector else "FFS", boson in goldstones))
    rows.sort(key=lambda r: (r[3], r[2] != "FFV", r[0]))
    return rows, skipped


def numeric_fermion_markdown(bundle, table, leg_names, title, note):
    """A numeric table of one-boson fermion couplings, for legs with no usable closed form.

    ``table`` is an ``extract_fermion_vertices`` output and ``leg_names`` maps the
    ``IndexedBase``-plus-index legs it contains to LaTeX (``{(base, index): tex}``); a leg not
    in it falls back to the model's Dirac and boson names. Coefficients are printed as
    ``|c|`` at the benchmark, because these are the ones whose symbolic form is a numeric
    radical (a numerically diagonalised mixing), not a formula.
    """
    fields = field_names(bundle)
    fermions = fermion_base_names(bundle)
    vals = bundle.values()
    mu = sp.Symbol("mu", integer=True)
    structures = {sp.Symbol("PL", commutative=False): "P_L", sp.Symbol("PR", commutative=False): "P_R"}

    def leg(indexed):
        key = (indexed.base, int(indexed.indices[0])) if indexed.indices else indexed.base
        if key in leg_names:
            return leg_names[key]
        return fermions.get(indexed.base, rf"\mathrm{{{indexed.base}}}")

    def structure(gamma):
        text = str(gamma)
        chiral = "P_L" if "PL" in text else "P_R"
        return rf"\gamma^\mu {chiral}" if "gamma" in text else chiral

    rows = []
    for (bar, gamma, fld), by_n in table.items():
        for (boson,), coeff in by_n.get(1, {}).items():
            value = complex(sp.N(sp.simplify(coeff).subs(vals)))
            if abs(value) == 0:
                continue
            rows.append((f"{leg(bar)} {leg(fld)} {fields.get(boson, str(boson))}",
                         structure(gamma), abs(value)))
    rows.sort(key=lambda r: (-r[2], r[0]))
    lines = [f"## {title}", "", note, "",
             "| vertex | structure | $`\\lvert\\text{coupling}\\rvert`$ at the benchmark |", "|---|---|---|"]
    lines += [f"| $`{v}`$ | $`{st}`$ | {c:.3e} |" for v, st, c in rows]
    return "\n".join(lines) + "\n"


def vertices_markdown(bundle, rules, ufo_name=None, extra_sections=()):
    """The bosonic Feynman rules of ``rules`` as a Markdown page that renders on GitHub.

    Same dictionary as the LaTeX table (``vertices.tex``), grouped by vertex class, with
    physics names for fields and parameters. Rows with a Goldstone leg (Feynman-gauge vertices,
    dropped from the unitary-gauge UFO) come last, and rules too long for a table cell are
    written as display math under the table. The fermion couplings follow, taken from the same
    table the UFO export uses, with ``extra_sections`` (model-supplied Markdown) after them.
    """
    fields = field_names(bundle)
    names = tex_names(bundle)
    goldstones = set(bundle.goldstones)
    vectors = {bundle.bosons[k] for k in _VECTOR_KEYS if k in bundle.bosons}

    by_class = {}
    for legs in sorted(rules, key=str):                 # the row order of vertices.tex
        # vectors first, then scalars; otherwise the order feynlag gives
        ordered = sorted(legs, key=lambda f: f not in vectors)
        code = "".join("V" if f in vectors else "S" for f in ordered)
        gold = any(f in goldstones for f in legs)
        interaction = " ".join(fields.get(f, str(f)) for f in ordered)
        by_class.setdefault(code, []).append((interaction, _rule_tex(rules[legs], names, fields), gold))

    order = [c for c in CLASS_TITLES if c in by_class] + sorted(c for c in by_class if c not in CLASS_TITLES)
    total = sum(len(rows) for rows in by_class.values())

    def section(rows, limit=LONG_TEX):
        table = ["| interaction | Feynman rule |", "|---|---|"]
        long_rows = []
        for interaction, tex, _ in rows:
            if len(tex) > limit:
                long_rows.append((interaction, tex))
            else:
                table.append(f"| $`{interaction}`$ | $`{tex}`$ |")
        out = table if len(table) > 2 else []
        for interaction, tex in long_rows:
            out += ["", f"$`{interaction}`$", "", "```math", tex, "```"]
        while out and out[0] == "":
            out.pop(0)
        return out

    lines = [f"# Feynman rules: {_model_name(bundle)}", ""]
    ufo = f" and the [UFO]({ufo_name}/) for the exported couplings" if ufo_name else ""
    lines += [
        f"Tree-level vertices of `{bundle.id}` as feynlag derives them: {total} bosonic (potential and kinetic sectors) "
        "and the fermion couplings below.",
        "This page re-renders the rules of [`vertices.tex`](vertices.tex) with physics names; it adds no verification. "
        f"See the [card](../README.md) for what the tests pin against the literature, [`spectrum.md`](spectrum.md) for the masses{ufo}.",
        "",
        r"Each rule is $`i \times (\text{monomial coefficient}) \times \prod_f (\text{multiplicity of } f)!`$, "
        r"all momenta are incoming and $`\partial_\mu \to i\,p_\mu`$ ([`CONVENTIONS.md`](../../../CONVENTIONS.md)); "
        r"$`p_X`$ is the momentum of leg $`X`$.",
        "",
        f"## Bosonic vertices: {total} in all",
        "",
    ]
    for code in order:
        physical = [r for r in by_class[code] if not r[2]]
        if physical:
            lines += [f"### {CLASS_TITLES.get(code, code)} ({code}): {_plural(len(physical))}", ""]
            lines += section(physical) + [""]
    n_gold = sum(1 for rows in by_class.values() for r in rows if r[2])
    if n_gold:
        # not a collapsed <details>: GitHub leaves fenced math inside it unrendered
        lines += [f"### Feynman-gauge vertices with a Goldstone leg: {n_gold} in all", "",
                  "The unitary-gauge UFO drops these; they matter for a Feynman-gauge calculation.", ""]
        for code in order:
            gold_rows = [r for r in by_class[code] if r[2]]
            if gold_rows:
                lines += [f"#### {CLASS_TITLES.get(code, code)} ({code}): {_plural(len(gold_rows))}", ""]
                lines += section(gold_rows) + [""]

    ferm_rows, skipped = fermion_rows(bundle)
    n_ferm_gold = sum(1 for r in ferm_rows if r[3])
    lines += [f"## Fermion vertices: {len(ferm_rows)} in all", "",
              "One boson leg each, flattened as the UFO export flattens them: chiral keys merged into "
              r"$`P_L`$/$`P_R`$ slots, redundant colour copies dropped, Yukawa couplings resolved to masses. "
              "Gluon couplings are not included (no colour-octet particle is declared). "
              "Unlike the export, which is in unitary gauge, the Goldstone vertices are kept here; "
              "they are in their own subsection below.", ""]
    classes = (("FFV", "Fermion pair and a vector (FFV)"), ("FFS", "Fermion pair and a scalar (FFS)"))
    for code, title in classes:
        rows = [r for r in ferm_rows if r[2] == code and not r[3]]
        if rows:
            lines += [f"### {title}: {_plural(len(rows))}", ""]
            lines += section([(r[0], r[1], False) for r in rows], FERMION_LONG_TEX) + [""]
    if n_ferm_gold:
        lines += [f"### Fermion pairs with a Goldstone leg (Feynman gauge): {_plural(n_ferm_gold)}", "",
                  "Absent from the unitary-gauge UFO, which drops every Goldstone leg.", ""]
        for code, title in classes:
            rows = [r for r in ferm_rows if r[2] == code and r[3]]
            if rows:
                lines += [f"#### {title}: {_plural(len(rows))}", ""]
                lines += section([(r[0], r[1], False) for r in rows], FERMION_LONG_TEX) + [""]
    if skipped:
        legs = sorted({str(x.base) for key in skipped for x in (key[0], key[2])})
        lines += [f"{len(skipped)} further vertex keys involve fields with no Dirac particle "
                  f"(`{'`, `'.join(legs)}`) and are not in the table above; see the "
                  "[card](../README.md) and `FEYNLAG_GAPS.md` (FG-3).", ""]
    for extra in extra_sections:
        lines += [extra.rstrip("\n"), ""]
    return "\n".join(lines).rstrip("\n") + "\n"


def _plural(n, word="vertices", singular="vertex"):
    return f"{n} {singular if n == 1 else word}"


def _model_name(bundle):
    from . import MODELS_DIR
    from . import metadata as md
    meta_dir = MODELS_DIR / bundle.id
    if (meta_dir / "metadata.yaml").exists():
        return md.load(meta_dir)["name"]
    return bundle.id


def spectrum_markdown(bundle, masses):
    """``masses``: ``{label: expr}`` → a Markdown table at the benchmark.

    Labels are Markdown (write physics as ``$…$``); expressions are rendered with
    :func:`tex_names` so the table shows the physics symbols, not code names.
    """
    vals = bundle.values()
    names = tex_names(bundle)
    lines = ["| state | expression | value at benchmark |", "|---|---|---|"]
    for label, expr in masses.items():
        num = sp.sympify(expr).subs(vals)
        try:
            num = complex(num)
            num = f"{num.real:.6g}" if abs(num.imag) < 1e-12 else f"{num:.6g}"
        except TypeError:
            num = str(num)
        lines.append(f"| {label} | {_math(expr, names)} | {num} |")
    return "\n".join(lines) + "\n"


def standard_outputs(bundle, out_dir, ufo_name, masses, ufo=True, extra_vertex_sections=()):
    """UFO dir + LaTeX vertex table + spectrum table. Returns ``{path: description}``."""
    written = {}
    rules = {}
    for sector in ("potential", "kinetic"):
        rules.update(bundle.model.feynman_rules(bundle.boson_list, sector=sector,
                                                conjugate_map=bundle.cmap,
                                                simplifier=sp.simplify))
    (out_dir / "vertices.tex").write_text(latex_feynman_table(rules))
    written["vertices.tex"] = "bosonic Feynman rules (i × coefficient × n!)"
    (out_dir / "vertices.md").write_text(
        vertices_markdown(bundle, rules, ufo_name if ufo else None, extra_vertex_sections))
    written["vertices.md"] = "bosonic and fermion vertices as Markdown, grouped by vertex class"
    (out_dir / "spectrum.md").write_text(spectrum_markdown(bundle, masses))
    written["spectrum.md"] = "tree-level spectrum at the benchmark"
    if ufo:
        path, report, skipped = export_ufo(bundle, out_dir / ufo_name, ufo_name)
        if not report.ok:
            raise RuntimeError(f"UFO round-trip failed: {report.failures}")
        written[ufo_name + "/"] = f"UFO ({len(report.couplings)} couplings round-tripped)"
    return written
