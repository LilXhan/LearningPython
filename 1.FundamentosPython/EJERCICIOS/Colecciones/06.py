"""
    Dado el diccionario que almacena la talla de algunas personas 
    {'Marcelo': 1.80, 'José':1.50, 'Oscar':1.70, 'Jorge': 1.40}, 
    escriba un programa que dada una talla por el usuario imprima el nombre.

    Ejemplo:

    Ingrese una talla: 1.8

    Salida: Marcelo
"""

people = {
    'Marcelo': 1.80,
    'José': 1.50,
    'Oscar': 1.70,
    'Jorge': 1.40
}

while True:
    choice_tall = float(input(f"Choice a tall: {tuple(people.values())}\n"))

    if not choice_tall in people.values():
        continue

    for name, tall in people.items():
        if tall == choice_tall:
            print(f"The tall {tall} belonging to {name}")
    break;

