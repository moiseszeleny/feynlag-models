import pytest

from models.thdm_type2.model import build


@pytest.fixture(scope="session")
def thdm():
    return build()


@pytest.fixture(scope="session")
def ftab(thdm):
    return thdm.fermion_table()
