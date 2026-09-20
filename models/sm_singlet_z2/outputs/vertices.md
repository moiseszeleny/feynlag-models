# Feynman rules: SM + real singlet scalar (Z2-symmetric, spontaneously broken)

Tree-level vertices of `sm_singlet_z2` as feynlag derives them: 64 bosonic (potential and kinetic sectors) and the fermion couplings below.
This page re-renders the rules of [`vertices.tex`](vertices.tex) with physics names; it adds no verification. See the [card](../README.md) for what the tests pin against the literature, [`spectrum.md`](spectrum.md) for the masses and the [UFO](SM_SINGLET_Z2_UFO/) for the exported couplings.

Each rule is $`i \times (\text{monomial coefficient}) \times \prod_f (\text{multiplicity of } f)!`$, all momenta are incoming and $`\partial_\mu \to i\,p_\mu`$ ([`CONVENTIONS.md`](../../../CONVENTIONS.md)); $`p_X`$ is the momentum of leg $`X`$.

## Bosonic vertices: 64 in all

### Cubic scalar (SSS): 4 vertices

$`h_1 h_1 h_1`$

```math
3 i \left(- 2 {\lambda} {v} \cos^{3}{\left({\theta} \right)} - {\lambda_{HS}} {v} \sin^{2}{\left({\theta} \right)} \cos{\left({\theta} \right)} - {\lambda_{HS}} {v_S} \sin{\left({\theta} \right)} \cos^{2}{\left({\theta} \right)} - 2 {\lambda_S} {v_S} \sin^{3}{\left({\theta} \right)}\right)
```

$`h_1 h_1 h_2`$

```math
i \left(6 {\lambda} {v} \sin{\left({\theta} \right)} \cos^{2}{\left({\theta} \right)} - 3 {\lambda_{HS}} {v} \sin{\left({\theta} \right)} \cos^{2}{\left({\theta} \right)} + {\lambda_{HS}} {v} \sin{\left({\theta} \right)} - 3 {\lambda_{HS}} {v_S} \cos^{3}{\left({\theta} \right)} + 2 {\lambda_{HS}} {v_S} \cos{\left({\theta} \right)} + 6 {\lambda_S} {v_S} \cos^{3}{\left({\theta} \right)} - 6 {\lambda_S} {v_S} \cos{\left({\theta} \right)}\right)
```

$`h_1 h_2 h_2`$

```math
i \left(- 6 {\lambda} {v} \sin^{2}{\left({\theta} \right)} \cos{\left({\theta} \right)} + 3 {\lambda_{HS}} {v} \sin^{2}{\left({\theta} \right)} \cos{\left({\theta} \right)} - {\lambda_{HS}} {v} \cos{\left({\theta} \right)} - 3 {\lambda_{HS}} {v_S} \sin^{3}{\left({\theta} \right)} + 2 {\lambda_{HS}} {v_S} \sin{\left({\theta} \right)} + 6 {\lambda_S} {v_S} \sin^{3}{\left({\theta} \right)} - 6 {\lambda_S} {v_S} \sin{\left({\theta} \right)}\right)
```

$`h_2 h_2 h_2`$

```math
3 i \left(2 {\lambda} {v} \sin^{3}{\left({\theta} \right)} + {\lambda_{HS}} {v} \sin{\left({\theta} \right)} \cos^{2}{\left({\theta} \right)} - {\lambda_{HS}} {v_S} \sin^{2}{\left({\theta} \right)} \cos{\left({\theta} \right)} - 2 {\lambda_S} {v_S} \cos^{3}{\left({\theta} \right)}\right)
```

### Quartic scalar (SSSS): 5 vertices

$`h_1 h_1 h_1 h_1`$

```math
6 i \left(- {\lambda} \cos^{4}{\left({\theta} \right)} - \frac{{\lambda_{HS}} \left(1 - \cos{\left(4 {\theta} \right)}\right)}{8} - {\lambda_S} \sin^{4}{\left({\theta} \right)}\right)
```

$`h_1 h_1 h_1 h_2`$

```math
3 i \left(2 {\lambda} \cos^{2}{\left({\theta} \right)} - 2 {\lambda_{HS}} \cos^{2}{\left({\theta} \right)} + {\lambda_{HS}} + 2 {\lambda_S} \cos^{2}{\left({\theta} \right)} - 2 {\lambda_S}\right) \sin{\left({\theta} \right)} \cos{\left({\theta} \right)}
```

$`h_1 h_1 h_2 h_2`$

