class Rectangle:

    def __init__(self, a, b, color):
        self.a = a
        self.b = b
        self.color = color

    def rectangle_description(self):
        print(f"Rectangle {self.a} x {self.b}, color {self.color}")

    def rectangle_area(self):
        area = self.a * self.b
        print(f"Rectangle area: {area}")
        return area

    def rectangle_perimeter(self):
        perimeter = 2 * (self.a + self.b)
        print(f"Rectangle perimeter: {perimeter}")
        return perimeter

    def change_color(self, color):
        self.color = color
