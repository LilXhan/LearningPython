"""
    Escribir un programa que reciba por teclado la edad de 3 personas ingresadas por 
    el usuario y determinar la edad del más joven entre ellos.
"""

contador = 0
low = 1000000

while contador < 3:
        contador += 1
        num = int(input(f"Enter {contador}° age:\n"))

        if num < low:
            low = num

print(f"The youngest age is {low} years.")