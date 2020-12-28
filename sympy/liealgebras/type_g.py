# -*- coding: utf-8 -*-

from .cartan_base import Standard_Cartan
from sympy import Matrix

class TypeG(Standard_Cartan):

    def __new__(cls, n):
        if n != 2:
            raise ValueError("n should be 2")
        return Standard_Cartan.__new__(cls, "G", 2)


    def dimension(self):
        """Dimension of the vector space V underlying the Lie algebra

        Examples
        ========

        >>> from sympy.liealgebras.cartan_type import CartanType
        >>> c = CartanType("G2")
        >>> c.dimension()
        3
        """
        return 3

    def simple_root(self, i):
        """The ith simple root of G_2

        Every lie algebra has a unique root system.
        Given a root system Q, there is a subset of the
        roots such that an element of Q is called a
        simple root if it cannot be written as the sum
        of two elements in Q.  If we let D denote the
        set of simple roots, then it is clear that every
        element of Q can be written as a linear combination
        of elements of D with all coefficients non-negative.

        Examples
        ========

        >>> from sympy.liealgebras.cartan_type import CartanType
        >>> c = CartanType("G2")
        >>> c.simple_root(1)
        Matrix([[0, 1, -1]])

        """
        if i == 1:
            return Matrix([[0, 1, -1]])
        else:
            return Matrix([[1, -2, 1]])


    def roots(self):
        """
        Returns the total number of roots of G_2
        """
        return 12

    def basis(self):
        """
        Returns the number of independent generators of G_2
        """
        return 14

    def dynkin_diagram(self):
        diag = "0≡<≡0\n1   2"
        return diag
