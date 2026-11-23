"""<Model name>: <one line>.  Written as parent + delta.

Contract: ``ID``, ``PARENT``, ``build(benchmark=None) -> ModelBundle``,
optional ``outputs(bundle, out_dir) -> {path: description}``.
"""

import sympy as sp

from feynlag import Model
from feynlag_models import MODELS_DIR
from feynlag_models import metadata as md
from feynlag_models.bundle import ModelBundle
from feynlag_models.outputs import standard_outputs
from models.sm import model as sm

ID = "new_model"
PARENT = "sm"


def benchmark_point():
    return md.benchmark_inputs(MODELS_DIR / ID)


def build(benchmark=None):
    bench = benchmark_point() if benchmark is None else dict(benchmark)
    p = sm.pieces(bench, higgs=True)          # the parent, before Model assembly
    # --- delta: new fields / parameters / terms -----------------------------
    P = p.params                              # the model's ParameterSet, extended in place
    # x = P.external("x", bench["x"], tex=TEX["x"]); S = Scalar(...); p.fields.append(S)
    # p.add_term(expr, "potential", "name"); symbolic flavour indices are feynlag's FL_I, FL_J
    model = Model(ID, gauge_groups=p.gauge_groups, discrete_groups=p.discrete_groups,
                  fields=p.fields, parameters=P, lagrangian=p.lagrangian())
    model.solve_tadpoles([p.ew.mu2])
    raise NotImplementedError("finish the delta, rotations and the bundle")


def outputs(bundle, out_dir):
    masses = {}
    return standard_outputs(bundle, out_dir, "NEW_MODEL_UFO", masses)
