"""
    Contar el número de espacios en un string dado.
"""

def counter(str):
    return str.count(" ")
str = input("Ingrese una oracion:\n")
result = counter(str)
print(f"El número de espacios en tu oracion es de: {result}")

