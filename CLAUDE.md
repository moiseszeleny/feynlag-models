# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A **verified library of minimal Standard Model extensions** built with
[`feynlag`](https://github.com/moiseszeleny/feynlag), a SymPy library that derives tree-level
Feynman rules. feynlag is pinned to an exact git commit in `pyproject.toml` / `uv.lock`, and
its local checkout is `../lagrangian`. Every model ships a physics card (`README.md`), a
`NEXT_STEPS.md`, machine-readable `metadata.yaml`, tests that pin its physics against the
literature, and stamped outputs (UFO, LaTeX). The repository supports a SciPost Physics
Codebases article, so **verification is the differentiator**. `REPORT.md` is the running
status report (maturity per model, xfails, `TODO(verify)` list, gaps).

## Commands

```bash
uv sync --all-extras                               # after any pyproject/uv.lock change
uv run pytest -q -m "not slow"                     # fast suite, what CI runs (~4 min)
uv run pytest -q models/thdm_type2                 # one model
uv run pytest -q "models/thdm_type2/tests/test_l2_literature.py::test_hVV_HVV_sin_cos_beta_minus_alpha"
uv run pytest -q tests                             # repo-level: metadata validation, genealogy, template (seconds)
uv run pytest -q -m slow                           # MadGraph checks (manual / release workflow)
uv run python scripts/build_outputs.py [--check] [<id> ...]
uv run python scripts/build_genealogy.py [--check]
```

- There is no linter or formatter.
- CI (`.github/workflows/fast.yml`) runs the fast suite on Python 3.12 and 3.13, then both
  `--check` scripts. Regenerate outputs and the genealogy whenever a model's physics,
  `metadata.yaml` `parents`, or `maturity_level` changes.
- `models/` and `feynlag_models/` are installed as packages. If you add a new top-level
  package or the project was installed before a directory existed, run
  `uv sync --reinstall-package feynlag-models`.
- `uv run` silently re-syncs `.venv` to whatever feynlag commit `pyproject.toml` pins on the
  current branch. Branches can pin different commits.

## Architecture

The flow is `SMPieces` → feynlag `Model` → `ModelBundle` → tests, outputs and UFO.

- **`models/sm/model.py` is the root and the parent of everything.**
  - `pieces(benchmark, higgs=True)` returns a `feynlag_models.bundle.SMPieces`: the gauge
    groups, one fermion generation (t, b, τ, ν_τ, with colour), the parameter list, and
    sector-tagged Lagrangian terms, before any `Model` exists.
  - `higgs=False` omits the Higgs doublet and Yukawas, for models that replace the scalar
    sector, like the 2HDM.
  - Reusable pieces: `yukawa_terms(p, Hd, Hu, ye, yd, yu)` builds the Yukawas for any pair of
    doublets. `dirac_specs(p)` gives the Dirac fermions for export. `ew_boson_particles`
    and `width_params` give the UFO boson particles and width inputs.
- **Each child `models/<id>/model.py` is "parent + delta".** It calls `sm.pieces(...)`,
  appends fields, parameters and `p.add_term(expr, sector, name)`, then assembles the `Model`.
  - `build()` then solves tadpoles, registers rotations (the Weinberg and W± rotations via
    feynlag's `to_physical_basis` or the primitives), and returns a `ModelBundle`.
  - The bundle holds the model, the physical `bosons` dict, the conjugate map, the charges,
    a `ParameterSet` including the mass and angle internals, the Dirac specs, the UFO
    particles, the Goldstones, and model-specific handles in `extra`.
  - Term `name`s matter: tests identify terms by name, for example
    `only_failures(report, ["soft_z2_breaking"])`.
  - A model may define `outputs(bundle, out_dir)`, usually via
    `feynlag_models.outputs.standard_outputs`.
- **The numeric benchmark lives only in `metadata.yaml → benchmark.inputs`.** Models read it
  via `feynlag_models.metadata.benchmark_inputs`, and `build(benchmark=dict)` overrides it.
  `bundle.values()` evaluates every parameter at that point.
- **`feynlag_models/` is shared and model-independent.**
  - `checks.py`: `assert_dual_equal` (symbolic `simplify` plus feynlag's `numeric_equal`),
    Goldstone and massive-boson counting, and `only_failures`.
  - `ufo.py`: `export_ufo`, a unitary-gauge export. It drops Goldstone legs and applies the
    documented sign flip of the W⁺W⁻γ/Z triple-gauge coupling. `flatten_fermion_vertices` merges
    chiral keys into FFS/FFV vertices. `DiracSpec.copies` lists the redundant quark colour
    components to skip. `exported_vertex_classes` reads a written UFO.
  - `metadata.py`: the v2 validator. `registry.py`: model discovery. `stamp.py`:
    `STAMP.json` provenance.
- **Tests.**
  - Each model has `tests/conftest.py` with a **session-scoped** fixture that calls `build()`
    once (building and extracting take 10–60 s), plus files `test_l0_l1.py`,
    `test_l2_literature.py` and `test_l3_ufo.py`.
  - `tests/test_repo.py` validates every `metadata.yaml`. It checks that each `ufo_scope`
    matches the committed UFO. It has one negative test per validator rule, each run on a
    tampered copy of the 2HDM metadata. If you rename a test or change a discrepancy's
    status in `models/thdm_type2`, update those negative tests.
- **`scripts/build_outputs.py --check`** regenerates into a temporary directory and diffs the
  result against the committed outputs. It ignores exactly two volatile items: `STAMP.json`,
  and the `__date__` line feynlag writes into the UFO `__init__.py`.

## Hard rules

- **Never modify feynlag.** If something is missing or wrong, add a row to
  `FEYNLAG_GAPS.md` saying what was attempted, what failed, and which item stopped. Then stop
  that item or keep a clearly labelled workaround *outside* feynlag, and pin the bug with a
  strict xfail. Check `FEYNLAG_GAPS.md` for open gaps and the workarounds that still apply at
  the current pin before building on the affected features.
- **One source of truth for conventions: `CONVENTIONS.md`.** It fixes the metric, potential
  signs, VEV normalisation, `rotation_2x2(θ) = [[c, s], [−s, c]]` with new = R·old, the
  Feynman-rule definition, and names and PDG codes. Any difference from a paper goes into
  `metadata.yaml`: an entry in `discrepancies` (`status: convention` if that is all it is)
  and a `conventions_map` on the reference. Do not leave it only in a test docstring.
- **Honesty rules (strict).**
  - Never invent numerical reference values, experimental bounds, equation numbers or
    citations. Write `TODO(verify)` instead. `REPORT.md` lists them all.
  - Tests against the literature cite the equation or table they reproduce, through
    `literature_checks` (ref key, structured `location`, exact `source_version`,
    `checked_on`).
  - In prose, tag statements **[feynlag-verified: test]** or **[physics judgment]**.
  - Never weaken a failing test. A paper relation we do not reproduce becomes a strict
    `xfail`, recorded as an `open` discrepancy, next to a passing test for the independently
    derived result.
  - `maturity_level` must be honest. `maturity_evidence` must name existing, non-xfail tests.

## Maturity levels (definition of done)

- **L0**: fields declared, Lagrangian invariant (gauge and declared discrete symmetries), anomalies cancel.
- **L1**: tadpoles solved, full spectrum, Goldstone counting correct.
- **L2**: key masses, mixings and vertices checked against the literature, both symbolically
  and at random numeric points.
- **L3**: UFO exported and round-tripped (`verify_ufo_numeric`).
- **L4**: MadGraph cross-section check with `slow_evidence` filled in. Otherwise stay at L3.
  MadGraph is installed at `~/.local/mg5dl/MG5_aMC_v3_7_2`. No model has reached L4 yet.

## metadata.yaml (schema version 2)

`schema/metadata.schema.json` gives the shape, and `feynlag_models.metadata.validate` adds
the cross-checks:
- Evidence and key-result tests must exist and must not be xfails.
- An `open` discrepancy or a `feynlag_gaps` entry that names a test must point at a strict xfail.
- `feynlag_gaps` ids must be rows of `FEYNLAG_GAPS.md`.
- References cited by literature checks at L2 or above need `inspire` or `doi`. Software
  references need `url` and `commit` instead.
- `benchmark.placeholders` (for example guessed widths) must be a subset of `benchmark.inputs`.
- `outputs.ufo_scope` must be present exactly when `outputs.ufo` is set.
- L3 requires a UFO, and `slow_evidence` is required exactly at L4.
- `parents` entries are `{id, relation: extends | replaces_sector, sector?}`, and the
  genealogy is built from them alone.

## Physics and SymPy traps met in this repository

- Closed forms containing `sqrt` or `atan`, like mixing angles and eigenvalues, only simplify
  on a fixed branch. Substitute a positive dummy that encodes the benchmark regime, as
  `_branch()` does in `models/sm_singlet_z2/tests/test_l2_literature.py`. Never feed a raw
  difference to `sqrt`.
- Substitute the angle solution *before* setting a coupling to zero (`.subs(θ, sol).subs(λ, 0)`).
  The other order leaves an unsimplifiable `atan(0/…)`.
- Write small differences in a cancellation-free form. The seesaw light mass is
  `2m_D²/(√(M_R²+4m_D²)+M_R)`, not `(√…−M_R)/2`, so the UFO card keeps its precision.
- Mass eigenvalues and angles live in `InternalParameter`s whose expressions still contain the
  angle symbol. Resolve them with `bundle.params.resolve()` or `bundle.values()`, or
  substitute `rot.angle_solution`.

## Reading the literature

- WebFetch cannot read arXiv PDFs. Download them with `curl` and read them with
  `pdftotext -layout`. Check the bracket structure of displayed equations before declaring a
  sign discrepancy: a dropped bracket once produced a false one (2HDM D-1).
- Take INSPIRE ids, DOIs and journal details from the INSPIRE API, for example
  `curl -G https://inspirehep.net/api/literature --data-urlencode "q=arxiv:1106.0034"`.
  Record `verified_against` honestly (`arxiv_text`, `published`, `inspire_record`,
  `source_code`, `none`).
- Physics Reports and other Elsevier journals are paywalled from here.

## Workflow

- **New model.**
  1. Copy `templates/new_model/` to `models/<id>/` and fill in `metadata.yaml` first.
  2. Write `model.py` as parent + delta.
  3. Climb the levels one at a time, with one commit per level, running the tests each time.
  4. Regenerate outputs and the genealogy, and update `last_reviewed`.
- **Shared checkout.** Other Claude sessions may work in this checkout, including feynlag-gap
  work on its own branches. Check `git status` and `git branch` before committing, and stage
  explicit paths rather than `git add -A`.
- **Commits.** There is no global git identity on this machine. Commit with
  `git -c user.name="Moises Zeleny" -c user.email="moiseszeleny@gmail.com" commit ...`.
