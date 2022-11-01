""" 
    Dada la matriz, [[1,2,3],[4,5,6],[7,8,9]], calcule el promedio de la diagonal
    principal. Hint: Los 3 elementos de la diagonal son 1,5,9
"""

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

diagonal = [matriz[0][0], matriz[1][1], matriz[2][2]]

promedio = sum(diagonal) / len(diagonal)

print(f"El promedio de la diagonal es: {promedio}")