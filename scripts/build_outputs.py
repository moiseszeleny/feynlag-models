"""Generate every model's ``outputs/`` (UFO, LaTeX vertex table, spectrum, stamp).

Each ``models/<id>/model.py`` may define ``outputs(bundle, out_dir)`` returning
a dict ``{relative_path: description}`` of what it wrote; this script wraps it
with the provenance stamp. ``--check`` regenerates into a temporary directory
and diffs against the committed files, ignoring the two volatile provenance
items: ``STAMP.json`` and the ``__date__`` line feynlag's UFO writer stamps into
the UFO ``__init__.py`` (``feynlag/export/ufo/writer.py``, ``datetime.date.today()``).

Run:  uv run python scripts/build_outputs.py [--check] [<id> ...]
"""

import filecmp
import re
import shutil
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from feynlag_models import MODELS_DIR  # noqa: E402
from feynlag_models.registry import load, model_ids  # noqa: E402
from feynlag_models.stamp import write_stamp  # noqa: E402

IGNORE = {"STAMP.json", "__pycache__"}
#: lines that legitimately change between regenerations (UFO ``__date__`` stamp)
VOLATILE_LINE = re.compile(r'^__date__ = "\d{4}-\d{2}-\d{2}"$')


def _same_modulo_volatile(path_a, path_b):
    """True if two text files differ only in volatile provenance lines."""
    try:
        lines = [[ln for ln in Path(p).read_text().splitlines() if not VOLATILE_LINE.match(ln)]
                 for p in (path_a, path_b)]
    except (UnicodeDecodeError, OSError):
        return False
    return lines[0] == lines[1]


def build_one(model_id, out_dir):
    out_dir = Path(out_dir)
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)
    mod = load(model_id)
    bundle = mod.build()
    written = mod.outputs(bundle, out_dir) if hasattr(mod, "outputs") else {}
    write_stamp(out_dir / "STAMP.json", model_id)
    return written


def _diff_dirs(a, b):
    cmp = filecmp.dircmp(a, b, ignore=list(IGNORE))
    diffs = list(cmp.left_only) + list(cmp.right_only)
    diffs += [f for f in cmp.diff_files
              if not _same_modulo_volatile(Path(a) / f, Path(b) / f)]
    for sub in cmp.subdirs.values():
        diffs += [f"{sub.left}: {d}" for d in _diff_dirs(sub.left, sub.right)]
    return diffs


def main(argv):
    check = "--check" in argv
    ids = [a for a in argv if not a.startswith("--")] or model_ids()
    rc = 0
    for mid in ids:
        target = MODELS_DIR / mid / "outputs"
        if check:
            with tempfile.TemporaryDirectory() as tmp:
                build_one(mid, Path(tmp) / "outputs")
                if not target.exists():
                    print(f"{mid}: outputs/ missing"); rc = 1; continue
                diffs = _diff_dirs(Path(tmp) / "outputs", target)
                print(f"{mid}: {'up to date' if not diffs else 'DIFFERS: ' + ', '.join(map(str, diffs))}")
                rc = rc or (1 if diffs else 0)
        else:
            written = build_one(mid, target)
            print(f"{mid}: wrote {', '.join(written) or 'STAMP.json only'}")
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
