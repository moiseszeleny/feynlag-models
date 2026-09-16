# Standard Model (root) — physics card

**id** `sm` · **parents** none · **maturity** L3 (UFO round-trip; MadGraph cross-section
agreement for the electroweak+lepton sector is documented upstream in feynlag's
`docs/benchmark.md` and is *not* re-claimed here as L4).

Tags: **[feynlag-verified: test]** = a test in `tests/` pins it; **[physics judgment]** = not machine-checked.

## Problem addressed
None — this is the reference theory. Its gaps are the problems the children address:
massless neutrinos (→ `seesaw_type1`), a single scalar and no portal to a hidden sector
(→ `sm_singlet_z2`), a minimal scalar sector with no charged/CP-odd Higgs (→ `thdm_type2`).
[physics judgment]

## Field content
| field | spin | SU(3)_c × SU(2)_L × U(1)_Y | generations | components |
|---|---|---|---|---|
| `H` | 0 | (1, 2, 1/2) | 1 | `Gp`, `H0 → (v + h + i G0)/√2` |
| `Ll` | 1/2 (L) | (1, 2, −1/2) | 1 | `nuL`, `eL` (τ generation) |
| `eR` | 1/2 (R) | (1, 1, −1) | 1 | `eR` |
| `QL` | 1/2 (L) | (3, 2, 1/6) | 1 | `uL_c`, `dL_c` |
| `uR` | 1/2 (R) | (3, 1, 2/3) | 1 | `uR_c` |
| `dR` | 1/2 (R) | (3, 1, −1/3) | 1 | `dR_c` |
| `W`, `B`, `G` | 1 | adjoint | — | gauge bosons |

One generation (third: t, b, τ, ν_τ). Gauge anomalies cancel with this content
**[feynlag-verified: `tests/test_l0_l1.py::test_validate_invariance_and_anomalies`]**.

## New symmetry and breaking
No new symmetry. `SU(2)_L × U(1)_Y → U(1)_em` by `⟨H⁰⟩ = v/√2`; three Goldstones for
`W±, Z` **[feynlag-verified: `tests/test_l0_l1.py::test_goldstone_count`]**.

## New Lagrangian terms
The full renormalisable SM (CONVENTIONS.md):
`L = (D_μH)†(D^μH) + μ² H†H − λ (H†H)² + Σ_ψ i ψ̄ γ^μ D_μ ψ − (y_τ L̄ H e_R + y_b Q̄ H d_R + y_t Q̄ H̃ u_R + h.c.)`
(pure-gauge `−¼FF` terms are implicit in feynlag's Yang–Mills machinery).

## Key mechanism
- `μ² = λ v²`, `m_h² = 2 λ v²` **[feynlag-verified: `test_tadpole_and_higgs_mass`]**
- `m_W = g v/2`, `m_Z = √(g²+g′²) v/2`, `m_γ = 0` **[feynlag-verified: `test_gauge_masses`]**
- `m_f = y_f v/√2` **[feynlag-verified: `test_fermion_masses`]**
- Feynman rules `hWW = i g m_W g^{μν}`, `hZZ = i g_Z m_Z g^{μν}`, `h f f̄ = −i m_f/v`,
  `Z f f̄ = i g_Z γ^μ (T³ P_L − Q s_W²)`, `W ν̄ ℓ = i (g/√2) γ^μ P_L`, `h³ = −3i m_h²/v`
  **[feynlag-verified: `tests/test_l2_literature.py`]**

## Characteristic scale
`v ≈ 246 GeV`. [physics judgment]

## Observables that test it
Higgs signal strengths, `m_W`/`m_Z`/`sin²θ_W` electroweak precision fits, top and bottom
Yukawas via `t t̄ h` and `h → b b̄`. Benchmark inputs in `metadata.yaml` are round
PDG-like numbers, not measurements; see `NEXT_STEPS.md` for sources. [physics judgment]

## Genealogy
Parents: none. Children: `sm_singlet_z2`, `seesaw_type1`, `thdm_type2` (see `GENEALOGY.md`).
