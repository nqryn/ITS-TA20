from abc import ABC

"""
ABSTRACTION
Clasa abstractă FormaGeometrica
Conține un field PI=3.14
Conține o metodă abstractă aria (opțional)
Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
probabil am colturi’
"""


class FormaGeometrica(ABC):
    def aria(self):
        raise NotImplementedError

    def descrie(self):
        print("Cel mai probabil am colturi")


"""
INHERITANCE
Clasa Pătrat - moștenește FormaGeometrica
constructor pentru latură

ENCAPSULATION
    latura este proprietate privată
    Implementează getter, setter, deleter pentru latură
    Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
    implementezi metoda abstractă aria)
"""


class Patrat(FormaGeometrica):

    def __init__(self, latura):
        self.__lat = latura

    def aria(self):
        return self.__lat ** 2

    # getter
    @property
    def lat(self):
        return self.__lat

    @lat.setter
    def lat(self, new_lat):
        self.__lat = new_lat


patrat = Patrat(10)
print(patrat.lat)
print(patrat.aria())
patrat.lat = 12
print(patrat.aria())
