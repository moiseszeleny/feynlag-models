# Conventions (single source of truth)

Inherits every convention of `feynlag` (`CONVENTIONS.md` there, pinned by its
tests); this file fixes what the model library adds. A model that departs from
any item must state the map in its card.

## Markdown
Physics is written in LaTeX; code (file paths, test ids, Python and parameter identifiers,
commands, metadata keys) stays in backticks. When prose names a code object and its physics,
give both, e.g. `lamHS` ($\lambda_{HS}$). GitHub's Markdown pipeline mangles some TeX before
MathJax sees it, so these rules are enforced by `tests/test_markdown_math.py`:

- **Inline math** is `$…$`. Use the backtick-delimited form (dollar, backtick, formula,
  backtick, dollar) when the formula contains a backslash followed by punctuation (`\,`, `\{`,
  `\}`, `\;`, …; Markdown deletes the backslash) or several subscripts (GitHub may read the
  underscores as italics).
- **No `<` or `>` inside math**: GitHub double-escapes them. Write `\lt` and `\gt`
  (`\le`, `\ge` are fine).
- **Display math** is a fenced block with the language `math`, **at top level, never
  indented**; inside a list item it renders as a code block. End the list item with its text,
  put the block after it, and continue with ordinary text or a new item. Do not end a line of
  the block with a double backslash (Markdown reads it as a hard line break); start the next
  row on the same line instead (`… \\ & + …`).
- In table cells write $\vert$ as `\vert` or `\lvert…\rvert`, never a bare `|`.
- Keep a space or ordinary punctuation next to each inline formula. Two formulas joined by a
  dash or preceded by a quote mark do not render: write ranges as inequalities
  (`140 \le m_H \le 180`) or in words.
- Math does not render inside `*italics*`; put a title that contains a formula in quotes and
  use the backtick form.
- No formula Unicode (Greek letters, superscripts, $\sqrt{}$, $\dagger$, …) outside math,
  including inside code spans.

## Metric, Dirac algebra, covariant derivative
- Metric $(+,-,-,-)$; $`\{\gamma^\mu,\gamma^\nu\} = 2g^{\mu\nu}`$; $\gamma_5 = i\gamma^0\gamma^1\gamma^2\gamma^3$;
  $P_L = (1-\gamma_5)/2$, $P_R = (1+\gamma_5)/2$; $C = i\gamma^2\gamma^0$.
- $D_\mu = \partial_\mu - i g T^a A^a_\mu$ for every gauge factor.
- Kinetic terms $+(D_\mu\phi)^\dagger(D^\mu\phi)$, $+i\bar\psi\gamma^\mu D_\mu\psi$,
  $-\tfrac14 F_{\mu\nu}F^{\mu\nu}$; a real scalar has $+\tfrac12(\partial_\mu S)^2$.

## Scalar potentials (the Lagrangian stores $-V$ in sector `potential`)
- **SM**:

```math
V = -\mu^2 H^\dagger H + \lambda (H^\dagger H)^2,\qquad
H = \begin{pmatrix} G^+ \\ (v + h + i G^0)/\sqrt2 \end{pmatrix},
```

tadpole $\mu^2 = \lambda v^2$; $m_h^2 = 2\lambda v^2$; $m_W = g v/2$,
$`m_Z = \sqrt{g^2 + g'^2}\,v/2`$.
- **Real singlet ($Z_2$)**:
  $V \supset \tfrac12\mu_S^2 S^2 + \tfrac14\lambda_S S^4 + \tfrac12\lambda_{HS}(H^\dagger H)S^2$,
  with $S \to v_S + s$ (no $1/\sqrt2$ for a real field). The CP-even block is in the basis
  $(h, s)$. Mass eigenstates $(h_1, h_2) = R(\theta)(h, s)$; $h_1$ is the lighter state at the
  benchmark.
