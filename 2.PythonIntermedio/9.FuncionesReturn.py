"""
    Normalmente una funcion recibe unos parametros, por ejemplo la suma y deberia retornarme la respuesta de esa suma
    para posteriormente usarlo.
"""

# Version normal

suma = 0

for x in range(1, 10):
    suma += x

# print(suma) # -> 45

# Version con funcion
# Las funciones pueden retornar un valor 

def sum_with_range(min, max):
    print(min, max)
    sum = 0
    for x in range(min, max):
        sum += x
    return sum

# result = sum

result = sum_with_range(1, 10)
print(result)
result_2 = sum_with_range(result, result + 10)
print(result_2)
