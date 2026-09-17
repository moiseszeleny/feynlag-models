# Pilot report — feynlag-models (2026-09-16)

Scope: freeze the format on `sm` (root) + three extensions. feynlag pinned at
`92b5d909714ac01754c0e7c16f19871471122f07` (origin/main), sympy 1.14.0, Python 3.13.

## Maturity reached

| model | claimed | evidence | notes |
|---|---|---|---|
| `sm` | **L3** | 10 tests | UFO round-trip with t, b, τ, ν, EW bosons; L4 not re-claimed (feynlag's own MadGraph benchmark covers EW+leptons) |
| `sm_singlet_z2` | **L3** | 13 passed | Robens–Stefaniak Eqs. (7)–(13) reproduced (α = −θ, regime λ_S v_S² > λ v²); gaps FG-1, FG-2 resolved |
| `seesaw_type1` | **L2** | 10 tests | Takagi spectrum, seesaw series, Atre et al. Eq. (2.5) couplings; **L3 stopped** (FG-3, no Majorana UFO) |
| `thdm_type2` | **L3** | 14 passed + 1 strict xfail | GH Eqs. (6)–(17), Branco Eq. (16)/Table 2; benchmark inverted from (125, 300, 300, 320) GeV re-derived exactly by feynlag |

Fast suite at the end of the pilot: `56 passed, 3 xfailed` (115 s); see the schema v2 section for the current count. `scripts/build_outputs.py --check` and
`scripts/build_genealogy.py --check` pass (outputs reproducible modulo `STAMP.json`).

## Failing / skipped / xfail tests (none weakened)

- `thdm_type2::test_charged_higgs_quark_lepton_relative_sign_branco` — **strict xfail**: Branco et al.
  Eq. (16) as extracted has a relative minus sign between the `ū d H⁺` and `ν̄ ℓ H⁺` terms; feynlag and a
  hand derivation from the identical `Q̄H₁d_R` / `L̄H₁e_R` structures give the same sign. Needs a check
  against the published version / their sign conventions before the article.
- No test is skipped. No `slow` (MadGraph) test exists yet: **L4 was not attempted** for any model.

## TODO(verify) list (43 markers; `grep -rn "TODO(verify)" models CONVENTIONS.md`)

Categories:
1. **Journal details of every reference** (venue/volume/page; `inspire`/`doi` fields are `null`) — all
   models. The arXiv numbers and the equation/table numbers used in tests were read from the arXiv PDF
   texts (`pdftotext`) on 2026-09-16 for Robens–Stefaniak (1501.02234v2), Pruna–Robens (1303.1150v3),
   Atre et al. (0901.3589v2), Branco et al. (1106.0034), Gunion–Haber (hep-ph/0207010); the classic
   seesaw papers (Minkowski, GRS, Yanagida, Mohapatra–Senjanović) were **not** fetched.
2. **Experimental bounds** in every `NEXT_STEPS.md` §2 except the ones read from Robens–Stefaniak
   Table II (singlet `|sin α|` ranges) and Atre et al. footnote 1 (`|V_μ4|² < 9.2×10⁻⁸`); Run-2 numbers,
   `B → X_s γ` `m_H±` bound, `0νββ`, cosmology are all `TODO(verify)`.
3. **Textbook locations** for the SM rules (Peskin–Schroeder chapter/figure; PDG review equation numbers).
4. **Branco et al. Eqs. (5)–(6)** as extracted read `m_A² ∝ [m12²/(v1v2) − 2λ5]`, `m_H±² ∝ [… − λ4 − λ5]`,
   inconsistent with Gunion–Haber Eqs. (10)–(11) for the same potential normalisation; we match GH and
   feynlag's own pinned tests.
5. PDG code convention for the heavy neutrino (`9900012`).

## FEYNLAG_GAPS.md (three entries, two resolved)

- **FG-1** (resolved, feynlag PR #19) `Model.mass_matrix` double-shifted a real VEV'd scalar
  (`Scalar(real=True)` + `expand_vev`), evaluating every block at `S = 2v_S`. The workaround
  `feynlag_models.checks.scalar_mass_block` is removed; `sm_singlet_z2` uses `Model.mass_matrix`.
- **FG-2** (resolved, feynlag PR #19) `check_discrete_invariance` false-failed on `Dmu`-built kinetic
  terms. `sm_singlet_z2` now validates with its `Z2` declared; `thdm_type2` checks `Z2` on every term.
- **FG-3** No UFO export for Majorana fermions → `seesaw_type1` stops at L2.

Additional limitations recorded in the cards (not gaps stopping an item): unitary-gauge UFO only;
quartic gauge self-couplings in the rotated basis and gluon vertices are not exported; widths of new
scalars are placeholder inputs; one generation, no CKM.

## Schema changes — implemented as schema version 2 (2026-09-16)

All nine recommendations are in `schema/metadata.schema.json` (v2) and enforced by
`feynlag_models/metadata.py::validate`; `tests/test_repo.py` has one negative test per rule.

1. `literature_checks[].location` is structured (`equation|table|section|note`) with required
   `source_version` (exact arXiv version read) and `checked_on`.
2. `discrepancies[]` (`open|resolved|convention`); an open one with a test must point at a strict xfail.
3. `references[].conventions_map` holds the symbol dictionaries that used to live in test docstrings.
4. `benchmark = {inputs, placeholders, derived_from?}`; the 2HDM physical point is now a test
   (`test_benchmark_matches_physical_inputs`), and placeholder widths are machine-readable.
5. References carry `kind` and `verified_against`; those cited by literature checks at L2+ need an
   INSPIRE id or DOI (software: url + commit). All ids and journal details came from INSPIRE API
   records on 2026-09-16; every reference-detail `TODO(verify)` is gone.
6. `parents[] = {id, relation, sector?}`; the genealogy labels edges (`sm -->|replaces higgs| thdm_type2`).
7. `feynlag_gaps[] = {id, test?}` (id must be a row of `FEYNLAG_GAPS.md`, test a strict xfail);
   `outputs.ufo_scope` is required with a UFO and checked against the committed UFO's `vertices.py`.
8. `u1y` and charges are rational strings; `extra_charges` is a typed list `{group, kind, charge}`.
9. `slow_evidence[]` is required exactly at L4 (empty for all four models).

What the migration surfaced:
- **SM, D-1 (convention):** the PDG 2024 EW review, Eqs. (10.2)/(10.6), has the opposite global sign
  for every gauge coupling to fermions (equivalent to g → −g). The SM L2 checks now cite PDG
  equation numbers read from the review instead of an unread textbook.
- **2HDM, D-2 (open):** Branco et al. Eqs. (5)–(6) as extracted give `m_A²`, `m_H±²` prefactors
  that differ from Gunion–Haber Eqs. (10)–(11); possibly a PDF-extraction artefact.
- **Singlet, D-1 (convention):** α = −θ, now recorded instead of living only in a docstring.

Suite after the migration: `71 passed, 1 skipped, 3 xfailed` (the skip is the UFO-scope check for
`seesaw_type1`, which declares no UFO). `TODO(verify)` markers: 43 → 30; the remaining ones are
experimental bounds in `NEXT_STEPS.md` tables, the open 2HDM sign question, and the heavy-neutrino
PDG code.

## What to do next

- Attempt L4 for `sm_singlet_z2` (`e⁺e⁻ → Z h1` vs stock `sm` × cos²θ) with the MG5 at `~/.local/mg5dl`.
- Resolve 2HDM discrepancies D-1 (Branco Eq. 16 sign) and D-2 (Eqs. 5–6 prefactors) against the published text.
- Fill the experimental-bound tables in each `NEXT_STEPS.md` from current PDG / ATLAS / CMS sources.
