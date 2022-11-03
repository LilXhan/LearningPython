"""
    Escribir una función encontrar_2 que reciba por parámetro dos cadenas:
    cadena y subcadena. Retornar la posición de la subcadena si esta se encuentra 
    dentro de la cadena y -1 si no se encuentra. No usar find().

    Ejemplo: si los argumentos son “abbbccda” y “bbc” entonces se retorna 2.
"""

def encontrar_2(str, str_2):
    posicion = 0
    if str.count(str_2):
        var = len(str_2) 
        for x in range(len(str)):
            if str[x:var + x] == str_2:
                break
            else:
                print(str[x:var + x])
                posicion += 1
        return posicion
    else:
        return -1

print(encontrar_2('abbbccda', 'cc'))

a = "abbbccda"
print(a[0:2])