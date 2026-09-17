# Next steps — `thdm_type2`

## 1. Natural extensions
- `thdm_type1`, `thdm_type_x` (lepton-specific), `thdm_type_y` (flipped): same scalar sector, different Z₂ charges of `d_R`, `e_R` (Branco Table 1).
- `inert_doublet`: exact Z₂, `v2 = 0`, `H2` odd → scalar dark matter (feynlag: same fields, no second tadpole).
- `thdm_cpv`: complex `m12²`, `λ5` → CP violation in the scalar sector (3×3 neutral mixing; feynlag's 2×2 analytic route no longer applies → numeric diagonalisation).
- `n2hdm`: 2HDM + real singlet (combines with `sm_singlet_z2`).
- `thdm_s3` / 3HDM with S₃ (feynlag `examples/thdm_s3.py`).
- Three generations with CKM in the charged-Higgs vertex (`V_ud` of Branco Eq. 16) via feynlag's mass-basis insertion.

## 2. Observables and current bounds
| observable | value / bound | source | checked on |
|---|---|---|---|
| `m_H±` lower bound from `B → X_s γ` (type II, all `tan β`) | TODO(verify) — Misiak & Steinhauser, arXiv:1702.04571 (NNLO) | | TODO(verify) |
| `tan β`–`m_A` exclusion from `A/H → ττ` | TODO(verify) — ATLAS/CMS Run-2 searches | ATLAS, CMS | TODO(verify) |
| `cos(β−α)` vs `tan β` from Higgs signal strengths (type II) | TODO(verify) — ATLAS/CMS combined coupling fits interpreted in the 2HDM | ATLAS, CMS | TODO(verify) |
| `H⁺ → tb`, `H⁺ → τν` direct limits | TODO(verify) | ATLAS, CMS | TODO(verify) |
| electroweak `T` parameter constraint on `m_A − m_H±` | TODO(verify) — Gfitter / PDG EW review | | TODO(verify) |
| theory: perturbative unitarity, boundedness from below (GH Eq. 4: `λ3 + λ4 − |λ5| > −√(λ1λ2)`, `λ1, λ2 > 0`) | inequalities on the `λ_i`; not yet implemented as tests | Gunion–Haber Eq. (4) (checked 2026-09-16) | 2026-09-16 |

## 3. Open theoretical questions
- Which of the `λ_i` basis or the physical basis (`m_h, m_H, m_A, m_H±, tan β, cos(β−α), m12²`) should be the UFO inputs (this pilot uses the `λ_i`; the physical-basis inversion is in the benchmark comment of `metadata.yaml`).
- Sign conventions for `A` and `H⁺` couplings across the literature (the pilot found a relative-sign discrepancy with Branco Eq. 16, see the card).
- Vacuum structure: charge-breaking and CP-breaking minima, panic vacua; tree-level stability conditions.

## 4. What feynlag cannot yet do for this model
- No physical-basis input inversion (`InternalParameter`s for `λ_i` from masses); done by hand in the benchmark comment.
- No boundedness-from-below / unitarity / oblique-parameter helpers (simple inequalities a child could add).
- No loops (`h → γγ` with the `H±` loop, `B → X_s γ`); feynlag's loop module covers only the SM `gg/γγ/Zγ` effective vertices.
- Unitary-gauge UFO only; quartic gauge couplings, gluon vertices and Goldstone vertices are not exported (see `models/sm/NEXT_STEPS.md`).
- Widths `W_HH, W_A0, W_Hp` are placeholders in the UFO card.

## 5. Key references
1. G. C. Branco, P. M. Ferreira, L. Lavoura, M. N. Rebelo, M. Sher, J. P. Silva, *Theory and phenomenology of two-Higgs-doublet models*, Phys. Rept. 516 (2012) 1, arXiv:1106.0034.
2. J. F. Gunion, H. E. Haber, *The CP-conserving two-Higgs-doublet model: the approach to the decoupling limit*, Phys. Rev. D 67 (2003) 075019, arXiv:hep-ph/0207010.
3. J. F. Gunion, H. E. Haber, G. Kane, S. Dawson, *The Higgs Hunter's Guide*, Front. Phys. 80 (2000) 1.
4. M. Misiak, M. Steinhauser, *Weak radiative decays of the B meson and bounds on M_H± in the Two-Higgs-Doublet Model*, Eur. Phys. J. C 77 (2017) 201, arXiv:1702.04571.
