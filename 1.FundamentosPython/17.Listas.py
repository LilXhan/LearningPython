# Una estructura de dato mas importante y se trabajaras mucho con estas

# ¿Que hace interesante a una lista?
# Es que tiene bastantes funcionalidades para almacenar informacion, ya que nos permite guardar varios elementos.
# Las listas nos permite almacenar varios datos de diferentes tipos

numbers = [1, 2, 3, 4]
print(numbers)
print(type(numbers)) # <class 'list'>

tasks = ["make a dishes", "play videogames"]
print(tasks)

types = [1, "Hola", True]
print(types)

# Indexing con listas

print(numbers[0])
print(tasks[0])

# A las listas se les puede mutar, cosa que con los strings no se puede


"""
text = 'hola'
text[0] = 'm' --> nos daria error ya que un string no se puede modificar o mutar de esta manera
print(text)

LA UNICA MANERA DE MUTAR UN TEXTO ES CON UN REPLACE
 
text = "hola"
text = text.replace('h', 'm')
print(text)
"""

# Mutando o actualizando una lista

tasks[0] = "watch platzi courses"
print(tasks)

# Se puede actualizar la misma posicion las veces que queramos

tasks[0] = "do the dishes"
print(tasks)

# Slicing con listas

print(numbers[:3])

# Tambien se puede comprobar si hay o no hay un eleo en una lista

if True in types:
    print("Si hay un True")

print("Hola" in types)

