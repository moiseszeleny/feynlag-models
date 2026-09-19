# Next steps — `sm`

## 1. Natural extensions
- `sm_singlet_z2` (real singlet, scalar mixing), `seesaw_type1` (heavy Majorana $\nu$), `thdm_type2` (second doublet) — in this repository.
- `sm_ckm` (three generations, CKM mixing through a unitary $d_L$ rotation built on `feynlag.standard_ckm`), in this repository.
- Proposed child: `sm_qcd_ufo` (gluon vertices exported with colour tensors).

## 2. Observables and current bounds
| observable | value / bound | source | checked on |
|---|---|---|---|
| $m_h$ | $125.11 \pm 0.09$ (stat.) $\pm 0.06$ (syst.) GeV (ATLAS diphoton + four-lepton, the most precise measurement quoted); Run-1 ATLAS+CMS combination $125.09 \pm 0.21 \pm 0.11$ GeV | PDG 2024 Higgs review (M. Carena et al., revised August 2023), Sec. 11.4.1 | 2026-09-17 |
| $m_Z$ | $91.1880 \pm 0.0020$ GeV | PDG 2024 EW review, Eq. (10.58) | 2026-09-17 |
| $m_W$ | $80.360 \pm 0.012$ GeV (average without CDF II, width floating); $80.366 \pm 0.012$ GeV with the width at its SM value | PDG 2024 EW review, Eqs. (10.63), (10.65) | 2026-09-17 |
| $m_t$ | $172.61 \pm 0.25$ (exp.) GeV plus $`\Delta m_{\rm MC} = 0 \pm 0.52`$ GeV | PDG 2024 EW review, Eq. (10.21) | 2026-09-17 |
| $m_b$ | $`\overline{m}_b(\overline{m}_b) = 4.183 \pm 0.007`$ GeV | PDG 2024 b-quark Listings, MS-mass evaluation | 2026-09-17 |
| $m_\tau$ | $1776.93 \pm 0.09$ MeV | PDG 2024 tau Listings, tau-mass average | 2026-09-17 |
| Higgs coupling modifiers (ATLAS Run 2) | $\kappa_W = 1.05 \pm 0.06$, $\kappa_Z = 0.99 \pm 0.06$, $\kappa_t = 0.94 \pm 0.11$, $\kappa_b = 0.89 \pm 0.11$, $`\kappa_\tau = 0.93 \pm 0.07`$ | PDG 2024 Higgs review, Table 11.8 | 2026-09-17 |
| Higgs coupling modifiers (CMS Run 2) | $\kappa_W = 1.02 \pm 0.08$, $\kappa_Z = 1.04 \pm 0.07$, $\kappa_t = 1.01 \pm 0.11$, $\kappa_b = 0.99 \pm 0.16$, $`\kappa_\tau = 0.92 \pm 0.08`$ | PDG 2024 Higgs review, Table 11.8 | 2026-09-17 |
| global signal strength | $\mu = 1.05 \pm 0.06$ (ATLAS Run 2) | ATLAS, Nature 607 (2022) 52, arXiv:2207.00092v2, combined-measurement section | 2026-09-17 |

The benchmark inputs in `metadata.yaml` are the values feynlag's MadGraph benchmark uses
(`gw`, `g1`, `v` from the $(\alpha_{\text{EW}}^{-1}, G_F, M_Z)$ scheme) and round masses; they are inputs, not measurements.

## 3. Open theoretical questions
Hierarchy problem, neutrino masses, dark matter, baryogenesis, strong CP — the standard list;
this card makes no claim beyond tree level. [physics judgment]

## 4. What feynlag cannot yet do for this model
- No $R_\xi$ gauge fixing or ghosts (unitary-gauge UFO only; Goldstone vertices are dropped at export).
- The exported UFO is complete for FFV/FFS/VVS/VVSS/SSS/SSSS/VVV/VVVV. (The quartic gauge
  self-couplings in the rotated $W^\pm, Z, \gamma$ basis arrived with feynlag's `gauge_basis`,
  pinned since `efffdb0`, and are checked against MadGraph's stock `sm` in
  `tests/test_l3_ufo.py`.)
- Gluon vertices are not exported in this pilot (no colour-octet particle); quark vertices
  carry `Identity(1,2)` colour flow so the model imports, but hadron-collider use needs the
  gluon sector (feynlag supports it; not wired here).
- Loops ($h \to \gamma\gamma$, $h \to gg$) exist in feynlag's `pheno.loop` as imported effective vertices, not as derived rules.
- Only one generation here; the three-generation root with CKM mixing is `sm_ckm`.

## 5. Key references
1. M. E. Peskin, D. V. Schroeder, *An Introduction to Quantum Field Theory*, Addison-Wesley (1995) — SM Feynman rules.
2. Particle Data Group (S. Navas et al.), *Review of Particle Physics*, Phys. Rev. D 110 (2024) 030001 — Sec. 10, "Electroweak Model and Constraints on New Physics" (J. Erler, A. Freitas); Eqs. (10.1)–(10.7) read on 2026-09-16.
3. Particle Data Group (S. Navas et al.), *Review of Particle Physics*, Phys. Rev. D 110 (2024) 030001 — Sec. 11, "Status of Higgs Boson Physics" (M. Carena, C. Grojean, M. Kado, V. Sharma), revised August 2023; Table 11.8 and Sec. 11.4.1 read on 2026-09-17. INSPIRE 2817040.
4. ATLAS Collaboration, "A detailed map of Higgs boson interactions by the ATLAS experiment ten years after the discovery", Nature 607 (2022) 52, arXiv:2207.00092v2, DOI 10.1038/s41586-022-04893-w, INSPIRE 2104706.
5. feynlag, `docs/benchmark.md` — MadGraph round-trip of the exported SM UFO ($e^+e^- \to \mu^+\mu^-$, $e^+e^- \to W^+W^-$).
