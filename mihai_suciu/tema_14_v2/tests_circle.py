import pytest
from mock import patch
from pct1_circle import Circle


@pytest.fixture
def circle_test():
    circle_4_test = Circle(2, 'red')
    return circle_4_test


@patch('builtins.print')
def test_circle_description(mock_print, circle_test):
    circle_test.circle_description()
    mock_print.assert_called_with(f"Radius: {circle_test.radius} Color: {circle_test.color}")


@patch('builtins.print')
def test_circle_area(mock_print, circle_test):
    circle_test.circle_area()
    mock_print.assert_called_with(f"Circle area: 12.56")


@patch('builtins.print')
def test_circle_diameter(mock_print, circle_test):
    circle_test.circle_diameter()
    mock_print.assert_called_with(f"Circle diameter: 4")


@patch('builtins.print')
def test_circle_circumference(mock_print, circle_test):
    circle_test.circle_circumference()
    mock_print.assert_called_with(f"Circle circumference: 12.56")
