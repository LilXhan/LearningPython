"""
    Higher Order Function y Lambda Function

    Funcion Map:

    Map su funcion principal es hacer transformaciones a una lista dadas de elementos, se dan normalmente
    bajo las listas
"""


numbers = [1, 2, 3, 4]

# Transformando cada uno de los elementos

# Version Normal

numbers_v2 = []

for i in numbers:
    numbers_v2.append(i * 2)

print(numbers_v2)

# Version map

numbers_v3 = list(map(lambda x:x * 2, numbers)) # -> [2, 4, 6, 8]
print(numbers_v3)

# Otro ejemplo

numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7]

result = list(map(lambda x, y: x + y, numbers_1, numbers_2)) # -> [6, 8, 10]
print(result)
