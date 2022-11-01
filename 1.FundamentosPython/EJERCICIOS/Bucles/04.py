"""
    Escribir un programa que reciba por teclado los tres lados(cm) de un
    triángulo ingresados por el usuario y compruebe si es un triángulo equilátero, isósceles o escaleno.

    Un triángulo es equilátero si tiene los tres lados iguales.
    Un triángulo es escaleno si tiene los tres lados desiguales.
    Un triángulo es isósceles si tiene al menos dos lados iguales.
"""



side_first = int(input(f"Input the first side:\n"))
side_second = int(input("Input the second side:\n"))
side_third = int(input("Input the third side:\n"))

if side_first == side_second and side_second == side_third:
    print("It's a equilateral triangle.")
elif side_first == side_second or side_second == side_third or side_first == side_third:
    print("It's a isosceles triangle.")
else:
    print("It's a scalene triangle.")

