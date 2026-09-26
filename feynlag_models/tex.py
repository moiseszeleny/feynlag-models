r"""LaTeX names for every symbol a model creates: the single source of truth.

feynlag builds a symbol declared with a tex as a ``TexSymbol``, so plain ``sympy.latex`` of any
Lagrangian piece, mass matrix or Feynman rule prints physics notation with no caller-side map.
:data:`TEX` maps a **symbol name** to its LaTeX name and is passed as-is to feynlag's builders
(``electroweak_scaffold(tex=TEX)``, ``to_physical_basis(..., tex=TEX)``, ``expand_vev(..., tex=TEX)``);
:func:`external`/:func:`internal` declare parameters with their tex looked up here.

Parameter texs come from every model's ``metadata.yaml`` ``free_parameters[].tex`` (which win) and
:data:`PARAM_TEX` (derived internals, couplings fixed by the scaffold), and are brace-wrapped: SymPy
does not parenthesize a name like ``g'``, and ``g'^{2}`` is invalid LaTeX.
"""

from feynlag import ExternalParameter, InternalParameter

from . import MODELS_DIR
from . import metadata as md

_FLAVOURS = {"e": "e", "mu": r"\mu", "tau": r"\tau"}
_QUARKS = "udcsbt"

#: parameters no model's metadata names: scaffold couplings, derived internals, widths
PARAM_TEX = {
    "gw": "g", "g1": "g'", "gs": "g_s", "v": "v", "lam": r"\lambda", "mu2": r"\mu^2",
    "MT": "m_t", "MB": "m_b", "MTA": r"m_\tau",
    "MU": "m_u", "MC": "m_c", "MD": "m_d", "MS": "m_s", "ME": "m_e", "MMU": r"m_\mu",
    "MW": "m_W", "MZ": "m_Z", "MH": "m_h",
    "WW": r"\Gamma_W", "WZ": r"\Gamma_Z", "WH": r"\Gamma_h", "WT": r"\Gamma_t",
    **{f"y{f}": f"y_{f}" for f in _QUARKS},
    "ye": "y_e", "ymu": r"y_\mu", "ytau": r"y_\tau",
    # CKM (sm_ckm)
    "th12": r"\theta_{12}", "th13": r"\theta_{13}", "th23": r"\theta_{23}", "deltaCP": r"\delta",
    **{f"V{u}{d}": f"V_{{{u}{d}}}" for u in "uct" for d in "dsb"},
    # singlet (sm_singlet_z2)
    "vS": "v_S", "lamS": r"\lambda_S", "lamHS": r"\lambda_{HS}", "muS2": r"\mu_S^2",
    "theta": r"\theta", "MH1": "m_{h_1}", "MH2": "m_{h_2}", "WH2": r"\Gamma_{h_2}",
    # 2HDM (thdm_type2)
    "v1": "v_1", "v2": "v_2", "alpha": r"\alpha", "beta": r"\beta", "tanb": r"\tan\beta",
    "m12sq": "m_{12}^2", "m11sq": "m_{11}^2", "m22sq": "m_{22}^2",
    **{f"lam{k}": rf"\lambda_{k}" for k in range(1, 6)},
    "MH0": "m_h", "MHH": "m_H", "MA0": "m_A", "MHp": r"m_{H^\pm}",
    "WHH": r"\Gamma_H", "WA0": r"\Gamma_A", "WHp": r"\Gamma_{H^\pm}",
    # seesaw (seesaw_type1, seesaw_type1_2n)
    "yv": r"y_\nu", "MR": "M_R", "mD": "m_D", "MN1": "m_{N_1}", "MN2": "m_{N_2}",
}

#: bosons: the SM scaffold's weak-basis components and fluctuations, and every physical state
BOSON_TEX = {
    "Gp": "G^+", "Gm": "G^-", "H0": "H^0", "H0_r": "h", "H0_i": "G^0",
    "W_1": "W^1", "W_2": "W^2", "W_3": "W^3", "B": "B",
    "Z": "Z", "A": r"\gamma", "Wp": "W^+", "Wm": "W^-",
    "h1": "h_1", "h2": "h_2",
    # 2HDM: doublet fluctuations and the physical states
    "H10_r": r"\rho_1", "H20_r": r"\rho_2", "H10_i": r"\eta_1", "H20_i": r"\eta_2",
    "h": "h", "H": "H", "G0": "G^0", "A0": "A", "Hp": "H^+", "Hm": "H^-",
}


def metadata_tex():
    """``{name: tex}`` from every model's ``free_parameters``; raises if two models disagree."""
    out, where = {}, {}
    for d in sorted(p for p in MODELS_DIR.iterdir() if (p / "metadata.yaml").exists()):
        for fp in md.load(d)["free_parameters"]:
            name, tex = fp["name"], fp.get("tex")
            if not tex:
                continue
            if name in out and out[name] != tex:
                raise ValueError(f"parameter {name!r}: tex {out[name]!r} in {where[name]} "
                                 f"but {tex!r} in {d.name}")
            out[name], where[name] = tex, d.name
    return out


def _braced(tex):
    return "{" + tex + "}"


#: ``{symbol name: LaTeX}`` for every parameter and boson (parameters brace-wrapped)
TEX = {**{n: _braced(t) for n, t in {**PARAM_TEX, **metadata_tex()}.items()}, **BOSON_TEX}


def external(name, value=None, **kwargs):
    """``ExternalParameter`` with its tex from :data:`TEX`."""
    return ExternalParameter(name, value, tex=TEX.get(name), **kwargs)


def internal(name, expr=None, **kwargs):
    """``InternalParameter`` with its tex from :data:`TEX`."""
    return InternalParameter(name, expr, tex=TEX.get(name), **kwargs)
