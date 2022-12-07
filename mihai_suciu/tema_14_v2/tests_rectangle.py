import pytest
from mock import patch
from pct2_rectangle import Rectangle


@pytest.fixture()
def rectangle_test():
    rectangle_4_test = Rectangle(2, 3, 'red')
    return rectangle_4_test


@patch('builtins.print')
def test_rectangle_description(mock_print, rectangle_test):
    rectangle_test.rectangle_description()
    mock_print.assert_called_with(f"Rectangle {rectangle_test.a} x {rectangle_test.b}, color {rectangle_test.color}")


@patch('builtins.print')
def test_rectangle_area(mock_print, rectangle_test):
    rectangle_test.rectangle_area()
    mock_print.assert_called_with(f"Rectangle area: 6")


@patch('builtins.print')
def test_rectangle_perimeter(mock_print, rectangle_test):
    rectangle_test.rectangle_perimeter()
    mock_print.assert_called_with(f"Rectangle perimeter: 10")


@patch('builtins.print')
def test_change_color(mock_print, rectangle_test):
    rectangle_test.change_color('blue')
    rectangle_test.rectangle_description()
    mock_print.assert_called_with(f"Rectangle {rectangle_test.a} x {rectangle_test.b}, color blue")
