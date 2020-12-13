import math


class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
        self.module = None
        self.angle = None
        self._convert_to_polar()

    def _convert_to_polar(self):
        self.module = math.hypot(self.real, self.img)
        self.angle = math.atan2(self.real, self.img)

    def show_complex(self):
        print(complex(self.real, self.img))

    @staticmethod
    def add(complex_1, complex_2):
        return Complex(complex_1.real + complex_2.real, complex_1.img + complex_2.img)

    @staticmethod
    def subtract(complex_1, complex_2):
        return Complex(complex_1.real - complex_2.real, complex_1.img - complex_2.img)

    @staticmethod
    def multiply(complex_1, complex_2):
        result = complex(complex_1.real, complex_1.img) * complex(complex_2.real, complex_2.img)
        return Complex(result.real, result.imag)

    @staticmethod
    def divide(complex_1, complex_2):
        result = complex(complex_1.real, complex_1.img) / complex(complex_2.real, complex_2.img)
        return Complex(result.real, result.imag)
