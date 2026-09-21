# Feynman rules: Standard Model with three generations and CKM quark mixing

Tree-level vertices of `sm_ckm` as feynlag derives them: 38 bosonic (potential and kinetic sectors) and the fermion couplings below.
This page re-renders the rules of [`vertices.tex`](vertices.tex) with physics names; it adds no verification. See the [card](../README.md) for what the tests pin against the literature, [`spectrum.md`](spectrum.md) for the masses and the [UFO](SM_CKM_UFO/) for the exported couplings.

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

## Fermion vertices: 87 in all

One boson leg each, flattened as the UFO export flattens them: chiral keys merged into $`P_L`$/$`P_R`$ slots, redundant colour copies dropped, Yukawa couplings resolved to masses. Gluon couplings are not included (no colour-octet particle is declared). Unlike the export, which is in unitary gauge, the Goldstone vertices are kept here; they are in their own subsection below.

### Fermion pair and a vector (FFV): 45 vertices

| interaction | Feynman rule |
|---|---|
| $`\bar{\mu} \mu Z`$ | $`i \gamma^\mu \left[\left(\frac{{g'}^{2} - {g}^{2}}{2 \sqrt{{g'}^{2} + {g}^{2}}}\right) P_L + \left(\frac{{g'}^{2}}{\sqrt{{g'}^{2} + {g}^{2}}}\right) P_R\right]`$ |
| $`\bar{\mu} \mu \gamma`$ | $`i \gamma^\mu \left(- \frac{{g'} {g}}{\sqrt{{g'}^{2} + {g}^{2}}}\right)`$ |
| $`\bar{\mu} \nu_\mu W^-`$ | $`i \gamma^\mu \left(\frac{\sqrt{2} {g}}{2}\right) P_L`$ |
| $`\bar{\nu}_\mu \mu W^+`$ | $`i \gamma^\mu \left(\frac{\sqrt{2} {g}}{2}\right) P_L`$ |
| $`\bar{\nu}_\mu \nu_\mu Z`$ | $`i \gamma^\mu \left(\frac{\sqrt{{g'}^{2} + {g}^{2}}}{2}\right) P_L`$ |
| $`\bar{\nu}_\tau \nu_\tau Z`$ | $`i \gamma^\mu \left(\frac{\sqrt{{g'}^{2} + {g}^{2}}}{2}\right) P_L`$ |
| $`\bar{\nu}_\tau \tau W^+`$ | $`i \gamma^\mu \left(\frac{\sqrt{2} {g}}{2}\right) P_L`$ |
| $`\bar{\nu}_e \nu_e Z`$ | $`i \gamma^\mu \left(\frac{\sqrt{{g'}^{2} + {g}^{2}}}{2}\right) P_L`$ |
| $`\bar{\nu}_e e W^+`$ | $`i \gamma^\mu \left(\frac{\sqrt{2} {g}}{2}\right) P_L`$ |
| $`\bar{\tau} \nu_\tau W^-`$ | $`i \gamma^\mu \left(\frac{\sqrt{2} {g}}{2}\right) P_L`$ |
| $`\bar{\tau} \tau Z`$ | $`i \gamma^\mu \left[\left(\frac{{g'}^{2} - {g}^{2}}{2 \sqrt{{g'}^{2} + {g}^{2}}}\right) P_L + \left(\frac{{g'}^{2}}{\sqrt{{g'}^{2} + {g}^{2}}}\right) P_R\right]`$ |
| $`\bar{\tau} \tau \gamma`$ | $`i \gamma^\mu \left(- \frac{{g'} {g}}{\sqrt{{g'}^{2} + {g}^{2}}}\right)`$ |
| $`\bar{b} b Z`$ | $`i \gamma^\mu \left[\left(\frac{- {g'}^{2} - 3 {g}^{2}}{6 \sqrt{{g'}^{2} + {g}^{2}}}\right) P_L + \left(\frac{{g'}^{2}}{3 \sqrt{{g'}^{2} + {g}^{2}}}\right) P_R\right]`$ |
| $`\bar{b} b \gamma`$ | $`i \gamma^\mu \left(- \frac{{g'} {g}}{3 \sqrt{{g'}^{2} + {g}^{2}}}\right)`$ |
| $`\bar{b} c W^-`$ | $`i \gamma^\mu \left(\frac{\sqrt{2} {g} \sin{\left({\theta_{23}} \right)} \cos{\left({\theta_{13}} \right)}}{2}\right) P_L`$ |
| $`\bar{b} t W^-`$ | $`i \gamma^\mu \left(\frac{\sqrt{2} {g} \cos{\left({\theta_{13}} \right)} \cos{\left({\theta_{23}} \right)}}{2}\right) P_L`$ |
| $`\bar{b} u W^-`$ | $`i \gamma^\mu \left(\frac{\sqrt{2} {g} e^{i {\delta}} \sin{\left({\theta_{13}} \right)}}{2}\right) P_L`$ |
| $`\bar{c} b W^+`$ | $`i \gamma^\mu \left(\frac{\sqrt{2} {g} \sin{\left({\theta_{23}} \right)} \cos{\left({\theta_{13}} \right)}}{2}\right) P_L`$ |
| $`\bar{c} c Z`$ | $`i \gamma^\mu \left[\left(\frac{- {g'}^{2} + 3 {g}^{2}}{6 \sqrt{{g'}^{2} + {g}^{2}}}\right) P_L + \left(- \frac{2 {g'}^{2}}{3 \sqrt{{g'}^{2} + {g}^{2}}}\right) P_R\right]`$ |
| $`\bar{c} c \gamma`$ | $`i \gamma^\mu \left(\frac{2 {g'} {g}}{3 \sqrt{{g'}^{2} + {g}^{2}}}\right)`$ |
| $`\bar{d} d Z`$ | $`i \gamma^\mu \left[\left(\frac{- {g'}^{2} - 3 {g}^{2}}{6 \sqrt{{g'}^{2} + {g}^{2}}}\right) P_L + \left(\frac{{g'}^{2}}{3 \sqrt{{g'}^{2} + {g}^{2}}}\right) P_R\right]`$ |
| $`\bar{d} d \gamma`$ | $`i \gamma^\mu \left(- \frac{{g'} {g}}{3 \sqrt{{g'}^{2} + {g}^{2}}}\right)`$ |
| $`\bar{d} u W^-`$ | $`i \gamma^\mu \left(\frac{\sqrt{2} {g} \cos{\left({\theta_{12}} \right)} \cos{\left({\theta_{13}} \right)}}{2}\right) P_L`$ |
| $`\bar{e} \nu_e W^-`$ | $`i \gamma^\mu \left(\frac{\sqrt{2} {g}}{2}\right) P_L`$ |
| $`\bar{e} e Z`$ | $`i \gamma^\mu \left[\left(\frac{{g'}^{2} - {g}^{2}}{2 \sqrt{{g'}^{2} + {g}^{2}}}\right) P_L + \left(\frac{{g'}^{2}}{\sqrt{{g'}^{2} + {g}^{2}}}\right) P_R\right]`$ |
| $`\bar{e} e \gamma`$ | $`i \gamma^\mu \left(- \frac{{g'} {g}}{\sqrt{{g'}^{2} + {g}^{2}}}\right)`$ |
| $`\bar{s} s Z`$ | $`i \gamma^\mu \left[\left(\frac{- {g'}^{2} - 3 {g}^{2}}{6 \sqrt{{g'}^{2} + {g}^{2}}}\right) P_L + \left(\frac{{g'}^{2}}{3 \sqrt{{g'}^{2} + {g}^{2}}}\right) P_R\right]`$ |
| $`\bar{s} s \gamma`$ | $`i \gamma^\mu \left(- \frac{{g'} {g}}{3 \sqrt{{g'}^{2} + {g}^{2}}}\right)`$ |
| $`\bar{s} u W^-`$ | $`i \gamma^\mu \left(\frac{\sqrt{2} {g} \sin{\left({\theta_{12}} \right)} \cos{\left({\theta_{13}} \right)}}{2}\right) P_L`$ |
| $`\bar{t} b W^+`$ | $`i \gamma^\mu \left(\frac{\sqrt{2} {g} \cos{\left({\theta_{13}} \right)} \cos{\left({\theta_{23}} \right)}}{2}\right) P_L`$ |
| $`\bar{t} t Z`$ | $`i \gamma^\mu \left[\left(\frac{- {g'}^{2} + 3 {g}^{2}}{6 \sqrt{{g'}^{2} + {g}^{2}}}\right) P_L + \left(- \frac{2 {g'}^{2}}{3 \sqrt{{g'}^{2} + {g}^{2}}}\right) P_R\right]`$ |
| $`\bar{t} t \gamma`$ | $`i \gamma^\mu \left(\frac{2 {g'} {g}}{3 \sqrt{{g'}^{2} + {g}^{2}}}\right)`$ |
| $`\bar{u} b W^+`$ | $`i \gamma^\mu \left(\frac{\sqrt{2} {g} e^{- i {\delta}} \sin{\left({\theta_{13}} \right)}}{2}\right) P_L`$ |
| $`\bar{u} d W^+`$ | $`i \gamma^\mu \left(\frac{\sqrt{2} {g} \cos{\left({\theta_{12}} \right)} \cos{\left({\theta_{13}} \right)}}{2}\right) P_L`$ |
| $`\bar{u} s W^+`$ | $`i \gamma^\mu \left(\frac{\sqrt{2} {g} \sin{\left({\theta_{12}} \right)} \cos{\left({\theta_{13}} \right)}}{2}\right) P_L`$ |
| $`\bar{u} u Z`$ | $`i \gamma^\mu \left[\left(\frac{- {g'}^{2} + 3 {g}^{2}}{6 \sqrt{{g'}^{2} + {g}^{2}}}\right) P_L + \left(- \frac{2 {g'}^{2}}{3 \sqrt{{g'}^{2} + {g}^{2}}}\right) P_R\right]`$ |
| $`\bar{u} u \gamma`$ | $`i \gamma^\mu \left(\frac{2 {g'} {g}}{3 \sqrt{{g'}^{2} + {g}^{2}}}\right)`$ |

