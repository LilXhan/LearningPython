"""
    List Comprehension:

    Listas con una sintaxis mas corta, y por ende mas facil de ver

    [element for element in iterable]

    - Podemos recorrer listas, tuplas y un conjunto

    List Comprehension con condiciones:

    [element for element in iterable if condition]
"""

# Version Normal

numbers = []
for x in range(1, 11):
    if x % 2 == 0:
        numbers.append(x * 2)

print(numbers)

# Version List Comprehension 

# element lo obtenemos del iterable for element in range(1, 11)

numbers_v2 = [element * 2 for element in range(1, 11) if element % 2 == 0]
print(numbers_v2)