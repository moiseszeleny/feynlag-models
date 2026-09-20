# Feynman rules: Two-Higgs-doublet model, type II, CP-conserving, softly broken Z2

Tree-level vertices of `thdm_type2` as feynlag derives them: 154 bosonic (potential and kinetic sectors) and the fermion couplings below.
This page re-renders the rules of [`vertices.tex`](vertices.tex) with physics names; it adds no verification. See the [card](../README.md) for what the tests pin against the literature, [`spectrum.md`](spectrum.md) for the masses and the [UFO](THDM_TYPE2_UFO/) for the exported couplings.

Each rule is $`i \times (\text{monomial coefficient}) \times \prod_f (\text{multiplicity of } f)!`$, all momenta are incoming and $`\partial_\mu \to i\,p_\mu`$ ([`CONVENTIONS.md`](../../../CONVENTIONS.md)); $`p_X`$ is the momentum of leg $`X`$.

## Bosonic vertices: 154 in all

### Cubic scalar (SSS): 8 vertices

$`A A H`$

```math
i \left(- {\lambda_1} {v_1} \sin^{2}{\left({\beta} \right)} \cos{\left({\alpha} \right)} - {\lambda_2} {v_2} \sin{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} - {\lambda_3} {v_1} \cos{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} - {\lambda_3} {v_2} \sin{\left({\alpha} \right)} \sin^{2}{\left({\beta} \right)} - {\lambda_4} {v_1} \cos{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} - {\lambda_4} {v_2} \sin{\left({\alpha} \right)} \sin^{2}{\left({\beta} \right)} + \frac{{\lambda_5} {v_1} \left(\cos{\left({\alpha} - 2 {\beta} \right)} - \cos{\left({\alpha} + 2 {\beta} \right)}\right)}{2} + {\lambda_5} {v_1} \cos{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} + \frac{{\lambda_5} {v_2} \left(- \sin{\left({\alpha} - 2 {\beta} \right)} + \sin{\left({\alpha} + 2 {\beta} \right)}\right)}{2} + {\lambda_5} {v_2} \sin{\left({\alpha} \right)} \sin^{2}{\left({\beta} \right)}\right)
```

$`A A h`$

```math
i \left({\lambda_1} {v_1} \sin{\left({\alpha} \right)} \sin^{2}{\left({\beta} \right)} - {\lambda_2} {v_2} \cos{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} + {\lambda_3} {v_1} \sin{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} - {\lambda_3} {v_2} \sin^{2}{\left({\beta} \right)} \cos{\left({\alpha} \right)} + {\lambda_4} {v_1} \sin{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} - {\lambda_4} {v_2} \sin^{2}{\left({\beta} \right)} \cos{\left({\alpha} \right)} + \frac{{\lambda_5} {v_1} \left(- \sin{\left({\alpha} - 2 {\beta} \right)} + \sin{\left({\alpha} + 2 {\beta} \right)}\right)}{2} - {\lambda_5} {v_1} \sin{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} - \frac{{\lambda_5} {v_2} \left(\cos{\left({\alpha} - 2 {\beta} \right)} - \cos{\left({\alpha} + 2 {\beta} \right)}\right)}{2} + {\lambda_5} {v_2} \sin^{2}{\left({\beta} \right)} \cos{\left({\alpha} \right)}\right)
```

$`H H H`$

```math
3 i \left(- {\lambda_1} {v_1} \cos^{3}{\left({\alpha} \right)} - {\lambda_2} {v_2} \sin^{3}{\left({\alpha} \right)} - {\lambda_3} {v_1} \sin^{2}{\left({\alpha} \right)} \cos{\left({\alpha} \right)} - {\lambda_3} {v_2} \sin{\left({\alpha} \right)} \cos^{2}{\left({\alpha} \right)} - {\lambda_4} {v_1} \sin^{2}{\left({\alpha} \right)} \cos{\left({\alpha} \right)} - {\lambda_4} {v_2} \sin{\left({\alpha} \right)} \cos^{2}{\left({\alpha} \right)} - {\lambda_5} {v_1} \sin^{2}{\left({\alpha} \right)} \cos{\left({\alpha} \right)} - {\lambda_5} {v_2} \sin{\left({\alpha} \right)} \cos^{2}{\left({\alpha} \right)}\right)
```

$`H H h`$

```math
i \left(3 {\lambda_1} {v_1} \sin{\left({\alpha} \right)} \cos^{2}{\left({\alpha} \right)} + 3 {\lambda_2} {v_2} \cos^{3}{\left({\alpha} \right)} - 3 {\lambda_2} {v_2} \cos{\left({\alpha} \right)} - 3 {\lambda_3} {v_1} \sin{\left({\alpha} \right)} \cos^{2}{\left({\alpha} \right)} + {\lambda_3} {v_1} \sin{\left({\alpha} \right)} - 3 {\lambda_3} {v_2} \cos^{3}{\left({\alpha} \right)} + 2 {\lambda_3} {v_2} \cos{\left({\alpha} \right)} - 3 {\lambda_4} {v_1} \sin{\left({\alpha} \right)} \cos^{2}{\left({\alpha} \right)} + {\lambda_4} {v_1} \sin{\left({\alpha} \right)} - 3 {\lambda_4} {v_2} \cos^{3}{\left({\alpha} \right)} + 2 {\lambda_4} {v_2} \cos{\left({\alpha} \right)} - 3 {\lambda_5} {v_1} \sin{\left({\alpha} \right)} \cos^{2}{\left({\alpha} \right)} + {\lambda_5} {v_1} \sin{\left({\alpha} \right)} - 3 {\lambda_5} {v_2} \cos^{3}{\left({\alpha} \right)} + 2 {\lambda_5} {v_2} \cos{\left({\alpha} \right)}\right)
```

$`H H^- H^+`$

```math
i \left(- {\lambda_1} {v_1} \sin^{2}{\left({\beta} \right)} \cos{\left({\alpha} \right)} - {\lambda_2} {v_2} \sin{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} - {\lambda_3} {v_1} \cos{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} - {\lambda_3} {v_2} \sin{\left({\alpha} \right)} \sin^{2}{\left({\beta} \right)} + \frac{{\lambda_4} {v_1} \left(\cos{\left({\alpha} - 2 {\beta} \right)} - \cos{\left({\alpha} + 2 {\beta} \right)}\right)}{4} + \frac{{\lambda_4} {v_2} \left(- \sin{\left({\alpha} - 2 {\beta} \right)} + \sin{\left({\alpha} + 2 {\beta} \right)}\right)}{4} + \frac{{\lambda_5} {v_1} \left(\cos{\left({\alpha} - 2 {\beta} \right)} - \cos{\left({\alpha} + 2 {\beta} \right)}\right)}{4} + \frac{{\lambda_5} {v_2} \left(- \sin{\left({\alpha} - 2 {\beta} \right)} + \sin{\left({\alpha} + 2 {\beta} \right)}\right)}{4}\right)
```

$`H h h`$

```math
i \left(- 3 {\lambda_1} {v_1} \sin^{2}{\left({\alpha} \right)} \cos{\left({\alpha} \right)} + 3 {\lambda_2} {v_2} \sin^{3}{\left({\alpha} \right)} - 3 {\lambda_2} {v_2} \sin{\left({\alpha} \right)} + 3 {\lambda_3} {v_1} \sin^{2}{\left({\alpha} \right)} \cos{\left({\alpha} \right)} - {\lambda_3} {v_1} \cos{\left({\alpha} \right)} - 3 {\lambda_3} {v_2} \sin^{3}{\left({\alpha} \right)} + 2 {\lambda_3} {v_2} \sin{\left({\alpha} \right)} + 3 {\lambda_4} {v_1} \sin^{2}{\left({\alpha} \right)} \cos{\left({\alpha} \right)} - {\lambda_4} {v_1} \cos{\left({\alpha} \right)} - 3 {\lambda_4} {v_2} \sin^{3}{\left({\alpha} \right)} + 2 {\lambda_4} {v_2} \sin{\left({\alpha} \right)} + 3 {\lambda_5} {v_1} \sin^{2}{\left({\alpha} \right)} \cos{\left({\alpha} \right)} - {\lambda_5} {v_1} \cos{\left({\alpha} \right)} - 3 {\lambda_5} {v_2} \sin^{3}{\left({\alpha} \right)} + 2 {\lambda_5} {v_2} \sin{\left({\alpha} \right)}\right)
```

$`H^- H^+ h`$

```math
i \left({\lambda_1} {v_1} \sin{\left({\alpha} \right)} \sin^{2}{\left({\beta} \right)} - {\lambda_2} {v_2} \cos{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} + {\lambda_3} {v_1} \sin{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} - {\lambda_3} {v_2} \sin^{2}{\left({\beta} \right)} \cos{\left({\alpha} \right)} + \frac{{\lambda_4} {v_1} \left(- \sin{\left({\alpha} - 2 {\beta} \right)} + \sin{\left({\alpha} + 2 {\beta} \right)}\right)}{4} - \frac{{\lambda_4} {v_2} \left(\cos{\left({\alpha} - 2 {\beta} \right)} - \cos{\left({\alpha} + 2 {\beta} \right)}\right)}{4} + \frac{{\lambda_5} {v_1} \left(- \sin{\left({\alpha} - 2 {\beta} \right)} + \sin{\left({\alpha} + 2 {\beta} \right)}\right)}{4} - \frac{{\lambda_5} {v_2} \left(\cos{\left({\alpha} - 2 {\beta} \right)} - \cos{\left({\alpha} + 2 {\beta} \right)}\right)}{4}\right)
```

$`h h h`$

```math
3 i \left({\lambda_1} {v_1} \sin^{3}{\left({\alpha} \right)} - {\lambda_2} {v_2} \cos^{3}{\left({\alpha} \right)} + {\lambda_3} {v_1} \sin{\left({\alpha} \right)} \cos^{2}{\left({\alpha} \right)} - {\lambda_3} {v_2} \sin^{2}{\left({\alpha} \right)} \cos{\left({\alpha} \right)} + {\lambda_4} {v_1} \sin{\left({\alpha} \right)} \cos^{2}{\left({\alpha} \right)} - {\lambda_4} {v_2} \sin^{2}{\left({\alpha} \right)} \cos{\left({\alpha} \right)} + {\lambda_5} {v_1} \sin{\left({\alpha} \right)} \cos^{2}{\left({\alpha} \right)} - {\lambda_5} {v_2} \sin^{2}{\left({\alpha} \right)} \cos{\left({\alpha} \right)}\right)
```

