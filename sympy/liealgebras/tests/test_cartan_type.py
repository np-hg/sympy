from sympy.liealgebras.cartan_type import CartanType
from sympy.liealgebras.cartan_base import Standard_Cartan

def test_Standard_Cartan():
    c = CartanType("A4")
    assert c.rank() == 4
    assert c.series == "A"
    m = Standard_Cartan("A", 2)
    assert m.rank() == 2
    assert m.series == "A"
    b = CartanType("B12")
    assert b.rank() == 12
    assert b.series == "B"
