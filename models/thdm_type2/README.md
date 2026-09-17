# Two-Higgs-doublet model, type II (CP-conserving, softly broken $Z_2$) — physics card

**id** `thdm_type2` · **parents** `sm` · **maturity** L3 (UFO round-trip; no MadGraph run)

Tags: **[feynlag-verified: test]** = pinned by a test in `tests/`; **[physics judgment]** = not machine-checked.

## Problem addressed
The minimal extended Higgs sector: a second doublet gives a charged Higgs $H^\pm$, a CP-odd $A$
and a second CP-even $H$, with natural flavour conservation enforced by a $Z_2$. Type II, where up-type
quarks couple to $\Phi_2$ and down-type quarks and leptons to $\Phi_1$, is the Yukawa pattern of the MSSM
Higgs sector and the standard target for $\tan\beta$, charged-Higgs and alignment-limit studies. [physics judgment]

## Field content
| field | spin | $SU(3)_c \times SU(2)_L \times U(1)_Y$ | extra charges | generations |
|---|---|---|---|---|
| $H_1$ (`H1`, replaces the SM $H$) | $0$ | $(1, 2, \tfrac12)$ | $Z_2$: $+1$ | 1 |
| $H_2$ (`H2`) | $0$ | $(1, 2, \tfrac12)$ | $Z_2$: $-1$ | 1 |
| $u_R$ (`uR`, SM field, now $Z_2$-odd) | $\tfrac12$ (R) | $(3, 1, \tfrac23)$ | $Z_2$: $-1$ | 1 |
| + the rest of `sm` | | | $Z_2$: $+1$ | |

Anomalies cancel as in the SM (no new fermions) **[feynlag-verified: `tests/test_l0_l1.py::test_validate_invariance_and_anomalies`]**.

## New symmetry and breaking
$Z_2$: $H_2 \to -H_2$, $u_R \to -u_R$. It is **softly broken** by the dimension-two term
$`-m_{12}^2(H_1^\dagger H_2 + \text{h.c.})`$, the *only* $Z_2$-odd term in the Lagrangian, kinetic terms
included **[feynlag-verified: `test_z2_softly_broken_only_by_m12sq`]**. Electroweak symmetry is broken by
$`\langle H_i^0\rangle = v_i/\sqrt2`$, with $\tan\beta = v_2/v_1$ and $v^2 = v_1^2 + v_2^2$.

## New Lagrangian terms
The potential is Branco et al. Eq. (2), equivalently Gunion–Haber Eq. (1) with $\lambda_6 = \lambda_7 = 0$:

```math
\begin{aligned}
V ={}& m_{11}^2 H_1^\dagger H_1 + m_{22}^2 H_2^\dagger H_2 - m_{12}^2\left(H_1^\dagger H_2 + \text{h.c.}\right)
      + \tfrac12\lambda_1 (H_1^\dagger H_1)^2 + \tfrac12\lambda_2 (H_2^\dagger H_2)^2
    \\ & + \lambda_3 (H_1^\dagger H_1)(H_2^\dagger H_2) + \lambda_4 \lvert H_1^\dagger H_2\rvert^2
      + \tfrac12\lambda_5\left[(H_1^\dagger H_2)^2 + \text{h.c.}\right].
\end{aligned}
```

The kinetic terms are $\lvert D H_1\rvert^2 + \lvert D H_2\rvert^2$, and the type-II Yukawas are

```math
-y_\tau \bar L_L H_1 e_R - y_b \bar Q_L H_1 d_R - y_t \bar Q_L \tilde H_2 u_R + \text{h.c.},\qquad
y_b = \frac{\sqrt2 m_b}{v_1},\quad y_\tau = \frac{\sqrt2 m_\tau}{v_1},\quad y_t = \frac{\sqrt2 m_t}{v_2}
```

**[feynlag-verified: `test_fermion_masses`]**.

## Key mechanism
- Tadpoles (GH Eqs. 6–7) **[feynlag-verified: `test_tadpoles_gunion_haber_eq6_eq7`]**:
  $`m_{11}^2 = m_{12}^2 t_\beta - \tfrac12 v^2(\lambda_1 c_\beta^2 + \lambda_{345} s_\beta^2)`$, and $m_{22}^2$
  by exchanging $1 \leftrightarrow 2$.
- Mass blocks: the CP-even block equals Branco Eq. (7) and GH Eqs. (12)–(13). The CP-odd and charged blocks
  are proportional to the same matrix, with one Goldstone each **[feynlag-verified: `test_mass_blocks`]**:

```math
M^2_{\text{odd}},\ M^2_{\pm} \propto \begin{pmatrix} v_2^2 & -v_1 v_2 \\ -v_1 v_2 & v_1^2 \end{pmatrix},\qquad
m_A^2 = \frac{m_{12}^2}{s_\beta c_\beta} - \lambda_5 v^2,\qquad
m_{H^\pm}^2 = m_A^2 + \tfrac12 v^2(\lambda_5 - \lambda_4)
```

