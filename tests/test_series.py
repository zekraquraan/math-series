import pytest
from series.series import fibonacci
from series.series import lucas
from series.series import sum_series



# /////////////test_lucas/////////
def test_lucas_one():
    actual=lucas(1)
    excepted=1
    assert actual == excepted

def test_lucas_zero():
    actual=lucas(0)
    excepted=2
    assert actual == excepted

def test_lucas_two():
    actual=lucas(2)
    excepted=3
    assert actual == excepted

def test_lucas_three():
    actual=lucas(3)
    excepted=4
    assert actual == excepted

def test_lucas_therteen():
    actual=lucas(13)
    excepted=521
    assert actual == excepted


def test_lucas_string():
    actual=lucas("5")
    excepted="please inter a number"
    assert actual == excepted




# /////////////test_fibonacci/////////
def test_fibonacci_one():
    actual=fibonacci(1)
    excepted=1
    assert actual == excepted

def test_fibonacci_zero():
    actual=fibonacci(0)
    excepted=0
    assert actual == excepted

def test_fibonacci_two():
    actual=fibonacci(2)
    excepted=1
    assert actual == excepted

def test_fibonacci_three():
    actual=fibonacci(3)
    excepted=2
    assert actual == excepted

def test_fibonacci_therteen():
    actual=fibonacci(13)
    excepted=233
    assert actual == excepted


def test_fibonacci_string():
    actual=fibonacci("5")
    excepted="please inter a number"
    assert actual == excepted



# /////////////test_sum_series/////////
def test_sum_series_zero_fibonaci():
    actual=sum_series(0,0,1)
    excepted=0
    assert actual == excepted

def test_sum_series_one_fibonaci():
    actual=sum_series(1,0,1)
    excepted=1
    assert actual == excepted

def test_sum_series_zero_lucas():
    actual=sum_series(0,0,2)
    excepted=2
    assert actual == excepted

def test_sum_series_one_lucas():
    actual=sum_series(1,0,2)
    excepted=1
    assert actual == excepted

def test_sum_series_two_fibonaci():
    actual=sum_series(2,0,1)
    excepted=1
    assert actual == excepted

def test_sum_series_two_lucas():
    actual=sum_series(2,0,2)
    excepted=3
    assert actual == excepted

def test_sum_series_three_fibonacci():
    actual=sum_series(3,0,1)
    excepted=2
    assert actual == excepted

def test_sum_series_three_lucas():
    actual=sum_series(3,0,2)
    excepted=4
    assert actual == excepted

def test_sum_series_therteen_fibonacci():
    actual=sum_series(13,0,1)
    excepted=233
    assert actual == excepted

def test_sum_series_therteen_lucas():
    actual=sum_series(13,0,2)
    excepted=521
    assert actual == excepted


def test_sum_series_three():
    actual=sum_series(3,3,4)
    excepted=11
    assert actual == excepted

def test_sum_series_four():
    actual=sum_series(4,3,4)
    excepted=18
    assert actual == excepted

def test_sum_series_five():
    actual=sum_series(5,8,9)
    excepted=69
    assert actual == excepted

def test_sum_series_six():
    actual=sum_series(6,7,8)
    excepted=99
    assert actual == excepted

def test_sum_series_six():
    actual=sum_series("6",7,9)
    excepted="please inter a number"
    assert actual == excepted