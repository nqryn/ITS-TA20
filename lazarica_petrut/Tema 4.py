# Tema 4
# Exercitiul 1
print("Exercitiul 1")

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']

print("> For")
for i in masini:
    print(f"Mașina mea preferată este {i}")

z = 0
print("> While")
while z < len(masini):
    print(f"Mașina mea preferată este {masini[z]}")
    z += 1

# Exercitiul 2
print("Exercitiul 2")



# Exercitiul 3
print("Exercitiul 3")

var_mercedes = "Mercedes"
for i in masini:
    if i == var_mercedes:
        print("> Am găsit mașina dorită de dvs")
        break
    else:
        print(f"Am găsit mașina {i}. Mai căutam")

# Exercitiul 4
print("Exercitiul 4")

nu_masina = ["Lăstun", "Trabant"]
for i in masini:
    if i not in nu_masina:
        print(f"S-ar putea să vă placă mașina {i}")

# Exercitiul 5
print("Exercitiul 5")

masini_vechi = []

for i in masini:
    if i in nu_masina:
        masini_vechi.append(i)
        #masini = ["Tesla" if i in nu_masina else i for i in masini] #"Functioneaza dar nu prea inteleg cum"
for i in range(len(masini)):
    if masini[i] in nu_masina:
        masini[i] = "Tesla"

print(f"Modele vechi {masini_vechi}")
print(f"Modele noi {masini}")

# Exercitiul 6
print("Exercitiul 6")

pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}
masini_buget = []
for key,value in pret_masini.items():
    if value <= 15000:
        print(key, "=", value)
        masini_buget.append(key)
print(f"Pentru un buget de sub 15000 euro puteți alege mașina:\n{masini_buget}")

# Exercitiul 7
print("Exercitiul 7")

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
list_count = 0
for i in numere:
    if i == 3:
        list_count += 1
print(f"Nr. '3' apare de {list_count} ori")

# Exercitiul 8
print("Exercitiul 8")

suma_nr = 0
for i in numere:
    suma_nr += i
print(f"Suma listei este {suma_nr}")

# Exercitiul 9
print("Exercitiul 9")

nr_mare = 0
for i in numere:
    if i > nr_mare:
        nr_mare = i
print(f"Cel mai mare numar este {nr_mare}")

# Exercitiul 10
print("Exercitiul 10")

nr_negativ = []
for i in numere:
    if i >= 0:
        nr_negativ.append(i * (-1))
    else:
        nr_negativ.append(i)
print(f"Numerele negative sunt {nr_negativ}")




































