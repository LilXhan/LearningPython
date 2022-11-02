"""
    Funciones

    Las funciones son muy importante dentro de cualquier lenguaje de pogramacion, 
    normalmente dentro de nuestros pogramas nosotros tenemos grandes bloques de codigo que basicamente
    nos toca ejecutarlos multiples veces, en vez de volver a reescribir ese codigo multiples veces lo
    que hacemos es encerrar esa bloque de codigo en algo llamado funciones. Y esas funciones luego
    las podemos usar varias veces desde diferentes puntos y con eso logramos gran reutilizacion del codigo
    y a largo tiempo ganar mantenibilidad.
"""

# la funcion mas basica es la funcion print, la funcion print recibe un argumento -> print(argumento)

print('hola')

# Hacemos nuestra primera funcion de impresion -> def my_function(parametro)

def my_print(text):
    print(text * 2)
    
# Llamar una funcion -> my_function(argumento)

my_print("Este es mi texto") # -> Este es mi textoEste es mi texto
my_print("Hola") # -> HolaHola

# Otro ejemplo

a = 10
b = 90

c = a + b

# Hacerlo en una funcion

def suma(a, b):
    print(a + b)

suma(10, 90) # -> 100
suma(1, 5) # -> 6

# Podemos utilizar una funcion dentro de otra funcion, una funcion dentro de otra:

def suma_v2(a, b):
    my_print(a + b)

suma_v2(10, 90) # -> 200
suma_v2(100, 500) # -> 1200