# Next steps — `froggatt_nielsen`

Write formulas in LaTeX and code in backticks (`CONVENTIONS.md`, section "Markdown").

## 1. Natural extensions
- **A mass for the familon.** $`U(1)_{\rm FN}`$ is exact here, so $a$ is massless. A soft
  breaking term such as $`\mu_b^2\,\phi^2 + \text{h.c.}`$ (or a higher power of $\phi$) gives $a$ a
  mass and turns it into a pseudo-Goldstone, which opens a UFO export without a massless
  pseudoscalar. [physics judgment]
- **Discrete $`Z_N`$ instead of $U(1)$.** LNS-2 Sec. 2.1 requires the horizontal symmetry of the
  full Lagrangian to be a $`Z_N \subset U(1)`$, so that a term breaking it by $n \gt N$ units is
  suppressed only by $\lambda^{n \bmod N}$. A $`Z_N`$ benchmark would remove the Goldstone and
  could use feynlag's `ZN`, but only once per-generation charges are expressible (FG-7).
- **Gauged $`U(1)_{\rm FN}`$.** A new $Z'$ eats $a$. The per-generation charges must then satisfy
  the mixed and cubic anomaly conditions (or be cancelled by extra fermions or a Green–Schwarz
  mechanism). feynlag's anomaly check would apply once the charges can be declared per generation
  (FG-7). [physics judgment]
- **Neutrino masses and lepton mixing.** The lepton charges are placeholders (they copy the down
  sector), and neutrinos are massless as in `sm_ckm`. A Weinberg operator with FN suppression, or
  FN-charged $\nu_R$ in the style of `seesaw_type1_2n`, would give a PMNS matrix with its own
  $\epsilon$ scaling. [physics judgment]
- **Stage-1 fit (`feynlag-anomalies`, P3 of the flavour puzzle).** Fit $\epsilon$ and the
  $`c_{ij}`$ to the measured masses and $\lvert V_{ij}\rvert$ with `bundle.extra["Yu"/"Yd"]` and
  `feynlag_models.flavor`, and compare the span of $`\log_{10}\lvert c_{ij}\rvert`$ with the SM's.
  That fit belongs to `feynlag-anomalies`, not to this repository; the benchmark $`c_{ij}`$ are a
  seeded draw and stay one.
- **Flavon FCNC.** The couplings $`\lvert n_{ij}\rvert M_{ij}/v_\phi`$ of $s$ and $`n_{ij} M_{ij}/v_\phi`$ of $a$ are off-diagonal in the
  mass basis. Rotating them with the numeric $`U_L`$, $`U_R`$ gives the tree-level
  $\Delta F = 2$ operators that bound $v_\phi$ (LNS-2 Sec. 4.2 estimates
  $`F_K \sim m_d m_s/\langle S\rangle^2`$). A careful confrontation needs stage-2 tools.
- **Different charge assignments.** The charges are benchmark inputs, so other LNS assignments
  (for example the two-$U(1)$ models of LNS-1 Eq. (7.5) or LNS-2 Eq. (2.21), which need a second
  flavon) can be added as benchmarks or as a child model.

## 2. Observables and current bounds
| observable | value / bound | source | checked on |
|---|---|---|---|
| expansion parameter $\epsilon$ | $\lambda \sim 0.2$ ("in the range 0.20 − 0.22" in the text) | LNS-2, hep-ph/9310320v1, Secs. 1 and 2.1 | 2026-10-05 |
| target hierarchy $\lvert V_{us}\rvert$, $\lvert V_{cb}\rvert$, $\lvert V_{ub}\rvert$ | $\lambda$, $\lambda^2$, $\lambda^3$ to $\lambda^4$ (orders of magnitude) | LNS-2 Eq. (1.2) | 2026-10-05 |
| measured quark masses and CKM | not used here: the benchmark is not a fit; P3 uses the Huang–Zhou masses and PDG 2024 CKM | `feynlag-anomalies` | |
| bounds on $v_\phi$ (or $\Lambda$) from $K$, $B$, $D$ mixing and from familon emission | TODO(verify) | not read | |

