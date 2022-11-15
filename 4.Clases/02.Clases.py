# Atributos de clases -> crear variables o atributos dentro de una clase

class Usuario:
    # Atributos de clase
    username = 'Username por default'
    email = ''

# Acceder a la variable username

print(Usuario.username) # -> Username por default

# Se puede modificar el atributo o variable dentro de una clase clase

Usuario.username = 'User 1'
print(Usuario.username) # -> User 1

Usuario.email = "alvaradofeikd@gmail.com"
print(Usuario.email)