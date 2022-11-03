# Funciones lambda

# Funcion normal

def increment(x):
    return x + 1

# version lambda

inscrement_v2 = lambda x:x + 1

result = increment(10)
result_v2 = inscrement_v2(10)
print(result) # -> 11
print(result_v2) # -> 11

# OTRO EJEMPLO

full_name = lambda name, surname:(f"{name} {surname}").title()


print(full_name("flavio", "alvarado tucto")) # -> Flavio Alvarado Tucto
