"""
    Escribir un programa que reciba por teclado dos cadenas ingresadas por el usuario, luego el 
    programa deberá crear una nueva cadena formada por las dos cadenas dadas, estas
    deben estar separadas por un espacio y sin vocales.

    Ejemplo: si las cadenas son "cincuenta" y "sesenta" entonces la nueva cadena deverá ser "cncnt ssnt".
"""

str_first = input("Input the first string:\n")
str_second = input("Input the second string:\n")

str_all= ""

vowels = ['a', 'e', 'i', 'o', 'u']

for x in str_first:
    if not x.lower() in vowels:
        str_all += x

str_all += " "

for x in str_second:
    if not x.lower() in vowels:
        str_all += x

print(str_all)