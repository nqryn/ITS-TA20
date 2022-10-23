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
    Pi = 3.14

    def aria(self):
        raise NotImplementedError

    def descrie(self):
        print("Cel mai probabil am colturi")


"""
INHERITANCE
Clasa Pătrat - moștenește FormaGeometrica
constructor pentru latură
"""

class Patrat(FormaGeometrica):

    def __init__(self, lat):
        self.__lat = lat

    """
    ENCAPSULATION
    latura este proprietate privată
    Implementează getter, setter, deleter pentru latură
    Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
    implementezi metoda abstractă aria)
    """

    def latura(self):
        return self.__lat

    def get_latura(self):
        return self.__lat

    def set_latura(self, latura):
        self.__lat = latura

    def del_latura(self):
        print("latura a fost stearsa")
        self.__lat = None
    def aria(self):
        return self.latura()**2

class Cerc(FormaGeometrica):

    def __init__(self, raza):
        self.__r = raza

    def get_raza(self):
        return self.__r

    def del_raza(self):
        print("Raza cercului a fost stearsa")
        self.__r = None

    def aria(self):
        return self.Pi * self.__r**2

    def descrie(self):
        print("Eu nu am colturi")





patrat1 = Patrat(3)

print("Patrat:")
patrat1.descrie()
print(f"Aria patratului este: {patrat1.aria()}")
print("-"*50)
cerc1 = Cerc(5)
print("Cerc:")
cerc1.descrie()
print(f"Aria cercului este {cerc1.aria()}")
print("-"*50)

cerc1.descrie()