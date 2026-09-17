"""Repository-level checks: every metadata validates, genealogy builds, template is valid."""

import subprocess
import sys

import pytest

from feynlag_models import ROOT
from feynlag_models import metadata as md
from feynlag_models.registry import model_dirs, model_ids


import copy


@pytest.mark.parametrize("model_dir", model_dirs(), ids=lambda p: p.name)
def test_metadata_validates(model_dir):
    md.validate(model_dir, known_ids=set(model_ids()))


def test_template_metadata_validates():
    tmpl = ROOT / "templates" / "new_model"
    md.validate(tmpl, known_ids=set(model_ids()) | {"new_model"})


def test_genealogy_script_runs():
    out = subprocess.run([sys.executable, str(ROOT / "scripts" / "build_genealogy.py"), "--check"],
                         capture_output=True, text=True, cwd=ROOT)
    assert out.returncode == 0, out.stdout + out.stderr


def test_every_model_has_the_fixed_files():
    for d in model_dirs():
        for name in ("model.py", "metadata.yaml", "README.md", "NEXT_STEPS.md", "tests"):
            assert (d / name).exists(), f"{d.name} lacks {name}"


def test_physics_card_sections():
    required = ["## Problem addressed", "## Field content", "## New symmetry",
                "## New Lagrangian terms", "## Key mechanism", "## Characteristic scale",
                "## Observables", "## Genealogy"]
    for d in model_dirs():
        text = (d / "README.md").read_text()
        for sec in required:
            assert sec in text, f"{d.name}/README.md lacks section {sec!r}"


def test_next_steps_sections():
    required = ["## 1. Natural extensions", "## 2. Observables and current bounds",
                "## 3. Open theoretical questions", "## 4. What feynlag cannot yet do",
                "## 5. Key references"]
    for d in model_dirs():
        text = (d / "NEXT_STEPS.md").read_text()
        for sec in required:
            assert sec in text, f"{d.name}/NEXT_STEPS.md lacks section {sec!r}"


def test_outputs_check_ignores_ufo_date(tmp_path):
    """The reproducibility check must tolerate the UFO ``__date__`` stamp and nothing else."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("build_outputs", ROOT / "scripts" / "build_outputs.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    src = ROOT / "models" / "sm" / "outputs" / "SM_UFO" / "__init__.py"
    text = src.read_text()
    assert '__date__ = "' in text
    other_day = tmp_path / "a.py"
    other_day.write_text(text.replace('__date__ = "2026-09-16"', '__date__ = "2031-01-01"'))
    assert mod._same_modulo_volatile(src, other_day)
    changed = tmp_path / "b.py"
    changed.write_text(text.replace("gauge = [0]", "gauge = [1]"))
    assert not mod._same_modulo_volatile(src, changed)


@pytest.mark.parametrize("model_dir", model_dirs(), ids=lambda p: p.name)
def test_ufo_scope_matches_committed_ufo(model_dir):
    """``outputs.ufo_scope.vertex_classes`` is exactly what the committed UFO contains."""
    from feynlag_models.ufo import exported_vertex_classes
    meta = md.load(model_dir)
    if not meta["outputs"]["ufo"]:
        pytest.skip("model declares no UFO")
    found = exported_vertex_classes(model_dir / meta["outputs"]["ufo"])
    assert found == set(meta["outputs"]["ufo_scope"]["vertex_classes"]), sorted(found)


# ---- negative tests: each tampering must be rejected for the intended reason
THDM = ROOT / "models" / "thdm_type2"


def _tampered(edit):
    meta = copy.deepcopy(md.load(THDM))
    edit(meta)
    return meta


def _rejects(meta, fragment):
    with pytest.raises(ValueError) as exc:
        md.validate(THDM, known_ids=set(model_ids()), meta=meta)
    assert fragment in str(exc.value), str(exc.value)


def test_unmodified_thdm_is_accepted():
    md.validate(THDM, known_ids=set(model_ids()), meta=_tampered(lambda m: None))


def test_rejects_unknown_gap_id():
    _rejects(_tampered(lambda m: m["feynlag_gaps"].append({"id": "FG-99"})), "not a row of FEYNLAG_GAPS.md")


def test_rejects_open_discrepancy_on_non_xfail_test():
    def edit(m):
        m["discrepancies"][0]["test"] = "tests/test_l2_literature.py::test_charged_higgs_yukawa_eq16"
    _rejects(_tampered(edit), "must be @pytest.mark.xfail(strict=True)")


def test_rejects_xfail_as_maturity_evidence():
    def edit(m):
        m["maturity_evidence"]["L2"].append(
            "tests/test_l2_literature.py::test_charged_higgs_quark_lepton_relative_sign_branco")
    _rejects(_tampered(edit), "cannot be evidence")


def test_rejects_cited_reference_without_id():
    def edit(m):
        ref = next(r for r in m["references"] if r["key"] == "gunion2003")
        ref["inspire"] = ref["doi"] = None
    _rejects(_tampered(edit), "needs an inspire id or a doi")


def test_rejects_placeholder_not_in_inputs():
    _rejects(_tampered(lambda m: m["benchmark"]["placeholders"].append("WXX")), "placeholders not in inputs")


def test_rejects_l4_without_slow_evidence():
    def edit(m):
        m["maturity_level"] = 4
        m["maturity_evidence"]["L4"] = ["tests/test_l3_ufo.py::test_ufo_roundtrip"]
    _rejects(_tampered(edit), "slow_evidence must be non-empty")


def test_rejects_ufo_without_scope():
    _rejects(_tampered(lambda m: m["outputs"].pop("ufo_scope")), "ufo_scope must be given")


def test_rejects_unknown_parent():
    _rejects(_tampered(lambda m: m["parents"].append({"id": "nope", "relation": "extends"})),
             "not a known model id")


def test_rejects_replaces_sector_without_sector():
    def edit(m):
        m["parents"][0].pop("sector")
    _rejects(_tampered(edit), "schema")
