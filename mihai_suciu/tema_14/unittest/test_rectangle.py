from pct2_rectangle import Rectangle


def test_rectangle_description():
    rec_test = Rectangle(1, 2, 'red')
    assert rec_test.a == 1 and rec_test.b == 2 and rec_test.color == 'red'


def test_rectangle_area():
    rec_test = Rectangle(1, 2, 'red')
    assert rec_test.rectangle_area() == 2


def test_rectangle_perimeter():
    rec_test = Rectangle(1, 2, 'red')
    assert rec_test.rectangle_perimeter() == 6


def test_change_color():
    rec_test = Rectangle(1, 2, 'red')
    rec_test.change_color('yellow')
    assert rec_test.color == 'yellow'
