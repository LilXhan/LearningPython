# Diccionarios: Definición y Lectura

# Se comportan el como los diccionarios en la vida real, donde tu buscas una palabra (key) y esa palabra esta
# relacionada a una definicion o un valor (value)

# Llave (Key), Valor (Value)

my_dict = {}
print(type(my_dict))

my_dict = {
    'name': 'Flavio',
    'last_name': 'Alvarado',
    'age': 89
}

print(my_dict)

# Saber cuantos elementos hay dentro del diccionario -> len(dict)

print(len(my_dict)) # esto nos muestra cuantas parejas tenemos clave y valor

# Como yo puedo leer el valor de una key en este diccionario

print(my_dict['name'])
print(my_dict['last_name'])

# Tambien podemos hacer esto, la diferencia es que en mi get si no existe el valor y nos devuelve None
# None -> no hay nada definido ahi
# recomendable usar get(valor) si no estamos seguros de que exista la key

print(my_dict.get('un valor')) # -> None

# Si no estas seguro que una llave esta dentro de un diccionario, lo podemos validar con un in

print('avion' in my_dict) # -> devuelve False
print('name' in my_dict) # -> devuelve True

