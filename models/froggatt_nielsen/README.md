# SM + Froggatt–Nielsen flavon (global $`U(1)_{\rm FN}`$, three generations) — physics card

**id** `froggatt_nielsen` · **parents** `sm_ckm` (replaces the `yukawa` sector) · **maturity** L2
(no UFO: not requested, and the model has a massless Goldstone and operators of dimension up to 10;
see "Observables that test it")

Tags: **[feynlag-verified: test]** = pinned by a test in `tests/`; **[physics judgment]** = not machine-checked.

## Problem addressed
The SM fits the nine charged-fermion masses and the CKM matrix with free Yukawas that span more
than five orders of magnitude. In the Froggatt–Nielsen (FN) mechanism a horizontal
$`U(1)_{\rm FN}`$, under which the generations carry different integer charges, forbids most
renormalizable Yukawas. A flavon $\phi$ gets a vev, and each Yukawa comes from a
higher-dimension operator with an $O(1)$ coefficient, suppressed by a power of
$`\epsilon = v_\phi/(\sqrt2\,\Lambda)`$ fixed by the charges. The hierarchy becomes a statement
about integers. The model was requested by `feynlag-anomalies` (`puzzles/flavor_puzzle`,
`model_requests/froggatt_nielsen.md`), whose stage-1 fit needs the Yukawas as functions of
$\epsilon$ and the $`c_{ij}`$. [physics judgment]

## Field content
| field | spin | $SU(3)_c \times SU(2)_L \times U(1)_Y$ | extra charges | generations |
|---|---|---|---|---|
| $\phi$ (`phi`) | $0$ (complex) | $(1, 1, 0)$ | $`U(1)_{\rm FN}`$: $+1$ (global) | 1 |
| $H$, $L_L$, $e_R$, $Q_L$, $u_R$, $d_R$ of `sm_ckm` | as in `sm_ckm` | as in `sm_ckm` | $`U(1)_{\rm FN}`$ per generation (below); $H$: $0$ | 3 |

The fermion charges are integer benchmark inputs (`qQ1` … `qe3`), so a different assignment is a
different benchmark of the same model, not a different model. At the benchmark:

| multiplet | $q_1$ | $q_2$ | $q_3$ | LNS-2 Eq. (2.5) |
|---|---|---|---|---|
| $Q_L$ (`qQ1..3`) | $3$ | $2$ | $0$ | $q(Q_L) = H(Q) = (3, 2, 0)$ |
| $u_R$ (`qu1..3`) | $-3$ | $-1$ | $0$ | $q(u_R) = -H(\bar u) = -(3, 1, 0)$ |
| $d_R$ (`qd1..3`) | $-3$ | $-2$ | $-2$ | $q(d_R) = -H(\bar d) = -(3, 2, 2)$ |
| $L_L$ (`qL1..3`) | $3$ | $2$ | $0$ | placeholder, copies $Q_L$ |
| $e_R$ (`qe1..3`) | $-3$ | $-2$ | $-2$ | placeholder, copies $d_R$ |

The quark charges are the "master model" of Leurer, Nir and Seiberg (LNS-2, hep-ph/9310320v1,
Eq. (2.5)). LNS write left-handed Weyl fields $Q$, $\bar u$, $\bar d$ and a flavon $S$ of charge
$-1$, so their $H(\bar f)$ is our $-q(f_R)$ and their $S$ is our $\phi^*$
**[feynlag-verified: `tests/test_l2_literature.py::test_benchmark_charges_are_lns_master_model`]**.
The lepton charges are a placeholder choice, not taken from the literature
(`benchmark.placeholders`). [physics judgment]

## New symmetry and breaking
$`U(1)_{\rm FN}`$ is a **global** symmetry, exact in the Lagrangian and spontaneously broken by
$`\langle\phi\rangle = v_\phi/\sqrt2`$, with $`\phi = (v_\phi + s + i a)/\sqrt2`$. The choice of a
global, exact $U(1)$ (rather than a $`Z_N`$, explicit soft breaking, or a gauged $U(1)$) was left
to the implementer by the request and is recorded in `metadata.yaml`. [physics judgment]

- Invariance holds monomial by monomial in every term of the exact Lagrangian, with $\phi$: $+1$,
  the per-generation fermion charges and $H$: $0$. One wrong charge breaks the up Yukawa, so the
  check has teeth **[feynlag-verified: `tests/test_l0_l1.py::test_global_u1_fn_every_term`]**.
  feynlag has no global continuous symmetry and no per-generation charges (FG-7), so the charges
  are counted outside feynlag (`feynlag_models.checks.global_u1_violations`); a $`Z_N`$ with one
  charge per multiplet cannot express them
  **[feynlag-verified: `test_feynlag_flavour_dependent_charge_gap`, strict xfail]**.
