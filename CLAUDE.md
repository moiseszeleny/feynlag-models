# CLAUDE.md — permanent rules for `feynlag-models`

## What this repository is

A **verified library of minimal Standard Model extensions** built with
[`feynlag`](https://github.com/moiseszeleny/feynlag) (pinned exactly in
`pyproject.toml` / `uv.lock`). Every model ships a physics card (`README.md`),
a `NEXT_STEPS.md`, machine-readable `metadata.yaml`, tests that pin its physics
against the literature, and stamped outputs (UFO, LaTeX). It supports a SciPost
Physics Codebases article, so **verification is the differentiator**.

## Hard rules

- **Never modify `feynlag`.** If something is missing, append an entry to
  `FEYNLAG_GAPS.md` (what was attempted, what failed, which model item stopped)
  and stop that item. Do not monkey-patch, vendor, or work around the library.
- **One source of truth for conventions:** `CONVENTIONS.md`. Metric, potential
  signs, VEV normalization, rotation conventions, Feynman-rule definition, names,
  PDG codes. A model that needs a different convention must document the map.
- **Honesty rules (strict):**
  - Never invent numerical reference values, experimental bounds, or citations.
    If unsure, write `TODO(verify)`. The final report lists every `TODO(verify)`.
  - Tests against the literature must cite the equation/table they reproduce
    (reference key in `metadata.yaml` → `references`, location in
    `literature_checks`).
  - In prose, distinguish what **feynlag verified** (name the test) from
    **physics judgment**.
  - If a test fails, report it; do not weaken the test to make it pass.
  - Record `maturity_level` honestly; `maturity_evidence` must name tests that
    exist and pass for every claimed level.

## Maturity levels (definition of done)

- **L0**: fields declared, Lagrangian invariant (gauge + declared discrete), anomalies cancel.
- **L1**: tadpoles solved, full spectrum, Goldstone counting correct.
- **L2**: key masses/mixings/vertices checked against literature values, both
  symbolically and at random numeric points (`numeric_equal`).
- **L3**: UFO exported and importable (`verify_ufo_numeric` round-trip passes).
- **L4**: MadGraph cross-section check (only if feasible; otherwise stay at L3).

## Layout and contracts

- `models/<id>/model.py` exposes `ID`, `PARENT`, and `build(benchmark=None) -> ModelBundle`.
  Children are written as **parent + delta**: call `models.sm.model.pieces(...)`
  and add/replace fields, terms, parameters before assembling the `Model`.
- `models/<id>/metadata.yaml` follows `schema/metadata.schema.json`; the
  `benchmark` block is the *only* numeric point tests and outputs use.
- `models/<id>/README.md` (physics card) has the fixed sections listed in
  `templates/new_model/README.md`; `NEXT_STEPS.md` likewise.
- `models/<id>/outputs/` is generated only by `scripts/build_outputs.py`
  (stamped with the repo git hash and library versions). Never hand-edit.
- `scripts/build_genealogy.py` derives the family tree from `parents` alone.
- `templates/new_model/` is the skeleton for future models.

## Commands

```bash
uv sync --all-extras
uv run pytest -q -m "not slow"          # fast suite (CI on push)
uv run pytest -q models/<id>            # one model
uv run pytest -q -m slow                # MadGraph checks (manual / release)
uv run python scripts/build_outputs.py [--check] [<id> ...]
uv run python scripts/build_genealogy.py [--check]
```

## Workflow for a new model

1. Copy `templates/new_model/` to `models/<id>/`, fill `metadata.yaml` first.
2. Write `model.py` as parent + delta. Run L0 tests. Commit.
3. Climb the levels one at a time; one commit per level; never skip a level.
4. Regenerate outputs and the genealogy; update `last_reviewed`.
