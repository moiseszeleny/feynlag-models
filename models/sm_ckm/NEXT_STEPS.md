# Next steps — `sm_ckm`

Write formulas in LaTeX and code in backticks (`CONVENTIONS.md`, section "Markdown").

## 1. Natural extensions
- `thdm_type2` with three generations: the charged-Higgs vertex carries $V_{ud}$ (Branco Eq. 16).
  This model's `sm.pieces(generations=3)` and the unitary $d_L$ rotation carry over directly.
- `sm_ckm_seesaw` (or `seesaw_type1` with three generations): massive neutrinos and a PMNS matrix.
  This is blocked at L3 by FG-3 (no Majorana UFO).
- `sm_qcd_ufo`: gluon vertices exported with colour tensors (the other proposed child of `sm`).
- Wolfenstein inputs ($\lambda$, $A$, $\bar\rho$, $\bar\eta$ of PDG Eq. 12.4) as an alternative
  parameter set, cross-checked against the standard angles.

## 2. Observables and current bounds
| observable | value / bound | source | checked on |
|---|---|---|---|
| $\sin\theta_{12}$, $\sin\theta_{13}$, $\sin\theta_{23}$, $\delta$ | $0.22501$, $0.003732$, $0.04183$, $1.147$ (central values; the uncertainties are in the source) | PDG 2024 CKM review, Eq. (12.28) | 2026-09-17 |
| $\lvert V_{ij}\rvert$ (global fit) | Eq. (12.27) | PDG 2024 CKM review | 2026-09-17 |
| Jarlskog invariant $J$ | $3.12$ ($+0.13$, $-0.12$) $\times 10^{-5}$ | PDG 2024 CKM review, text before Eq. (12.28) | 2026-09-17 |
| $m_u$, $m_d$, $m_s$ | TODO(verify): take from the PDG quark-mass review; the benchmark uses placeholders | PDG | TODO(verify) |

## 3. Open theoretical questions
- The origin of the flavour hierarchy and of $\delta$ (the flavour puzzle). [physics judgment]
- The benchmark takes the PDG angles, not the edition feynlag's `standard_ckm` defaults come from.
  Those defaults (0.22500, 0.003675, 0.04182, 1.144) have an unidentified PDG edition,
  TODO(verify).

## 4. What feynlag cannot yet do for this model
- `fermion_mass_matrix` (and `majorana_mass_matrix`) mishandle integer flavour indices, FG-4. The
  L1 masses use the workaround `feynlag_models.checks.fermion_mass_block`.
- No symbolic $3\times3$ complex SVD. The CKM enters as an input rotation (feynlag's documented
  route), so $V$ is not derived from a generic $Y_d$.
- The UFO writes each coupling as an expression in the angles. The `Vud` … `Vtb` internals are
  exported but not referenced by the vertices.
- Unitary-gauge UFO only; quartic gauge couplings, gluon vertices and Goldstone vertices are not
  exported (see `models/sm/NEXT_STEPS.md`).
- Loops (meson mixing, penguins) are outside feynlag's tree-level scope.

## 5. Key references
1. Particle Data Group (S. Navas et al.), *Review of Particle Physics*, Phys. Rev. D 110 (2024) 030001.
   Sec. 12, "CKM Quark-Mixing Matrix" (A. Ceccucci, Z. Ligeti, Y. Sakai), revised April 2024; Eqs. (12.1)–(12.4),
   (12.27), (12.28) read on 2026-09-17.
2. feynlag, `src/feynlag/flavor.py` and `tests/test_ckm.py` at the pinned commit (the direct-insertion route).
3. MadGraph5_aMC@NLO v3.7.2, `models/sm/parameters.py` (default $m_c$, $m_e$, $m_\mu$).
