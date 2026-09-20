"""Standard ``outputs/`` content shared by every model."""

import sympy as sp

from feynlag import latex_feynman_table

from .ufo import export_ufo


#: LaTeX names for symbols that are not free parameters (internals, derived angles/VEVs)
DEFAULT_TEX = {
    "gw": "g", "g1": "g'", "gs": "g_s", "v": "v", "lam": r"\lambda",
    "MT": "m_t", "MB": "m_b", "MTA": r"m_\tau",
    "MU": "m_u", "MC": "m_c", "MD": "m_d", "MS": "m_s", "ME": "m_e", "MMU": r"m_\mu",
    "th12": r"\theta_{12}", "th13": r"\theta_{13}", "th23": r"\theta_{23}", "deltaCP": r"\delta",
    "v1": "v_1", "v2": "v_2", "alpha": r"\alpha", "beta": r"\beta", "theta": r"\theta",
    "tanb": r"\tan\beta", "m12sq": "m_{12}^2", "mD": "m_D", "MR": "M_R", "yv": r"y_\nu",
    "lamS": r"\lambda_S", "lamHS": r"\lambda_{HS}", "vS": "v_S",
    **{f"lam{k}": rf"\lambda_{k}" for k in range(1, 6)},
}


def tex_names(bundle):
    """``{Symbol: LaTeX}`` for every parameter: metadata ``free_parameters[].tex`` wins."""
    from . import MODELS_DIR
    from . import metadata as md
    names = dict(DEFAULT_TEX)
    meta_dir = MODELS_DIR / bundle.id
    if (meta_dir / "metadata.yaml").exists():
        for fp in md.load(meta_dir)["free_parameters"]:
            if fp.get("tex"):
                names[fp["name"]] = fp["tex"]
    # braces keep a name with its own sub/superscripts valid when SymPy raises it to a power
    return {p.symbol: "{" + names[p.name] + "}" for p in bundle.params if p.name in names}


def _math(expr, symbol_names):
    """Inline Markdown math for a table cell (a bare ``|`` would split the cell)."""
    tex = sp.latex(expr, symbol_names=symbol_names)
    tex = tex.replace(r"\left|", r"\left\vert ").replace(r"\right|", r"\right\vert ")
    # GitHub double-escapes < and > inside math (CONVENTIONS.md, "Markdown")
    tex = tex.replace("<", r" \lt ").replace(">", r" \gt ")
    return f"$`{tex}`$"


#: LaTeX names of the physical bosons, keyed by the ``bundle.bosons`` keys
FIELD_TEX = {
    "h": "h", "h1": "h_1", "h2": "h_2", "H": "H", "A0": "A",
    "G0": "G^0", "Gp": "G^+", "Gm": "G^-", "Hp": "H^+", "Hm": "H^-",
    "Z": "Z", "A": r"\gamma", "Wp": "W^+", "Wm": "W^-",
}
_VECTOR_KEYS = ("A", "Z", "Wp", "Wm")
#: section order and titles of the vertex classes (V = vector, S = scalar)
CLASS_TITLES = {
    "SSS": "Cubic scalar", "SSSS": "Quartic scalar", "VSS": "Vector and two scalars",
    "VVS": "Two vectors and a scalar", "VVSS": "Two vectors and two scalars",
}
#: a rule whose TeX is longer than this leaves the table for a display block
LONG_TEX = 140


def field_names(bundle):
    """``{field Symbol: LaTeX}`` for the bundle's physical bosons (matched by identity)."""
    return {sym: FIELD_TEX.get(key, rf"\mathrm{{{key}}}") for key, sym in bundle.bosons.items()}


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


def vertices_markdown(bundle, rules, ufo_name=None):
    """The bosonic Feynman rules of ``rules`` as a Markdown page that renders on GitHub.

    Same dictionary as the LaTeX table (``vertices.tex``), grouped by vertex class, with
    physics names for fields and parameters. Rows with a Goldstone leg (Feynman-gauge vertices,
    dropped from the unitary-gauge UFO) come last, and rules too long for a table cell are
    written as display math under the table.
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

    def section(rows):
        table = ["| interaction | Feynman rule |", "|---|---|"]
        long_rows = []
        for interaction, tex, _ in rows:
            if len(tex) > LONG_TEX:
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
        f"Bosonic vertices of `{bundle.id}` (potential and kinetic sectors), {total} in all, as feynlag derives them at tree level.",
        "This page re-renders the rules of [`vertices.tex`](vertices.tex) with physics names; it adds no verification. "
        f"See the [card](../README.md) for what the tests pin against the literature, [`spectrum.md`](spectrum.md) for the masses{ufo}.",
        "",
        r"Each rule is $`i \times (\text{monomial coefficient}) \times \prod_f (\text{multiplicity of } f)!`$, "
        r"all momenta are incoming and $`\partial_\mu \to i\,p_\mu`$ ([`CONVENTIONS.md`](../../../CONVENTIONS.md)); "
        r"$`p_X`$ is the momentum of leg $`X`$.",
        "",
    ]
    for code in order:
        physical = [r for r in by_class[code] if not r[2]]
        if physical:
            lines += [f"## {CLASS_TITLES.get(code, code)} ({code}): {len(physical)} vertices", ""]
            lines += section(physical) + [""]
    n_gold = sum(1 for rows in by_class.values() for r in rows if r[2])
    if n_gold:
        # not a collapsed <details>: GitHub leaves fenced math inside it unrendered
        lines += [f"## Feynman-gauge vertices with a Goldstone leg: {n_gold} in all", "",
                  "The unitary-gauge UFO drops these; they matter for a Feynman-gauge calculation.", ""]
        for code in order:
            gold_rows = [r for r in by_class[code] if r[2]]
            if gold_rows:
                lines += [f"### {CLASS_TITLES.get(code, code)} ({code}): {len(gold_rows)} vertices", ""]
                lines += section(gold_rows) + [""]
    return "\n".join(lines).rstrip("\n") + "\n"


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


def standard_outputs(bundle, out_dir, ufo_name, masses, ufo=True):
    """UFO dir + LaTeX vertex table + spectrum table. Returns ``{path: description}``."""
    written = {}
    rules = {}
    for sector in ("potential", "kinetic"):
        rules.update(bundle.model.feynman_rules(bundle.boson_list, sector=sector,
                                                conjugate_map=bundle.cmap,
                                                simplifier=sp.simplify))
    (out_dir / "vertices.tex").write_text(latex_feynman_table(rules))
    written["vertices.tex"] = "bosonic Feynman rules (i × coefficient × n!)"
    (out_dir / "vertices.md").write_text(vertices_markdown(bundle, rules, ufo_name if ufo else None))
    written["vertices.md"] = "the same rules as Markdown, grouped by vertex class"
    (out_dir / "spectrum.md").write_text(spectrum_markdown(bundle, masses))
    written["spectrum.md"] = "tree-level spectrum at the benchmark"
    if ufo:
        path, report, skipped = export_ufo(bundle, out_dir / ufo_name, ufo_name)
        if not report.ok:
            raise RuntimeError(f"UFO round-trip failed: {report.failures}")
        written[ufo_name + "/"] = f"UFO ({len(report.couplings)} couplings round-tripped)"
    return written
