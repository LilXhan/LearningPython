"""
Escribir una función contador_elementos_lista que reciba como parámetro una lista anidada 
L de números y un número n. La función cuenta el número de listas anidadas que contienen un 
elemento en particular.

Plantee 2 formas de solución.

Ejemplo 1:

L = [[1, 3], [5, 7], [1, 11], [1, 15, 7], [5, 6, 21]] n = 1 Entonces la función retornará 3.

Ejemplo 2:

L = [['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']] n = 'B' Entonces la función retornará 2.
"""

#1era forma

L = [[1, 3], [5, 7], [1, 11], [1, 15, 7], [5, 6, 21]]

def contador_elementos_lista(l, n):
    contador = 0
    for item in L:
        for num in item:
            if num == n:
                contador += 1
    return contador

print(contador_elementos_lista(L, 5))

# 2da forma

L2 = [['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']] 

def contador_elementos_lista_v2(l, s):
    list_compr = [i for i in l if i.count(s)]
    return len(list_compr)

print(contador_elementos_lista_v2(L2, "B"))