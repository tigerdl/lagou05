import pytest

from get_data import get_yaml_data
from pythoncode.calculator import Calculator



class TestCalc:
    def setup_class(self):
        self.calc = Calculator()

    @pytest.mark.parametrize("a,b,expect",get_yaml_data()[0])
    def test_add(self,a,b,expect):
        result = self.calc.add(a,b)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", get_yaml_data()[0])
    def test_sub(self, a, b, expect):
        result = self.calc.sub(a, b)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", get_yaml_data()[0])
    def test_mul(self, a, b, expect):
        result = self.calc.mul(a, b)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", get_yaml_data()[0])
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        assert result == expect
