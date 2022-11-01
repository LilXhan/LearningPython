# Loops: While (Mientras)

# Los ciclos es una forma de ejecutar un codigo repetitivamente 

"""
while True:
    print("Se ejecuto.\n")


counter = 0
while counter < 10:
    counter += 1
    print(f"{counter}")

# Romper el mientras

counter = 0

while counter < 20:
    counter += 1
    # Podemos detenerlo dentro del flujo
    if counter == 15:
        # el break de forma forzada de rompe el ciclo:
        break;
    print(f"{counter}")
"""

counter = 0

while counter < 20:
    counter += 1
    if counter < 15:
        # continue, lo que hace es saltar automaticamente al siguiente ciclo o iteracion
        # obviando todo lo que hay de esa linea para abajo, ¿que quiere decir? no se va a ejecutar.
        continue;
    print(f"{counter}")
