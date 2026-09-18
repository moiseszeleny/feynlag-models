# Pilot report — feynlag-models (2026-09-16)

Scope: freeze the format on `sm` (root) + three extensions. feynlag pinned at
`92b5d909714ac01754c0e7c16f19871471122f07` (origin/main), sympy 1.14.0, Python 3.13.

## Maturity reached

| model | claimed | evidence | notes |
|---|---|---|---|
| `sm` | **L3** | 10 tests | UFO round-trip with $t$, $b$, $\tau$, $\nu$ and the EW bosons; L4 not re-claimed (feynlag's own MadGraph benchmark covers EW+leptons) |
| `sm_singlet_z2` | **L3** | 13 passed | Robens–Stefaniak Eqs. (7)–(13) reproduced ($\alpha = -\theta$, regime $\lambda_S v_S^2 \gt \lambda v^2$); gaps FG-1, FG-2 resolved |
| `seesaw_type1` | **L2** | 10 tests | Takagi spectrum, seesaw series, Atre et al. Eq. (2.5) couplings; **L3 stopped** (FG-3, no Majorana UFO) |
| `sm_ckm` (added 2026-09-17) | **L3** | 12 passed + 1 strict xfail (FG-4) | three generations, CKM through a unitary $d_L$ rotation; PDG 2024 CKM review Eqs. (12.2), (12.3), (12.27), (12.28) and $J$; GIM derived |
| `thdm_type2` | **L3** | 14 passed + 1 strict xfail | GH Eqs. (6)–(17), Branco Eq. (16)/Table 2; benchmark inverted from (125, 300, 300, 320) GeV re-derived exactly by feynlag |

Fast suite at the end of the pilot: `56 passed, 3 xfailed` (115 s); see the schema v2 section for the current count. `scripts/build_outputs.py --check` and
`scripts/build_genealogy.py --check` pass (outputs reproducible modulo `STAMP.json`).

## Failing / skipped / xfail tests (none weakened)

- ~~`thdm_type2::test_charged_higgs_quark_lepton_relative_sign_branco`~~ — removed: the "discrepancy" was a
  transcription error (see "2HDM discrepancies re-checked" below).
- `thdm_type2::test_mA_mHp_branco_arxiv_text_eq5_6` — **strict xfail**: Branco et al.'s printed $m_A^2$, $m_{H^\pm}^2$
  prefactors (discrepancy D-2).
- No test is skipped. No `slow` (MadGraph) test exists yet: **L4 was not attempted** for any model.

## TODO(verify) list at the end of the pilot (43 markers; 17 after the schema-v2 migration, 6 after 2026-09-17 — see below)

Categories:
1. **Journal details of every reference** (venue/volume/page; `inspire`/`doi` fields are `null`) — all
   models. The arXiv numbers and the equation/table numbers used in tests were read from the arXiv PDF
   texts (`pdftotext`) on 2026-09-16 for Robens–Stefaniak (1501.02234v2), Pruna–Robens (1303.1150v3),
   Atre et al. (0901.3589v2), Branco et al. (1106.0034), Gunion–Haber (hep-ph/0207010); the classic
   seesaw papers (Minkowski, GRS, Yanagida, Mohapatra–Senjanović) were **not** fetched.
2. **Experimental bounds** in every `NEXT_STEPS.md` §2 except the ones read from Robens–Stefaniak
   Table II (singlet $\lvert\sin\alpha\rvert$ ranges) and Atre et al. footnote 1 ($\lvert V_{\mu 4}\rvert^2 \lt 9.2\times10^{-8}$); Run-2 numbers,
   the $B \to X_s\gamma$ bound on $m_{H^\pm}$, $0\nu\beta\beta$, cosmology are all `TODO(verify)`.
3. **Textbook locations** for the SM rules (Peskin–Schroeder chapter/figure; PDG review equation numbers).
4. **Branco et al. Eqs. (5)–(6)** as extracted read $m_A^2 \propto [m_{12}^2/(v_1v_2) - 2\lambda_5]$ and $m_{H^\pm}^2 \propto [\ldots - \lambda_4 - \lambda_5]$,
   inconsistent with Gunion–Haber Eqs. (10)–(11) for the same potential normalisation; we match GH and
   feynlag's own pinned tests.
5. PDG code convention for the heavy neutrino (`9900012`).

## FEYNLAG_GAPS.md (four entries, two resolved)

- **FG-1** (resolved, feynlag PR #19) `Model.mass_matrix` double-shifted a real VEV'd scalar
  (`Scalar(real=True)` + `expand_vev`), evaluating every block at `S = 2v_S`. The workaround
  `feynlag_models.checks.scalar_mass_block` is removed; `sm_singlet_z2` uses `Model.mass_matrix`.
- **FG-2** (resolved, feynlag PR #19) `check_discrete_invariance` false-failed on `Dmu`-built kinetic
  terms. `sm_singlet_z2` now validates with its `Z2` declared; `thdm_type2` checks `Z2` on every term.
- **FG-3** No UFO export for Majorana fermions, so `seesaw_type1` stops at L2.
- **FG-4** (open, found by `sm_ckm`) `fermion_mass_matrix` and `majorana_mass_matrix` mangle integer flavour
  indices. `sm_ckm` reads its mass matrices with `feynlag_models.checks.fermion_mass_block` and pins the gap with a strict xfail.

Additional limitations recorded in the cards (not gaps stopping an item): unitary-gauge UFO only;
quartic gauge self-couplings in the rotated basis and gluon vertices are not exported; widths of new
scalars are placeholder inputs; every model except `sm_ckm` has one generation and no CKM.

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
  for every gauge coupling to fermions (equivalent to $g \to -g$). The SM L2 checks now cite PDG
  equation numbers read from the review instead of an unread textbook.
- **2HDM, D-2 (open):** Branco et al. Eqs. (5)–(6) as extracted give $m_A^2$, $m_{H^\pm}^2$ prefactors
  that differ from Gunion–Haber Eqs. (10)–(11); possibly a PDF-extraction artefact.
- **Singlet, D-1 (convention):** $\alpha = -\theta$, now recorded instead of living only in a docstring.

Suite after the migration: `71 passed, 1 skipped, 3 xfailed` (the skip is the UFO-scope check for
`seesaw_type1`, which declares no UFO). `TODO(verify)` markers: from 43 down to 30; the remaining ones are
experimental bounds in `NEXT_STEPS.md` tables, the open 2HDM sign question, and the heavy-neutrino
PDG code.

## 2HDM discrepancies re-checked (2026-09-16)

The published Branco et al. text could not be read: ScienceDirect returned HTTP 403. The checks below use
arXiv v1, v2 and v3 of Branco et al. and arXiv v3 of Aoki et al. (Phys. Rev. D 80 (2009) 015017), whose
notation Branco's Eq. (16) follows.

- **D-1, resolved (my error).** Eq. (16) has one minus sign in front of a bracket holding both the quark and
  the lepton charged-Higgs terms, and Aoki Eq. (6) is identical. The pilot transcription dropped the bracket.
  Both papers give the two terms the same sign, as feynlag does. The strict xfail became a passing test.
- **D-3, convention (new).** Aoki Eq. (4) defines $H^+$ exactly as we do, yet their Eq. (6) has the opposite
  overall sign to a direct derivation from it. This is equivalent to $H^+ \to -H^+$ and has no observable effect.
- **D-2, open.** Branco's printed $`m_A^2 = [m_{12}^2/(v_1v_2) - 2\lambda_5]\,v^2`$ and $`m_+^2 = [m_{12}^2/(v_1v_2) - \lambda_4 - \lambda_5]\,v^2`$ are
  inline text in all three arXiv versions, so they are not an extraction artefact. They contradict the paper's
  own potential: a plain-SymPy derivation without feynlag, Gunion–Haber Eqs. (10)–(11), and feynlag all give
  $-\lambda_5$ and $-(\lambda_4+\lambda_5)/2$. The printed $m_A^2$ differs by exactly $\lambda_5 v^2$. A strict xfail now encodes the printed
  formulas; whether the published version still has them is unknown.

Lesson recorded: read the bracket structure in `pdftotext -layout` output before declaring a sign discrepancy.

## `sm_ckm` (2026-09-17)

- `sm.pieces(generations=3)`, `yukawa_terms` with matrix couplings, `dirac_specs` for twelve fermions and a
  flavour-aware `DiracSpec.flavor` are shared code; the four existing models' outputs are byte-identical.
- The benchmark CKM angles are PDG 2024 Eq. (12.28) central values, not feynlag's `standard_ckm` defaults
  (0.22500, 0.003675, 0.04182, 1.144), whose PDG edition is `TODO(verify)`.
- $m_u$, $m_d$, $m_s$ are `benchmark.placeholders`; $m_c$, $m_e$, $m_\mu$ are the MadGraph v3.7.2 `sm` defaults.

## Experimental bounds read in (2026-09-17)

Every `NEXT_STEPS.md` §2 table was filled from sources read with `pdftotext` on 2026-09-17; the
`TODO(verify)` count went from 17 to 6, and each survivor now names the source that was read and
why it holds no quotable number (the limit is a contour or a figure, not a printed value).

Read in: PDG 2024 EW review Eqs. (10.21), (10.58), (10.63), (10.65), (10.98), (10.99); PDG 2024
Higgs review Sec. 11.4.1 and Table 11.8; PDG 2024 quark-masses review Eqs. (60.5), (60.7), (60.8);
PDG 2024 $\tau$ and b-quark Listings; PDG 2024 neutrino review Eqs. (14.101), (14.102);
KamLAND-Zen arXiv:2406.11438; Planck 2018 VI arXiv:1807.06209 Eq. (63b); Misiak–Steinhauser
arXiv:1702.04571v1 ($`m_{H^\pm} \gt 580`$ GeV, type II); Fernandez-Martinez et al. arXiv:1605.08774;
ATLAS Nature 607 (2022) 52 (arXiv:2207.00092v2, $\mu = 1.05 \pm 0.06$).

Also settled: the heavy-neutrino PDG code 9900012 is the FeynRules HeavyN UFO's `N1`
(`SM_HeavyN_NLO/particles.py`, downloaded and read), and feynlag's `standard_ckm` defaults are the
**PDG 2022** edition's Eq. (12.28) for three of four values — $`\sin\theta_{13} = 0.003675`$ matches no
edition and stays `TODO(verify)`.

One derived bound is labelled as such: in `sm_singlet_z2`, $`\mu = \cos^2\theta`$ turns the measured
ATLAS signal strength into $`\sin^2\theta \lesssim 0.01`$ ($1\sigma$) / $`\lesssim 0.07`$ ($2\sigma$)
[physics judgment].

## What to do next

- Attempt L4 for `sm_singlet_z2` ($e^+e^- \to Z h_1$ against the stock `sm` result times $\cos^2\theta$) with the MG5 at `~/.local/mg5dl`.
- Check 2HDM discrepancy D-2 (Branco Eqs. 5–6 prefactors) against the published Phys. Rept. text (paywalled from here).
- Fill the experimental-bound tables in each `NEXT_STEPS.md` from current PDG / ATLAS / CMS sources.