$`\bar{c} d W^+`$

```math
i \gamma^\mu \left(- \frac{\sqrt{2} {g} \left(e^{i {\delta}} \sin{\left({\theta_{13}} \right)} \sin{\left({\theta_{23}} \right)} \cos{\left({\theta_{12}} \right)} + \sin{\left({\theta_{12}} \right)} \cos{\left({\theta_{23}} \right)}\right)}{2}\right) P_L
```

$`\bar{c} s W^+`$

```math
i \gamma^\mu \left(\frac{\sqrt{2} {g} \left(- e^{i {\delta}} \sin{\left({\theta_{12}} \right)} \sin{\left({\theta_{13}} \right)} \sin{\left({\theta_{23}} \right)} + \cos{\left({\theta_{12}} \right)} \cos{\left({\theta_{23}} \right)}\right)}{2}\right) P_L
```

$`\bar{d} c W^-`$

```math
i \gamma^\mu \left(- \frac{\sqrt{2} {g} \left(e^{i {\delta}} \sin{\left({\theta_{12}} \right)} \cos{\left({\theta_{23}} \right)} + \sin{\left({\theta_{13}} \right)} \sin{\left({\theta_{23}} \right)} \cos{\left({\theta_{12}} \right)}\right) e^{- i {\delta}}}{2}\right) P_L
```

