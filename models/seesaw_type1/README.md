# Type-I seesaw — physics card

**id** `seesaw_type1` · **parents** `sm` · **maturity** L2 (L3 blocked: feynlag has no UFO path for Majorana fermions, `FEYNLAG_GAPS.md` FG-3)

Tags: **[feynlag-verified: test]** = pinned by a test in `tests/`; **[physics judgment]** = not machine-checked.

## Problem addressed
Neutrino masses. One gauge-singlet right-handed neutrino with a Dirac Yukawa and a large
Majorana mass gives the light neutrino a tiny Majorana mass $m_\nu \approx m_D^2/M_R$ and a heavy
partner $N$ whose gauge and Higgs couplings are suppressed by the mixing $V \approx m_D/M_R$. [physics judgment]

## Field content
| field | spin | $SU(3)_c \times SU(2)_L \times U(1)_Y$ | extra charges | generations |
|---|---|---|---|---|
| $\nu_R$ (`nuR`) | $\tfrac12$ (R) | $(1, 1, 0)$ | lepton number $L = 1$ | 1 |
| + everything of `sm` | | | | |

Anomaly cancellation is untouched (a total singlet) **[feynlag-verified: `tests/test_l0_l1.py::test_validate_invariance_and_anomalies`]**.

## New symmetry and breaking
No new symmetry is imposed. The SM's accidental lepton number $U(1)_L$ is **explicitly broken** by
two units by the Majorana mass $`-\tfrac12 M_R\,\nu_R^T C\nu_R + \text{h.c.}`$; the physical neutrinos
are Majorana. [physics judgment]

## New Lagrangian terms

```math
\mathcal L \supset -y_\nu\,\bar L_L \tilde H \nu_R - \tfrac12 M_R\,\nu_R^T C \nu_R + \text{h.c.},
\qquad \tilde H = (H^{0*}, -H^{+*}),\qquad C = i\gamma^2\gamma^0 .
```

## Key mechanism
- The Dirac mass is $m_D = y_\nu v/\sqrt2$ and the Majorana block is $M_R$. In the basis
  $n = (\nu_L, \nu_R^c)$ the mass matrix is symmetric
  **[feynlag-verified: `test_mass_matrix_entries`]**:

```math
M_\nu = \begin{pmatrix} 0 & m_D \\ m_D & M_R \end{pmatrix}.
```

- Takagi factorisation $M_\nu = U D U^T$ at the benchmark: $U D U^T$ reconstructs $M_\nu$, with one
  light and one heavy state, and the closed-form singular values
  $`m_{\nu,N} = \big(\sqrt{M_R^2 + 4m_D^2} \mp M_R\big)/2`$ agree
  **[feynlag-verified: `test_takagi_spectrum_at_benchmark`]**
- Seesaw formula, as a symbolic series
  **[feynlag-verified: `tests/test_l2_literature.py::test_seesaw_formula_vs_exact_eigenvalue`]**:

```math
m_\nu^{\text{exact}} = \frac{m_D^2}{M_R}\left(1 - \frac{m_D^2}{M_R^2} + \dots\right).
```

- Physical couplings come through `MajoranaRotation`, which substitutes
  $\nu_L \to U^*\chi_L$ and $\nu_R \to U\chi_R$. They match Atre–Han–Pascoli–Zhang Eq. (2.5): full
  strength for the light state and a factor $V$ for $N$
  **[feynlag-verified: `test_W_coupling_eq_2_5`, `test_Z_coupling_eq_2_5`, `test_h_nu_N_coupling`]**:

```math
W^-\bar e\chi_k = \frac{g}{\sqrt2}\,U_{\nu_L k},\qquad
Z\bar\chi_k\chi_{k'} = \frac{g_Z}{2}\,U_{\nu_L k}U_{\nu_L k'},\qquad
h\bar\chi_k\chi_{k'} = \frac{y_\nu}{\sqrt2}\,U_{\nu_L k}U_{\nu_R k'} .
```

- Decoupling: $`V = m_D/\sqrt{m_D^2 + m_N^2} \to 0`$ as $M_R \to \infty$, with
  $`V = m_D/M_R + \mathcal O(m_D^3/M_R^3)`$ **[feynlag-verified: `test_decoupling_M_R_to_infinity`]**

## Characteristic scale
$M_R$. At the benchmark ($y_\nu = 10^{-6}$, $M_R = 1$ TeV): $m_D \approx 0.17$ MeV,
$m_\nu \approx 0.03$ eV, $m_N \approx 1$ TeV, $V \approx 1.7\times10^{-7}$ (`outputs/spectrum.md`).
With $y_\nu \sim 1$ the same $m_\nu$ needs $M_R \sim 10^{14}$ to $10^{15}$ GeV; a TeV-scale $N$ with
observable mixing requires $y_\nu \ll 1$ or a cancellation structure (inverse or linear seesaw).
[physics judgment]

## Observables that test it
Neutrinoless double beta decay ($\Delta L = 2$), direct searches for heavy neutral leptons via
$W \to \ell N$ and $Z \to \nu N$ with rates $\propto \lvert V_{\ell N}\rvert^2$, lepton-flavour violation
in 3-generation versions, and the light-neutrino mass scale (cosmology, KATRIN). [physics judgment]

## Genealogy
Parent: `sm`. Proposed children: 3-generation seesaw with the Casas–Ibarra parametrisation,
inverse seesaw, type-II (scalar triplet) and type-III (fermion triplet) seesaws, and
`sm_singlet_z2` + `seesaw_type1` (singlet-generated $M_R$). See `GENEALOGY.md`.
