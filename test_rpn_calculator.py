import pytest

from assertpy import assert_that
from rpn_calculator import RpnCalculator


def test_push():
    calc = RpnCalculator()

    calc.push(0)


@pytest.mark.parametrize(
    "i, j, k, expected", [(1, 2, 3, 3), (-1, -2, -3, -3), (-1, 0, 1, 1)]
)
def test_push_multiple(i, j, k, expected):
    calc = RpnCalculator()

    calc.push(i, j, k)

    v = calc.result()

    assert_that(v).is_equal_to(expected)


def test_push_no_values():
    calc = RpnCalculator()

    calc.push()


@pytest.mark.parametrize("i, expected", [(0, 0), (1, 1), (-1, -1)])
def test_pop(i, expected):
    calc = RpnCalculator()
    calc.push(i)

    v = calc.pop()

    assert_that(v).is_equal_to(expected)


@pytest.mark.parametrize("i, j, expected", [(0, 1, 1), (3, 2, 2), (-1, -2, -2)])
def test_result(i, j, expected):
    calc = RpnCalculator()
    calc.push(i, j)

    v = calc.result()

    assert_that(v).is_equal_to(expected)


@pytest.mark.parametrize(
    "i, j, expected", [(1, 2, [1, 2]), (-1, 1, [-1, 1]), (0, 1, [0, 1])]
)
def test_stack(i, j, expected):
    calc = RpnCalculator()
    calc.push(i, j)

    stack = calc.stack()

    assert_that(stack).is_equal_to(expected)


def test_clear():
    calc = RpnCalculator()
    calc.push(1, 2)

    assert_that(calc.stack()).is_not_empty()

    calc.clear()

    assert_that(calc.stack()).is_empty()


@pytest.mark.parametrize("i, j, expected", [(1, 2, 3), (0, 1, 1), (-1, 1, 0)])
def test_add(i, j, expected):
    calc = RpnCalculator()
    calc.push(i, j)

    calc.add()

    v = calc.result()
    assert_that(v).is_equal_to(expected)


@pytest.mark.parametrize("i, j, expected", [(3, 2, 1), (0, 1, -1), (1, 1, 0)])
def test_sub(i, j, expected):
    calc = RpnCalculator()
    calc.push(i, j)

    calc.sub()

    v = calc.result()
    assert_that(v).is_equal_to(expected)


@pytest.mark.parametrize("i, j, expected", [(1, 2, 2), (-1, 2, -2), (2, 3, 6)])
def test_mul(i, j, expected):
    calc = RpnCalculator()
    calc.push(i, j)

    calc.mul()

    v = calc.result()
    assert_that(v).is_equal_to(expected)


@pytest.mark.parametrize("i, j, expected", [(6, 3, 2), (-10, 5, -2), (9, 3, 3)])
def test_div(i, j, expected):
    calc = RpnCalculator()
    calc.push(i, j)

    calc.div()

    v = calc.result()
    assert_that(v).is_equal_to(expected)


@pytest.mark.parametrize("i, expected", [(100, 10), (9, 3), (64, 8)])
def test_sqrt(i, expected):
    calc = RpnCalculator()
    calc.push(i)

    calc.sqrt()

    v = calc.result()
    assert_that(v).is_equal_to(expected)