- **2HDM (CP-conserving, softly broken $Z_2$)**, in the Gunion–Haber / Branco et al. form, all
  parameters real:

```math
\begin{aligned}
V ={}& m_{11}^2 H_1^\dagger H_1 + m_{22}^2 H_2^\dagger H_2
      - m_{12}^2\left(H_1^\dagger H_2 + \text{h.c.}\right)
      + \tfrac12\lambda_1 (H_1^\dagger H_1)^2 + \tfrac12\lambda_2 (H_2^\dagger H_2)^2
    \\ & + \lambda_3 (H_1^\dagger H_1)(H_2^\dagger H_2) + \lambda_4 \lvert H_1^\dagger H_2\rvert^2
      + \tfrac12\lambda_5\left[(H_1^\dagger H_2)^2 + \text{h.c.}\right],
\end{aligned}
```

$H_i = \big(H_i^+,\ (v_i + \rho_i + i\eta_i)/\sqrt2\big)$, $\tan\beta = v_2/v_1$,
$v^2 = v_1^2 + v_2^2 \approx (246\ \text{GeV})^2$.
$Z_2$: $H_2 \to -H_2$, and the only $Z_2$-odd term is the $m_{12}^2$ term. Type II:
$u_R \to -u_R$ (couples to $\tilde H_2$); $d_R$ and $e_R$ are even (couple to $H_1$).

## Rotations
feynlag's `rotation_2x2(theta)` is

```math
R(\theta) = \begin{pmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{pmatrix},
\qquad \text{new} = R \cdot \text{old}.
```

- $(H, h) = R(\alpha)(\rho_1, \rho_2)$: $H = c_\alpha\rho_1 + s_\alpha\rho_2$,
  $h = -s_\alpha\rho_1 + c_\alpha\rho_2$; $h$ is the lighter CP-even state.
- $(G^0, A) = R(\beta)(\eta_1, \eta_2)$; $(G^+, H^+) = R(\beta)(H_1^+, H_2^+)$.
- Singlet: $(h_1, h_2) = R(\theta)(h, s)$, with $\tan 2\theta$ from the off-diagonal condition.
- Weinberg: $(Z, A) = R(-\theta_W)(W^3, B)$, $\tan\theta_W = g'/g$;
  $W^\pm = (W^1 \mp i W^2)/\sqrt2$.
- Every angle is verified against its defining $\tan 2\theta$ relation, not only
  $c^2 + s^2 = 1$.

## Fermions
- One generation per model unless the model says otherwise, with third-generation names
  $t, b, \tau, \nu_\tau$. Dirac fermions are two Weyl fields (`tL`/`tR`, …). Yukawas are
  $`-y\,\bar\psi_L\Phi\psi_R + \text{h.c.}`$ with $\tilde\Phi = (\Phi^{0*}, -\Phi^{+*})$.
  The Dirac mass is $m_f = y_f v/\sqrt2$ (SM, seesaw, singlet) or $y_f v_i/\sqrt2$ (2HDM).
- **Three generations** (`sm.pieces(generations=3)`, used by `sm_ckm`): flavour indices are the
  integers $0, 1, 2$, the Yukawa matrices enter as $`-Y^{ab}\,\bar\psi_{L a}\Phi\psi_{R b} + \text{h.c.}`$,
  and $Y_u$, $Y_e$ are diagonal. Quark mixing lives in the down sector:
  $`Y_d = V\,\mathrm{diag}(y_d, y_s, y_b)`$ and the mass basis is $d_L' = V d_L$, so the charged
  current is $`\bar u_{L i} V_{ij} d_{L j}`$. Rows of $V$ are $u, c, t$ and columns are $d, s, b$.
- **CKM matrix**: feynlag's `standard_ckm`, the PDG standard parametrization (PDG 2024 CKM review,
  Eq. 12.3) in `th12`, `th13`, `th23` ($\theta_{ij}$, first quadrant) and `deltaCP` ($\delta$), with
  complex internals `Vud` … `Vtb`. Leptons have no mixing (neutrinos are massless).
