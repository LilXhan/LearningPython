"""
    Una empresa ha decidido dar una bonificación del 5% al empleado cuyo
    tiempo de servicio sea superior a 3 años.

    Escribir un programa que reciba por teclado el monto del salario y los años
    de servicio e imprima la cantidad neta de la bonificación.
"""

salary = int(input("Enter salary:\n"))
years_service = int(input("Enter the years of service:\n"))


if salary <= 3:
    print("You do not receive a bonus, your salary remains the same")
else:
    bonus = salary + (salary * (5/100))
    print(f"You receive a bonus, your new salary is {bonus} dollars.")