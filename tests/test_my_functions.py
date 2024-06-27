import pytest
import sources.my_functions as my_functions
import time
import allure
from selenium import webdriver


# pytest tests/test_my_functions.py COMMAND

# Functions based tests:


def test_add():
    result = my_functions.add(1,4)
    assert result == 5


def test_division_by_zeo():
    with pytest.raises(ValueError):
        my_functions.divide(10,0)
#    with pytest.raises(ZeroDivisionError):  #when expecting an error and want test to pass


def test_adding_strings():
    result = my_functions.add('I love ','gaming')
    assert result == 'I love gaming'


@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = my_functions.add(1, 4)
    assert result == 5


@pytest.mark.skip(reason="This feature is currently broken")
def test_add():
    assert my_functions.add(1,3) == 4


@pytest.mark.xfail(reason="We cannot divide by zeo")
def test_divide_zero_broken():
    my_functions.divide(1,0)
