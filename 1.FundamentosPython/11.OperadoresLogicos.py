# Operadores logicos and y or

# and
# todas las partes de la operacion deben ser verdaderos para que me devuelva un verdadero, solo basta
# que una parte es falza para que devuelva False

print('AND')
print('True and True =>', True and True) # devuelve True
print('True and False =>', True and False) # devuelve False
print('False and True =>', False and True) # devuelve False
print('False and False =>', False and False) # devuelve False

print(10 > 5 and 5 < 10) # Devuelve True
print(10 > 5 and 5 > 10) # Devuelve False

stock = input("Ingrese el número de stock => ")
stock = int(stock)

print(stock >= 100 and stock <= 1000)

# or
# solo basta que una parte sea verdadera para que toda las partes se conviertan en verdaderas

print('OR ')
print('True or True =>', True or True) # devuelve True
print('True or False =>', True or False) # devuelve True
print('False or True =>', False or True) # devuelve True
print('False or False =>', False or False) # devuelve False

role = input("Digita el rol => ")
print(role == "admin" or role == "seller")