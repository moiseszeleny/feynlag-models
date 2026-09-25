# Next steps — `seesaw_type1`

## 1. Natural extensions
- `seesaw_type1_2n` (built): three lepton generations and two $\nu_R$, giving two massive light neutrinos and a massless lightest one, with a numeric Takagi factorisation of the $5\times5$ block.
- `seesaw_type1_3gen`: three $\nu_R$, Casas–Ibarra parametrisation (Nucl. Phys. B 618 (2001) 171, arXiv:hep-ph/0103065), numeric Takagi factorisation of the $6\times6$ block.
- `inverse_seesaw`: add a singlet $S_L$ with a small $`\mu\, S_L^T C S_L`$ term, so $V$ is unsuppressed at a TeV-scale $M$.
- `seesaw_type2` (scalar triplet, $Y = 1$) and `seesaw_type3` (fermion triplet, $Y = 0$): different `feynlag` reps, same Takagi machinery.
- Singlet-scalar origin of $M_R$ (a $`y_N S\,\nu_R^T C\nu_R`$ term): the child of `sm_singlet_z2` and this model (a Majoron if $U(1)_L$ is global).

## 2. Observables and current bounds
| observable | value / bound | source | checked on |
|---|---|---|---|
| $\lvert V_{\mu 4}\rvert^2$ for a 33.9 MeV neutral fermion (historical anomaly follow-up) | $\lt 9.2\times10^{-8}$ at 95% C.L. | Atre et al. arXiv:0901.3589v2, footnote 1 of Sec. 2.2 (their Ref. [63]) | 2026-09-16 |
| $`\lvert V_{\ell N}\rvert^2`$ against $m_N$ for $`1 \lesssim m_N \lesssim 100`$ GeV (LHC, LEP, beam dumps) | TODO(verify): the compilation exists only as exclusion curves (Bolton–Deppisch–Dev, arXiv:1912.03058, Figs. 6–8 and Appendix A), with no representative number in the text; digitising a figure is not a reading | ATLAS, CMS, LHCb, NA62, Belle | 2026-09-17 (source read, no quotable number) |
| $0\nu\beta\beta$ half-life, $^{136}$Xe | $`T_{1/2}^{0\nu} \gt 2.3\times10^{26}`$ yr at 90% CL, giving $`m_{ee} \lt 36-156`$ meV across nuclear matrix elements | PDG 2024 neutrino review (M.C. Gonzalez-Garcia et al., revised September 2023), Eq. (14.101) with the preceding paragraph | 2026-09-17 |
| $0\nu\beta\beta$ half-life, $^{76}$Ge | $`T_{1/2}^{0\nu} \gt 1.8\times10^{26}`$ yr at 90% CL (GERDA final), giving $`m_{ee} \lt 79-180`$ meV | PDG 2024 neutrino review, Eq. (14.102) and Sec. 14.9.3 | 2026-09-17 |
| $0\nu\beta\beta$, latest $^{136}$Xe dataset | $`T_{1/2}^{0\nu} \gt 3.8\times10^{26}`$ yr at 90% CL, $`\langle m_{\beta\beta}\rangle \lt 28-122`$ meV | KamLAND-Zen, arXiv:2406.11438, abstract | 2026-09-17 |
| sum of light neutrino masses | $`\sum m_\nu \lt 0.12`$ eV at 95% CL (TT,TE,EE+lowE+lensing+BAO); $`\lt 0.24`$ eV without BAO | Planck 2018 VI, arXiv:1807.06209, Eq. (63b) and Table 2 | 2026-09-17 |
| electroweak precision / lepton universality limits on the mixing (non-unitarity) | at $2\sigma$ the mixings are bounded between $0.1$ and $0.01$, except the $e-\mu$ entry, bounded by $0.005$ from $`\mu \to e\gamma`$; the fit prefers non-zero mixing of order $0.03-0.04$ in the $e$ and $\tau$ sectors at $1-2\sigma$ | Fernandez-Martinez, Hernandez-Garcia, Lopez-Pavon, JHEP 08 (2016) 033, arXiv:1605.08774, abstract | 2026-09-17 |

The $m_{ee}$ ranges above span the nuclear-matrix-element spread quoted by the PDG review, which is a factor 2–3 for a given half-life. [physics judgment]

## 3. Open theoretical questions
- Naturalness of the hierarchy $y_\nu \sim 10^{-6}$ at $M_R \sim$ TeV versus $y_\nu \sim 1$ at $M_R \sim 10^{14}$ GeV, and which regime is testable.
- Leptogenesis: the one-generation model has no CP phase; needs at least two generations.
- Stability of the Higgs vacuum under a large $y_\nu$ (RGE).

## 4. What feynlag cannot yet do for this model
- **FG-3**: no UFO export of Majorana-fermion vertices; the model stops at L2. A MadGraph study of $pp \to \ell N$ needs the `HeavyN`-style UFO conventions (Majorana fermion flow) that feynlag does not emit.
- Symbolic Takagi factorisation of the $2\times2$ block is avoided (nested radicals); masses are pinned by closed forms and numerics at the benchmark; 3 generations would be numeric only.
- No loops ($N \to \nu\gamma$, and $\mu \to e\gamma$ from $N$ exchange), and no $0\nu\beta\beta$ amplitude (a 4-fermion operator at low energy; feynlag's FFFF track could take the matched operator).
- $\Gamma(N \to \ell W, \nu Z, \nu h)$: tree-level FFV/FFS widths that feynlag's `DecayCalculator` can compute for Dirac particles; the Majorana factor-of-2 bookkeeping is not validated there.

## 5. Key references
1. P. Minkowski, "$`\mu \to e\gamma`$ at a rate of one out of $`10^9`$ muon decays?", Phys. Lett. B 67 (1977) 421.
2. M. Gell-Mann, P. Ramond, R. Slansky, *Complex Spinors and Unified Theories*, Conf. Proc. C 790927 (1979) 315, arXiv:1306.4669; T. Yanagida, *Horizontal gauge symmetry and masses of neutrinos*, Conf. Proc. C 7902131 (1979) 95.
3. R. N. Mohapatra, G. Senjanović, *Neutrino Mass and Spontaneous Parity Nonconservation*, Phys. Rev. Lett. 44 (1980) 912.
4. A. Atre, T. Han, S. Pascoli, B. Zhang, *The Search for Heavy Majorana Neutrinos*, JHEP 05 (2009) 030, arXiv:0901.3589.
5. J. A. Casas, A. Ibarra, "Oscillating neutrinos and $`\mu \to e, \gamma`$", Nucl. Phys. B 618 (2001) 171, arXiv:hep-ph/0103065.
