"""
    Plantear 2 formas de encontrar los números comunes entre 2 listas sin usar set.
"""

l1 = [1, 2, 3, 4, "hola"]
l2 = [3, 4, 5, "hola", 6]

# 1era forma

list_repated = [i for i in l1 if i in l2]
print(list_repated)

# 2da forma

list_repated_v2 = list(filter(lambda x: x in l2, l1))
print(list_repated_v2)