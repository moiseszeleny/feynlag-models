# Next steps — `sm_singlet_z2`

## 1. Natural extensions
- `sm_singlet_dm`: same field with $\langle S\rangle = 0$ (exact $Z_2$, scalar dark matter; no mixing, and $\lambda_{HS}$ controls portal annihilation).
- `sm_csinglet`: complex singlet with a global $U(1)$, either spontaneously broken (a Goldstone or Majoron) or softly broken.
- `sm_singlet_z2 + seesaw_type1`: the singlet generating $M_R$ through a $y_N S\,\nu_R^T C\nu_R$ term.
- General xSM with cubic terms ($a_1 S H^\dagger H$, $b_3 S^3$) for electroweak baryogenesis studies.

## 2. Observables and current bounds
Values below were read from the arXiv v2 text of Robens–Stefaniak (Table II, allowed $\lvert\sin\alpha\rvert$ at
$\tan\beta = 0.15$, $m_h = 125.14$ GeV; their $\alpha = -\theta$) on 2026-09-16. They are 2015 Run-1 results and
must be updated with Run-2 combinations before being used in a paper.

| observable | value / bound | source | checked on |
|---|---|---|---|
| $\lvert\sin\alpha\rvert$ for $m_H = 300$ GeV | allowed $[0.067, 0.31]$, upper limit from $m_W$ at NLO | arXiv:1501.02234v2, Table II | 2026-09-16 |
| $\lvert\sin\alpha\rvert$ for $m_H = 500$ GeV | allowed $[0.046, 0.24]$, upper limit from $m_W$ at NLO | arXiv:1501.02234v2, Table II | 2026-09-16 |
| $\lvert\sin\alpha\rvert$ for $m_H = 1000$ GeV | allowed $[0.018, 0.17]$, upper limit from $\lambda_1$ perturbativity | arXiv:1501.02234v2, Table II | 2026-09-16 |
| $\lvert\sin\alpha\rvert$ for $140 \le m_H \le 180$ GeV | upper limit between $0.31$ and $0.46$ from Higgs signal rates | arXiv:1501.02234v2, Table II | 2026-09-16 |
| lower limits on $\lvert\sin\alpha\rvert$ in the table | from vacuum stability at a scale $\sim 4\times10^{10}$ GeV (RGE) | arXiv:1501.02234v2, Table II caption | 2026-09-16 |
| Run-2 Higgs signal-strength bound on $\sin^2\theta$ | TODO(verify) — ATLAS/CMS combination | ATLAS, CMS | TODO(verify) |
| direct $h_2 \to ZZ, WW, hh$ limits (Run 2) | TODO(verify) | ATLAS, CMS | TODO(verify) |

## 3. Open theoretical questions
- Vacuum stability and perturbativity under RGE running (the lower limits above depend on the cutoff scale).
- Whether $\langle S\rangle \neq 0$ with an exact $Z_2$ is cosmologically acceptable (domain walls) or a small explicit breaking is needed.
- Electroweak phase transition strength as a function of $`(\lambda_S, \lambda_{HS}, v_S)`$ (needs the finite-temperature potential).

## 4. What feynlag cannot yet do for this model
- No loops: $h_2 \to \gamma\gamma$ and $h_1 \to \gamma\gamma$ with the rescaled couplings would follow from feynlag's `pheno.loop` effective vertices only.
- $`\Gamma(h_2 \to h_1 h_1)`$ (Pruna–Robens Eq. 12) is a tree-level SSS width feynlag's `DecayCalculator` can compute; not done in this pilot.
- No RGE running, unitarity or boundedness-from-below checks (Eqs. 4–5 of the reference) — they are simple inequalities a child could add as tests.
- Unitary-gauge UFO only; quartic gauge couplings and gluon vertices not exported (see `models/sm/NEXT_STEPS.md`).

## 5. Key references
1. T. Robens, T. Stefaniak, *Status of the Higgs Singlet Extension of the Standard Model after LHC Run 1*, Eur. Phys. J. C 75 (2015) 104, arXiv:1501.02234, doi:10.1140/epjc/s10052-015-3323-y.
2. G. M. Pruna, T. Robens, *The Higgs Singlet extension parameter space in the light of the LHC discovery*, Phys. Rev. D 88 (2013) 115012, arXiv:1303.1150.
3. V. Barger, P. Langacker, M. McCaskey, M. Ramsey-Musolf, G. Shaughnessy, *LHC phenomenology of an extended Standard Model with a real scalar singlet*, Phys. Rev. D 77 (2008) 035005, arXiv:0706.4311 (general xSM with cubic terms).
