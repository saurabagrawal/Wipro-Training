# import pytest
#
# from src.calculations import add, sub, mul, div, ne
#
#
# def test_add():
#     res = add(10,5)
#     assert res == 15, 'Addition Error'
#
# def test_sub():
#     res = sub(10,5)
#     assert res == 5, 'subtraction Error'
#
# def test_mul():
#     res = mul(10,5)
#     assert res == 50, 'multiplication Error'
#
# def test_div():
#     res = div(10,5)
#     assert res == 2.0, 'division Error'
#
# def test_ne():
#     res = ne(10,5)
#     assert res == True, 'NE'
#
# def test_driver():
#     with pytest.raises(ZeroDivisionError):
#         div(10, 0)

import pytest

from src.calculations import Calculations

class TestCalculations:

    calc = Calculations()


    def test_add(self):
        res = self.calc.add(10, 5)
        assert res == 15, 'Addition Error'

    def test_sub(self):
        res = self.calc.sub(10, 5)
        assert res == 5, 'subtraction Error'

    def test_mul(self):
        res = self.calc.mul(10, 5)
        assert res == 50, 'multiplication Error'

    def test_div(self):
        res = self.calc.div(10, 5)
        assert res == 2.0, 'division Error'
    def test_ne(self):
        res = self.calc.ne(10, 10)
        assert res == True, 'NE'

    # def test_driver(self):
    #     with pytest.raises(ZeroDivisionError):
    #         self.calc.div(10, 0)


