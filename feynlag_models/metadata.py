"""Load and validate ``metadata.yaml`` files (schema version 2).

Two layers: the JSON Schema in ``schema/metadata.schema.json`` (shape), and the
cross-checks in :func:`validate` (consistency with the directory, the parents,
the claimed maturity level, the tests, ``FEYNLAG_GAPS.md`` and the references).
"""

import ast
import datetime
import json
import re
from pathlib import Path

import jsonschema
import yaml

from . import MODELS_DIR, ROOT, SCHEMA_PATH

LEVELS = ("L0", "L1", "L2", "L3", "L4")
GAPS_PATH = ROOT / "FEYNLAG_GAPS.md"


# ------------------------------------------------------------------ loading

def load_schema():
    return json.loads(SCHEMA_PATH.read_text())


def _dates_to_str(obj):
    """YAML turns ``2026-09-16`` into ``datetime.date``; the schema wants ISO strings."""
    if isinstance(obj, dict):
        return {k: _dates_to_str(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_dates_to_str(v) for v in obj]
    if isinstance(obj, (datetime.date, datetime.datetime)):
        return obj.isoformat()
    return obj


def load(model_dir):
    """Parse ``<model_dir>/metadata.yaml`` (no validation)."""
    with (Path(model_dir) / "metadata.yaml").open() as fh:
        return _dates_to_str(yaml.safe_load(fh))


def benchmark_inputs(model_dir):
    """The numeric input point of a model (``benchmark.inputs``) as a fresh dict."""
    return dict(load(model_dir)["benchmark"]["inputs"])


def parent_ids(meta):
    return [p["id"] for p in meta["parents"]]


def gap_ids(path=GAPS_PATH):
    """Ids of the rows of ``FEYNLAG_GAPS.md`` (``| FG-n | …``)."""
    return set(re.findall(r"^\|\s*(FG-\d+)\s*\|", Path(path).read_text(), flags=re.M))


# ------------------------------------------------------------- test lookup

def _functions(test_file):
    """``{name: FunctionDef}`` for every ``test*`` function in a file (static)."""
    tree = ast.parse(Path(test_file).read_text())
    return {n.name: n for n in ast.walk(tree)
            if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
            and n.name.startswith("test")}


def _resolve(model_dir, node_id):
    """``tests/x.py::test_y`` → ``(FunctionDef, None)`` or ``(None, error)``."""
    path, _, func = node_id.partition("::")
    func = func.split("::")[-1]              # allow Class::method
    test_file = Path(model_dir) / path
    if not test_file.exists():
        return None, f"{node_id}: file {path} does not exist"
    node = _functions(test_file).get(func)
    if node is None:
        return None, f"{node_id}: no function {func} in {path}"
    return node, None


def _is_strict_xfail(func):
    """True if decorated with ``pytest.mark.xfail(..., strict=True)``."""
    for dec in func.decorator_list:
        if not isinstance(dec, ast.Call):
            continue
        name = ast.unparse(dec.func)
        if name.endswith("mark.xfail"):
            for kw in dec.keywords:
                if kw.arg == "strict" and isinstance(kw.value, ast.Constant) \
                        and kw.value.value is True:
                    return True
    return False


# --------------------------------------------------------------- validation

def validate(model_dir, known_ids=None, meta=None):
    """Validate one model's metadata; returns the parsed dict.

    Args:
        model_dir: the model directory (test ids resolve relative to it).
        known_ids: ids a parent may name (default: every ``models/*`` dir).
        meta: an already-loaded dict to validate instead of the file (tests).

    Raises ``ValueError`` listing every problem found.
    """
    model_dir = Path(model_dir)
    meta = load(model_dir) if meta is None else meta
    try:
        jsonschema.validate(meta, load_schema(), cls=jsonschema.Draft202012Validator)
    except jsonschema.ValidationError as exc:
        raise ValueError(f"{model_dir.name}/metadata.yaml: schema: {exc.message} "
                         f"at {list(exc.absolute_path)}") from None

    problems = []

    def check_test(node_id, what, strict_xfail=None):
        node, err = _resolve(model_dir, node_id)
        if err:
            problems.append(f"{what}: {err}")
            return
        if strict_xfail is True and not _is_strict_xfail(node):
            problems.append(f"{what}: {node_id} must be @pytest.mark.xfail(strict=True)")
        if strict_xfail is False and _is_strict_xfail(node):
            problems.append(f"{what}: {node_id} is a strict xfail and cannot be evidence")

    # identity and genealogy
    if meta["id"] != model_dir.name:
        problems.append(f"id {meta['id']!r} != directory name {model_dir.name!r}")
    if known_ids is None:
        known_ids = {p.name for p in MODELS_DIR.iterdir() if p.is_dir()}
    ids = parent_ids(meta)
    if len(ids) != len(set(ids)):
        problems.append("duplicate parent ids")
    for parent in ids:
        if parent not in known_ids:
            problems.append(f"parent {parent!r} is not a known model id")
        if parent == meta["id"]:
            problems.append("a model cannot be its own parent")

    # maturity
    level = meta["maturity_level"]
    for k, name in enumerate(LEVELS):
        evidence = meta["maturity_evidence"][name]
        if k <= level and not evidence:
            problems.append(f"maturity_level {level} claimed but {name} has no evidence")
        if k > level and evidence:
            problems.append(f"{name} lists evidence but maturity_level is {level}")
        for node_id in evidence:
            check_test(node_id, f"{name} evidence", strict_xfail=False)
    if (level == 4) != bool(meta["slow_evidence"]):
        problems.append("slow_evidence must be non-empty exactly when maturity_level is 4")
    for run in meta["slow_evidence"]:
        check_test(run["test"], "slow_evidence")

    # key results, benchmark
    for kr in meta["key_results"]:
        check_test(kr["test"], "key result", strict_xfail=False)
    bench = meta["benchmark"]
    missing = set(bench["placeholders"]) - set(bench["inputs"])
    if missing:
        problems.append(f"benchmark placeholders not in inputs: {sorted(missing)}")
    if "derived_from" in bench and "test" in bench["derived_from"]:
        check_test(bench["derived_from"]["test"], "benchmark.derived_from")

    # references and literature
    refs = {r["key"]: r for r in meta["references"]}
    if len(refs) != len(meta["references"]):
        problems.append("duplicate reference keys")
    if level >= 2 and not meta["literature_checks"]:
        problems.append("L2 claimed but literature_checks is empty")
    cited = set()
    for chk in meta["literature_checks"]:
        if chk["ref"] not in refs:
            problems.append(f"literature check {chk['quantity']!r} cites unknown ref {chk['ref']!r}")
        cited.add(chk["ref"])
        check_test(chk["test"], "literature check", strict_xfail=False)
    if level >= 2:
        for key in sorted(cited & set(refs)):
            r = refs[key]
            if r["kind"] == "software":
                if not (r.get("url") and r.get("commit")):
                    problems.append(f"reference {key!r} (software) cited at L{level} needs url and commit")
            elif not (r.get("inspire") or r.get("doi")):
                problems.append(f"reference {key!r} cited at L{level} needs an inspire id or a doi")

    # discrepancies
    seen = set()
    for d in meta["discrepancies"]:
        if d["id"] in seen:
            problems.append(f"duplicate discrepancy id {d['id']}")
        seen.add(d["id"])
        if d["ref"] not in refs:
            problems.append(f"discrepancy {d['id']} cites unknown ref {d['ref']!r}")
        if "test" in d:
            check_test(d["test"], f"discrepancy {d['id']}",
                       strict_xfail=True if d["status"] == "open" else None)

    # feynlag gaps
    known_gaps = gap_ids()
    for g in meta["feynlag_gaps"]:
        if g["id"] not in known_gaps:
            problems.append(f"feynlag gap {g['id']} is not a row of FEYNLAG_GAPS.md")
        if "test" in g:
            check_test(g["test"], f"feynlag gap {g['id']}", strict_xfail=True)

    # outputs
    out = meta["outputs"]
    if bool(out["ufo"]) != ("ufo_scope" in out):
        problems.append("outputs.ufo_scope must be given exactly when outputs.ufo is set")
    if level >= 3 and not out["ufo"]:
        problems.append(f"maturity_level {level} claims L3 but outputs.ufo is null")

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
