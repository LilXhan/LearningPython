"""
    Dictionary Comprehension

    {key:value for var in iterable}
"""

import random

# Version normal

dict = {}
for x in range(1, 6):
    dict[x] = x * 2

print(dict)

# Version comprehension

dict_v2 = {i:i*2 for i in range(1, 6)}
print(dict_v2)


# OTRO EJEMPLO


# Version Normal

countries = ['col', 'mex', 'bol', 'pe']

population = {}

for countrie in countries:
    population[countrie] = random.randint(1, 100)

print(population)


# Version comprehension

population_v2 = {countrie:random.randint(1, 100) for countrie in countries}
print(population_v2)


# OTRO EJEMPLO

names = ['Nico', 'Sule', 'Flavio']
ages = [12, 15, 46]

# Para unir 2 listas usamos el zip()

print(zip(names, ages)) # -> [('Nico', 12), ('Sule', 15), ('Flavio', 46)]

people = {name:age for name, age in zip(names, ages)}

print(people)