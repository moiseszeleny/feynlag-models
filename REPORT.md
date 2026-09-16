# Pilot report — feynlag-models (2026-09-16)

Scope: freeze the format on `sm` (root) + three extensions. feynlag pinned at
`92b5d909714ac01754c0e7c16f19871471122f07` (origin/main), sympy 1.14.0, Python 3.13.

## Maturity reached

| model | claimed | evidence | notes |
|---|---|---|---|
| `sm` | **L3** | 10 tests | UFO round-trip with t, b, τ, ν, EW bosons; L4 not re-claimed (feynlag's own MadGraph benchmark covers EW+leptons) |
| `sm_singlet_z2` | **L3** | 13 passed + 2 strict xfail | Robens–Stefaniak Eqs. (7)–(13) reproduced (α = −θ, regime λ_S v_S² > λ v²); gaps FG-1, FG-2 |
| `seesaw_type1` | **L2** | 10 tests | Takagi spectrum, seesaw series, Atre et al. Eq. (2.5) couplings; **L3 stopped** (FG-3, no Majorana UFO) |
| `thdm_type2` | **L3** | 14 passed + 1 strict xfail | GH Eqs. (6)–(17), Branco Eq. (16)/Table 2; benchmark inverted from (125, 300, 300, 320) GeV re-derived exactly by feynlag |

Fast suite: `56 passed, 3 xfailed` (115 s). `scripts/build_outputs.py --check` and
`scripts/build_genealogy.py --check` pass (outputs reproducible modulo `STAMP.json`).

## Failing / skipped / xfail tests (none weakened)

- `sm_singlet_z2::test_feynlag_mass_matrix_real_scalar_gap` — **strict xfail**, FG-1 (feynlag bug).
- `sm_singlet_z2::test_feynlag_discrete_kinetic_gap` — **strict xfail**, FG-2 (feynlag bug).
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

## FEYNLAG_GAPS.md (three entries)

- **FG-1** `Model.mass_matrix` double-shifts a real VEV'd scalar (`Scalar(real=True)` + `expand_vev`):
  every scalar block is evaluated at `S = 2v_S`. Workaround outside feynlag: `feynlag_models.checks.scalar_mass_block`.
- **FG-2** `check_discrete_invariance` false-fails on `Dmu`-built kinetic terms even when the group does
  not act on the field. Z₂ is verified term by term on the non-kinetic sectors.
- **FG-3** No UFO export for Majorana fermions → `seesaw_type1` stops at L2.

Additional limitations recorded in the cards (not gaps stopping an item): unitary-gauge UFO only;
quartic gauge self-couplings in the rotated basis and gluon vertices are not exported; widths of new
scalars are placeholder inputs; one generation, no CKM.

## Schema changes recommended before scaling

1. `literature_checks[].where` → structured `{equation, table, source_version, checked_on}` instead of free text; make `checked_on` mandatory.
2. Add a top-level `discrepancies:` list (`{quantity, ref, where, status: open|resolved, test}`) — the Branco relative-sign case shows this is needed.
3. Add `conventions_map:` (`{their_symbol: our_symbol, note}`) per reference; today it lives in test docstrings.
4. `benchmark` → `{inputs: {...}, derived_from: {...}, placeholders: [WH2, ...]}` so inverted physical points and placeholder widths are machine-readable.
5. `references[]`: make `inspire` or `doi` mandatory at L2+, add `verified_against: arxiv_v2_text|published`.
6. `parents[]` → `[{id, relation: extends|replaces_sector}]` (the 2HDM replaces the Higgs sector).
7. `maturity_evidence` should list known `xfail` gap tests explicitly (`gap_tests:`), and `outputs` should carry `ufo_scope` (gauge, exported vertex classes).
8. `new_fields[].u1y` as a string rational always (`"1/2"`), and `extra_charges` values typed.
9. Consider `slow_evidence:` for L4 (MadGraph run id, process, numbers) so L4 claims are auditable.

## What to do next

- Decide whether FG-1/FG-2 get fixed in feynlag (the strict xfails flip automatically when they are).
- Attempt L4 for `sm_singlet_z2` (`e⁺e⁻ → Z h1` vs stock `sm` × cos²θ) with the MG5 at `~/.local/mg5dl`.
- Resolve the Branco Eq. (16) sign question and the Eqs. (5)–(6) normalisation against the published text.
