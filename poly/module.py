import numpy as np
from typing import Union
from numbers import Number


class Poly:
    def __init__(self, coef: Union[Number, list, tuple, dict, np.ndarray], symbol: str = 'x'):
        """
        Initializes the polynomial.

        :param coef:    constants in front of the indeterminate extents
        :param symbol:  symbol denoting the polynomial indeterminate
        """

        if not(isinstance(coef, (Number, list, tuple, dict, np.ndarray)) and isinstance(symbol, str)):
            raise TypeError("The input must be of the appropriate type.")

        if isinstance(coef, Number):
            if np.isnan(coef) or np.isinf(coef):
                raise ValueError("Coefficients must be well-defined.")

            self._coef = {0: float(coef)}

        elif isinstance(coef, dict):
            if len(coef) == 0:
                raise ValueError("Coefficients are not provided.")

            if any(map(lambda x: not(isinstance(x, int)), coef.keys())):
                raise TypeError("Exponents must be the int type.")

            if any(map(lambda x: x < 0, coef.keys())):
                raise ValueError("Exponents must be greater than or equal to zero.")

            if any(map(lambda x: not(isinstance(x, Number)), coef.values())):
                raise TypeError("Coefficients must be of the Number type.")

            if any(map(lambda x: np.isnan(x) or np.isinf(x), coef.values())):
                raise ValueError("Coefficients must be well-defined.")

            self._coef = {idx: float(c) for idx, c in coef.items() if c != 0.0}

        else:
            if len(coef) == 0:
                raise ValueError("Coefficients are not provided.")

            if any(map(lambda x: not(isinstance(x, Number)), coef)):
                raise TypeError("Coefficients must be of the Number type.")

            if any(map(lambda x: np.isnan(x) or np.isinf(x), coef)):
                raise ValueError("Coefficients must be well-defined.")

            self._coef = {idx: float(c) for idx, c in enumerate(coef) if c != 0.0}

        if len(self._coef) == 0:
            self._coef = {0: 0.0}

        self._symbol = symbol

    @property
    def symbol(self):
        """
        Gets the symbol.

        :return:  symbol denoting the polynomial indeterminate
        """

        return self._symbol

    @property
    def coef(self):
        """
        Gets the coefficients.

        :return:  constants in front of the indeterminate extents
        """

        return self._coef

    @property
    def degree(self):
        """
        Returns the maximum degree of the polynomial indeterminates.

        :return:  degree of the polynomial
        """

        return max(self._coef.keys())

    def copy(self):
        """
        Copies the polynomial object.

        :return:  polynomial duplicate
        """

        return Poly(self._coef, symbol=self.symbol)

    @staticmethod
    def _div_monomials(divisible, divisor, symbol: str = 'x'):
        """
        Divides the greater degree monomial by the smaller degree monomial.

        :param divisible:  greater degree monomial
        :param divisor:    smaller degree monomial
        :param symbol:     symbol denoting the polynomial indeterminate
        :return:           quotient of the division
        """

        if not(isinstance(divisible, Poly)):
            divisible = Poly(divisible, symbol=symbol)

        if not(isinstance(divisor, Poly)):
            divisor = Poly(divisor,  symbol=symbol)

        if (len(divisible) != 1) or (len(divisor) != 1):
            raise ValueError("The input is supposed to be monomials.")

        if divisible.symbol != divisor.symbol:
            raise ValueError("Monomial symbols differ.")

        if divisible.degree < divisor.degree:
            raise ValueError("The divisible must have a greater or equal degree comparing to the divisor.")

        if (divisor.degree == 0) and (divisor.coef[0] == 0):
            raise ZeroDivisionError("Division by zero.")

        divisible_tup = list(divisible.coef.items())[0]
        divisor_tup = list(divisor.coef.items())[0]
        res = {divisible_tup[0] - divisor_tup[0]: divisible_tup[1] / divisor_tup[1]}

        return Poly(res, symbol=divisible.symbol)

    def __len__(self):
        """
        Computes the length of the polynomial.

        :return:  number of monomials with non-zero coefficients
        """

        return len(self._coef)

    def __str__(self):
        """
        Produces the human-readable string representation for the polynomial.

        :return:  polynomial string representation
        """

        if (len(self._coef) == 1) and (self._coef.get(0) is not None):
            return str(self._coef[0])
        else:
            poly_string = ''
            for idx, c in sorted(self._coef.items(), key=lambda x: -x[0]):
                if (len(poly_string) != 0) and (c > 0):
                    poly_string += '+ '
                elif (len(poly_string) != 0) and (c < 0):
                    poly_string += '- '
                elif (len(poly_string) == 0) and (c < 0):
                    poly_string += '-'

                if idx > 1:
                    if np.isclose(abs(c), 1.0):
                        poly_string += f'{self._symbol}^{idx} '
                    else:
                        poly_string += f'{abs(c)}*{self._symbol}^{idx} '
                elif idx == 1:
                    if np.isclose(abs(c), 1.0):
                        poly_string += f'{self._symbol} '
                    else:
                        poly_string += f'{abs(c)}*{self._symbol} '
                else:
                    poly_string += str(abs(c))

        poly_string = poly_string.strip()

        return poly_string

    def __add__(self, other):
        """
        Computes the sum of two polynomials.

        :param other:  polynomial summand
        :return:       sum of two polynomials
        """

        if not isinstance(other, Poly):
            other = Poly(other, symbol=self.symbol)
        elif self._symbol != other.symbol:
            raise ValueError("Polynomial symbols differ.")

        res_coef = self._coef.copy()
        for idx, c in other.coef.items():
            res_coef[idx] = res_coef.get(idx, 0.0) + c

        return Poly(res_coef, symbol=self.symbol)

    def __sub__(self, other):
        """
        Computes the difference between two polynomials.

        :param other:  polynomial subtrahend
        :return:       the difference between two polynomials
        """

        if not isinstance(other, Poly):
            other = Poly(other, symbol=self.symbol)
        elif self._symbol != other.symbol:
            raise ValueError("Polynomial symbols differ.")

        res_coef = self._coef.copy()
        for idx, c in other.coef.items():
            res_coef[idx] = res_coef.get(idx, 0.0) - c

        return Poly(res_coef, symbol=self.symbol)

    def __neg__(self):
        """
        Computes the negation of the polynomial.

        :return:  initial polynomial multiplied by (-1)
        """

        res_coef = dict(map(lambda x: (x[0], -x[1]), self._coef.items()))
        return Poly(res_coef, symbol=self.symbol)

    def __mul__(self, other):
        """
        Computes the product of two polynomials.

        :param other:  polynomial multiplier
        :return:       product of two polynomials
        """

        if not isinstance(other, Poly):
            other = Poly(other, symbol=self.symbol)
        elif self._symbol != other.symbol:
            raise ValueError("Polynomial symbols differ.")

        res_coef = {}
        for idx1, c1 in self._coef.items():
            for idx2, c2 in other.coef.items():
                res_coef[idx1 + idx2] = res_coef.get(idx1 + idx2, 0.0) + c1 * c2

        return Poly(res_coef, symbol=self.symbol)

    def __pow__(self, power, modulo=None):
        """
        Computes an integer power of the polynomial.

        :param power:  exponent
        :return:       polynomial raised to an integer power
        """

        if not isinstance(power, int):
            raise TypeError("The power must be of the int type.")

        res = Poly(1.0, symbol=self.symbol)
        if power < 0:
            raise ValueError("The power must be greater than or equal to zero.")
        elif power > 0:
            for i in range(power):
                res *= self

        return res

    def __divmod__(self, other):
        """
        Computes the quotient and the remainder of two polynomials in a tuple

        :param other:  polynomial divisor
        :return:       tuple that contains quotient and remainder of the division
        """

        if not isinstance(other, Poly):
            other = Poly(other, symbol=self.symbol)
        elif self._symbol != other.symbol:
            raise ValueError("Polynomial symbols differ.")

        if self.degree < other.degree:
            return Poly(0, symbol=self.symbol), self

        residual = self.copy()
        divisor_max = dict([max(other.coef.items(), key=lambda x: x[0])])
        quotient = Poly(0, symbol=self.symbol)
        while residual.degree >= other.degree:
            residual_max = dict([max(residual._coef.items(), key=lambda x: x[0])])
            quotient_cur = self._div_monomials(Poly(residual_max, symbol=self.symbol),
                                               Poly(divisor_max, symbol=self.symbol))
            residual -= quotient_cur * other
            quotient += quotient_cur

        return quotient, residual

    def __eq__(self, other):
        """
        Returns True if two polynomials are equal.

        :param other:  compared polynomial
        :return:       boolean comparison result
        """

        if not isinstance(other, Poly):
            raise TypeError("The compared entity must of the Poly type.")

        if self._symbol != other.symbol:
            return False
        elif self._coef != other.coef:
            return False
        else:
            return True

    def __ne__(self, other):
        """
        Returns True if two polynomials are different.

        :param other:  compared polynomial
        :return:       boolean comparison result
        """

        if not isinstance(other, Poly):
            raise TypeError("The compared entity must of the Poly type.")

        if self._symbol != other.symbol:
            return True
        elif self._coef != other.coef:
            return True
        else:
            return False
