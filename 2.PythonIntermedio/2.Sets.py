"""
    Sets o Conjuntos

    Tiene que ver con esta teoria de conjuntos, un conjunto tiene o agrupa elementos que tienen algo en común.
    
    Ejemplo:

    paises_de_america = {'Perú', 'Mexico', 'Argentina'}

    Caracteristicas:

    - Se pueden modificar -> A un conjunto lo podemos modificar (Agregar, 
    quitar elementos y hasta unirlos con otros conjuntos )
    - No tienen orden
    - No permite duplicados -> Yo no puedo tener 2 veces el mismo elemento
"""

# Definiendo nuestro primer conjunto, se habran con llaves como los diccionarios, solo que aqui no tenemos parejas
# de key y value, si no que directamente solo tendra los elementos

# set_countries = {'col', 'mex', 'bol', 'col'} -> en este caso tenemos 2 'col' pero automaticamente el conjunto
# eliminara el elemento repetido y solo dejara uno ya que no acepta elementos duplicados

set_countries = {'col', 'mex', 'bol'}
print(set_countries)
print(type(set_countries))

set_numbers = {1, 2, 2, 443, 23}
print(set_numbers)
print(type(set_numbers))

set_typles = {1, 'Hola', False, 1.5}
print(set_typles) # al imprimir set_typles nos cambia el orden pero no nos debe importar, no importa el orden que le demos.
print(type(set_typles))

# creando un conjunto o set apartir de un string

set_from_string = set('hoola')
print(set_from_string)

# creando un conjunto apartir de una tupla

set_from_tuple = set(('abc', 'cbv', 'as', 'abc'))
print(set_from_tuple)

# Solo números no repetidos

numbers = [1, 2, 3, 1, 2, 3, 4]
set_numbers = set(numbers)
print(set_numbers)
unique_numbers = list(set_numbers)
print(unique_numbers)

# Para que vamos a usar los conjuntos, un caso practico seria, si queremos eliminar elementos duplicados
# de una lista