$`\bar{d} t W^-`$

```math
i \gamma^\mu \left(\frac{\sqrt{2} {g} \left(e^{i {\delta}} \sin{\left({\theta_{12}} \right)} \sin{\left({\theta_{23}} \right)} - \sin{\left({\theta_{13}} \right)} \cos{\left({\theta_{12}} \right)} \cos{\left({\theta_{23}} \right)}\right) e^{- i {\delta}}}{2}\right) P_L
```

$`\bar{s} c W^-`$

```math
i \gamma^\mu \left(\frac{\sqrt{2} {g} \left(e^{i {\delta}} \cos{\left({\theta_{12}} \right)} \cos{\left({\theta_{23}} \right)} - \sin{\left({\theta_{12}} \right)} \sin{\left({\theta_{13}} \right)} \sin{\left({\theta_{23}} \right)}\right) e^{- i {\delta}}}{2}\right) P_L
```

$`\bar{s} t W^-`$

```math
i \gamma^\mu \left(- \frac{\sqrt{2} {g} \left(e^{i {\delta}} \sin{\left({\theta_{23}} \right)} \cos{\left({\theta_{12}} \right)} + \sin{\left({\theta_{12}} \right)} \sin{\left({\theta_{13}} \right)} \cos{\left({\theta_{23}} \right)}\right) e^{- i {\delta}}}{2}\right) P_L
```

