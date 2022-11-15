

word_usr: str = input("Ingrese una palabra:\n")

def list_str(string: str) -> list:
    list_str = []
    count = 0
    for letter in string:
        list_str.append(letter)
        list_str.append(letter)
    
    return list_str

result: list = list_str(word_usr)
print(result)