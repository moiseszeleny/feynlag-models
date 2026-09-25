# Feynman rules: Type-I seesaw with three lepton generations and two right-handed neutrinos

Tree-level vertices of `seesaw_type1_2n` as feynlag derives them: 38 bosonic (potential and kinetic sectors) and the fermion couplings below.
This page re-renders the rules of [`vertices.tex`](vertices.tex) with physics names; it adds no verification. See the [card](../README.md) for what the tests pin against the literature, [`spectrum.md`](spectrum.md) for the masses.

Each rule is $`i \times (\text{monomial coefficient}) \times \prod_f (\text{multiplicity of } f)!`$, all momenta are incoming and $`\partial_\mu \to i\,p_\mu`$ ([`CONVENTIONS.md`](../../../CONVENTIONS.md)); $`p_X`$ is the momentum of leg $`X`$.

## Bosonic vertices: 38 in all

### Cubic scalar (SSS): 1 vertex

| interaction | Feynman rule |
|---|---|
| $`h h h`$ | $`- 6 i {\lambda} {v}`$ |

### Quartic scalar (SSSS): 1 vertex

| interaction | Feynman rule |
|---|---|
| $`h h h h`$ | $`- 6 i {\lambda}`$ |

### Two vectors and a scalar (VVS): 2 vertices

| interaction | Feynman rule |
|---|---|
| $`W^- W^+ h`$ | $`\frac{i {g}^{2} {v}}{2}`$ |
| $`Z Z h`$ | $`\frac{i {v} \left({g'}^{2} + {g}^{2}\right)}{2}`$ |

### Two vectors and two scalars (VVSS): 2 vertices

| interaction | Feynman rule |
|---|---|
| $`W^- W^+ h h`$ | $`\frac{i {g}^{2}}{2}`$ |
| $`Z Z h h`$ | $`\frac{i \left({g'}^{2} + {g}^{2}\right)}{2}`$ |

### Feynman-gauge vertices with a Goldstone leg: 32 in all

The unitary-gauge UFO drops these; they matter for a Feynman-gauge calculation.

#### Cubic scalar (SSS): 2 vertices

| interaction | Feynman rule |
|---|---|
| $`G^- G^+ h`$ | $`- 2 i {\lambda} {v}`$ |
| $`G^0 G^0 h`$ | $`- 2 i {\lambda} {v}`$ |

#### Quartic scalar (SSSS): 5 vertices

| interaction | Feynman rule |
|---|---|
| $`G^- G^- G^+ G^+`$ | $`- 4 i {\lambda}`$ |
| $`G^- G^+ G^0 G^0`$ | $`- 2 i {\lambda}`$ |
| $`G^- G^+ h h`$ | $`- 2 i {\lambda}`$ |
| $`G^0 G^0 G^0 G^0`$ | $`- 6 i {\lambda}`$ |
| $`G^0 G^0 h h`$ | $`- 2 i {\lambda}`$ |

#### Vector and two scalars (VSS): 7 vertices