$`\bar{t} d W^+`$

```math
i \gamma^\mu \left(\frac{\sqrt{2} {g} \left(- e^{i {\delta}} \sin{\left({\theta_{13}} \right)} \cos{\left({\theta_{12}} \right)} \cos{\left({\theta_{23}} \right)} + \sin{\left({\theta_{12}} \right)} \sin{\left({\theta_{23}} \right)}\right)}{2}\right) P_L
```

$`\bar{t} s W^+`$

```math
i \gamma^\mu \left(- \frac{\sqrt{2} {g} \left(e^{i {\delta}} \sin{\left({\theta_{12}} \right)} \sin{\left({\theta_{13}} \right)} \cos{\left({\theta_{23}} \right)} + \sin{\left({\theta_{23}} \right)} \cos{\left({\theta_{12}} \right)}\right)}{2}\right) P_L
```

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

### Fermion pairs with a Goldstone leg (Feynman gauge): 33 vertices

Absent from the unitary-gauge UFO, which drops every Goldstone leg.

#### Fermion pair and a scalar (FFS): 33 vertices

| interaction | Feynman rule |
|---|---|
| $`\bar{\mu} \mu G^0`$ | $`i \left[\left(\frac{i {m_\mu}}{{v}}\right) P_L + \left(- \frac{i {m_\mu}}{{v}}\right) P_R\right]`$ |
| $`\bar{\mu} \nu_\mu G^-`$ | $`i \left(- \frac{\sqrt{2} {m_\mu}}{{v}}\right) P_L`$ |
| $`\bar{\nu}_\mu \mu G^+`$ | $`i \left(- \frac{\sqrt{2} {m_\mu}}{{v}}\right) P_R`$ |
| $`\bar{\nu}_\tau \tau G^+`$ | $`i \left(- \frac{\sqrt{2} {m_\tau}}{{v}}\right) P_R`$ |
| $`\bar{\nu}_e e G^+`$ | $`i \left(- \frac{\sqrt{2} {m_e}}{{v}}\right) P_R`$ |
| $`\bar{\tau} \nu_\tau G^-`$ | $`i \left(- \frac{\sqrt{2} {m_\tau}}{{v}}\right) P_L`$ |
| $`\bar{\tau} \tau G^0`$ | $`i \left[\left(\frac{i {m_\tau}}{{v}}\right) P_L + \left(- \frac{i {m_\tau}}{{v}}\right) P_R\right]`$ |
| $`\bar{b} b G^0`$ | $`i \left[\left(\frac{i {m_b}}{{v}}\right) P_L + \left(- \frac{i {m_b}}{{v}}\right) P_R\right]`$ |
| $`\bar{b} u G^-`$ | $`i \left[\left(- \frac{\sqrt{2} {m_b} e^{i {\delta}} \sin{\left({\theta_{13}} \right)}}{{v}}\right) P_L + \left(\frac{\sqrt{2} {m_u} e^{i {\delta}} \sin{\left({\theta_{13}} \right)}}{{v}}\right) P_R\right]`$ |
| $`\bar{c} c G^0`$ | $`i \left[\left(- \frac{i {m_c}}{{v}}\right) P_L + \left(\frac{i {m_c}}{{v}}\right) P_R\right]`$ |
| $`\bar{d} d G^0`$ | $`i \left[\left(\frac{i {m_d}}{{v}}\right) P_L + \left(- \frac{i {m_d}}{{v}}\right) P_R\right]`$ |
| $`\bar{e} \nu_e G^-`$ | $`i \left(- \frac{\sqrt{2} {m_e}}{{v}}\right) P_L`$ |
| $`\bar{e} e G^0`$ | $`i \left[\left(\frac{i {m_e}}{{v}}\right) P_L + \left(- \frac{i {m_e}}{{v}}\right) P_R\right]`$ |
| $`\bar{s} s G^0`$ | $`i \left[\left(\frac{i {m_s}}{{v}}\right) P_L + \left(- \frac{i {m_s}}{{v}}\right) P_R\right]`$ |
| $`\bar{t} t G^0`$ | $`i \left[\left(- \frac{i {m_t}}{{v}}\right) P_L + \left(\frac{i {m_t}}{{v}}\right) P_R\right]`$ |
| $`\bar{u} b G^+`$ | $`i \left[\left(\frac{\sqrt{2} {m_u} e^{- i {\delta}} \sin{\left({\theta_{13}} \right)}}{{v}}\right) P_L + \left(- \frac{\sqrt{2} {m_b} e^{- i {\delta}} \sin{\left({\theta_{13}} \right)}}{{v}}\right) P_R\right]`$ |
| $`\bar{u} u G^0`$ | $`i \left[\left(- \frac{i {m_u}}{{v}}\right) P_L + \left(\frac{i {m_u}}{{v}}\right) P_R\right]`$ |