```math
i \left(- \frac{3 {\lambda} \left(1 - \cos{\left(4 {\theta} \right)}\right)}{4} + \frac{{\lambda_{HS}} \left(1 - \cos{\left(4 {\theta} \right)}\right)}{2} - {\lambda_{HS}} \sin^{4}{\left({\theta} \right)} - {\lambda_{HS}} \cos^{4}{\left({\theta} \right)} - \frac{3 {\lambda_S} \left(1 - \cos{\left(4 {\theta} \right)}\right)}{4}\right)
```

$`h_1 h_2 h_2 h_2`$

```math
3 i \left(2 {\lambda} \sin^{2}{\left({\theta} \right)} - 2 {\lambda_{HS}} \sin^{2}{\left({\theta} \right)} + {\lambda_{HS}} + 2 {\lambda_S} \sin^{2}{\left({\theta} \right)} - 2 {\lambda_S}\right) \sin{\left({\theta} \right)} \cos{\left({\theta} \right)}
```

$`h_2 h_2 h_2 h_2`$

```math
6 i \left(- {\lambda} \sin^{4}{\left({\theta} \right)} - \frac{{\lambda_{HS}} \left(1 - \cos{\left(4 {\theta} \right)}\right)}{8} - {\lambda_S} \cos^{4}{\left({\theta} \right)}\right)
```

### Two vectors and a scalar (VVS): 4 vertices

| interaction | Feynman rule |
|---|---|
| $`W^- W^+ h_1`$ | $`\frac{i {g}^{2} {v} \cos{\left({\theta} \right)}}{2}`$ |
| $`W^- W^+ h_2`$ | $`- \frac{i {g}^{2} {v} \sin{\left({\theta} \right)}}{2}`$ |
| $`Z Z h_1`$ | $`\frac{i {v} \left({g'}^{2} + {g}^{2}\right) \cos{\left({\theta} \right)}}{2}`$ |
| $`Z Z h_2`$ | $`\frac{i {v} \left(- {g'}^{2} - {g}^{2}\right) \sin{\left({\theta} \right)}}{2}`$ |

### Two vectors and two scalars (VVSS): 6 vertices

| interaction | Feynman rule |
|---|---|
| $`W^- W^+ h_1 h_1`$ | $`\frac{i {g}^{2} \cos^{2}{\left({\theta} \right)}}{2}`$ |
| $`W^- W^+ h_1 h_2`$ | $`- \frac{i {g}^{2} \sin{\left(2 {\theta} \right)}}{4}`$ |
| $`W^- W^+ h_2 h_2`$ | $`\frac{i {g}^{2} \sin^{2}{\left({\theta} \right)}}{2}`$ |
| $`Z Z h_1 h_1`$ | $`\frac{i \left({g'}^{2} + {g}^{2}\right) \cos^{2}{\left({\theta} \right)}}{2}`$ |
| $`Z Z h_1 h_2`$ | $`\frac{i \left(- {g'}^{2} - {g}^{2}\right) \sin{\left(2 {\theta} \right)}}{4}`$ |
| $`Z Z h_2 h_2`$ | $`\frac{i \left({g'}^{2} + {g}^{2}\right) \sin^{2}{\left({\theta} \right)}}{2}`$ |

### Feynman-gauge vertices with a Goldstone leg: 45 in all

The unitary-gauge UFO drops these; they matter for a Feynman-gauge calculation.

#### Cubic scalar (SSS): 4 vertices

| interaction | Feynman rule |
|---|---|
| $`G^- G^+ h_1`$ | $`- i \left(2 {\lambda} {v} \cos{\left({\theta} \right)} + {\lambda_{HS}} {v_S} \sin{\left({\theta} \right)}\right)`$ |
| $`G^- G^+ h_2`$ | $`i \left(2 {\lambda} {v} \sin{\left({\theta} \right)} - {\lambda_{HS}} {v_S} \cos{\left({\theta} \right)}\right)`$ |
| $`G^0 G^0 h_1`$ | $`- i \left(2 {\lambda} {v} \cos{\left({\theta} \right)} + {\lambda_{HS}} {v_S} \sin{\left({\theta} \right)}\right)`$ |
| $`G^0 G^0 h_2`$ | $`i \left(2 {\lambda} {v} \sin{\left({\theta} \right)} - {\lambda_{HS}} {v_S} \cos{\left({\theta} \right)}\right)`$ |

#### Quartic scalar (SSSS): 9 vertices

