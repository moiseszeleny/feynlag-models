import pytest

from models.sm_singlet_z2.model import build


@pytest.fixture(scope="session")
def xsm():
    return build()
