# Profundizaremos un poco mas con el tipo de variable int

# numero de vidas que tenemos en un videojuego
lives = 3 # lives = "3" -> tipo string
print(type(lives))

age = 12

# presupuesto de una persona
buget = 100


# Float, presicion decimal

temperature = 12.12
print(type(temperature))

# Actualizando los valores
lives = 2
print(lives)
lives = 1
print(lives)

# Operaciones

lives = 12 + 15
print(lives)

lives = lives - 1
print(lives)

# forma abreviada

lives -= 1
print(lives)

lives -= 5
print(lives)

lives += 5
print(lives)

# notaciones cientificas

number = 4500000000000000000000.1
print(number)

number_b = 0.00000000000000000000001
print(number_b)

# TIP: es una muy buena practica no solo en python si no en cualquier lenguaje de programacion, que nosotros
# solo con leerlo sepamos de que trata esa variable que estamos manipulando con ella 

# RETO: Hacer un pograma que calcule el promedio de tus gastos del mes de enero, febrero y marzo, los gatos
# pueden ser investados aqui solo buscamos que calcules el promedio.

gasto_enero = 1000
gasto_febrero = 2000
gasto_marzo = 1600

total_gastos = gasto_enero + gasto_febrero + gasto_marzo

promedio = total_gastos / 3

print(promedio)



