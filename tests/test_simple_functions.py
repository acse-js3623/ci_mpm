import pytest
import math
from simple_functions import sin, my_sum, factorial

class TestSimpleFunctions(object):
    '''Class to test our simple functions are working correctly'''

    @pytest.mark.parametrize('iterable, expected', [
        ([8, 7, 5], 20),
        ((10, -2, 5, -10, 1), 4)
    ])
    def test_my_add(self, iterable, expected):
        '''Test our add function'''
        isum = my_sum(iterable)
        assert isum == expected

    @pytest.mark.parametrize('number, expected', [
        (5, 120),
        (3, 6),
        (1, 1)
    ])
    def test_factorial(self, number, expected):
        '''Test our factorial function'''
        answer = factorial(number)
        assert answer == expected

    def test_sin_identity(self):
        for angle in range(0, 360, 10):
            radians = math.radians(angle)
            result = sin(radians)
            expected = math.sin(radians)
            assert math.isclose(result, expected, rel_tol=1e-9)
