import pytest
import sympy as sp

from feynlag import extract_fermion_vertices
from models.seesaw_type1_2n.model import build, physical_neutrino_lagrangian


@pytest.fixture(scope="session")
def ss():
    return build()


@pytest.fixture(scope="session")
def chi_table(ss):
    """Fermion vertices with the neutrinos in the Majorana mass basis χ_k."""
    return extract_fermion_vertices(physical_neutrino_lagrangian(ss), ss.boson_list)


def coupling(table, key, boson, vals):
    c = table.get(key, {}).get(1, {}).get((boson,), 0)
    return complex(sp.N(sp.sympify(c).subs(vals))) if c != 0 else 0j
