import series


def test_fibonacci():
    assert series.fibonacci(0) == 0
    assert series.fibonacci(1) == 1
    assert series.fibonacci(2) == 1
    assert series.fibonacci(3) == 2
    assert series.fibonacci(4) == 3
    assert series.fibonacci(5) == 5
    assert series.fibonacci(6) == 8


def test_lucas():
    assert series.lucas(0) == 2
    assert series.lucas(1) == 1
    assert series.lucas(2) == 3
    assert series.lucas(3) == 4
    assert series.lucas(4) == 7
    assert series.lucas(5) == 11








def test_sum_series():
    assert series.sum_series(0) == 0
    assert series.sum_series(1) == 1
    assert series.sum_series(2) == 1
    assert series.sum_series(3) == 2
    assert series.sum_series(4) == 3
    assert series.sum_series(5) == 5

    assert series.sum_series(0, 2, 1) == 2
    assert series.sum_series(1, 2, 1) == 1
    assert series.sum_series(2, 2, 1) == 3
    assert series.sum_series(3, 2, 1) == 4
    assert series.sum_series(4, 2, 1) == 7
    assert series.sum_series(5, 2, 1) == 11

    assert series.sum_series(0, 3, 4) == 3
    assert series.sum_series(1, 3, 4) == 4
    assert series.sum_series(2, 3, 4) == 7
    assert series.sum_series(3, 3, 4) == 11
    assert series.sum_series(4, 3, 4) == 18
    assert series.sum_series(5, 3, 4) == 29

