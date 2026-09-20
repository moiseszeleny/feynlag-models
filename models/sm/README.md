# Standard Model (root) — physics card

**id** `sm` · **parents** none · **maturity** L3 (UFO round-trip; MadGraph cross-section
agreement for the electroweak+lepton sector is documented upstream in feynlag's
`docs/benchmark.md` and is *not* re-claimed here as L4).

Tags: **[feynlag-verified: test]** = a test in `tests/` pins it; **[physics judgment]** = not machine-checked.

## Problem addressed
None — this is the reference theory. Its gaps are the problems the children address:
massless neutrinos (`seesaw_type1`), a single scalar and no portal to a hidden sector
(`sm_singlet_z2`), and a minimal scalar sector with no charged or CP-odd Higgs (`thdm_type2`).
[physics judgment]

## Field content
| field | spin | $SU(3)_c \times SU(2)_L \times U(1)_Y$ | generations | components |
|---|---|---|---|---|
| $H$ (`H`) | $0$ | $(1, 2, \tfrac12)$ | 1 | $G^+$ (`Gp`), $H^0 \to (v + h + iG^0)/\sqrt2$ (`H0`) |
| $L_L$ (`Ll`) | $\tfrac12$ (L) | $(1, 2, -\tfrac12)$ | 1 | $\nu_L$, $e_L$ (`nuL`, `eL`; $\tau$ generation) |
| $e_R$ (`eR`) | $\tfrac12$ (R) | $(1, 1, -1)$ | 1 | `eR` |
| $Q_L$ (`QL`) | $\tfrac12$ (L) | $(3, 2, \tfrac16)$ | 1 | `uL_c`, `dL_c` |
| $u_R$ (`uR`) | $\tfrac12$ (R) | $(3, 1, \tfrac23)$ | 1 | `uR_c` |
| $d_R$ (`dR`) | $\tfrac12$ (R) | $(3, 1, -\tfrac13)$ | 1 | `dR_c` |
| $W$, $B$, $G$ | $1$ | adjoint | — | gauge bosons |

One generation (the third: $t$, $b$, $\tau$, $\nu_\tau$). Gauge anomalies cancel with this content
**[feynlag-verified: `tests/test_l0_l1.py::test_validate_invariance_and_anomalies`]**.

## New symmetry and breaking
No new symmetry. $`SU(2)_L \times U(1)_Y \to U(1)_{\text{em}}`$ by $\langle H^0\rangle = v/\sqrt2$;
three Goldstones for $W^\pm$ and $Z$ **[feynlag-verified: `tests/test_l0_l1.py::test_goldstone_count`]**.

## New Lagrangian terms
The full renormalisable SM (`CONVENTIONS.md`):

```math
\mathcal L = (D_\mu H)^\dagger (D^\mu H) + \mu^2 H^\dagger H - \lambda (H^\dagger H)^2
+ \sum_\psi i\bar\psi\gamma^\mu D_\mu\psi
- \left(y_\tau \bar L_L H e_R + y_b \bar Q_L H d_R + y_t \bar Q_L \tilde H u_R + \text{h.c.}\right)
```

The pure-gauge $-\tfrac14 F_{\mu\nu}F^{\mu\nu}$ terms are implicit in feynlag's Yang–Mills machinery.

## Key mechanism
- $\mu^2 = \lambda v^2$, $m_h^2 = 2\lambda v^2$ **[feynlag-verified: `test_tadpole_and_higgs_mass`]**
- $m_W = g v/2$, $`m_Z = \sqrt{g^2 + g'^2}\,v/2`$, $m_\gamma = 0$ **[feynlag-verified: `test_gauge_masses`]**
- $m_f = y_f v/\sqrt2$ **[feynlag-verified: `test_fermion_masses`]**
- Feynman rules $hWW = i g m_W g^{\mu\nu}$, $hZZ = i g_Z m_Z g^{\mu\nu}$, $hf\bar f = -i m_f/v$,
  $Zf\bar f = i g_Z \gamma^\mu (T^3 P_L - Q s_W^2)$, $W\bar\nu\ell = i (g/\sqrt2)\gamma^\mu P_L$,
  $h^3 = -3i m_h^2/v$ **[feynlag-verified: `tests/test_l2_literature.py`]**

## Characteristic scale
$v \approx 246$ GeV. [physics judgment]

## Observables that test it
Higgs signal strengths, electroweak precision fits of $m_W$, $m_Z$ and $\sin^2\theta_W$, and the top
and bottom Yukawas via $t\bar t h$ and $h \to b\bar b$. Benchmark inputs in `metadata.yaml` are round
PDG-like numbers, not measurements; see `NEXT_STEPS.md` for sources. [physics judgment]

Generated pages: [`outputs/vertices.md`](outputs/vertices.md) (bosonic Feynman rules, grouped by vertex class) and [`outputs/spectrum.md`](outputs/spectrum.md) (masses at the benchmark).

## Genealogy
Parents: none. Children: `sm_ckm`, `sm_singlet_z2`, `seesaw_type1`, `thdm_type2` (see `GENEALOGY.md`).
