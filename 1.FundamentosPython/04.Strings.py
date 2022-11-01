# Profundizaremos un poco mas con el tipo de variable string

name = "Flavio"
last_name = "Alvarado Tucto"
print(name)
print(last_name)

# Concatenando

full_name = name + " " + last_name
print(full_name)


quote = "I'm Flavio"
print(quote)

quote2 = 'She said "Hello"'
print(quote2)

# format
# una forma de python de darle estructura a nuestro texto

#template -> plantilla

# Concatenacion

template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name

print('v1 =>', template)

# Funcion Format

template = "Hola, mi nombre es {} y mi appelido es {}".format(name, last_name)

print('v2 =>', template)

template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"

print('v3 =>', template)

# RETO: Agregar una 3era variable a esa plantilla hola mi nombre es (nombre) (apellido) y mi edad es (edad) años.
# Utilizar un input para la variable edad.

age = input("Ingresa tu edad:\n")

template = f"Hola mi nombre es {name} {last_name} y mi edad es {age} años"

print(template)




