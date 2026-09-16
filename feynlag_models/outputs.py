"""Standard ``outputs/`` content shared by every model."""

import sympy as sp

from feynlag import latex_feynman_table

from .ufo import export_ufo


def spectrum_markdown(bundle, masses):
    """``masses``: ``{label: expr}`` (mass², or mass) → a Markdown table at the benchmark."""
    vals = bundle.values()
    lines = ["| state | expression | value at benchmark |", "|---|---|---|"]
    for label, expr in masses.items():
        num = sp.sympify(expr).subs(vals)
        try:
            num = complex(num)
            num = f"{num.real:.6g}" if abs(num.imag) < 1e-12 else f"{num:.6g}"
        except TypeError:
            num = str(num)
        lines.append(f"| {label} | `{sp.latex(expr)}` | {num} |")
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
