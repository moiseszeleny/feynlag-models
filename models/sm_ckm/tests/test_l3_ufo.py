"""L3: the exported UFO imports and every coupling evaluates (round-trip)."""

import cmath

from feynlag_models.ufo import export_ufo, exported_vertex_classes

NAMES = ["u", "c", "t", "d", "s", "b", "e-", "mu-", "ta-", "ve", "vm", "vt"]


def test_ufo_roundtrip(ckm, tmp_path):
    path, report, skipped = export_ufo(ckm, tmp_path / "SM_CKM_UFO", "SM_CKM_UFO")
    assert report.ok, report.failures
    assert not skipped, skipped                      # every fermion key exported
    particles = (path / "particles.py").read_text()
    for name in NAMES:
        assert f"name='{name}'" in particles, name
    assert exported_vertex_classes(path) == {"FFS", "FFV", "SSS", "SSSS", "VVS", "VVSS", "VVV"}

    vals = ckm.values()
    g = vals[ckm.pieces.gw.s]
    s12, s13, s23, d = (ckm.benchmark[k] for k in ("s12", "s13", "s23", "deltaCP"))
    c12, c13 = (1 - s12**2) ** 0.5, (1 - s13**2) ** 0.5
    Vus, Vub = s12 * c13, s13 * cmath.exp(-1j * d)
    couplings = list(report.couplings.values())
    for V in (Vus, Vub, c12 * c13):
        target = g / 2**0.5 * V                      # raw W⁺ ū d coefficient
        assert any(abs(c - target) < 1e-12 or abs(c - 1j * target) < 1e-12
                   for c in couplings), V

    # GIM: no neutral-boson vertex between different down flavours was written
    vertices = (path / "vertices.py").read_text()
    for a, b in (("d", "s"), ("d", "b"), ("s", "b")):
        for bos in ("Z", "a", "h"):
            assert f"P.{a}__tilde__, P.{b}, P.{bos}" not in vertices
            assert f"P.{b}__tilde__, P.{a}, P.{bos}" not in vertices
