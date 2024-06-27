import pytest
import math
import sources.shapes as shapes


# for testing multiple values
@pytest.mark.parametrize("side_length, expected_area", [(5, 25), (3, 9), (2, 4), (4, 16)])
def test_multiple_square_areas(side_length, expected_area):
    assert shapes.Square(side_length).area() == expected_area


@pytest.mark.parametrize("side_length, expected_perimeter", [(5, 20), (3, 12), (2, 8), (4, 16)])
def test_multiple_square_areas(side_length, expected_perimeter):
    assert shapes.Square(side_length).perimeter() == expected_perimeter
