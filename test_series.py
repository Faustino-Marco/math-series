from series import fibonacci as fib
from series import lucas as luc
from series import sum_series as sum

def test_fib_input_1():
    actual = fib(1)
    expected = 1
    assert actual == expected


def test_fib_9():
    actual = fib(9)
    expected = 55
    assert actual == expected


def test_luc_0():
    actual = luc(0)
    expected = 2
    assert actual == expected


def test_luc_8():
    actual = luc(8)
    expected = 47
    assert actual == expected


def test_sum_2_start_at_3_4():
    actual = sum(2, 3, 4)
    expected = 7
    assert actual == expected


