# Operadores de comparacion son muy utiles para cierto flujos de trabajo en python

# > mayor que, retorna True o False
print(10 > 3) # retorna un True
print(3 > 7) # retorna un False
print(7 > 7) # retorna un False

# < menor que
print(5 < 6) # retorna un True
print(6 < 5) # retorna un False
print(5 < 5) # retorna un False

# >= mayor o igual, para casos donde tenemos el mismo valor

print(2 >= 1) # retorna un True
print(2 >= 3) # retorna un False
print(2 >= 2) # retorna un True

# <= menor o igual

print(1 <= 2) # retorna un True
print(2 <= 1) # retorna un False
print(2 <= 2) # retorna un True

# == igualdad

print(6 == 6) # retorna un True
print(5 == 2) # retorna un False

# != distinto que

print(6 != 10) # retorna un True
print(6 != 6) # retorna un False

# CON STRINGS

print("Apple" == 'Apple')  # retorna un True, no hay diferencia de crearlo con comilla doble o sencilla
print("Apple" == 'apple')  # retorna un False, puede ser la misma palabra pero cuando uno tiene mayuscula y el otro no
                           # segun python no son iguales

print("1" == 1) # retorna un False, por que son tipo de datos diferentes, puede que tenga el mismo valor, pero uno es 
                # de tipo string y el otro un int

age = 18
print(age >= 18) # retorna un True, que si es mayor de edad

age = 15
print(age >= 18) # retorna un False, osea que es menor de edad
