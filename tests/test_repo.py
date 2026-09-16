"""Repository-level checks: every metadata validates, genealogy builds, template is valid."""

import subprocess
import sys

import pytest

from feynlag_models import ROOT
from feynlag_models import metadata as md
from feynlag_models.registry import model_dirs, model_ids


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
