# Vamos aprender de transformar de un tipo a otro quiere decir que un de un número vamos a poder transformalo a un string
# o viceversa tambien veremos si ¿podremos convertir un booleano a un string?

# Cambiar de forma dinamica

name = "Flavio"
print(type(name))

name = 12
print(type(name))

name = True
print(type(name))

print("Flavio" + " Molina") # concatena los dos strings
print(10 + 20) # como son números va a realizar una operacion matematica

# No se puede hacer esto, porque no sabe si lo concatena o lo suma

# print("Flavio" + 30) -> ERROR
print("Flavio" + "30")

#######################################################################################################################

age = 12
# print("Mi edad es " + age) -> nos dara un error, porque ese mas no va hacer la concatenacion entre diferentes tipos
# la solucion es volver edad a un string.

print("Mi edad es " + str(age))
print(f"Mi edad es {age}") # -> automaticamente transforma todo lo que este adentro a string


age = input('Escribe tu edad => ') # input siempre nos devuelve una cadena
print(type(age))
# print(f"Tu edad en 10 años sera {age + 10}")  -> ERROR 

age = int(age)
print(f"Tu edad en 10 años sera {age + 10} años")

# ¿Pero que pasa si en el input ingresa un nombre, como reaccionaria python?
# Nos dara error, no podemos transformar cualquier string a un número.
# porque python no puede convertir una cadena de texto a un entero
# Mas adelante veremos como solucionar esto.

