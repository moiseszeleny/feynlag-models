"""Every weak-basis field component carries its own LaTeX name (feynlag ``component_tex``).

So ``sympy.latex`` of any Lagrangian piece, operator or mass matrix of a model prints physics
notation with no caller-side name map (feynlag-anomalies UG-2).
"""

import pytest
import sympy as sp
from feynlag import TexSymbol

from feynlag_models.registry import build, model_ids


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
