"""L3: the exported UFO imports and every coupling evaluates (round-trip)."""

import sympy as sp

from feynlag_models.ufo import export_ufo


def test_ufo_roundtrip(sm, tmp_path):
    path, report, skipped = export_ufo(sm, tmp_path / "SM_UFO", "SM_UFO")
    assert report.ok, report.failures
    assert not skipped, skipped                      # every fermion key exported
    vals = sm.values()
    g, v = vals[sm.pieces.gw.s], vals[sm.pieces.ew.v.s]
    target = 1j * g**2 * v / 2                       # hWW
    assert any(abs(c - target) < 1e-9 for c in report.couplings.values())
    text = (path / "vertices.py").read_text()
    assert "Identity(1,2)" in text                   # quark vertices carry colour flow
    assert (path / "particles.py").exists()
