# Feynman rules: Standard Model (one Higgs doublet, one full fermion generation)

Bosonic vertices of `sm` (potential and kinetic sectors), 38 in all, as feynlag derives them at tree level.
This page re-renders the rules of [`vertices.tex`](vertices.tex) with physics names; it adds no verification. See the [card](../README.md) for what the tests pin against the literature, [`spectrum.md`](spectrum.md) for the masses and the [UFO](SM_UFO/) for the exported couplings.

Each rule is $`i \times (\text{monomial coefficient}) \times \prod_f (\text{multiplicity of } f)!`$, all momenta are incoming and $`\partial_\mu \to i\,p_\mu`$ ([`CONVENTIONS.md`](../../../CONVENTIONS.md)); $`p_X`$ is the momentum of leg $`X`$.

## Cubic scalar (SSS): 1 vertices

| interaction | Feynman rule |
|---|---|
| $`h h h`$ | $`- 6 i {\lambda} {v}`$ |

## Quartic scalar (SSSS): 1 vertices

| interaction | Feynman rule |
|---|---|
| $`h h h h`$ | $`- 6 i {\lambda}`$ |

## Two vectors and a scalar (VVS): 2 vertices

| interaction | Feynman rule |
|---|---|
| $`W^- W^+ h`$ | $`\frac{i {g}^{2} {v}}{2}`$ |
| $`Z Z h`$ | $`\frac{i {v} \left({g'}^{2} + {g}^{2}\right)}{2}`$ |

## Two vectors and two scalars (VVSS): 2 vertices

| interaction | Feynman rule |
|---|---|
| $`W^- W^+ h h`$ | $`\frac{i {g}^{2}}{2}`$ |
| $`Z Z h h`$ | $`\frac{i \left({g'}^{2} + {g}^{2}\right)}{2}`$ |

## Feynman-gauge vertices with a Goldstone leg: 32 in all

The unitary-gauge UFO drops these; they matter for a Feynman-gauge calculation.

### Cubic scalar (SSS): 2 vertices

| interaction | Feynman rule |
|---|---|
| $`G^- G^+ h`$ | $`- 2 i {\lambda} {v}`$ |
| $`G^0 G^0 h`$ | $`- 2 i {\lambda} {v}`$ |

### Quartic scalar (SSSS): 5 vertices

| interaction | Feynman rule |
|---|---|
| $`G^- G^- G^+ G^+`$ | $`- 4 i {\lambda}`$ |
| $`G^- G^+ G^0 G^0`$ | $`- 2 i {\lambda}`$ |
| $`G^- G^+ h h`$ | $`- 2 i {\lambda}`$ |
| $`G^0 G^0 G^0 G^0`$ | $`- 6 i {\lambda}`$ |
| $`G^0 G^0 h h`$ | $`- 2 i {\lambda}`$ |

### Vector and two scalars (VSS): 7 vertices

| interaction | Feynman rule |
|---|---|
| $`\gamma G^- G^+`$ | $`\frac{i {g'} {g} \left({p_{G^-}} - {p_{G^+}}\right)}{\sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`Z G^- G^+`$ | $`\frac{i \left(- {g'}^{2} {p_{G^-}} + {g'}^{2} {p_{G^+}} + {g}^{2} {p_{G^-}} - {g}^{2} {p_{G^+}}\right)}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`W^+ G^- G^0`$ | $`\frac{{g} \left(- {p_{G^-}} + {p_{G^0}}\right)}{2}`$ |
| $`W^+ G^- h`$ | $`\frac{i {g} \left({p_{G^-}} - {p_{h}}\right)}{2}`$ |
| $`W^- G^+ G^0`$ | $`\frac{{g} \left(- {p_{G^+}} + {p_{G^0}}\right)}{2}`$ |
| $`W^- G^+ h`$ | $`\frac{i {g} \left(- {p_{G^+}} + {p_{h}}\right)}{2}`$ |
| $`Z G^0 h`$ | $`\frac{- {g'}^{2} {p_{G^0}} + {g'}^{2} {p_{h}} - {g}^{2} {p_{G^0}} + {g}^{2} {p_{h}}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |

### Two vectors and a scalar (VVS): 4 vertices

| interaction | Feynman rule |
|---|---|
| $`\gamma W^+ G^-`$ | $`\frac{i {g'} {g}^{2} {v}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`\gamma W^- G^+`$ | $`\frac{i {g'} {g}^{2} {v}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`W^+ Z G^-`$ | $`- \frac{i {g'}^{2} {g} {v}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`W^- Z G^+`$ | $`- \frac{i {g'}^{2} {g} {v}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |

### Two vectors and two scalars (VVSS): 14 vertices

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
