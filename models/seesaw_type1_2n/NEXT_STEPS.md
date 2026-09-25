# Next steps — `seesaw_type1_2n`

## 1. Natural extensions
- A benchmark fitted to the two measured oscillation splittings and the PMNS angles, through the
  two-$\nu_R$ Casas–Ibarra form (Ibarra–Ross, Phys. Lett. B 591 (2004) 285, Eq. (6), already
  reproduced by `test_casas_ibarra_two_rhn_eq_6` for arbitrary inputs). Only complex $z$ and
  the PMNS phases are missing; `numeric_takagi` would need a complex version.
- `seesaw_type1_3gen`: three $\nu_R$ with a $6\times6$ block (the lightest neutrino then becomes massive).
- A non-diagonal $M_R$, or complex Yukawas (CP phases and leptogenesis). `numeric_takagi` handles
  real matrices only; complex ones need a numeric SVD-based Takagi.
- CKM mixing in the quark sector (combine with `sm_ckm`), which does not change the neutrino sector at tree level.

## 2. Observables and current bounds
| observable | value / bound | source | checked on |
|---|---|---|---|
| $\Delta m^2_{21}$, $\lvert\Delta m^2_{3\ell}\rvert$ | TODO(verify) | global oscillation fit (to be read, not quoted from memory) | — |
| $0\nu\beta\beta$ and $\sum m_\nu$ | see `models/seesaw_type1/NEXT_STEPS.md` §2 (the same sources apply) | PDG 2024, KamLAND-Zen, Planck 2018 | 2026-09-17 |
| $\lvert V_{\ell N}\rvert^2$ against $m_N$ | TODO(verify) | heavy-neutral-lepton searches | — |

## 3. Open theoretical questions
- Which texture of $y^\nu$ reproduces normal ordering with $m_1 = 0$, and how much tuning a TeV-scale $M_R$ needs.
- Leptogenesis needs complex $y^\nu$; the present real benchmark has no CP violation.

## 4. What feynlag cannot yet do for this model
- **FG-3**: no UFO export of Majorana-fermion vertices, so the model stops at L2.
- **FG-5**: `diagonalize_takagi` is symbolic and does not finish on the generic $5\times5$; the workaround
  `feynlag_models.checks.numeric_takagi` is used instead, so masses and mixings exist only at numeric points.
- No loops ($\mu \to e\gamma$ from $N$ exchange), and no $0\nu\beta\beta$ amplitude.

## 5. Key references
1. P. Minkowski, "$`\mu \to e\gamma`$ at a rate of one out of $`10^9`$ muon decays?", Phys. Lett. B 67 (1977) 421.
2. A. Atre, T. Han, S. Pascoli, B. Zhang, *The Search for Heavy Majorana Neutrinos*, JHEP 05 (2009) 030, arXiv:0901.3589.
3. A. Ibarra, G. G. Ross, *Neutrino phenomenology: the case of two right-handed neutrinos*, Phys. Lett. B 591 (2004) 285, arXiv:hep-ph/0312138.
4. P. H. Frampton, S. L. Glashow, T. Yanagida, *Cosmological sign of neutrino CP violation*, Phys. Lett. B 548 (2002) 119, arXiv:hep-ph/0208157 (the minimal two-$\nu_R$ seesaw with $m(\nu_1) = 0$, for a two-zero texture).
5. J. A. Casas, A. Ibarra, "Oscillating neutrinos and $`\mu \to e, \gamma`$", Nucl. Phys. B 618 (2001) 171, arXiv:hep-ph/0103065.
