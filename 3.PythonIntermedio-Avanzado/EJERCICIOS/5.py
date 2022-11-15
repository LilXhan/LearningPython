def deco1(funcParametro):

    def decorando(n):
        print("Hola, estoy decorando esta funcion")
        funcParametro(n)
        print("Termine de decorar")
    
    return decorando


@deco1
def mostrar(n):
    print("Ingresaste el número", n)

mostrar(30)