$`\bar{b} c G^-`$

```math
i \left[\left(- \frac{\sqrt{2} {m_b} \sin{\left({\theta_{23}} \right)} \cos{\left({\theta_{13}} \right)}}{{v}}\right) P_L + \left(\frac{\sqrt{2} {m_c} \sin{\left({\theta_{23}} \right)} \cos{\left({\theta_{13}} \right)}}{{v}}\right) P_R\right]
```

$`\bar{b} t G^-`$

```math
i \left[\left(- \frac{\sqrt{2} {m_b} \cos{\left({\theta_{13}} \right)} \cos{\left({\theta_{23}} \right)}}{{v}}\right) P_L + \left(\frac{\sqrt{2} {m_t} \cos{\left({\theta_{13}} \right)} \cos{\left({\theta_{23}} \right)}}{{v}}\right) P_R\right]
```

$`\bar{c} b G^+`$

```math
i \left[\left(\frac{\sqrt{2} {m_c} \sin{\left({\theta_{23}} \right)} \cos{\left({\theta_{13}} \right)}}{{v}}\right) P_L + \left(- \frac{\sqrt{2} {m_b} \sin{\left({\theta_{23}} \right)} \cos{\left({\theta_{13}} \right)}}{{v}}\right) P_R\right]
```

$`\bar{c} d G^+`$

```math
i \left[\left(- \frac{\sqrt{2} {m_c} \left(e^{i {\delta}} \sin{\left({\theta_{13}} \right)} \sin{\left({\theta_{23}} \right)} \cos{\left({\theta_{12}} \right)} + \sin{\left({\theta_{12}} \right)} \cos{\left({\theta_{23}} \right)}\right)}{{v}}\right) P_L + \left(\frac{\sqrt{2} {m_d} \left(e^{i {\delta}} \sin{\left({\theta_{13}} \right)} \sin{\left({\theta_{23}} \right)} \cos{\left({\theta_{12}} \right)} + \sin{\left({\theta_{12}} \right)} \cos{\left({\theta_{23}} \right)}\right)}{{v}}\right) P_R\right]
```

