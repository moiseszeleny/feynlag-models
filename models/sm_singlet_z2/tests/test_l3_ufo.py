"""L3: UFO export (h1, h2 + SM) imports and round-trips numerically."""

from feynlag_models.ufo import export_ufo


def test_ufo_roundtrip(xsm, tmp_path):
    path, report, skipped = export_ufo(xsm, tmp_path / "XSM_UFO", "SM_SINGLET_Z2_UFO")
    assert report.ok, report.failures
    assert not skipped, skipped
    vals = xsm.values()
    import cmath
    g, v, th = vals[xsm.pieces.gw.s], vals[xsm.pieces.ew.v.s], vals[xsm.extra["theta"].s]
    target = 1j * g**2 * v / 2 * cmath.cos(th)          # h1WW
    assert any(abs(c - target) < 1e-9 for c in report.couplings.values())
    names = (path / "particles.py").read_text()
    assert "'h2'" in names and "'h'" in names
