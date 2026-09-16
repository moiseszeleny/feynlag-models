# feynlag-models

A **verified library of minimal Standard Model extensions** built with
[`feynlag`](https://github.com/moiseszeleny/feynlag) (pinned exactly in `pyproject.toml`).
Each model ships a physics card, a next-steps guide, machine-readable metadata, tests that
pin its physics against the literature, and stamped outputs (UFO, LaTeX).

See `CLAUDE.md` for the rules, `CONVENTIONS.md` for the conventions, `GENEALOGY.md` for
the family tree, `FEYNLAG_GAPS.md` for what the library could not do, and `REPORT.md` for
the pilot report.

```bash
uv sync --all-extras
uv run pytest -q -m "not slow"
```
