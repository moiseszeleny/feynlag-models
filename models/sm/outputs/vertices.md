# Feynman rules: Standard Model (one Higgs doublet, one full fermion generation)

Tree-level vertices of `sm` as feynlag derives them: 38 bosonic (potential and kinetic sectors) and the fermion couplings below.
This page re-renders the rules of [`vertices.tex`](vertices.tex) with physics names; it adds no verification. See the [card](../README.md) for what the tests pin against the literature, [`spectrum.md`](spectrum.md) for the masses and the [UFO](SM_UFO/) for the exported couplings.

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

## Fermion vertices: 21 in all

One boson leg each, as the UFO exports them: chiral keys merged into $`P_L`$/$`P_R`$ slots, redundant colour copies dropped, Yukawa couplings resolved to masses. Gluon couplings are not included (no colour-octet particle is declared).

### Fermion pair and a vector (FFV): 11 vertices

| interaction | Feynman rule |
|---|---|
| $`\bar{\nu}_\tau \nu_\tau Z`$ | $`i \gamma^\mu \left(\frac{\sqrt{{g'}^{2} + {g}^{2}}}{2}\right) P_L`$ |
| $`\bar{\nu}_\tau \tau W^+`$ | $`i \gamma^\mu \left(\frac{\sqrt{2} {g}}{2}\right) P_L`$ |
| $`\bar{\tau} \nu_\tau W^-`$ | $`i \gamma^\mu \left(\frac{\sqrt{2} {g}}{2}\right) P_L`$ |
| $`\bar{\tau} \tau Z`$ | $`i \gamma^\mu \left[\left(\frac{{g'}^{2} - {g}^{2}}{2 \sqrt{{g'}^{2} + {g}^{2}}}\right) P_L + \left(\frac{{g'}^{2}}{\sqrt{{g'}^{2} + {g}^{2}}}\right) P_R\right]`$ |
| $`\bar{\tau} \tau \gamma`$ | $`i \gamma^\mu \left(- \frac{{g'} {g}}{\sqrt{{g'}^{2} + {g}^{2}}}\right)`$ |
| $`\bar{b} b Z`$ | $`i \gamma^\mu \left[\left(\frac{- {g'}^{2} - 3 {g}^{2}}{6 \sqrt{{g'}^{2} + {g}^{2}}}\right) P_L + \left(\frac{{g'}^{2}}{3 \sqrt{{g'}^{2} + {g}^{2}}}\right) P_R\right]`$ |
| $`\bar{b} b \gamma`$ | $`i \gamma^\mu \left(- \frac{{g'} {g}}{3 \sqrt{{g'}^{2} + {g}^{2}}}\right)`$ |
| $`\bar{b} t W^-`$ | $`i \gamma^\mu \left(\frac{\sqrt{2} {g}}{2}\right) P_L`$ |
| $`\bar{t} b W^+`$ | $`i \gamma^\mu \left(\frac{\sqrt{2} {g}}{2}\right) P_L`$ |
| $`\bar{t} t Z`$ | $`i \gamma^\mu \left[\left(\frac{- {g'}^{2} + 3 {g}^{2}}{6 \sqrt{{g'}^{2} + {g}^{2}}}\right) P_L + \left(- \frac{2 {g'}^{2}}{3 \sqrt{{g'}^{2} + {g}^{2}}}\right) P_R\right]`$ |
| $`\bar{t} t \gamma`$ | $`i \gamma^\mu \left(\frac{2 {g'} {g}}{3 \sqrt{{g'}^{2} + {g}^{2}}}\right)`$ |

### Fermion pair and a scalar (FFS): 10 vertices

| interaction | Feynman rule |
|---|---|
| $`\bar{\nu}_\tau \tau G^+`$ | $`i \left(- \frac{\sqrt{2} {m_\tau}}{{v}}\right) P_R`$ |
| $`\bar{\tau} \nu_\tau G^-`$ | $`i \left(- \frac{\sqrt{2} {m_\tau}}{{v}}\right) P_L`$ |
| $`\bar{\tau} \tau G^0`$ | $`i \left[\left(\frac{i {m_\tau}}{{v}}\right) P_L + \left(- \frac{i {m_\tau}}{{v}}\right) P_R\right]`$ |
| $`\bar{\tau} \tau h`$ | $`i \left(- \frac{{m_\tau}}{{v}}\right)`$ |
| $`\bar{b} b G^0`$ | $`i \left[\left(\frac{i {m_b}}{{v}}\right) P_L + \left(- \frac{i {m_b}}{{v}}\right) P_R\right]`$ |
| $`\bar{b} b h`$ | $`i \left(- \frac{{m_b}}{{v}}\right)`$ |
| $`\bar{b} t G^-`$ | $`i \left[\left(- \frac{\sqrt{2} {m_b}}{{v}}\right) P_L + \left(\frac{\sqrt{2} {m_t}}{{v}}\right) P_R\right]`$ |
| $`\bar{t} b G^+`$ | $`i \left[\left(\frac{\sqrt{2} {m_t}}{{v}}\right) P_L + \left(- \frac{\sqrt{2} {m_b}}{{v}}\right) P_R\right]`$ |
| $`\bar{t} t G^0`$ | $`i \left[\left(- \frac{i {m_t}}{{v}}\right) P_L + \left(\frac{i {m_t}}{{v}}\right) P_R\right]`$ |
| $`\bar{t} t h`$ | $`i \left(- \frac{{m_t}}{{v}}\right)`$ |
