# Comparando flotantes

# Precision en números float

x = 3.3
print(x)
y = 1.1 + 2.2 # resultado -> 3.3000000000000003
print(y)

print(x == y) # Retorna un False

# ¿Entonces como podriamos comparar flotantes?

# Forma con strings
# Transformar a y a un formato str y cortarle esos valores

y_str = format(y, ".2g") # usamos la funcion format pasarle el valor en este caso y, y decirle que solo tenga 2 digitos
print('str =>', y_str)

# ahora convertimos el int y a un string , y lo comparamos

print(y_str == str(y))

print("*" * 30)

# Forma matematica

tolerance = 0.00001
print(abs(x - y) < tolerance)
print(abs(x - y))


