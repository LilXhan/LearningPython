"""
    Dictionary Comprehension with Conditionals

    {key:value for var in iterable if condition}
"""

import random

countries = {'col', 'mex', 'bol', 'pe'}

population = {country:random.randint(1, 100) for country in countries}

print(population)

result = {country:population for country, population in population.items() if population > 20}
print(result)

# Otro ejemplo

text = 'hola soy flavio'
# vowels = ['a', 'e', 'i', 'o', 'u']

unique_vowels = {c:text.count(c) for c in text if c.lower() in 'aeiou'} # 'aeiou' -> patron
print(unique_vowels)


