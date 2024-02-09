from random import randint

import pytest

from numeric_notation_parser import notation_to_integer_generator


def test_simple_formating():
    for id in [randint(-1000, 1000) for _ in range(10)]:
        assert list(notation_to_integer_generator(str(id))) == [id]


def test_multples_simple_formating():
    assert list(notation_to_integer_generator("10,20,30,42,0,-100")) == [10, 20, 30, 42, 0, -100]


def test_range_formating():
    assert list(notation_to_integer_generator("0-10")) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert list(notation_to_integer_generator("10-0")) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert list(notation_to_integer_generator("-20--25")) == [-20, -21, -22, -23, -24, -25]


def test_range_with_step():
    assert list(notation_to_integer_generator("0-10/2")) == [0, 2, 4, 6, 8, 10]
    assert list(notation_to_integer_generator("0-10/3")) == [0, 3, 6, 9]
    assert list(notation_to_integer_generator("10-0/3")) == [10, 7, 4, 1]


def test_with_everything():
    assert list(notation_to_integer_generator("42,100,-100,20-30/2,0--1")) == [42, 100, -100, 20, 22, 24, 26, 28, 30, 0, -1]
