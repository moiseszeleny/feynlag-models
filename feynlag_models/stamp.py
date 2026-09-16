"""Provenance stamp for generated outputs."""

import datetime
import json
import platform
import re
import subprocess
import sys

import sympy
import feynlag

from . import ROOT, __version__


def _git(*args):
    try:
        return subprocess.check_output(["git", *args], cwd=ROOT,
                                       text=True, stderr=subprocess.DEVNULL).strip()
    except Exception:  # noqa: BLE001 — stamp must never fail a build
        return None


def feynlag_pin():
    """The feynlag git commit pinned in pyproject.toml (None if unpinned)."""
    text = (ROOT / "pyproject.toml").read_text()
    m = re.search(r"feynlag\.git@([0-9a-f]{7,40})", text)
    return m.group(1) if m else None


def make_stamp(model_id):
    return {
        "model": model_id,
        "generated": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        "feynlag_models_version": __version__,
        "repo_commit": _git("rev-parse", "HEAD"),
        "repo_dirty": bool(_git("status", "--porcelain")),
        "feynlag_version": feynlag.__version__,
        "feynlag_commit": feynlag_pin(),
        "sympy_version": sympy.__version__,
        "python": sys.version.split()[0],
        "platform": platform.platform(),
    }


def write_stamp(path, model_id):
    stamp = make_stamp(model_id)
    path.write_text(json.dumps(stamp, indent=2) + "\n")
    return stamp
