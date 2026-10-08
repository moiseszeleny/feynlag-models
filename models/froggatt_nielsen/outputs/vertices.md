# Feynman rules: SM + Froggatt-Nielsen flavon (global U(1)_FN, three generations)

Tree-level vertices of `froggatt_nielsen` as feynlag derives them: 72 bosonic (potential and kinetic sectors) and the fermion couplings below.
This page re-renders the rules of [`vertices.tex`](vertices.tex) with physics names; it adds no verification. See the [card](../README.md) for what the tests pin against the literature, [`spectrum.md`](spectrum.md) for the masses.

Each rule is $`i \times (\text{monomial coefficient}) \times \prod_f (\text{multiplicity of } f)!`$, all momenta are incoming and $`\partial_\mu \to i\,p_\mu`$ ([`CONVENTIONS.md`](../../../CONVENTIONS.md)); $`p_X`$ is the momentum of leg $`X`$.

## Bosonic vertices: 72 in all

### Cubic scalar (SSS): 6 vertices

| interaction | Feynman rule |
|---|---|
| $`h_1 a a`$ | $`- i \left({\lambda_{H\phi}} {v} \cos{\left({\theta} \right)} + 2 {\lambda_\phi} {v_\phi} \sin{\left({\theta} \right)}\right)`$ |
| $`h_2 a a`$ | $`i \left({\lambda_{H\phi}} {v} \sin{\left({\theta} \right)} - 2 {\lambda_\phi} {v_\phi} \cos{\left({\theta} \right)}\right)`$ |

$`h_1 h_1 h_1`$

```math
3 i \left(- 2 {\lambda} {v} \cos^{3}{\left({\theta} \right)} - {\lambda_{H\phi}} {v} \sin^{2}{\left({\theta} \right)} \cos{\left({\theta} \right)} - {\lambda_{H\phi}} {v_\phi} \sin{\left({\theta} \right)} \cos^{2}{\left({\theta} \right)} - 2 {\lambda_\phi} {v_\phi} \sin^{3}{\left({\theta} \right)}\right)
```

$`h_1 h_1 h_2`$

```math
i \left(6 {\lambda} {v} \sin{\left({\theta} \right)} \cos^{2}{\left({\theta} \right)} - 3 {\lambda_{H\phi}} {v} \sin{\left({\theta} \right)} \cos^{2}{\left({\theta} \right)} + {\lambda_{H\phi}} {v} \sin{\left({\theta} \right)} - 3 {\lambda_{H\phi}} {v_\phi} \cos^{3}{\left({\theta} \right)} + 2 {\lambda_{H\phi}} {v_\phi} \cos{\left({\theta} \right)} + 6 {\lambda_\phi} {v_\phi} \cos^{3}{\left({\theta} \right)} - 6 {\lambda_\phi} {v_\phi} \cos{\left({\theta} \right)}\right)
```

$`h_1 h_2 h_2`$

```math
i \left(- 6 {\lambda} {v} \sin^{2}{\left({\theta} \right)} \cos{\left({\theta} \right)} + 3 {\lambda_{H\phi}} {v} \sin^{2}{\left({\theta} \right)} \cos{\left({\theta} \right)} - {\lambda_{H\phi}} {v} \cos{\left({\theta} \right)} - 3 {\lambda_{H\phi}} {v_\phi} \sin^{3}{\left({\theta} \right)} + 2 {\lambda_{H\phi}} {v_\phi} \sin{\left({\theta} \right)} + 6 {\lambda_\phi} {v_\phi} \sin^{3}{\left({\theta} \right)} - 6 {\lambda_\phi} {v_\phi} \sin{\left({\theta} \right)}\right)
```

$`h_2 h_2 h_2`$

```math
3 i \left(2 {\lambda} {v} \sin^{3}{\left({\theta} \right)} + {\lambda_{H\phi}} {v} \sin{\left({\theta} \right)} \cos^{2}{\left({\theta} \right)} - {\lambda_{H\phi}} {v_\phi} \sin^{2}{\left({\theta} \right)} \cos{\left({\theta} \right)} - 2 {\lambda_\phi} {v_\phi} \cos^{3}{\left({\theta} \right)}\right)
```

### Quartic scalar (SSSS): 9 vertices

| interaction | Feynman rule |
|---|---|
| $`h_1 h_1 a a`$ | $`i \left(- {\lambda_{H\phi}} \cos^{2}{\left({\theta} \right)} - 2 {\lambda_\phi} \sin^{2}{\left({\theta} \right)}\right)`$ |
| $`h_1 h_2 a a`$ | $`\frac{i \left({\lambda_{H\phi}} - 2 {\lambda_\phi}\right) \sin{\left(2 {\theta} \right)}}{2}`$ |
| $`h_2 h_2 a a`$ | $`i \left(- {\lambda_{H\phi}} \sin^{2}{\left({\theta} \right)} - 2 {\lambda_\phi} \cos^{2}{\left({\theta} \right)}\right)`$ |
| $`a a a a`$ | $`- 6 i {\lambda_\phi}`$ |

$`h_1 h_1 h_1 h_1`$

```math
6 i \left(- {\lambda} \cos^{4}{\left({\theta} \right)} - \frac{{\lambda_{H\phi}} \left(1 - \cos{\left(4 {\theta} \right)}\right)}{8} - {\lambda_\phi} \sin^{4}{\left({\theta} \right)}\right)
```

$`h_1 h_1 h_1 h_2`$

```math
3 i \left(2 {\lambda} \cos^{2}{\left({\theta} \right)} - 2 {\lambda_{H\phi}} \cos^{2}{\left({\theta} \right)} + {\lambda_{H\phi}} + 2 {\lambda_\phi} \cos^{2}{\left({\theta} \right)} - 2 {\lambda_\phi}\right) \sin{\left({\theta} \right)} \cos{\left({\theta} \right)}
```

$`h_1 h_1 h_2 h_2`$

```math
i \left(- \frac{3 {\lambda} \left(1 - \cos{\left(4 {\theta} \right)}\right)}{4} + \frac{{\lambda_{H\phi}} \left(1 - \cos{\left(4 {\theta} \right)}\right)}{2} - {\lambda_{H\phi}} \sin^{4}{\left({\theta} \right)} - {\lambda_{H\phi}} \cos^{4}{\left({\theta} \right)} - \frac{3 {\lambda_\phi} \left(1 - \cos{\left(4 {\theta} \right)}\right)}{4}\right)
```

$`h_1 h_2 h_2 h_2`$

```math
3 i \left(2 {\lambda} \sin^{2}{\left({\theta} \right)} - 2 {\lambda_{H\phi}} \sin^{2}{\left({\theta} \right)} + {\lambda_{H\phi}} + 2 {\lambda_\phi} \sin^{2}{\left({\theta} \right)} - 2 {\lambda_\phi}\right) \sin{\left({\theta} \right)} \cos{\left({\theta} \right)}
```

$`h_2 h_2 h_2 h_2`$

