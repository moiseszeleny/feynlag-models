# Type-I seesaw, three generations and two right-handed neutrinos — physics card

**id** `seesaw_type1_2n` · **parents** `sm` · **maturity** L1 (L3 blocked by FG-3, no UFO path for Majorana fermions; the Takagi factorisation uses a workaround for FG-5, see `FEYNLAG_GAPS.md`)

Tags: **[feynlag-verified: test]** = pinned by a test in `tests/`; **[physics judgment]** = not machine-checked.

## Problem addressed
Neutrino masses with **two** independent mass splittings. The one-generation `seesaw_type1` gives
$\operatorname{rank} m_\nu \le 1$, so only one light neutrino is massive. With three lepton
generations and two gauge-singlet $\nu_R$, the light matrix
$m_\nu \approx -m_D M_R^{-1} m_D^T$ has rank 2: the lightest neutrino is massless, and the
other two carry two independent $\Delta m^2$. [physics judgment]

## Field content
| field | spin | $SU(3)_c \times SU(2)_L \times U(1)_Y$ | extra charges | generations |
|---|---|---|---|---|
| $\nu_R$ (`nuR`) | $\tfrac12$ (R) | $(1, 1, 0)$ | lepton number $L = 1$ | 2 |
| $L_L$, $e_R$, $Q_L$, $u_R$, $d_R$ of `sm` | $\tfrac12$ | as in `sm` | | 3 |

The quarks are `sm`'s three flavour-diagonal generations **without** CKM mixing: quark mixing
does not enter the neutrino sector at tree level. [physics judgment]
Anomaly cancellation is untouched, because the $\nu_R$ are total singlets
**[feynlag-verified: `tests/test_l0_l1.py::test_validate_invariance_and_anomalies`]**.

## New symmetry and breaking
No new symmetry is imposed. The SM's accidental lepton number $U(1)_L$ is **explicitly broken**
by two units by the Majorana masses; the physical neutrinos are Majorana. [physics judgment]

## New Lagrangian terms

```math
\mathcal L \supset -\sum_{a=e,\mu,\tau}\sum_{b=1,2} y^\nu_{ab}\,\bar L_{a} \tilde H \nu_{R b}
- \tfrac12 \sum_{k=1,2} M_k\,\nu_{R k}^T C \nu_{R k} + \text{h.c.},
\qquad \tilde H = (H^{0*}, -H^{+*}) .
```

$M_R = \operatorname{diag}(M_1, M_2)$ is taken diagonal (the $\nu_R$ basis), and the Yukawa
$y^\nu$ is a general real $3\times2$ matrix.

## Key mechanism
- $m_D = y^\nu v/\sqrt2$ is $3\times2$, read off the Lagrangian by feynlag's `fermion_mass_matrix`.
  That function returns a square matrix; its third column is exactly zero because there is no
  third $\nu_R$. In the basis $n = (\nu_L, \nu_R^c)$ the $5\times5$ mass matrix is
  **[feynlag-verified: `tests/test_l0_l1.py::test_mass_matrix_entries`]**:

```math
M_\nu = \begin{pmatrix} 0_{3\times3} & m_D \\ m_D^T & M_R \end{pmatrix} = U D U^T .
```

- The Takagi factorisation is numeric at the benchmark. It uses `feynlag_models.checks.numeric_takagi`
  at 50 digits, because feynlag's symbolic `diagonalize_takagi` does not finish (FG-5). $U D U^T$
  reconstructs $M_\nu$ to about 40 digits **[feynlag-verified: `test_takagi_spectrum_at_benchmark`]**
- **Rank 2.** Exactly one light neutrino is massless. The two massive light states have distinct
  masses, which gives two independent $\Delta m^2$. The heavy states sit at $M_1$ and $M_2$
  **[feynlag-verified: `test_light_sector_rank_two`]**. The light masses agree with the singular
  values of $m_\nu = -m_D M_R^{-1} m_D^T$, including the zero, up to $\mathcal O(m_D^2/M_R^2)$
  **[feynlag-verified: `test_seesaw_formula_matrix`]**, and the light–heavy mixing agrees with
  $\lvert U_{a N_m}\rvert \approx \lvert (m_D M_R^{-1})_{am}\rvert$
  **[feynlag-verified: `test_light_heavy_mixing_at_benchmark`]**.
- The physical Majorana states $\chi_k$ ($\nu_{1,2,3}$, $N_{1,2}$, ordered by mass) come from
  feynlag's `MajoranaRotation` with $n_L = 3$, whose output is fed by the numeric $U$.

## Characteristic scale
$M_{1,2}$. At the benchmark ($y^\nu \sim 10^{-6}$, $M_1 = 1$ TeV, $M_2 = 3$ TeV) the light masses
are $0$, $\approx 0.016$ eV and $\approx 0.040$ eV; the numbers are in `outputs/spectrum.md`. The benchmark is
hand-chosen and not a fit to oscillation data. [physics judgment]

## Observables that test it
Two oscillation mass splittings with a massless lightest neutrino, neutrinoless double beta
decay ($\Delta L = 2$), heavy neutral lepton searches via $W \to \ell N$ and $Z \to \nu N$ with
rates $\propto |V_{\ell N}|^2$, and lepton-flavour violation such as $\mu \to e\gamma$ (loop level,
not computed here). [physics judgment]

Generated pages: [`outputs/vertices.md`](outputs/vertices.md) (bosonic and fermion Feynman rules, grouped by vertex class) and [`outputs/spectrum.md`](outputs/spectrum.md) (masses at the benchmark).

## Genealogy
Parent: `sm` (at three generations). Sibling of `seesaw_type1`, which it reduces to when one
lepton generation couples to one $\nu_R$. Proposed children: the three-$\nu_R$ `seesaw_type1_3gen`,
and this model with a Casas–Ibarra benchmark fitted to oscillation data. See `GENEALOGY.md`.
