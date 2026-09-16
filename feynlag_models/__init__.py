"""Shared, model-independent helpers for the feynlag-models library.

Nothing here contains the physics of any single model; that lives in
``models/<id>/model.py``.
"""

from pathlib import Path

__version__ = "0.1.0"

#: repository root (the directory holding ``pyproject.toml``)
ROOT = Path(__file__).resolve().parent.parent
MODELS_DIR = ROOT / "models"
SCHEMA_PATH = ROOT / "schema" / "metadata.schema.json"
