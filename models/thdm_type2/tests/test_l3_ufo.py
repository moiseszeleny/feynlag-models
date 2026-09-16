"""L3: UFO export of the 2HDM (h, H, A, H± + SM) imports and round-trips."""

import cmath

from feynlag_models.ufo import export_ufo


def test_ufo_roundtrip(thdm, tmp_path):
    path, report, skipped = export_ufo(thdm, tmp_path / "THDM_UFO", "THDM_TYPE2_UFO")
    assert report.ok, report.failures
    assert not skipped, skipped
    vals = thdm.values()
    e = thdm.extra
    g, v = vals[thdm.pieces.gw.s], vals[e["v"].s]
    target = 1j * g**2 * v / 2 * cmath.sin(vals[e["beta"].s] - vals[e["alpha"].s])   # hWW
    assert any(abs(c - target) < 1e-9 for c in report.couplings.values())
    names = (path / "particles.py").read_text()
    for n in ("'h'", "'h2'", "'h3'", "'h+'", "'h-'"):
        assert n in names, n
