# Next steps — `thdm_type2`

## 1. Natural extensions
- `thdm_type1`, `thdm_type_x` (lepton-specific), `thdm_type_y` (flipped): same scalar sector, different $Z_2$ charges of $d_R$ and $e_R$ (Branco Table 1).
- `inert_doublet`: exact $Z_2$, $v_2 = 0$ and an odd $H_2$, giving scalar dark matter (feynlag: same fields, no second tadpole).
- `thdm_cpv`: complex $m_{12}^2$ and $\lambda_5$ give CP violation in the scalar sector ($3\times3$ neutral mixing; feynlag's $2\times2$ analytic route no longer applies, so diagonalisation is numeric).
- `n2hdm`: 2HDM + real singlet (combines with `sm_singlet_z2`).
- `thdm_s3`, a 3HDM with $S_3$ (feynlag `examples/thdm_s3.py`).
- Three generations with CKM in the charged-Higgs vertex ($V_{ud}$ of Branco Eq. 16), reusing `sm.pieces(generations=3)` and the unitary $d_L$ rotation of `sm_ckm`.

## 2. Observables and current bounds
| observable | value / bound | source | checked on |
|---|---|---|---|
| $`m_{H^\pm}`$ lower bound from $`B \to X_s\gamma`$ (type II, all $\tan\beta$) | $\gt 580$ GeV at 95% CL (the most conservative of the methods compared; the bound spans 570–800 GeV depending on the method) | Misiak, Steinhauser, Eur. Phys. J. C 77 (2017) 201, arXiv:1702.04571v1, abstract and Sec. 5 | 2026-09-17 |
| exclusion in the ($\tan\beta$, $m_A$) plane from $`A/H \to \tau\tau`$ | TODO(verify): the PDG 2024 Higgs review (Table 11.11) lists only the ATLAS and CMS references; the limits themselves are exclusion contours, not numbers | ATLAS, CMS | 2026-09-17 (source read, no quotable number) |
| $`\cos(\beta - \alpha)`$ against $\tan\beta$ from Higgs signal strengths (type II) | TODO(verify): the coupling modifiers of PDG Table 11.8 (see `models/sm/NEXT_STEPS.md`) constrain this plane only through a 2HDM fit, which is published as contours | ATLAS, CMS | 2026-09-17 (source read, no quotable number) |
| direct limits on $`H^+ \to tb`$ and $`H^+ \to \tau\nu`$ | TODO(verify): same as the row above — PDG 2024 Higgs review Sec. 11.6.1.1 and Table 11.11 point at the searches, whose results are cross-section limit curves | ATLAS, CMS | 2026-09-17 (source read, no quotable number) |
| electroweak oblique parameters | $`T = 0.01 \pm 0.12`$, $`S = -0.04 \pm 0.10`$, $`U = -0.01 \pm 0.09`$; with $U = 0$: $`T = 0.00 \pm 0.06`$, $`S = -0.05 \pm 0.07`$ | PDG 2024 EW review, Eqs. (10.98), (10.99) | 2026-09-17 |
| theory: perturbative unitarity, boundedness from below (GH Eq. 4: $`\lambda_3 + \lambda_4 - \lvert\lambda_5\rvert \gt -\sqrt{\lambda_1\lambda_2}`$, $`\lambda_1, \lambda_2 \gt 0`$) | inequalities on the $\lambda_i$; not yet implemented as tests | Gunion–Haber Eq. (4) (checked 2026-09-16) | 2026-09-16 |

## 3. Open theoretical questions
- Whether the $\lambda_i$ basis or the physical basis ($`m_h, m_H, m_A, m_{H^\pm}, \tan\beta, \cos(\beta - \alpha), m_{12}^2`$) should be the UFO inputs (this pilot uses the $\lambda_i$; the physical-basis point is `benchmark.derived_from` in `metadata.yaml`).
- Sign conventions for $A$ and $H^+$ couplings across the literature: Branco Eq. (16) and Aoki Eq. (6) agree with us up to $H^+ \to -H^+$ (discrepancy D-3). Branco's printed $m_A^2$ and $m_{H^\pm}^2$ prefactors (discrepancy D-2) still need a check against the published Phys. Rept. text, which was paywalled on 2026-09-16.
- Vacuum structure: charge-breaking and CP-breaking minima, panic vacua; tree-level stability conditions.

## 4. What feynlag cannot yet do for this model
- No physical-basis input inversion (`InternalParameter`s for the $\lambda_i$ from masses); done by hand for `benchmark.derived_from`.
- No boundedness-from-below / unitarity / oblique-parameter helpers (simple inequalities a child could add).
- No loops ($h \to \gamma\gamma$ with the $H^\pm$ loop, $B \to X_s\gamma$); feynlag's loop module covers only the SM $gg$, $\gamma\gamma$ and $Z\gamma$ effective vertices.
- Unitary-gauge UFO only; gluon vertices not exported (see `models/sm/NEXT_STEPS.md`).
  Quartic gauge couplings are exported since the `efffdb0` pin.
- The widths `WHH`, `WA0` and `WHp` are placeholders in the UFO card.

## 5. Key references
1. G. C. Branco, P. M. Ferreira, L. Lavoura, M. N. Rebelo, M. Sher, J. P. Silva, *Theory and phenomenology of two-Higgs-doublet models*, Phys. Rept. 516 (2012) 1, arXiv:1106.0034.
2. J. F. Gunion, H. E. Haber, *The CP-conserving two-Higgs-doublet model: the approach to the decoupling limit*, Phys. Rev. D 67 (2003) 075019, arXiv:hep-ph/0207010.
3. J. F. Gunion, H. E. Haber, G. Kane, S. Dawson, *The Higgs Hunter's Guide*, Front. Phys. 80 (2000) 1.
4. M. Misiak, M. Steinhauser, "Weak radiative decays of the B meson and bounds on $`M_{H^\pm}`$ in the Two-Higgs-Doublet Model", Eur. Phys. J. C 77 (2017) 201, arXiv:1702.04571.
