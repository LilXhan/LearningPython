"""
    Dada la siguiente lista ["Hola", "Amigos", "Hoy", True] , escriba
    un programa que pida al usuario una palabra, dicha palabra debe ser agregada al final y al inicio de la lista.
"""

list = ["Hola", "Amigos", "Hoy", True]

word = input("Enter a word:\n")

list.append(word)
list.insert(0, word)

print(list)