- The flavon phase $a$ is an exactly massless Goldstone. With the three would-be Goldstones eaten
  by $W^\pm$ and $Z$, there are four massless real scalars
  **[feynlag-verified: `test_goldstone_count`]**.
- Gauge anomalies are those of `sm_ckm`, since $\phi$ is a gauge singlet; the global
  $`U(1)_{\rm FN}`$ is not required to be anomaly-free
  **[feynlag-verified: `test_validate_exact_operators`]** (gauge anomalies only).

## New Lagrangian terms
The flavon kinetic term, the potential

```math
V \supset -\mu_\phi^2 \lvert\phi\rvert^2 + \lambda_\phi \lvert\phi\rvert^4 + \lambda_{H\phi}\, H^\dagger H\, \lvert\phi\rvert^2 ,
```

and, replacing the renormalizable Yukawas of `sm_ckm`, the exact FN operators (CONVENTIONS.md,
Froggatt–Nielsen):

```math
-\mathcal L \supset c^u_{ij} \left(\frac{\phi}{\Lambda}\right)^{n^u_{ij}} \bar Q_i \tilde H u_j + c^d_{ij} \left(\frac{\phi}{\Lambda}\right)^{n^d_{ij}} \bar Q_i H d_j + c^e_{ij} \left(\frac{\phi}{\Lambda}\right)^{n^e_{ij}} \bar L_i H e_j + \text{h.c.}, \qquad n^f_{ij} = q(F_{L,i}) - q(f_{R,j}),
```

with $\phi^*$ in place of $\phi$ when $n \lt 0$ (none at the benchmark: every power is
non-negative, as LNS-2 Eq. (4.2) requires). The 27 coefficients
$`c_{ij} = \lvert c_{ij}\rvert e^{i\alpha_{ij}}`$ (`cu11_abs`, `cu11_arg`, …) are complex. The
operators are gauge invariant, hermitian and anomaly-free, and have mass dimension 4 once each
$1/\Lambda^n$ is counted against $\phi^n$
**[feynlag-verified: `test_validate_exact_operators`]**. The power of $\phi$ in each entry
follows the charges **[feynlag-verified: `test_flavon_powers_follow_the_charges`]**. The tadpoles
are

```math
\mu^2 = \lambda v^2 + \tfrac12 \lambda_{H\phi} v_\phi^2, \qquad \mu_\phi^2 = \lambda_\phi v_\phi^2 + \tfrac12 \lambda_{H\phi} v^2
```

**[feynlag-verified: `test_tadpoles`]**.

### Two models from one set of declarations
`build()` assembles two feynlag `Model`s from the same fields and parameters.

- `bundle.extra["model_exact"]` carries the exact operators above, of dimension up to $4 + 6$ at
  the benchmark. L0 (invariance, hermiticity, anomalies, dimension) and the fermion mass matrices
  use it.
- `bundle.model` replaces every $\phi^n$ by its expansion to **linear order** in the flavon
  fluctuation, $`\phi^n \to w^{n-1}\,(n\phi - (n-1)\,w)`$ with $`w = v_\phi/\sqrt2`$. This is exact
  at the vacuum and in the couplings of one flavon to a fermion pair; it drops every vertex with two
  or more flavons attached to a fermion pair (for example $`s\,s\,\bar f f`$ and $`a\,a\,\bar f f`$). The
  spectrum, the rotations, the vertices and the generated pages use this model, because
  extracting the exact operators gives up to nine-boson vertices and was about ten times slower
  (probe on 2026-10-05). Both models give identical fermion mass matrices, and the linearised
  entries agree with the exact ones in value and first derivative at the vacuum
  **[feynlag-verified: `test_fermion_mass_matrices`, `test_flavon_powers_follow_the_charges`]**.

## Key mechanism
- **Texture.** After symmetry breaking

```math
Y^f_{ij} = c^f_{ij}\, \epsilon^{\,n^f_{ij}}, \qquad \epsilon = \frac{v_\phi}{\sqrt2\,\Lambda}, \qquad M_f = \frac{v}{\sqrt2}\, Y^f ,
```

  read off the Lagrangian by feynlag's `fermion_mass_matrix` for both models
  **[feynlag-verified: `test_fermion_mass_matrices`]**. With the master-model charges the powers
  are those of LNS-2 Eq. (2.6), down $`[[6,5,5],[5,4,4],[3,2,2]]`$ and up
  $`[[6,4,3],[5,3,2],[3,1,0]]`$, entry by entry and symbolically
  **[feynlag-verified: `tests/test_l2_literature.py::test_yukawa_texture_lns_eq_2_6`]**.
