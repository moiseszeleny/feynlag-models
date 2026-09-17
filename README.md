# feynlag-models

A **verified library of minimal Standard Model extensions** built with
[`feynlag`](https://github.com/moiseszeleny/feynlag) (pinned exactly in `pyproject.toml`).
Each model ships a physics card, a next-steps guide, machine-readable metadata, tests that
pin its physics against the literature, and stamped outputs (UFO, LaTeX).

See `CLAUDE.md` for the rules, `CONVENTIONS.md` for the conventions, `GENEALOGY.md` for
the family tree, `FEYNLAG_GAPS.md` for what the library could not do, and `REPORT.md` for
the pilot report.

| model | what | maturity |
|---|---|---|
| [`sm`](models/sm/README.md) | Standard Model root, one full generation | L3 |
| [`sm_singlet_z2`](models/sm_singlet_z2/README.md) | real singlet, spontaneously broken $Z_2$, scalar mixing | L3 |
| [`seesaw_type1`](models/seesaw_type1/README.md) | one $\nu_R$ with a Majorana mass, Takagi seesaw | L2 |
| [`thdm_type2`](models/thdm_type2/README.md) | type-II 2HDM, CP-conserving, softly broken $Z_2$ | L3 |

Maturity levels (`CLAUDE.md`): L0 declared+invariant+anomaly-free · L1 tadpoles+spectrum+Goldstones ·
L2 literature-checked (symbolic and numeric) · L3 UFO round-trip · L4 MadGraph cross-section.

```bash
uv sync --all-extras
uv run pytest -q -m "not slow"                 # 71 passed, 3 strict xfails (documented gaps/discrepancies)
uv run python scripts/build_outputs.py --check
uv run python scripts/build_genealogy.py --check
```
