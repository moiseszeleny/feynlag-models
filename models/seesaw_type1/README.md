# Type-I seesaw — physics card

**id** `seesaw_type1` · **parents** `sm` · **maturity** L2 (L3 blocked: feynlag has no UFO path for Majorana fermions, FEYNLAG_GAPS.md FG-3)

Tags: **[feynlag-verified: test]** = pinned by a test in `tests/`; **[physics judgment]** = not machine-checked.

## Problem addressed
Neutrino masses. One gauge-singlet right-handed neutrino with a Dirac Yukawa and a large
Majorana mass gives the light neutrino a tiny Majorana mass `m_ν ≈ m_D²/M_R` and a heavy
partner `N` whose gauge and Higgs couplings are suppressed by the mixing `V ≈ m_D/M_R`. [physics judgment]

## Field content
| field | spin | SU(3)_c × SU(2)_L × U(1)_Y | extra charges | generations |
|---|---|---|---|---|
| `nuR` | 1/2 (R) | (1, 1, 0) | — | 1 |
| + everything of `sm` | | | | |

Anomaly cancellation is untouched (a total singlet) **[feynlag-verified: `tests/test_l0_l1.py::test_validate_invariance_and_anomalies`]**.

## New symmetry and breaking
No new symmetry is imposed. The SM's accidental lepton number `U(1)_L` is **explicitly broken** by
two units by the Majorana mass `−½ M_R ν_Rᵀ C ν_R + h.c.`; the physical neutrinos are Majorana. [physics judgment]

## New Lagrangian terms
`L ⊃ −y_ν L̄ H̃ ν_R − ½ M_R ν_Rᵀ C ν_R + h.c.`, `H̃ = (H⁰*, −H⁺*)`, `C = iγ²γ⁰`.

## Key mechanism
- Dirac mass `m_D = y_ν v/√2`, Majorana block `M_R`; in `n = (ν_L, ν_R^c)`,
  `M_ν = [[0, m_D], [m_D, M_R]]` (symmetric) **[feynlag-verified: `test_mass_matrix_entries`]**
- Takagi factorisation `M_ν = U D Uᵀ` at the benchmark: `U D Uᵀ` reconstructs `M_ν`; one light and one
  heavy state; the closed-form singular values `m_{ν,N} = (√(M_R²+4m_D²) ∓ M_R)/2` agree
  **[feynlag-verified: `test_takagi_spectrum_at_benchmark`]**
- Seesaw formula: `m_ν(exact) = m_D²/M_R · (1 − m_D²/M_R² + …)` (symbolic series)
  **[feynlag-verified: `tests/test_l2_literature.py::test_seesaw_formula_vs_exact_eigenvalue`]**
- Physical couplings through `MajoranaRotation` (ν_L → U* χ_L, ν_R → U χ_R):
  `W⁻ ē χ_k = (g/√2) U[ν_L,k]`, `Z χ̄_k χ_k′ = (g_Z/2) U[ν_L,k] U[ν_L,k′]`, `h χ̄_k χ_k′ = (y_ν/√2) U[ν_L,k] U[ν_R,k′]`
  — full strength for the light state, `× V` for `N`, matching Atre–Han–Pascoli–Zhang Eq. (2.5)
  **[feynlag-verified: `test_W_coupling_eq_2_5`, `test_Z_coupling_eq_2_5`, `test_h_nu_N_coupling`]**
- Decoupling: `V = m_D/√(m_D² + m_N²) → 0` as `M_R → ∞`, `V = m_D/M_R + O(m_D³/M_R³)`
  **[feynlag-verified: `test_decoupling_M_R_to_infinity`]**

## Characteristic scale
`M_R`. At the benchmark (`y_ν = 10⁻⁶`, `M_R = 1 TeV`): `m_D ≈ 0.17 MeV`, `m_ν ≈ 0.03 eV`,
`m_N ≈ 1 TeV`, `V ≈ 1.7×10⁻⁷` (`outputs/spectrum.md`). With `y_ν ~ 1` the same `m_ν` needs
`M_R ~ 10¹⁴–10¹⁵ GeV`; TeV-scale `N` with observable mixing requires `y_ν ≪ 1` or a
cancellation structure (inverse/linear seesaw). [physics judgment]

## Observables that test it
Neutrinoless double beta decay (`ΔL = 2`), direct searches for heavy neutral leptons via
`W → ℓ N` and `Z → ν N` with rates `∝ |V_ℓN|²`, lepton-flavour violation in 3-generation
versions, and the light-neutrino mass scale (cosmology, KATRIN). [physics judgment]

## Genealogy
Parent: `sm`. Proposed children: 3-generation seesaw with Casas–Ibarra parametrisation,
inverse seesaw, type-II (scalar triplet) and type-III (fermion triplet) seesaws, `sm_singlet_z2 +
seesaw_type1` (singlet-generated `M_R`). See `GENEALOGY.md`.
