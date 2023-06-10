import unittest
import numpy as np
from poly import Poly


class TestPoly(unittest.TestCase):

    def test_init(self):
        # Wrong input types
        self.assertRaises(TypeError, Poly, coef='abc')
        self.assertRaises(TypeError, Poly, coef=[0, 1, 2], symbol=0)

        # NaN and Inf values as a Number input
        self.assertRaises(ValueError, Poly, coef=np.nan)
        self.assertRaises(ValueError, Poly, coef=np.nan)

        # Empty list/tuple/dict/np.ndarray as an input
        self.assertRaises(ValueError, Poly, coef=[])
        self.assertRaises(ValueError, Poly, coef=())
        self.assertRaises(ValueError, Poly, coef={})
        self.assertRaises(ValueError, Poly, coef=np.array([]))

        # Wrong key and value types in the input dict
        self.assertRaises(TypeError, Poly, coef={'a': 1, 'b': 2, 'c': 3})
        self.assertRaises(TypeError, Poly, coef={1: 'a', 2: 'b', 3: 'c'})

        # Wrong key value in the input dict
        self.assertRaises(ValueError, Poly, coef={-1: 1, 2: 2, 3: 3})

        # NaN and Inf values in the input dict
        self.assertRaises(ValueError, Poly, coef={1: np.nan, 2: 2, 3: 3})
        self.assertRaises(ValueError, Poly, coef={1: 1, 2: np.inf, 3: 3})

        # Wrong value types in the input list/tuple/np.ndarray
        self.assertRaises(TypeError, Poly, coef=['a', 'b', 'c'])
        self.assertRaises(TypeError, Poly, coef=('a', 'b', 'c'))
        self.assertRaises(TypeError, Poly, coef=np.array(['a', 'b', 'c']))

        # NaN and Inf values in the input dict list/tuple/np.ndarray
        self.assertRaises(ValueError, Poly, coef=[np.nan, 2, 3])
        self.assertRaises(ValueError, Poly, coef=(np.nan, 2, 3))
        self.assertRaises(ValueError, Poly, coef=np.array([np.nan, 2, 3]))
        self.assertRaises(ValueError, Poly, coef=[1, np.inf, 3])
        self.assertRaises(ValueError, Poly, coef=(1, np.inf, 3))
        self.assertRaises(ValueError, Poly, coef=np.array([1, np.inf, 3]))

    def test_symbol(self):
        # Default symbol
        self.assertEqual(Poly({0: 0}).symbol, 'x')
        self.assertEqual(Poly([1, 1, 1]).symbol, 'x')

        # Arbitrary symbol
        self.assertEqual(Poly({0: 0}, symbol='y').symbol, 'y')
        self.assertEqual(Poly([1, 1, 1], symbol='y').symbol, 'y')

    def test_coef(self):
        # Number input
        self.assertEqual(Poly(0).coef, {0: 0.0})
        self.assertEqual(Poly(1).coef, {0: 1.0})

        # List input
        self.assertEqual(Poly([0]).coef, {0: 0.0})
        self.assertEqual(Poly([0, 0, 0]).coef, {0: 0.0})
        self.assertEqual(Poly([0, 0, 1]).coef, {2: 1.0})
        self.assertEqual(Poly([1, 0, 1]).coef, {0: 1.0, 2: 1.0})
        self.assertEqual(Poly([1, 1, 1]).coef, {0: 1.0, 1: 1.0, 2: 1.0})

        # Tuple input
        self.assertEqual(Poly((0,)).coef, {0: 0.0})
        self.assertEqual(Poly((0, 0, 0)).coef, {0: 0.0})
        self.assertEqual(Poly((0, 0, 1)).coef, {2: 1.0})
        self.assertEqual(Poly((1, 0, 1)).coef, {0: 1.0, 2: 1.0})
        self.assertEqual(Poly((1, 1, 1)).coef, {0: 1.0, 1: 1.0, 2: 1.0})

        # np.ndarray input
        self.assertEqual(Poly(np.array([0])).coef, {0: 0.0})
        self.assertEqual(Poly(np.array([0, 0, 0])).coef, {0: 0.0})
        self.assertEqual(Poly(np.array([0, 0, 1])).coef, {2: 1.0})
        self.assertEqual(Poly(np.array([1, 0, 1])).coef, {0: 1.0, 2: 1.0})
        self.assertEqual(Poly(np.array([1, 1, 1])).coef, {0: 1.0, 1: 1.0, 2: 1.0})

        # Dict input
        self.assertEqual(Poly({0: 0}).coef, {0: 0})
        self.assertEqual(Poly({0: 0, 2: 0, 5: 0}).coef, {0: 0.0})
        self.assertEqual(Poly({0: 0, 2: 0, 5: 1}).coef, {5: 1.0})
        self.assertEqual(Poly({0: 1, 1: 0, 2: 1}).coef, {0: 1.0, 2: 1.0})
        self.assertEqual(Poly({0: 1, 1: 1, 2: 1}).coef, {0: 1.0, 1: 1.0, 2: 1.0})

    def test_degree(self):
        # Number input
        self.assertEqual(Poly(0).degree, 0)
        self.assertEqual(Poly(5).degree, 0)

        # List input
        self.assertEqual(Poly([0]).degree, 0)
        self.assertEqual(Poly([0, 0, 0]).degree, 0)
        self.assertEqual(Poly([0, 1, 0]).degree, 1)
        self.assertEqual(Poly([1, 0, 1]).degree, 2)
        self.assertEqual(Poly([1, 1, 1]).degree, 2)

        # Tuple input
        self.assertEqual(Poly((0,)).degree, 0)
        self.assertEqual(Poly((0, 0, 0)).degree, 0)
        self.assertEqual(Poly((0, 1, 0)).degree, 1)
        self.assertEqual(Poly((1, 0, 1)).degree, 2)
        self.assertEqual(Poly((1, 1, 1)).degree, 2)

        # np.ndarray input
        self.assertEqual(Poly(np.array([0])).degree, 0)
        self.assertEqual(Poly(np.array([0, 0, 0])).degree, 0)
        self.assertEqual(Poly(np.array([0, 1, 0])).degree, 1)
        self.assertEqual(Poly(np.array([1, 0, 1])).degree, 2)
        self.assertEqual(Poly(np.array([1, 1, 1])).degree, 2)

        # Dict input
        self.assertEqual(Poly({0: 0}).degree, 0)
        self.assertEqual(Poly({0: 0, 2: 0, 5: 0}).degree, 0)
        self.assertEqual(Poly({0: 0, 2: 0, 5: 1}).degree, 5)
        self.assertEqual(Poly({0: 1, 1: 0, 2: 1}).degree, 2)
        self.assertEqual(Poly({0: 1, 1: 1, 5: 1}).degree, 5)

    def test_copy(self):
        poly = Poly({1: 1, 2: 2, 3: 3})
        poly_copy = poly.copy()

        # Test for being an instance of Poly class
        self.assertIsInstance(poly_copy, Poly)

        # Test for equality
        self.assertEqual(poly_copy, poly)

        # Test for pointing different memory regions
        self.assertIsNot(poly_copy, poly)

    def test_div_monomials(self):
        # Wrong input length
        self.assertRaises(ValueError, Poly._div_monomials, Poly({4: 5}), Poly({0: 1, 2: 3}))
        self.assertRaises(ValueError, Poly._div_monomials, Poly({0: 1, 2: 3}), Poly({4: 5}))
        self.assertRaises(ValueError, Poly._div_monomials, Poly({0: 1, 2: 3}), Poly({4: 5, 6: 7}))

        # Different symbols for the indeterminate
        self.assertRaises(ValueError, Poly._div_monomials, Poly({2: 3}, symbol='x'), Poly({0: 1}, symbol='y'))

        # Divisor has a greater degree than divisible
        self.assertRaises(ValueError, Poly._div_monomials, Poly({0: 1}), Poly({2: 3}))

        # Division by zero
        self.assertRaises(ZeroDivisionError, Poly._div_monomials, Poly({2: 3}), Poly({0: 0}))

        # Number input
        self.assertEqual(Poly._div_monomials(Poly(10), 5), Poly(2))
        self.assertEqual(Poly._div_monomials(Poly(0), Poly(15)), Poly(0))

        # List input
        self.assertEqual(Poly._div_monomials(Poly([10]), Poly([5])), Poly(2))

        # Dict input
        self.assertEqual(Poly._div_monomials(Poly({0: 10}, symbol='y'), Poly({0: 5}, symbol='y')),
                         Poly(2, symbol='y'))
        self.assertEqual(Poly._div_monomials(Poly({5: 2}), Poly({3: 0.5})), Poly({2: 4}))
        self.assertEqual(Poly._div_monomials(Poly({10: 0.5}), Poly({0: 10})), Poly({10: 0.05}))

        # Number and list input
        self.assertEqual(Poly._div_monomials(Poly([10]), 5), Poly(2))

        # List and dict input
        self.assertEqual(Poly._div_monomials(Poly([10]), Poly({0: 5})), Poly(2))

        # Number and dict input
        self.assertEqual(Poly._div_monomials(Poly({10: 0.5}, symbol='y'), 10, symbol='y'),
                         Poly({10: 0.05}, symbol='y'))

    def test_len(self):
        # By definition
        self.assertEqual(len(Poly(5)), 1)
        self.assertEqual(len(Poly({0: 0, 2: 0, 5: 0})), 1)
        self.assertEqual(len(Poly({0: 0, 2: 0, 5: 1})), 1)
        self.assertEqual(len(Poly({0: 1, 1: 0, 2: 1})), 2)
        self.assertEqual(len(Poly({0: 1, 1: 1, 5: 1})), 3)

    def test_str(self):
        # Monomial representation
        self.assertEqual(str(Poly(5)), '5.0')
        self.assertEqual(str(Poly({10: -5})), '-5.0*x^10')
        self.assertEqual(str(Poly({0: 0, 2: 0, 5: 0})), '0.0')
        self.assertEqual(str(Poly({0: 0, 2: 0, 5: 1})), 'x^5')
        self.assertEqual(str(Poly({10: 5}, symbol='y')), '5.0*y^10')

        # Polynomial representation
        self.assertEqual(str(Poly({0: 1, 2: 1, 5: 1})), 'x^5 + x^2 + 1.0')
        self.assertEqual(str(Poly({1: 2, 3: 4, 5: 6})), '6.0*x^5 + 4.0*x^3 + 2.0*x')
        self.assertEqual(str(Poly({0: -1, 2: -3, 4: -5}, symbol='z')), '-5.0*z^4 - 3.0*z^2 - 1.0')

    def test_add(self):
        # Different symbols for the indeterminate
        with self.assertRaises(ValueError):
            poly = Poly({0: 1, 2: 1, 5: 1}, symbol='y') + Poly({1: 2, 3: 4, 5: 6}, symbol='z')

        # Number input
        self.assertEqual(Poly(5) + 10, Poly(15))
        self.assertEqual(Poly(0) + Poly(15), Poly(15))

        # List input
        self.assertEqual(Poly([0]) + Poly([15]), Poly(15))
        self.assertEqual(Poly([1, 2, 3]) + Poly([3, 2, 1]), Poly([4, 4, 4]))
        self.assertEqual(Poly([1, 2, 3, 4]) + Poly([3, 2, 1]), Poly([4, 4, 4, 4]))

        # Dict input
        self.assertEqual(Poly({0: 0}) + Poly({0: 15}), Poly(15))
        self.assertEqual(Poly({1: 1, 2: 2}) + Poly({1: 2, 2: 3}), Poly({1: 3, 2: 5}))
        self.assertEqual(Poly({1: 1, 2: 2}) + Poly({3: 3, 4: 4}), Poly({1: 1, 2: 2, 3: 3, 4: 4}))

        # Number and list input
        self.assertEqual(Poly([1, 2, 3]) + 4, Poly([5, 2, 3]))

        # List and dict input
        self.assertEqual(Poly([1, 2, 3]) + Poly({2: 5}), Poly([1, 2, 8]))

        # Number and dict input
        self.assertEqual(Poly({3: 3, 4: 4}) + 2, Poly({0: 2, 3: 3, 4: 4}))

    def test_sub(self):
        # Different symbols for the indeterminate
        with self.assertRaises(ValueError):
            poly = Poly({0: 1, 2: 1, 5: 1}, symbol='y') - Poly({1: 2, 3: 4, 5: 6}, symbol='z')

        # Number input
        self.assertEqual(Poly(5) - 10, Poly(-5))
        self.assertEqual(Poly(0) - Poly(15), Poly(-15))

        # List input
        self.assertEqual(Poly([0]) - Poly([15]), Poly(-15))
        self.assertEqual(Poly([1, 2, 3]) - Poly([3, 2, 1]), Poly([-2, 0, 2]))
        self.assertEqual(Poly([1, 2, 3, 4]) - Poly([3, 2, 1]), Poly([-2, 0, 2, 4]))

        # Dict input
        self.assertEqual(Poly({0: 0}) - Poly({0: 15}), Poly(-15))
        self.assertEqual(Poly({1: 1, 2: 2}) - Poly({1: 2, 2: 3}), Poly({1: -1, 2: -1}))
        self.assertEqual(Poly({1: 1, 2: 2}) - Poly({3: 3, 4: 4}), Poly({1: 1, 2: 2, 3: -3, 4: -4}))

        # Number and list input
        self.assertEqual(Poly([1, 2, 3]) - 4, Poly([-3, 2, 3]))

        # List and dict input
        self.assertEqual(Poly([1, 2, 3]) - Poly({2: 5}), Poly([1, 2, -2]))

        # Number and dict input
        self.assertEqual(Poly({3: 3, 4: 4}) - 2, Poly({0: -2, 3: 3, 4: 4}))

    def test_neg(self):
        # Number input
        self.assertEqual(-Poly(5), Poly(-5))

        # List input
        self.assertEqual(-Poly([1, 2, 3, 4]), Poly([-1, -2, -3, -4]))

        # Dict input
        self.assertEqual(-Poly({3: 3, 4: 4}), Poly({3: -3, 4: -4}))

    def test_mul(self):
        # Different symbols for the indeterminate
        with self.assertRaises(ValueError):
            poly = Poly({0: 1, 2: 1, 5: 1}, symbol='y') * Poly({1: 2, 3: 4, 5: 6}, symbol='z')

        # Number input
        self.assertEqual(Poly(-5) * 10, Poly(-50))
        self.assertEqual(Poly(0) * Poly(15), Poly(0))

        # List input
        self.assertEqual(Poly([0]) * Poly([15]), Poly(0))
        self.assertEqual(Poly([1, 2, 3]) * Poly([3, 2, 1]), Poly([3, 8, 14, 8, 3]))
        self.assertEqual(Poly([1, 2, 3, 4]) * Poly([3, 2, 1]), Poly([3, 8, 14, 20, 11, 4]))

        # Dict input
        self.assertEqual(Poly({0: 0}) * Poly({0: 15}), Poly(0))
        self.assertEqual(Poly({1: 1, 2: 2}) * Poly({1: 2, 2: 3}), Poly({2: 2, 3: 7, 4: 6}))
        self.assertEqual(Poly({1: 1, 2: 2}) * Poly({3: 3, 4: 4}), Poly({4: 3, 5: 10, 6: 8}))

        # Number and list input
        self.assertEqual(Poly([1, 2, 3]) * 4, Poly([4, 8, 12]))

        # List and dict input
        self.assertEqual(Poly([1, 2, 3]) * Poly({2: 5}), Poly({2: 5, 3: 10, 4: 15}))

        # Number and dict input
        self.assertEqual(Poly({3: 3, 4: 4}) * 2, Poly({3: 6, 4: 8}))

    def test_pow(self):
        # Wrong input type
        with self.assertRaises(TypeError):
            poly = Poly({0: 1, 2: 1, 5: 1}, symbol='y') ** 0.5

        # Wrong input value
        with self.assertRaises(ValueError):
            poly = Poly({0: 1, 2: 1, 5: 1}, symbol='y') ** (-5)

        # Number input
        self.assertEqual(Poly(-5) ** 3, Poly(-125))

        # List input
        self.assertEqual(Poly([1, 2, 3]) ** 3, Poly([1, 6, 21, 44, 63, 54, 27]))

        # Dict input
        self.assertEqual(Poly({3: 3, 4: 4}) ** 3, Poly({9: 27, 10: 108, 11: 144, 12: 64}))

    def test_divmod(self):
        # Different symbols for the indeterminate
        with self.assertRaises(ValueError):
            poly = divmod(Poly({0: 1, 2: 1, 5: 1}, symbol='y'), Poly({1: 2, 3: 4, 5: 6}, symbol='z'))

        # Zero quotient
        self.assertEqual(divmod(Poly({0: 5, 1: 2}, symbol='y'), Poly({2: 4, 3: 5}, symbol='y')),
                         (Poly(0, symbol='y'), Poly({0: 5, 1: 2}, symbol='y')))

        # Zero remainder
        self.assertEqual(divmod(Poly([-4, 6, 0, -3, 1], symbol='y'), Poly([-1, 1], symbol='y')),
                         (Poly([4, -2, -2, 1], symbol='y'), Poly(0, symbol='y')))

        # Non-zero quotient and remainder
        self.assertEqual(divmod(Poly([-3, -22, 23, -10, 2]), Poly([5, -3, 1])),
                         (Poly([1, -4, 2]), Poly([-8, 1])))

    def test_eq(self):
        # Wrong input type
        with self.assertRaises(TypeError):
            # Number input
            Poly(-5) == -5

            # List input
            Poly([1, 2, 3]) == [1, 2, 3]

            # Dict input
            Poly({3: 3, 4: 4}) == {3: 3, 4: 4}

        # Different symbols for the indeterminate
        self.assertFalse(Poly({1: 2, 3: 4, 5: 6}, symbol='x') == Poly({1: 2, 3: 4, 5: 6}, symbol='y'))

        # Different coefficients, but the same symbol
        self.assertFalse(Poly({3: 4, 5: 6}) == Poly({1: 2, 3: 4, 5: 6}))

        # Number and list input
        self.assertTrue(Poly(5, symbol='y') == Poly([5], symbol='y'))

        # List and dict input
        self.assertTrue(Poly({1: 2, 3: 4, 5: 6}, symbol='y') == Poly([0, 2, 0, 4, 0, 6], symbol='y'))

        # Number and dict input
        self.assertTrue(Poly(5, symbol='y') == Poly({0: 5}, symbol='y'))

        # Everything the same
        poly = Poly({1: 2, 3: 4, 5: 6})
        self.assertTrue(poly == Poly({1: 2, 3: 4, 5: 6}))

    def test_ne(self):
        # Wrong input type
        with self.assertRaises(TypeError):
            # Number input
            Poly(-5) != -5

            # List input
            Poly([1, 2, 3]) != [1, 2, 3]

            # Dict input
            Poly({3: 3, 4: 4}) != {3: 3, 4: 4}

        # Different symbols for the indeterminate
        self.assertTrue(Poly({1: 2, 3: 4, 5: 6}, symbol='x') != Poly({1: 2, 3: 4, 5: 6}, symbol='y'))

        # Different coefficients, but the same symbol
        self.assertTrue(Poly({3: 4, 5: 6}) != Poly({1: 2, 3: 4, 5: 6}))

        # Number and list input
        self.assertFalse(Poly(5, symbol='y') != Poly([5], symbol='y'))

        # List and dict input
        self.assertFalse(Poly({1: 2, 3: 4, 5: 6}, symbol='y') != Poly([0, 2, 0, 4, 0, 6], symbol='y'))

        # Number and dict input
        self.assertFalse(Poly(5, symbol='y') != Poly({0: 5}, symbol='y'))

        # Everything the same
        poly = Poly({1: 2, 3: 4, 5: 6})
        self.assertFalse(poly != Poly({1: 2, 3: 4, 5: 6}))


if __name__ == '__main__':
    unittest.main()
