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
    (out_dir / "spectrum.md").write_text(spectrum_markdown(bundle, masses))
    written["spectrum.md"] = "tree-level spectrum at the benchmark"
    if ufo:
        path, report, skipped = export_ufo(bundle, out_dir / ufo_name, ufo_name)
        if not report.ok:
            raise RuntimeError(f"UFO round-trip failed: {report.failures}")
        written[ufo_name + "/"] = f"UFO ({len(report.couplings)} couplings round-tripped)"
    return written
