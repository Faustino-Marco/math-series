from series import fibonacci as fib
from series import lucas as luc
from series import sum_series as sum

def test_fib_input_0():
    actual = fib(0)
    expected = 0
    assert actual == expected


def test_fib_1():
    actual = fib(1)
    expected = 1
    assert actual == expected


def test_luc_0():
    actual = luc(0)
    expected = 2
    assert actual == expected


def test_luc_1():
    actual = luc(1)
    expected = 1
    assert actual == expected


def test_sum_2_start_at_3_4():
    actual = sum(2, 3, 4)
    expected = 7
    assert actual == expected


