"""
    Escribir un código que permita calcular un descuento basado en las siguientes reglas o consideraciones:

    - Más de 10 años de experiencia, 5% de descuento.
    - Más de 20 años de experiencia, 17% de descuento.
    - Si es más de 25 años de experiencia y varón, 20% de descuento.
    - Si es más de 25 años de experiencia y mujer, 23% de descuento.
"""



while True:

    años_exp = int(input("Ingrese sus años de experiencia:\n"))
    sexo = input("Escriba su sexo: (mujer o varon):\n")

    if not sexo.lower() in ("mujer", "varon"):
        print("Escoge una de las opciones validas.")
        continue

    if años_exp > 10 and años_exp <= 20:
        print("Usted recibe 5% de descuento.")
    elif años_exp > 20 and años_exp <= 25:
        print("Usted recibira, 17% de descuento.")
    elif años_exp > 25 and sexo == "varon":
        print("Usted recibe un 20% de descuento.")
    elif años_exp > 25 and sexo == "mujer":
        print("Usted rescibe un 23% de descuento")
    else:
        print("Usted no recibe nada.")
    break;