$`\bar{c} s G^+`$

```math
i \left[\left(\frac{\sqrt{2} {m_c} \left(- e^{i {\delta}} \sin{\left({\theta_{12}} \right)} \sin{\left({\theta_{13}} \right)} \sin{\left({\theta_{23}} \right)} + \cos{\left({\theta_{12}} \right)} \cos{\left({\theta_{23}} \right)}\right)}{{v}}\right) P_L + \left(\frac{\sqrt{2} {m_s} \left(e^{i {\delta}} \sin{\left({\theta_{12}} \right)} \sin{\left({\theta_{13}} \right)} \sin{\left({\theta_{23}} \right)} - \cos{\left({\theta_{12}} \right)} \cos{\left({\theta_{23}} \right)}\right)}{{v}}\right) P_R\right]
```

$`\bar{d} c G^-`$

```math
i \left[\left(\frac{\sqrt{2} {m_d} \left(e^{i {\delta}} \sin{\left({\theta_{12}} \right)} \cos{\left({\theta_{23}} \right)} + \sin{\left({\theta_{13}} \right)} \sin{\left({\theta_{23}} \right)} \cos{\left({\theta_{12}} \right)}\right) e^{- i {\delta}}}{{v}}\right) P_L + \left(- \frac{\sqrt{2} {m_c} \left(e^{i {\delta}} \sin{\left({\theta_{12}} \right)} \cos{\left({\theta_{23}} \right)} + \sin{\left({\theta_{13}} \right)} \sin{\left({\theta_{23}} \right)} \cos{\left({\theta_{12}} \right)}\right) e^{- i {\delta}}}{{v}}\right) P_R\right]
```

$`\bar{d} t G^-`$

```math
i \left[\left(\frac{\sqrt{2} {m_d} \left(- e^{i {\delta}} \sin{\left({\theta_{12}} \right)} \sin{\left({\theta_{23}} \right)} + \sin{\left({\theta_{13}} \right)} \cos{\left({\theta_{12}} \right)} \cos{\left({\theta_{23}} \right)}\right) e^{- i {\delta}}}{{v}}\right) P_L + \left(\frac{\sqrt{2} {m_t} \left(e^{i {\delta}} \sin{\left({\theta_{12}} \right)} \sin{\left({\theta_{23}} \right)} - \sin{\left({\theta_{13}} \right)} \cos{\left({\theta_{12}} \right)} \cos{\left({\theta_{23}} \right)}\right) e^{- i {\delta}}}{{v}}\right) P_R\right]
```

$`\bar{d} u G^-`$

```math
i \left[\left(- \frac{\sqrt{2} {m_d} \cos{\left({\theta_{12}} \right)} \cos{\left({\theta_{13}} \right)}}{{v}}\right) P_L + \left(\frac{\sqrt{2} {m_u} \cos{\left({\theta_{12}} \right)} \cos{\left({\theta_{13}} \right)}}{{v}}\right) P_R\right]
```

$`\bar{s} c G^-`$

```math
i \left[\left(\frac{\sqrt{2} {m_s} \left(- e^{i {\delta}} \cos{\left({\theta_{12}} \right)} \cos{\left({\theta_{23}} \right)} + \sin{\left({\theta_{12}} \right)} \sin{\left({\theta_{13}} \right)} \sin{\left({\theta_{23}} \right)}\right) e^{- i {\delta}}}{{v}}\right) P_L + \left(\frac{\sqrt{2} {m_c} \left(e^{i {\delta}} \cos{\left({\theta_{12}} \right)} \cos{\left({\theta_{23}} \right)} - \sin{\left({\theta_{12}} \right)} \sin{\left({\theta_{13}} \right)} \sin{\left({\theta_{23}} \right)}\right) e^{- i {\delta}}}{{v}}\right) P_R\right]
```

$`\bar{s} t G^-`$

