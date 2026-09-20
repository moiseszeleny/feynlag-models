# Standard Model with three generations and CKM mixing — physics card

**id** `sm_ckm` · **parents** `sm` (extends) · **maturity** L3 (UFO round-trip; no MadGraph
cross-section check, so not L4).

Tags: **[feynlag-verified: test]** = a test in `tests/` pins it; **[physics judgment]** = not machine-checked.

## Problem addressed
The root `sm` has one generation, so it has no quark mixing and no CP violation in the charged
current. This model restores the full flavour structure of the SM: three generations, the CKM
matrix in the $W$ couplings, and no tree-level flavour-changing neutral currents. It is the
parent for flavour-dependent extensions. [physics judgment]

## Field content
| field | spin | $SU(3)_c \times SU(2)_L \times U(1)_Y$ | extra charges | generations |
|---|---|---|---|---|
| $H$ (`H`) | $0$ | $(1, 2, \tfrac12)$ | none | 1 |
| $L_L$ (`Ll`) | $\tfrac12$ (L) | $(1, 2, -\tfrac12)$ | none | 3 |
| $e_R$ (`eR`) | $\tfrac12$ (R) | $(1, 1, -1)$ | none | 3 |
| $Q_L$ (`QL`) | $\tfrac12$ (L) | $(3, 2, \tfrac16)$ | none | 3 |
| $u_R$ (`uR`) | $\tfrac12$ (R) | $(3, 1, \tfrac23)$ | none | 3 |
| $d_R$ (`dR`) | $\tfrac12$ (R) | $(3, 1, -\tfrac13)$ | none | 3 |

The same fields as `sm`, with `nflavors=3` (`sm.pieces(generations=3)`). Gauge invariance and
anomaly cancellation hold with the complex $Y_d$
**[feynlag-verified: `tests/test_l0_l1.py::test_validate_invariance_and_anomalies`]**.
Neutrinos are massless, so lepton mixing can be rotated away and there is no PMNS matrix.
[physics judgment]

## New symmetry and breaking
No new symmetry. Electroweak breaking is that of `sm`, with three Goldstone bosons
**[feynlag-verified: `test_goldstone_count`]**. With three generations the Yukawas break the
$U(3)^5$ flavour symmetry down to baryon and lepton numbers, and the one physical phase $\delta$
violates CP. [physics judgment]

## New Lagrangian terms
The Yukawa sector becomes a matrix sector, written in the weak basis where $Y_u$ and $Y_e$ are diagonal:

```math
\mathcal L_Y = -\bar L_L\, Y_e\, H e_R - \bar Q_L\, Y_d\, H d_R - \bar Q_L\, Y_u\, \tilde H u_R + \text{h.c.},
\qquad Y_d = V\,\mathrm{diag}(y_d, y_s, y_b),\quad y_f = \sqrt2\, m_f / v .
```

$V$ is feynlag's `standard_ckm`, the PDG standard parametrization in $\theta_{12}$, $\theta_{13}$,
$\theta_{23}$ and $\delta$ (`th12`, `th13`, `th23`, `deltaCP`).

## Key mechanism
The mass basis is reached by the unitary rotation $d_L' = V d_L$ (`Rotation(kind="unitary")`,
registered on the `Model` for each colour; the mass-basis fields are the auxiliary `dLm1..3`).
- The weak-basis mass matrices are $M_u = \mathrm{diag}(m_u, m_c, m_t)$,
  $M_e = \mathrm{diag}(m_e, m_\mu, m_\tau)$ and $`M_d = V\,\mathrm{diag}(m_d, m_s, m_b)`$, and
  $V^\dagger M_d$ is diagonal **[feynlag-verified: `test_fermion_masses`]**.
- $`V = R_{23}\,U_{13}(\delta)\,R_{12}`$ and $V^\dagger V = 1$
  **[feynlag-verified: `test_ckm_standard_parametrization_and_unitarity`]**.
- The charged current is $`W^+ \bar u_i d_j = i\,(g/\sqrt2)\,V_{ij}\,\gamma^\mu P_L`$, the same as
  feynlag's direct CKM insertion **[feynlag-verified: `test_charged_current_ckm`]**.
- GIM: the $Z$, $\gamma$, $h$ and $G^0$ couplings between different down flavours cancel
  exactly, and the diagonal ones are the `sm` values. This is derived from the rotation, not
  imposed **[feynlag-verified: `test_gim_no_tree_level_fcnc`]**.
- The Jarlskog invariant is

```math
J = \mathrm{Im}\left(V_{us} V_{cb} V_{ub}^* V_{cs}^*\right) = c_{12} c_{23} c_{13}^2\, s_{12} s_{23} s_{13} \sin\delta ,
```

  **[feynlag-verified: `test_jarlskog_invariant`]**.

## Characteristic scale
$v \approx 246$ GeV, as in `sm`. The flavour structure spans the hierarchy from $m_u$ to $m_t$ and
$s_{13} \ll s_{23} \ll s_{12} \ll 1$. [physics judgment]

## Observables that test it
- CKM magnitudes and $\delta$ from the PDG global fit (Eqs. 12.27, 12.28 of the PDG 2024 review).
  At the benchmark, every $\lvert V_{ij}\rvert$ lies inside the $1\sigma$ fit band
  **[feynlag-verified: `test_ckm_magnitudes_at_benchmark`]**.
- $J$ lies inside its quoted fit band **[feynlag-verified: `test_jarlskog_invariant`]**.
- CP asymmetries such as $\sin 2\beta$, and FCNC processes such as $B_s$ mixing and
  $B \to X_s\gamma$. These are loop-level and outside this tree-level card. [physics judgment]
- The benchmark inputs are listed in `metadata.yaml`. $m_u$, $m_d$ and $m_s$ are placeholders.

Generated pages: [`outputs/vertices.md`](outputs/vertices.md) (bosonic and fermion Feynman rules, grouped by vertex class) and [`outputs/spectrum.md`](outputs/spectrum.md) (masses at the benchmark).

## Genealogy
Parent: `sm` (extends: same fields with three generations, plus CKM mixing). No children yet;
see `NEXT_STEPS.md`.
