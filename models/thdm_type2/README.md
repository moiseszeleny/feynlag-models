# Two-Higgs-doublet model, type II (CP-conserving, softly broken Z₂) — physics card

**id** `thdm_type2` · **parents** `sm` · **maturity** L3 (UFO round-trip; no MadGraph run)

Tags: **[feynlag-verified: test]** = pinned by a test in `tests/`; **[physics judgment]** = not machine-checked.

## Problem addressed
The minimal extended Higgs sector: a second doublet gives a charged Higgs `H±`, a CP-odd `A`
and a second CP-even `H`, with natural flavour conservation enforced by a Z₂. Type II (up-type
quarks from `Φ₂`, down-type quarks and leptons from `Φ₁`) is the Yukawa pattern of the MSSM
Higgs sector and the standard target for `tan β`, charged-Higgs and alignment-limit studies. [physics judgment]

## Field content
| field | spin | SU(3)_c × SU(2)_L × U(1)_Y | extra charges | generations |
|---|---|---|---|---|
| `H1` (replaces the SM `H`) | 0 | (1, 2, 1/2) | Z₂: +1 | 1 |
| `H2` | 0 | (1, 2, 1/2) | Z₂: −1 | 1 |
| `uR` (SM field, now Z₂-odd) | 1/2 (R) | (3, 1, 2/3) | Z₂: −1 | 1 |
| + the rest of `sm` | | | Z₂: +1 | |

Anomalies cancel as in the SM (no new fermions) **[feynlag-verified: `tests/test_l0_l1.py::test_validate_invariance_and_anomalies`]**.

## New symmetry and breaking
Z₂: `H2 → −H2`, `u_R → −u_R`. **Softly broken** by the dimension-two term `−m12² (H1†H2 + h.c.)`,
the *only* Z₂-odd term in the Lagrangian **[feynlag-verified: `test_z2_softly_broken_only_by_m12sq`]**
(kinetic terms excluded from the check because of FEYNLAG_GAPS.md FG-2). Electroweak breaking by
`⟨H_i⁰⟩ = v_i/√2`, `tan β = v2/v1`, `v² = v1² + v2²`.

## New Lagrangian terms
`V = m11² H1†H1 + m22² H2†H2 − m12² (H1†H2 + h.c.) + ½λ1 (H1†H1)² + ½λ2 (H2†H2)² + λ3 (H1†H1)(H2†H2) + λ4 |H1†H2|² + ½λ5 [(H1†H2)² + h.c.]`
(Branco et al. Eq. 2; Gunion–Haber Eq. 1 with `λ6 = λ7 = 0`), `|D H1|² + |D H2|²`, and the type-II Yukawas
`−y_τ L̄ H1 e_R − y_b Q̄ H1 d_R − y_t Q̄ H̃2 u_R + h.c.` with `y_b = √2 m_b/v1`, `y_τ = √2 m_τ/v1`, `y_t = √2 m_t/v2`
**[feynlag-verified: `test_fermion_masses`]**.

## Key mechanism
- Tadpoles `m11² = m12² tβ − ½v²(λ1 cβ² + λ345 sβ²)`, `m22²` by `1↔2` (GH Eqs. 6–7) **[feynlag-verified: `test_tadpoles_gunion_haber_eq6_eq7`]**
- Mass blocks: CP-even = Branco Eq. (7) = GH Eqs. (12)–(13); CP-odd and charged `∝ [[v2², −v1v2], [−v1v2, v1²]]`
  with one Goldstone each **[feynlag-verified: `test_mass_blocks`]**; `m_A² = m12²/(sβcβ) − λ5 v²`,
  `m_H±² = m_A² + ½v²(λ5 − λ4)` (GH Eqs. 10–11) **[feynlag-verified: `test_mA_mHp_gunion_haber_eq10_eq11`]**;
  the same values follow from Branco's potential with plain SymPy, no feynlag **[verified: `test_mA_mHp_independent_of_feynlag`]**.
  Branco et al.'s printed formulas (arXiv v1–v3) have `−2λ5` and `−λ4 − λ5` instead, which is inconsistent with their own
  potential (discrepancy D-2, open, strict xfail `test_mA_mHp_branco_arxiv_text_eq5_6`; the published text was not accessible).