(GH Eqs. 10–11) **[feynlag-verified: `test_mA_mHp_gunion_haber_eq10_eq11`]**. The same values follow
from Branco's potential with plain SymPy, without feynlag
**[verified: `test_mA_mHp_independent_of_feynlag`]**. Branco et al.'s printed formulas (arXiv v1–v3)
have $-2\lambda_5$ and $-\lambda_4 - \lambda_5$ instead, which is inconsistent with their own potential
(discrepancy D-2, open, strict xfail `test_mA_mHp_branco_arxiv_text_eq5_6`; the published text was not
accessible).
- The rotations $`(H, h) = R(\alpha)(\rho_1, \rho_2)`$, $`(G^0, A) = R(\beta)(\eta_1, \eta_2)`$ and
  $`(G^+, H^+) = R(\beta)(H_1^+, H_2^+)`$ diagonalise the three blocks, leaving three Goldstones for
  $W^\pm$ and $Z$
  **[feynlag-verified: `test_spectrum_and_rotations_at_benchmark`, `test_goldstone_count_and_gauge_masses`]**.
  feynlag's $`\alpha = \tfrac12\arctan\big(2M_{12}/(M_{11} - M_{22})\big)`$ has $\cos 2\alpha \gt 0$, so the
  label $H$ is the heavier state only when $M_{11} \gt M_{22}$. That holds at the benchmark; GH Eq. (17)
  chooses the branch with $m_H \ge m_h$ instead. [physics judgment on conventions]
- $hVV = \text{SM} \times \sin(\beta - \alpha)$, $HVV = \text{SM} \times \cos(\beta - \alpha)$, and there is
  no $AVV$ vertex **[feynlag-verified: `tests/test_l2_literature.py::test_hVV_HVV_sin_cos_beta_minus_alpha`]**
- Type-II Yukawa factors (Branco Table 2), with the $\bar f\gamma_5 f$ chiral structure for $A$
  **[feynlag-verified: `test_neutral_yukawa_xi_factors_table2`]**:

```math
\xi_h^u = \frac{c_\alpha}{s_\beta},\quad \xi_h^{d,\ell} = -\frac{s_\alpha}{c_\beta},\quad
\xi_H^u = \frac{s_\alpha}{s_\beta},\quad \xi_H^{d,\ell} = \frac{c_\alpha}{c_\beta},\quad
\xi_A^u = \cot\beta,\quad \xi_A^{d,\ell} = \tan\beta .
```

- Charged Higgs: $`\lvert H^+\bar t b\rvert = (\sqrt2/v)(m_t\cot\beta\,P_L + m_b\tan\beta\,P_R)`$, with the
  same sign for both chiralities as in Branco Eq. (16), and
  $`\lvert H^+\bar\nu\tau\rvert = (\sqrt2/v)\,m_\tau\tan\beta\,P_R`$
  **[feynlag-verified: `test_charged_higgs_yukawa_eq16`]**. The d-quark and lepton $H^+$ terms come out with
  the **same** sign; a hand derivation from the identical $\bar Q_L H_1 d_R$ and $\bar L_L H_1 e_R$
  structures agrees **[feynlag-verified: `test_charged_higgs_quark_lepton_same_sign_derived`]**. Branco et al.
  Eq. (16) and Aoki et al. Eq. (6) put one minus sign in front of a bracket holding both terms, so they agree
  on this relative sign **[feynlag-verified: `test_charged_higgs_quark_lepton_relative_sign_eq16`]**. Their
  overall sign of the $H^+$ line is opposite to ours, which is the unobservable redefinition
  $H^+ \to -H^+$ (metadata discrepancy D-3, a convention).
- Alignment, $\cos(\beta - \alpha) \to 0$, recovers every SM $h$ coupling
  **[feynlag-verified: `test_alignment_limit_recovers_sm_h`]**.

## Characteristic scale
$`m_A \sim m_H \sim m_{H^\pm} \sim \sqrt{m_{12}^2/(s_\beta c_\beta)}`$ (the soft scale), up to
$\lambda_i v^2$ splittings. The SM-like limit is decoupling ($m_{12}^2 \to \infty$) or alignment
($\cos(\beta - \alpha) \to 0$). Benchmark: $\tan\beta = 2$, $\cos(\beta - \alpha) = 0.1$ and
$`(m_h, m_H, m_A, m_{H^\pm}) = (125, 300, 300, 320)`$ GeV, inverted into the $\lambda_i$
(`outputs/spectrum.md` lists the re-derived values). [physics judgment]

## Observables that test it
$B \to X_s\gamma$ (type II: a strong lower bound on $m_{H^\pm}$), $B_s \to \mu\mu$ and
$b \to s\ell\ell$; Higgs signal strengths ($\sin(\beta - \alpha)$, $\xi_h^f$); direct searches for
$A/H \to \tau\tau$ at large $\tan\beta$ and for $H^+ \to tb, \tau\nu$; electroweak precision (the $T$
parameter from the splitting between $m_A$ and $m_{H^\pm}$). [physics judgment; see `NEXT_STEPS.md`]

## Genealogy
Parent: `sm` (Higgs sector replaced). Proposed children: `thdm_type1`, `thdm_type_x` and `thdm_type_y`
(other $Z_2$ charges), `inert_doublet` (exact $Z_2$, $v_2 = 0$), a CP-violating 2HDM (complex
$m_{12}^2$ and $\lambda_5$), 2HDM + singlet (N2HDM), and `thdm_s3` (3HDM with $S_3$; feynlag ships the
invariant-potential machinery). See `GENEALOGY.md`.
