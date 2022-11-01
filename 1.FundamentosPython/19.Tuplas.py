# Tuplas

# Las tuplas son parecidas a las listas, pero tienen algo parecido a las cadenas de texto y es que son 
# inmutables

numbers = (1, 2, 3, 5)
strings = ("Flavio", "Juan", "Pedro")
print(numbers)
print("0 =>", numbers[0])
print("-1 =>", numbers[-1])
print(type(numbers))


print(strings)
print(type(strings))

# Si son parecidos a las listas entonces, ¿para que usamos una  tupla?
# Ejemplo en una lista teniamos algo llamado el CRUD que era crear, leer, actualizar y eliminar
# pero en cambio en una tupla solo vamos a poder hacer la declaracion pero luego yo no voy a poder insertar
# mas elementos ahi.

# LOS METODOS QUE SE PUEDEN USAR EN LAS TUPLAS

# buscar un elemento dentro de la tupla con el metodo index(elemento)

print(strings.index("Flavio"))

# contar cuantas veces se repite un elemento en la tupla con el metodo count(elemento)

print(strings.count("Juan"))

# Sin embargo ¿Podemos hacer si nos dan una tupla y realmente queremos insertar un valor? 
# Naturalmente no lo vamos a poder hacer ya que las tuplas no tienen este comportamiento

# Pero podemos usar el siguiente procedimiento: convertir la tupla a una lista y viceversa

my_list = list(strings)

my_list.append("Miguel")
my_list[0] = "Dangel"

my_tuple = tuple(my_list)
print(my_tuple)






