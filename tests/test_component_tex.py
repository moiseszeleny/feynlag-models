"""Every symbol a model builds carries its own LaTeX name (feynlag ``TexSymbol``).

Weak-basis field components (``component_tex``), parameters and physical-basis bosons, so
``sympy.latex`` of any Lagrangian piece, operator, mass matrix or Feynman rule prints physics
notation with no caller-side name map (feynlag-anomalies UG-2). ``feynlag_models.tex.TEX`` is the
single source of the names.
"""

import pytest
import sympy as sp
from feynlag import TexSymbol

from feynlag_models.registry import build, model_ids
from feynlag_models.tex import TEX, metadata_tex


def _label(component):
    return component.label if isinstance(component, sp.IndexedBase) else component


@pytest.mark.parametrize("model_id", model_ids())
def test_every_component_has_tex(model_id):
    bundle = build(model_id)
    plain = [f"{f.name}.{_label(c)}" for f in bundle.model.fields for c in f.components
             if not isinstance(_label(c), TexSymbol)]
    assert not plain, f"components without component_tex: {plain}"


def test_sm_renders():
    bundle = build("sm")
    H, W, B, G, Ll, eR, QL = (f for f in bundle.model.fields
                              if f.name in ("H", "W", "B", "G", "Ll", "eR", "QL"))
    assert [sp.latex(c) for c in H.components] == ["G^+", "H^0"]
    assert sp.latex(W[2]) == "W^3" and sp.latex(G[7]) == "G^{8}"
    assert sp.latex(Ll.bar_components[0]) == r"\overline{\nu_L}"
    assert sp.latex(QL[3]) == "d_L^{1}"
    assert sp.latex(bundle.bosons["Gm"]) == "G^-"


@pytest.mark.parametrize("model_id", model_ids())
def test_every_parameter_and_boson_has_tex(model_id):
    bundle = build(model_id)
    plain = [p.name for p in bundle.params if not isinstance(p.symbol, TexSymbol)]
    plain += [f"boson {k}" for k, s in bundle.bosons.items() if not isinstance(s, TexSymbol)]
    assert not plain, f"symbols without tex: {plain}"
    # each symbol's own tex is the table's
    for p in bundle.params:
        assert sp.latex(p.symbol) == TEX[p.name]


def test_metadata_tex_is_consistent_and_wins():
    meta = metadata_tex()               # raises if two models disagree on a name
    assert all(TEX[n] == "{" + t + "}" for n, t in meta.items())


def test_sm_parameters_and_bosons_render():
    bundle = build("sm")
    params = {p.name: p.symbol for p in bundle.params}
    assert sp.latex(params["lam"] * params["v"] ** 2) == r"{\lambda} {v}^{2}"
    assert sp.latex(params["g1"] ** 2) == "{g'}^{2}"          # braced: g'^{2} is invalid LaTeX
    assert sp.latex(params["MW"]) == "{m_W}"
    b = bundle.bosons
    assert [sp.latex(b[k]) for k in ("h", "G0", "Z", "A", "Wp", "Wm")] == \
        ["h", "G^0", "Z", r"\gamma", "W^+", "W^-"]
    assert b["h"].name == "H0_r"                                # the name is unchanged


def test_thdm_physical_states_render():
    b = build("thdm_type2").bosons
    assert [sp.latex(b[k]) for k in ("h", "H", "A0", "Hp", "Hm")] == ["h", "H", "A", "H^+", "H^-"]
