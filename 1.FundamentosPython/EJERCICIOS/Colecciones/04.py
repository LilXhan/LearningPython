"""
    Dada una tupla de números (1,3,5,2,7,5,5,8,4,8,4,8,4), escriba un programa que dado 
    un elemento por el usuario, imprima el número de veces que se encuentra en la tupla.

    Ejemplo:

    Ingrese el elemento a contar: 4

    Salida: 3
"""

tuple = (1, 3, 5, 2, 7, 5, 5, 8, 4, 8, 4, 8, 4)

while True:
    num = int(input(f"Enter a number of the next list: {tuple}\n"))

    if not num in tuple:
        continue;

    print(f"Is repeated {tuple.count(num)} times")
    break;
