from pct1_circle import Circle


def test_circle_description():
    circle_test = Circle(2, 'blue')
    assert circle_test.radius == 2 and circle_test.color == 'blue'


def test_circle_area():
    circle_test = Circle(2, 'blue')
    assert circle_test.circle_area() == 12.56


def test_circle_diameter():
    circle_test = Circle(2, 'blue')
    assert circle_test.circle_diameter() == 4


def test_circle_circumference():
    circle_test = Circle(2, 'blue')
    assert circle_test.circle_circumference() == 12.56

