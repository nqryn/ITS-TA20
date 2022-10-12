from abc import ABC


class GeometricShape(ABC):
    PI = 3.14

    def area(self):
        raise NotImplementedError

    def description(self):
        print("I most likely have corners!")


class Square(GeometricShape):

    def __init__(self, side_length):
        self.__side_length = side_length

    @property
    def side_length(self):
        return self.__side_length

    @side_length.setter
    def side_length(self, side_length):
        self.__side_length = side_length

    @side_length.getter
    def side_length(self):
        return self.__side_length

    @side_length.deleter
    def side_length(self):
        print("Square side length deleted")
        self.__side_length = None

    def area(self):
        return self.side_length**2


class Circle(GeometricShape):

    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__radius = radius

    @radius.getter
    def radius(self):
        return self.__radius

    @radius.deleter
    def radius(self):
        print("Circle radius deleted")
        self.__radius = None

    def area(self):
        return self.PI * self.radius ** 2

    def description(self):
        print("I don't have corners!")


square1 = Square(2)
circle1 = Circle(2)
print("Circle:")
circle1.description()
print(f"Circle area: {circle1.area()}")
print()
print("Square:")
square1.description()
print(f"Square area: {square1.area()}")
print('*'*40)

square1.side_length = 5  # set side length
circle1.radius = 5  # set radius

print("Circle:")
circle1.description()
print(f"Circle area: {circle1.area()}")
print()
print("Square:")
square1.description()
print(f"Square area: {square1.area()}")
print('*'*40)

print(f"Square side length: {square1.side_length}")  # get side length
del square1.side_length  # del side length
print(f"Circle radius: {circle1.radius}")  # get radius
del circle1.radius  # del radius


