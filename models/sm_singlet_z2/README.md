# SM + real singlet scalar ($Z_2$, spontaneously broken) — physics card

**id** `sm_singlet_z2` · **parents** `sm` · **maturity** L3 (UFO round-trip; no MadGraph run)

Tags: **[feynlag-verified: test]** = pinned by a test in `tests/`; **[physics judgment]** = not machine-checked.

## Problem addressed
The minimal scalar portal: one real gauge singlet $S$ mixing with the Higgs. It is the template
for a second CP-even resonance, for a universal suppression of all Higgs couplings ($\cos\theta$), and
for hidden-sector portals and strong first-order electroweak phase transitions. [physics judgment]

## Field content
| field | spin | $SU(3)_c \times SU(2)_L \times U(1)_Y$ | extra charges | generations |
|---|---|---|---|---|
| $S$ (`S`, real) | $0$ | $(1, 1, 0)$ | $Z_2$: $-1$ | 1 |
| + everything of `sm` | | | $Z_2$: $+1$ | |

## New symmetry and breaking
A discrete $Z_2$ under which only $S$ is odd (it forbids linear and cubic singlet terms). It is
**spontaneously broken** by $\langle S\rangle = v_S$, which is what generates the mixing between $h$ and $s$.
$Z_2$ invariance holds for every term, the `Dmu` kinetic terms included
**[feynlag-verified: `tests/test_l0_l1.py::test_z2_invariance_of_every_term`]**.
A spontaneously broken discrete symmetry produces domain walls in the early universe; this card
takes no position on the cosmology. [physics judgment]

## New Lagrangian terms

```math
\mathcal L \supset \tfrac12(\partial_\mu S)^2 - \tfrac12\mu_S^2 S^2 - \tfrac14\lambda_S S^4
- \tfrac12\lambda_{HS}(H^\dagger H)S^2,\qquad S \to v_S + s .
```

Map to Robens–Stefaniak (arXiv:1501.02234, Eq. 3): $\lambda_1 \to \lambda$, $\lambda_2 \to \lambda_S$,
$\lambda_3 \to \lambda_{HS}$, $x \to v_S$, and their $S = (h^0 + x)/\sqrt2$.

## Key mechanism
- Tadpoles $`\mu^2 = \lambda v^2 + \tfrac12\lambda_{HS} v_S^2`$ and
  $`\mu_S^2 = -\lambda_S v_S^2 - \tfrac12\lambda_{HS} v^2`$ **[feynlag-verified: `test_tadpoles`]**
- The CP-even block from `Model.mass_matrix` equals Robens–Stefaniak Eq. (7)
  **[feynlag-verified: `test_mass_matrix_eq7`]**:

  ```math
  M^2 = \begin{pmatrix} 2\lambda v^2 & \lambda_{HS} v v_S \\ \lambda_{HS} v v_S & 2\lambda_S v_S^2 \end{pmatrix}.
  ```

- Mixing angle and eigenvalues (Eqs. 8–12, with $\alpha = -\theta$), valid in the benchmark regime
  $`\lambda_S v_S^2 > \lambda v^2`$
  **[feynlag-verified: `test_mixing_angle_eq11_eq12`, `test_mass_eigenvalues_eq8_eq9`]**:

  ```math
  \tan 2\theta = \frac{\lambda_{HS} v v_S}{\lambda v^2 - \lambda_S v_S^2},\qquad
  m_{1,2}^2 = \lambda v^2 + \lambda_S v_S^2 \mp \sqrt{(\lambda v^2 - \lambda_S v_S^2)^2 + (\lambda_{HS} v v_S)^2}.
  ```

- Universal rescaling: $h_1 XX = \cos\theta \times \text{SM}$ and $h_2 XX = -\sin\theta \times \text{SM}$
  for $X = W, Z, t, b, \tau$, with the sum rule $`g_{h_1VV}^2 + g_{h_2VV}^2 = g_{hVV,\text{SM}}^2`$
  **[feynlag-verified: `test_coupling_rescaling`]**
- $`\lambda_{HS} = (m_2^2 - m_1^2)\sin 2\alpha/(2 v v_S)`$ (Eq. 13)
  **[feynlag-verified: `test_lambda3_from_masses_eq13`]**; $\lambda_{HS} \to 0$ implies $\theta \to 0$
  **[feynlag-verified: `test_decoupling_lamHS_to_zero`]**
- The Goldstone count is unchanged (3) **[feynlag-verified: `test_goldstone_count_unchanged`]**

## Characteristic scale
$v_S$, and $`m_{h_2} \approx \sqrt{2\lambda_S}\,v_S`$ for small mixing. At the benchmark
($v_S = 500$ GeV, $\lambda_S = 0.3$, $\lambda_{HS} = 0.1$): $m_{h_1} \approx 120$ GeV,
$m_{h_2} \approx 389$ GeV, $\theta \approx -0.09$ (`outputs/spectrum.md`).
The benchmark is an input point, not a fit. [physics judgment]

## Observables that test it
Higgs signal strengths ($\mu = \cos^2\theta$ for all channels), direct searches for
$h_2 \to WW, ZZ, hh, t\bar t$, the $W$ mass at NLO, and, for $`m_{h_2} > 2 m_{h_1}`$,
$`\text{BR}(h_2 \to h_1 h_1)`$. See `NEXT_STEPS.md` for the current allowed
$\lvert\sin\alpha\rvert$ ranges from Robens–Stefaniak Table II. [physics judgment]

## Genealogy
Parent: `sm`. Proposed children: complex singlet (`sm_csinglet`), singlet with a $Z_2$-stable dark
matter candidate (no VEV), singlet + type-I seesaw (Majoron-like portal). See `GENEALOGY.md`.
