# Pilot report — feynlag-models (2026-09-16)

Scope: freeze the format on `sm` (root) + three extensions. feynlag pinned at
`92b5d909714ac01754c0e7c16f19871471122f07` (origin/main), sympy 1.14.0, Python 3.13.

## Maturity reached

| model | claimed | evidence | notes |
|---|---|---|---|
| `sm` | **L3** | 19 passed | UFO round-trip with $t$, $b$, $\tau$, $\nu$ and the EW bosons; L4 not re-claimed (feynlag's own MadGraph benchmark covers EW+leptons) |
| `sm_singlet_z2` | **L3** | 19 passed (FG-8 resolved in feynlag 0.5.1) | Robens–Stefaniak Eqs. (7)–(13) reproduced ($\alpha = -\theta$, regime $\lambda_S v_S^2 \gt \lambda v^2$); gaps FG-1, FG-2 resolved |
| `seesaw_type1` | **L2** | 16 passed + 3 strict xfails (FG-9, FG-10 twice) | Takagi spectrum, seesaw series, Atre et al. Eq. (2.5) couplings; **L3 stopped** (FG-3, no Majorana UFO) |
| `sm_ckm` (added 2026-09-17) | **L3** | 17 passed + 2 strict xfails (FG-9, FG-11) | three generations, CKM through a unitary $d_L$ rotation; PDG 2024 CKM review Eqs. (12.2), (12.3), (12.27), (12.28) and $J$; GIM derived |
| `seesaw_type1_2n` (added 2026-09-24) | **L2** | 20 passed + 1 strict xfail (FG-12) | three generations, two $\nu_R$: rank-2 light sector ($m_{\nu_1} = 0$), Atre et al. Eq. (2.5) per flavour, Ibarra–Ross Eq. (6) reproduced, one-generation limit equals `seesaw_type1`; **L3 stopped** (FG-3) |
| `froggatt_nielsen` (added 2026-10-05) | **L2** | 22 passed + 1 strict xfail (FG-13; the FG-6, FG-7 xfails were removed when both were resolved in feynlag 0.3.0) | three generations, global $`U(1)_{\rm FN}`$ flavon, exact $`c_{ij}(\phi/\Lambda)^{n_{ij}}`$ operators; LNS-2 Eqs. (2.3)–(2.7), (2.19) and LNS-1 Eqs. (5.7), (5.8) reproduced as textures, determinants and $\epsilon \to 0$ scaling; no UFO (not requested) |
| `thdm_type2` | **L3** | 25 passed + 1 strict xfail (D-2) | GH Eqs. (6)–(17), Branco Eq. (16)/Table 2; benchmark inverted from (125, 300, 300, 320) GeV re-derived exactly by feynlag |

Fast suite at the end of the pilot: `56 passed, 3 xfailed` (115 s); see the schema v2 section for the current count. `scripts/build_outputs.py --check` and
`scripts/build_genealogy.py --check` pass (outputs reproducible modulo `STAMP.json`).

## Failing / skipped / xfail tests (none weakened)

- ~~`thdm_type2::test_charged_higgs_quark_lepton_relative_sign_branco`~~ — removed: the "discrepancy" was a
  transcription error (see "2HDM discrepancies re-checked" below).
- `thdm_type2::test_mA_mHp_branco_arxiv_text_eq5_6` — **strict xfail**: Branco et al.'s printed $m_A^2$, $m_{H^\pm}^2$
  prefactors (discrepancy D-2).
- ~~`seesaw_type1_2n::test_feynlag_takagi_generic_matrix_gap`~~ — removed: FG-5 is resolved at the
  `e34b356` pin, and the model now builds with `diagonalize_takagi` itself.
- ~~`froggatt_nielsen::test_feynlag_svd_complex_gap`~~, ~~`froggatt_nielsen::test_feynlag_flavour_dependent_charge_gap`~~
  — removed: FG-6 and FG-7 are resolved at the `feynlag==0.3.0` pin, and the model uses
  `diagonalize_svd(method="numeric")` and `GlobalU1` itself.
- Strict xfails for open feynlag gaps, each named in its `FEYNLAG_GAPS.md` row: FG-9 (`seesaw_type1::test_feynlag_scalar_coupling_indices_gap`, `sm_ckm::test_feynlag_scalar_coupling_integer_indices_gap`), FG-10 (two in `seesaw_type1`), FG-11 (`sm_ckm::test_feynlag_integer_diagonal_flavour_matrix_gap`), FG-12 (`seesaw_type1_2n::test_feynlag_unequal_flavour_mass_block_gap`), and FG-13 (`froggatt_nielsen::test_feynlag_term_coverage_global_symmetry_gap`).
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

## FEYNLAG_GAPS.md (seven entries, four resolved)

- **FG-1** (resolved, feynlag PR #19) `Model.mass_matrix` double-shifted a real VEV'd scalar
  (`Scalar(real=True)` + `expand_vev`), evaluating every block at `S = 2v_S`. The workaround
  `feynlag_models.checks.scalar_mass_block` is removed; `sm_singlet_z2` uses `Model.mass_matrix`.
- **FG-2** (resolved, feynlag PR #19) `check_discrete_invariance` false-failed on `Dmu`-built kinetic
  terms. `sm_singlet_z2` now validates with its `Z2` declared; `thdm_type2` checks `Z2` on every term.
- **FG-3** No UFO export for Majorana fermions, so `seesaw_type1` stops at L2.
- **FG-4** (resolved, feynlag PR #20) `fermion_mass_matrix` and `majorana_mass_matrix` mangled integer
  flavour indices. Each term is now read at its own leg indices; the workaround
  `feynlag_models.checks.fermion_mass_block` is removed and `sm_ckm` uses feynlag's own builder.
- **FG-5** (resolved, feynlag PR #25) `diagonalize_takagi` was symbolic only (`Matrix.diagonalize`) and did
  not finish on the generic $5\times5$ seesaw matrix of `seesaw_type1_2n`. It now goes numeric (mpmath,
  50 digits) for a numeric matrix larger than $2\times2$. The workaround
  `feynlag_models.checks.numeric_takagi` and its `tests/test_checks.py` are removed.
- **FG-6** (resolved, feynlag PR #31, released in 0.3.0) `diagonalize_svd` was real-only: on a complex
  $3\times3$ it returned, without error, a non-unitary $U_L$ and complex "masses". It now takes a numeric
  route (mpmath complex SVD) with unitary rotations. `froggatt_nielsen` gets its masses and
  $`V_{\rm CKM}`$ from it; the workaround `feynlag_models.flavor` and `tests/test_flavor.py` are removed.
- **FG-7** (resolved, feynlag PR #32, released in 0.3.0) No global continuous symmetry and no
  per-generation charges on a `Model`. feynlag's `GlobalU1` takes one charge per flavour, and
  `froggatt_nielsen` declares $`U(1)_{\rm FN}`$ on its exact model; the workaround
  `feynlag_models.checks.global_u1_violations` is removed.

Additional limitations recorded in the cards (not gaps stopping an item): unitary-gauge UFO only;
gluon and QCD vertices are not exported; widths of new scalars are placeholder inputs; every model
except `sm_ckm`, `seesaw_type1_2n` and `froggatt_nielsen` has one generation; `sm_ckm` has the CKM
as an input rotation, and `froggatt_nielsen` derives it numerically from complex Yukawas. (Quartic gauge self-couplings **are** exported as of
the 2026-09-18 pin — see below.)

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

## feynlag pin moved to `efffdb0` (2026-09-18)

feynlag PRs #21 (physical-basis gauge self-couplings) and #23 (charged-Goldstone export
convention) landed; the pin moved from `31df7e1` to `efffdb0` and all four UFOs were
regenerated. Three consequences, each verified rather than assumed:

- **Quartic gauge couplings are now exported.** `Model.gauge_vertices(groups=[SU2L], basis=…)`
  derives the weak $\to$ physical rotation from the model's own `Rotation`s and returns VVV *and*
  VVVV, so `feynlag_models/ufo.py` no longer hand-types the electroweak matrix. `VVVV` joins
  `ufo_scope.vertex_classes` in all four models and leaves every `omitted` list.
- **The triple-gauge sign flip left this repository.** It is now feynlag's field $\to$ particle leg
  sign, applied by the writer. Removing our copy was mandatory, not cosmetic: keeping it would
  have applied the flip twice. The regenerated $AW^+W^-$ / $ZW^+W^-$ vertices come out with
  both the value **and** the leg order of MadGraph's stock `sm` (previously the legs were
  emitted transposed with a compensating sign — the same physics, harder to compare).
- **The 2HDM's ten VSS couplings changed sign** ($Zhh_3$, $Zh_2h_3$, $ZH^+H^-$, $\gamma H^+H^-$,
  $W^\mp H^\pm h/h_2/h_3$). feynlag's `VSS1` now carries the unconditional $-1$ that maps its
  $`\partial_\mu \to ip_\mu`$ onto UFO's; nothing applied it before, so those exports had been
  wrong by a sign since the pilot. `\gamma H^+H^-` now reproduces stock `sm`'s $\gamma G^+G^-$
  entry ($-i e$) exactly. No Lagrangian-level result moved — this is an export convention
  [feynlag-verified: `models/thdm_type2/tests/test_l3_ufo.py::test_vss_couplings_match_stock_sm`].

New pin: `models/sm/tests/test_l3_ufo.py` compares the exported cubic, quartic and
scalar–vector bosonic couplings to MadGraph's stock `sm` entry-by-entry (`GC_4`, `GC_53`,
`GC_5`, `GC_35`, `GC_36`, `GC_57`, `GC_72`, `GC_81`, `GC_34`, `GC_65`), the quartics in the
convention-free metric-pair basis. The `sm` benchmark already *is* the stock electroweak
point, so the comparison needs no MadGraph installation and runs in the fast suite. Nothing
pinned those signs before; only `build_outputs.py --check` would have noticed, as a diff.

The ten VSS couplings are pinned by `models/thdm_type2/tests/test_l3_ufo.py::test_vss_couplings_match_stock_sm`;
`models/sm` cannot, because the SM UFO has no VSS vertex in unitary gauge. In the Higgs basis the
second doublet couples to the gauge bosons like the SM doublet, with
$`\rho_\perp = \cos(\beta-\alpha)\,h - \sin(\beta-\alpha)\,H`$, so each vertex is a stock Goldstone vertex
(`GC_3`, `GC_61`, `GC_37`, `GC_60`, `GC_39`, `GC_38`) times $\cos(\beta-\alpha)$ or $-\sin(\beta-\alpha)$.
Charged Goldstone legs are divided by $i^q$, because $H^\pm$ carries no Goldstone phase.
Six vertices are pinned absolutely. Four of those, the charged $W$ ones, are not conjugate pairs,
so they tell an unconditional $-1$ from a pair-only one. The four vertices with an $A$ depend on the
sign of $A$ relative to MadGraph's $G^0$, a field convention, so they are pinned to share one sign.
Mutation checks (2026-09-19, run outside the repository): the pre-`efffdb0` UFO fails all six absolute
pins; a pair-only rule fails the four charged $W$ pins; flipping one $A$ vertex fails the other three.
The two conjugate-pair vertices alone would have passed the pair-only rule
[feynlag-verified: same test].

Fast suite after the pin and this test: `116 passed, 1 skipped, 1 xfailed`.

## `seesaw_type1_2n` (2026-09-24)

Built for `feynlag-anomalies` (`anomalies/neutrino_mass`), whose stage-1 fit needs two independent
$\Delta m^2$: `seesaw_type1` has $\operatorname{rank} m_\nu \le \min(n_L, n_R) = 1$. The request's
placeholder id `seesaw_type1_2N` is not a valid id (`^[a-z0-9_]+$`), hence `seesaw_type1_2n`.

- Three verified facts about feynlag that the model relies on. `fermion_mass_matrix` at
  `nflavors=3` returns a $3\times3$ whose third column is exactly zero (no $\nu_{R3}$), so the $3\times2$
  $m_D$ is a slice [feynlag-verified: `test_mass_matrix_entries`]. `MajoranaRotation` works at
  $n_L = 3$ (first use with $n_L \gt 1$ anywhere). And `MajoranaRotation.apply(expr, idx, n)` sums `expr` over every
  combination of `idx` even when `expr` does not contain it: with integer flavour indices it
  must be called as `apply(L, (), 1)`, or every term is counted $n^2$ times.
- The benchmark is a hand-chosen generic real Yukawa (light masses $\approx 0.016$ and $0.040$ eV);
  it is not a fit. A fit belongs to `feynlag-anomalies`, and the Ibarra–Ross Eq. (6) test shows the
  model maps $(m_2, m_3, U, z)$ to the right Yukawa.
- Literature read with `pdftotext` on 2026-09-24: Ibarra–Ross arXiv:hep-ph/0312138v2 (Secs. 2–3,
  Eqs. (1)–(6)), Frampton–Glashow–Yanagida arXiv:hep-ph/0208157, Atre et al. arXiv:0901.3589v2
  Eqs. (2.3)–(2.5). INSPIRE ids and DOIs from the INSPIRE API. The index-layout and sign difference
  from Ibarra–Ross is discrepancy D-1 (`convention`).
- Two new `TODO(verify)` markers, both in `models/seesaw_type1_2n/NEXT_STEPS.md` §2 (oscillation-fit
  values and heavy-neutral-lepton bounds, deliberately not quoted from memory).
- Fast suite with this model: `177 passed, 2 skipped, 2 xfailed` (about 7 minutes); the new model
  adds about 60 s. `build_outputs.py --check` and `build_genealogy.py --check` pass.

## feynlag pin moved to `e34b356` (2026-09-25)

feynlag PR #25 (numeric Takagi, FG-5) landed; the pin moved from `efffdb0` to `e34b356`, which also
brings in PR #24 (PyPI packaging, no library change). `seesaw_type1_2n` now builds its $U$, $D$ with
feynlag's `diagonalize_takagi`, and its tests use it too (`method="numeric"` for the $3\times3$ light
block and the L2 re-diagonalisations at other points). Two things were checked rather than assumed.
First, the new route reproduces the workaround: $U$ agrees to $2\times10^{-38}$ and $D$ to $10^{-47}$
at the benchmark. Second, the massless light state is now an exact $D = 0$ instead of the
workaround's $`4\times10^{-49}`$ remainder. No test tolerance changed, and `build_outputs.py --check` finds every
model's outputs up to date at the new pin; every `STAMP.json` was regenerated to record `e34b356`.
Every stamp before this one said `repo_dirty: true`, because `build_outputs.py` deletes `outputs/`
before stamping; `feynlag_models/stamp.py` now counts only changes outside the generated
`outputs/` directories as dirty.

Fast suite at this pin: `176 passed, 2 skipped, 1 xfailed` (the xfail is 2HDM D-2).

## `froggatt_nielsen` (2026-10-05)

Built for `feynlag-anomalies` (`puzzles/flavor_puzzle`, `model_requests/froggatt_nielsen.md`), whose
stage-1 fit (P3) needs the Yukawas as symbolic functions of $\epsilon$ and the $`c_{ij}`$ and a numeric
route to masses and $`V_{\rm CKM}`$. The request asked for L2; L2 is reached.

- **Design.** Parent `sm_ckm` (`replaces_sector: yukawa`). A complex singlet flavon $\phi$ (FN charge $+1$)
  and a **global, exact** $`U(1)_{\rm FN}`$, so the flavon phase $a$ is a massless Goldstone; the choice is
  recorded in `metadata.yaml` [physics judgment]. The per-generation fermion charges are integer
  benchmark inputs (`qQ1` … `qe3`). `build()` assembles two `Model`s: `extra["model_exact"]` with the exact
  $`c_{ij}(\phi/\Lambda)^{n_{ij}}`$ operators (dimension up to 10 at the benchmark) for L0 and the mass
  matrices, and `bundle.model` with $\phi^n$ linearised in the flavon fluctuation for the spectrum and
  vertices. The linearisation is exact at the vacuum and in one-flavon couplings and drops vertices with
  two or more flavons on a fermion pair; extracting the exact operators was about ten times slower.
- **Benchmark.** Quark charges are the LNS "master model", LNS-2 Eq. (2.5), under
  $q(Q_L) = H(Q)$, $q(f_R) = -H(\bar f)$ (their $S$ is our $\phi^*$). $\epsilon = 0.2$ from
  $v_\phi = 2\sqrt2$ TeV and $\Lambda = 10$ TeV. Lepton charges (a copy of the down sector), $\Lambda$ and the
  flavon couplings are `benchmark.placeholders`. The 27 complex $`c_{ij}`$ are one seeded draw
  (`default_rng(20261005)`), **not a fit**.
- **Tests.** L0/L1: 7 passed (exact operators valid, $`U(1)_{\rm FN}`$ per monomial with a negative
  control, flavon powers, tadpoles, CP-even block, four massless scalars, mass matrices from both models)
  and 2 strict xfails (FG-6, FG-7; both since removed, see below). L2: 7 passed against LNS-1 (hep-ph/9212278v1) and LNS-2
  (hep-ph/9310320v1): the master-model charges, the Eq. (2.6) textures symbolically, $\det Y$ exactly
  $\epsilon^{12}$ and $\epsilon^{9}$ (Eqs. (2.7), (2.19)), and the mass (Eq. (2.4)) and CKM (Eq. (2.3);
  LNS-1 Eqs. (5.7), (5.8)) scaling. "$X \sim \epsilon^p$" is tested as $`X/\epsilon^p`$ converging to a
  finite $O(1)$ limit between $\epsilon = 10^{-3}$ and $10^{-4}$ at 20 random $O(1)$ draws. The one-flavon
  couplings ($`\lvert n_{ij}\rvert M_{ij}/v_\phi`$ for $s$, $`n_{ij} M_{ij}/v_\phi`$ for $a$) are derived, not a literature check: LNS do not state them
  [physics judgment]. The helper `feynlag_models.flavor` had its own `tests/test_flavor.py` (21 passed).
- **Two new feynlag gaps.** FG-6 (`diagonalize_svd` real-only; workaround `feynlag_models.flavor`,
  `mpmath.svd_c` at 30 digits) and FG-7 (no global $U(1)$ or per-generation charges; workaround
  `feynlag_models.checks.global_u1_violations`). Both were resolved in feynlag 0.3.0 (2026-10-07):
  the model now uses feynlag's numeric `diagonalize_svd` and `GlobalU1`, the workarounds and the two
  strict xfails are removed, and the benchmark masses and $\lvert V_{ij}\rvert$ in `spectrum.md`
  are unchanged.
- **No UFO.** Not requested (P3 is gated at L2), and the export would carry the massless $a$; so L3 is
  not attempted, and `outputs` has the LaTeX and Markdown pages only.
- **Literature.** LNS-1 and LNS-2 read as arXiv v1 text with `pdftotext`, exponents checked against
  page renders; INSPIRE ids (341758, 359267) and DOIs from the INSPIRE API. Froggatt–Nielsen 1979
  (INSPIRE 131306) was **not** read (ScienceDirect 403, CDS bot challenge), so none of its equations is
  cited. New `TODO(verify)` markers, all in `models/froggatt_nielsen/NEXT_STEPS.md`: FN 1979 equations
  not read; published NPB versions of LNS-1 and LNS-2 not compared with the arXiv text; an exact
  literature source for the flavon couplings; bounds on $v_\phi$ from meson mixing and familon emission.

## CP-even labels: UG-4 (2026-10-28)

The ticket UG-4 in `feynlag-anomalies/docs/upstream_gaps.md` found two models whose CP-even labels
depend on the ordering of the diagonal entries of the mass matrix.

- **`thdm_type2` (fixed).** feynlag's `diagonalize_orthogonal_2x2` returns the principal branch,
  $`\tfrac12\arctan\big(2M_{12}/(M_{11}-M_{22})\big)`$, and promises no mass ordering, so this is
  not a feynlag gap. For $M_{11} \lt M_{22}$ the model's $H$ was the lighter state, against
  `CONVENTIONS.md` and Gunion–Haber. `model.alpha_branch` now shifts the branch by $\pm\pi/2$, so
  $`\alpha = \tfrac12\,\mathrm{atan2}(2M_{12}, M_{11}-M_{22})`$ and $h$ is the lighter state at every
  benchmark. At the committed benchmark ($M_{11} \gt M_{22}$) the shift is zero and every output is
  byte-identical. New tests: `test_labels_follow_mass_at_an_inverted_point` (the anomalies point
  $\tan\beta = 2$, $`\sin(\beta-\alpha) = 0.3`$, $m_h = 95$, $m_H = 125.2$ GeV; it failed with the
  labels swapped before the fix) and `test_alpha_branch_is_atan2`.
- **`sm_singlet_z2` (documented).** The labels follow mixing ($h_1$ is $h$-like), which
  feynlag-anomalies relies on. The $\mp$ key result and the benchmark wording now say that they
  hold for $M_{11} \lt M_{22}$. New test: `test_labels_follow_mixing_with_a_light_singlet`.

## `sm` on the feynlag 0.4.0 API (2026-11-17)

First of seven per-model migrations to feynlag 0.4.0's model-building API. All outputs are byte-identical
(`build_outputs.py --check` clean for all seven models, nothing regenerated).

- **Terms.** The one-generation Yukawas in `sm.yukawa_terms` are `feynlag.terms.yukawa(...)` (`tilde(H)` for
  the up quarks), also for the 2HDM's `Hd ≠ Hu`. The fermion currents are `feynlag.terms.kinetic(...)`, kept as one
  `gauge` term. The three-generation branch (explicit `Matrix` couplings at integer flavour indices) stays at
  component level until the `sm_ckm` migration: `yukawa()` takes a scalar coupling (one shared index) or an
  `IndexedBase` (two distinct indices). The Higgs sector keeps `higgs_lagrangian` for its term names.
- **Physical basis.** `model.mass_blocks(kind="gauge")` plus `model.diagonalize(...)` replace `to_physical_basis`.
  The scalar `mass_blocks` supply `h`, `G0`, `G+` (no rotation). Charges, conjugates and Goldstones come from
  `model.physical` (charges derived from the vacuum, no longer declared). The Weinberg matrix is now written
  $`g/\sqrt{g^2+g'^2}`$ instead of $`1/\sqrt{g'^2/g^2+1}`$, equal to $R(-\theta_W)$ **[feynlag-verified:
  test_gauge_rotations_conventions]**.
- **Parameters.** MW, MZ, MH are declared with `ParameterSet.internal` and `Model(parameters=P)` gets the full set.
- **Equality proof.** A comparison against the pre-migration build found every Lagrangian term (expanded),
  all 38 boson Feynman rules, every fermion vertex coefficient, every physical-basis sector, the masses,
  tadpole, rotations, bosons (symbol, assumptions, tex), cmap, charges, conjugates, Goldstones and the
  Dirac/UFO specs equal.
- **New tests.** `test_constructors_reproduce_component_yukawas`, `test_gauge_rotations_conventions`,
  `test_physical_registry`, `test_term_coverage` (no missing invariant, no remainder) and
  `test_summary_and_parameters` (no undeclared symbol).

## `sm_singlet_z2` on the feynlag 0.4.0 API (2026-11-18)

Second per-model migration. All outputs are byte-identical (`build_outputs.py --check` clean for all seven models).

- **Guided basis.** The CP-even $(H^0_r, S)$ block now comes from `model.mass_blocks(kind="scalar")`, with entries
  $2\lambda v^2$, $\lambda_{HS} v v_S$, $2\lambda_S v_S^2$. That is the same matrix as before, so FG-1's double shift does
  not reappear on this path **[feynlag-verified: test_mass_blocks_cp_even_no_double_shift]**. `model.diagonalize(even,
  names=["h1","h2"], angle=theta)` takes the symbolic $\tan 2\theta$ route on the principal branch. It registers
  $R(\theta)$, so $h_1$ stays the $h$-like state and the UG-4 labels follow mixing
  **[feynlag-verified: test_diagonalize_keeps_mixing_labels]**. `values=` is deliberately not passed: it would order
  the states by mass. The gauge rotations use the new shared `sm.ew_gauge_basis`, and charges, conjugates and
  Goldstones come from `model.physical`.
- **Terms and parameters.** $H^\dagger H$ via `inner(H, H)`. Parameters are declared once through `ParameterSet.external`
  and `.internal`, in the previous order, so the UFO parameter order is unchanged.
- **New gap FG-8.** `feynlag.terms.kinetic` gives a real scalar $(\partial S)^2$ instead of $\tfrac12(\partial S)^2$. The
  hand-written kinetic term stays, pinned by the strict xfail `test_feynlag_kinetic_real_scalar_gap`. (Resolved in
  feynlag 0.5.1; see below.)
- **Equality proof** against `main`: every term, rule, fermion vertex, physical-basis sector, the $h$–$S$ rotation
  (matrix, $\theta$, $\tan 2\theta$ relation), $M_{\rm even}$, $m_{h_{1,2}}$, the parameters and their order, and the bookkeeping maps
  are all identical or equal. The one formal difference is the Weinberg matrix's simpler form, as in the `sm` PR.

## feynlag pin moved to `0.5.1`; FG-8 resolved (2026-11-18)

- **Pin.** From `feynlag==0.4.0` to `feynlag==0.5.1` (tag `v0.5.1` = `919aace`). 0.5.0 is additive: two-to-two scattering
  and the pheno layer. Its one deprecation, importing engine names from `feynlag.pheno` itself, does not apply here:
  no file in this repository imports `feynlag.pheno`. On the bump alone, every committed output is byte-identical.
- **FG-8 resolved.** `kinetic(S)` now gives the real singlet $\tfrac12(\partial_\mu S)^2$, so `sm_singlet_z2` builds its
  `singlet_kinetic` term with it. Name and sector are unchanged.
  - The strict xfail became the passing `test_kinetic_real_scalar_canonical` **[feynlag-verified:
    test_kinetic_real_scalar_canonical]**.
  - `feynlag_gaps` is empty again, and the model is physics-equal to the previous `main` (every term identical).

## `thdm_type2` on the feynlag 0.4.0+ API (2026-11-18)

Third per-model migration, at the `feynlag==0.5.1` pin. Every other model's outputs are byte-identical.

- **CP-even block.** `model.mass_blocks(kind="scalar")` gives the $(\rho_1, \rho_2)$, $(\eta_1, \eta_2)$ and $(H_1^+, H_2^+)$ blocks.
  `model.diagonalize(even, names=["H","h"], angle=alpha, values=<benchmark>)` puts the heavier state first: the
  principal $`\tfrac12\arctan\big(2M_{12}/(M_{11}-M_{22})\big)`$, shifted by $\pm\pi/2$ when $M_{11} \lt M_{22}$. That is
  Gunion–Haber's $`\tfrac12\,\mathrm{atan2}(2M_{12}, M_{11}-M_{22})`$, the rule `alpha_branch` applied by hand since UG-4.
  `rot_even`'s angle solution, $\tan 2\alpha$ relation, matrix and $m^2$ are identical to before, both at the benchmark
  (no shift) and at the inverted point (shift $+\pi/2$). `branch_valid_for` is now in `extra`
  **[feynlag-verified: test_diagonalize_branch_matches_alpha_branch]**. `alpha_branch` stays as the independent reference.
- **CP-odd and charged blocks.** The Goldstone-fixed route with `angle=beta` registers exactly `rotation_2x2(beta)`
  with $\tan\beta = v_2/v_1$ attached. $G^-$ and $H^-$ come from `conjugate_names` **[feynlag-verified:
  test_goldstone_fixed_rotations]**. Gauge rotations use `sm.ew_gauge_basis`, the doublet kinetic terms `kinetic(H)`,
  the potential `inner()`, and parameters `ParameterSet.external/internal` in the previous order.
- **Equality proof** against `main`, at the benchmark and at the inverted point: all 154 boson rules and 171 fermion
  coefficients, every term (the kinetic terms expanded-equal), $\alpha$, $\beta$, every rotation, the bookkeeping and
  the parameter order are equal. $m_A$ and $m_{H^\pm}$ are written $`\sqrt{v_1^2+v_2^2}\,(\dots)`$ instead of
  $`\lvert v_1\cos\beta + v_2\sin\beta\rvert\,(\dots)`$. The two are symbolically equal: with $v_1 = v\cos\beta$,
  $v_2 = v\sin\beta$ ($v, \beta \gt 0$) the difference of the squared masses simplifies to zero
  **[feynlag-verified: test_mA_mHp_forms_symbolically_equal_to_previous]**. That is the only output change: two lines
  each in `THDM_TYPE2_UFO/parameters.py` and `spectrum.md`.
- **Coverage.** `term_coverage()` finds every CONVENTIONS.md term with no remainder. It reports as missing exactly
  what a hard $Z_2$ forbids: $\lambda_6$, $\lambda_7$ and the wrong-doublet Yukawas **[feynlag-verified: test_term_coverage]**.

## `seesaw_type1` on the feynlag 0.4.0+ API (2026-11-19)

Fourth per-model migration, at the `feynlag==0.5.1` pin. All outputs are byte-identical (`build_outputs.py --check` clean for
all seven models, nothing regenerated). FG-3 is unchanged: no UFO, `maturity_level: 2`.

- **Terms.** `LYukD` is `yukawa(yv, Ll, tilde(H), nuR)` and `LMaj` is `majorana_mass(MR, nuR, gamma=C P_L)`, in their
  flavour-diagonal form: a scalar coupling is flavour-universal, so both legs carry the one index `i`. The component-level
  terms they replace had the $\nu_R$ leg on `j`. With a scalar $y_\nu$ that coincides with $\delta_{ij}$ only at one
  generation, which is this model **[feynlag-verified: test_constructor_terms_are_the_diagonal_component_terms]**.
- **New gap FG-9.** An explicit `indices=(i, j)` with a scalar coupling is silently ignored. It should raise `ValueError`,
  since a flavour-universal coupling cannot take two distinct leg indices. The strict xfail asserts that both
  constructors raise.
- **`mass_blocks()`.** The scalar and gauge blocks are those of `sm`. The $(\nu_L, \nu_R)$ fermion block is reported,
  not raised, as not diagonalizable, with the note to use `seesaw_mass_matrix` + `diagonalize_takagi` +
  `MajoranaRotation`, which the model keeps **[feynlag-verified: test_mass_blocks_report_majorana_block]**. The gauge and
  Higgs states use the shared `sm.ew_gauge_basis` and the new `sm.sm_higgs_states`. Parameters are declared once,
  in the previous order.
- **New gap FG-10.** `term_coverage()` finds the potential and every dim-4 Yukawa ($y_\nu$ on $\bar L\tilde H\nu_R$
  included). It leaves the gauge-invariant bare Majorana mass as an unmatched remainder, because `suggest_yukawa` does
  not enumerate it (pinned by `test_term_coverage` and the strict xfail `test_feynlag_majorana_mass_coverage_gap`).
- **Equality proof** against `main`, at the level of the physics (one generation, the legacy $\nu_R[j]$ relabelled to
  $\nu_R[i]$):
  - all 38 boson rules, 137 fermion-table coefficients and **164 neutrino mass-basis vertex coefficients** are equal;
  - $m_D$, $M_R$, $M_\nu$, $U$, $D$, the Takagi masses and the `majorana_vertex_markdown` text are identical.
  - Without the relabel, the only differences are the flavour-index label of the $\nu_R$ leg, in the two terms and in
    the keys of the generic fermion table. The neutrino mass-basis vertices, $M_\nu$, $U$, $D$ and the masses agree
    even then.

## Review follow-up to `seesaw_type1` #23 (2026-11-19)

- **Majorana vertex tables at high precision.** `numeric_fermion_markdown` evaluated each coupling at double precision
  with float inputs. These couplings are differences of nearly equal radicals, so the printed digits were wrong:
  - in `seesaw_type1`, the heavy-heavy $`\bar N N Z`$ was printed `1.121e-14` instead of `1.123e-14`; the correct value
    is $`(g_Z/2)\lvert U_{\nu_L N}\rvert^2`$ **[feynlag-verified: test_heavy_heavy_Z_high_precision]**;
  - in `seesaw_type1_2n`, five light-neutrino Yukawa magnitudes of $10^{-23}$ to $10^{-29}$ were wrong, by up to 63%: 20 table
    rows, each magnitude appearing for $h$ and $G^0$ and in both chirality orderings.
  The function now evaluates at 40 digits with exact rational benchmark inputs. A 100-digit Takagi factorisation
  confirms the printed `seesaw_type1_2n` values **[feynlag-verified: test_majorana_table_precision]**. That model's own
  $10^{-40}$ cut already kept the working-precision noise (couplings of the massless $\nu_1$ at about $10^{-52}$ and below)
  out of the table.
- **FG-10 widened.** The row now quotes the `TermCoverage.unmatched` docstring correctly. It covers every fermion in a
  real representation: for a type-III-like triplet $\Sigma$ (SU(2) 3, $Y = 0$), `suggest_yukawa` offers nothing, and
  `majorana_mass` refuses the gauge-invariant $\Sigma^a \Sigma^a$ mass with a false claim. Second strict xfail:
  `test_feynlag_triplet_majorana_gap`.

## `sm_ckm` on the feynlag 0.4.0+ API (2026-11-20)

Fifth per-model migration, at the `feynlag==0.5.1` pin. All outputs are byte-identical (`build_outputs.py --check` clean
for all seven models, nothing regenerated).

- **Three-generation Yukawas.** The shared `sm._yukawa_terms_3`, also used by `seesaw_type1_2n` and `froggatt_nielsen`,
  builds each nonzero entry of the explicit $`3\times3`$ couplings with `feynlag.terms.yukawa`:
  - off-diagonal entries through a placeholder flavour matrix on `(a, b)`;
  - diagonal entries with the scalar form on the one index.
  They equal the component-level terms for $`Y_e`$, $`Y_u`$ (with `tilde(H)`) and the complex
  $`Y_d = V\,\mathrm{diag}(y)`$ **[feynlag-verified: test_constructors_reproduce_component_yukawas_3gen]**.
  All three models are physics-equal to `main`.
- **New gap FG-11.** `yukawa` refuses a flavour-matrix diagonal entry `indices=(a, a)` at an integer index. The check
  is meant for symbolic indices.
- **FG-9 note.** With integer indices the silent collapse moves an off-diagonal entry onto the diagonal. Second
  strict xfail `test_feynlag_scalar_coupling_integer_indices_gap`.
- **FG-4** was already resolved; `NEXT_STEPS.md` no longer describes its removed workaround.
- **`mass_blocks()`.** It reports every charged-lepton and quark block, per colour, as flavoured (numeric SVD
  route) and $`\nu_L`$ as massless, so the CKM stays the input rotation $`d'_L = V d_L`$ (`standard_ckm`, PDG
  Eq. 12.3). Gauge and Higgs states come from `sm.ew_gauge_basis` / `sm.sm_higgs_states`; parameters are declared once
  in the old order.
- **Coverage.** `term_coverage()` recognises the potential. Yukawas at explicit integer flavour indices are, as
  feynlag documents, left unmatched: exactly their $`P_R`$ half **[feynlag-verified: test_term_coverage]**.
- **Equality proof** (`sm_ckm` against `main`): 38 boson rules, **693 fermion coefficients** (charged current with
  $`V_{ij}`$, GIM-cancelled neutral currents, Higgs couplings), every CKM rotation and `V`, `V_expr`, `Yd` are
  identical or equal. The only formal flags are the expanded form of the three Yukawa terms and the Weinberg matrix.

## `seesaw_type1_2n` on the feynlag 0.4.0+ API (2026-11-20)

Sixth per-model migration, at the `feynlag==0.5.1` pin. All outputs are byte-identical (`build_outputs.py --check` clean
for all seven models, nothing regenerated).

- **Dirac Yukawa.** The $`3\times2`$ $`y_\nu`$ goes through the shared `sm._flavour_matrix_term`, now looping over the
  matrix's own shape (identical for the $`3\times3`$ users): off-diagonal entries on `indices=(a, b)`, the `a == b`
  entries `yv_e1` and `yv_mu2` in the single-index form (FG-11). The Majorana mass is one `majorana_mass` per $`k`$.
  Both equal the component-level terms **[feynlag-verified: test_constructors_reproduce_component_neutrino_terms]**.
- **New gap FG-12.** `mass_blocks(kind="fermion")` raises `NotImplementedError` for the $`3\times2`$
  $`(\nu_L, \nu_R)`$ block (different flavour counts), a refusal. The model uses only the scalar and gauge blocks,
  through `sm.sm_higgs_states` / `sm.ew_gauge_basis` **[feynlag-verified: test_mass_blocks_report_sm_blocks]**, and keeps
  the hand-built seesaw matrix, the numeric 50-digit Takagi and `MajoranaRotation`.
- **Coverage.** `term_coverage()` recognises the potential; the four integer-index Yukawas are missing, as documented,
  and the remainder is exactly the $`P_R`$ / $`C P_L`$ half of the Yukawa and Majorana sector, the bare $`\nu_R`$ mass
  included (FG-10) **[feynlag-verified: test_term_coverage]**.
- **Consumer interface** (feynlag-anomalies `neutrino_mass`): every `extra` key is kept; `yv_params` are exactly the
  Yukawa symbols of `Mnu` in a-major order and the masses are increasing **[feynlag-verified: test_consumer_interface]**.
- **Equality proof** (against `main`): 38 boson rules, 435 fermion coefficients and **637 neutrino-basis coefficients**
  equal; `Mnu`, `U`, `D`, `masses`, `MajoranaRotation` and the Majorana vertex page identical. The only formal flags are
  the expanded form of `LYukD` and the Weinberg matrix. `sm_ckm` and `froggatt_nielsen` re-proved equal for the helper
  change.

## `froggatt_nielsen` on the feynlag 0.4.0+ API (2026-11-21)

Seventh and last per-model migration, at the `feynlag==0.5.1` pin. All outputs are byte-identical (`build_outputs.py
--check` clean for all seven models, nothing regenerated).

- **Both models migrated.** `model_exact` (exact $`c_{ij}(\phi/\Lambda)^{n_{ij}}`$, `GlobalU1` U(1)_FN) and the
  linearised `bundle.model` take a `ParameterSet` (the exact one a snapshot, without the linearised internals), in
  the previous order. `validate()` still imposes U(1)_FN on every term **[feynlag-verified: test_global_u1_fn_every_term]**.
- **FN Yukawas.** `L_exact` and `L_linear` (through `sm.yukawa_terms`, the placeholder route for field-dependent
  entries) equal the component-level terms, both at the benchmark and at a charge set with $`n \lt 0`$ entries built
  from $`(\phi^*)^{\lvert n\rvert}`$ **[feynlag-verified: test_constructors_reproduce_component_yukawas_exact_and_linear]**.
- **Flavon.** `kinetic(phiF)` and `inner` give the hand-written $`(\partial\phi)^*(\partial\phi)`$ and potential
  **[feynlag-verified: test_flavon_kinetic_and_potential_constructors]**. The $`(h, s)`$ mixing comes from
  `mass_blocks()` and `diagonalize(…, angle=theta)` with the identical rotation matrix and angle solution; the flavon
  phase $`a`$ is a massless, non-eaten state **[feynlag-verified: test_mass_blocks_report_scalar_gauge_and_flavoured_blocks]**.
- **New gap FG-13.** `term_coverage` ignores `Model.global_groups`: on `model_exact` it reports seven U(1)_FN-violating
  flavon operators as missing, a wrong result **[feynlag-verified: test_term_coverage_model_exact]**.
- **Equality proof** (against `main`): 72 boson rules, **2289 fermion coefficients**, every rotation, `theta`, `MH1`,
  `MH2`, `Yu`, `Yd`, `Ye`, `eps` and the `model_exact` terms, parameters and `validate()` agree. The only formal flag
  is the Weinberg matrix's simpler form.

## What to do next

- Attempt L4 for `sm_singlet_z2` ($e^+e^- \to Z h_1$ against the stock `sm` result times $\cos^2\theta$) with the MG5 at `~/.local/mg5dl`.
- Check 2HDM discrepancy D-2 (Branco Eqs. 5–6 prefactors) against the published Phys. Rept. text (paywalled from here).
- Fill the experimental-bound tables in each `NEXT_STEPS.md` from current PDG / ATLAS / CMS sources.
- `froggatt_nielsen`: rotate the linearised model to the quark mass basis with feynlag 0.3.0's unitary
  `diagonalize_svd` rotations and `Rotation.bar` (flavon FCNC couplings); the stage-1 fit itself belongs
  to `feynlag-anomalies` (P3).
