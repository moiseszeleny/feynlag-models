# Next steps — `seesaw_type1`

## 1. Natural extensions
- `seesaw_type1_3gen`: three ν_R, Casas–Ibarra parametrisation (arXiv:hep-ph/0103065 — TODO(verify)), numeric Takagi of the 6×6 block.
- `inverse_seesaw`: add a singlet `S_L` with a small `μ S_Lᵀ C S_L`; `V` unsuppressed at TeV `M`.
- `seesaw_type2` (scalar triplet, `Y = 1`) and `seesaw_type3` (fermion triplet, `Y = 0`): different `feynlag` reps, same Takagi machinery.
- Singlet-scalar origin of `M_R` (`y_N S ν_Rᵀ C ν_R`): the child of `sm_singlet_z2` and this model (Majoron if the U(1)_L is global).

## 2. Observables and current bounds
| observable | value / bound | source | checked on |
|---|---|---|---|
| `\|V_μ4\|²` for a 33.9 MeV neutral fermion (historical anomaly follow-up) | `< 9.2 × 10⁻⁸` at 95% C.L. | Atre et al. arXiv:0901.3589v2, footnote 1 of Sec. 2.2 (their Ref. [63]) | 2026-09-16 |
| `\|V_ℓN\|²` vs `m_N` for `m_N ~ 1–100 GeV` (LHC, LEP, beam dumps) | TODO(verify) — use the current compilation (e.g. Bolton–Deppisch–Dev, arXiv:1912.03058) | ATLAS, CMS, LHCb, NA62, Belle | TODO(verify) |
| `0νββ` half-life (`m_ββ`) | TODO(verify) — KamLAND-Zen / GERDA / LEGEND | | TODO(verify) |
| sum of light neutrino masses | TODO(verify) — Planck + BAO | | TODO(verify) |
| electroweak precision / lepton universality limits on `\|V_ℓN\|²` (non-unitarity) | TODO(verify) — global fits (e.g. Fernandez-Martinez et al. arXiv:1605.08774) | | TODO(verify) |

## 3. Open theoretical questions
- Naturalness of the hierarchy `y_ν ~ 10⁻⁶` at `M_R ~ TeV` versus `y_ν ~ 1` at `M_R ~ 10¹⁴ GeV`; which regime is testable.
- Leptogenesis: the one-generation model has no CP phase; needs ≥ 2 generations.
- Stability of the Higgs vacuum under large `y_ν` (RGE).

## 4. What feynlag cannot yet do for this model
- **FG-3**: no UFO export of Majorana-fermion vertices; the model stops at L2. A MadGraph study of `pp → ℓ N` needs the `HeavyN`-style UFO conventions (Majorana fermion flow) that feynlag does not emit.
- Symbolic Takagi of the 2×2 block is avoided (nested radicals); masses are pinned by closed forms and numerics at the benchmark; 3 generations would be numeric only.
- No loops (`N → ν γ`, `μ → e γ` from `N` exchange), no `0νββ` amplitude (a 4-fermion operator at low energy; feynlag's FFFF track could take the matched operator).
- `Γ(N → ℓ W, ν Z, ν h)`: tree-level FFV/FFS widths that feynlag's `DecayCalculator` can compute for Dirac particles; the Majorana factor-of-2 bookkeeping is not validated there.

## 5. Key references
1. P. Minkowski, Phys. Lett. B 67 (1977) 421 — TODO(verify).
2. M. Gell-Mann, P. Ramond, R. Slansky, in *Supergravity* (North-Holland, 1979); T. Yanagida, KEK proceedings (1979) — TODO(verify).
3. R. N. Mohapatra, G. Senjanović, Phys. Rev. Lett. 44 (1980) 912 — TODO(verify).
4. A. Atre, T. Han, S. Pascoli, B. Zhang, *The Search for Heavy Majorana Neutrinos*, arXiv:0901.3589 (JHEP 05 (2009) 030 — TODO(verify)).
5. J. A. Casas, A. Ibarra, *Oscillating neutrinos and μ → e γ*, arXiv:hep-ph/0103065 — TODO(verify).
