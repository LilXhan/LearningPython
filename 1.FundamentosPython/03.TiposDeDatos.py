# Hay varios tipos de datos que tenemos en python, ya trabajamos con algunos de ellos pero lo veremos mas a detalle ahora mismo.


# dato tipo string (cadena de texto o cadena de caracteres), 

# se reconoce porque principalmente porque lo inicialimos con comilla doble 
# aunque tambien es posible hacerlo con comilla simple 

my_name = "Flavio"
my_name = 'Dangel'
print('my_name =>', my_name)
# aqui no imprimos la variable si no el tipo de variable que es
print(type(my_name))


# dato tipo integer o int (enteros o números)

# tiene que estar sin comillas para que sea reconocido como un número

my_age = 12
print('my_age =>', my_age)
print(type(my_age))


# dato tipo boolean (Falso o Verdadero) (True or False)
# is_single -> es_soltero

is_single = False
print('is_single =>', is_single)
print(type(is_single))


# inputs 
# los inputs asi le des un valor númerico, siempre va a tratar todo como un string y siempre te devolvera un string

my_age = input('Cual es tu edad? ')
print('my_age =>', my_age)
print(type(my_age))