- **Determinant.** Because $`n_{ij}`$ is additive in the two charges,
  $`\det Y^f = \det(c^f)\, \epsilon^{\sum_i (q(F_{L,i}) - q(f_{R,i}))}`$ exactly: $\epsilon^{12}$
  (down) and $\epsilon^{9}$ (up), LNS-2 Eqs. (2.19) and (2.7). The product of the numeric
  singular values equals $\lvert\det Y\rvert$ at the benchmark to 40 digits
  **[feynlag-verified: `test_determinant_is_charge_sum_lns_eq_2_19`]**.
- **Mass scaling.** $`m_{f_i}/(v/\sqrt2) \sim \epsilon^{\,q(F_{L,i}) - q(f_{R,i})}`$, equivalent to
  LNS-2 Eq. (2.4) for the mass ratios. Tested in the precise sense of $\sim$: at 20 random
  $O(1)$ draws of the $`c_{ij}`$, each singular value of $Y^f$ divided by $`\epsilon^{n_{ii}}`$
  converges between $\epsilon = 10^{-3}$ and $10^{-4}$ to a finite $O(1)$ limit
  **[feynlag-verified: `test_mass_scaling_lns_eq_2_4`]**.
- **Mixing scaling.** $`\lvert V_{ij}\rvert \sim \epsilon^{\,\lvert q(Q_{L,i}) - q(Q_{L,j})\rvert}`$
  (LNS-2 Eq. (2.3), LNS-1 Eq. (5.7)), so $`\lvert V_{us}\rvert \sim \epsilon`$,
  $`\lvert V_{cb}\rvert \sim \epsilon^2`$, $`\lvert V_{ub}\rvert \sim \epsilon^3`$ and
  $`\lvert V_{ub}\rvert \sim \lvert V_{us} V_{cb}\rvert`$ (LNS-1 Eq. (5.8)), in the same limit test
  **[feynlag-verified: `test_ckm_scaling_lns_eq_2_3`]**. At the benchmark $V$ is unitary and the
  masses are ordered in each sector **[feynlag-verified: `test_unitarity_and_benchmark_spectrum`]**.
- **Flavon couplings.** Expanding $\phi^n$ around the vacuum gives, in the weak basis,

```math
\mathcal L \supset -M_{ij}\left(\frac{h}{v} + \frac{\lvert n_{ij}\rvert\, s + i\, n_{ij}\, a}{v_\phi}\right) \bar f_{L,i} f_{R,j} + \text{h.c.}, \qquad h = c_\theta h_1 - s_\theta h_2, \quad s = s_\theta h_1 + c_\theta h_2 ,
```

  for either sign of $`n_{ij}`$: $\phi^n$ gives $n(s + ia)$, while $`(\phi^*)^{\lvert n\rvert}`$
  (used when $n \lt 0$) gives $`\lvert n\rvert(s - ia)`$. Checked entry by entry for the down sector
  against feynlag's vertices, at the benchmark (every $n \ge 0$)
  **[feynlag-verified: `test_flavon_couplings`]** and at a charge set with $`q(d_{R,1}) = +4`$, whose
  first column has $n = -1, -2, -4$ **[feynlag-verified: `test_flavon_couplings_negative_powers`]**. LNS do not state this coupling in this form
  (they estimate FCNC coefficients only, LNS-2 Sec. 4.2), so the formula is a derivation, not a
  literature check. [physics judgment] Because $`n_{ij}`$ is not a constant, the flavon couplings
  are not aligned with the masses: $s$ and $a$ mediate tree-level FCNC. [physics judgment]
- **Mass basis.** The $3\times3$ Yukawas are generic complex matrices, and feynlag's
  `diagonalize_svd` is real-only (FG-6). The masses and $`V_{\rm CKM}`$ come from a numeric
  biunitary decomposition outside feynlag (`feynlag_models.flavor`, `mpmath.svd_c`)
  **[feynlag-verified: `test_feynlag_svd_complex_gap`, strict xfail; `tests/test_flavor.py`]**.
- **Scalar spectrum.** The CP-even block in the basis $(h, s)$ is
  $`[[2\lambda v^2, \lambda_{H\phi} v v_\phi], [\lambda_{H\phi} v v_\phi, 2\lambda_\phi v_\phi^2]]`$,
  rotated to $(h_1, h_2)$ by $R(\theta)$ with $h_1$ the lighter state
  **[feynlag-verified: `test_cp_even_mass_matrix_and_spectrum`]**.

