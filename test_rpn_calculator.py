import pytest
from rpn_calculator import RpnCalculator


def test_push():
    calc = RpnCalculator()

    calc.push(0)


@pytest.mark.parametrize("i, r",
                         [(0, 0),
                          (1, 1),
                          (-1, -1)])
def test_pop(i, r):
    calc = RpnCalculator()
    calc.push(i)

    v = calc.pop()

    assert v == r


@pytest.mark.parametrize("i, j, r",
                         [(0, 1, 1),
                          (3, 2, 2),
                          (-1, -2, -2)])
def test_result(i, j, r):
    calc = RpnCalculator()
    calc.push(i)
    calc.push(j)

    v = calc.result()

    assert v == r


@pytest.mark.parametrize("i, j, r1, r2",
                         [(1, 2, 1, 2),
                          (-1, 1, -1, 1),
                          (0, 1, 0, 1)])
def test_stack(i, j, r1, r2):
    calc = RpnCalculator()
    calc.push(i)
    calc.push(j)

    s = calc.stack()

    assert s == [r1, r2]


def test_clear():
    calc = RpnCalculator()
    calc.push(1)
    calc.push(2)

    assert calc.stack()

    calc.clear()

    assert not calc.stack()


@pytest.mark.parametrize("i, j, exp",
                         [(1, 2, 3),
                          (0, 1, 1),
                          (-1, 1, 0)])
def test_add(i, j, exp):
    calc = RpnCalculator()
    calc.push(i)
    calc.push(j)

    calc.add()

    r = calc.result()
    assert r == exp


@pytest.mark.parametrize("i, j, expected",
                         [(3, 2, 1),
                          (0, 1, -1),
                          (1, 1, 0)])
def test_sub(i, j, expected):
    calc = RpnCalculator()
    calc.push(i)
    calc.push(j)

    calc.sub()

    r = calc.result()
    assert r == expected


@pytest.mark.parametrize("i, j, expected",
                         [(1, 2, 2),
                          (-1, 2, -2),
                          (2, 3, 6)])
def test_mul(i, j, expected):
    calc = RpnCalculator()
    calc.push(i)
    calc.push(j)

    calc.mul()

    r = calc.result()
    assert r == expected


@pytest.mark.parametrize("i, j, expected",
                         [(6, 3, 2),
                          (-10, 5, -2),
                          (9, 3, 3)])
def test_div(i, j, expected):
    calc = RpnCalculator()
    calc.push(i)
    calc.push(j)

    calc.div()

    r = calc.result()
    assert r == expected


@pytest.mark.parametrize("i, expected",
                         [(100, 10),
                          (9, 3),
                          (64, 8)])
def test_sqrt(i, expected):
    calc = RpnCalculator()
    calc.push(i)

    calc.sqrt()

    r = calc.result()
    assert r == expected
