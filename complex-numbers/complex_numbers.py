import math


class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __repr__(self) -> str:
        return str(self.real) + "+" + str(self.imaginary) + "i"

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(
                self.real + other.real, self.imaginary + other.imaginary
            )
        else:
            return ComplexNumber(self.real + other, self.imaginary)

    __radd__ = __add__

    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(
                (self.real * other.real - self.imaginary * other.imaginary),
                (self.imaginary * other.real + self.real * other.imaginary),
            )
        else:
            return ComplexNumber(self.real * other, self.imaginary * other)

    __rmul__ = __mul__

    def __sub__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(
                self.real - other.real, self.imaginary - other.imaginary
            )
        else:
            return ComplexNumber(self.real - other, self.imaginary)

    def __rsub__(self, other):
        return ComplexNumber(other - self.real, -1 * self.imaginary)

    def __truediv__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(
                (self.real * other.real + self.imaginary * other.imaginary)
                / (other.real ** 2 + other.imaginary ** 2),
                (self.imaginary * other.real - self.real * other.imaginary)
                / (other.real ** 2 + other.imaginary ** 2),
            )
        else:
            return ComplexNumber(self.real / other, self.imaginary / other)

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
            math.exp(self.real) * math.cos(self.imaginary),
            math.exp(self.real) * math.sin(self.imaginary),
        )