### Quartic scalar (SSSS): 14 vertices

$`A A A A`$

```math
3 i \left(- {\lambda_1} \sin^{4}{\left({\beta} \right)} - {\lambda_2} \cos^{4}{\left({\beta} \right)} - \frac{{\lambda_3} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{4} - \frac{{\lambda_4} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{4} - \frac{{\lambda_5} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{4}\right)
```

$`A A H H`$

```math
i \left(- {\lambda_1} \sin^{2}{\left({\beta} \right)} \cos^{2}{\left({\alpha} \right)} - {\lambda_2} \sin^{2}{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} - {\lambda_3} \sin^{2}{\left({\alpha} \right)} \sin^{2}{\left({\beta} \right)} - {\lambda_3} \cos^{2}{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} - {\lambda_4} \sin^{2}{\left({\alpha} \right)} \sin^{2}{\left({\beta} \right)} - {\lambda_4} \cos^{2}{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} + \frac{{\lambda_5} \left(\cos{\left(2 {\alpha} - 2 {\beta} \right)} - \cos{\left(2 {\alpha} + 2 {\beta} \right)}\right)}{2} + {\lambda_5} \sin^{2}{\left({\alpha} \right)} \sin^{2}{\left({\beta} \right)} + {\lambda_5} \cos^{2}{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)}\right)
```

$`A A H h`$

```math
\frac{i \left(2 {\lambda_1} \sin{\left(2 {\alpha} \right)} - {\lambda_1} \sin{\left(2 {\alpha} - 2 {\beta} \right)} - {\lambda_1} \sin{\left(2 {\alpha} + 2 {\beta} \right)} - 2 {\lambda_2} \sin{\left(2 {\alpha} \right)} - {\lambda_2} \sin{\left(2 {\alpha} - 2 {\beta} \right)} - {\lambda_2} \sin{\left(2 {\alpha} + 2 {\beta} \right)} + 2 {\lambda_3} \sin{\left(2 {\alpha} - 2 {\beta} \right)} + 2 {\lambda_3} \sin{\left(2 {\alpha} + 2 {\beta} \right)} + 2 {\lambda_4} \sin{\left(2 {\alpha} - 2 {\beta} \right)} + 2 {\lambda_4} \sin{\left(2 {\alpha} + 2 {\beta} \right)} - 6 {\lambda_5} \sin{\left(2 {\alpha} - 2 {\beta} \right)} + 2 {\lambda_5} \sin{\left(2 {\alpha} + 2 {\beta} \right)}\right)}{8}
```

$`A A H^- H^+`$

```math
i \left(- {\lambda_1} \sin^{4}{\left({\beta} \right)} - {\lambda_2} \cos^{4}{\left({\beta} \right)} - \frac{{\lambda_3} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{4} - \frac{{\lambda_4} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{4} - \frac{{\lambda_5} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{4}\right)
```

$`A A h h`$

```math
i \left(- {\lambda_1} \sin^{2}{\left({\alpha} \right)} \sin^{2}{\left({\beta} \right)} - {\lambda_2} \cos^{2}{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} - {\lambda_3} \sin^{2}{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} - {\lambda_3} \sin^{2}{\left({\beta} \right)} \cos^{2}{\left({\alpha} \right)} - {\lambda_4} \sin^{2}{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} - {\lambda_4} \sin^{2}{\left({\beta} \right)} \cos^{2}{\left({\alpha} \right)} - \frac{{\lambda_5} \left(\cos{\left(2 {\alpha} - 2 {\beta} \right)} - \cos{\left(2 {\alpha} + 2 {\beta} \right)}\right)}{2} + {\lambda_5} \sin^{2}{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} + {\lambda_5} \sin^{2}{\left({\beta} \right)} \cos^{2}{\left({\alpha} \right)}\right)
```

$`H H H H`$

```math
3 i \left(- {\lambda_1} \cos^{4}{\left({\alpha} \right)} - {\lambda_2} \sin^{4}{\left({\alpha} \right)} - \frac{{\lambda_3} \left(1 - \cos{\left(4 {\alpha} \right)}\right)}{4} - \frac{{\lambda_4} \left(1 - \cos{\left(4 {\alpha} \right)}\right)}{4} - \frac{{\lambda_5} \left(1 - \cos{\left(4 {\alpha} \right)}\right)}{4}\right)
```

$`H H H h`$

```math
3 i \left({\lambda_1} \cos^{2}{\left({\alpha} \right)} + {\lambda_2} \cos^{2}{\left({\alpha} \right)} - {\lambda_2} - 2 {\lambda_3} \cos^{2}{\left({\alpha} \right)} + {\lambda_3} - 2 {\lambda_4} \cos^{2}{\left({\alpha} \right)} + {\lambda_4} - 2 {\lambda_5} \cos^{2}{\left({\alpha} \right)} + {\lambda_5}\right) \sin{\left({\alpha} \right)} \cos{\left({\alpha} \right)}
```

$`H H H^- H^+`$

```math
i \left(- {\lambda_1} \sin^{2}{\left({\beta} \right)} \cos^{2}{\left({\alpha} \right)} - {\lambda_2} \sin^{2}{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} - {\lambda_3} \sin^{2}{\left({\alpha} \right)} \sin^{2}{\left({\beta} \right)} - {\lambda_3} \cos^{2}{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} + \frac{{\lambda_4} \left(\cos{\left(2 {\alpha} - 2 {\beta} \right)} - \cos{\left(2 {\alpha} + 2 {\beta} \right)}\right)}{4} + \frac{{\lambda_5} \left(\cos{\left(2 {\alpha} - 2 {\beta} \right)} - \cos{\left(2 {\alpha} + 2 {\beta} \right)}\right)}{4}\right)
```

$`H H h h`$

```math
i \left(3 {\lambda_1} \sin^{4}{\left({\alpha} \right)} - 3 {\lambda_1} \sin^{2}{\left({\alpha} \right)} + 3 {\lambda_2} \sin^{4}{\left({\alpha} \right)} - 3 {\lambda_2} \sin^{2}{\left({\alpha} \right)} - 6 {\lambda_3} \sin^{4}{\left({\alpha} \right)} + 6 {\lambda_3} \sin^{2}{\left({\alpha} \right)} - {\lambda_3} - 6 {\lambda_4} \sin^{4}{\left({\alpha} \right)} + 6 {\lambda_4} \sin^{2}{\left({\alpha} \right)} - {\lambda_4} - 6 {\lambda_5} \sin^{4}{\left({\alpha} \right)} + 6 {\lambda_5} \sin^{2}{\left({\alpha} \right)} - {\lambda_5}\right)
```

$`H H^- H^+ h`$

```math
\frac{i \left(2 {\lambda_1} \sin{\left(2 {\alpha} \right)} - {\lambda_1} \sin{\left(2 {\alpha} - 2 {\beta} \right)} - {\lambda_1} \sin{\left(2 {\alpha} + 2 {\beta} \right)} - 2 {\lambda_2} \sin{\left(2 {\alpha} \right)} - {\lambda_2} \sin{\left(2 {\alpha} - 2 {\beta} \right)} - {\lambda_2} \sin{\left(2 {\alpha} + 2 {\beta} \right)} + 2 {\lambda_3} \sin{\left(2 {\alpha} - 2 {\beta} \right)} + 2 {\lambda_3} \sin{\left(2 {\alpha} + 2 {\beta} \right)} - 2 {\lambda_4} \sin{\left(2 {\alpha} - 2 {\beta} \right)} + 2 {\lambda_4} \sin{\left(2 {\alpha} + 2 {\beta} \right)} - 2 {\lambda_5} \sin{\left(2 {\alpha} - 2 {\beta} \right)} + 2 {\lambda_5} \sin{\left(2 {\alpha} + 2 {\beta} \right)}\right)}{8}
```

$`H h h h`$

```math
3 i \left({\lambda_1} \sin^{2}{\left({\alpha} \right)} + {\lambda_2} \sin^{2}{\left({\alpha} \right)} - {\lambda_2} - 2 {\lambda_3} \sin^{2}{\left({\alpha} \right)} + {\lambda_3} - 2 {\lambda_4} \sin^{2}{\left({\alpha} \right)} + {\lambda_4} - 2 {\lambda_5} \sin^{2}{\left({\alpha} \right)} + {\lambda_5}\right) \sin{\left({\alpha} \right)} \cos{\left({\alpha} \right)}
```

$`H^- H^- H^+ H^+`$

```math
2 i \left(- {\lambda_1} \sin^{4}{\left({\beta} \right)} - {\lambda_2} \cos^{4}{\left({\beta} \right)} - \frac{{\lambda_3} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{4} - \frac{{\lambda_4} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{4} - \frac{{\lambda_5} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{4}\right)
```

$`H^- H^+ h h`$

```math
i \left(- {\lambda_1} \sin^{2}{\left({\alpha} \right)} \sin^{2}{\left({\beta} \right)} - {\lambda_2} \cos^{2}{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} - {\lambda_3} \sin^{2}{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} - {\lambda_3} \sin^{2}{\left({\beta} \right)} \cos^{2}{\left({\alpha} \right)} - \frac{{\lambda_4} \left(\cos{\left(2 {\alpha} - 2 {\beta} \right)} - \cos{\left(2 {\alpha} + 2 {\beta} \right)}\right)}{4} - \frac{{\lambda_5} \left(\cos{\left(2 {\alpha} - 2 {\beta} \right)} - \cos{\left(2 {\alpha} + 2 {\beta} \right)}\right)}{4}\right)
```

$`h h h h`$

```math
3 i \left(- {\lambda_1} \sin^{4}{\left({\alpha} \right)} - {\lambda_2} \cos^{4}{\left({\alpha} \right)} - \frac{{\lambda_3} \left(1 - \cos{\left(4 {\alpha} \right)}\right)}{4} - \frac{{\lambda_4} \left(1 - \cos{\left(4 {\alpha} \right)}\right)}{4} - \frac{{\lambda_5} \left(1 - \cos{\left(4 {\alpha} \right)}\right)}{4}\right)
```

### Vector and two scalars (VSS): 10 vertices

