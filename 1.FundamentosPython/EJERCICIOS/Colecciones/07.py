"""
    Guarde los datos de una persona (nombre,apellido,edad) en un diccionario, luego imprimalo en el 
    siguiente formato. "Hola mi nombre es [nombre] [apellido], y tengo [edad] años".
"""

person = {}

person['name'] = input("Ingrese su nombre:\n")
person['surname'] = input("Ingrese sus apellidos:\n")
person['age'] = int(input("Ingrese su edad:\n"))

print(f"Hola mi nombre es {person['name'] + ' ' + person['surname']}, y tengo {person['age']} años")