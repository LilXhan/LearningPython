"""
    Encontrar todos los números comprendidos entre 7 y 537 que contengan el dígito 7
"""

only_seven = [i for i in range(7, 537) if str(i).count("7")]
print(only_seven)