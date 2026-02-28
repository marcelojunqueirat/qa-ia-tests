import pytest
from calculadora import Calculator


class TestCalculator:
    @pytest.fixture
    def calc(self):
        return Calculator()

    def test_add(self, calc):
        assert calc.add(2, 3) == 5
        assert calc.add(-1, 1) == 0
        assert calc.add(0, 0) == 0

    def test_sub(self, calc):
        assert calc.sub(5, 3) == 2
        assert calc.sub(0, 5) == -5
        assert calc.sub(10, 10) == 0

    def test_mul(self, calc):
        assert calc.mul(2, 3) == 6
        assert calc.mul(-2, 3) == -6
        assert calc.mul(0, 100) == 0

    def test_div(self, calc):
        assert calc.div(6, 2) == 3
        assert calc.div(5, 2) == 2.5
        assert calc.div(-10, 2) == -5

    def test_div_by_zero(self, calc):
        with pytest.raises(ZeroDivisionError, match="Divisão por zero"):
            calc.div(10, 0)

    def test_pow(self, calc):
        assert calc.pow(2, 3) == 8
        assert calc.pow(5, 0) == 1
        assert calc.pow(2, -1) == 0.5

    def test_sqrt(self, calc):
        assert calc.sqrt(4) == 2
        assert calc.sqrt(9) == 3
        assert calc.sqrt(0) == 0

    def test_sqrt_negative(self, calc):
        with pytest.raises(ValueError, match="Raiz quadrada de número negativo"):
            calc.sqrt(-1)

    def test_sin(self, calc):
        assert calc.sin(0) == 0
        assert abs(calc.sin(3.14159/2) - 1) < 0.001
        assert abs(calc.sin(3.14159) - 0) < 0.001

    def test_cos(self, calc):
        assert calc.cos(0) == 1
        assert abs(calc.cos(3.14159/2) - 0) < 0.001
        assert abs(calc.cos(3.14159) - (-1)) < 0.001

    def test_tan(self, calc):
        assert calc.tan(0) == 0
        assert abs(calc.tan(3.14159/4) - 1) < 0.001
        assert abs(calc.tan(3.14159) - 0) < 0.001