| interaction | Feynman rule |
|---|---|
| $`G^- G^- G^+ G^+`$ | $`- 4 i {\lambda}`$ |
| $`G^- G^+ G^0 G^0`$ | $`- 2 i {\lambda}`$ |
| $`G^- G^+ h_1 h_1`$ | $`i \left(- 2 {\lambda} \cos^{2}{\left({\theta} \right)} - {\lambda_{HS}} \sin^{2}{\left({\theta} \right)}\right)`$ |
| $`G^- G^+ h_1 h_2`$ | $`\frac{i \left(2 {\lambda} - {\lambda_{HS}}\right) \sin{\left(2 {\theta} \right)}}{2}`$ |
| $`G^- G^+ h_2 h_2`$ | $`i \left(- 2 {\lambda} \sin^{2}{\left({\theta} \right)} - {\lambda_{HS}} \cos^{2}{\left({\theta} \right)}\right)`$ |
| $`G^0 G^0 G^0 G^0`$ | $`- 6 i {\lambda}`$ |
| $`G^0 G^0 h_1 h_1`$ | $`i \left(- 2 {\lambda} \cos^{2}{\left({\theta} \right)} - {\lambda_{HS}} \sin^{2}{\left({\theta} \right)}\right)`$ |
| $`G^0 G^0 h_1 h_2`$ | $`\frac{i \left(2 {\lambda} - {\lambda_{HS}}\right) \sin{\left(2 {\theta} \right)}}{2}`$ |
| $`G^0 G^0 h_2 h_2`$ | $`i \left(- 2 {\lambda} \sin^{2}{\left({\theta} \right)} - {\lambda_{HS}} \cos^{2}{\left({\theta} \right)}\right)`$ |

#### Vector and two scalars (VSS): 10 vertices

| interaction | Feynman rule |
|---|---|
| $`\gamma G^- G^+`$ | $`\frac{i {g'} {g} \left({p_{G^-}} - {p_{G^+}}\right)}{\sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`Z G^- G^+`$ | $`\frac{i \left(- {g'}^{2} {p_{G^-}} + {g'}^{2} {p_{G^+}} + {g}^{2} {p_{G^-}} - {g}^{2} {p_{G^+}}\right)}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`W^+ G^- G^0`$ | $`\frac{{g} \left(- {p_{G^-}} + {p_{G^0}}\right)}{2}`$ |
| $`W^+ G^- h_1`$ | $`\frac{i {g} \left({p_{G^-}} - {p_{h_1}}\right) \cos{\left({\theta} \right)}}{2}`$ |
| $`W^+ G^- h_2`$ | $`\frac{i {g} \left(- {p_{G^-}} + {p_{h_2}}\right) \sin{\left({\theta} \right)}}{2}`$ |
| $`W^- G^+ G^0`$ | $`\frac{{g} \left(- {p_{G^+}} + {p_{G^0}}\right)}{2}`$ |
| $`W^- G^+ h_1`$ | $`\frac{i {g} \left(- {p_{G^+}} + {p_{h_1}}\right) \cos{\left({\theta} \right)}}{2}`$ |
| $`W^- G^+ h_2`$ | $`\frac{i {g} \left({p_{G^+}} - {p_{h_2}}\right) \sin{\left({\theta} \right)}}{2}`$ |

$`Z G^0 h_1`$

```math
\frac{\left(- {g'}^{2} {p_{G^0}} + {g'}^{2} {p_{h_1}} - {g}^{2} {p_{G^0}} + {g}^{2} {p_{h_1}}\right) \cos{\left({\theta} \right)}}{2 \sqrt{{g'}^{2} + {g}^{2}}}
```

$`Z G^0 h_2`$

```math
\frac{\left({g'}^{2} {p_{G^0}} - {g'}^{2} {p_{h_2}} + {g}^{2} {p_{G^0}} - {g}^{2} {p_{h_2}}\right) \sin{\left({\theta} \right)}}{2 \sqrt{{g'}^{2} + {g}^{2}}}
```

#### Two vectors and a scalar (VVS): 4 vertices

