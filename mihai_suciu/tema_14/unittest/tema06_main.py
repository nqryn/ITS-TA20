# from pct1_circle import Circle
# from pct2_rectangle import Rectangle
from pct3_employee import Employee
# from pct4_bank_account import BankAccount
# from o1_invoice import Invoice
# from o2_car import Car
# from o3_todo import ToDoList

# """
# 1.Clasa Cerc
# Atribute: raza, culoare
# Constructor pentru ambele atribute
# Metode:
# - descrie_cerc() - va PRINTA culoarea și raza
# - aria() - va RETURNA aria
# - diametru()
# - circumferinta()
# """
# print("Pct.1:")
#
# circle1 = Circle(2, 'white')
# circle2 = Circle(3, 'black')
# circle3 = Circle(4, 'red')
#
# circle1.circle_description()
# circle2.circle_description()
# circle3.circle_description()
# print()
# circle1.circle_area()
# circle2.circle_area()
# circle3.circle_area()
# print()
# circle1.circle_diameter()
# circle2.circle_diameter()
# circle3.circle_diameter()
# print()
# circle1.circle_circumference()
# circle2.circle_circumference()
# circle3.circle_circumference()
# print()

# """
# 2. Clasa Dreptunghi
# Atribute: lungime, latime, culoare
# Constructor pentru toate atributele
# Metode:
# - descrie()
# - aria()
# - perimetrul()
# - schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
# Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
# self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
# descrie()
# """
# print("Pct.2:")
#
# rectangle1 = Rectangle(1, 2, 'yellow')
# rectangle2 = Rectangle(2, 3, 'green')
# rectangle3 = Rectangle(3, 4, 'orange')
#
# rectangle1.rectangle_description()
# rectangle2.rectangle_description()
# rectangle3.rectangle_description()
# print()
# rectangle1.rectangle_area()
# rectangle2.rectangle_area()
# rectangle3.rectangle_area()
# print()
# rectangle1.rectangle_perimeter()
# rectangle2.rectangle_perimeter()
# rectangle3.rectangle_perimeter()
# print()
# rectangle1.change_color('red')
# rectangle2.change_color('magenta')
# rectangle3.change_color('grey')
# print()
# rectangle1.rectangle_description()
# rectangle2.rectangle_description()
# rectangle3.rectangle_description()
# print()
#
"""
3. Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pt toate atributele
Metode:
- descrie()
- nume_complet()
- salariu_lunar()
- salariu_anual()
- marire_salariu(procent)
"""
print("Pct.3:")

employee1 = Employee('John', 'Smith', 1000)
employee2 = Employee('Tom', 'Hurry', 4000)
employee3 = Employee('Brad', 'Hanks', 5500)

employee1.employee_description()
employee1.employee_full_name()
employee1.employee_monthly_salary()
employee1.employee_yearly_salary()
employee1.employee_salary_raise(10)
print('-'*30)
employee1.employee_description()
employee1.employee_full_name()
employee1.employee_monthly_salary()
employee1.employee_yearly_salary()
employee1.employee_salary_raise(15)
print('-'*30)
employee1.employee_description()
employee1.employee_full_name()
employee1.employee_monthly_salary()
employee1.employee_yearly_salary()
employee1.employee_salary_raise(5)
print('-'*30)
print()

