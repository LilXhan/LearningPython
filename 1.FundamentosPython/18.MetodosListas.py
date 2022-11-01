# Metodos de listas

# C R U D
# Create Read Update Delete
# Crear, Leer, Actualizar y Eliminar -> Mayormente en una lista podremos hacer todo esto sin mayor dificultades

# 1. CREAR - CREATE

numbers = [1, 2, 3, 4, 5]

# 2. LEER - READ

print(numbers[1]) # Estamos leyendo la posicion número 1

# 3. ACTUALIZAR - UPDATE

numbers[4] = 10
print(numbers)

numbers.append(500) # el metodo append nos sirve para agregar un número al final de la lista
print(numbers)


# el metodo insert sirve para agregar un elemento a la posicion a la que queramos recibe 2 parametros la posicion y
# el elemento el cual queremos agregar
# insert(la posicion, elemento)
# no elimina elementos solo agrega un nuevo elemento y lo demas se corre.

numbers.insert(0, 100) 
print(numbers)

numbers.insert(3, "Lista")
print(numbers)

# metodo para unir o fusionar 2 listas

tasks = ["lavar", "trabajar", "barrer"]

new_list = numbers + tasks

# el metodo index(elemento), sirve para saber en que posicion se encuentra un elemento

index = new_list.index("lavar")

new_list[index] = "todo change"
print(new_list)


# 4. ELIMINAR - DELETE

# el metodo remove(elemento), remueve o elimina elementos de la lista o array

new_list.remove("todo change")
print(new_list)

# el metodo pop(), elimina el ultimo elemento de la lista

new_list.pop()
print(new_list)

# al metodo pop(indice), tambien se le puede dar una posicion y lo elimina

new_list.pop(0)
print(new_list)

# el metodo reverse(), transforma toda la lista al reverso

new_list.reverse()
print(new_list)

# el metodo sort(), lo que hace es ordenar, del menor al mayor

numbers_a = [3, 4, 5, 0, 2, 1]

numbers_a.sort()
print(numbers_a)

# tambien sirve para los strings, en el orden del abecedario
# OJO: NO SE PUEDE MEZCLAR UNA LISTA O ARRAY CON TIPOS MEZCLADOS OSEA SI UNA LISTA TIENE STRINGS , NUMEROS, ETC 
# NOS ARROJARA ERROR

strings_a = ["re", "a", "u", "b", "c"]

strings_a.sort()
print(strings_a)