| interaction | Feynman rule |
|---|---|
| $`\gamma W^+ G^-`$ | $`\frac{i {g'} {g}^{2} {v}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`\gamma W^- G^+`$ | $`\frac{i {g'} {g}^{2} {v}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`W^+ Z G^-`$ | $`- \frac{i {g'}^{2} {g} {v}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`W^- Z G^+`$ | $`- \frac{i {g'}^{2} {g} {v}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |

#### Two vectors and two scalars (VVSS): 18 vertices

| interaction | Feynman rule |
|---|---|
| $`\gamma \gamma G^- G^+`$ | $`\frac{2 i {g'}^{2} {g}^{2}}{{g'}^{2} + {g}^{2}}`$ |
| $`\gamma Z G^- G^+`$ | $`\frac{i {g'} {g} \left(- {g'}^{2} + {g}^{2}\right)}{{g'}^{2} + {g}^{2}}`$ |
| $`\gamma W^+ G^- G^0`$ | $`- \frac{{g'} {g}^{2}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`\gamma W^+ G^- h_1`$ | $`\frac{i {g'} {g}^{2} \cos{\left({\theta} \right)}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`\gamma W^+ G^- h_2`$ | $`- \frac{i {g'} {g}^{2} \sin{\left({\theta} \right)}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`\gamma W^- G^+ G^0`$ | $`\frac{{g'} {g}^{2}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`\gamma W^- G^+ h_1`$ | $`\frac{i {g'} {g}^{2} \cos{\left({\theta} \right)}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`\gamma W^- G^+ h_2`$ | $`- \frac{i {g'} {g}^{2} \sin{\left({\theta} \right)}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`W^- W^+ G^- G^+`$ | $`\frac{i {g}^{2}}{2}`$ |
| $`Z Z G^- G^+`$ | $`\frac{i \left(\frac{{g'}^{4}}{2} - {g'}^{2} {g}^{2} + \frac{{g}^{4}}{2}\right)}{{g'}^{2} + {g}^{2}}`$ |
| $`W^+ Z G^- G^0`$ | $`\frac{{g'}^{2} {g}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`W^+ Z G^- h_1`$ | $`- \frac{i {g'}^{2} {g} \cos{\left({\theta} \right)}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`W^+ Z G^- h_2`$ | $`\frac{i {g'}^{2} {g} \sin{\left({\theta} \right)}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`W^- Z G^+ G^0`$ | $`- \frac{{g'}^{2} {g}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`W^- Z G^+ h_1`$ | $`- \frac{i {g'}^{2} {g} \cos{\left({\theta} \right)}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`W^- Z G^+ h_2`$ | $`\frac{i {g'}^{2} {g} \sin{\left({\theta} \right)}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`W^- W^+ G^0 G^0`$ | $`\frac{i {g}^{2}}{2}`$ |
| $`Z Z G^0 G^0`$ | $`\frac{i \left({g'}^{2} + {g}^{2}\right)}{2}`$ |

## Fermion vertices: 24 in all

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

### Fermion pair and a scalar (FFS): 13 vertices

| interaction | Feynman rule |
|---|---|
| $`\bar{\nu}_\tau \tau G^+`$ | $`i \left(- \frac{\sqrt{2} {m_\tau}}{{v}}\right) P_R`$ |
| $`\bar{\tau} \nu_\tau G^-`$ | $`i \left(- \frac{\sqrt{2} {m_\tau}}{{v}}\right) P_L`$ |
| $`\bar{\tau} \tau G^0`$ | $`i \left[\left(\frac{i {m_\tau}}{{v}}\right) P_L + \left(- \frac{i {m_\tau}}{{v}}\right) P_R\right]`$ |
| $`\bar{\tau} \tau h_1`$ | $`i \left(- \frac{{m_\tau} \cos{\left({\theta} \right)}}{{v}}\right)`$ |
| $`\bar{\tau} \tau h_2`$ | $`i \left(\frac{{m_\tau} \sin{\left({\theta} \right)}}{{v}}\right)`$ |
| $`\bar{b} b G^0`$ | $`i \left[\left(\frac{i {m_b}}{{v}}\right) P_L + \left(- \frac{i {m_b}}{{v}}\right) P_R\right]`$ |
| $`\bar{b} b h_1`$ | $`i \left(- \frac{{m_b} \cos{\left({\theta} \right)}}{{v}}\right)`$ |
| $`\bar{b} b h_2`$ | $`i \left(\frac{{m_b} \sin{\left({\theta} \right)}}{{v}}\right)`$ |
| $`\bar{b} t G^-`$ | $`i \left[\left(- \frac{\sqrt{2} {m_b}}{{v}}\right) P_L + \left(\frac{\sqrt{2} {m_t}}{{v}}\right) P_R\right]`$ |
| $`\bar{t} b G^+`$ | $`i \left[\left(\frac{\sqrt{2} {m_t}}{{v}}\right) P_L + \left(- \frac{\sqrt{2} {m_b}}{{v}}\right) P_R\right]`$ |
| $`\bar{t} t G^0`$ | $`i \left[\left(- \frac{i {m_t}}{{v}}\right) P_L + \left(\frac{i {m_t}}{{v}}\right) P_R\right]`$ |
| $`\bar{t} t h_1`$ | $`i \left(- \frac{{m_t} \cos{\left({\theta} \right)}}{{v}}\right)`$ |
| $`\bar{t} t h_2`$ | $`i \left(\frac{{m_t} \sin{\left({\theta} \right)}}{{v}}\right)`$ |
