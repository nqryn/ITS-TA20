# Tema 1
# Exercitii obligatorii

# 1
# Variabilele sunt cuti cu etichete in care putem stoca diferite tipuri de date.

# 2
#String
mystring = "Salut"
#Intiger
myintiger = 99
#Float
myfloat = 2.0
#Bool
mybool = False
notmybool = True

# 3
print (type(mystring), mystring, type(myintiger), myintiger, type(myfloat), myfloat, type(mybool), mybool, type(notmybool),notmybool)

# 4
myfloat = round(myfloat)
print(type(myfloat), myfloat)

# 5
myfloat = float(myfloat)
print(mystring)
print(myintiger)
print(myfloat)
print(mybool)

# 6
nume = str(input("Care este numele tau?\n"))
prenume = str(input("Care este prenumele tau?\n"))
print(F"Te numesti {nume} {prenume}!")
print(F"Si are {len(nume)+len(prenume)} caratere")

# 7
lungime=int(input("Introduceti lungimea\n"))
latimea=int(input("Introduceti latimea\n"))
print(f"Aria dreptunghiului este {lungime*latimea}")

# 8,9,10
string8= "Coral is either the stupidest animal or the smartest rock"
numarat = string8.count("the")
print(f"Cuvantul 'the' apare de {numarat} ori in textul 'Coral is either the stupidest animal or the smartest rock'")
assert string8 == int, "Aceasta variabila nu este numar"