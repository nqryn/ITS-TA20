# Tema 5
# Exercitiul 1
print("Exercitiul 1")

nr_a = int(input("1 Scrie un nr\n"))
nr_b = int(input("2 Scrie un nr\n"))
def suma_mea(a, b):
    return a + b

print(f"Suma ta este {suma_mea(nr_a, nr_b)}")


# Exercitiul 2
print("Exercitiul 2")

def functie_numere_pare(numar):
    if numar % 2 == 0:
        return True
    else:
        return False

numar = int(input("Introdu un numar\n"))
print(functie_numere_pare(numar))

# Exercitiul 3
print("Exercitiul 3")

def nume_return(a, b, c):
    return len(a + b + c)

nume = str(input("Introdu numele:\n"))
prenumele1 = str(input("Introdu primul prenumele:\n"))
prenumele2 = str(input("Introdu cel de al doilea prenumele:\n"))

print(f"Lungimea numelui este {nume_return(nume, prenumele1, prenumele2)}")

# Exercitiul 4
print("Exercitiul 4")

def aria_dreptunghiului(lungime, latime):
    return lungime * latime

lungime = int(input("Introdu lungimea dreptunghiului\n"))
latime = int(input("Introdu latimea dreptunghiului\n"))

print(f"Aria draptunghiului este {aria_dreptunghiului(lungime, latime)}")

# Exercitiul 5
print("Exercitiul 5")

def aria_cercului(raza):
    pi = 3.14159
    return pi * (raza ** 2)

raza = int(input("Introdu raza cerului\n"))
print(f"Aria cercului este {aria_cercului(raza)}")

# Exercitiul 6
print("Exercitiul 6")

def gaseste_caracter(caracter, string1):
    if caracter in string1:
        return True
    else:
        return False

string1 = str(input("Scrie un cuvant\n"))
caracter = str(input("Ce caracter cauti?\n"))
print(gaseste_caracter(caracter, string1))

# Exercitiul 7
print("Exercitiul 7")

# Exercitiul 8
print("Exercitiul 8")

lista = []
lista_pozitiva = []

def functie_lista():
    for i in lista:
        if i >= 0:
            lista_pozitiva.append(i)

for i in range(5):
    nr = int(input(f"Introdu nr {i}/5 in lista:\n"))
    lista.append(nr)

functie_lista()

print(lista_pozitiva)

# Exercitiul 9
print("Exercitiul 9")

def functie_nr_mic_mare():
    if nr1 > nr2:
        print(f"Primul număr {nr1} este mai mare decat al doilea {nr2}")
    elif nr2 > nr1:
        print(f"Al doilea {nr2} este mai mare decat primul {nr1}")
    else:
        print("Numerele sunt egale.")

nr1 = int(input("1 Introdu un nr:\n"))
nr2 = int(input("2 Introdu un nr:\n"))

functie_nr_mic_mare()

# Exercitiul 10
print("Exercitiul 10")

set1 = set()

def functie_set():
    if input_set not in set1:
        print("Am adaugat numărul nou în set")
        return True
    else:
        print("Nu am adaugat numărul în set. Acesta există deja")
        return False


for i in range(5):
    input_set = int(input(f"Introdu nr {i}/5 in set\n"))
    functie_set()
    set1.add(input_set)

print(set1)
