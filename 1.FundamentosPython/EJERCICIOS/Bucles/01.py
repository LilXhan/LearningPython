"""
    Escribir un programa que reciba por teclado dos números y un operador matemático(+,-,*,/). 
    Realice la operación correspondiente e imprima el resultado.
    En caso el operador sea distinto a los mencionados imprimir "Operador no aceptado"
"""

import operator

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

while True:
    number_1 = int(input("Ingrese el primer número:\n"))
    number_2 = int(input("Ingrese el segundo número:\n"))

    operacion = input("Ingrese el operador de la operacion que desea realizar:\n"
                      "Suma -> +\n"
                      "Resta -> -\n"
                      "Multiplicacion -> *\n"
                      "Division -> /\n")
    
    if not operacion in operators.keys():
        print("Operador no aceptado.")
        break;

    for op, operation in operators.items():
        if op == operacion:
            print(f"El resultado de tu operacion es: {operation(number_1, number_2)}")
            break;
    break;