- The Majorana mass is $`-\tfrac12 M_R\,\nu_R^T C\nu_R + \text{h.c.}`$ In the seesaw basis
  $n = (\nu_L, \nu_R^c)$:

```math
M_\nu = \begin{pmatrix} 0 & m_D \\ m_D^T & M_R \end{pmatrix},\qquad
M_\nu = U D U^T\ (D \ge 0),\qquad
m_\nu \approx -m_D M_R^{-1} m_D^T .
```

## Feynman rules and export
- The vertex is

```math
i\,\frac{\partial^n \mathcal L}{\partial\phi_1\cdots\partial\phi_n}\bigg\vert_0
= i \times (\text{monomial coefficient}) \times \prod_f (\text{multiplicity of } f)!\,.
```

- Momenta are incoming, and $`\partial_\mu\phi \to i\,p(\phi)_\mu\,\phi`$ (feynlag's convention,
  pinned by its VSS test).
- UFO triple-gauge couplings built from the complex $W^\pm$ rotation are sign-flipped
  (`gAWW`, `gZWW`) at export, following the feynlag MadGraph benchmark. The flip lives in
  `feynlag_models/ufo.py` and nowhere else.
- UFO fermion couplings are the raw Lagrangian coefficients; the writer applies the $i$.

## Names and PDG codes
| state | physics symbol | code symbol | UFO name | PDG | note |
|---|---|---|---|---|---|
| CP-even Higgs (SM-like) | $h$, $h_1$ | `h`, `h1` | `h` | 25 | |
| second CP-even | $H$ (2HDM), $h_2$ (singlet) | `H`, `h2` | `h2` | 35 | FeynRules-2HDM-style lowercase names avoid case clashes in MadGraph |
| CP-odd | $A$ | `A0` | `h3` | 36 | |
| charged Higgs | $H^\pm$ | `Hp`, `Hm` | `h+`, `h-` | 37 | |
| neutral / charged Goldstone | $G^0$, $G^\pm$ | `G0`, `Gp`, `Gm` | `G0`, `G+`, `G-` | 250, 251 | as in the FeynRules SM; dropped from unitary-gauge exports |
| $Z$, photon, $W$ | $Z$, $A$, $W^\pm$ | `Z`, `A`, `Wp`, `Wm` | `Z`, `a`, `W+`, `W-` | 23, 22, 24 | |
| heavy Majorana neutrino | $N$ | `chiL[k]`, `chiR[k]` | none (not exportable, FG-3) | 9900012 | HeavyN-UFO style code — TODO(verify) |
| leptons / quarks | $\tau$, $\nu_\tau$, $t$, $b$ | `ta`, `vt`, `t`, `b` | `ta-`, `vt`, `t`, `b` | 15, 16, 6, 5 | |
| three generations | $u, c, t$; $d, s, b$; $e, \mu, \tau$; $\nu_e, \nu_\mu, \nu_\tau$ | same, `mu`, `ve`, `vm` | `u c t`, `d s b`, `e- mu- ta-`, `ve vm vt` | 2, 4, 6; 1, 3, 5; 11, 13, 15; 12, 14, 16 | FeynRules SM names |

Parameter names are snake ASCII and UFO-safe (`lam_HS`, `vS`, `m12sq`, `tanb`).
Model ids match `^[a-z0-9_]+$` and equal their directory names.

## Verification discipline
- Dual check for every physical result: `sp.simplify(a - b) == 0` **and**
  `feynlag.numeric_equal(a, b, symbols)` at random points (`feynlag_models.checks.dual_equal`).
- Benchmark numbers come from `metadata.yaml` `benchmark.inputs` only.
- Every statement in a card is tagged **[feynlag-verified: test]** or **[physics judgment]**.
- Unknown numbers, bounds, equation numbers or citations are written `TODO(verify)`.
