import pytest

from models.froggatt_nielsen.model import build


@pytest.fixture(scope="session")
def fn():
    return build()
