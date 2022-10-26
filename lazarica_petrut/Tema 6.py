# Tema 6
# Exercitiul 1
pi = 3.14159

class Cerc:

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print(self.raza)
        print(self.culoare)

    def aria(self):
        return pi * self.raza**2

    def diametru(self):
        return  self.raza*2

    def circumferinta(self):
        return 2*pi*self.raza

cerc_rosu = Cerc(2, "rosu")
cerc_verde = Cerc(8, "verde")

cerc_verde.descrie_cerc()
print(cerc_rosu.aria())

# Exercitiul 2

class Dreptunghi:

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        print(self.lungime)
        print(self.latime)
        print(self.culoare)

    def aria(self):
        return self.lungime * self.latime

    def perimetru(self):
        return (self.lungime * 2) + (self.latime * 2)

    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare
        self.descrie()

dreptunghi_rosu = Dreptunghi(2, 4, "rosu")

dreptunghi_rosu.descrie()
print(dreptunghi_rosu.perimetru())

# Exercitiul 3

class Angajat:

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(self.nume)
        print(self.prenume)
        print(self.salariu)

    def nume_complet(self):
        return self.nume + " " + self.prenume

    def salariu_lunar(self):
        return self.salariu

    def salariu_anual(self):
        return self.salariu * 12

    def marire_salariu(self, procent):
        return (procent / 100) * self.salariu

ion = Angajat("Ion", "Popescu", 3000)
ion.descrie()
print(ion.salariu_lunar())
print(ion.salariu_anual())
print(ion.marire_salariu(15))

# Exercitiul 4

class Cont:

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f"Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei")

    def debitare_cont(self, suma):
        pass
    def creditare_cont(self, suma):
        pass

ion = Cont("RO1241251", "Ion Gheorghe", 2000)
ion.afisare_sold()