| interaction | Feynman rule |
|---|---|
| $`\gamma H^- H^+`$ | $`\frac{i {g'} {g} \left({p_{H^-}} - {p_{H^+}}\right)}{\sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`W^+ A H^-`$ | $`\frac{{g} \left({p_{A}} - {p_{H^-}}\right)}{2}`$ |
| $`W^- A H^+`$ | $`\frac{{g} \left({p_{A}} - {p_{H^+}}\right)}{2}`$ |
| $`W^+ H H^-`$ | $`\frac{i {g} \left(- {p_{H}} + {p_{H^-}}\right) \sin{\left({\alpha} - {\beta} \right)}}{2}`$ |
| $`W^- H H^+`$ | $`\frac{i {g} \left({p_{H}} - {p_{H^+}}\right) \sin{\left({\alpha} - {\beta} \right)}}{2}`$ |
| $`Z H^- H^+`$ | $`\frac{i \left(- {g'}^{2} {p_{H^-}} + {g'}^{2} {p_{H^+}} + {g}^{2} {p_{H^-}} - {g}^{2} {p_{H^+}}\right)}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`W^+ H^- h`$ | $`\frac{i {g} \left({p_{H^-}} - {p_{h}}\right) \cos{\left({\alpha} - {\beta} \right)}}{2}`$ |
| $`W^- H^+ h`$ | $`\frac{i {g} \left(- {p_{H^+}} + {p_{h}}\right) \cos{\left({\alpha} - {\beta} \right)}}{2}`$ |

$`Z A H`$

```math
\frac{\left(- {g'}^{2} {p_{A}} + {g'}^{2} {p_{H}} - {g}^{2} {p_{A}} + {g}^{2} {p_{H}}\right) \sin{\left({\alpha} - {\beta} \right)}}{2 \sqrt{{g'}^{2} + {g}^{2}}}
```

$`Z A h`$

```math
\frac{\left(- {g'}^{2} {p_{A}} + {g'}^{2} {p_{h}} - {g}^{2} {p_{A}} + {g}^{2} {p_{h}}\right) \cos{\left({\alpha} - {\beta} \right)}}{2 \sqrt{{g'}^{2} + {g}^{2}}}
```

### Two vectors and a scalar (VVS): 8 vertices

