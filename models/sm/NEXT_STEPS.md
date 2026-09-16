# Next steps — `sm`

## 1. Natural extensions
- `sm_singlet_z2` (real singlet, scalar mixing), `seesaw_type1` (heavy Majorana ν), `thdm_type2` (second doublet) — in this repository.
- Proposed children: `sm_ckm` (three generations + CKM via feynlag's mass-basis insertion, `feynlag.standard_ckm`), `sm_qcd_ufo` (gluon vertices exported with colour tensors).

## 2. Observables and current bounds
| observable | value / bound | source | checked on |
|---|---|---|---|
| `m_h`, `m_W`, `m_Z`, `m_t`, `m_b`, `m_τ` | TODO(verify) — take from the current PDG Review of Particle Physics | PDG | TODO(verify) |
| Higgs coupling modifiers κ_V, κ_f | TODO(verify) — ATLAS/CMS combination | ATLAS, CMS | TODO(verify) |

The benchmark inputs in `metadata.yaml` are the values feynlag's MadGraph benchmark uses
(`gw`, `g1`, `v` from the (α_EW⁻¹, G_F, M_Z) scheme) and round masses; they are inputs, not measurements.

## 3. Open theoretical questions
Hierarchy problem, neutrino masses, dark matter, baryogenesis, strong CP — the standard list;
this card makes no claim beyond tree level. [physics judgment]

## 4. What feynlag cannot yet do for this model
- No R_ξ gauge fixing / ghosts (unitary-gauge UFO only; Goldstone vertices are dropped at export).
- Quartic gauge self-couplings in the rotated `W±, Z, γ` basis are not exported (feynlag's
  `assemble_vvvv` works in the real weak basis; the physical-basis assembly is not in the
  pinned commit). The exported UFO is therefore complete for FFV/FFS/VVS/VVSS/SSS/SSSS/VVV only.
- Gluon vertices are not exported in this pilot (no colour-octet particle); quark vertices
  carry `Identity(1,2)` colour flow so the model imports, but hadron-collider use needs the
  gluon sector (feynlag supports it; not wired here).
- Loops (Higgs → γγ, gg) exist in feynlag's `pheno.loop` as imported effective vertices, not as derived rules.
- Only one generation; no CKM (feynlag's CKM insertion route exists, see `examples/sm_ckm.py`).

## 5. Key references
1. M. E. Peskin, D. V. Schroeder, *An Introduction to Quantum Field Theory*, Addison-Wesley (1995) — SM Feynman rules.
2. Particle Data Group, *Review of Particle Physics*, "Electroweak Model and Constraints on New Physics" review.
3. feynlag, `docs/benchmark.md` — MadGraph round-trip of the exported SM UFO (`e⁺e⁻ → μ⁺μ⁻`, `e⁺e⁻ → W⁺W⁻`).
