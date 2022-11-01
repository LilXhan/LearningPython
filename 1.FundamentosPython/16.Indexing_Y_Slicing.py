# Conceptos Indexing y Slicing

text = "Ella sabe Python"

# Indexing -> los textos tienen un indicador, un indicador con el cual yo puedo ingresar a nivel de posiciones

print(text[0]) # nos retorna el caracter que este en esa posicion 0
print(text[1]) # nos retorna el caracter que este en la posicion 1
# print(text[999]) -> si le damos una posicion que no existe nos da error

# ¿Como hariamos para ingresar a la ultima posicion?

print(text[-1]) # nos devuelve el ultimo caracter del string
print(text[-2]) # nos devuelve el penultimo caracter del string 


# Slicing -> basado en las posiciones de nuestro string, podemos sacar ciertas partes del texto

print(text[0:5]) # en este caso el 5 no lo toma, tomaria un número anterior osea desde el 0 a 4
print(text[10:16]) # devuelve Python
print(text[:10]) # nos devuelve todo el string desde el punto 0 hasta 10

print(text[5:]) # nos devuelve desde el punto 5 hasta el final
print(text[:]) # va desde el inicio y hasta el final

print(text[10:16:2]) # el número de saltos
print(text[::2]) # del inicio al final y saltar de dos a dos


