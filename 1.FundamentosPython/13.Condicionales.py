# Condicionales

if True:
    print("deberia ejecutarse") # si se ejecuta

if False:
    print("no deberia ejecutarse") # no se ejecuta

"""
pet = input("¿Cual es tu mascota favorita?\n")

if pet == "perro":
    print("Genial tienes buen gusto.")

if pet == "gato":
    print("Espero tengas suerte.")

if pet == "pez":
    print("Eres lo maximo.")
"""

"""
stock = input("Digita el stock:\n")
stock = int(stock)
if stock >= 100 and stock <= 1000:
    print("Stock correcto.")
else:
    print("Stock incorrecto")
"""

pet = input("¿Cual es tu mascota favorita?\n")

if pet == "perro":
    print("Genial tienes buen gusto.")
elif pet == "gato":
    print("Espero tengas suerte.")
elif pet == "pez":
    print("Eres lo maximo.")
else:
    print("No tienes ninguna mascota interesante.")

# RETO: CREA UN POGRAMA QUE DEVUELVA SI EL NÚMERO ES PAR O IMPAR

num = input("Ingrese el número que desea evaluar:\n")
residuo = int(num) % 2

if residuo == 0:
    print("Es par.")
else:
    print("Es impar.")
