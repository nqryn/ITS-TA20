# Tema 3
# Exercitiul 1
print("Exercitiul 1")

note_muzicale = ["do", "re", "mi", "fa", "so", "la", "si", "do"]
print(note_muzicale)
note_muzicale = note_muzicale[::-1]
print(note_muzicale)
note_muzicale.reverse()
print(note_muzicale)

# Exercitiul 2
print("Exercitiul 2")

numar_do = note_muzicale.count("do")
print(f"'do' apare de {numar_do} ori")

# Exercitiul 3
print("Exercitiul 3")

lista1 = [3,1,0,2]
lista2 = [6,5,4]

lista_unita = lista1 + lista2
print(lista_unita)

unpack_list = [*lista1, *lista2]
print(unpack_list)

lista1.append(lista2)
print(lista1)

# Exercitiul 4
print("Exercitiul 4")

lista_unita.sort()
print(lista_unita)

lista_unita.sort(reverse=True)
print(lista_unita)
# nu inteleg cum sa sortez numarul 0

# Exercitiul 5
print("Exercitiul 5")

if len(lista_unita) > 0:
    print(f"Lista nu este goală. Lista are {len(lista_unita)} elemente")
else:
    print("Lista este goală.")

# Exercitiul 6
print("Exercitiul 6")

lista_unita.clear()
print(lista_unita)

# Exercitiul 7
print("Exercitiul 7")

if len(lista_unita) > 0:
    print(f"Lista nu este goală. Lista are {len(lista_unita)} elemente")
else:
    print("Lista este goală.")

# Exercitiul 8
print("Exercitiul 8")

dict1 = {
    "Ana": 8,
    "Gigel": 10,
    "Dorel": 5
         }
elevi = dict1.keys()
print(elevi)

# Exercitiul 9
print("Exercitiul 9")

print(f" Ana a luat nota {dict1.get('Ana')}\n Gigel a luat nota {dict1.get('Gigel')}\n Dorel a luat nota {dict1.get('Dorel')}")

# Exercitiul 10
print("Exercitiul 10")

dict1["Dorel"] = 6
print(f"Dorel are nota {dict1.get('Dorel')}")

# Exercitiul 11
print("Exercitiul 11")

dict1.pop("Gigel")
dict1["Ionica"] = 9
print(dict1)

# Exercitiul 12
print("Exercitiul 12")

zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
zile_sapt.add('luni')

print(zile_sapt)

# Exercitiul 13
print("Exercitiul 13")

if set(weekend).issubset(set(zile_sapt)):
    print("Weekend este un subset al zilelor din săptămâna")
else:
    print("Weekend nu un subset al zilelor din săptămâna")

# Exercitiul 14
print("Exercitiul 14")

diferenta_set = zile_sapt.difference(weekend)
print(diferenta_set)

# Exercitiul 15
print("Exercitiul 15")

intersectie_set = zile_sapt.intersection(weekend)
print(intersectie_set)