# Un ciclo dentro de otro ciclo


matriz = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]

# Posiciones dentro de una lista que esta dentro de otra lista

print(matriz[0][2])

for row in matriz:
    for column in row:
        print(column)