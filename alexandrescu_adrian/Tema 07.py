from abc import ABC
"""
ABSTRACTION
Clasa abstractă FormaGeometrica
Conține un field PI=3.14 """

class FormaGeometrica(ABC):
    Pi = 3.14

# Conține o metodă abstractă aria (opțional)

    def aria(self):
        raise NotImplementedError

# Conține o metodă a clasei descrie() - aceasta printează pe ecran "Cel mai probabil am colturi"

    def descrie(self):
        print("Cel mai probabil am colturi")


"""
INHERITANCE
Clasa Pătrat - moștenește FormaGeometrica
constructor pentru latură
"""

class Patrat(FormaGeometrica):

    def __init__(self, latura):
        self.__latura = latura

    """
    ENCAPSULATION       
    Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
    implementezi metoda abstractă aria)
    """
# latura este proprietate privată
    def latura(self):
        return self.__latura

# Implementează getter, setter, deleter pentru latură
    def get_latura(self):
        return self.__latura

    def set_latura(self, latura):
        self.__latura = latura

    def del_latura(self):
        print("latura a fost stearsa")
        self.__latura = None
    def aria(self):
        return self.latura()**2

class Cerc(FormaGeometrica):

    def __init__(self, raza):
        self.__raza = raza

    def get_raza(self):
        return self.__raza

    def del_raza(self):
        print("Raza cercului a fost stearsa")
        self.__raza = None

    def aria(self):
        return self.Pi * self.__raza**2

    def descrie(self):
        print("Eu nu am colturi")



patrat1 = Patrat(10)

print("Patrat:")
patrat1.descrie()
print(f"Aria patratului este: {patrat1.aria()}")
print("-"*20)
cerc1 = Cerc(8)
print("Cerc:")
cerc1.descrie()
print(f"Aria cercului este {cerc1.aria()}")
print("-"*20)
