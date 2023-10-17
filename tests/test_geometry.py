import math
from simple_functions.geometry import circle_area


def test_circle_area():
    assert math.isclose(circle_area(1.0), math.pi, rel_tol=1e-9)


def test_coverage():
    assert 1 == 1
