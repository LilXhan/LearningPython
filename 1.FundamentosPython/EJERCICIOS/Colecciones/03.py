"""
    Dada una lista de números enteros [15,20,50,80,40,60], escriba un programa
    que dado un dato por el usuario, este sea eliminado de la lista. Tome en cuenta 
    que el usuario ingresará datos que se encuentran dentro de la lista

    Ejemplo:

    Ingrese el dato a eliminar: 60

    Salida: [15,20,50,80,40]
"""

numbers = [15, 20, 50, 80, 40, 60]

while True:
    num = int(input(f"Enter a some this numbers: {numbers}\n"))

    if not num in numbers:
        continue

    numbers.remove(num)
    print(numbers)