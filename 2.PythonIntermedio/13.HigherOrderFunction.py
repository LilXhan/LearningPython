
"""
    Higher Order Function -> HOF
    Funciones de Orden Superior
    
    Es que nosotros a una funcion le podemos enviar otra funcion y ejecutarla desde ahi.
"""

# Version normal

def increment(x):
    return x + 1

def high_order_function(x, funct):
    return x + funct(x)

result = high_order_function(2, increment)

print(result) # -> 2 + (2 + 1)

# uno de los grandes beneficios de los hof es poder utilizando las lambdas

increment_v2 = lambda x:x + 1
high_order_function_v2 = lambda x, func: x + func(x)

result = high_order_function_v2(4, increment_v2)
print(result)

result = high_order_function_v2(4, lambda x:x + 2)
print(result)
result = high_order_function_v2(4, lambda x:x + 4)
print(result)

# otro ejemplo

