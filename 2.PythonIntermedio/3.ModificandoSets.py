# Modificando conjuntos o sets

# CRUD DE LOS SETS

set_countries = {'col', 'mex', 'bol'}

# El tamaño de este conjunto o saber cuantos elementos hay dentro de este set -> len(set)

size = len(set_countries) # -> 3
print(size)

# Saber si un elemento es dentro del conjunto o set -> in

print('pe' in set_countries) # -> False
print('col' in set_countries) # -> True

# Agregar elementos a nuestro conjunto -> add() 

set_countries.add('pe')
print(set_countries)

# Actualizar los elementos (muy similar a agregar elementos pero aqui podemos mandar un pequeño conjunto
# y todo ese conjunto se sumara al set) -> update(set)

set_countries.update({'ar', 'ecua', 'pe'})
print(set_countries)

# Remover elementos de nuestro conjunto -> remove()

set_countries.remove('col')
print(set_countries)
set_countries.remove('ar')
print(set_countries)

# set_countries.remove('ar') -> manda un error si queremos eliminar un elemento que no existe, podemos usar el metodo
# discard()

set_countries.discard('arg')
print(set_countries)

# Limpiar todo un conjunto osea eliminar exactamente todo -> clear()

set_countries.clear()
print(set_countries)
len(set_countries) # -> 0

