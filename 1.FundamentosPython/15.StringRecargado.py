# Vamos a aprender mucho mas de los strings

# in buscara si la cadena esta dentro del texto devuele True si esta dentro y False si no.
# OJO: Tambien son sensibles a las mayusculas, osea que si uno tiene mayuscula y el otro no no se considerara
# como si fueran iguales.



text = "Ella sabe programar en Python"

"""
print("Javascript" in text) -> devuelve False, ya que la cadena "Javascript" no esta dentro del texto
print("Python" in text) -> devuelve True, ya que la cadena "Python" si se encuentra en el texto
print("python" in text) -> devuelve Fase, ya que uno empieza con mayuscula y el otro no

if "JS" in text:
    print("Elegiste el mejor lenguaje de pogramación para principiantes.")
else:
    print("Tambien elegiste bien.")
"""

# METODOS STRING

# Metodo para evaluar el tamaño de un string, el metodo len()
# este metodo examina el tamaño en el número de caracteres, tambien se cuentan los espacios

size = len(text)
print(size)

# Metodo para volver todo un string a mayusculas, el metodo upper()
# este metodo vuelve toda la cadena a mayusculas

print(text)
print(text.upper())

# Metodo para volver todo un string a miniscula, el metodo lower()
# este metodo vuelve todo el texto a miniscula

print(text)
print(text.lower())

# Metodo para contar el número de apariciones que tiene una letra en especifico o una cadena, el metodo count()
# este metodo cuenta cuantas veces se repite el string que le pasemos

print(text.count("a"))

# Metodo para transformar los caracteres de un string, las mayusculas las pasa a minisculas y las minisculas a mayusculas
# el metodo swapcase()

print(text.swapcase())

# Metodo para saber si un texto inicia con algo en especifico, el metodo startwith()
# Metodo para saber si un texto termina con algo en especifico, el metodo endswith()

print(text.startswith("Ella")) # devuelve True, porque el texto si comienza con Ella
print(text.endswith("Rust")) # devuelve False, porque el texto no termina con Rust

# Metodo para reemplazar un pedazo del string por otro, el metodo replace()

print(text.replace("Python", "Go"))

text_2 = "este es un titulo"
print(text_2)

# Metodo para poner el primer termino en mayuscula, el metodo capitalize()

print(text_2.capitalize())

# Metodo para poner el inicio de cada una de las palabras en mayuscula, el metodo title()

print(text_2.title())

# esta funcion nos dice si este texto es potencialmente un número, la funcion es isdigit()

age = "18" 
name = "Pedrito"

print(age.isdigit()) # devuelve True, ya que es considerado potencialmente como un número
print(name.isdigit()) # devuelve False, ya que no es considerado potencialmente un numero ya que son todo letras

# RETO: DEL JUEGO DE PIEDRA PAPEL Y TIJERA TRANSFORMA EL INPUT DEL USUARIO A MINISCULAS