import pytest

from models.sm.model import build


@pytest.fixture(scope="session")
def sm():
    return build()