## Characteristic scale
The benchmark has $\epsilon = 0.2$, the order of the expansion parameter $\lambda \sim 0.2$ of LNS-2 (Sec. 2.1), from
$v_\phi = 2\sqrt2$ TeV and $\Lambda = 10$ TeV. $\Lambda$, $`\lambda_\phi = 0.1`$ and
$`\lambda_{H\phi} = 0.01`$ are placeholders. Only $\epsilon$ enters the fermion masses and mixings;
$v_\phi$ alone sets the flavon couplings ($`n_{ij} M_{ij}/v_\phi`$) and, with $`\lambda_\phi`$,
the mass of $h_2$. At the benchmark $`m_{h_1} \approx 124.9`$ GeV, $`m_{h_2} \approx 1.26`$ TeV
and $\theta \approx -0.0044$ (computed with `bundle.values()` on 2026-10-05; see
[`outputs/spectrum.md`](outputs/spectrum.md)). [physics judgment] The FN messengers of mass
$\Lambda$ are integrated out and not in the model. [physics judgment]

## Observables that test it
- Fermion masses and $\lvert V_{ij}\rvert$, as functions of $\epsilon$ and the $`c_{ij}`$. The
  benchmark $`c_{ij}`$ are **one seeded random draw** (`numpy.random.default_rng(20261005)`,
  $\lvert c\rvert$ uniform in $[0.5, 2]$, phase uniform), **not a fit**: at the benchmark the
  masses are $O(1)$ multiples of the FN powers, not the measured values (for example
  $\lvert V_{us}\rvert \approx 0.19$, $m_t \approx 95$ GeV, computed on 2026-10-05, not pinned by a
  test). [physics judgment] Fitting is the job of `feynlag-anomalies` (P3 of the flavour puzzle).
- Flavon-mediated FCNC (meson mixing, $\mu \to e\gamma$ once leptons mix) and the massless
  Goldstone $a$ (a familon), which couples to $\bar f_i f_j$ with strength $`n_{ij} M_{ij}/v_\phi`$.
  These constrain $v_\phi$ and are not checked here. [physics judgment]
- **No UFO.** Not requested (P3 needs L2), and an export would carry a massless pseudoscalar and,
  for the exact model, operators up to dimension 10; the generated pages come from the linearised
  model (`ufo: null`). [physics judgment]

**API used by the flavour puzzle.**

- `bundle.extra["Yu"]`, `["Yd"]`, `["Ye"]`: symbolic $3\times3$ Yukawas $`c_{ij}\,\epsilon^{n_{ij}}`$
  in the symbols `eps` and `cu11_abs`, `cu11_arg`, … (`extra["Y"]` maps `up`, `down`, `lepton` to
  the same matrices; `extra["powers"]` holds the integer $`n_{ij}`$ and `extra["fn_charges"]` the
  charges).
- `bundle.extra["eps"]` is the internal parameter $\epsilon$ (`.s` its symbol, `.expr` its
  definition $`v_\phi/(\sqrt2\Lambda)`$); `extra["c_params"]` lists the 54 coefficient parameters,
  and `extra["c_abs"]`, `extra["c_arg"]` hold them per sector; `extra["C"]` the complex $c$ matrices.
- `feynlag_models.flavor.ckm_from_yukawas(Yu, Yd, values)` returns
  $`V = U_{L,u}^\dagger U_{L,d}`$ as a numpy array (rows $u, c, t$; columns $d, s, b$),
  `mass_spectrum(Y, v, values)` the ascending Dirac masses, and `numeric_biunitary(M, values)` the
  triple $`(U_L, m, U_R)`$ with $`M = U_L\,\mathrm{diag}(m)\,U_R^\dagger`$. `values` maps symbols
  to numbers, for example `bundle.values()` with `eps` and the $`c_{ij}`$ overridden. Rotations and
  $V$ are defined up to rephasing; $\lvert V\rvert$ and the masses are physical
  **[feynlag-verified: `tests/test_flavor.py`]**.

Generated pages: [`outputs/vertices.md`](outputs/vertices.md) (bosonic and fermion Feynman rules of the linearised model, grouped by vertex class) and [`outputs/spectrum.md`](outputs/spectrum.md) (masses at the benchmark).

## Genealogy
Parent: `sm_ckm` (`replaces_sector`, sector `yukawa`). The three generations, the gauge sector and
the Higgs doublet are `sm_ckm`'s; its renormalizable Yukawas and the CKM input rotation are
replaced by the FN operators, so $V$ is an output here, not an input. No children yet; see
`NEXT_STEPS.md`.

Sources: LNS-1 (hep-ph/9212278v1) and LNS-2 (hep-ph/9310320v1), read as arXiv text on
2026-10-05. Froggatt and Nielsen's 1979 paper was **not** read (paywalled; only its INSPIRE
record and abstract), so no equation of it is cited. [physics judgment]