# """
# 4.Clasa Cont
# Atribute: iban, titular_cont, sold
# Constructor pentru toate atributele
# Metode:
# - afisare_sold() - Titularul x are în contul y suma de n lei
# - debitare_cont(suma)
# - creditare_cont(suma)
# """
# print("Pct.4:")
#
#
# holder1 = BankAccount('Jimmy Locking', 'GB04 1238 RONC 3123 1234', 0, 0)
# holder2 = BankAccount('Brad Button', 'GB02 1234 RONC 4195 6512', 0, 0)
# holder3 = BankAccount('Ellen Smith', 'GB07 3951 RONC 7562 7924', 0, 0)
#
# holder1.print_account_balance()
# holder1.make_a_deposit()
# holder1.print_account_balance()
# holder1.make_a_withdrawal()
# holder1.print_account_balance()
# print()
#
# """
# 1. Clasa Factura
# Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
# avea aceeași serie), număr, nume_produs, cantitate, pret_buc
# Constructor: toate atributele, fara serie
# Metode:
# - schimbă_cantitatea(cantitate)
# - schimbă_prețul(pret)
# - schimbă_nume_produs(nume)
# - generează_factura() - va printa tabelar dacă reușiți
# Factura seria x numar y
# Data: generați automat data de azi
# Produs | cantitate | preț bucată | Total
# Telefon | 7        |     700     | 49000
# """
# print("OPTIONAL:")
# print("Pct.1:")
#
# invoice1 = Invoice('0001', 'Dell  ', 1, 1200)
# invoice2 = Invoice('0002', 'Galaxy', 8, 200)
# invoice3 = Invoice('0003', 'LG 32" ', 7, 150)
#
# invoice1.generate_invoice()
# invoice2.generate_invoice()
# invoice3.generate_invoice()
# print('*'*80)
#
# invoice1.change_price(1000)
# invoice2.change_price(300)
# invoice3.change_price(200)
# invoice1.change_quantity(2)
# invoice2.change_quantity(3)
# invoice3.change_quantity(5)
# invoice1.change_product_name('Laptop')
# invoice2.change_product_name('Tablet')
# invoice3.change_product_name('Monitor')
# invoice1.generate_invoice()
# invoice2.generate_invoice()
# invoice3.generate_invoice()
# print('*'*80)
#
# """
# 2.Clasa Masina
# Atribute: marca, model, viteza maxima, viteza_actuala, culoare,
# culori_disponibile (set), inmatriculata (bool)
# Culoare = gri - toate mașinile cand ies din fabrica sunt gri
# Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
# Culori disponibile = alegeți voi 5-7 culori
# Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
# Inmatriculata = False
# Constructor: model, viteza_maxima
# Metode:
# - descrie() - se vor printa toate atributele, în afară de culori_disponibile
# - înmatriculare() - va schimba atributul înmatriculată în True
# - vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
# culoare e în opțiunea de culori disponibile, altfel afișați o eroare
# - accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e
# negativă-eroare, daca viteza e mai mare decat viteza_max - masina va
# accelera până la viteza maximă
# - franeaza() - mașina se va opri și va avea viteza 0
# """
# print("Pct.2:")
#
# car1 = Car('X1', 160)
# car2 = Car('X3', 180)
# car3 = Car('X5', 250)
#
# car1.description()
# print("Car certification:")
# car1.certification()
# car1.certification()
# print("Painting the car:")
# car1.paint('Orange')
# print(f"Car is accelerating:")
# car1.acceleration(180)
# print("Car brakes:")
# car1.car_break()
# print('*'*80)
#
# car2.description()
# print("Car certification:")
# car2.certification()
# print("Painting the car:")
# car2.paint('White')
# print(f"Car is accelerating:")
# car2.acceleration(180)
# print("Car brakes:")
# car2.car_break()
# print('*'*80)
#
# car3.description()
# print("Car certification:")
# car3.certification()
# print("Painting the car:")
# car3.paint('White')
# print(f"Car is accelerating:")
# car3.acceleration(180)
# print("Car brakes:")
# car3.car_break()
# print('*'*80)
#
# """
# 3. Clasa TodoList
# Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
# La început nu avem taskuri, dict e gol și nu avem nevoie de constructor
#
# Metode:
# - adauga_task(nume, descriere) - se va adauga in dict
# - finalizează_task(nume) - se va sterge din dict
# - afișează_todo_list() - doar cheile
# - afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului,
# printăm detalii suplimentare
#
# + Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l
# adauge.
# + Dacă acesta răspunde nu - la revedere
# + Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în dict
# """
# print("Pct.3:")
#
# task = ToDoList()
#
# task.add_task('8:00', 'breakfast')
# task.add_task('13:00', 'lunch')
# task.add_task('19:00', 'dinner')
#
# task.print_todo_list()
# task.print_todo_list_details()
# task.print_task_details('8:00')
# task.finish_task('8:00')
# task.print_todo_list()
#
# task.print_task_details('21:00')
# task.print_todo_list_details()
#
# task.finish_task('8:00')
# task.finish_task('13:00')
# task.finish_task('19:00')
# task.print_todo_list()
# task.print_todo_list_details()
