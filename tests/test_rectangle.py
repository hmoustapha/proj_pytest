import pytest
import sources.shapes as shapes
import math


def test_area(my_rectangle):
    assert my_rectangle.area() == 20*10


def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == (20*2) + (10*2)


def test_not_equal(my_rectangle, weird_rectangle):
    assert my_rectangle != weird_rectangle
