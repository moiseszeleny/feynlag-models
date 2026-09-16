import pytest

from models.new_model.model import build


@pytest.fixture(scope="session")
def bundle():
    return build()


def test_l0_validate(bundle):
    report = bundle.model.validate()
    assert report.ok, report.summary()


def test_l1_spectrum(bundle):
    pytest.skip("L1 not yet claimed")
