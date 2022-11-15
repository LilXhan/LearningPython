
while True:
    try:
        num_usr = int(input("Ingrese un número:\n"))
        break
    except:
        print("Ingrese un número valido")


def value_double(num: int) -> str:
    return str(num * 2)

result: str = value_double(num_usr)

print(result)
