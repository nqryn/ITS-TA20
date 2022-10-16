# Tema 2
# Exercitiul 1
# If else = daca ceva este intrun anumit fel executa acea comanda,
# daca nu, atunti executa alta comanda.

# Exercitiul 2
print("Introdu un numar")
x = int(input())
if type(x) == int:
    print(f"{x} este numar natural")
else:
    print(f"{x} nu este numar natural")

# Exercitiul 3
if x > 0:
    print(f"{x} este pozitiv")
elif x < 0:
    print(f"{x} este numar negativ")
else:
    print(f"{x} este numar neutru")

# Exercitiul 4
if x > -2 and x <13:
    print(f"{x} este intre -2 si 13")
else:
    print(f"{x} NU este intre -2 si 13")

# Exercitiul 5
y = int(2)
if x > y:
    diferenta = x-y
else:
    diferenta = y-x
print(f"Diferenta dintre {x} si {y} este {diferenta}")

# Exercitiul 6
if not(x > 5 and x < 27):
    print(f"{x} nu este intre 5 si 27")

# Exercitiul 7
if x == y:
    print(f"{x} = {y}")
elif x>y:
    print(f"{x} este mai mare decat {y}")
else:
    print(f"{y} este mai mare decat {x}")

# Exercitiul 8
print("---Triunghi---")
lx = int(input("Cat este latura x\n"))
ly = int(input("Cat este latura y\n"))
lz = int(input("Cat este latura z\n"))

if lz == ly and lz == lx:
    print("triunghiul este echilateral")
elif lz == lx:
    print("triunghiul este isoscel")
elif lz == ly:
    print("triunghiul este isoscel")
elif lx == ly:
    print("triunghiul este isoscel")
else:
    print("triunghiul este oarecare")

# Exercitiul 9
print("Introdu o litera")
litera = str(input())
if(litera == 'a' or litera == 'e' or litera == 'i' or litera == 'o' or litera == 'u' or litera == 'A' or litera == 'E' or litera == 'I' or litera == 'O' or litera == 'U'):
    print("Litera ", litera, " este vocala")
else:
    print("Litera ", litera, " este consoana")

# Exercitiul 10
print("Ce nota ai la test?")
nota_test = int(input())

if nota_test >= 9:
    print("A")
elif nota_test >= 8:
    print("B")
elif nota_test >= 7:
    print("C")
elif nota_test >= 6:
    print("D")
elif nota_test > 4:
    print("E")
else:
    print("F")


