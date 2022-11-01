# Loops: For

# El mas usado, en el for tambien se itera, pero tenemos un numero dado de iteraciones dadas por algun elemento

# for (elemento iterador) in ()

"""
for element in range(1, 21):
    print(element)
"""

my_list = [23, 45, 67, 89, 43]
for element in my_list:
    print(element)

my_tuple = ('Flavio', 'Nico', 'Juli', 'Carla')
for element in my_tuple:
    print(element)


product = {
    'name': 'Camisa',
    'price': 100,
    'stock': 89
}

for key in product:
    print(f"{key} =>", product[key])

# Una forma mejor

for key, value in product.items():
    print(f"{key} => {value}")

# Una forma mas compleja

people = [
    {
        'name': 'Nico',
        'age': 34
    },
    {
        'name': 'Pedro',
        'age': 45
    },
    {
        'name': 'Santi',
        'age': 4
    }
]

# ¿Como iterarlo?

for person in people:
    print(person)
    print("name =>", person['name'])
    """
    for key, value in person.items():
        print(f"{key} => {value}")
    """
