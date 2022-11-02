"""
    Parametros por defecto y multiples returns
"""

# Parametros con valores por defecto

def find_volume(length = 1, width = 1, depth = 1):
    return length * width * depth, width, "Hola" # -> (20, 20, 'hola') retornamos multiples valores y lo convierte 
    # en una tupla.

result, width, string = find_volume(width = 20) #  width = 20 -> solo le enviamos este dato en caso solo el width
print(result)
print(width)
print(string)




