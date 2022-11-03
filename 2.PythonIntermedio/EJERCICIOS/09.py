"""
    Escribir una función elimina_duplicados que reciba como parámetro una lista L y 
    retorne una nueva lista sin los elementos duplicados. Si el argumento es 
    [500,100,200,300,200,100,600,400,800,400,500,900] la función devuelve 
    [500, 100, 200, 300, 600, 400, 800, 900]

    Plantee 2 formas de solución
"""

# 1era forma

lista_2 = [500,100,200,300,200,100,600,400,800,400,500,900]
lista_2 = set(lista_2)
lista_2 = list(lista_2)
print(lista_2)

# 2da forma

def elimina_duplicados(l):
    new_list = []
    for x in l:
        if not x in new_list:
            new_list.append(x)
    return new_list

lista_2 = [500,100,200,300,200,100,600,400,800,400,500,900]

print(elimina_duplicados(lista_2))