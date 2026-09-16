"""Load and validate ``metadata.yaml`` files.

Two layers: the JSON Schema in ``schema/metadata.schema.json`` (shape), and the
cross-checks below (consistency with the directory, the parents, the claimed
maturity level and the literature references).
"""

import ast
import json
from pathlib import Path

import jsonschema
import yaml

from . import MODELS_DIR, SCHEMA_PATH

LEVELS = ("L0", "L1", "L2", "L3", "L4")


def load_schema():
    return json.loads(SCHEMA_PATH.read_text())


def load(model_dir):
    """Parse ``<model_dir>/metadata.yaml`` (no validation)."""
    model_dir = Path(model_dir)
    with (model_dir / "metadata.yaml").open() as fh:
        meta = yaml.safe_load(fh)
    # YAML turns 2026-09-16 into datetime.date; the schema wants the ISO string
    if hasattr(meta.get("last_reviewed"), "isoformat"):
        meta["last_reviewed"] = meta["last_reviewed"].isoformat()
    return meta


def _test_functions(test_file):
    """Names of ``test_*`` functions/methods defined in a test file (static)."""
    tree = ast.parse(Path(test_file).read_text())
    names = set()
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) \
                and node.name.startswith("test"):
            names.add(node.name)
    return names


def _resolve_test_id(model_dir, node_id):
    """``tests/test_x.py::test_y`` → (path, function) or an error string."""
    if "::" not in node_id:
        return f"{node_id}: expected 'path::function'"
    path, _, func = node_id.partition("::")
    func = func.split("::")[-1]          # allow Class::method
    test_file = Path(model_dir) / path
    if not test_file.exists():
        return f"{node_id}: file {path} does not exist"
    if func not in _test_functions(test_file):
        return f"{node_id}: no function {func} in {path}"
    return None


def validate(model_dir, known_ids=None):
    """Validate one model's metadata; returns the parsed dict.

    Raises ``ValueError`` listing every problem found.
    """
    model_dir = Path(model_dir)
    meta = load(model_dir)
    problems = []
    try:
        jsonschema.validate(meta, load_schema(),
                            cls=jsonschema.Draft202012Validator)
    except jsonschema.ValidationError as exc:
        problems.append(f"schema: {exc.message} at {list(exc.absolute_path)}")
        raise ValueError("\n".join(problems))

    if meta["id"] != model_dir.name:
        problems.append(f"id {meta['id']!r} != directory name {model_dir.name!r}")
    if known_ids is None:
        known_ids = {p.name for p in MODELS_DIR.iterdir() if p.is_dir()}
    for parent in meta["parents"]:
        if parent not in known_ids:
            problems.append(f"parent {parent!r} is not a known model id")
        if parent == meta["id"]:
            problems.append("a model cannot be its own parent")

    level = meta["maturity_level"]
    for k, name in enumerate(LEVELS):
        ids = meta["maturity_evidence"][name]
        if k <= level and not ids:
            problems.append(f"maturity_level {level} claimed but {name} has no evidence")
        if k > level and ids:
            problems.append(f"{name} lists evidence but maturity_level is {level}")
        for node_id in ids:
            err = _resolve_test_id(model_dir, node_id)
            if err:
                problems.append(f"{name} evidence {err}")

    ref_keys = {r["key"] for r in meta["references"]}
    for chk in meta["literature_checks"]:
        if chk["ref"] not in ref_keys:
            problems.append(f"literature check {chk['quantity']!r} cites unknown ref {chk['ref']!r}")
        err = _resolve_test_id(model_dir, chk["test"])
        if err:
            problems.append(f"literature check {err}")
    for kr in meta["key_results"]:
        err = _resolve_test_id(model_dir, kr["test"])
        if err:
            problems.append(f"key result {err}")
    if level >= 2 and not meta["literature_checks"]:
        problems.append("L2 claimed but literature_checks is empty")

    if problems:
        raise ValueError(f"{model_dir.name}/metadata.yaml:\n  " + "\n  ".join(problems))
    return meta


def todo_verify(model_dir):
    """Every line in the model directory containing ``TODO(verify)``."""
    hits = []
    for path in sorted(Path(model_dir).rglob("*")):
        if path.is_file() and path.suffix in {".yaml", ".md", ".py", ".tex"} \
                and "outputs" not in path.parts:
            for n, line in enumerate(path.read_text().splitlines(), 1):
                if "TODO(verify)" in line:
                    hits.append((path, n, line.strip()))
    return hits