## 3. Open theoretical questions
- **Holomorphy.** LNS work in a supersymmetric theory, where Yukawa entries with negative charge
  sums vanish (no powers of $S^\dagger$; LNS-2 Sec. 4.1). This model is non-supersymmetric, so
  such entries would come with $\phi^*$; none occur at the benchmark, but other charge assignments
  would change the textures. [physics judgment]
- **Flavon couplings are not from the literature.** $`n_{ij} M_{ij}/v_\phi`$ is derived here
  (`test_flavon_couplings`); neither LNS paper states it in this form (LNS-1 Eq. (8.5) and LNS-2
  Sec. 4.2 give only order-of-magnitude FCNC estimates). A source that states it exactly is
  TODO(verify).
- **The linearised model.** Vertices with two or more flavons on a fermion pair are dropped
  (README, "Two models from one set of declarations"). They matter for $hh$ or $ss$ production
  from fermions at high energy, not for the masses or the one-flavon couplings. [physics judgment]
- **$O(1)$ coefficients.** "Natural" depends on the distribution of the $`c_{ij}`$; the L2 tests
  draw $\lvert c\rvert$ uniformly in $[0.5, 2]$, which is a choice. [physics judgment]

## 4. What feynlag cannot yet do for this model
- **FG-6.** `diagonalize_svd` is real-only: on a complex $3\times3$ it returns a non-unitary $U_L$
  and complex "masses" without error. Masses and $`V_{\rm CKM}`$ come from the workaround
  `feynlag_models.flavor` (`numeric_biunitary`, `ckm_from_yukawas`, `mass_spectrum`), pinned by
  `test_feynlag_svd_complex_gap` (strict xfail).
- **FG-7.** No global continuous symmetry, and `ZN.assign` gives a multiplet one charge, so
  per-generation FN charges cannot be declared on the `Model`. Invariance is counted outside
  feynlag (`feynlag_models.checks.global_u1_violations`), pinned by
  `test_feynlag_flavour_dependent_charge_gap` (strict xfail).
- **Mass-basis vertices.** There is no numeric mass-basis rotation for the complex Yukawas, so the
  vertices are in the weak basis. Extracting vertices from the exact operators (up to nine bosons
  per vertex) was about ten times slower than from the linearised model (probe on 2026-10-05),
  which is why `bundle.model` is linearised. Not a gap row: it is a cost, not a wrong result.
- **No UFO.** Not attempted (not requested). Unitary-gauge export would have to handle the
  massless $a$, and the higher-dimension operators would need the linearised form.

## 5. Key references
1. M. Leurer, Y. Nir, N. Seiberg, "Mass matrix models", Nucl. Phys. B 398 (1993) 319–342,
   arXiv:hep-ph/9212278, doi:10.1016/0550-3213(93)90112-3, INSPIRE 341758. Read: arXiv v1 text
   (the only version), Secs. 5–8; Eqs. (5.2)–(5.9), (6.4), (6.5), (7.3)–(7.5), (8.5). The
   published version was not compared (Elsevier paywall), TODO(verify).
2. M. Leurer, Y. Nir, N. Seiberg, "Mass matrix models: The Sequel", Nucl. Phys. B 420 (1994)
   468–504, arXiv:hep-ph/9310320, doi:10.1016/0550-3213(94)90074-4, INSPIRE 359267. Read: arXiv
   v1 text (the only version), Secs. 1, 2, 4; Eqs. (1.2)–(1.4), (2.1)–(2.8), (2.18)–(2.22),
   (4.1)–(4.3). The published version was not compared, TODO(verify).
3. C. D. Froggatt, H. B. Nielsen, "Hierarchy of Quark Masses, Cabibbo Angles and CP Violation",
   Nucl. Phys. B 147 (1979) 277–298, doi:10.1016/0550-3213(79)90316-X, INSPIRE 131306. **Not
   read** (ScienceDirect and CDS unreachable from here); only the INSPIRE record and abstract.
   Its equations are TODO(verify).
