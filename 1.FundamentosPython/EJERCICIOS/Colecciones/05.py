"""
    Dado el diccionario que almacena la talla de algunas personas 
    {'Marcelo': 1.80, 'José':1.50, 'Oscar':1.70, 'Jorge': 1.40}, escriba un programa que dado 
    un nombre ingresado por el usuario imprime la talla.

    Ejemplo:

    Ingrese un nombre: Marcelo

    Salida: 1.80
"""

people = {
    'Marcelo': 1.80,
    'José': 1.50,
    'Oscar': 1.70,
    'Jorge': 1.40
}

while True:

    opcion_player = input(f"Choices a opcion_player: {tuple(people.keys())}\n")
    opcion_player = opcion_player.lower()
    opcion_player = opcion_player.capitalize()

    if not opcion_player in list(people.keys()):
        continue
    
    for name, tall in people.items():
        if name == opcion_player:
            print(f"His tall of {name} is {tall}")
    break;