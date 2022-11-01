# Diccionarios: Inserción y Actualizacion

person = {
    'name': 'Nico',
    'surname': 'Alvarado',
    'langs': ['Python', 'Javascript'],
    'age': 99
}

print(person)

# Como actualizar un atributo

person['name'] = "Santi"
print(person)

person['age'] -= 50
print(person)

person['langs'].append('Rust')
print(person)

# Eliminar un atributo uno de esos pares key: value

del [person['surname']]
print(person)

# Otra forma es con el metodo pop(key)

person.pop('age')
print(person)

# obtener los items de un diccionario

print("Items")
print(person.items())

print("Values")
print(person.values())

print("Keys")
print(person.keys())