| interaction | Feynman rule |
|---|---|
| $`\gamma W^+ H^-`$ | $`\frac{i {g'} {g}^{2} \left(- {v_1} \sin{\left({\beta} \right)} + {v_2} \cos{\left({\beta} \right)}\right)}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`\gamma W^- H^+`$ | $`\frac{i {g'} {g}^{2} \left(- {v_1} \sin{\left({\beta} \right)} + {v_2} \cos{\left({\beta} \right)}\right)}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`W^- W^+ H`$ | $`\frac{i {g}^{2} \left({v_1} \cos{\left({\alpha} \right)} + {v_2} \sin{\left({\alpha} \right)}\right)}{2}`$ |
| $`W^+ Z H^-`$ | $`\frac{i {g'}^{2} {g} \left({v_1} \sin{\left({\beta} \right)} - {v_2} \cos{\left({\beta} \right)}\right)}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`W^- Z H^+`$ | $`\frac{i {g'}^{2} {g} \left({v_1} \sin{\left({\beta} \right)} - {v_2} \cos{\left({\beta} \right)}\right)}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`W^- W^+ h`$ | $`\frac{i {g}^{2} \left(- {v_1} \sin{\left({\alpha} \right)} + {v_2} \cos{\left({\alpha} \right)}\right)}{2}`$ |

$`Z Z H`$

```math
\frac{i \left({g'}^{2} {v_1} \cos{\left({\alpha} \right)} + {g'}^{2} {v_2} \sin{\left({\alpha} \right)} + {g}^{2} {v_1} \cos{\left({\alpha} \right)} + {g}^{2} {v_2} \sin{\left({\alpha} \right)}\right)}{2}
```

$`Z Z h`$

```math
\frac{i \left(- {g'}^{2} {v_1} \sin{\left({\alpha} \right)} + {g'}^{2} {v_2} \cos{\left({\alpha} \right)} - {g}^{2} {v_1} \sin{\left({\alpha} \right)} + {g}^{2} {v_2} \cos{\left({\alpha} \right)}\right)}{2}
```

### Two vectors and two scalars (VVSS): 22 vertices

| interaction | Feynman rule |
|---|---|
| $`\gamma \gamma H^- H^+`$ | $`\frac{2 i {g'}^{2} {g}^{2}}{{g'}^{2} + {g}^{2}}`$ |
| $`\gamma W^+ A H^-`$ | $`- \frac{{g'} {g}^{2}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`\gamma W^- A H^+`$ | $`\frac{{g'} {g}^{2}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`\gamma W^+ H H^-`$ | $`\frac{i {g'} {g}^{2} \sin{\left({\alpha} - {\beta} \right)}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`\gamma W^- H H^+`$ | $`\frac{i {g'} {g}^{2} \sin{\left({\alpha} - {\beta} \right)}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`\gamma Z H^- H^+`$ | $`\frac{i {g'} {g} \left(- {g'}^{2} + {g}^{2}\right)}{{g'}^{2} + {g}^{2}}`$ |
| $`\gamma W^+ H^- h`$ | $`\frac{i {g'} {g}^{2} \cos{\left({\alpha} - {\beta} \right)}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`\gamma W^- H^+ h`$ | $`\frac{i {g'} {g}^{2} \cos{\left({\alpha} - {\beta} \right)}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`W^- W^+ A A`$ | $`\frac{i {g}^{2}}{2}`$ |
| $`Z Z A A`$ | $`\frac{i \left({g'}^{2} + {g}^{2}\right)}{2}`$ |
| $`W^+ Z A H^-`$ | $`\frac{{g'}^{2} {g}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`W^- Z A H^+`$ | $`- \frac{{g'}^{2} {g}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`W^- W^+ H H`$ | $`\frac{i {g}^{2}}{2}`$ |
| $`Z Z H H`$ | $`\frac{i \left({g'}^{2} + {g}^{2}\right)}{2}`$ |
| $`W^+ Z H H^-`$ | $`- \frac{i {g'}^{2} {g} \sin{\left({\alpha} - {\beta} \right)}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`W^- Z H H^+`$ | $`- \frac{i {g'}^{2} {g} \sin{\left({\alpha} - {\beta} \right)}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`W^- W^+ H^- H^+`$ | $`\frac{i {g}^{2}}{2}`$ |
| $`Z Z H^- H^+`$ | $`\frac{i \left({g'} - {g}\right)^{2} \left({g'} + {g}\right)^{2}}{2 \left({g'}^{2} + {g}^{2}\right)}`$ |
| $`W^+ Z H^- h`$ | $`- \frac{i {g'}^{2} {g} \cos{\left({\alpha} - {\beta} \right)}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`W^- Z H^+ h`$ | $`- \frac{i {g'}^{2} {g} \cos{\left({\alpha} - {\beta} \right)}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`W^- W^+ h h`$ | $`\frac{i {g}^{2}}{2}`$ |
| $`Z Z h h`$ | $`\frac{i \left({g'}^{2} + {g}^{2}\right)}{2}`$ |

### Feynman-gauge vertices with a Goldstone leg: 92 in all

The unitary-gauge UFO drops these; they matter for a Feynman-gauge calculation.

#### Cubic scalar (SSS): 14 vertices

$`A G^0 H`$

```math
\frac{i \left(- {\lambda_1} {v_1} \sin{\left({\alpha} - 2 {\beta} \right)} + {\lambda_1} {v_1} \sin{\left({\alpha} + 2 {\beta} \right)} - {\lambda_2} {v_2} \cos{\left({\alpha} - 2 {\beta} \right)} + {\lambda_2} {v_2} \cos{\left({\alpha} + 2 {\beta} \right)} + {\lambda_3} {v_1} \sin{\left({\alpha} - 2 {\beta} \right)} - {\lambda_3} {v_1} \sin{\left({\alpha} + 2 {\beta} \right)} + {\lambda_3} {v_2} \cos{\left({\alpha} - 2 {\beta} \right)} - {\lambda_3} {v_2} \cos{\left({\alpha} + 2 {\beta} \right)} + {\lambda_4} {v_1} \sin{\left({\alpha} - 2 {\beta} \right)} - {\lambda_4} {v_1} \sin{\left({\alpha} + 2 {\beta} \right)} + {\lambda_4} {v_2} \cos{\left({\alpha} - 2 {\beta} \right)} - {\lambda_4} {v_2} \cos{\left({\alpha} + 2 {\beta} \right)} - 3 {\lambda_5} {v_1} \sin{\left({\alpha} - 2 {\beta} \right)} - {\lambda_5} {v_1} \sin{\left({\alpha} + 2 {\beta} \right)} - 3 {\lambda_5} {v_2} \cos{\left({\alpha} - 2 {\beta} \right)} - {\lambda_5} {v_2} \cos{\left({\alpha} + 2 {\beta} \right)}\right)}{4}
```

$`A G^0 h`$

```math
\frac{i \left(- {\lambda_1} {v_1} \cos{\left({\alpha} - 2 {\beta} \right)} + {\lambda_1} {v_1} \cos{\left({\alpha} + 2 {\beta} \right)} + {\lambda_2} {v_2} \sin{\left({\alpha} - 2 {\beta} \right)} - {\lambda_2} {v_2} \sin{\left({\alpha} + 2 {\beta} \right)} + {\lambda_3} {v_1} \cos{\left({\alpha} - 2 {\beta} \right)} - {\lambda_3} {v_1} \cos{\left({\alpha} + 2 {\beta} \right)} - {\lambda_3} {v_2} \sin{\left({\alpha} - 2 {\beta} \right)} + {\lambda_3} {v_2} \sin{\left({\alpha} + 2 {\beta} \right)} + {\lambda_4} {v_1} \cos{\left({\alpha} - 2 {\beta} \right)} - {\lambda_4} {v_1} \cos{\left({\alpha} + 2 {\beta} \right)} - {\lambda_4} {v_2} \sin{\left({\alpha} - 2 {\beta} \right)} + {\lambda_4} {v_2} \sin{\left({\alpha} + 2 {\beta} \right)} - 3 {\lambda_5} {v_1} \cos{\left({\alpha} - 2 {\beta} \right)} - {\lambda_5} {v_1} \cos{\left({\alpha} + 2 {\beta} \right)} + 3 {\lambda_5} {v_2} \sin{\left({\alpha} - 2 {\beta} \right)} + {\lambda_5} {v_2} \sin{\left({\alpha} + 2 {\beta} \right)}\right)}{4}
```

$`A G^- H^+`$

```math
- \frac{{\lambda_4} {v_1} \cos{\left({\beta} \right)}}{2} - \frac{{\lambda_4} {v_2} \sin{\left({\beta} \right)}}{2} + \frac{{\lambda_5} {v_1} \cos{\left({\beta} \right)}}{2} + \frac{{\lambda_5} {v_2} \sin{\left({\beta} \right)}}{2}
```

$`A G^+ H^-`$

```math
\frac{{\lambda_4} {v_1} \cos{\left({\beta} \right)}}{2} + \frac{{\lambda_4} {v_2} \sin{\left({\beta} \right)}}{2} - \frac{{\lambda_5} {v_1} \cos{\left({\beta} \right)}}{2} - \frac{{\lambda_5} {v_2} \sin{\left({\beta} \right)}}{2}
```

$`G^0 G^0 H`$

```math
i \left(- {\lambda_1} {v_1} \cos{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} - {\lambda_2} {v_2} \sin{\left({\alpha} \right)} \sin^{2}{\left({\beta} \right)} - {\lambda_3} {v_1} \sin^{2}{\left({\beta} \right)} \cos{\left({\alpha} \right)} - {\lambda_3} {v_2} \sin{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} - {\lambda_4} {v_1} \sin^{2}{\left({\beta} \right)} \cos{\left({\alpha} \right)} - {\lambda_4} {v_2} \sin{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} - \frac{{\lambda_5} {v_1} \left(\cos{\left({\alpha} - 2 {\beta} \right)} - \cos{\left({\alpha} + 2 {\beta} \right)}\right)}{2} + {\lambda_5} {v_1} \sin^{2}{\left({\beta} \right)} \cos{\left({\alpha} \right)} - \frac{{\lambda_5} {v_2} \left(- \sin{\left({\alpha} - 2 {\beta} \right)} + \sin{\left({\alpha} + 2 {\beta} \right)}\right)}{2} + {\lambda_5} {v_2} \sin{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)}\right)
```

$`G^0 G^0 h`$

```math
i \left({\lambda_1} {v_1} \sin{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} - {\lambda_2} {v_2} \sin^{2}{\left({\beta} \right)} \cos{\left({\alpha} \right)} + {\lambda_3} {v_1} \sin{\left({\alpha} \right)} \sin^{2}{\left({\beta} \right)} - {\lambda_3} {v_2} \cos{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} + {\lambda_4} {v_1} \sin{\left({\alpha} \right)} \sin^{2}{\left({\beta} \right)} - {\lambda_4} {v_2} \cos{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} - \frac{{\lambda_5} {v_1} \left(- \sin{\left({\alpha} - 2 {\beta} \right)} + \sin{\left({\alpha} + 2 {\beta} \right)}\right)}{2} - {\lambda_5} {v_1} \sin{\left({\alpha} \right)} \sin^{2}{\left({\beta} \right)} + \frac{{\lambda_5} {v_2} \left(\cos{\left({\alpha} - 2 {\beta} \right)} - \cos{\left({\alpha} + 2 {\beta} \right)}\right)}{2} + {\lambda_5} {v_2} \cos{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)}\right)
```

$`G^0 G^- H^+`$

```math
- \frac{{\lambda_4} {v_1} \sin{\left({\beta} \right)}}{2} + \frac{{\lambda_4} {v_2} \cos{\left({\beta} \right)}}{2} + \frac{{\lambda_5} {v_1} \sin{\left({\beta} \right)}}{2} - \frac{{\lambda_5} {v_2} \cos{\left({\beta} \right)}}{2}
```

$`G^0 G^+ H^-`$

```math
\frac{{\lambda_4} {v_1} \sin{\left({\beta} \right)}}{2} - \frac{{\lambda_4} {v_2} \cos{\left({\beta} \right)}}{2} - \frac{{\lambda_5} {v_1} \sin{\left({\beta} \right)}}{2} + \frac{{\lambda_5} {v_2} \cos{\left({\beta} \right)}}{2}
```

$`G^- G^+ H`$

```math
i \left(- {\lambda_1} {v_1} \cos{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} - {\lambda_2} {v_2} \sin{\left({\alpha} \right)} \sin^{2}{\left({\beta} \right)} - {\lambda_3} {v_1} \sin^{2}{\left({\beta} \right)} \cos{\left({\alpha} \right)} - {\lambda_3} {v_2} \sin{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} - \frac{{\lambda_4} {v_1} \left(\cos{\left({\alpha} - 2 {\beta} \right)} - \cos{\left({\alpha} + 2 {\beta} \right)}\right)}{4} - \frac{{\lambda_4} {v_2} \left(- \sin{\left({\alpha} - 2 {\beta} \right)} + \sin{\left({\alpha} + 2 {\beta} \right)}\right)}{4} - \frac{{\lambda_5} {v_1} \left(\cos{\left({\alpha} - 2 {\beta} \right)} - \cos{\left({\alpha} + 2 {\beta} \right)}\right)}{4} - \frac{{\lambda_5} {v_2} \left(- \sin{\left({\alpha} - 2 {\beta} \right)} + \sin{\left({\alpha} + 2 {\beta} \right)}\right)}{4}\right)
```

$`G^- G^+ h`$

```math
i \left({\lambda_1} {v_1} \sin{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} - {\lambda_2} {v_2} \sin^{2}{\left({\beta} \right)} \cos{\left({\alpha} \right)} + {\lambda_3} {v_1} \sin{\left({\alpha} \right)} \sin^{2}{\left({\beta} \right)} - {\lambda_3} {v_2} \cos{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} - \frac{{\lambda_4} {v_1} \left(- \sin{\left({\alpha} - 2 {\beta} \right)} + \sin{\left({\alpha} + 2 {\beta} \right)}\right)}{4} + \frac{{\lambda_4} {v_2} \left(\cos{\left({\alpha} - 2 {\beta} \right)} - \cos{\left({\alpha} + 2 {\beta} \right)}\right)}{4} - \frac{{\lambda_5} {v_1} \left(- \sin{\left({\alpha} - 2 {\beta} \right)} + \sin{\left({\alpha} + 2 {\beta} \right)}\right)}{4} + \frac{{\lambda_5} {v_2} \left(\cos{\left({\alpha} - 2 {\beta} \right)} - \cos{\left({\alpha} + 2 {\beta} \right)}\right)}{4}\right)
```

$`G^- H H^+`$

```math
i \left({\lambda_1} {v_1} \sin{\left({\beta} \right)} \cos{\left({\alpha} \right)} \cos{\left({\beta} \right)} - {\lambda_2} {v_2} \sin{\left({\alpha} \right)} \sin{\left({\beta} \right)} \cos{\left({\beta} \right)} - {\lambda_3} {v_1} \sin{\left({\beta} \right)} \cos{\left({\alpha} \right)} \cos{\left({\beta} \right)} + {\lambda_3} {v_2} \sin{\left({\alpha} \right)} \sin{\left({\beta} \right)} \cos{\left({\beta} \right)} - {\lambda_4} {v_1} \sin{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} + \frac{{\lambda_4} {v_1} \sin{\left({\alpha} \right)}}{2} - {\lambda_4} {v_2} \cos{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} + \frac{{\lambda_4} {v_2} \cos{\left({\alpha} \right)}}{2} - {\lambda_5} {v_1} \sin{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} + \frac{{\lambda_5} {v_1} \sin{\left({\alpha} \right)}}{2} - {\lambda_5} {v_2} \cos{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} + \frac{{\lambda_5} {v_2} \cos{\left({\alpha} \right)}}{2}\right)
```

$`G^- H^+ h`$

```math
i \left(- {\lambda_1} {v_1} \sin{\left({\alpha} \right)} \sin{\left({\beta} \right)} \cos{\left({\beta} \right)} - {\lambda_2} {v_2} \sin{\left({\beta} \right)} \cos{\left({\alpha} \right)} \cos{\left({\beta} \right)} + {\lambda_3} {v_1} \sin{\left({\alpha} \right)} \sin{\left({\beta} \right)} \cos{\left({\beta} \right)} + {\lambda_3} {v_2} \sin{\left({\beta} \right)} \cos{\left({\alpha} \right)} \cos{\left({\beta} \right)} + {\lambda_4} {v_1} \sin^{2}{\left({\beta} \right)} \cos{\left({\alpha} \right)} - \frac{{\lambda_4} {v_1} \cos{\left({\alpha} \right)}}{2} - {\lambda_4} {v_2} \sin{\left({\alpha} \right)} \sin^{2}{\left({\beta} \right)} + \frac{{\lambda_4} {v_2} \sin{\left({\alpha} \right)}}{2} + {\lambda_5} {v_1} \sin^{2}{\left({\beta} \right)} \cos{\left({\alpha} \right)} - \frac{{\lambda_5} {v_1} \cos{\left({\alpha} \right)}}{2} - {\lambda_5} {v_2} \sin{\left({\alpha} \right)} \sin^{2}{\left({\beta} \right)} + \frac{{\lambda_5} {v_2} \sin{\left({\alpha} \right)}}{2}\right)
```

$`G^+ H H^-`$

```math
i \left({\lambda_1} {v_1} \sin{\left({\beta} \right)} \cos{\left({\alpha} \right)} \cos{\left({\beta} \right)} - {\lambda_2} {v_2} \sin{\left({\alpha} \right)} \sin{\left({\beta} \right)} \cos{\left({\beta} \right)} - {\lambda_3} {v_1} \sin{\left({\beta} \right)} \cos{\left({\alpha} \right)} \cos{\left({\beta} \right)} + {\lambda_3} {v_2} \sin{\left({\alpha} \right)} \sin{\left({\beta} \right)} \cos{\left({\beta} \right)} - {\lambda_4} {v_1} \sin{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} + \frac{{\lambda_4} {v_1} \sin{\left({\alpha} \right)}}{2} - {\lambda_4} {v_2} \cos{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} + \frac{{\lambda_4} {v_2} \cos{\left({\alpha} \right)}}{2} - {\lambda_5} {v_1} \sin{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} + \frac{{\lambda_5} {v_1} \sin{\left({\alpha} \right)}}{2} - {\lambda_5} {v_2} \cos{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} + \frac{{\lambda_5} {v_2} \cos{\left({\alpha} \right)}}{2}\right)
```

$`G^+ H^- h`$

```math
i \left(- {\lambda_1} {v_1} \sin{\left({\alpha} \right)} \sin{\left({\beta} \right)} \cos{\left({\beta} \right)} - {\lambda_2} {v_2} \sin{\left({\beta} \right)} \cos{\left({\alpha} \right)} \cos{\left({\beta} \right)} + {\lambda_3} {v_1} \sin{\left({\alpha} \right)} \sin{\left({\beta} \right)} \cos{\left({\beta} \right)} + {\lambda_3} {v_2} \sin{\left({\beta} \right)} \cos{\left({\alpha} \right)} \cos{\left({\beta} \right)} + {\lambda_4} {v_1} \sin^{2}{\left({\beta} \right)} \cos{\left({\alpha} \right)} - \frac{{\lambda_4} {v_1} \cos{\left({\alpha} \right)}}{2} - {\lambda_4} {v_2} \sin{\left({\alpha} \right)} \sin^{2}{\left({\beta} \right)} + \frac{{\lambda_4} {v_2} \sin{\left({\alpha} \right)}}{2} + {\lambda_5} {v_1} \sin^{2}{\left({\beta} \right)} \cos{\left({\alpha} \right)} - \frac{{\lambda_5} {v_1} \cos{\left({\alpha} \right)}}{2} - {\lambda_5} {v_2} \sin{\left({\alpha} \right)} \sin^{2}{\left({\beta} \right)} + \frac{{\lambda_5} {v_2} \sin{\left({\alpha} \right)}}{2}\right)
```

#### Quartic scalar (SSSS): 46 vertices

| interaction | Feynman rule |
|---|---|
| $`A G^- H H^+`$ | $`\frac{\left(- {\lambda_4} + {\lambda_5}\right) \cos{\left({\alpha} - {\beta} \right)}}{2}`$ |
| $`A G^- H^+ h`$ | $`\frac{\left({\lambda_4} - {\lambda_5}\right) \sin{\left({\alpha} - {\beta} \right)}}{2}`$ |
| $`A G^+ H H^-`$ | $`\frac{\left({\lambda_4} - {\lambda_5}\right) \cos{\left({\alpha} - {\beta} \right)}}{2}`$ |
| $`A G^+ H^- h`$ | $`\frac{\left(- {\lambda_4} + {\lambda_5}\right) \sin{\left({\alpha} - {\beta} \right)}}{2}`$ |
| $`G^0 G^- H H^+`$ | $`\frac{\left({\lambda_4} - {\lambda_5}\right) \sin{\left({\alpha} - {\beta} \right)}}{2}`$ |
| $`G^0 G^- H^+ h`$ | $`\frac{\left({\lambda_4} - {\lambda_5}\right) \cos{\left({\alpha} - {\beta} \right)}}{2}`$ |
| $`G^0 G^+ H H^-`$ | $`\frac{\left(- {\lambda_4} + {\lambda_5}\right) \sin{\left({\alpha} - {\beta} \right)}}{2}`$ |
| $`G^0 G^+ H^- h`$ | $`\frac{\left(- {\lambda_4} + {\lambda_5}\right) \cos{\left({\alpha} - {\beta} \right)}}{2}`$ |

$`A A A G^0`$

```math
3 i \left({\lambda_1} \sin^{2}{\left({\beta} \right)} + {\lambda_2} \sin^{2}{\left({\beta} \right)} - {\lambda_2} - 2 {\lambda_3} \sin^{2}{\left({\beta} \right)} + {\lambda_3} - 2 {\lambda_4} \sin^{2}{\left({\beta} \right)} + {\lambda_4} - 2 {\lambda_5} \sin^{2}{\left({\beta} \right)} + {\lambda_5}\right) \sin{\left({\beta} \right)} \cos{\left({\beta} \right)}
```

$`A A G^0 G^0`$

```math
i \left(3 {\lambda_1} \sin^{4}{\left({\beta} \right)} - 3 {\lambda_1} \sin^{2}{\left({\beta} \right)} + 3 {\lambda_2} \sin^{4}{\left({\beta} \right)} - 3 {\lambda_2} \sin^{2}{\left({\beta} \right)} - 6 {\lambda_3} \sin^{4}{\left({\beta} \right)} + 6 {\lambda_3} \sin^{2}{\left({\beta} \right)} - {\lambda_3} - 6 {\lambda_4} \sin^{4}{\left({\beta} \right)} + 6 {\lambda_4} \sin^{2}{\left({\beta} \right)} - {\lambda_4} - 6 {\lambda_5} \sin^{4}{\left({\beta} \right)} + 6 {\lambda_5} \sin^{2}{\left({\beta} \right)} - {\lambda_5}\right)
```

$`A A G^- G^+`$

```math
i \left(- \frac{{\lambda_1} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{8} - \frac{{\lambda_2} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{8} - {\lambda_3} \sin^{4}{\left({\beta} \right)} - {\lambda_3} \cos^{4}{\left({\beta} \right)} + \frac{{\lambda_4} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{4} + \frac{{\lambda_5} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{4}\right)
```

$`A A G^- H^+`$

```math
i \left({\lambda_1} \sin^{2}{\left({\beta} \right)} + {\lambda_2} \sin^{2}{\left({\beta} \right)} - {\lambda_2} - 2 {\lambda_3} \sin^{2}{\left({\beta} \right)} + {\lambda_3} - 2 {\lambda_4} \sin^{2}{\left({\beta} \right)} + {\lambda_4} - 2 {\lambda_5} \sin^{2}{\left({\beta} \right)} + {\lambda_5}\right) \sin{\left({\beta} \right)} \cos{\left({\beta} \right)}
```

$`A A G^+ H^-`$

```math
i \left({\lambda_1} \sin^{2}{\left({\beta} \right)} + {\lambda_2} \sin^{2}{\left({\beta} \right)} - {\lambda_2} - 2 {\lambda_3} \sin^{2}{\left({\beta} \right)} + {\lambda_3} - 2 {\lambda_4} \sin^{2}{\left({\beta} \right)} + {\lambda_4} - 2 {\lambda_5} \sin^{2}{\left({\beta} \right)} + {\lambda_5}\right) \sin{\left({\beta} \right)} \cos{\left({\beta} \right)}
```

$`A G^0 G^0 G^0`$

```math
3 i \left({\lambda_1} \cos^{2}{\left({\beta} \right)} + {\lambda_2} \cos^{2}{\left({\beta} \right)} - {\lambda_2} - 2 {\lambda_3} \cos^{2}{\left({\beta} \right)} + {\lambda_3} - 2 {\lambda_4} \cos^{2}{\left({\beta} \right)} + {\lambda_4} - 2 {\lambda_5} \cos^{2}{\left({\beta} \right)} + {\lambda_5}\right) \sin{\left({\beta} \right)} \cos{\left({\beta} \right)}
```

$`A G^0 G^- G^+`$

```math
i \left({\lambda_1} \cos^{2}{\left({\beta} \right)} + {\lambda_2} \cos^{2}{\left({\beta} \right)} - {\lambda_2} - 2 {\lambda_3} \cos^{2}{\left({\beta} \right)} + {\lambda_3} - 2 {\lambda_4} \cos^{2}{\left({\beta} \right)} + {\lambda_4} - 2 {\lambda_5} \cos^{2}{\left({\beta} \right)} + {\lambda_5}\right) \sin{\left({\beta} \right)} \cos{\left({\beta} \right)}
```

$`A G^0 G^- H^+`$

```math
\frac{i \left(- \frac{{\lambda_1} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{4} - \frac{{\lambda_2} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{4} + \frac{{\lambda_3} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{2} + \frac{{\lambda_4} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{4} - {\lambda_4} \sin^{4}{\left({\beta} \right)} - {\lambda_4} \cos^{4}{\left({\beta} \right)} + \frac{{\lambda_5} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{4} - {\lambda_5} \sin^{4}{\left({\beta} \right)} - {\lambda_5} \cos^{4}{\left({\beta} \right)}\right)}{2}
```

$`A G^0 G^+ H^-`$

```math
\frac{i \left(- \frac{{\lambda_1} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{4} - \frac{{\lambda_2} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{4} + \frac{{\lambda_3} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{2} + \frac{{\lambda_4} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{4} - {\lambda_4} \sin^{4}{\left({\beta} \right)} - {\lambda_4} \cos^{4}{\left({\beta} \right)} + \frac{{\lambda_5} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{4} - {\lambda_5} \sin^{4}{\left({\beta} \right)} - {\lambda_5} \cos^{4}{\left({\beta} \right)}\right)}{2}
```

$`A G^0 H H`$

```math
\frac{i \left(2 {\lambda_1} \sin{\left(2 {\beta} \right)} - {\lambda_1} \sin{\left(2 {\alpha} - 2 {\beta} \right)} + {\lambda_1} \sin{\left(2 {\alpha} + 2 {\beta} \right)} - 2 {\lambda_2} \sin{\left(2 {\beta} \right)} - {\lambda_2} \sin{\left(2 {\alpha} - 2 {\beta} \right)} + {\lambda_2} \sin{\left(2 {\alpha} + 2 {\beta} \right)} + 2 {\lambda_3} \sin{\left(2 {\alpha} - 2 {\beta} \right)} - 2 {\lambda_3} \sin{\left(2 {\alpha} + 2 {\beta} \right)} + 2 {\lambda_4} \sin{\left(2 {\alpha} - 2 {\beta} \right)} - 2 {\lambda_4} \sin{\left(2 {\alpha} + 2 {\beta} \right)} - 6 {\lambda_5} \sin{\left(2 {\alpha} - 2 {\beta} \right)} - 2 {\lambda_5} \sin{\left(2 {\alpha} + 2 {\beta} \right)}\right)}{8}
```

$`A G^0 H h`$

```math
\frac{i \left(- {\lambda_1} \cos{\left(2 {\alpha} - 2 {\beta} \right)} + {\lambda_1} \cos{\left(2 {\alpha} + 2 {\beta} \right)} - {\lambda_2} \cos{\left(2 {\alpha} - 2 {\beta} \right)} + {\lambda_2} \cos{\left(2 {\alpha} + 2 {\beta} \right)} + 2 {\lambda_3} \cos{\left(2 {\alpha} - 2 {\beta} \right)} - 2 {\lambda_3} \cos{\left(2 {\alpha} + 2 {\beta} \right)} + 2 {\lambda_4} \cos{\left(2 {\alpha} - 2 {\beta} \right)} - 2 {\lambda_4} \cos{\left(2 {\alpha} + 2 {\beta} \right)} - 6 {\lambda_5} \cos{\left(2 {\alpha} - 2 {\beta} \right)} - 2 {\lambda_5} \cos{\left(2 {\alpha} + 2 {\beta} \right)}\right)}{8}
```

$`A G^0 H^- H^+`$

```math
i \left({\lambda_1} \sin^{2}{\left({\beta} \right)} + {\lambda_2} \sin^{2}{\left({\beta} \right)} - {\lambda_2} - 2 {\lambda_3} \sin^{2}{\left({\beta} \right)} + {\lambda_3} - 2 {\lambda_4} \sin^{2}{\left({\beta} \right)} + {\lambda_4} - 2 {\lambda_5} \sin^{2}{\left({\beta} \right)} + {\lambda_5}\right) \sin{\left({\beta} \right)} \cos{\left({\beta} \right)}
```

$`A G^0 h h`$

```math
\frac{i \left(2 {\lambda_1} \sin{\left(2 {\beta} \right)} + {\lambda_1} \sin{\left(2 {\alpha} - 2 {\beta} \right)} - {\lambda_1} \sin{\left(2 {\alpha} + 2 {\beta} \right)} - 2 {\lambda_2} \sin{\left(2 {\beta} \right)} + {\lambda_2} \sin{\left(2 {\alpha} - 2 {\beta} \right)} - {\lambda_2} \sin{\left(2 {\alpha} + 2 {\beta} \right)} - 2 {\lambda_3} \sin{\left(2 {\alpha} - 2 {\beta} \right)} + 2 {\lambda_3} \sin{\left(2 {\alpha} + 2 {\beta} \right)} - 2 {\lambda_4} \sin{\left(2 {\alpha} - 2 {\beta} \right)} + 2 {\lambda_4} \sin{\left(2 {\alpha} + 2 {\beta} \right)} + 6 {\lambda_5} \sin{\left(2 {\alpha} - 2 {\beta} \right)} + 2 {\lambda_5} \sin{\left(2 {\alpha} + 2 {\beta} \right)}\right)}{8}
```

$`G^0 G^0 G^0 G^0`$

```math
3 i \left(- {\lambda_1} \cos^{4}{\left({\beta} \right)} - {\lambda_2} \sin^{4}{\left({\beta} \right)} - \frac{{\lambda_3} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{4} - \frac{{\lambda_4} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{4} - \frac{{\lambda_5} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{4}\right)
```

$`G^0 G^0 G^- G^+`$

```math
i \left(- {\lambda_1} \cos^{4}{\left({\beta} \right)} - {\lambda_2} \sin^{4}{\left({\beta} \right)} - \frac{{\lambda_3} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{4} - \frac{{\lambda_4} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{4} - \frac{{\lambda_5} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{4}\right)
```

$`G^0 G^0 G^- H^+`$

```math
i \left({\lambda_1} \cos^{2}{\left({\beta} \right)} + {\lambda_2} \cos^{2}{\left({\beta} \right)} - {\lambda_2} - 2 {\lambda_3} \cos^{2}{\left({\beta} \right)} + {\lambda_3} - 2 {\lambda_4} \cos^{2}{\left({\beta} \right)} + {\lambda_4} - 2 {\lambda_5} \cos^{2}{\left({\beta} \right)} + {\lambda_5}\right) \sin{\left({\beta} \right)} \cos{\left({\beta} \right)}
```

$`G^0 G^0 G^+ H^-`$

```math
i \left({\lambda_1} \cos^{2}{\left({\beta} \right)} + {\lambda_2} \cos^{2}{\left({\beta} \right)} - {\lambda_2} - 2 {\lambda_3} \cos^{2}{\left({\beta} \right)} + {\lambda_3} - 2 {\lambda_4} \cos^{2}{\left({\beta} \right)} + {\lambda_4} - 2 {\lambda_5} \cos^{2}{\left({\beta} \right)} + {\lambda_5}\right) \sin{\left({\beta} \right)} \cos{\left({\beta} \right)}
```

$`G^0 G^0 H H`$

```math
i \left(- {\lambda_1} \cos^{2}{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} - {\lambda_2} \sin^{2}{\left({\alpha} \right)} \sin^{2}{\left({\beta} \right)} - {\lambda_3} \sin^{2}{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} - {\lambda_3} \sin^{2}{\left({\beta} \right)} \cos^{2}{\left({\alpha} \right)} - {\lambda_4} \sin^{2}{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} - {\lambda_4} \sin^{2}{\left({\beta} \right)} \cos^{2}{\left({\alpha} \right)} - \frac{{\lambda_5} \left(\cos{\left(2 {\alpha} - 2 {\beta} \right)} - \cos{\left(2 {\alpha} + 2 {\beta} \right)}\right)}{2} + {\lambda_5} \sin^{2}{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} + {\lambda_5} \sin^{2}{\left({\beta} \right)} \cos^{2}{\left({\alpha} \right)}\right)
```

$`G^0 G^0 H h`$

```math
\frac{i \left(2 {\lambda_1} \sin{\left(2 {\alpha} \right)} + {\lambda_1} \sin{\left(2 {\alpha} - 2 {\beta} \right)} + {\lambda_1} \sin{\left(2 {\alpha} + 2 {\beta} \right)} - 2 {\lambda_2} \sin{\left(2 {\alpha} \right)} + {\lambda_2} \sin{\left(2 {\alpha} - 2 {\beta} \right)} + {\lambda_2} \sin{\left(2 {\alpha} + 2 {\beta} \right)} - 2 {\lambda_3} \sin{\left(2 {\alpha} - 2 {\beta} \right)} - 2 {\lambda_3} \sin{\left(2 {\alpha} + 2 {\beta} \right)} - 2 {\lambda_4} \sin{\left(2 {\alpha} - 2 {\beta} \right)} - 2 {\lambda_4} \sin{\left(2 {\alpha} + 2 {\beta} \right)} + 6 {\lambda_5} \sin{\left(2 {\alpha} - 2 {\beta} \right)} - 2 {\lambda_5} \sin{\left(2 {\alpha} + 2 {\beta} \right)}\right)}{8}
```

$`G^0 G^0 H^- H^+`$

```math
i \left(- \frac{{\lambda_1} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{8} - \frac{{\lambda_2} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{8} - {\lambda_3} \sin^{4}{\left({\beta} \right)} - {\lambda_3} \cos^{4}{\left({\beta} \right)} + \frac{{\lambda_4} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{4} + \frac{{\lambda_5} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{4}\right)
```

$`G^0 G^0 h h`$

```math
i \left(- {\lambda_1} \sin^{2}{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} - {\lambda_2} \sin^{2}{\left({\beta} \right)} \cos^{2}{\left({\alpha} \right)} - {\lambda_3} \sin^{2}{\left({\alpha} \right)} \sin^{2}{\left({\beta} \right)} - {\lambda_3} \cos^{2}{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} - {\lambda_4} \sin^{2}{\left({\alpha} \right)} \sin^{2}{\left({\beta} \right)} - {\lambda_4} \cos^{2}{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} + \frac{{\lambda_5} \left(\cos{\left(2 {\alpha} - 2 {\beta} \right)} - \cos{\left(2 {\alpha} + 2 {\beta} \right)}\right)}{2} + {\lambda_5} \sin^{2}{\left({\alpha} \right)} \sin^{2}{\left({\beta} \right)} + {\lambda_5} \cos^{2}{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)}\right)
```

$`G^- G^- G^+ G^+`$

```math
2 i \left(- {\lambda_1} \cos^{4}{\left({\beta} \right)} - {\lambda_2} \sin^{4}{\left({\beta} \right)} - \frac{{\lambda_3} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{4} - \frac{{\lambda_4} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{4} - \frac{{\lambda_5} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{4}\right)
```

$`G^- G^- G^+ H^+`$

```math
2 i \left({\lambda_1} \cos^{2}{\left({\beta} \right)} + {\lambda_2} \cos^{2}{\left({\beta} \right)} - {\lambda_2} - 2 {\lambda_3} \cos^{2}{\left({\beta} \right)} + {\lambda_3} - 2 {\lambda_4} \cos^{2}{\left({\beta} \right)} + {\lambda_4} - 2 {\lambda_5} \cos^{2}{\left({\beta} \right)} + {\lambda_5}\right) \sin{\left({\beta} \right)} \cos{\left({\beta} \right)}
```

$`G^- G^- H^+ H^+`$

```math
2 i \left(- \frac{{\lambda_1} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{8} - \frac{{\lambda_2} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{8} + \frac{{\lambda_3} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{4} + \frac{{\lambda_4} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{4} - {\lambda_5} \sin^{4}{\left({\beta} \right)} - {\lambda_5} \cos^{4}{\left({\beta} \right)}\right)
```

$`G^- G^+ G^+ H^-`$

```math
2 i \left({\lambda_1} \cos^{2}{\left({\beta} \right)} + {\lambda_2} \cos^{2}{\left({\beta} \right)} - {\lambda_2} - 2 {\lambda_3} \cos^{2}{\left({\beta} \right)} + {\lambda_3} - 2 {\lambda_4} \cos^{2}{\left({\beta} \right)} + {\lambda_4} - 2 {\lambda_5} \cos^{2}{\left({\beta} \right)} + {\lambda_5}\right) \sin{\left({\beta} \right)} \cos{\left({\beta} \right)}
```

$`G^- G^+ H H`$

```math
i \left(- {\lambda_1} \cos^{2}{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} - {\lambda_2} \sin^{2}{\left({\alpha} \right)} \sin^{2}{\left({\beta} \right)} - {\lambda_3} \sin^{2}{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} - {\lambda_3} \sin^{2}{\left({\beta} \right)} \cos^{2}{\left({\alpha} \right)} - \frac{{\lambda_4} \left(\cos{\left(2 {\alpha} - 2 {\beta} \right)} - \cos{\left(2 {\alpha} + 2 {\beta} \right)}\right)}{4} - \frac{{\lambda_5} \left(\cos{\left(2 {\alpha} - 2 {\beta} \right)} - \cos{\left(2 {\alpha} + 2 {\beta} \right)}\right)}{4}\right)
```

$`G^- G^+ H h`$

```math
\frac{i \left(2 {\lambda_1} \sin{\left(2 {\alpha} \right)} + {\lambda_1} \sin{\left(2 {\alpha} - 2 {\beta} \right)} + {\lambda_1} \sin{\left(2 {\alpha} + 2 {\beta} \right)} - 2 {\lambda_2} \sin{\left(2 {\alpha} \right)} + {\lambda_2} \sin{\left(2 {\alpha} - 2 {\beta} \right)} + {\lambda_2} \sin{\left(2 {\alpha} + 2 {\beta} \right)} - 2 {\lambda_3} \sin{\left(2 {\alpha} - 2 {\beta} \right)} - 2 {\lambda_3} \sin{\left(2 {\alpha} + 2 {\beta} \right)} + 2 {\lambda_4} \sin{\left(2 {\alpha} - 2 {\beta} \right)} - 2 {\lambda_4} \sin{\left(2 {\alpha} + 2 {\beta} \right)} + 2 {\lambda_5} \sin{\left(2 {\alpha} - 2 {\beta} \right)} - 2 {\lambda_5} \sin{\left(2 {\alpha} + 2 {\beta} \right)}\right)}{8}
```

$`G^- G^+ H^- H^+`$

```math
i \left(- \frac{{\lambda_1} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{4} - \frac{{\lambda_2} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{4} + \frac{{\lambda_3} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{4} - {\lambda_3} \sin^{4}{\left({\beta} \right)} - {\lambda_3} \cos^{4}{\left({\beta} \right)} + \frac{{\lambda_4} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{4} - {\lambda_4} \sin^{4}{\left({\beta} \right)} - {\lambda_4} \cos^{4}{\left({\beta} \right)} + \frac{{\lambda_5} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{2}\right)
```

$`G^- G^+ h h`$

```math
i \left(- {\lambda_1} \sin^{2}{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} - {\lambda_2} \sin^{2}{\left({\beta} \right)} \cos^{2}{\left({\alpha} \right)} - {\lambda_3} \sin^{2}{\left({\alpha} \right)} \sin^{2}{\left({\beta} \right)} - {\lambda_3} \cos^{2}{\left({\alpha} \right)} \cos^{2}{\left({\beta} \right)} + \frac{{\lambda_4} \left(\cos{\left(2 {\alpha} - 2 {\beta} \right)} - \cos{\left(2 {\alpha} + 2 {\beta} \right)}\right)}{4} + \frac{{\lambda_5} \left(\cos{\left(2 {\alpha} - 2 {\beta} \right)} - \cos{\left(2 {\alpha} + 2 {\beta} \right)}\right)}{4}\right)
```

$`G^- H H H^+`$

```math
\frac{i \left(2 {\lambda_1} \sin{\left(2 {\beta} \right)} - {\lambda_1} \sin{\left(2 {\alpha} - 2 {\beta} \right)} + {\lambda_1} \sin{\left(2 {\alpha} + 2 {\beta} \right)} - 2 {\lambda_2} \sin{\left(2 {\beta} \right)} - {\lambda_2} \sin{\left(2 {\alpha} - 2 {\beta} \right)} + {\lambda_2} \sin{\left(2 {\alpha} + 2 {\beta} \right)} + 2 {\lambda_3} \sin{\left(2 {\alpha} - 2 {\beta} \right)} - 2 {\lambda_3} \sin{\left(2 {\alpha} + 2 {\beta} \right)} - 2 {\lambda_4} \sin{\left(2 {\alpha} - 2 {\beta} \right)} - 2 {\lambda_4} \sin{\left(2 {\alpha} + 2 {\beta} \right)} - 2 {\lambda_5} \sin{\left(2 {\alpha} - 2 {\beta} \right)} - 2 {\lambda_5} \sin{\left(2 {\alpha} + 2 {\beta} \right)}\right)}{8}
```

$`G^- H H^+ h`$

```math
\frac{i \left(- {\lambda_1} \cos{\left(2 {\alpha} - 2 {\beta} \right)} + {\lambda_1} \cos{\left(2 {\alpha} + 2 {\beta} \right)} - {\lambda_2} \cos{\left(2 {\alpha} - 2 {\beta} \right)} + {\lambda_2} \cos{\left(2 {\alpha} + 2 {\beta} \right)} + 2 {\lambda_3} \cos{\left(2 {\alpha} - 2 {\beta} \right)} - 2 {\lambda_3} \cos{\left(2 {\alpha} + 2 {\beta} \right)} - 2 {\lambda_4} \cos{\left(2 {\alpha} - 2 {\beta} \right)} - 2 {\lambda_4} \cos{\left(2 {\alpha} + 2 {\beta} \right)} - 2 {\lambda_5} \cos{\left(2 {\alpha} - 2 {\beta} \right)} - 2 {\lambda_5} \cos{\left(2 {\alpha} + 2 {\beta} \right)}\right)}{8}
```

$`G^- H^- H^+ H^+`$

```math
2 i \left({\lambda_1} \sin^{2}{\left({\beta} \right)} + {\lambda_2} \sin^{2}{\left({\beta} \right)} - {\lambda_2} - 2 {\lambda_3} \sin^{2}{\left({\beta} \right)} + {\lambda_3} - 2 {\lambda_4} \sin^{2}{\left({\beta} \right)} + {\lambda_4} - 2 {\lambda_5} \sin^{2}{\left({\beta} \right)} + {\lambda_5}\right) \sin{\left({\beta} \right)} \cos{\left({\beta} \right)}
```

$`G^- H^+ h h`$

```math
\frac{i \left(2 {\lambda_1} \sin{\left(2 {\beta} \right)} + {\lambda_1} \sin{\left(2 {\alpha} - 2 {\beta} \right)} - {\lambda_1} \sin{\left(2 {\alpha} + 2 {\beta} \right)} - 2 {\lambda_2} \sin{\left(2 {\beta} \right)} + {\lambda_2} \sin{\left(2 {\alpha} - 2 {\beta} \right)} - {\lambda_2} \sin{\left(2 {\alpha} + 2 {\beta} \right)} - 2 {\lambda_3} \sin{\left(2 {\alpha} - 2 {\beta} \right)} + 2 {\lambda_3} \sin{\left(2 {\alpha} + 2 {\beta} \right)} + 2 {\lambda_4} \sin{\left(2 {\alpha} - 2 {\beta} \right)} + 2 {\lambda_4} \sin{\left(2 {\alpha} + 2 {\beta} \right)} + 2 {\lambda_5} \sin{\left(2 {\alpha} - 2 {\beta} \right)} + 2 {\lambda_5} \sin{\left(2 {\alpha} + 2 {\beta} \right)}\right)}{8}
```

$`G^+ G^+ H^- H^-`$

```math
2 i \left(- \frac{{\lambda_1} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{8} - \frac{{\lambda_2} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{8} + \frac{{\lambda_3} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{4} + \frac{{\lambda_4} \left(1 - \cos{\left(4 {\beta} \right)}\right)}{4} - {\lambda_5} \sin^{4}{\left({\beta} \right)} - {\lambda_5} \cos^{4}{\left({\beta} \right)}\right)
```

$`G^+ H H H^-`$

```math
\frac{i \left(2 {\lambda_1} \sin{\left(2 {\beta} \right)} - {\lambda_1} \sin{\left(2 {\alpha} - 2 {\beta} \right)} + {\lambda_1} \sin{\left(2 {\alpha} + 2 {\beta} \right)} - 2 {\lambda_2} \sin{\left(2 {\beta} \right)} - {\lambda_2} \sin{\left(2 {\alpha} - 2 {\beta} \right)} + {\lambda_2} \sin{\left(2 {\alpha} + 2 {\beta} \right)} + 2 {\lambda_3} \sin{\left(2 {\alpha} - 2 {\beta} \right)} - 2 {\lambda_3} \sin{\left(2 {\alpha} + 2 {\beta} \right)} - 2 {\lambda_4} \sin{\left(2 {\alpha} - 2 {\beta} \right)} - 2 {\lambda_4} \sin{\left(2 {\alpha} + 2 {\beta} \right)} - 2 {\lambda_5} \sin{\left(2 {\alpha} - 2 {\beta} \right)} - 2 {\lambda_5} \sin{\left(2 {\alpha} + 2 {\beta} \right)}\right)}{8}
```

$`G^+ H H^- h`$

```math
\frac{i \left(- {\lambda_1} \cos{\left(2 {\alpha} - 2 {\beta} \right)} + {\lambda_1} \cos{\left(2 {\alpha} + 2 {\beta} \right)} - {\lambda_2} \cos{\left(2 {\alpha} - 2 {\beta} \right)} + {\lambda_2} \cos{\left(2 {\alpha} + 2 {\beta} \right)} + 2 {\lambda_3} \cos{\left(2 {\alpha} - 2 {\beta} \right)} - 2 {\lambda_3} \cos{\left(2 {\alpha} + 2 {\beta} \right)} - 2 {\lambda_4} \cos{\left(2 {\alpha} - 2 {\beta} \right)} - 2 {\lambda_4} \cos{\left(2 {\alpha} + 2 {\beta} \right)} - 2 {\lambda_5} \cos{\left(2 {\alpha} - 2 {\beta} \right)} - 2 {\lambda_5} \cos{\left(2 {\alpha} + 2 {\beta} \right)}\right)}{8}
```

$`G^+ H^- H^- H^+`$

```math
2 i \left({\lambda_1} \sin^{2}{\left({\beta} \right)} + {\lambda_2} \sin^{2}{\left({\beta} \right)} - {\lambda_2} - 2 {\lambda_3} \sin^{2}{\left({\beta} \right)} + {\lambda_3} - 2 {\lambda_4} \sin^{2}{\left({\beta} \right)} + {\lambda_4} - 2 {\lambda_5} \sin^{2}{\left({\beta} \right)} + {\lambda_5}\right) \sin{\left({\beta} \right)} \cos{\left({\beta} \right)}
```

$`G^+ H^- h h`$

```math
\frac{i \left(2 {\lambda_1} \sin{\left(2 {\beta} \right)} + {\lambda_1} \sin{\left(2 {\alpha} - 2 {\beta} \right)} - {\lambda_1} \sin{\left(2 {\alpha} + 2 {\beta} \right)} - 2 {\lambda_2} \sin{\left(2 {\beta} \right)} + {\lambda_2} \sin{\left(2 {\alpha} - 2 {\beta} \right)} - {\lambda_2} \sin{\left(2 {\alpha} + 2 {\beta} \right)} - 2 {\lambda_3} \sin{\left(2 {\alpha} - 2 {\beta} \right)} + 2 {\lambda_3} \sin{\left(2 {\alpha} + 2 {\beta} \right)} + 2 {\lambda_4} \sin{\left(2 {\alpha} - 2 {\beta} \right)} + 2 {\lambda_4} \sin{\left(2 {\alpha} + 2 {\beta} \right)} + 2 {\lambda_5} \sin{\left(2 {\alpha} - 2 {\beta} \right)} + 2 {\lambda_5} \sin{\left(2 {\alpha} + 2 {\beta} \right)}\right)}{8}
```

#### Vector and two scalars (VSS): 10 vertices

| interaction | Feynman rule |
|---|---|
| $`\gamma G^- G^+`$ | $`\frac{i {g'} {g} \left({p_{G^-}} - {p_{G^+}}\right)}{\sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`W^+ G^0 G^-`$ | $`\frac{{g} \left({p_{G^0}} - {p_{G^-}}\right)}{2}`$ |
| $`W^- G^0 G^+`$ | $`\frac{{g} \left({p_{G^0}} - {p_{G^+}}\right)}{2}`$ |
| $`Z G^- G^+`$ | $`\frac{i \left(- {g'}^{2} {p_{G^-}} + {g'}^{2} {p_{G^+}} + {g}^{2} {p_{G^-}} - {g}^{2} {p_{G^+}}\right)}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`W^+ G^- H`$ | $`\frac{i {g} \left({p_{G^-}} - {p_{H}}\right) \cos{\left({\alpha} - {\beta} \right)}}{2}`$ |
| $`W^+ G^- h`$ | $`\frac{i {g} \left(- {p_{G^-}} + {p_{h}}\right) \sin{\left({\alpha} - {\beta} \right)}}{2}`$ |
| $`W^- G^+ H`$ | $`\frac{i {g} \left(- {p_{G^+}} + {p_{H}}\right) \cos{\left({\alpha} - {\beta} \right)}}{2}`$ |
| $`W^- G^+ h`$ | $`\frac{i {g} \left({p_{G^+}} - {p_{h}}\right) \sin{\left({\alpha} - {\beta} \right)}}{2}`$ |

$`Z G^0 H`$

```math
\frac{\left(- {g'}^{2} {p_{G^0}} + {g'}^{2} {p_{H}} - {g}^{2} {p_{G^0}} + {g}^{2} {p_{H}}\right) \cos{\left({\alpha} - {\beta} \right)}}{2 \sqrt{{g'}^{2} + {g}^{2}}}
```

$`Z G^0 h`$

```math
\frac{\left({g'}^{2} {p_{G^0}} - {g'}^{2} {p_{h}} + {g}^{2} {p_{G^0}} - {g}^{2} {p_{h}}\right) \sin{\left({\alpha} - {\beta} \right)}}{2 \sqrt{{g'}^{2} + {g}^{2}}}
```

#### Two vectors and a scalar (VVS): 4 vertices

| interaction | Feynman rule |
|---|---|
| $`\gamma W^+ G^-`$ | $`\frac{i {g'} {g}^{2} \left({v_1} \cos{\left({\beta} \right)} + {v_2} \sin{\left({\beta} \right)}\right)}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`\gamma W^- G^+`$ | $`\frac{i {g'} {g}^{2} \left({v_1} \cos{\left({\beta} \right)} + {v_2} \sin{\left({\beta} \right)}\right)}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`W^+ Z G^-`$ | $`- \frac{i {g'}^{2} {g} \left({v_1} \cos{\left({\beta} \right)} + {v_2} \sin{\left({\beta} \right)}\right)}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`W^- Z G^+`$ | $`- \frac{i {g'}^{2} {g} \left({v_1} \cos{\left({\beta} \right)} + {v_2} \sin{\left({\beta} \right)}\right)}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |

#### Two vectors and two scalars (VVSS): 18 vertices

| interaction | Feynman rule |
|---|---|
| $`\gamma \gamma G^- G^+`$ | $`\frac{2 i {g'}^{2} {g}^{2}}{{g'}^{2} + {g}^{2}}`$ |
| $`\gamma W^+ G^0 G^-`$ | $`- \frac{{g'} {g}^{2}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`\gamma W^- G^0 G^+`$ | $`\frac{{g'} {g}^{2}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`\gamma Z G^- G^+`$ | $`\frac{i {g'} {g} \left(- {g'}^{2} + {g}^{2}\right)}{{g'}^{2} + {g}^{2}}`$ |
| $`\gamma W^+ G^- H`$ | $`\frac{i {g'} {g}^{2} \cos{\left({\alpha} - {\beta} \right)}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`\gamma W^+ G^- h`$ | $`- \frac{i {g'} {g}^{2} \sin{\left({\alpha} - {\beta} \right)}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`\gamma W^- G^+ H`$ | $`\frac{i {g'} {g}^{2} \cos{\left({\alpha} - {\beta} \right)}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`\gamma W^- G^+ h`$ | $`- \frac{i {g'} {g}^{2} \sin{\left({\alpha} - {\beta} \right)}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`W^- W^+ G^0 G^0`$ | $`\frac{i {g}^{2}}{2}`$ |
| $`Z Z G^0 G^0`$ | $`\frac{i \left({g'}^{2} + {g}^{2}\right)}{2}`$ |
| $`W^+ Z G^0 G^-`$ | $`\frac{{g'}^{2} {g}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`W^- Z G^0 G^+`$ | $`- \frac{{g'}^{2} {g}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`W^- W^+ G^- G^+`$ | $`\frac{i {g}^{2}}{2}`$ |
| $`Z Z G^- G^+`$ | $`\frac{i \left({g'} - {g}\right)^{2} \left({g'} + {g}\right)^{2}}{2 \left({g'}^{2} + {g}^{2}\right)}`$ |
| $`W^+ Z G^- H`$ | $`- \frac{i {g'}^{2} {g} \cos{\left({\alpha} - {\beta} \right)}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`W^+ Z G^- h`$ | $`\frac{i {g'}^{2} {g} \sin{\left({\alpha} - {\beta} \right)}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`W^- Z G^+ H`$ | $`- \frac{i {g'}^{2} {g} \cos{\left({\alpha} - {\beta} \right)}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |
| $`W^- Z G^+ h`$ | $`\frac{i {g'}^{2} {g} \sin{\left({\alpha} - {\beta} \right)}}{2 \sqrt{{g'}^{2} + {g}^{2}}}`$ |

## Fermion vertices: 31 in all

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

### Fermion pair and a scalar (FFS): 20 vertices

| interaction | Feynman rule |
|---|---|
| $`\bar{\nu}_\tau \tau G^+`$ | $`i \left(- \frac{\sqrt{2} {m_\tau}}{{v}}\right) P_R`$ |
| $`\bar{\nu}_\tau \tau H^+`$ | $`i \left(\frac{\sqrt{2} {m_\tau} \tan{\left({\beta} \right)}}{{v}}\right) P_R`$ |
| $`\bar{\tau} \nu_\tau G^-`$ | $`i \left(- \frac{\sqrt{2} {m_\tau}}{{v}}\right) P_L`$ |
| $`\bar{\tau} \nu_\tau H^-`$ | $`i \left(\frac{\sqrt{2} {m_\tau} \tan{\left({\beta} \right)}}{{v}}\right) P_L`$ |
| $`\bar{\tau} \tau A`$ | $`i \left[\left(- \frac{i {m_\tau} \tan{\left({\beta} \right)}}{{v}}\right) P_L + \left(\frac{i {m_\tau} \tan{\left({\beta} \right)}}{{v}}\right) P_R\right]`$ |
| $`\bar{\tau} \tau G^0`$ | $`i \left[\left(\frac{i {m_\tau}}{{v}}\right) P_L + \left(- \frac{i {m_\tau}}{{v}}\right) P_R\right]`$ |
| $`\bar{\tau} \tau H`$ | $`i \left(- \frac{{m_\tau} \cos{\left({\alpha} \right)}}{{v} \cos{\left({\beta} \right)}}\right)`$ |
| $`\bar{\tau} \tau h`$ | $`i \left(\frac{{m_\tau} \sin{\left({\alpha} \right)}}{{v} \cos{\left({\beta} \right)}}\right)`$ |
| $`\bar{b} b A`$ | $`i \left[\left(- \frac{i {m_b} \tan{\left({\beta} \right)}}{{v}}\right) P_L + \left(\frac{i {m_b} \tan{\left({\beta} \right)}}{{v}}\right) P_R\right]`$ |
| $`\bar{b} b G^0`$ | $`i \left[\left(\frac{i {m_b}}{{v}}\right) P_L + \left(- \frac{i {m_b}}{{v}}\right) P_R\right]`$ |
| $`\bar{b} b H`$ | $`i \left(- \frac{{m_b} \cos{\left({\alpha} \right)}}{{v} \cos{\left({\beta} \right)}}\right)`$ |
| $`\bar{b} b h`$ | $`i \left(\frac{{m_b} \sin{\left({\alpha} \right)}}{{v} \cos{\left({\beta} \right)}}\right)`$ |
| $`\bar{b} t G^-`$ | $`i \left[\left(- \frac{\sqrt{2} {m_b}}{{v}}\right) P_L + \left(\frac{\sqrt{2} {m_t}}{{v}}\right) P_R\right]`$ |
| $`\bar{b} t H^-`$ | $`i \left[\left(\frac{\sqrt{2} {m_b} \tan{\left({\beta} \right)}}{{v}}\right) P_L + \left(\frac{\sqrt{2} {m_t}}{{v} \tan{\left({\beta} \right)}}\right) P_R\right]`$ |
| $`\bar{t} b G^+`$ | $`i \left[\left(\frac{\sqrt{2} {m_t}}{{v}}\right) P_L + \left(- \frac{\sqrt{2} {m_b}}{{v}}\right) P_R\right]`$ |
| $`\bar{t} b H^+`$ | $`i \left[\left(\frac{\sqrt{2} {m_t}}{{v} \tan{\left({\beta} \right)}}\right) P_L + \left(\frac{\sqrt{2} {m_b} \tan{\left({\beta} \right)}}{{v}}\right) P_R\right]`$ |
| $`\bar{t} t A`$ | $`i \left[\left(- \frac{i {m_t}}{{v} \tan{\left({\beta} \right)}}\right) P_L + \left(\frac{i {m_t}}{{v} \tan{\left({\beta} \right)}}\right) P_R\right]`$ |
| $`\bar{t} t G^0`$ | $`i \left[\left(- \frac{i {m_t}}{{v}}\right) P_L + \left(\frac{i {m_t}}{{v}}\right) P_R\right]`$ |
| $`\bar{t} t H`$ | $`i \left(- \frac{{m_t} \sin{\left({\alpha} \right)}}{{v} \sin{\left({\beta} \right)}}\right)`$ |
| $`\bar{t} t h`$ | $`i \left(- \frac{{m_t} \cos{\left({\alpha} \right)}}{{v} \sin{\left({\beta} \right)}}\right)`$ |
