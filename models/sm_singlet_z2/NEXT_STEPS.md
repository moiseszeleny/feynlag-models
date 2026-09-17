# Next steps — `sm_singlet_z2`

## 1. Natural extensions
- `sm_singlet_dm`: same field with `⟨S⟩ = 0` (exact Z₂, scalar dark matter; no mixing, `λ_HS` = portal annihilation).
- `sm_csinglet`: complex singlet with a global U(1) (spontaneously broken → Goldstone/Majoron, or softly broken).
- `sm_singlet_z2 + seesaw_type1`: the singlet generating `M_R` through a `y_N S ν_Rᵀ C ν_R` term.
- General xSM with cubic terms (`a₁ S H†H`, `b₃ S³`) for electroweak baryogenesis studies.

## 2. Observables and current bounds
Values below were read from the arXiv v2 text of Robens–Stefaniak (Table II, allowed `|sin α|` at
`tan β = 0.15`, `m_h = 125.14 GeV`; their α = −θ) on 2026-09-16. They are 2015 Run-1 results and
must be updated with Run-2 combinations before being used in a paper.

| observable | value / bound | source | checked on |
|---|---|---|---|
| `\|sin α\|` for `m_H = 300 GeV` | allowed `[0.067, 0.31]`, upper limit from `m_W` at NLO | arXiv:1501.02234v2, Table II | 2026-09-16 |
| `\|sin α\|` for `m_H = 500 GeV` | allowed `[0.046, 0.24]`, upper limit from `m_W` at NLO | arXiv:1501.02234v2, Table II | 2026-09-16 |
| `\|sin α\|` for `m_H = 1000 GeV` | allowed `[0.018, 0.17]`, upper limit from λ₁ perturbativity | arXiv:1501.02234v2, Table II | 2026-09-16 |
| `\|sin α\|` for `m_H = 140–180 GeV` | upper limit `0.31–0.46` from Higgs signal rates | arXiv:1501.02234v2, Table II | 2026-09-16 |
| lower limits on `\|sin α\|` in the table | from vacuum stability at a scale ~4×10¹⁰ GeV (RGE) | arXiv:1501.02234v2, Table II caption | 2026-09-16 |
| Run-2 Higgs signal-strength bound on `sin²θ` | TODO(verify) — ATLAS/CMS combination | ATLAS, CMS | TODO(verify) |
| direct `h2 → ZZ/WW/hh` limits (Run 2) | TODO(verify) | ATLAS, CMS | TODO(verify) |

## 3. Open theoretical questions
- Vacuum stability and perturbativity under RGE running (the lower limits above depend on the cutoff scale).
- Whether `⟨S⟩ ≠ 0` with an exact Z₂ is cosmologically acceptable (domain walls) or a small explicit breaking is needed.
- Electroweak phase transition strength as a function of `(λ_S, λ_HS, v_S)` (needs the finite-temperature potential).

## 4. What feynlag cannot yet do for this model
- **FG-1**: `Model.mass_matrix` double-shifts a real VEV'd scalar; this repository evaluates the blocks with
  `feynlag_models.checks.scalar_mass_block` (public `build_mass_matrix` + one vacuum evaluation).
- **FG-2**: the discrete-invariance check false-fails on `Dmu`-built kinetic terms; Z₂ is verified term by term on the non-kinetic sector.
- No loops: `h2 → γγ`, `h1 → γγ` with the rescaled couplings would follow from feynlag's `pheno.loop` effective vertices only.
- `Γ(h2 → h1 h1)` (Pruna–Robens Eq. 12) is a tree-level SSS width feynlag's `DecayCalculator` can compute; not done in this pilot.
- No RGE running, unitarity or boundedness-from-below checks (Eqs. 4–5 of the reference) — they are simple inequalities a child could add as tests.
- Unitary-gauge UFO only; quartic gauge couplings and gluon vertices not exported (see `models/sm/NEXT_STEPS.md`).

## 5. Key references
1. T. Robens, T. Stefaniak, *Status of the Higgs Singlet Extension of the Standard Model after LHC Run 1*, Eur. Phys. J. C 75 (2015) 104, arXiv:1501.02234, doi:10.1140/epjc/s10052-015-3323-y.
2. G. M. Pruna, T. Robens, *The Higgs Singlet extension parameter space in the light of the LHC discovery*, Phys. Rev. D 88 (2013) 115012, arXiv:1303.1150.
3. V. Barger, P. Langacker, M. McCaskey, M. Ramsey-Musolf, G. Shaughnessy, *LHC phenomenology of an extended Standard Model with a real scalar singlet*, Phys. Rev. D 77 (2008) 035005, arXiv:0706.4311 (general xSM with cubic terms).
