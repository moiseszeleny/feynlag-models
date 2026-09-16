# Conventions (single source of truth)

Inherits every convention of `feynlag` (`CONVENTIONS.md` there, pinned by its
tests); this file fixes what the model library adds. A model that departs from
any item must state the map in its card.

## Metric, Dirac algebra, covariant derivative
- Metric `(+, −, −, −)`; `{γ^μ, γ^ν} = 2 g^{μν}`; `γ₅ = iγ⁰γ¹γ²γ³`;
  `P_L = (1 − γ₅)/2`, `P_R = (1 + γ₅)/2`; `C = iγ²γ⁰`.
- `D_μ = ∂_μ − i g T^a A^a_μ` for every gauge factor.
- Kinetic terms `+(D_μφ)†(D^μφ)`, `+i ψ̄ γ^μ D_μ ψ`, `−¼ F F`; real scalar `+½ (∂S)²`.

## Scalar potentials (the Lagrangian stores `−V` in sector `potential`)
- **SM**: `V = −μ² H†H + λ (H†H)²`, `H = (G⁺, (v + h + i G⁰)/√2)`;
  tadpole `μ² = λ v²`; `m_h² = 2 λ v²`; `m_W = g v/2`, `m_Z = √(g² + g′²) v/2`.
- **Real singlet (Z₂)**: `V ⊃ +½ μ_S² S² + ¼ λ_S S⁴ + ½ λ_HS (H†H) S²`;
  `S → v_S + s` (no `1/√2` for a real field). CP-even block in the basis `(h, s)`.
  Mass eigenstates `(h1, h2) = R(θ)(h, s)`; `h1` is the lighter state at the benchmark.
- **2HDM (CP-conserving, softly broken Z₂)**, Gunion–Haber / Branco et al. form:
  `V = m11² H1†H1 + m22² H2†H2 − m12² (H1†H2 + h.c.) + ½λ1 (H1†H1)² + ½λ2 (H2†H2)²
  + λ3 (H1†H1)(H2†H2) + λ4 |H1†H2|² + ½λ5 [(H1†H2)² + h.c.]`, all parameters real;
  `H_i = (H_i⁺, (v_i + ρ_i + i η_i)/√2)`, `tan β = v2/v1`, `v² = v1² + v2² ≈ (246 GeV)²`.
  Z₂: `H2 → −H2`; the only Z₂-odd term is `m12²`. Type II: `u_R → −u_R` (couples to `H̃2`),
  `d_R`, `e_R` even (couple to `H1`).

## Rotations (feynlag `rotation_2x2(θ) = [[c, s], [−s, c]]`, `new = R · old`)
- `(H, h) = R(α)(ρ1, ρ2)`: `H = cα ρ1 + sα ρ2`, `h = −sα ρ1 + cα ρ2`; `h` is the lighter CP-even state.
- `(G⁰, A) = R(β)(η1, η2)`; `(G⁺, H⁺) = R(β)(H1⁺, H2⁺)`.
- Singlet: `(h1, h2) = R(θ)(h, s)` with `tan 2θ` from the off-diagonal condition.
- Weinberg: `(Z, A) = R(−θ_W)(W³, B)`, `tan θ_W = g′/g`; `W^± = (W¹ ∓ i W²)/√2`.
- Every angle is verified against its defining `tan 2θ` relation, not only `c² + s² = 1`.

## Fermions
- One generation per model (third generation names: `t, b, τ, ν_τ`); Dirac fermions are
  two Weyl fields (`tL`/`tR`, …). Yukawas `−y ψ̄_L Φ ψ_R + h.c.`, `Φ̃ = (Φ⁰*, −Φ⁺*)`;
  Dirac mass `m_f = y_f v/√2` (SM, seesaw, singlet) or `y_f v_i/√2` (2HDM).
- Majorana mass `−½ M_R ν_Rᵀ C ν_R + h.c.`; seesaw basis `n = (ν_L, ν_R^c)`,
  `M_ν = [[0, m_D], [m_Dᵀ, M_R]]`, Takagi `M_ν = U D Uᵀ` (`D ≥ 0`), light `m_ν ≈ −m_D M_R⁻¹ m_Dᵀ`.

## Feynman rules and export
- Vertex = `i × ∂ⁿ L / ∂φ₁…∂φₙ |₀ = i × (monomial coefficient) × ∏_f (multiplicity of f)!`.
- Momenta incoming; `∂_μ φ → i p(φ)_μ φ` (feynlag convention, pinned by its VSS test).
- UFO triple-gauge couplings built from the complex `W^±` rotation are sign-flipped
  (`gAWW`, `gZWW`) at export, following the feynlag MadGraph benchmark; the flip lives in
  `feynlag_models/ufo.py` and nowhere else.
- UFO fermion couplings are the raw Lagrangian coefficients; the writer applies the `i`.

## Names and PDG codes
| state | symbol | PDG | note |
|---|---|---|---|
| CP-even Higgs (SM-like) | `h` / `h1` | 25 | |
| second CP-even | `H` (2HDM), `h2` (singlet) | 35 | |
| CP-odd | `A0` | 36 | |
| charged Higgs | `Hp`/`Hm` | 37 | |
| neutral / charged Goldstone | `G0`, `Gp`/`Gm` | 250, 251 | as in the FeynRules SM |
| Z, photon, W | `Z`, `A`, `Wp`/`Wm` | 23, 22, 24 | |
| heavy Majorana neutrino | `N` | 9900012 | HeavyN-UFO style code — TODO(verify) |
| leptons / quarks | `ta-`, `vt`, `t`, `b` | 15, 16, 6, 5 | |

Parameter names are snake ASCII and UFO-safe (`lam_HS`, `vS`, `m12sq`, `tanb`).
Model ids match `^[a-z0-9_]+$` and equal their directory names.

## Verification discipline
- Dual check for every physical result: `sp.simplify(a − b) == 0` **and**
  `feynlag.numeric_equal(a, b, symbols)` at random points (`feynlag_models.checks.dual_equal`).
- Benchmark numbers come from `metadata.yaml → benchmark` only.
- Every statement in a card is tagged **[feynlag-verified: test]** or **[physics judgment]**.
- Unknown numbers, bounds, equation numbers or citations are written `TODO(verify)`.
