from math import exp, sin, cos


class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __repr__(self) -> str:
        return str(self.real) + "+" + str(self.imaginary) + "i"

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def _complex_test(func):
        def inner(self, other):
            if not isinstance(other, ComplexNumber):
                other = ComplexNumber(other, 0)
            return func(self, other)

        return inner

    @_complex_test
    def __add__(self, other):
        return ComplexNumber(
            self.real + other.real, self.imaginary + other.imaginary
        )

    __radd__ = __add__

    @_complex_test
    def __mul__(self, other):
        return ComplexNumber(
            (self.real * other.real - self.imaginary * other.imaginary),
            (self.imaginary * other.real + self.real * other.imaginary),
        )

    __rmul__ = __mul__

    @_complex_test
    def __sub__(self, other):
        return ComplexNumber(
            self.real - other.real, self.imaginary - other.imaginary
        )

    def __rsub__(self, other):
        return ComplexNumber(other - self.real, -1 * self.imaginary)

    @_complex_test
    def __truediv__(self, other):
        return ComplexNumber(
            (self.real * other.real + self.imaginary * other.imaginary)
            / (other.real ** 2 + other.imaginary ** 2),
            (self.imaginary * other.real - self.real * other.imaginary)
            / (other.real ** 2 + other.imaginary ** 2),
        )

    def __rtruediv__(self, other):
        return ComplexNumber(
            other / (self.real ** 2 + self.imaginary ** 2),
            -1 * other / (self.real ** 2 + self.imaginary ** 2),
        )

    def __abs__(self):
        return (self.real ** 2 + self.imaginary ** 2) ** 0.5

    def conjugate(self):
        return ComplexNumber(self.real, self.imaginary * -1)

    def exp(self):
        return ComplexNumber(
            exp(self.real) * cos(self.imaginary),
            exp(self.real) * sin(self.imaginary),
        )
