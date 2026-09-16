"""Discover models and import their ``model.py`` modules."""

import importlib
from pathlib import Path

from . import MODELS_DIR
from . import metadata as _metadata


def model_dirs():
    """Every ``models/<id>/`` directory holding a ``metadata.yaml``."""
    return sorted(p for p in MODELS_DIR.iterdir()
                  if p.is_dir() and (p / "metadata.yaml").exists())


def model_ids():
    return [p.name for p in model_dirs()]


def metadata(model_id):
    return _metadata.load(MODELS_DIR / model_id)


def load(model_id):
    """Import ``models.<id>.model`` and return the module."""
    return importlib.import_module(f"models.{model_id}.model")


def build(model_id, benchmark=None):
    """Build a model's bundle at its metadata benchmark (or an override)."""
    return load(model_id).build(benchmark=benchmark)
