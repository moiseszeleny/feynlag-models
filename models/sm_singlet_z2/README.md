# SM + real singlet scalar (Z₂, spontaneously broken) — physics card

**id** `sm_singlet_z2` · **parents** `sm` · **maturity** L3 (UFO round-trip; no MadGraph run)

Tags: **[feynlag-verified: test]** = pinned by a test in `tests/`; **[physics judgment]** = not machine-checked.

## Problem addressed
The minimal scalar portal: one real gauge singlet `S` mixing with the Higgs. It is the template
for a second CP-even resonance, for a universal suppression of all Higgs couplings (cos θ), and
for hidden-sector portals and strong first-order electroweak phase transitions. [physics judgment]

## Field content
| field | spin | SU(3)_c × SU(2)_L × U(1)_Y | extra charges | generations |
|---|---|---|---|---|
| `S` (real) | 0 | (1, 1, 0) | Z₂: −1 | 1 |
| + everything of `sm` | | | Z₂: +1 | |

## New symmetry and breaking
A discrete Z₂ under which only `S` is odd (forbids linear and cubic singlet terms). It is
**spontaneously broken** by `⟨S⟩ = v_S`, which is what generates the `h`–`s` mixing.
Z₂ invariance of every term, the `Dmu` kinetic terms included **[feynlag-verified: `tests/test_l0_l1.py::test_z2_invariance_of_every_term`]**.
A spontaneously broken discrete symmetry produces domain walls
in the early universe; this card takes no position on the cosmology. [physics judgment]

## New Lagrangian terms
`L ⊃ ½ (∂_μ S)² − ½ μ_S² S² − ¼ λ_S S⁴ − ½ λ_HS (H†H) S²`, `S → v_S + s`.
Map to Robens–Stefaniak (arXiv:1501.02234, Eq. 3): `λ₁ → λ`, `λ₂ → λ_S`, `λ₃ → λ_HS`, `x → v_S`, their `S = (h⁰ + x)/√2`.

## Key mechanism
- Tadpoles `μ² = λ v² + ½ λ_HS v_S²`, `μ_S² = −λ_S v_S² − ½ λ_HS v²` **[feynlag-verified: `test_tadpoles`]**
- CP-even block `M² = [[2λv², λ_HS v v_S], [λ_HS v v_S, 2λ_S v_S²]]` = Robens–Stefaniak Eq. (7) **[feynlag-verified: `test_mass_matrix_eq7`]**, from `Model.mass_matrix`.
- `tan 2θ = λ_HS v v_S/(λv² − λ_S v_S²)`; `m²_{1,2} = λv² + λ_S v_S² ∓ √((λv² − λ_S v_S²)² + (λ_HS v v_S)²)` (Eqs. 8–12, α = −θ) **[feynlag-verified: `test_mixing_angle_eq11_eq12`, `test_mass_eigenvalues_eq8_eq9`]**, in the regime `λ_S v_S² > λ v²` of the benchmark.
- Universal rescaling: `h1 X X = cos θ × SM`, `h2 X X = −sin θ × SM` for `X = W, Z, t, b, τ`; sum rule `g²_{h1VV} + g²_{h2VV} = g²_{hVV,SM}` **[feynlag-verified: `test_coupling_rescaling`]**
- `λ_HS = (m₂² − m₁²) sin 2α/(2 v v_S)` (Eq. 13) **[feynlag-verified: `test_lambda3_from_masses_eq13`]**; `λ_HS → 0 ⇒ θ → 0` **[feynlag-verified: `test_decoupling_lamHS_to_zero`]**
- Goldstone count unchanged (3) **[feynlag-verified: `test_goldstone_count_unchanged`]**

## Characteristic scale
`v_S` and `m_{h2} ≈ √(2λ_S) v_S` for small mixing; at the benchmark (`v_S = 500 GeV`, `λ_S = 0.3`,
`λ_HS = 0.1`) `m_{h1} ≈ 120 GeV`, `m_{h2} ≈ 389 GeV`, `θ ≈ −0.09` (`outputs/spectrum.md`).
The benchmark is an input point, not a fit. [physics judgment]

## Observables that test it
Higgs signal strengths (`μ = cos²θ` for all channels), direct searches for `h2 → WW, ZZ, hh, tt̄`,
the `W` mass at NLO, and, for `m_{h2} > 2 m_{h1}`, `BR(h2 → h1 h1)`. See `NEXT_STEPS.md` for the
current allowed `|sin α|` ranges from Robens–Stefaniak Table II. [physics judgment]

## Genealogy
Parent: `sm`. Proposed children: complex singlet (`sm_csinglet`), singlet + `Z₂`-stable dark
matter (no VEV), singlet + type-I seesaw (Majoron-like portal). See `GENEALOGY.md`.
