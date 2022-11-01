"""
    Dada una lista L, escribir un programa que cree una
    nueva lista sin los elementos duplicados. Utilice operador in o not in.

    Si la lista es [500,100,200,300,200,100,600,400,800,400,500,900] el programa debe 
    crear una nueva lista que contenga [500, 100, 200, 300, 600, 400, 800, 900]
"""

numbers = [500, 100, 200, 300, 200, 100, 600, 400, 800, 400, 500, 900]

new_list = []

for number in numbers:
    if not number in new_list:
        new_list.append(number)

print(new_list)