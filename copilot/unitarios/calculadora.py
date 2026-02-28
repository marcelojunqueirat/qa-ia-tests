from math import sqrt, pow, sin, cos, tan

class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Divisão por zero")
        return a / b

    def pow(self, a, b):
        return pow(a, b)

    def sqrt(self, a):
        if a < 0:
            raise ValueError("Raiz quadrada de número negativo")
        return sqrt(a)

    def sin(self, a):
        return sin(a)

    def cos(self, a):
        return cos(a)

    def tan(self, a):
        return tan(a)
