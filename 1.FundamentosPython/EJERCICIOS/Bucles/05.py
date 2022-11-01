"""
    Escriba un programa que reciba un número n ingresado por teclado por el usuario e 
    imprima la tabla de multiplicar de n desde 1 hasta 100.
"""

def table_mul(n: int) -> str:
    for i in range(1, 101):
        print(f"{i} x {n} = {i * n}")

num = int(input("Enter a number:\n"))

table_mul(num)