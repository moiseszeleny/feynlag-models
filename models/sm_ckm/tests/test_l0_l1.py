"""L0 (declared, invariant, anomaly-free) and L1 (tadpoles, spectrum, Goldstones)."""

import sympy as sp


def test_validate_invariance_and_anomalies(ckm):
    report = ckm.model.validate()
    assert report.ok, report.summary()
    assert report.checks["anomalies"] is not None        # quarks present → really checked
    assert report.checks["anomalies"].ok
    # the down Yukawa really is the non-diagonal, complex one
    Yd = ckm.extra["Yd"]
    assert any(Yd[a, b] != 0 for a in range(3) for b in range(3) if a != b)
    assert Yd.has(sp.I)

