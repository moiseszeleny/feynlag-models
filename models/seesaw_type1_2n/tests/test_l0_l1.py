"""L0/L1: invariance, anomalies, the 5×5 seesaw mass matrix and its Takagi spectrum."""

import signal

import pytest
import sympy as sp

from feynlag import diagonalize_takagi


def test_validate_invariance_and_anomalies(ss):
    """The 3×2 Dirac Yukawa via H̃ and the two Majorana masses are gauge invariant and
    hermitian; the gauge-singlet ν_R leave the anomaly cancellation of `sm` untouched."""
    report = ss.model.validate()
    assert report.ok, report.summary()
    assert report.checks["anomalies"] is not None and report.checks["anomalies"].ok


@pytest.mark.xfail(strict=True, raises=TimeoutError,
                   reason="FG-5: diagonalize_takagi is symbolic and does not finish on a generic 5×5")
def test_feynlag_takagi_generic_matrix_gap(ss):
    """feynlag's own Takagi factorisation of the benchmark 5×5 within 10 s."""
    def timeout(*_):
        raise TimeoutError
    old = signal.signal(signal.SIGALRM, timeout)
    signal.alarm(10)
    try:
        diagonalize_takagi(ss.extra["Mn"])
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, old)