- Rotations `(H, h) = R(α)(ρ1, ρ2)`, `(G⁰, A) = R(β)(η1, η2)`, `(G⁺, H⁺) = R(β)(H1⁺, H2⁺)` diagonalise the three blocks;
  three Goldstones for `W±, Z` **[feynlag-verified: `test_spectrum_and_rotations_at_benchmark`, `test_goldstone_count_and_gauge_masses`]**.
  feynlag's `α = ½ atan(2M12/(M11−M22))` has `cos 2α > 0`; the label `H` is the heavier state only when `M11 > M22`
  (true at the benchmark; GH Eq. 17 chooses the branch with `m_H ≥ m_h` instead). [physics judgment on conventions]
- `hVV = SM × sin(β−α)`, `HVV = SM × cos(β−α)`, no `AVV` **[feynlag-verified: `tests/test_l2_literature.py::test_hVV_HVV_sin_cos_beta_minus_alpha`]**
- Type-II Yukawa factors (Branco Table 2): `ξ_h^u = cα/sβ`, `ξ_h^{d,ℓ} = −sα/cβ`, `ξ_H^u = sα/sβ`, `ξ_H^{d,ℓ} = cα/cβ`,
  `ξ_A^u = cotβ`, `ξ_A^{d,ℓ} = tanβ` with the `f̄γ5f` chiral structure for `A` **[feynlag-verified: `test_neutral_yukawa_xi_factors_table2`]**
- Charged Higgs: `|H⁺ t̄ b| = (√2/v)(m_t cotβ P_L + m_b tanβ P_R)` (same sign for both chiralities, as in Branco Eq. 16),
  `|H⁺ ν̄ τ| = (√2/v) m_τ tanβ P_R` **[feynlag-verified: `test_charged_higgs_yukawa_eq16`]**. The d-quark and lepton
  `H⁺` terms come out with the **same** sign (hand derivation from the identical `Q̄H1d_R`/`L̄H1e_R` structure agrees,
  **[feynlag-verified: `test_charged_higgs_quark_lepton_same_sign_derived`]**). Branco et al. Eq. (16) and Aoki et al.
  Eq. (6) put one minus sign in front of a bracket holding both terms, so they agree on this relative sign
  **[feynlag-verified: `test_charged_higgs_quark_lepton_relative_sign_eq16`]**. Their overall sign of the H⁺ line
  is opposite to ours, which is the unobservable redefinition H⁺ → −H⁺ (metadata discrepancy D-3, a convention).
- Alignment `cos(β−α) → 0` recovers every SM `h` coupling **[feynlag-verified: `test_alignment_limit_recovers_sm_h`]**.

## Characteristic scale
`m_A ~ m_H ~ m_H± ~ √(m12²/(sβcβ))` (the soft scale) up to `λ_i v²` splittings; the SM-like limit is
decoupling `m12² → ∞` or alignment `cos(β−α) → 0`. Benchmark: `tan β = 2`, `cos(β−α) = 0.1`,
`(m_h, m_H, m_A, m_H±) = (125, 300, 300, 320) GeV` inverted into `λ_i` (see `outputs/spectrum.md` for the re-derived values). [physics judgment]

## Observables that test it
`B → X_s γ` (type II: strong lower bound on `m_H±`), `B_s → μμ`, `b → s ℓℓ`; Higgs signal strengths
(`sin(β−α)`, `ξ_h^f`); direct searches `A/H → ττ` at large `tan β`, `H⁺ → tb, τν`; electroweak precision (`T`
parameter from the `m_A`–`m_H±` splitting). [physics judgment; see `NEXT_STEPS.md`]

## Genealogy
Parent: `sm` (Higgs sector replaced). Proposed children: `thdm_type1`, `thdm_type_x`/`_y` (other Z₂ charges),
`inert_doublet` (exact Z₂, `v2 = 0`), CP-violating 2HDM (complex `m12², λ5`), 2HDM + singlet (N2HDM),
`thdm_s3` (3HDM with S₃ — feynlag ships the invariant potential machinery). See `GENEALOGY.md`.