```math
6 i \left(- {\lambda} \sin^{4}{\left({\theta} \right)} - \frac{{\lambda_{H\phi}} \left(1 - \cos{\left(4 {\theta} \right)}\right)}{8} - {\lambda_\phi} \cos^{4}{\left({\theta} \right)}\right)
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

### Feynman-gauge vertices with a Goldstone leg: 47 in all

The unitary-gauge UFO drops these; they matter for a Feynman-gauge calculation.

#### Cubic scalar (SSS): 4 vertices

| interaction | Feynman rule |
|---|---|
| $`G^- G^+ h_1`$ | $`- i \left(2 {\lambda} {v} \cos{\left({\theta} \right)} + {\lambda_{H\phi}} {v_\phi} \sin{\left({\theta} \right)}\right)`$ |
| $`G^- G^+ h_2`$ | $`i \left(2 {\lambda} {v} \sin{\left({\theta} \right)} - {\lambda_{H\phi}} {v_\phi} \cos{\left({\theta} \right)}\right)`$ |
| $`G^0 G^0 h_1`$ | $`- i \left(2 {\lambda} {v} \cos{\left({\theta} \right)} + {\lambda_{H\phi}} {v_\phi} \sin{\left({\theta} \right)}\right)`$ |
| $`G^0 G^0 h_2`$ | $`i \left(2 {\lambda} {v} \sin{\left({\theta} \right)} - {\lambda_{H\phi}} {v_\phi} \cos{\left({\theta} \right)}\right)`$ |

#### Quartic scalar (SSSS): 11 vertices

| interaction | Feynman rule |
|---|---|
| $`G^- G^- G^+ G^+`$ | $`- 4 i {\lambda}`$ |
| $`G^- G^+ G^0 G^0`$ | $`- 2 i {\lambda}`$ |
| $`G^- G^+ h_1 h_1`$ | $`i \left(- 2 {\lambda} \cos^{2}{\left({\theta} \right)} - {\lambda_{H\phi}} \sin^{2}{\left({\theta} \right)}\right)`$ |
| $`G^- G^+ h_1 h_2`$ | $`\frac{i \left(2 {\lambda} - {\lambda_{H\phi}}\right) \sin{\left(2 {\theta} \right)}}{2}`$ |
| $`G^- G^+ h_2 h_2`$ | $`i \left(- 2 {\lambda} \sin^{2}{\left({\theta} \right)} - {\lambda_{H\phi}} \cos^{2}{\left({\theta} \right)}\right)`$ |
| $`G^- G^+ a a`$ | $`- i {\lambda_{H\phi}}`$ |
| $`G^0 G^0 G^0 G^0`$ | $`- 6 i {\lambda}`$ |
| $`G^0 G^0 h_1 h_1`$ | $`i \left(- 2 {\lambda} \cos^{2}{\left({\theta} \right)} - {\lambda_{H\phi}} \sin^{2}{\left({\theta} \right)}\right)`$ |
| $`G^0 G^0 h_1 h_2`$ | $`\frac{i \left(2 {\lambda} - {\lambda_{H\phi}}\right) \sin{\left(2 {\theta} \right)}}{2}`$ |
| $`G^0 G^0 h_2 h_2`$ | $`i \left(- 2 {\lambda} \sin^{2}{\left({\theta} \right)} - {\lambda_{H\phi}} \cos^{2}{\left({\theta} \right)}\right)`$ |
| $`G^0 G^0 a a`$ | $`- i {\lambda_{H\phi}}`$ |

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

## Fermion vertices: 176 in all

One boson leg each, flattened as the UFO export flattens them: chiral keys merged into $`P_L`$/$`P_R`$ slots, redundant colour copies dropped, Yukawa couplings resolved to masses. Gluon couplings are not included (no colour-octet particle is declared). Unlike the export, which is in unitary gauge, the Goldstone vertices are kept here; they are in their own subsection below.

### Fermion pair and a vector (FFV): 33 vertices

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
| $`\bar{b} t W^-`$ | $`i \gamma^\mu \left(\frac{\sqrt{2} {g}}{2}\right) P_L`$ |
| $`\bar{c} c Z`$ | $`i \gamma^\mu \left[\left(\frac{- {g'}^{2} + 3 {g}^{2}}{6 \sqrt{{g'}^{2} + {g}^{2}}}\right) P_L + \left(- \frac{2 {g'}^{2}}{3 \sqrt{{g'}^{2} + {g}^{2}}}\right) P_R\right]`$ |
| $`\bar{c} c \gamma`$ | $`i \gamma^\mu \left(\frac{2 {g'} {g}}{3 \sqrt{{g'}^{2} + {g}^{2}}}\right)`$ |
| $`\bar{c} s W^+`$ | $`i \gamma^\mu \left(\frac{\sqrt{2} {g}}{2}\right) P_L`$ |
| $`\bar{d} d Z`$ | $`i \gamma^\mu \left[\left(\frac{- {g'}^{2} - 3 {g}^{2}}{6 \sqrt{{g'}^{2} + {g}^{2}}}\right) P_L + \left(\frac{{g'}^{2}}{3 \sqrt{{g'}^{2} + {g}^{2}}}\right) P_R\right]`$ |
| $`\bar{d} d \gamma`$ | $`i \gamma^\mu \left(- \frac{{g'} {g}}{3 \sqrt{{g'}^{2} + {g}^{2}}}\right)`$ |
| $`\bar{d} u W^-`$ | $`i \gamma^\mu \left(\frac{\sqrt{2} {g}}{2}\right) P_L`$ |
| $`\bar{e} \nu_e W^-`$ | $`i \gamma^\mu \left(\frac{\sqrt{2} {g}}{2}\right) P_L`$ |
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

### Fermion pair and a scalar (FFS): 80 vertices

$`\bar{\mu} \mu a`$

```math
i \left[\left(\frac{\sqrt{2} i {\lvert c^e_{22}\rvert} {v} {v_\phi}^{3} e^{- i {\alpha^e_{22}}}}{2 {\Lambda}^{4}}\right) P_L + \left(- \frac{\sqrt{2} i {\lvert c^e_{22}\rvert} {v} {v_\phi}^{3} e^{i {\alpha^e_{22}}}}{2 {\Lambda}^{4}}\right) P_R\right]
```

$`\bar{\mu} \mu h_1`$

```math
i \left[\left(- \frac{\sqrt{2} {\lvert c^e_{22}\rvert} {v_\phi}^{3} \left(4 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{- i {\alpha^e_{22}}}}{8 {\Lambda}^{4}}\right) P_L + \left(- \frac{\sqrt{2} {\lvert c^e_{22}\rvert} {v_\phi}^{3} \left(4 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{i {\alpha^e_{22}}}}{8 {\Lambda}^{4}}\right) P_R\right]
```

$`\bar{\mu} \mu h_2`$

```math
i \left[\left(\frac{\sqrt{2} {\lvert c^e_{22}\rvert} {v_\phi}^{3} \left(- 4 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{- i {\alpha^e_{22}}}}{8 {\Lambda}^{4}}\right) P_L + \left(\frac{\sqrt{2} {\lvert c^e_{22}\rvert} {v_\phi}^{3} \left(- 4 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{i {\alpha^e_{22}}}}{8 {\Lambda}^{4}}\right) P_R\right]
```

$`\bar{\mu} \tau a`$

```math
i \left[\left(\frac{\sqrt{2} i {\lvert c^e_{32}\rvert} {v} {v_\phi} e^{- i {\alpha^e_{32}}}}{2 {\Lambda}^{2}}\right) P_L + \left(- \frac{\sqrt{2} i {\lvert c^e_{23}\rvert} {v} {v_\phi}^{3} e^{i {\alpha^e_{23}}}}{2 {\Lambda}^{4}}\right) P_R\right]
```

$`\bar{\mu} \tau h_1`$

```math
i \left[\left(- \frac{\sqrt{2} {\lvert c^e_{32}\rvert} {v_\phi} \left(2 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{- i {\alpha^e_{32}}}}{4 {\Lambda}^{2}}\right) P_L + \left(- \frac{\sqrt{2} {\lvert c^e_{23}\rvert} {v_\phi}^{3} \left(4 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{i {\alpha^e_{23}}}}{8 {\Lambda}^{4}}\right) P_R\right]
```

$`\bar{\mu} \tau h_2`$

```math
i \left[\left(\frac{\sqrt{2} {\lvert c^e_{32}\rvert} {v_\phi} \left(- 2 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{- i {\alpha^e_{32}}}}{4 {\Lambda}^{2}}\right) P_L + \left(\frac{\sqrt{2} {\lvert c^e_{23}\rvert} {v_\phi}^{3} \left(- 4 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{i {\alpha^e_{23}}}}{8 {\Lambda}^{4}}\right) P_R\right]
```

$`\bar{\mu} e a`$

```math
i \left[\left(\frac{5 i {\lvert c^e_{12}\rvert} {v} {v_\phi}^{4} e^{- i {\alpha^e_{12}}}}{8 {\Lambda}^{5}}\right) P_L + \left(- \frac{5 i {\lvert c^e_{21}\rvert} {v} {v_\phi}^{4} e^{i {\alpha^e_{21}}}}{8 {\Lambda}^{5}}\right) P_R\right]
```

$`\bar{\mu} e h_1`$

```math
i \left[\left(- \frac{{\lvert c^e_{12}\rvert} {v_\phi}^{4} \left(5 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{- i {\alpha^e_{12}}}}{8 {\Lambda}^{5}}\right) P_L + \left(- \frac{{\lvert c^e_{21}\rvert} {v_\phi}^{4} \left(5 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{i {\alpha^e_{21}}}}{8 {\Lambda}^{5}}\right) P_R\right]
```

$`\bar{\mu} e h_2`$

```math
i \left[\left(\frac{{\lvert c^e_{12}\rvert} {v_\phi}^{4} \left(- 5 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{- i {\alpha^e_{12}}}}{8 {\Lambda}^{5}}\right) P_L + \left(\frac{{\lvert c^e_{21}\rvert} {v_\phi}^{4} \left(- 5 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{i {\alpha^e_{21}}}}{8 {\Lambda}^{5}}\right) P_R\right]
```

$`\bar{\tau} \mu a`$

```math
i \left[\left(\frac{\sqrt{2} i {\lvert c^e_{23}\rvert} {v} {v_\phi}^{3} e^{- i {\alpha^e_{23}}}}{2 {\Lambda}^{4}}\right) P_L + \left(- \frac{\sqrt{2} i {\lvert c^e_{32}\rvert} {v} {v_\phi} e^{i {\alpha^e_{32}}}}{2 {\Lambda}^{2}}\right) P_R\right]
```

$`\bar{\tau} \mu h_1`$

```math
i \left[\left(- \frac{\sqrt{2} {\lvert c^e_{23}\rvert} {v_\phi}^{3} \left(4 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{- i {\alpha^e_{23}}}}{8 {\Lambda}^{4}}\right) P_L + \left(- \frac{\sqrt{2} {\lvert c^e_{32}\rvert} {v_\phi} \left(2 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{i {\alpha^e_{32}}}}{4 {\Lambda}^{2}}\right) P_R\right]
```

$`\bar{\tau} \mu h_2`$

```math
i \left[\left(\frac{\sqrt{2} {\lvert c^e_{23}\rvert} {v_\phi}^{3} \left(- 4 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{- i {\alpha^e_{23}}}}{8 {\Lambda}^{4}}\right) P_L + \left(\frac{\sqrt{2} {\lvert c^e_{32}\rvert} {v_\phi} \left(- 2 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{i {\alpha^e_{32}}}}{4 {\Lambda}^{2}}\right) P_R\right]
```

$`\bar{\tau} \tau a`$

```math
i \left[\left(\frac{\sqrt{2} i {\lvert c^e_{33}\rvert} {v} {v_\phi} e^{- i {\alpha^e_{33}}}}{2 {\Lambda}^{2}}\right) P_L + \left(- \frac{\sqrt{2} i {\lvert c^e_{33}\rvert} {v} {v_\phi} e^{i {\alpha^e_{33}}}}{2 {\Lambda}^{2}}\right) P_R\right]
```

$`\bar{\tau} \tau h_1`$

```math
i \left[\left(- \frac{\sqrt{2} {\lvert c^e_{33}\rvert} {v_\phi} \left(2 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{- i {\alpha^e_{33}}}}{4 {\Lambda}^{2}}\right) P_L + \left(- \frac{\sqrt{2} {\lvert c^e_{33}\rvert} {v_\phi} \left(2 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{i {\alpha^e_{33}}}}{4 {\Lambda}^{2}}\right) P_R\right]
```

$`\bar{\tau} \tau h_2`$

```math
i \left[\left(\frac{\sqrt{2} {\lvert c^e_{33}\rvert} {v_\phi} \left(- 2 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{- i {\alpha^e_{33}}}}{4 {\Lambda}^{2}}\right) P_L + \left(\frac{\sqrt{2} {\lvert c^e_{33}\rvert} {v_\phi} \left(- 2 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{i {\alpha^e_{33}}}}{4 {\Lambda}^{2}}\right) P_R\right]
```

$`\bar{\tau} e a`$

```math
i \left[\left(\frac{5 i {\lvert c^e_{13}\rvert} {v} {v_\phi}^{4} e^{- i {\alpha^e_{13}}}}{8 {\Lambda}^{5}}\right) P_L + \left(- \frac{3 i {\lvert c^e_{31}\rvert} {v} {v_\phi}^{2} e^{i {\alpha^e_{31}}}}{4 {\Lambda}^{3}}\right) P_R\right]
```

$`\bar{\tau} e h_1`$

```math
i \left[\left(- \frac{{\lvert c^e_{13}\rvert} {v_\phi}^{4} \left(5 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{- i {\alpha^e_{13}}}}{8 {\Lambda}^{5}}\right) P_L + \left(- \frac{{\lvert c^e_{31}\rvert} {v_\phi}^{2} \left(3 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{i {\alpha^e_{31}}}}{4 {\Lambda}^{3}}\right) P_R\right]
```

$`\bar{\tau} e h_2`$

```math
i \left[\left(\frac{{\lvert c^e_{13}\rvert} {v_\phi}^{4} \left(- 5 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{- i {\alpha^e_{13}}}}{8 {\Lambda}^{5}}\right) P_L + \left(\frac{{\lvert c^e_{31}\rvert} {v_\phi}^{2} \left(- 3 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{i {\alpha^e_{31}}}}{4 {\Lambda}^{3}}\right) P_R\right]
```

$`\bar{b} b a`$

```math
i \left[\left(\frac{\sqrt{2} i {\lvert c^d_{33}\rvert} {v} {v_\phi} e^{- i {\alpha^d_{33}}}}{2 {\Lambda}^{2}}\right) P_L + \left(- \frac{\sqrt{2} i {\lvert c^d_{33}\rvert} {v} {v_\phi} e^{i {\alpha^d_{33}}}}{2 {\Lambda}^{2}}\right) P_R\right]
```

$`\bar{b} b h_1`$

```math
i \left[\left(- \frac{\sqrt{2} {\lvert c^d_{33}\rvert} {v_\phi} \left(2 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{- i {\alpha^d_{33}}}}{4 {\Lambda}^{2}}\right) P_L + \left(- \frac{\sqrt{2} {\lvert c^d_{33}\rvert} {v_\phi} \left(2 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{i {\alpha^d_{33}}}}{4 {\Lambda}^{2}}\right) P_R\right]
```

$`\bar{b} b h_2`$

```math
i \left[\left(\frac{\sqrt{2} {\lvert c^d_{33}\rvert} {v_\phi} \left(- 2 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{- i {\alpha^d_{33}}}}{4 {\Lambda}^{2}}\right) P_L + \left(\frac{\sqrt{2} {\lvert c^d_{33}\rvert} {v_\phi} \left(- 2 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{i {\alpha^d_{33}}}}{4 {\Lambda}^{2}}\right) P_R\right]
```

$`\bar{b} d a`$

```math
i \left[\left(\frac{5 i {\lvert c^d_{13}\rvert} {v} {v_\phi}^{4} e^{- i {\alpha^d_{13}}}}{8 {\Lambda}^{5}}\right) P_L + \left(- \frac{3 i {\lvert c^d_{31}\rvert} {v} {v_\phi}^{2} e^{i {\alpha^d_{31}}}}{4 {\Lambda}^{3}}\right) P_R\right]
```

$`\bar{b} d h_1`$

```math
i \left[\left(- \frac{{\lvert c^d_{13}\rvert} {v_\phi}^{4} \left(5 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{- i {\alpha^d_{13}}}}{8 {\Lambda}^{5}}\right) P_L + \left(- \frac{{\lvert c^d_{31}\rvert} {v_\phi}^{2} \left(3 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{i {\alpha^d_{31}}}}{4 {\Lambda}^{3}}\right) P_R\right]
```

$`\bar{b} d h_2`$

```math
i \left[\left(\frac{{\lvert c^d_{13}\rvert} {v_\phi}^{4} \left(- 5 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{- i {\alpha^d_{13}}}}{8 {\Lambda}^{5}}\right) P_L + \left(\frac{{\lvert c^d_{31}\rvert} {v_\phi}^{2} \left(- 3 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{i {\alpha^d_{31}}}}{4 {\Lambda}^{3}}\right) P_R\right]
```

$`\bar{b} s a`$

```math
i \left[\left(\frac{\sqrt{2} i {\lvert c^d_{23}\rvert} {v} {v_\phi}^{3} e^{- i {\alpha^d_{23}}}}{2 {\Lambda}^{4}}\right) P_L + \left(- \frac{\sqrt{2} i {\lvert c^d_{32}\rvert} {v} {v_\phi} e^{i {\alpha^d_{32}}}}{2 {\Lambda}^{2}}\right) P_R\right]
```

$`\bar{b} s h_1`$

```math
i \left[\left(- \frac{\sqrt{2} {\lvert c^d_{23}\rvert} {v_\phi}^{3} \left(4 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{- i {\alpha^d_{23}}}}{8 {\Lambda}^{4}}\right) P_L + \left(- \frac{\sqrt{2} {\lvert c^d_{32}\rvert} {v_\phi} \left(2 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{i {\alpha^d_{32}}}}{4 {\Lambda}^{2}}\right) P_R\right]
```

$`\bar{b} s h_2`$

```math
i \left[\left(\frac{\sqrt{2} {\lvert c^d_{23}\rvert} {v_\phi}^{3} \left(- 4 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{- i {\alpha^d_{23}}}}{8 {\Lambda}^{4}}\right) P_L + \left(\frac{\sqrt{2} {\lvert c^d_{32}\rvert} {v_\phi} \left(- 2 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{i {\alpha^d_{32}}}}{4 {\Lambda}^{2}}\right) P_R\right]
```

$`\bar{c} c a`$

```math
i \left[\left(\frac{3 i {\lvert c^u_{22}\rvert} {v} {v_\phi}^{2} e^{- i {\alpha^u_{22}}}}{4 {\Lambda}^{3}}\right) P_L + \left(- \frac{3 i {\lvert c^u_{22}\rvert} {v} {v_\phi}^{2} e^{i {\alpha^u_{22}}}}{4 {\Lambda}^{3}}\right) P_R\right]
```

$`\bar{c} c h_1`$

```math
i \left[\left(- \frac{{\lvert c^u_{22}\rvert} {v_\phi}^{2} \left(3 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{- i {\alpha^u_{22}}}}{4 {\Lambda}^{3}}\right) P_L + \left(- \frac{{\lvert c^u_{22}\rvert} {v_\phi}^{2} \left(3 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{i {\alpha^u_{22}}}}{4 {\Lambda}^{3}}\right) P_R\right]
```

$`\bar{c} c h_2`$

```math
i \left[\left(\frac{{\lvert c^u_{22}\rvert} {v_\phi}^{2} \left(- 3 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{- i {\alpha^u_{22}}}}{4 {\Lambda}^{3}}\right) P_L + \left(\frac{{\lvert c^u_{22}\rvert} {v_\phi}^{2} \left(- 3 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{i {\alpha^u_{22}}}}{4 {\Lambda}^{3}}\right) P_R\right]
```

$`\bar{c} t a`$

```math
i \left[\left(\frac{i {\lvert c^u_{32}\rvert} {v} e^{- i {\alpha^u_{32}}}}{2 {\Lambda}}\right) P_L + \left(- \frac{\sqrt{2} i {\lvert c^u_{23}\rvert} {v} {v_\phi} e^{i {\alpha^u_{23}}}}{2 {\Lambda}^{2}}\right) P_R\right]
```

$`\bar{c} t h_1`$

```math
i \left[\left(- \frac{{\lvert c^u_{32}\rvert} \left({v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{- i {\alpha^u_{32}}}}{2 {\Lambda}}\right) P_L + \left(- \frac{\sqrt{2} {\lvert c^u_{23}\rvert} {v_\phi} \left(2 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{i {\alpha^u_{23}}}}{4 {\Lambda}^{2}}\right) P_R\right]
```

$`\bar{c} t h_2`$

```math
i \left[\left(\frac{{\lvert c^u_{32}\rvert} \left(- {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{- i {\alpha^u_{32}}}}{2 {\Lambda}}\right) P_L + \left(\frac{\sqrt{2} {\lvert c^u_{23}\rvert} {v_\phi} \left(- 2 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{i {\alpha^u_{23}}}}{4 {\Lambda}^{2}}\right) P_R\right]
```

$`\bar{c} u a`$

```math
i \left[\left(\frac{\sqrt{2} i {\lvert c^u_{12}\rvert} {v} {v_\phi}^{3} e^{- i {\alpha^u_{12}}}}{2 {\Lambda}^{4}}\right) P_L + \left(- \frac{5 i {\lvert c^u_{21}\rvert} {v} {v_\phi}^{4} e^{i {\alpha^u_{21}}}}{8 {\Lambda}^{5}}\right) P_R\right]
```

$`\bar{c} u h_1`$

```math
i \left[\left(- \frac{\sqrt{2} {\lvert c^u_{12}\rvert} {v_\phi}^{3} \left(4 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{- i {\alpha^u_{12}}}}{8 {\Lambda}^{4}}\right) P_L + \left(- \frac{{\lvert c^u_{21}\rvert} {v_\phi}^{4} \left(5 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{i {\alpha^u_{21}}}}{8 {\Lambda}^{5}}\right) P_R\right]
```

$`\bar{c} u h_2`$

```math
i \left[\left(\frac{\sqrt{2} {\lvert c^u_{12}\rvert} {v_\phi}^{3} \left(- 4 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{- i {\alpha^u_{12}}}}{8 {\Lambda}^{4}}\right) P_L + \left(\frac{{\lvert c^u_{21}\rvert} {v_\phi}^{4} \left(- 5 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{i {\alpha^u_{21}}}}{8 {\Lambda}^{5}}\right) P_R\right]
```

$`\bar{d} b a`$

```math
i \left[\left(\frac{3 i {\lvert c^d_{31}\rvert} {v} {v_\phi}^{2} e^{- i {\alpha^d_{31}}}}{4 {\Lambda}^{3}}\right) P_L + \left(- \frac{5 i {\lvert c^d_{13}\rvert} {v} {v_\phi}^{4} e^{i {\alpha^d_{13}}}}{8 {\Lambda}^{5}}\right) P_R\right]
```

$`\bar{d} b h_1`$

```math
i \left[\left(- \frac{{\lvert c^d_{31}\rvert} {v_\phi}^{2} \left(3 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{- i {\alpha^d_{31}}}}{4 {\Lambda}^{3}}\right) P_L + \left(- \frac{{\lvert c^d_{13}\rvert} {v_\phi}^{4} \left(5 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{i {\alpha^d_{13}}}}{8 {\Lambda}^{5}}\right) P_R\right]
```

$`\bar{d} b h_2`$

```math
i \left[\left(\frac{{\lvert c^d_{31}\rvert} {v_\phi}^{2} \left(- 3 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{- i {\alpha^d_{31}}}}{4 {\Lambda}^{3}}\right) P_L + \left(\frac{{\lvert c^d_{13}\rvert} {v_\phi}^{4} \left(- 5 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{i {\alpha^d_{13}}}}{8 {\Lambda}^{5}}\right) P_R\right]
```

$`\bar{d} d a`$

```math
i \left[\left(\frac{3 \sqrt{2} i {\lvert c^d_{11}\rvert} {v} {v_\phi}^{5} e^{- i {\alpha^d_{11}}}}{8 {\Lambda}^{6}}\right) P_L + \left(- \frac{3 \sqrt{2} i {\lvert c^d_{11}\rvert} {v} {v_\phi}^{5} e^{i {\alpha^d_{11}}}}{8 {\Lambda}^{6}}\right) P_R\right]
```

$`\bar{d} d h_1`$

```math
i \left[\left(- \frac{\sqrt{2} {\lvert c^d_{11}\rvert} {v_\phi}^{5} \left(6 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{- i {\alpha^d_{11}}}}{16 {\Lambda}^{6}}\right) P_L + \left(- \frac{\sqrt{2} {\lvert c^d_{11}\rvert} {v_\phi}^{5} \left(6 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{i {\alpha^d_{11}}}}{16 {\Lambda}^{6}}\right) P_R\right]
```

$`\bar{d} d h_2`$

```math
i \left[\left(\frac{\sqrt{2} {\lvert c^d_{11}\rvert} {v_\phi}^{5} \left(- 6 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{- i {\alpha^d_{11}}}}{16 {\Lambda}^{6}}\right) P_L + \left(\frac{\sqrt{2} {\lvert c^d_{11}\rvert} {v_\phi}^{5} \left(- 6 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{i {\alpha^d_{11}}}}{16 {\Lambda}^{6}}\right) P_R\right]
```

$`\bar{d} s a`$

```math
i \left[\left(\frac{5 i {\lvert c^d_{21}\rvert} {v} {v_\phi}^{4} e^{- i {\alpha^d_{21}}}}{8 {\Lambda}^{5}}\right) P_L + \left(- \frac{5 i {\lvert c^d_{12}\rvert} {v} {v_\phi}^{4} e^{i {\alpha^d_{12}}}}{8 {\Lambda}^{5}}\right) P_R\right]
```

$`\bar{d} s h_1`$

```math
i \left[\left(- \frac{{\lvert c^d_{21}\rvert} {v_\phi}^{4} \left(5 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{- i {\alpha^d_{21}}}}{8 {\Lambda}^{5}}\right) P_L + \left(- \frac{{\lvert c^d_{12}\rvert} {v_\phi}^{4} \left(5 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{i {\alpha^d_{12}}}}{8 {\Lambda}^{5}}\right) P_R\right]
```

$`\bar{d} s h_2`$

```math
i \left[\left(\frac{{\lvert c^d_{21}\rvert} {v_\phi}^{4} \left(- 5 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{- i {\alpha^d_{21}}}}{8 {\Lambda}^{5}}\right) P_L + \left(\frac{{\lvert c^d_{12}\rvert} {v_\phi}^{4} \left(- 5 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{i {\alpha^d_{12}}}}{8 {\Lambda}^{5}}\right) P_R\right]
```

$`\bar{e} \mu a`$

```math
i \left[\left(\frac{5 i {\lvert c^e_{21}\rvert} {v} {v_\phi}^{4} e^{- i {\alpha^e_{21}}}}{8 {\Lambda}^{5}}\right) P_L + \left(- \frac{5 i {\lvert c^e_{12}\rvert} {v} {v_\phi}^{4} e^{i {\alpha^e_{12}}}}{8 {\Lambda}^{5}}\right) P_R\right]
```

$`\bar{e} \mu h_1`$

```math
i \left[\left(- \frac{{\lvert c^e_{21}\rvert} {v_\phi}^{4} \left(5 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{- i {\alpha^e_{21}}}}{8 {\Lambda}^{5}}\right) P_L + \left(- \frac{{\lvert c^e_{12}\rvert} {v_\phi}^{4} \left(5 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{i {\alpha^e_{12}}}}{8 {\Lambda}^{5}}\right) P_R\right]
```

$`\bar{e} \mu h_2`$

```math
i \left[\left(\frac{{\lvert c^e_{21}\rvert} {v_\phi}^{4} \left(- 5 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{- i {\alpha^e_{21}}}}{8 {\Lambda}^{5}}\right) P_L + \left(\frac{{\lvert c^e_{12}\rvert} {v_\phi}^{4} \left(- 5 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{i {\alpha^e_{12}}}}{8 {\Lambda}^{5}}\right) P_R\right]
```

$`\bar{e} \tau a`$

```math
i \left[\left(\frac{3 i {\lvert c^e_{31}\rvert} {v} {v_\phi}^{2} e^{- i {\alpha^e_{31}}}}{4 {\Lambda}^{3}}\right) P_L + \left(- \frac{5 i {\lvert c^e_{13}\rvert} {v} {v_\phi}^{4} e^{i {\alpha^e_{13}}}}{8 {\Lambda}^{5}}\right) P_R\right]
```

$`\bar{e} \tau h_1`$

```math
i \left[\left(- \frac{{\lvert c^e_{31}\rvert} {v_\phi}^{2} \left(3 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{- i {\alpha^e_{31}}}}{4 {\Lambda}^{3}}\right) P_L + \left(- \frac{{\lvert c^e_{13}\rvert} {v_\phi}^{4} \left(5 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{i {\alpha^e_{13}}}}{8 {\Lambda}^{5}}\right) P_R\right]
```

$`\bar{e} \tau h_2`$

```math
i \left[\left(\frac{{\lvert c^e_{31}\rvert} {v_\phi}^{2} \left(- 3 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{- i {\alpha^e_{31}}}}{4 {\Lambda}^{3}}\right) P_L + \left(\frac{{\lvert c^e_{13}\rvert} {v_\phi}^{4} \left(- 5 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{i {\alpha^e_{13}}}}{8 {\Lambda}^{5}}\right) P_R\right]
```

$`\bar{e} e a`$

```math
i \left[\left(\frac{3 \sqrt{2} i {\lvert c^e_{11}\rvert} {v} {v_\phi}^{5} e^{- i {\alpha^e_{11}}}}{8 {\Lambda}^{6}}\right) P_L + \left(- \frac{3 \sqrt{2} i {\lvert c^e_{11}\rvert} {v} {v_\phi}^{5} e^{i {\alpha^e_{11}}}}{8 {\Lambda}^{6}}\right) P_R\right]
```

$`\bar{e} e h_1`$

```math
i \left[\left(- \frac{\sqrt{2} {\lvert c^e_{11}\rvert} {v_\phi}^{5} \left(6 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{- i {\alpha^e_{11}}}}{16 {\Lambda}^{6}}\right) P_L + \left(- \frac{\sqrt{2} {\lvert c^e_{11}\rvert} {v_\phi}^{5} \left(6 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{i {\alpha^e_{11}}}}{16 {\Lambda}^{6}}\right) P_R\right]
```

$`\bar{e} e h_2`$

```math
i \left[\left(\frac{\sqrt{2} {\lvert c^e_{11}\rvert} {v_\phi}^{5} \left(- 6 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{- i {\alpha^e_{11}}}}{16 {\Lambda}^{6}}\right) P_L + \left(\frac{\sqrt{2} {\lvert c^e_{11}\rvert} {v_\phi}^{5} \left(- 6 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{i {\alpha^e_{11}}}}{16 {\Lambda}^{6}}\right) P_R\right]
```

$`\bar{s} b a`$

```math
i \left[\left(\frac{\sqrt{2} i {\lvert c^d_{32}\rvert} {v} {v_\phi} e^{- i {\alpha^d_{32}}}}{2 {\Lambda}^{2}}\right) P_L + \left(- \frac{\sqrt{2} i {\lvert c^d_{23}\rvert} {v} {v_\phi}^{3} e^{i {\alpha^d_{23}}}}{2 {\Lambda}^{4}}\right) P_R\right]
```

$`\bar{s} b h_1`$

```math
i \left[\left(- \frac{\sqrt{2} {\lvert c^d_{32}\rvert} {v_\phi} \left(2 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{- i {\alpha^d_{32}}}}{4 {\Lambda}^{2}}\right) P_L + \left(- \frac{\sqrt{2} {\lvert c^d_{23}\rvert} {v_\phi}^{3} \left(4 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{i {\alpha^d_{23}}}}{8 {\Lambda}^{4}}\right) P_R\right]
```

$`\bar{s} b h_2`$

```math
i \left[\left(\frac{\sqrt{2} {\lvert c^d_{32}\rvert} {v_\phi} \left(- 2 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{- i {\alpha^d_{32}}}}{4 {\Lambda}^{2}}\right) P_L + \left(\frac{\sqrt{2} {\lvert c^d_{23}\rvert} {v_\phi}^{3} \left(- 4 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{i {\alpha^d_{23}}}}{8 {\Lambda}^{4}}\right) P_R\right]
```

$`\bar{s} d a`$

```math
i \left[\left(\frac{5 i {\lvert c^d_{12}\rvert} {v} {v_\phi}^{4} e^{- i {\alpha^d_{12}}}}{8 {\Lambda}^{5}}\right) P_L + \left(- \frac{5 i {\lvert c^d_{21}\rvert} {v} {v_\phi}^{4} e^{i {\alpha^d_{21}}}}{8 {\Lambda}^{5}}\right) P_R\right]
```

$`\bar{s} d h_1`$

```math
i \left[\left(- \frac{{\lvert c^d_{12}\rvert} {v_\phi}^{4} \left(5 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{- i {\alpha^d_{12}}}}{8 {\Lambda}^{5}}\right) P_L + \left(- \frac{{\lvert c^d_{21}\rvert} {v_\phi}^{4} \left(5 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{i {\alpha^d_{21}}}}{8 {\Lambda}^{5}}\right) P_R\right]
```

$`\bar{s} d h_2`$

```math
i \left[\left(\frac{{\lvert c^d_{12}\rvert} {v_\phi}^{4} \left(- 5 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{- i {\alpha^d_{12}}}}{8 {\Lambda}^{5}}\right) P_L + \left(\frac{{\lvert c^d_{21}\rvert} {v_\phi}^{4} \left(- 5 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{i {\alpha^d_{21}}}}{8 {\Lambda}^{5}}\right) P_R\right]
```

$`\bar{s} s a`$

```math
i \left[\left(\frac{\sqrt{2} i {\lvert c^d_{22}\rvert} {v} {v_\phi}^{3} e^{- i {\alpha^d_{22}}}}{2 {\Lambda}^{4}}\right) P_L + \left(- \frac{\sqrt{2} i {\lvert c^d_{22}\rvert} {v} {v_\phi}^{3} e^{i {\alpha^d_{22}}}}{2 {\Lambda}^{4}}\right) P_R\right]
```

$`\bar{s} s h_1`$

```math
i \left[\left(- \frac{\sqrt{2} {\lvert c^d_{22}\rvert} {v_\phi}^{3} \left(4 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{- i {\alpha^d_{22}}}}{8 {\Lambda}^{4}}\right) P_L + \left(- \frac{\sqrt{2} {\lvert c^d_{22}\rvert} {v_\phi}^{3} \left(4 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{i {\alpha^d_{22}}}}{8 {\Lambda}^{4}}\right) P_R\right]
```

$`\bar{s} s h_2`$

```math
i \left[\left(\frac{\sqrt{2} {\lvert c^d_{22}\rvert} {v_\phi}^{3} \left(- 4 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{- i {\alpha^d_{22}}}}{8 {\Lambda}^{4}}\right) P_L + \left(\frac{\sqrt{2} {\lvert c^d_{22}\rvert} {v_\phi}^{3} \left(- 4 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{i {\alpha^d_{22}}}}{8 {\Lambda}^{4}}\right) P_R\right]
```

$`\bar{t} c a`$

```math
i \left[\left(\frac{\sqrt{2} i {\lvert c^u_{23}\rvert} {v} {v_\phi} e^{- i {\alpha^u_{23}}}}{2 {\Lambda}^{2}}\right) P_L + \left(- \frac{i {\lvert c^u_{32}\rvert} {v} e^{i {\alpha^u_{32}}}}{2 {\Lambda}}\right) P_R\right]
```

$`\bar{t} c h_1`$

```math
i \left[\left(- \frac{\sqrt{2} {\lvert c^u_{23}\rvert} {v_\phi} \left(2 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{- i {\alpha^u_{23}}}}{4 {\Lambda}^{2}}\right) P_L + \left(- \frac{{\lvert c^u_{32}\rvert} \left({v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{i {\alpha^u_{32}}}}{2 {\Lambda}}\right) P_R\right]
```

$`\bar{t} c h_2`$

```math
i \left[\left(\frac{\sqrt{2} {\lvert c^u_{23}\rvert} {v_\phi} \left(- 2 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{- i {\alpha^u_{23}}}}{4 {\Lambda}^{2}}\right) P_L + \left(\frac{{\lvert c^u_{32}\rvert} \left(- {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{i {\alpha^u_{32}}}}{2 {\Lambda}}\right) P_R\right]
```

$`\bar{t} t h_1`$

```math
i \left[\left(- \frac{\sqrt{2} {\lvert c^u_{33}\rvert} e^{- i {\alpha^u_{33}}} \cos{\left({\theta} \right)}}{2}\right) P_L + \left(- \frac{\sqrt{2} {\lvert c^u_{33}\rvert} e^{i {\alpha^u_{33}}} \cos{\left({\theta} \right)}}{2}\right) P_R\right]
```

$`\bar{t} t h_2`$

```math
i \left[\left(\frac{\sqrt{2} {\lvert c^u_{33}\rvert} e^{- i {\alpha^u_{33}}} \sin{\left({\theta} \right)}}{2}\right) P_L + \left(\frac{\sqrt{2} {\lvert c^u_{33}\rvert} e^{i {\alpha^u_{33}}} \sin{\left({\theta} \right)}}{2}\right) P_R\right]
```

$`\bar{t} u a`$

```math
i \left[\left(\frac{3 i {\lvert c^u_{13}\rvert} {v} {v_\phi}^{2} e^{- i {\alpha^u_{13}}}}{4 {\Lambda}^{3}}\right) P_L + \left(- \frac{3 i {\lvert c^u_{31}\rvert} {v} {v_\phi}^{2} e^{i {\alpha^u_{31}}}}{4 {\Lambda}^{3}}\right) P_R\right]
```

$`\bar{t} u h_1`$

```math
i \left[\left(- \frac{{\lvert c^u_{13}\rvert} {v_\phi}^{2} \left(3 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{- i {\alpha^u_{13}}}}{4 {\Lambda}^{3}}\right) P_L + \left(- \frac{{\lvert c^u_{31}\rvert} {v_\phi}^{2} \left(3 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{i {\alpha^u_{31}}}}{4 {\Lambda}^{3}}\right) P_R\right]
```

$`\bar{t} u h_2`$

```math
i \left[\left(\frac{{\lvert c^u_{13}\rvert} {v_\phi}^{2} \left(- 3 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{- i {\alpha^u_{13}}}}{4 {\Lambda}^{3}}\right) P_L + \left(\frac{{\lvert c^u_{31}\rvert} {v_\phi}^{2} \left(- 3 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{i {\alpha^u_{31}}}}{4 {\Lambda}^{3}}\right) P_R\right]
```

$`\bar{u} c a`$

```math
i \left[\left(\frac{5 i {\lvert c^u_{21}\rvert} {v} {v_\phi}^{4} e^{- i {\alpha^u_{21}}}}{8 {\Lambda}^{5}}\right) P_L + \left(- \frac{\sqrt{2} i {\lvert c^u_{12}\rvert} {v} {v_\phi}^{3} e^{i {\alpha^u_{12}}}}{2 {\Lambda}^{4}}\right) P_R\right]
```

$`\bar{u} c h_1`$

```math
i \left[\left(- \frac{{\lvert c^u_{21}\rvert} {v_\phi}^{4} \left(5 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{- i {\alpha^u_{21}}}}{8 {\Lambda}^{5}}\right) P_L + \left(- \frac{\sqrt{2} {\lvert c^u_{12}\rvert} {v_\phi}^{3} \left(4 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{i {\alpha^u_{12}}}}{8 {\Lambda}^{4}}\right) P_R\right]
```

$`\bar{u} c h_2`$

```math
i \left[\left(\frac{{\lvert c^u_{21}\rvert} {v_\phi}^{4} \left(- 5 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{- i {\alpha^u_{21}}}}{8 {\Lambda}^{5}}\right) P_L + \left(\frac{\sqrt{2} {\lvert c^u_{12}\rvert} {v_\phi}^{3} \left(- 4 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{i {\alpha^u_{12}}}}{8 {\Lambda}^{4}}\right) P_R\right]
```

$`\bar{u} t a`$

```math
i \left[\left(\frac{3 i {\lvert c^u_{31}\rvert} {v} {v_\phi}^{2} e^{- i {\alpha^u_{31}}}}{4 {\Lambda}^{3}}\right) P_L + \left(- \frac{3 i {\lvert c^u_{13}\rvert} {v} {v_\phi}^{2} e^{i {\alpha^u_{13}}}}{4 {\Lambda}^{3}}\right) P_R\right]
```

$`\bar{u} t h_1`$

```math
i \left[\left(- \frac{{\lvert c^u_{31}\rvert} {v_\phi}^{2} \left(3 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{- i {\alpha^u_{31}}}}{4 {\Lambda}^{3}}\right) P_L + \left(- \frac{{\lvert c^u_{13}\rvert} {v_\phi}^{2} \left(3 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{i {\alpha^u_{13}}}}{4 {\Lambda}^{3}}\right) P_R\right]
```

$`\bar{u} t h_2`$

```math
i \left[\left(\frac{{\lvert c^u_{31}\rvert} {v_\phi}^{2} \left(- 3 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{- i {\alpha^u_{31}}}}{4 {\Lambda}^{3}}\right) P_L + \left(\frac{{\lvert c^u_{13}\rvert} {v_\phi}^{2} \left(- 3 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{i {\alpha^u_{13}}}}{4 {\Lambda}^{3}}\right) P_R\right]
```

$`\bar{u} u a`$

```math
i \left[\left(\frac{3 \sqrt{2} i {\lvert c^u_{11}\rvert} {v} {v_\phi}^{5} e^{- i {\alpha^u_{11}}}}{8 {\Lambda}^{6}}\right) P_L + \left(- \frac{3 \sqrt{2} i {\lvert c^u_{11}\rvert} {v} {v_\phi}^{5} e^{i {\alpha^u_{11}}}}{8 {\Lambda}^{6}}\right) P_R\right]
```

$`\bar{u} u h_1`$

```math
i \left[\left(- \frac{\sqrt{2} {\lvert c^u_{11}\rvert} {v_\phi}^{5} \left(6 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{- i {\alpha^u_{11}}}}{16 {\Lambda}^{6}}\right) P_L + \left(- \frac{\sqrt{2} {\lvert c^u_{11}\rvert} {v_\phi}^{5} \left(6 {v} \sin{\left({\theta} \right)} + {v_\phi} \cos{\left({\theta} \right)}\right) e^{i {\alpha^u_{11}}}}{16 {\Lambda}^{6}}\right) P_R\right]
```

$`\bar{u} u h_2`$

```math
i \left[\left(\frac{\sqrt{2} {\lvert c^u_{11}\rvert} {v_\phi}^{5} \left(- 6 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{- i {\alpha^u_{11}}}}{16 {\Lambda}^{6}}\right) P_L + \left(\frac{\sqrt{2} {\lvert c^u_{11}\rvert} {v_\phi}^{5} \left(- 6 {v} \cos{\left({\theta} \right)} + {v_\phi} \sin{\left({\theta} \right)}\right) e^{i {\alpha^u_{11}}}}{16 {\Lambda}^{6}}\right) P_R\right]
```

### Fermion pairs with a Goldstone leg (Feynman gauge): 63 vertices

Absent from the unitary-gauge UFO, which drops every Goldstone leg.

#### Fermion pair and a scalar (FFS): 63 vertices

| interaction | Feynman rule |
|---|---|
| $`\bar{\mu} \nu_\mu G^-`$ | $`i \left(- \frac{{\lvert c^e_{22}\rvert} {v_\phi}^{4} e^{- i {\alpha^e_{22}}}}{4 {\Lambda}^{4}}\right) P_L`$ |
| $`\bar{\mu} \nu_\tau G^-`$ | $`i \left(- \frac{{\lvert c^e_{32}\rvert} {v_\phi}^{2} e^{- i {\alpha^e_{32}}}}{2 {\Lambda}^{2}}\right) P_L`$ |
| $`\bar{\mu} \nu_e G^-`$ | $`i \left(- \frac{\sqrt{2} {\lvert c^e_{12}\rvert} {v_\phi}^{5} e^{- i {\alpha^e_{12}}}}{8 {\Lambda}^{5}}\right) P_L`$ |
| $`\bar{\nu}_\mu \mu G^+`$ | $`i \left(- \frac{{\lvert c^e_{22}\rvert} {v_\phi}^{4} e^{i {\alpha^e_{22}}}}{4 {\Lambda}^{4}}\right) P_R`$ |
| $`\bar{\nu}_\mu \tau G^+`$ | $`i \left(- \frac{{\lvert c^e_{23}\rvert} {v_\phi}^{4} e^{i {\alpha^e_{23}}}}{4 {\Lambda}^{4}}\right) P_R`$ |
| $`\bar{\nu}_\mu e G^+`$ | $`i \left(- \frac{\sqrt{2} {\lvert c^e_{21}\rvert} {v_\phi}^{5} e^{i {\alpha^e_{21}}}}{8 {\Lambda}^{5}}\right) P_R`$ |
| $`\bar{\nu}_\tau \mu G^+`$ | $`i \left(- \frac{{\lvert c^e_{32}\rvert} {v_\phi}^{2} e^{i {\alpha^e_{32}}}}{2 {\Lambda}^{2}}\right) P_R`$ |
| $`\bar{\nu}_\tau \tau G^+`$ | $`i \left(- \frac{{\lvert c^e_{33}\rvert} {v_\phi}^{2} e^{i {\alpha^e_{33}}}}{2 {\Lambda}^{2}}\right) P_R`$ |
| $`\bar{\nu}_\tau e G^+`$ | $`i \left(- \frac{\sqrt{2} {\lvert c^e_{31}\rvert} {v_\phi}^{3} e^{i {\alpha^e_{31}}}}{4 {\Lambda}^{3}}\right) P_R`$ |
| $`\bar{\nu}_e \mu G^+`$ | $`i \left(- \frac{\sqrt{2} {\lvert c^e_{12}\rvert} {v_\phi}^{5} e^{i {\alpha^e_{12}}}}{8 {\Lambda}^{5}}\right) P_R`$ |
| $`\bar{\nu}_e \tau G^+`$ | $`i \left(- \frac{\sqrt{2} {\lvert c^e_{13}\rvert} {v_\phi}^{5} e^{i {\alpha^e_{13}}}}{8 {\Lambda}^{5}}\right) P_R`$ |
| $`\bar{\nu}_e e G^+`$ | $`i \left(- \frac{{\lvert c^e_{11}\rvert} {v_\phi}^{6} e^{i {\alpha^e_{11}}}}{8 {\Lambda}^{6}}\right) P_R`$ |
| $`\bar{\tau} \nu_\mu G^-`$ | $`i \left(- \frac{{\lvert c^e_{23}\rvert} {v_\phi}^{4} e^{- i {\alpha^e_{23}}}}{4 {\Lambda}^{4}}\right) P_L`$ |
| $`\bar{\tau} \nu_\tau G^-`$ | $`i \left(- \frac{{\lvert c^e_{33}\rvert} {v_\phi}^{2} e^{- i {\alpha^e_{33}}}}{2 {\Lambda}^{2}}\right) P_L`$ |
| $`\bar{\tau} \nu_e G^-`$ | $`i \left(- \frac{\sqrt{2} {\lvert c^e_{13}\rvert} {v_\phi}^{5} e^{- i {\alpha^e_{13}}}}{8 {\Lambda}^{5}}\right) P_L`$ |
| $`\bar{b} t G^-`$ | $`i \left[\left(- \frac{{\lvert c^d_{33}\rvert} {v_\phi}^{2} e^{- i {\alpha^d_{33}}}}{2 {\Lambda}^{2}}\right) P_L + \left({\lvert c^u_{33}\rvert} e^{i {\alpha^u_{33}}}\right) P_R\right]`$ |
| $`\bar{e} \nu_\mu G^-`$ | $`i \left(- \frac{\sqrt{2} {\lvert c^e_{21}\rvert} {v_\phi}^{5} e^{- i {\alpha^e_{21}}}}{8 {\Lambda}^{5}}\right) P_L`$ |
| $`\bar{e} \nu_\tau G^-`$ | $`i \left(- \frac{\sqrt{2} {\lvert c^e_{31}\rvert} {v_\phi}^{3} e^{- i {\alpha^e_{31}}}}{4 {\Lambda}^{3}}\right) P_L`$ |
| $`\bar{e} \nu_e G^-`$ | $`i \left(- \frac{{\lvert c^e_{11}\rvert} {v_\phi}^{6} e^{- i {\alpha^e_{11}}}}{8 {\Lambda}^{6}}\right) P_L`$ |
| $`\bar{t} b G^+`$ | $`i \left[\left({\lvert c^u_{33}\rvert} e^{- i {\alpha^u_{33}}}\right) P_L + \left(- \frac{{\lvert c^d_{33}\rvert} {v_\phi}^{2} e^{i {\alpha^d_{33}}}}{2 {\Lambda}^{2}}\right) P_R\right]`$ |
| $`\bar{t} t G^0`$ | $`i \left[\left(- \frac{\sqrt{2} i {\lvert c^u_{33}\rvert} e^{- i {\alpha^u_{33}}}}{2}\right) P_L + \left(\frac{\sqrt{2} i {\lvert c^u_{33}\rvert} e^{i {\alpha^u_{33}}}}{2}\right) P_R\right]`$ |

$`\bar{\mu} \mu G^0`$

```math
i \left[\left(\frac{\sqrt{2} i {\lvert c^e_{22}\rvert} {v_\phi}^{4} e^{- i {\alpha^e_{22}}}}{8 {\Lambda}^{4}}\right) P_L + \left(- \frac{\sqrt{2} i {\lvert c^e_{22}\rvert} {v_\phi}^{4} e^{i {\alpha^e_{22}}}}{8 {\Lambda}^{4}}\right) P_R\right]
```

$`\bar{\mu} \tau G^0`$

```math
i \left[\left(\frac{\sqrt{2} i {\lvert c^e_{32}\rvert} {v_\phi}^{2} e^{- i {\alpha^e_{32}}}}{4 {\Lambda}^{2}}\right) P_L + \left(- \frac{\sqrt{2} i {\lvert c^e_{23}\rvert} {v_\phi}^{4} e^{i {\alpha^e_{23}}}}{8 {\Lambda}^{4}}\right) P_R\right]
```

$`\bar{\mu} e G^0`$

```math
i \left[\left(\frac{i {\lvert c^e_{12}\rvert} {v_\phi}^{5} e^{- i {\alpha^e_{12}}}}{8 {\Lambda}^{5}}\right) P_L + \left(- \frac{i {\lvert c^e_{21}\rvert} {v_\phi}^{5} e^{i {\alpha^e_{21}}}}{8 {\Lambda}^{5}}\right) P_R\right]
```

$`\bar{\tau} \mu G^0`$

```math
i \left[\left(\frac{\sqrt{2} i {\lvert c^e_{23}\rvert} {v_\phi}^{4} e^{- i {\alpha^e_{23}}}}{8 {\Lambda}^{4}}\right) P_L + \left(- \frac{\sqrt{2} i {\lvert c^e_{32}\rvert} {v_\phi}^{2} e^{i {\alpha^e_{32}}}}{4 {\Lambda}^{2}}\right) P_R\right]
```

$`\bar{\tau} \tau G^0`$

```math
i \left[\left(\frac{\sqrt{2} i {\lvert c^e_{33}\rvert} {v_\phi}^{2} e^{- i {\alpha^e_{33}}}}{4 {\Lambda}^{2}}\right) P_L + \left(- \frac{\sqrt{2} i {\lvert c^e_{33}\rvert} {v_\phi}^{2} e^{i {\alpha^e_{33}}}}{4 {\Lambda}^{2}}\right) P_R\right]
```

$`\bar{\tau} e G^0`$

```math
i \left[\left(\frac{i {\lvert c^e_{13}\rvert} {v_\phi}^{5} e^{- i {\alpha^e_{13}}}}{8 {\Lambda}^{5}}\right) P_L + \left(- \frac{i {\lvert c^e_{31}\rvert} {v_\phi}^{3} e^{i {\alpha^e_{31}}}}{4 {\Lambda}^{3}}\right) P_R\right]
```

$`\bar{b} b G^0`$

```math
i \left[\left(\frac{\sqrt{2} i {\lvert c^d_{33}\rvert} {v_\phi}^{2} e^{- i {\alpha^d_{33}}}}{4 {\Lambda}^{2}}\right) P_L + \left(- \frac{\sqrt{2} i {\lvert c^d_{33}\rvert} {v_\phi}^{2} e^{i {\alpha^d_{33}}}}{4 {\Lambda}^{2}}\right) P_R\right]
```

$`\bar{b} c G^-`$

```math
i \left[\left(- \frac{{\lvert c^d_{23}\rvert} {v_\phi}^{4} e^{- i {\alpha^d_{23}}}}{4 {\Lambda}^{4}}\right) P_L + \left(\frac{\sqrt{2} {\lvert c^u_{32}\rvert} {v_\phi} e^{i {\alpha^u_{32}}}}{2 {\Lambda}}\right) P_R\right]
```

$`\bar{b} d G^0`$

```math
i \left[\left(\frac{i {\lvert c^d_{13}\rvert} {v_\phi}^{5} e^{- i {\alpha^d_{13}}}}{8 {\Lambda}^{5}}\right) P_L + \left(- \frac{i {\lvert c^d_{31}\rvert} {v_\phi}^{3} e^{i {\alpha^d_{31}}}}{4 {\Lambda}^{3}}\right) P_R\right]
```

$`\bar{b} s G^0`$

```math
i \left[\left(\frac{\sqrt{2} i {\lvert c^d_{23}\rvert} {v_\phi}^{4} e^{- i {\alpha^d_{23}}}}{8 {\Lambda}^{4}}\right) P_L + \left(- \frac{\sqrt{2} i {\lvert c^d_{32}\rvert} {v_\phi}^{2} e^{i {\alpha^d_{32}}}}{4 {\Lambda}^{2}}\right) P_R\right]
```

$`\bar{b} u G^-`$

```math
i \left[\left(- \frac{\sqrt{2} {\lvert c^d_{13}\rvert} {v_\phi}^{5} e^{- i {\alpha^d_{13}}}}{8 {\Lambda}^{5}}\right) P_L + \left(\frac{\sqrt{2} {\lvert c^u_{31}\rvert} {v_\phi}^{3} e^{i {\alpha^u_{31}}}}{4 {\Lambda}^{3}}\right) P_R\right]
```

$`\bar{c} b G^+`$

```math
i \left[\left(\frac{\sqrt{2} {\lvert c^u_{32}\rvert} {v_\phi} e^{- i {\alpha^u_{32}}}}{2 {\Lambda}}\right) P_L + \left(- \frac{{\lvert c^d_{23}\rvert} {v_\phi}^{4} e^{i {\alpha^d_{23}}}}{4 {\Lambda}^{4}}\right) P_R\right]
```

$`\bar{c} c G^0`$

```math
i \left[\left(- \frac{i {\lvert c^u_{22}\rvert} {v_\phi}^{3} e^{- i {\alpha^u_{22}}}}{4 {\Lambda}^{3}}\right) P_L + \left(\frac{i {\lvert c^u_{22}\rvert} {v_\phi}^{3} e^{i {\alpha^u_{22}}}}{4 {\Lambda}^{3}}\right) P_R\right]
```

$`\bar{c} d G^+`$

```math
i \left[\left(\frac{{\lvert c^u_{12}\rvert} {v_\phi}^{4} e^{- i {\alpha^u_{12}}}}{4 {\Lambda}^{4}}\right) P_L + \left(- \frac{\sqrt{2} {\lvert c^d_{21}\rvert} {v_\phi}^{5} e^{i {\alpha^d_{21}}}}{8 {\Lambda}^{5}}\right) P_R\right]
```

$`\bar{c} s G^+`$

```math
i \left[\left(\frac{\sqrt{2} {\lvert c^u_{22}\rvert} {v_\phi}^{3} e^{- i {\alpha^u_{22}}}}{4 {\Lambda}^{3}}\right) P_L + \left(- \frac{{\lvert c^d_{22}\rvert} {v_\phi}^{4} e^{i {\alpha^d_{22}}}}{4 {\Lambda}^{4}}\right) P_R\right]
```

$`\bar{c} t G^0`$

```math
i \left[\left(- \frac{i {\lvert c^u_{32}\rvert} {v_\phi} e^{- i {\alpha^u_{32}}}}{2 {\Lambda}}\right) P_L + \left(\frac{\sqrt{2} i {\lvert c^u_{23}\rvert} {v_\phi}^{2} e^{i {\alpha^u_{23}}}}{4 {\Lambda}^{2}}\right) P_R\right]
```

$`\bar{c} u G^0`$

```math
i \left[\left(- \frac{\sqrt{2} i {\lvert c^u_{12}\rvert} {v_\phi}^{4} e^{- i {\alpha^u_{12}}}}{8 {\Lambda}^{4}}\right) P_L + \left(\frac{i {\lvert c^u_{21}\rvert} {v_\phi}^{5} e^{i {\alpha^u_{21}}}}{8 {\Lambda}^{5}}\right) P_R\right]
```

$`\bar{d} b G^0`$

```math
i \left[\left(\frac{i {\lvert c^d_{31}\rvert} {v_\phi}^{3} e^{- i {\alpha^d_{31}}}}{4 {\Lambda}^{3}}\right) P_L + \left(- \frac{i {\lvert c^d_{13}\rvert} {v_\phi}^{5} e^{i {\alpha^d_{13}}}}{8 {\Lambda}^{5}}\right) P_R\right]
```

$`\bar{d} c G^-`$

```math
i \left[\left(- \frac{\sqrt{2} {\lvert c^d_{21}\rvert} {v_\phi}^{5} e^{- i {\alpha^d_{21}}}}{8 {\Lambda}^{5}}\right) P_L + \left(\frac{{\lvert c^u_{12}\rvert} {v_\phi}^{4} e^{i {\alpha^u_{12}}}}{4 {\Lambda}^{4}}\right) P_R\right]
```

$`\bar{d} d G^0`$

```math
i \left[\left(\frac{\sqrt{2} i {\lvert c^d_{11}\rvert} {v_\phi}^{6} e^{- i {\alpha^d_{11}}}}{16 {\Lambda}^{6}}\right) P_L + \left(- \frac{\sqrt{2} i {\lvert c^d_{11}\rvert} {v_\phi}^{6} e^{i {\alpha^d_{11}}}}{16 {\Lambda}^{6}}\right) P_R\right]
```

$`\bar{d} s G^0`$

```math
i \left[\left(\frac{i {\lvert c^d_{21}\rvert} {v_\phi}^{5} e^{- i {\alpha^d_{21}}}}{8 {\Lambda}^{5}}\right) P_L + \left(- \frac{i {\lvert c^d_{12}\rvert} {v_\phi}^{5} e^{i {\alpha^d_{12}}}}{8 {\Lambda}^{5}}\right) P_R\right]
```

$`\bar{d} t G^-`$

```math
i \left[\left(- \frac{\sqrt{2} {\lvert c^d_{31}\rvert} {v_\phi}^{3} e^{- i {\alpha^d_{31}}}}{4 {\Lambda}^{3}}\right) P_L + \left(\frac{\sqrt{2} {\lvert c^u_{13}\rvert} {v_\phi}^{3} e^{i {\alpha^u_{13}}}}{4 {\Lambda}^{3}}\right) P_R\right]
```

$`\bar{d} u G^-`$

```math
i \left[\left(- \frac{{\lvert c^d_{11}\rvert} {v_\phi}^{6} e^{- i {\alpha^d_{11}}}}{8 {\Lambda}^{6}}\right) P_L + \left(\frac{{\lvert c^u_{11}\rvert} {v_\phi}^{6} e^{i {\alpha^u_{11}}}}{8 {\Lambda}^{6}}\right) P_R\right]
```

$`\bar{e} \mu G^0`$

```math
i \left[\left(\frac{i {\lvert c^e_{21}\rvert} {v_\phi}^{5} e^{- i {\alpha^e_{21}}}}{8 {\Lambda}^{5}}\right) P_L + \left(- \frac{i {\lvert c^e_{12}\rvert} {v_\phi}^{5} e^{i {\alpha^e_{12}}}}{8 {\Lambda}^{5}}\right) P_R\right]
```

$`\bar{e} \tau G^0`$

```math
i \left[\left(\frac{i {\lvert c^e_{31}\rvert} {v_\phi}^{3} e^{- i {\alpha^e_{31}}}}{4 {\Lambda}^{3}}\right) P_L + \left(- \frac{i {\lvert c^e_{13}\rvert} {v_\phi}^{5} e^{i {\alpha^e_{13}}}}{8 {\Lambda}^{5}}\right) P_R\right]
```

$`\bar{e} e G^0`$

```math
i \left[\left(\frac{\sqrt{2} i {\lvert c^e_{11}\rvert} {v_\phi}^{6} e^{- i {\alpha^e_{11}}}}{16 {\Lambda}^{6}}\right) P_L + \left(- \frac{\sqrt{2} i {\lvert c^e_{11}\rvert} {v_\phi}^{6} e^{i {\alpha^e_{11}}}}{16 {\Lambda}^{6}}\right) P_R\right]
```

$`\bar{s} b G^0`$

```math
i \left[\left(\frac{\sqrt{2} i {\lvert c^d_{32}\rvert} {v_\phi}^{2} e^{- i {\alpha^d_{32}}}}{4 {\Lambda}^{2}}\right) P_L + \left(- \frac{\sqrt{2} i {\lvert c^d_{23}\rvert} {v_\phi}^{4} e^{i {\alpha^d_{23}}}}{8 {\Lambda}^{4}}\right) P_R\right]
```

$`\bar{s} c G^-`$

```math
i \left[\left(- \frac{{\lvert c^d_{22}\rvert} {v_\phi}^{4} e^{- i {\alpha^d_{22}}}}{4 {\Lambda}^{4}}\right) P_L + \left(\frac{\sqrt{2} {\lvert c^u_{22}\rvert} {v_\phi}^{3} e^{i {\alpha^u_{22}}}}{4 {\Lambda}^{3}}\right) P_R\right]
```

$`\bar{s} d G^0`$

```math
i \left[\left(\frac{i {\lvert c^d_{12}\rvert} {v_\phi}^{5} e^{- i {\alpha^d_{12}}}}{8 {\Lambda}^{5}}\right) P_L + \left(- \frac{i {\lvert c^d_{21}\rvert} {v_\phi}^{5} e^{i {\alpha^d_{21}}}}{8 {\Lambda}^{5}}\right) P_R\right]
```

$`\bar{s} s G^0`$

```math
i \left[\left(\frac{\sqrt{2} i {\lvert c^d_{22}\rvert} {v_\phi}^{4} e^{- i {\alpha^d_{22}}}}{8 {\Lambda}^{4}}\right) P_L + \left(- \frac{\sqrt{2} i {\lvert c^d_{22}\rvert} {v_\phi}^{4} e^{i {\alpha^d_{22}}}}{8 {\Lambda}^{4}}\right) P_R\right]
```

$`\bar{s} t G^-`$

```math
i \left[\left(- \frac{{\lvert c^d_{32}\rvert} {v_\phi}^{2} e^{- i {\alpha^d_{32}}}}{2 {\Lambda}^{2}}\right) P_L + \left(\frac{{\lvert c^u_{23}\rvert} {v_\phi}^{2} e^{i {\alpha^u_{23}}}}{2 {\Lambda}^{2}}\right) P_R\right]
```

$`\bar{s} u G^-`$

```math
i \left[\left(- \frac{\sqrt{2} {\lvert c^d_{12}\rvert} {v_\phi}^{5} e^{- i {\alpha^d_{12}}}}{8 {\Lambda}^{5}}\right) P_L + \left(\frac{\sqrt{2} {\lvert c^u_{21}\rvert} {v_\phi}^{5} e^{i {\alpha^u_{21}}}}{8 {\Lambda}^{5}}\right) P_R\right]
```

$`\bar{t} c G^0`$

```math
i \left[\left(- \frac{\sqrt{2} i {\lvert c^u_{23}\rvert} {v_\phi}^{2} e^{- i {\alpha^u_{23}}}}{4 {\Lambda}^{2}}\right) P_L + \left(\frac{i {\lvert c^u_{32}\rvert} {v_\phi} e^{i {\alpha^u_{32}}}}{2 {\Lambda}}\right) P_R\right]
```

$`\bar{t} d G^+`$

```math
i \left[\left(\frac{\sqrt{2} {\lvert c^u_{13}\rvert} {v_\phi}^{3} e^{- i {\alpha^u_{13}}}}{4 {\Lambda}^{3}}\right) P_L + \left(- \frac{\sqrt{2} {\lvert c^d_{31}\rvert} {v_\phi}^{3} e^{i {\alpha^d_{31}}}}{4 {\Lambda}^{3}}\right) P_R\right]
```

$`\bar{t} s G^+`$

```math
i \left[\left(\frac{{\lvert c^u_{23}\rvert} {v_\phi}^{2} e^{- i {\alpha^u_{23}}}}{2 {\Lambda}^{2}}\right) P_L + \left(- \frac{{\lvert c^d_{32}\rvert} {v_\phi}^{2} e^{i {\alpha^d_{32}}}}{2 {\Lambda}^{2}}\right) P_R\right]
```

$`\bar{t} u G^0`$

```math
i \left[\left(- \frac{i {\lvert c^u_{13}\rvert} {v_\phi}^{3} e^{- i {\alpha^u_{13}}}}{4 {\Lambda}^{3}}\right) P_L + \left(\frac{i {\lvert c^u_{31}\rvert} {v_\phi}^{3} e^{i {\alpha^u_{31}}}}{4 {\Lambda}^{3}}\right) P_R\right]
```

$`\bar{u} b G^+`$

```math
i \left[\left(\frac{\sqrt{2} {\lvert c^u_{31}\rvert} {v_\phi}^{3} e^{- i {\alpha^u_{31}}}}{4 {\Lambda}^{3}}\right) P_L + \left(- \frac{\sqrt{2} {\lvert c^d_{13}\rvert} {v_\phi}^{5} e^{i {\alpha^d_{13}}}}{8 {\Lambda}^{5}}\right) P_R\right]
```

$`\bar{u} c G^0`$

```math
i \left[\left(- \frac{i {\lvert c^u_{21}\rvert} {v_\phi}^{5} e^{- i {\alpha^u_{21}}}}{8 {\Lambda}^{5}}\right) P_L + \left(\frac{\sqrt{2} i {\lvert c^u_{12}\rvert} {v_\phi}^{4} e^{i {\alpha^u_{12}}}}{8 {\Lambda}^{4}}\right) P_R\right]
```

$`\bar{u} d G^+`$

```math
i \left[\left(\frac{{\lvert c^u_{11}\rvert} {v_\phi}^{6} e^{- i {\alpha^u_{11}}}}{8 {\Lambda}^{6}}\right) P_L + \left(- \frac{{\lvert c^d_{11}\rvert} {v_\phi}^{6} e^{i {\alpha^d_{11}}}}{8 {\Lambda}^{6}}\right) P_R\right]
```

$`\bar{u} s G^+`$

```math
i \left[\left(\frac{\sqrt{2} {\lvert c^u_{21}\rvert} {v_\phi}^{5} e^{- i {\alpha^u_{21}}}}{8 {\Lambda}^{5}}\right) P_L + \left(- \frac{\sqrt{2} {\lvert c^d_{12}\rvert} {v_\phi}^{5} e^{i {\alpha^d_{12}}}}{8 {\Lambda}^{5}}\right) P_R\right]
```

$`\bar{u} t G^0`$

```math
i \left[\left(- \frac{i {\lvert c^u_{31}\rvert} {v_\phi}^{3} e^{- i {\alpha^u_{31}}}}{4 {\Lambda}^{3}}\right) P_L + \left(\frac{i {\lvert c^u_{13}\rvert} {v_\phi}^{3} e^{i {\alpha^u_{13}}}}{4 {\Lambda}^{3}}\right) P_R\right]
```

$`\bar{u} u G^0`$

```math
i \left[\left(- \frac{\sqrt{2} i {\lvert c^u_{11}\rvert} {v_\phi}^{6} e^{- i {\alpha^u_{11}}}}{16 {\Lambda}^{6}}\right) P_L + \left(\frac{\sqrt{2} i {\lvert c^u_{11}\rvert} {v_\phi}^{6} e^{i {\alpha^u_{11}}}}{16 {\Lambda}^{6}}\right) P_R\right]
```

## Fermion legs are weak-basis states

The fermion vertices above are in the **weak (flavour) basis**: a leg named $`u`$, $`c`$, $`t`$ (or
$`d`$, $`s`$, $`b`$; $`e`$, $`\mu`$, $`\tau`$) is the generation-1, 2, 3 weak state, not a mass
eigenstate, and the Yukawa-type couplings are the entries of $`M = v\,Y/\sqrt2`$ with
$`Y_{ij} = c_{ij}\,\epsilon^{n_{ij}}`$. The complex $`3\times3`$ Yukawas are diagonalised only
numerically (feynlag's `diagonalize_svd(method="numeric")`); the resulting masses and
$`\lvert V_{ij}\rvert`$ at the benchmark are in [`spectrum.md`](spectrum.md). The flavon couplings
are those of the operators linearised in the flavon fluctuation (see the [card](../README.md)).
