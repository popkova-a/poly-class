# poly-class

A Python implementation of a polynomial class over the real numbers $\mathbb{R}$. Supports human-readable string representation, arithmetic operations, and equality comparison. Includes a full `unittest` test suite.

---

## Project Structure

```
.
├── poly/
│   ├── __init__.py      # Exposes Poly from poly.module
│   └── module.py        # Poly class implementation
├── tests/
│   ├── __init__.py      # Package initializer
│   └── test_poly.py     # unittest test suite
└── __main__.py          # Entry point — discovers and runs all tests
```

---

## Module

### `poly/module.py`

Contains the `Poly` class — the sole public interface of the package.

#### `Poly`

Represents a univariate polynomial over $\mathbb{R}$. Coefficients are stored internally as a `dict` mapping integer exponents to `float` values. Zero-coefficient terms are automatically dropped, except for the zero polynomial which is stored as `{0: 0.0}`.

**Constructor:**

```python
Poly(coef, symbol='x')
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `coef` | `Number`, `list`, `tuple`, `dict`, `np.ndarray` | Polynomial coefficients. For sequences, index `i` is the coefficient of `x^i`. For dicts, keys are exponents and values are coefficients. |
| `symbol` | `str` | Indeterminate symbol used in string representation. Defaults to `'x'`. |

**Properties:**

- `symbol` — Returns the indeterminate symbol.
- `coef` — Returns the internal coefficient dictionary `{exponent: coefficient}`.
- `degree` — Returns the highest exponent with a non-zero coefficient.

**Methods:**

- `copy()` — Returns a deep copy of the polynomial as a new `Poly` instance.

**Dunder methods:**

| Method | Operator | Description |
|--------|----------|-------------|
| `__len__` | `len(p)` | Number of terms with non-zero coefficients. |
| `__str__` | `str(p)` | Human-readable representation, e.g. `x^5 + 3.0*x^2 - 1.0`, sorted by descending degree. |
| `__add__` | `p + q` | Polynomial addition. Right operand may be a scalar. |
| `__sub__` | `p - q` | Polynomial subtraction. Right operand may be a scalar. |
| `__neg__` | `-p` | Negation (multiplies all coefficients by -1). |
| `__mul__` | `p * q` | Polynomial multiplication. Right operand may be a scalar. |
| `__pow__` | `p ** n` | Raises a polynomial to a non-negative integer power. |
| `__divmod__` | `divmod(p, q)` | Returns `(quotient, remainder)` via polynomial long division. |
| `__eq__` | `p == q` | Returns `True` if both symbol and coefficients are identical. |
| `__ne__` | `p != q` | Returns `True` if symbol or coefficients differ. |

Comparison operators (`==`, `!=`) only accept another `Poly` instance and raise `TypeError` otherwise. Binary arithmetic operators raise `ValueError` if the two operands use different indeterminate symbols.

**Static method:**

- `_div_monomials(divisible, divisor, symbol)` — Internal helper that divides two single-term polynomials (monomials). Used by `__divmod__` during long division.

---

## Tests

### `tests/test_poly.py`

A `unittest.TestCase` subclass (`TestPoly`) with one test method per feature. Each method covers correct behaviour, type errors, value errors, and edge cases such as zero polynomials, all-zero coefficient inputs, and mixed input types.

| Test method | What it covers |
|-------------|----------------|
| `test_init` | All valid and invalid constructor inputs across every accepted type. |
| `test_symbol` | Default and custom indeterminate symbols. |
| `test_coef` | Coefficient storage and zero-term elimination for all input types. |
| `test_degree` | Degree computation including the all-zero case. |
| `test_copy` | Instance equality, type, and memory independence of copies. |
| `test_div_monomials` | Edge cases for the internal monomial division helper. |
| `test_len` | Length counting after zero-term removal. |
| `test_str` | String formatting for constants, monomials, and full polynomials. |
| `test_add` | Addition with scalars and polynomials of various input types. |
| `test_sub` | Subtraction with scalars and polynomials of various input types. |
| `test_neg` | Unary negation across all input types. |
| `test_mul` | Multiplication with scalars and polynomials of various input types. |
| `test_pow` | Integer powers including zero power; rejects floats and negative integers. |
| `test_divmod` | Zero quotient, zero remainder, and mixed quotient/remainder cases. |
| `test_eq` | Equality by symbol and coefficients; rejects non-`Poly` comparands. |
| `test_ne` | Inequality by symbol and coefficients; rejects non-`Poly` comparands. |

---

## Dependencies

```
numpy
```

Install with:

```bash
pip install numpy
```

---

## Usage

```python
from poly import Poly

p = Poly([1, 0, 1])        # 1 + x^2
q = Poly({0: -1, 1: 2})    # -1 + 2x

print(p + q)               # x^2 + 2.0*x
print(p * q)               # 2.0*x^3 - x^2 + 2.0*x - 1.0
print(p ** 2)              # x^4 + 2.0*x^2 + 1.0

quotient, remainder = divmod(p, q)
```

---

## Running Tests

```bash
python -m pytest
```

Or using the built-in runner:

```bash
python __main__.py
```
