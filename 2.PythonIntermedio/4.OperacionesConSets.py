"""
    Operaciones entre conjuntos (fundamentales dentro de la teoria de conjuntos)

    Union (une 2 conjuntos y deja los elementos sin duplicar)
    Interseccion (Cuales son los elementos que tienen en comun un conjunto con el otro)
    Diferencia (Trata de dejar los elementos del primer conjunto removiendole del segundo conjunto)
    Diferencia Simetrica (Que el resultado de un conjunto es practicamente es la union pero sin la interseccion)
"""

# Union -> union()

set_a= {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

set_c = set_a.union(set_b)
# Tambien se puede con un operador:
set_c = set_a | set_b

print(set_c) # -> {'col', 'pe', 'bol', 'mex'}

# Interseccion -> intersection()

set_c = set_a.intersection(set_b)
# Tambien se puede con un operador
set_c = set_a & set_b

print(set_c) # -> {'bol'}

# Diferencia -> difference()

set_c = set_a.difference(set_b)
# Tambien se puede hacer con un operador
set_c = set_a - set_b

print(set_c) # -> {'col', 'mex'}

# Diferencia Simetrica

set_c = set_a.symmetric_difference(set_b)
# Tambien se puede hacer con un operador
set_c = set_a ^ set_b

print(set_c)








