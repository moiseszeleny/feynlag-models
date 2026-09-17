import pytest

from models.sm_ckm.model import build


@pytest.fixture(scope="session")
def ckm():
    return build()
