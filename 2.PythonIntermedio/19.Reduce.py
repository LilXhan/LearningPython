"""
    Reduce

    Reducir algo a un solo valor
"""

# Para usar reduce enemos que importar functools

import functools

numbers = [1, 2, 3, 4]

result = functools.reduce(lambda counter, item: counter + item, numbers)
print(result) # -> 10