| interaction | Feynman rule |
|---|---|
| $`\gamma G^- G^+`$ | $`\frac{i {g'} {g} \left({p_{G^-}} - {p_{G^+}}\right)}{\sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`Z G^- G^+`$ | $`\frac{i \left(- {g'}^{2} {p_{G^-}} + {g'}^{2} {p_{G^+}} + {g}^{2} {p_{G^-}} - {g}^{2} {p_{G^+}}\right)}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`W^+ G^- G^0`$ | $`\frac{{g} \left(- {p_{G^-}} + {p_{G^0}}\right)}{2}`$ |
| $`W^+ G^- h`$ | $`\frac{i {g} \left({p_{G^-}} - {p_{h}}\right)}{2}`$ |
| $`W^- G^+ G^0`$ | $`\frac{{g} \left(- {p_{G^+}} + {p_{G^0}}\right)}{2}`$ |
| $`W^- G^+ h`$ | $`\frac{i {g} \left(- {p_{G^+}} + {p_{h}}\right)}{2}`$ |
| $`Z G^0 h`$ | $`\frac{- {g'}^{2} {p_{G^0}} + {g'}^{2} {p_{h}} - {g}^{2} {p_{G^0}} + {g}^{2} {p_{h}}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |

#### Two vectors and a scalar (VVS): 4 vertices

| interaction | Feynman rule |
|---|---|
| $`\gamma W^+ G^-`$ | $`\frac{i {g'} {g}^{2} {v}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`\gamma W^- G^+`$ | $`\frac{i {g'} {g}^{2} {v}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`W^+ Z G^-`$ | $`- \frac{i {g'}^{2} {g} {v}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`W^- Z G^+`$ | $`- \frac{i {g'}^{2} {g} {v}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |

#### Two vectors and two scalars (VVSS): 14 vertices

| interaction | Feynman rule |
|---|---|
| $`\gamma \gamma G^- G^+`$ | $`\frac{2 i {g'}^{2} {g}^{2}}{{g'}^{2} + {g}^{2}}`$ |
| $`\gamma Z G^- G^+`$ | $`\frac{i {g'} {g} \left(- {g'}^{2} + {g}^{2}\right)}{{g'}^{2} + {g}^{2}}`$ |
| $`\gamma W^+ G^- G^0`$ | $`- \frac{{g'} {g}^{2}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`\gamma W^+ G^- h`$ | $`\frac{i {g'} {g}^{2}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`\gamma W^- G^+ G^0`$ | $`\frac{{g'} {g}^{2}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`\gamma W^- G^+ h`$ | $`\frac{i {g'} {g}^{2}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`W^- W^+ G^- G^+`$ | $`\frac{i {g}^{2}}{2}`$ |
| $`Z Z G^- G^+`$ | $`\frac{i \left(\frac{{g'}^{4}}{2} - {g'}^{2} {g}^{2} + \frac{{g}^{4}}{2}\right)}{{g'}^{2} + {g}^{2}}`$ |
| $`W^+ Z G^- G^0`$ | $`\frac{{g'}^{2} {g}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`W^+ Z G^- h`$ | $`- \frac{i {g'}^{2} {g}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`W^- Z G^+ G^0`$ | $`- \frac{{g'}^{2} {g}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`W^- Z G^+ h`$ | $`- \frac{i {g'}^{2} {g}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`W^- W^+ G^0 G^0`$ | $`\frac{i {g}^{2}}{2}`$ |
| $`Z Z G^0 G^0`$ | $`\frac{i \left({g'}^{2} + {g}^{2}\right)}{2}`$ |

## Fermion vertices: 48 in all

One boson leg each, flattened as the UFO export flattens them: chiral keys merged into $`P_L`$/$`P_R`$ slots, redundant colour copies dropped, Yukawa couplings resolved to masses. Gluon couplings are not included (no colour-octet particle is declared). Unlike the export, which is in unitary gauge, the Goldstone vertices are kept here; they are in their own subsection below.

### Fermion pair and a vector (FFV): 24 vertices

| interaction | Feynman rule |
|---|---|
| $`\bar{\mu} \mu Z`$ | $`i \gamma^\mu \left[\left(\frac{{g'}^{2} - {g}^{2}}{2 \sqrt{{g'}^{2} + {g}^{2}}}\right) P_L + \left(\frac{{g'}^{2}}{\sqrt{{g'}^{2} + {g}^{2}}}\right) P_R\right]`$ |
| $`\bar{\mu} \mu \gamma`$ | $`i \gamma^\mu \left(- \frac{{g'} {g}}{\sqrt{{g'}^{2} + {g}^{2}}}\right)`$ |
| $`\bar{\tau} \tau Z`$ | $`i \gamma^\mu \left[\left(\frac{{g'}^{2} - {g}^{2}}{2 \sqrt{{g'}^{2} + {g}^{2}}}\right) P_L + \left(\frac{{g'}^{2}}{\sqrt{{g'}^{2} + {g}^{2}}}\right) P_R\right]`$ |
| $`\bar{\tau} \tau \gamma`$ | $`i \gamma^\mu \left(- \frac{{g'} {g}}{\sqrt{{g'}^{2} + {g}^{2}}}\right)`$ |
| $`\bar{b} b Z`$ | $`i \gamma^\mu \left[\left(\frac{- {g'}^{2} - 3 {g}^{2}}{6 \sqrt{{g'}^{2} + {g}^{2}}}\right) P_L + \left(\frac{{g'}^{2}}{3 \sqrt{{g'}^{2} + {g}^{2}}}\right) P_R\right]`$ |
| $`\bar{b} b \gamma`$ | $`i \gamma^\mu \left(- \frac{{g'} {g}}{3 \sqrt{{g'}^{2} + {g}^{2}}}\right)`$ |
| $`\bar{b} t W^-`$ | $`i \gamma^\mu \left(\frac{\sqrt{2} {g}}{2}\right) P_L`$ |
| $`\bar{c} c Z`$ | $`i \gamma^\mu \left[\left(\frac{- {g'}^{2} + 3 {g}^{2}}{6 \sqrt{{g'}^{2} + {g}^{2}}}\right) P_L + \left(- \frac{2 {g'}^{2}}{3 \sqrt{{g'}^{2} + {g}^{2}}}\right) P_R\right]`$ |
| $`\bar{c} c \gamma`$ | $`i \gamma^\mu \left(\frac{2 {g'} {g}}{3 \sqrt{{g'}^{2} + {g}^{2}}}\right)`$ |
| $`\bar{c} s W^+`$ | $`i \gamma^\mu \left(\frac{\sqrt{2} {g}}{2}\right) P_L`$ |
| $`\bar{d} d Z`$ | $`i \gamma^\mu \left[\left(\frac{- {g'}^{2} - 3 {g}^{2}}{6 \sqrt{{g'}^{2} + {g}^{2}}}\right) P_L + \left(\frac{{g'}^{2}}{3 \sqrt{{g'}^{2} + {g}^{2}}}\right) P_R\right]`$ |
| $`\bar{d} d \gamma`$ | $`i \gamma^\mu \left(- \frac{{g'} {g}}{3 \sqrt{{g'}^{2} + {g}^{2}}}\right)`$ |
| $`\bar{d} u W^-`$ | $`i \gamma^\mu \left(\frac{\sqrt{2} {g}}{2}\right) P_L`$ |
| $`\bar{e} e Z`$ | $`i \gamma^\mu \left[\left(\frac{{g'}^{2} - {g}^{2}}{2 \sqrt{{g'}^{2} + {g}^{2}}}\right) P_L + \left(\frac{{g'}^{2}}{\sqrt{{g'}^{2} + {g}^{2}}}\right) P_R\right]`$ |
| $`\bar{e} e \gamma`$ | $`i \gamma^\mu \left(- \frac{{g'} {g}}{\sqrt{{g'}^{2} + {g}^{2}}}\right)`$ |
| $`\bar{s} c W^-`$ | $`i \gamma^\mu \left(\frac{\sqrt{2} {g}}{2}\right) P_L`$ |
| $`\bar{s} s Z`$ | $`i \gamma^\mu \left[\left(\frac{- {g'}^{2} - 3 {g}^{2}}{6 \sqrt{{g'}^{2} + {g}^{2}}}\right) P_L + \left(\frac{{g'}^{2}}{3 \sqrt{{g'}^{2} + {g}^{2}}}\right) P_R\right]`$ |
| $`\bar{s} s \gamma`$ | $`i \gamma^\mu \left(- \frac{{g'} {g}}{3 \sqrt{{g'}^{2} + {g}^{2}}}\right)`$ |
| $`\bar{t} b W^+`$ | $`i \gamma^\mu \left(\frac{\sqrt{2} {g}}{2}\right) P_L`$ |
| $`\bar{t} t Z`$ | $`i \gamma^\mu \left[\left(\frac{- {g'}^{2} + 3 {g}^{2}}{6 \sqrt{{g'}^{2} + {g}^{2}}}\right) P_L + \left(- \frac{2 {g'}^{2}}{3 \sqrt{{g'}^{2} + {g}^{2}}}\right) P_R\right]`$ |
| $`\bar{t} t \gamma`$ | $`i \gamma^\mu \left(\frac{2 {g'} {g}}{3 \sqrt{{g'}^{2} + {g}^{2}}}\right)`$ |
| $`\bar{u} d W^+`$ | $`i \gamma^\mu \left(\frac{\sqrt{2} {g}}{2}\right) P_L`$ |
| $`\bar{u} u Z`$ | $`i \gamma^\mu \left[\left(\frac{- {g'}^{2} + 3 {g}^{2}}{6 \sqrt{{g'}^{2} + {g}^{2}}}\right) P_L + \left(- \frac{2 {g'}^{2}}{3 \sqrt{{g'}^{2} + {g}^{2}}}\right) P_R\right]`$ |
| $`\bar{u} u \gamma`$ | $`i \gamma^\mu \left(\frac{2 {g'} {g}}{3 \sqrt{{g'}^{2} + {g}^{2}}}\right)`$ |

### Fermion pair and a scalar (FFS): 9 vertices

| interaction | Feynman rule |
|---|---|
| $`\bar{\mu} \mu h`$ | $`i \left(- \frac{{m_\mu}}{{v}}\right)`$ |
| $`\bar{\tau} \tau h`$ | $`i \left(- \frac{{m_\tau}}{{v}}\right)`$ |
| $`\bar{b} b h`$ | $`i \left(- \frac{{m_b}}{{v}}\right)`$ |
| $`\bar{c} c h`$ | $`i \left(- \frac{{m_c}}{{v}}\right)`$ |
| $`\bar{d} d h`$ | $`i \left(- \frac{{m_d}}{{v}}\right)`$ |
| $`\bar{e} e h`$ | $`i \left(- \frac{{m_e}}{{v}}\right)`$ |
| $`\bar{s} s h`$ | $`i \left(- \frac{{m_s}}{{v}}\right)`$ |
| $`\bar{t} t h`$ | $`i \left(- \frac{{m_t}}{{v}}\right)`$ |
| $`\bar{u} u h`$ | $`i \left(- \frac{{m_u}}{{v}}\right)`$ |

### Fermion pairs with a Goldstone leg (Feynman gauge): 15 vertices

Absent from the unitary-gauge UFO, which drops every Goldstone leg.

#### Fermion pair and a scalar (FFS): 15 vertices

| interaction | Feynman rule |
|---|---|
| $`\bar{\mu} \mu G^0`$ | $`i \left[\left(\frac{i {m_\mu}}{{v}}\right) P_L + \left(- \frac{i {m_\mu}}{{v}}\right) P_R\right]`$ |
| $`\bar{\tau} \tau G^0`$ | $`i \left[\left(\frac{i {m_\tau}}{{v}}\right) P_L + \left(- \frac{i {m_\tau}}{{v}}\right) P_R\right]`$ |
| $`\bar{b} b G^0`$ | $`i \left[\left(\frac{i {m_b}}{{v}}\right) P_L + \left(- \frac{i {m_b}}{{v}}\right) P_R\right]`$ |
| $`\bar{b} t G^-`$ | $`i \left[\left(- \frac{\sqrt{2} {m_b}}{{v}}\right) P_L + \left(\frac{\sqrt{2} {m_t}}{{v}}\right) P_R\right]`$ |
| $`\bar{c} c G^0`$ | $`i \left[\left(- \frac{i {m_c}}{{v}}\right) P_L + \left(\frac{i {m_c}}{{v}}\right) P_R\right]`$ |
| $`\bar{c} s G^+`$ | $`i \left[\left(\frac{\sqrt{2} {m_c}}{{v}}\right) P_L + \left(- \frac{\sqrt{2} {m_s}}{{v}}\right) P_R\right]`$ |
| $`\bar{d} d G^0`$ | $`i \left[\left(\frac{i {m_d}}{{v}}\right) P_L + \left(- \frac{i {m_d}}{{v}}\right) P_R\right]`$ |
| $`\bar{d} u G^-`$ | $`i \left[\left(- \frac{\sqrt{2} {m_d}}{{v}}\right) P_L + \left(\frac{\sqrt{2} {m_u}}{{v}}\right) P_R\right]`$ |
| $`\bar{e} e G^0`$ | $`i \left[\left(\frac{i {m_e}}{{v}}\right) P_L + \left(- \frac{i {m_e}}{{v}}\right) P_R\right]`$ |
| $`\bar{s} c G^-`$ | $`i \left[\left(- \frac{\sqrt{2} {m_s}}{{v}}\right) P_L + \left(\frac{\sqrt{2} {m_c}}{{v}}\right) P_R\right]`$ |
| $`\bar{s} s G^0`$ | $`i \left[\left(\frac{i {m_s}}{{v}}\right) P_L + \left(- \frac{i {m_s}}{{v}}\right) P_R\right]`$ |
| $`\bar{t} b G^+`$ | $`i \left[\left(\frac{\sqrt{2} {m_t}}{{v}}\right) P_L + \left(- \frac{\sqrt{2} {m_b}}{{v}}\right) P_R\right]`$ |
| $`\bar{t} t G^0`$ | $`i \left[\left(- \frac{i {m_t}}{{v}}\right) P_L + \left(\frac{i {m_t}}{{v}}\right) P_R\right]`$ |
| $`\bar{u} d G^+`$ | $`i \left[\left(\frac{\sqrt{2} {m_u}}{{v}}\right) P_L + \left(- \frac{\sqrt{2} {m_d}}{{v}}\right) P_R\right]`$ |
| $`\bar{u} u G^0`$ | $`i \left[\left(- \frac{i {m_u}}{{v}}\right) P_L + \left(\frac{i {m_u}}{{v}}\right) P_R\right]`$ |

39 further vertex keys involve fields with no Dirac particle (`eL`, `eLbar`, `eR`, `eRbar`, `nuL`, `nuLbar`, `nuR`, `nuRbar`) and are not in the table above; see the [card](../README.md) and `FEYNLAG_GAPS.md` (FG-3).

## Majorana neutrino vertices (numeric)

$`\nu_{1,2,3}`$ and $`N_{1,2}`$ are the light and heavy Majorana mass eigenstates ($`\chi_k`$ in the code), ordered by mass; $`\nu_1`$ is massless. The Takagi rotation is solved numerically at the benchmark, so these couplings have no closed form here; magnitudes are given instead, and the tests pin them against Atre et al. Eq. (2.5) (`tests/test_l2_literature.py`). Couplings below $`10^{-40}`$ vanish at the 50-digit working precision (for example $`Z\bar\nu_i\nu_j`$ with $`i \ne j`$) and are omitted.

| vertex | structure | $`\lvert\text{coupling}\rvert`$ at the benchmark |
|---|---|---|
| $`\bar{\nu_1} e W^+`$ | $`\gamma^\mu P_L`$ | 4.218e-01 |
| $`\bar{e} \nu_1 W^-`$ | $`\gamma^\mu P_L`$ | 4.218e-01 |
| $`\bar{\mu} \nu_2 W^-`$ | $`\gamma^\mu P_L`$ | 3.843e-01 |
| $`\bar{\nu_2} \mu W^+`$ | $`\gamma^\mu P_L`$ | 3.843e-01 |
| $`\bar{\nu_1} \nu_1 Z`$ | $`\gamma^\mu P_L`$ | 3.704e-01 |
| $`\bar{\nu_2} \nu_2 Z`$ | $`\gamma^\mu P_L`$ | 3.704e-01 |
| $`\bar{\nu_3} \nu_3 Z`$ | $`\gamma^\mu P_L`$ | 3.704e-01 |
| $`\bar{\nu_3} \tau W^+`$ | $`\gamma^\mu P_L`$ | 3.525e-01 |
| $`\bar{\tau} \nu_3 W^-`$ | $`\gamma^\mu P_L`$ | 3.525e-01 |
| $`\bar{\mu} \nu_3 W^-`$ | $`\gamma^\mu P_L`$ | 2.562e-01 |
| $`\bar{\nu_3} \mu W^+`$ | $`\gamma^\mu P_L`$ | 2.562e-01 |
| $`\bar{\nu_2} \tau W^+`$ | $`\gamma^\mu P_L`$ | 2.318e-01 |
| $`\bar{\tau} \nu_2 W^-`$ | $`\gamma^\mu P_L`$ | 2.318e-01 |
| $`\bar{\nu_1} \tau W^+`$ | $`\gamma^\mu P_L`$ | 1.882e-01 |
| $`\bar{\tau} \nu_1 W^-`$ | $`\gamma^\mu P_L`$ | 1.882e-01 |
| $`\bar{\nu_3} e W^+`$ | $`\gamma^\mu P_L`$ | 1.533e-01 |
| $`\bar{e} \nu_3 W^-`$ | $`\gamma^\mu P_L`$ | 1.533e-01 |
| $`\bar{\nu_2} e W^+`$ | $`\gamma^\mu P_L`$ | 1.093e-01 |
| $`\bar{e} \nu_2 W^-`$ | $`\gamma^\mu P_L`$ | 1.093e-01 |
| $`\bar{\nu_3} \tau G^+`$ | $`P_R`$ | 7.788e-03 |
| $`\bar{\tau} \nu_3 G^-`$ | $`P_L`$ | 7.788e-03 |
| $`\bar{\mu} \nu_1 W^-`$ | $`\gamma^\mu P_L`$ | 6.489e-03 |
| $`\bar{\nu_1} \mu W^+`$ | $`\gamma^\mu P_L`$ | 6.489e-03 |
| $`\bar{\nu_2} \tau G^+`$ | $`P_R`$ | 5.122e-03 |
| $`\bar{\tau} \nu_2 G^-`$ | $`P_L`$ | 5.122e-03 |
| $`\bar{\nu_1} \tau G^+`$ | $`P_R`$ | 4.158e-03 |
| $`\bar{\tau} \nu_1 G^-`$ | $`P_L`$ | 4.158e-03 |
| $`\bar{\mu} \nu_2 G^-`$ | $`P_L`$ | 5.049e-04 |
| $`\bar{\nu_2} \mu G^+`$ | $`P_R`$ | 5.049e-04 |
| $`\bar{\mu} \nu_3 G^-`$ | $`P_L`$ | 3.366e-04 |
| $`\bar{\nu_3} \mu G^+`$ | $`P_R`$ | 3.366e-04 |
| $`\bar{\mu} \nu_1 G^-`$ | $`P_L`$ | 8.526e-06 |
| $`\bar{\nu_1} \mu G^+`$ | $`P_R`$ | 8.526e-06 |
| $`\bar{\nu_1} e G^+`$ | $`P_R`$ | 2.680e-06 |
| $`\bar{e} \nu_1 G^-`$ | $`P_L`$ | 2.680e-06 |
| $`\bar{N_2} \tau G^+`$ | $`P_L`$ | 1.100e-06 |
| $`\bar{\tau} N_2 G^-`$ | $`P_R`$ | 1.100e-06 |
| $`\bar{\nu_3} e G^+`$ | $`P_R`$ | 9.742e-07 |
| $`\bar{e} \nu_3 G^-`$ | $`P_L`$ | 9.742e-07 |
| $`\bar{N_2} \nu_2 G^0`$ | $`P_L`$ | 8.270e-07 |
| $`\bar{N_2} \nu_2 h`$ | $`P_L`$ | 8.270e-07 |
| $`\bar{\nu_2} N_2 G^0`$ | $`P_R`$ | 8.270e-07 |
| $`\bar{\nu_2} N_2 h`$ | $`P_R`$ | 8.270e-07 |
| $`\bar{N_1} \mu G^+`$ | $`P_L`$ | 8.000e-07 |
| $`\bar{\mu} N_1 G^-`$ | $`P_R`$ | 8.000e-07 |
| $`\bar{N_1} \nu_3 G^0`$ | $`P_L`$ | 7.618e-07 |
| $`\bar{N_1} \nu_3 h`$ | $`P_L`$ | 7.618e-07 |
| $`\bar{\nu_3} N_1 G^0`$ | $`P_R`$ | 7.618e-07 |
| $`\bar{\nu_3} N_1 h`$ | $`P_R`$ | 7.618e-07 |
| $`\bar{N_1} \tau G^+`$ | $`P_L`$ | 7.000e-07 |
| $`\bar{\tau} N_1 G^-`$ | $`P_R`$ | 7.000e-07 |
| $`\bar{\nu_2} e G^+`$ | $`P_R`$ | 6.946e-07 |
| $`\bar{e} \nu_2 G^-`$ | $`P_L`$ | 6.946e-07 |
| $`\bar{N_2} \mu G^+`$ | $`P_L`$ | 6.000e-07 |
| $`\bar{\mu} N_2 G^-`$ | $`P_R`$ | 6.000e-07 |
| $`\bar{N_2} e G^+`$ | $`P_L`$ | 5.000e-07 |
| $`\bar{e} N_2 G^-`$ | $`P_R`$ | 5.000e-07 |
| $`\bar{N_2} \nu_3 G^0`$ | $`P_L`$ | 4.755e-07 |
| $`\bar{N_2} \nu_3 h`$ | $`P_L`$ | 4.755e-07 |
| $`\bar{\nu_3} N_2 G^0`$ | $`P_R`$ | 4.755e-07 |
| $`\bar{\nu_3} N_2 h`$ | $`P_R`$ | 4.755e-07 |
| $`\bar{N_1} e G^+`$ | $`P_L`$ | 3.000e-07 |
| $`\bar{e} N_1 G^-`$ | $`P_R`$ | 3.000e-07 |
| $`\bar{N_1} \nu_2 G^0`$ | $`P_L`$ | 1.721e-07 |
| $`\bar{N_1} \nu_2 h`$ | $`P_L`$ | 1.721e-07 |
| $`\bar{\nu_2} N_1 G^0`$ | $`P_R`$ | 1.721e-07 |
| $`\bar{\nu_2} N_1 h`$ | $`P_R`$ | 1.721e-07 |
| $`\bar{N_1} \nu_3 Z`$ | $`\gamma^\mu P_L`$ | 6.947e-08 |
| $`\bar{\nu_3} N_1 Z`$ | $`\gamma^\mu P_L`$ | 6.947e-08 |
| $`\bar{N_1} \mu W^+`$ | $`\gamma^\mu P_L`$ | 6.433e-08 |
| $`\bar{\mu} N_1 W^-`$ | $`\gamma^\mu P_L`$ | 6.433e-08 |
| $`\bar{N_1} \tau W^+`$ | $`\gamma^\mu P_L`$ | 5.629e-08 |
| $`\bar{\tau} N_1 W^-`$ | $`\gamma^\mu P_L`$ | 5.629e-08 |
| $`\bar{N_2} \tau W^+`$ | $`\gamma^\mu P_L`$ | 2.949e-08 |
| $`\bar{\tau} N_2 W^-`$ | $`\gamma^\mu P_L`$ | 2.949e-08 |
| $`\bar{N_2} \nu_2 Z`$ | $`\gamma^\mu P_L`$ | 2.514e-08 |
| $`\bar{\nu_2} N_2 Z`$ | $`\gamma^\mu P_L`$ | 2.514e-08 |
| $`\bar{N_1} e W^+`$ | $`\gamma^\mu P_L`$ | 2.413e-08 |
| $`\bar{e} N_1 W^-`$ | $`\gamma^\mu P_L`$ | 2.413e-08 |
| $`\bar{N_2} \mu W^+`$ | $`\gamma^\mu P_L`$ | 1.608e-08 |
| $`\bar{\mu} N_2 W^-`$ | $`\gamma^\mu P_L`$ | 1.608e-08 |
| $`\bar{N_1} \nu_2 Z`$ | $`\gamma^\mu P_L`$ | 1.569e-08 |
| $`\bar{\nu_2} N_1 Z`$ | $`\gamma^\mu P_L`$ | 1.569e-08 |
| $`\bar{N_2} \nu_3 Z`$ | $`\gamma^\mu P_L`$ | 1.445e-08 |
| $`\bar{\nu_3} N_2 Z`$ | $`\gamma^\mu P_L`$ | 1.445e-08 |
| $`\bar{N_2} e W^+`$ | $`\gamma^\mu P_L`$ | 1.340e-08 |
| $`\bar{e} N_2 W^-`$ | $`\gamma^\mu P_L`$ | 1.340e-08 |
| $`\bar{N_1} \tau G^+`$ | $`P_R`$ | 1.244e-09 |
| $`\bar{\tau} N_1 G^-`$ | $`P_L`$ | 1.244e-09 |
| $`\bar{N_2} \tau G^+`$ | $`P_R`$ | 6.516e-10 |
| $`\bar{\tau} N_2 G^-`$ | $`P_L`$ | 6.516e-10 |
| $`\bar{N_1} \mu G^+`$ | $`P_R`$ | 8.453e-11 |
| $`\bar{\mu} N_1 G^-`$ | $`P_L`$ | 8.453e-11 |
| $`\bar{N_2} \mu G^+`$ | $`P_R`$ | 2.113e-11 |
| $`\bar{\mu} N_2 G^-`$ | $`P_L`$ | 2.113e-11 |
| $`\bar{\nu_3} \tau G^+`$ | $`P_L`$ | 1.742e-13 |
| $`\bar{\tau} \nu_3 G^-`$ | $`P_R`$ | 1.742e-13 |
| $`\bar{\nu_3} \nu_3 G^0`$ | $`P_R`$ | 1.615e-13 |
| $`\bar{\nu_3} \nu_3 G^0`$ | $`P_L`$ | 1.615e-13 |
| $`\bar{\nu_3} \nu_3 h`$ | $`P_R`$ | 1.615e-13 |
| $`\bar{\nu_3} \nu_3 h`$ | $`P_L`$ | 1.615e-13 |
| $`\bar{N_1} e G^+`$ | $`P_R`$ | 1.533e-13 |
| $`\bar{e} N_1 G^-`$ | $`P_L`$ | 1.533e-13 |
| $`\bar{N_1} N_1 G^0`$ | $`P_R`$ | 1.502e-13 |
| $`\bar{N_1} N_1 G^0`$ | $`P_L`$ | 1.502e-13 |
| $`\bar{N_1} N_1 h`$ | $`P_R`$ | 1.502e-13 |
| $`\bar{N_1} N_1 h`$ | $`P_L`$ | 1.502e-13 |
| $`\bar{\mu} \nu_3 G^-`$ | $`P_R`$ | 1.266e-13 |
| $`\bar{\nu_3} \mu G^+`$ | $`P_L`$ | 1.266e-13 |
| $`\bar{N_2} e G^+`$ | $`P_R`$ | 8.517e-14 |
| $`\bar{e} N_2 G^-`$ | $`P_L`$ | 8.517e-14 |
| $`\bar{\nu_3} e G^+`$ | $`P_L`$ | 7.579e-14 |
| $`\bar{e} \nu_3 G^-`$ | $`P_R`$ | 7.579e-14 |
| $`\bar{N_2} N_2 G^0`$ | $`P_R`$ | 7.469e-14 |
| $`\bar{N_2} N_2 G^0`$ | $`P_L`$ | 7.469e-14 |
| $`\bar{N_2} N_2 h`$ | $`P_R`$ | 7.469e-14 |
| $`\bar{N_2} N_2 h`$ | $`P_L`$ | 7.469e-14 |
| $`\bar{\mu} \nu_2 G^-`$ | $`P_R`$ | 7.461e-14 |
| $`\bar{\nu_2} \mu G^+`$ | $`P_L`$ | 7.461e-14 |
| $`\bar{\nu_2} \nu_2 G^0`$ | $`P_R`$ | 6.342e-14 |
| $`\bar{\nu_2} \nu_2 G^0`$ | $`P_L`$ | 6.342e-14 |
| $`\bar{\nu_2} \nu_2 h`$ | $`P_R`$ | 6.342e-14 |
| $`\bar{\nu_2} \nu_2 h`$ | $`P_L`$ | 6.342e-14 |
| $`\bar{N_1} N_2 G^0`$ | $`P_R`$ | 5.417e-14 |
| $`\bar{N_1} N_2 h`$ | $`P_R`$ | 5.417e-14 |
| $`\bar{N_2} N_1 G^0`$ | $`P_L`$ | 5.417e-14 |
| $`\bar{N_2} N_1 h`$ | $`P_L`$ | 5.417e-14 |
| $`\bar{\nu_2} \tau G^+`$ | $`P_L`$ | 4.500e-14 |
| $`\bar{\tau} \nu_2 G^-`$ | $`P_R`$ | 4.500e-14 |
| $`\bar{\nu_2} e G^+`$ | $`P_L`$ | 2.123e-14 |
| $`\bar{e} \nu_2 G^-`$ | $`P_R`$ | 2.123e-14 |
| $`\bar{N_1} N_2 G^0`$ | $`P_L`$ | 1.806e-14 |
| $`\bar{N_1} N_2 h`$ | $`P_L`$ | 1.806e-14 |
| $`\bar{N_2} N_1 G^0`$ | $`P_R`$ | 1.806e-14 |
| $`\bar{N_2} N_1 h`$ | $`P_R`$ | 1.806e-14 |
| $`\bar{N_1} N_1 Z`$ | $`\gamma^\mu P_L`$ | 1.370e-14 |
| $`\bar{N_2} N_2 Z`$ | $`\gamma^\mu P_L`$ | 2.270e-15 |
| $`\bar{\nu_2} \nu_3 Z`$ | $`\gamma^\mu P_L`$ | 1.962e-15 |
| $`\bar{\nu_3} \nu_2 Z`$ | $`\gamma^\mu P_L`$ | 1.962e-15 |
| $`\bar{N_1} N_2 Z`$ | $`\gamma^\mu P_L`$ | 1.646e-15 |
| $`\bar{N_2} N_1 Z`$ | $`\gamma^\mu P_L`$ | 1.646e-15 |
| $`\bar{N_1} \nu_3 G^0`$ | $`P_R`$ | 3.029e-20 |
| $`\bar{N_1} \nu_3 h`$ | $`P_R`$ | 3.029e-20 |
| $`\bar{\nu_3} N_1 G^0`$ | $`P_L`$ | 3.029e-20 |
| $`\bar{\nu_3} N_1 h`$ | $`P_L`$ | 3.029e-20 |
| $`\bar{N_2} \nu_3 G^0`$ | $`P_R`$ | 6.302e-21 |
| $`\bar{N_2} \nu_3 h`$ | $`P_R`$ | 6.302e-21 |
| $`\bar{\nu_3} N_2 G^0`$ | $`P_L`$ | 6.302e-21 |
| $`\bar{\nu_3} N_2 h`$ | $`P_L`$ | 6.302e-21 |
| $`\bar{N_2} \nu_2 G^0`$ | $`P_R`$ | 4.304e-21 |
| $`\bar{N_2} \nu_2 h`$ | $`P_R`$ | 4.304e-21 |
| $`\bar{\nu_2} N_2 G^0`$ | $`P_L`$ | 4.304e-21 |
| $`\bar{\nu_2} N_2 h`$ | $`P_L`$ | 4.304e-21 |
| $`\bar{N_1} \nu_2 G^0`$ | $`P_R`$ | 2.687e-21 |
| $`\bar{N_1} \nu_2 h`$ | $`P_R`$ | 2.687e-21 |
| $`\bar{\nu_2} N_1 G^0`$ | $`P_L`$ | 2.687e-21 |
| $`\bar{\nu_2} N_1 h`$ | $`P_L`$ | 2.687e-21 |
| $`\bar{N_1} \nu_1 G^0`$ | $`P_L`$ | 2.259e-22 |
| $`\bar{N_1} \nu_1 h`$ | $`P_L`$ | 2.259e-22 |
| $`\bar{\nu_1} N_1 G^0`$ | $`P_R`$ | 2.259e-22 |
| $`\bar{\nu_1} N_1 h`$ | $`P_R`$ | 2.259e-22 |
| $`\bar{N_2} \nu_1 G^0`$ | $`P_L`$ | 7.892e-23 |
| $`\bar{N_2} \nu_1 h`$ | $`P_L`$ | 7.892e-23 |
| $`\bar{\nu_1} N_2 G^0`$ | $`P_R`$ | 7.892e-23 |
| $`\bar{\nu_1} N_2 h`$ | $`P_R`$ | 7.892e-23 |
| $`\bar{\nu_2} \nu_3 G^0`$ | $`P_R`$ | 8.460e-28 |
| $`\bar{\nu_2} \nu_3 h`$ | $`P_R`$ | 8.460e-28 |
| $`\bar{\nu_3} \nu_2 G^0`$ | $`P_L`$ | 8.460e-28 |
| $`\bar{\nu_3} \nu_2 h`$ | $`P_L`$ | 8.460e-28 |
| $`\bar{\nu_2} \nu_3 G^0`$ | $`P_L`$ | 3.211e-28 |
| $`\bar{\nu_2} \nu_3 h`$ | $`P_L`$ | 3.211e-28 |
| $`\bar{\nu_3} \nu_2 G^0`$ | $`P_R`$ | 3.211e-28 |
| $`\bar{\nu_3} \nu_2 h`$ | $`P_R`$ | 3.211e-28 |
| $`\bar{\nu_1} \nu_3 G^0`$ | $`P_R`$ | 3.930e-29 |
| $`\bar{\nu_1} \nu_3 h`$ | $`P_R`$ | 3.930e-29 |
| $`\bar{\nu_3} \nu_1 G^0`$ | $`P_L`$ | 3.930e-29 |
| $`\bar{\nu_3} \nu_1 h`$ | $`P_L`$ | 3.930e-29 |
| $`\bar{\nu_1} \nu_2 G^0`$ | $`P_R`$ | 1.493e-29 |
| $`\bar{\nu_1} \nu_2 h`$ | $`P_R`$ | 1.493e-29 |
| $`\bar{\nu_2} \nu_1 G^0`$ | $`P_L`$ | 1.493e-29 |
| $`\bar{\nu_2} \nu_1 h`$ | $`P_L`$ | 1.493e-29 |
