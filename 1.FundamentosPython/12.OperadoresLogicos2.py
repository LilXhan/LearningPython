# Operador logico not

# Negar una operacion booleana

print(not(True)) # devuelve False
print(not(False)) # devuelve True

# and

print('AND')
print('not True and True =>', not (True and True)) # devuelve False
print('not True and False =>', not (True and False)) # devuelve True
print('not False and True =>', not (False and True)) # devuelve True
print('not False and False =>', not (False and False)) # devuelve True

stock = input("Ingrese el stock => ")
stock = int(stock)
print(not (stock >= 100 and stock <= 1000))