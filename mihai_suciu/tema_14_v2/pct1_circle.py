class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def circle_description(self):
        print(f"Radius: {self.radius} Color: {self.color}")

    def circle_area(self):
        area = 3.14*(self.radius**2)
        print(f"Circle area: {area}")

    def circle_diameter(self):
        diameter = 2*self.radius
        print(f"Circle diameter: {diameter}")

    def circle_circumference(self):
        circumference = 2*3.14*self.radius
        print(f"Circle circumference: {circumference}")