```math
i \left[\left(\frac{\sqrt{2} {m_s} \left(e^{i {\delta}} \sin{\left({\theta_{23}} \right)} \cos{\left({\theta_{12}} \right)} + \sin{\left({\theta_{12}} \right)} \sin{\left({\theta_{13}} \right)} \cos{\left({\theta_{23}} \right)}\right) e^{- i {\delta}}}{{v}}\right) P_L + \left(- \frac{\sqrt{2} {m_t} \left(e^{i {\delta}} \sin{\left({\theta_{23}} \right)} \cos{\left({\theta_{12}} \right)} + \sin{\left({\theta_{12}} \right)} \sin{\left({\theta_{13}} \right)} \cos{\left({\theta_{23}} \right)}\right) e^{- i {\delta}}}{{v}}\right) P_R\right]
```

$`\bar{s} u G^-`$

```math
i \left[\left(- \frac{\sqrt{2} {m_s} \sin{\left({\theta_{12}} \right)} \cos{\left({\theta_{13}} \right)}}{{v}}\right) P_L + \left(\frac{\sqrt{2} {m_u} \sin{\left({\theta_{12}} \right)} \cos{\left({\theta_{13}} \right)}}{{v}}\right) P_R\right]
```

$`\bar{t} b G^+`$

```math
i \left[\left(\frac{\sqrt{2} {m_t} \cos{\left({\theta_{13}} \right)} \cos{\left({\theta_{23}} \right)}}{{v}}\right) P_L + \left(- \frac{\sqrt{2} {m_b} \cos{\left({\theta_{13}} \right)} \cos{\left({\theta_{23}} \right)}}{{v}}\right) P_R\right]
```

$`\bar{t} d G^+`$

```math
i \left[\left(\frac{\sqrt{2} {m_t} \left(- e^{i {\delta}} \sin{\left({\theta_{13}} \right)} \cos{\left({\theta_{12}} \right)} \cos{\left({\theta_{23}} \right)} + \sin{\left({\theta_{12}} \right)} \sin{\left({\theta_{23}} \right)}\right)}{{v}}\right) P_L + \left(\frac{\sqrt{2} {m_d} \left(e^{i {\delta}} \sin{\left({\theta_{13}} \right)} \cos{\left({\theta_{12}} \right)} \cos{\left({\theta_{23}} \right)} - \sin{\left({\theta_{12}} \right)} \sin{\left({\theta_{23}} \right)}\right)}{{v}}\right) P_R\right]
```

$`\bar{t} s G^+`$

```math
i \left[\left(- \frac{\sqrt{2} {m_t} \left(e^{i {\delta}} \sin{\left({\theta_{12}} \right)} \sin{\left({\theta_{13}} \right)} \cos{\left({\theta_{23}} \right)} + \sin{\left({\theta_{23}} \right)} \cos{\left({\theta_{12}} \right)}\right)}{{v}}\right) P_L + \left(\frac{\sqrt{2} {m_s} \left(e^{i {\delta}} \sin{\left({\theta_{12}} \right)} \sin{\left({\theta_{13}} \right)} \cos{\left({\theta_{23}} \right)} + \sin{\left({\theta_{23}} \right)} \cos{\left({\theta_{12}} \right)}\right)}{{v}}\right) P_R\right]
```

$`\bar{u} d G^+`$

```math
i \left[\left(\frac{\sqrt{2} {m_u} \cos{\left({\theta_{12}} \right)} \cos{\left({\theta_{13}} \right)}}{{v}}\right) P_L + \left(- \frac{\sqrt{2} {m_d} \cos{\left({\theta_{12}} \right)} \cos{\left({\theta_{13}} \right)}}{{v}}\right) P_R\right]
```

$`\bar{u} s G^+`$

```math
i \left[\left(\frac{\sqrt{2} {m_u} \sin{\left({\theta_{12}} \right)} \cos{\left({\theta_{13}} \right)}}{{v}}\right) P_L + \left(- \frac{\sqrt{2} {m_s} \sin{\left({\theta_{12}} \right)} \cos{\left({\theta_{13}} \right)}}{{v}}\right) P_R\right]
```
